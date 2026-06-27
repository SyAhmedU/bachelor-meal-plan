// Bachelor Meal Plan — "Invent something new" endpoint (Groq-backed).
// POST { ingredients: "tomato, onion, oil" }
//   -> { recipe: { emoji, name, time, effort, serves, ingredients:[{emoji,name,qty}], steps:[...], tip } }
// Companion to the offline matcher: this is the ONLY online feature; the rest of the app works offline.
import { guard } from "./_guard.js";

const PRIMARY = process.env.BMP_COOK_MODEL || "llama-3.3-70b-versatile";
const FALLBACK = "llama-3.1-8b-instant";
const GROQ_URL = "https://api.groq.com/openai/v1/chat/completions";

// Common kitchen staples a bachelor is assumed to have — the model may use these
// freely on top of the ingredients the user typed, but nothing else exotic.
const STAPLES =
  "salt, black pepper, cooking oil, water, sugar, common Indian spices (turmeric, chilli powder, " +
  "cumin, coriander powder, garam masala), green chilli, ginger-garlic paste";

const SYSTEM =
  "You are a practical home-cook assistant for a busy bachelor cooking in a small kitchen. " +
  "Invent ONE simple, realistic recipe using mainly the ingredients the user lists. " +
  "HARD RULES:\n" +
  "1. HALAL ONLY — never use pork, ham, bacon, lard, alcohol, wine, or any non-halal ingredient, even if listed.\n" +
  "2. Use ONLY the ingredients the user gives, plus these everyday staples they're assumed to have: " + STAPLES + ". " +
  "Do NOT invent exotic or specialty ingredients the user didn't mention.\n" +
  "3. Keep it bachelor-simple: few steps, basic equipment (one pan/pot), under ~30 minutes where possible.\n" +
  "4. Be honest. If the listed ingredients genuinely can't make a sensible dish, say so in the 'tip' and keep the recipe minimal — never fabricate to look impressive.\n" +
  "5. Quantities are approximate, written casually (e.g. '1 medium', 'a handful', '2 tbsp').\n\n" +
  "Respond with ONLY a JSON object of this exact shape:\n" +
  '{ "emoji": "<one food emoji>", "name": "<short dish name>", "time": <minutes as a number>, ' +
  '"effort": "easy" | "simple" | "involved", "serves": <number>, ' +
  '"ingredients": [ { "emoji": "<emoji>", "name": "<ingredient>", "qty": "<amount, e.g. 1 medium>" } ], ' +
  '"steps": [ "<step 1>", "<step 2>" ], "tip": "<one short practical tip>" }\n' +
  "No prose outside the JSON.";

export default async function handler(req, res) {
  // CORS — GitHub Pages calls this cross-origin.
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") { res.status(204).end(); return; }
  if (req.method !== "POST") { res.status(405).json({ error: "Use POST." }); return; }

  if (!process.env.GROQ_API_KEY) {
    res.status(503).json({ error: "The AI isn't switched on yet — the matches above still work offline." });
    return;
  }

  const blocked = guard(req, res);
  if (blocked) return;

  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch { body = {}; } }
  body = body || {};

  const ingredients = String(body.ingredients || "").trim();
  if (!ingredients) { res.status(400).json({ error: "Add a few ingredients first." }); return; }
  if (ingredients.length > 600) { res.status(413).json({ error: "That's a lot — list just the key ingredients." }); return; }

  const user = "Ingredients I have right now: " + ingredients;

  try {
    const data = await callGroq(PRIMARY, user).catch(() => callGroq(FALLBACK, user));
    const recipe = parse(data.content);
    if (!recipe) { res.status(502).json({ error: "Couldn't shape a recipe from that — try again or tweak the ingredients." }); return; }
    res.status(200).json({ recipe, model: data.model });
  } catch {
    res.status(502).json({ error: "Couldn't reach the AI right now. The matches above still work — try again in a moment." });
  }
}

async function callGroq(model, user) {
  const r = await fetch(GROQ_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: "Bearer " + process.env.GROQ_API_KEY },
    body: JSON.stringify({
      model,
      temperature: 0.7,
      max_tokens: 900,
      response_format: { type: "json_object" },
      messages: [{ role: "system", content: SYSTEM }, { role: "user", content: user }],
    }),
  });
  if (!r.ok) throw new Error("groq " + r.status);
  const j = await r.json();
  return { content: j.choices?.[0]?.message?.content || "", model };
}

function parse(raw) {
  let obj;
  try { obj = JSON.parse(raw); }
  catch {
    const m = raw.match(/\{[\s\S]*\}/);
    try { obj = JSON.parse(m ? m[0] : "{}"); } catch { return null; }
  }
  if (!obj || typeof obj !== "object") return null;

  const ings = Array.isArray(obj.ingredients)
    ? obj.ingredients
        .map(i => (typeof i === "string"
          ? { emoji: "", name: i.trim(), qty: "" }
          : { emoji: String(i.emoji || "").trim(), name: String(i.name || "").trim(), qty: String(i.qty ?? "").trim() }))
        .filter(i => i.name)
    : [];
  const steps = Array.isArray(obj.steps)
    ? obj.steps.map(s => (typeof s === "string" ? s : String(s.text || ""))).map(s => s.trim()).filter(Boolean)
    : [];

  const name = String(obj.name || "").trim();
  if (!name || !steps.length) return null;

  const time = Number(obj.time);
  const serves = Number(obj.serves);
  return {
    emoji: String(obj.emoji || "🍳").trim() || "🍳",
    name,
    time: Number.isFinite(time) && time > 0 ? Math.round(time) : null,
    effort: ["easy", "simple", "involved"].includes(String(obj.effort)) ? obj.effort : "simple",
    serves: Number.isFinite(serves) && serves > 0 ? Math.round(serves) : null,
    ingredients: ings,
    steps,
    tip: String(obj.tip || "").trim(),
  };
}
