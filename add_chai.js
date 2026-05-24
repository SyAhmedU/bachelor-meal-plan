const fs = require('fs');
let content = fs.readFileSync('meals.js', 'utf8');

const CHAI_ING = `    {emoji:'🫙',name:'Tea leaves',nameTA:'தேயிலை',nameUR:'چائے پتی',qty:1,unit:'tsp'},
    {emoji:'🥛',name:'Full-fat milk',nameTA:'பால்',nameUR:'دودھ',qty:100,unit:'ml'},
    {emoji:'🍚',name:'Sugar',nameTA:'சர்க்கரை',nameUR:'چینی',qty:1,unit:'tsp'},`;

const CHAI_STEP = `    {text:'Make strong chai: pour 100ml milk + 150ml water into vessel on induction. Add 1 tsp tea leaves. Bring to boil, add 1 tsp sugar, strain into cup.',timer:120},`;

function modifyRecipe(c, id, options) {
  const { addIngredients = true, addStep = true, rename = null, addVessel = false } = options;

  const idStr = `id:'${id}'`;
  const idx = c.indexOf(idStr);
  if (idx === -1) { console.error('NOT FOUND:', id); return c; }

  // Find opening { of this recipe (scan back from id: position)
  let start = idx;
  while (start > 0 && c[start] !== '{') start--;

  // Find recipe end via video: field (always last property before },)
  const videoIdx = c.indexOf('\n  video:', idx);
  if (videoIdx === -1) { console.error('No video field for:', id); return c; }
  const recipeEnd = c.indexOf('\n},', videoIdx);
  if (recipeEnd === -1) { console.error('No recipe end for:', id); return c; }

  let block = c.slice(start, recipeEnd + 3);
  const prefix = c.slice(0, start);
  const suffix = c.slice(recipeEnd + 3);

  // Add vessel to equipment if needed (single-line equipment array)
  if (addVessel && !block.includes("'vessel'")) {
    block = block.replace(/equipment:\[([^\]]*)\]/, (_m, items) => {
      return !items.trim() ? `equipment:['vessel']` : `equipment:[${items.trimEnd()},'vessel']`;
    });
  }

  // Detect line ending used in this block
  const LE = block.includes('\r\n') ? '\r\n' : '\n';

  // Add chai ingredients (before ingredients close)
  if (addIngredients && !block.includes("name:'Tea leaves'")) {
    const ING_CLOSE = `${LE}  ],${LE}  steps:`;
    const pos = block.indexOf(ING_CLOSE);
    if (pos === -1) { console.error('No ingredients close in:', id); }
    else {
      const chaiIngLE = CHAI_ING.replace(/\n/g, LE);
      block = block.slice(0, pos) + LE + chaiIngLE + ING_CLOSE + block.slice(pos + ING_CLOSE.length);
      console.log(`  ${id}: chai ingredients added`);
    }
  } else if (addIngredients) {
    console.log(`  ${id}: already has Tea leaves, skipped`);
  }

  // Add chai step (before steps close)
  const alreadyHasChai = block.includes('Make strong chai')
    || block.includes('Make chai in vessel')
    || block.includes('Make chai:')
    || block.includes('chai separately in second vessel')
    || block.includes('for chai.');
  if (addStep && !alreadyHasChai) {
    const STEP_CLOSE = `${LE}  ],${LE}  tip:`;
    const pos = block.indexOf(STEP_CLOSE);
    if (pos === -1) { console.error('No steps close in:', id); }
    else {
      const chaiStepLE = CHAI_STEP.replace(/\n/g, LE);
      block = block.slice(0, pos) + LE + chaiStepLE + STEP_CLOSE + block.slice(pos + STEP_CLOSE.length);
      console.log(`  ${id}: chai step added`);
    }
  } else if (addStep) {
    console.log(`  ${id}: already has chai step, skipped`);
  }

  // Rename
  if (rename) {
    const [on, nn, ota, nta, our, nur] = rename;
    if (block.includes(`name:'${on}'`)) {
      block = block.replace(`name:'${on}'`, `name:'${nn}'`);
      block = block.replace(`nameTA:'${ota}'`, `nameTA:'${nta}'`);
      block = block.replace(`nameUR:'${our}'`, `nameUR:'${nur}'`);
      console.log(`  ${id}: renamed`);
    } else {
      console.log(`  ${id}: name not found for rename — skipped`);
    }
  }

  return prefix + block + suffix;
}

// ── INGREDIENTS ONLY (name/step already mentions chai) ────────────────────────
console.log('\n=== INGREDIENTS ONLY ===');
content = modifyRecipe(content, 'bm3', { addStep: false });
content = modifyRecipe(content, 'bh2', { addStep: false });
content = modifyRecipe(content, 'bs6', { addStep: false });

// ── BREAKFAST FULL TREATMENT ──────────────────────────────────────────────────
console.log('\n=== BREAKFAST FULL ===');
content = modifyRecipe(content, 'bs3', {
  addVessel: true,
  rename: ['Banana Smoothie + Boiled Eggs','Banana Smoothie + Boiled Eggs + Chai',
           'வாழைப்பழம் ஸ்மூதி + வேகவைத்த முட்டை','வாழைப்பழம் ஸ்மூதி + வேகவைத்த முட்டை + சாய்',
           'کیلے کی اسموتھی + ابلے انڈے','کیلے کی اسموتھی + ابلے انڈے + چائے'],
});
content = modifyRecipe(content, 'bs4', {
  addVessel: true,
  rename: ['Leftover Roti + Egg Bhurji','Leftover Roti + Egg Bhurji + Chai',
           'மீதமான ரொட்டி + முட்டை புர்ஜி','மீதமான ரொட்டி + முட்டை புர்ஜி + சாய்',
           'بچی ہوئی روٹی + انڈا بھرجی','بچی ہوئی روٹی + انڈا بھرجی + چائے'],
});
content = modifyRecipe(content, 'bs5', {
  addVessel: true,
  rename: ['Cold Roti + Curd + Pickle','Cold Roti + Curd + Pickle + Chai',
           'ரொட்டி + தயிர் + ஊறுகாய்','ரொட்டி + தயிர் + ஊறுகாய் + சாய்',
           'روٹی + دہی + اچار','روٹی + دہی + اچار + چائے'],
});
content = modifyRecipe(content, 'bm1', {
  addVessel: true,
  rename: ['Egg Dosa + Coconut Chutney','Egg Dosa + Coconut Chutney + Chai',
           'முட்டை தோசை + தேங்காய் சட்னி','முட்டை தோசை + தேங்காய் சட்னி + சாய்',
           'انڈے کا ڈوسا + ناریل کی چٹنی','انڈے کا ڈوسا + ناریل کی چٹنی + چائے'],
});
content = modifyRecipe(content, 'bm4', {
  addVessel: true,
  rename: ['Fresh Wheat Roti + Moong Dal','Fresh Wheat Roti + Moong Dal + Chai',
           'கோதுமை ரொட்டி + பாசிப்பருப்பு','கோதுமை ரொட்டி + பாசிப்பருப்பு + சாய்',
           'گندم کی روٹی + موں دال','گندم کی روٹی + موں دال + چائے'],
});
content = modifyRecipe(content, 'bm5', {
  rename: ['Fresh Roti + Paneer Bhurji','Fresh Roti + Paneer Bhurji + Chai',
           'ரொட்டி + பன்னீர் புர்ஜி','ரொட்டி + பன்னீர் புர்ஜி + சாய்',
           'روٹی + پنیر بھرجی','روٹی + پنیر بھرجی + چائے'],
});
content = modifyRecipe(content, 'bm6', {
  addVessel: true,
  rename: ['Baida Roti (Hyderabadi Egg Paratha)','Baida Roti (Hyderabadi Egg Paratha) + Chai',
           'பைதா ரோட்டி (முட்டை பராத்தா)','பைதா ரோட்டி (முட்டை பராத்தா) + சாய்',
           'بیضہ روٹی (حیدرآبادی انڈہ پراٹھا)','بیضہ روٹی (حیدرآبادی انڈہ پراٹھا) + چائے'],
});
content = modifyRecipe(content, 'bm7', {
  rename: ['Sheer Khurma (Festival Vermicelli Milk)','Sheer Khurma (Festival Vermicelli Milk) + Chai',
           'சீர் குர்மா (பண்டிகை பால் சேமியா)','சீர் குர்மா (பண்டிகை பால் சேமியா) + சாய்',
           'شیر خُرما','شیر خُرما + چائے'],
});
content = modifyRecipe(content, 'bm8', {
  rename: ['Egg Bhurji + Bread (Desi Scrambled Eggs)','Egg Bhurji + Bread (Desi Scrambled Eggs) + Chai',
           'முட்டை புர்ஜி + பிரட்','முட்டை புர்ஜி + பிரட் + சாய்',
           'انڈہ بھرجی + بریڈ','انڈہ بھرجی + بریڈ + چائے'],
});
content = modifyRecipe(content, 'bm9', {
  addVessel: true,
  rename: ['Aloo Paratha (Potato Stuffed Flatbread)','Aloo Paratha (Potato Stuffed Flatbread) + Chai',
           'ஆலு பராத்தா (உருளை கிழங்கு பராத்தா)','ஆலு பராத்தா (உருளை கிழங்கு பராத்தா) + சாய்',
           'آلو پراٹھا','آلو پراٹھا + چائے'],
});
content = modifyRecipe(content, 'bh1', {
  rename: ['Egg Paratha + Curd','Egg Paratha + Curd + Chai',
           'முட்டை பராத்தா + தயிர்','முட்டை பராத்தா + தயிர் + சாய்',
           'انڈا پراٹھا + دہی','انڈا پراٹھا + دہی + چائے'],
});
content = modifyRecipe(content, 'bh3', {
  addVessel: true,
  rename: ['Dosa with Egg & Onion Filling + Sambar','Dosa with Egg & Onion Filling + Sambar + Chai',
           'முட்டை மசாலா தோசை + சாம்பார்','முட்டை மசாலா தோசை + சாம்பார் + சாய்',
           'انڈے والا ڈوسا + سامبار','انڈے والا ڈوسا + سامبار + چائے'],
});
content = modifyRecipe(content, 'bh4', {
  addVessel: true,
  rename: ['Aloo Paratha + Curd','Aloo Paratha + Curd + Chai',
           'உருளைக்கிழங்கு பராட்டா + தயிர்','உருளைக்கிழங்கு பராட்டா + தயிர் + சாய்',
           'آلو پراٹھا + دہی','آلو پراٹھا + دہی + چائے'],
});
content = modifyRecipe(content, 'bh5', {
  addVessel: true,
  rename: ['Egg Kati Roll (Roti Wrap)','Egg Kati Roll (Roti Wrap) + Chai',
           'முட்டை ரோல் ரொட்டி','முட்டை ரோல் ரொட்டி + சாய்',
           'انڈا کاٹی رول','انڈا کاٹی رول + چائے'],
});
content = modifyRecipe(content, 'bh6', {
  addVessel: true,
  rename: ['Chicken Keema Paratha','Chicken Keema Paratha + Chai',
           'சிக்கன் கீமா பராத்தா','சிக்கன் கீமா பராத்தா + சாய்',
           'چکن قیمہ پراٹھا','چکن قیمہ پراٹھا + چائے'],
});
content = modifyRecipe(content, 'bh7', {
  addVessel: true,
  rename: ['Masala Omelette + Paratha (Full Protein Breakfast)','Masala Omelette + Paratha (Full Protein Breakfast) + Chai',
           'மசாலா ஆம்லெட் + பராத்தா','மசாலா ஆம்லெட் + பராத்தா + சாய்',
           'مصالہ آملیٹ + پراٹھا','مصالہ آملیٹ + پراٹھا + چائے'],
});
content = modifyRecipe(content, 'bs7', {
  rename: ['Savory Oats Upma','Savory Oats Upma + Chai',
           'ஓட்ஸ் உப்புமா','ஓட்ஸ் உப்புமா + சாய்',
           'نمکین اوٹس','نمکین اوٹس + چائے'],
});

// ── SNACK FULL TREATMENT ──────────────────────────────────────────────────────
console.log('\n=== SNACK FULL ===');
content = modifyRecipe(content, 'ss2', {
  addVessel: true,
  rename: ['Banana + Peanut Butter on Bread','Banana + Peanut Butter on Bread + Chai',
           'வாழைப்பழம் + வேர்க்கடலை வெண்ணெய் + பிரட்','வாழைப்பழம் + வேர்க்கடலை வெண்ணெய் + பிரட் + சாய்',
           'کیلا + مونگ پھلی مکھن + روٹی','کیلا + مونگ پھلی مکھن + روٹی + چائے'],
});
content = modifyRecipe(content, 'ss4', {
  rename: ['Mirchi Bajji (Chilli Fritters)','Mirchi Bajji (Chilli Fritters) + Chai',
           'மிளகாய் பஜ்ஜி','மிளகாய் பஜ்ஜி + சாய்',
           'مرچ بھجیا','مرچ بھجیا + چائے'],
});
content = modifyRecipe(content, 'sm2', {
  addVessel: true,
  rename: ['Egg Toast with Cheese (optional)','Egg Toast with Cheese + Chai',
           'முட்டை டோஸ்ட்','முட்டை டோஸ்ட் + சாய்',
           'انڈا ٹوسٹ','انڈا ٹوسٹ + چائے'],
});
content = modifyRecipe(content, 'sm3', {
  addVessel: true,
  rename: ['Banana Protein Smoothie','Banana Protein Smoothie + Chai',
           'வாழைப்பழம் புரோட்டின் ஷேக்','வாழைப்பழம் புரோட்டின் ஷேக் + சாய்',
           'کیلا پروٹین شیک','کیلا پروٹین شیک + چائے'],
});
content = modifyRecipe(content, 'sm4', {
  rename: ['Bread Samosa','Bread Samosa + Chai',
           'பிரட் சமோசா','பிரட் சமோசா + சாய்',
           'بریڈ سموسہ','بریڈ سموسہ + چائے'],
});
content = modifyRecipe(content, 'sh1', {
  addVessel: true,
  rename: ['Grilled Chicken Sandwich','Grilled Chicken Sandwich + Chai',
           'சிக்கன் சாண்ட்விச்','சிக்கன் சாண்ட்விச் + சாய்',
           'گرلڈ چکن سینڈوچ','گرلڈ چکن سینڈوچ + چائے'],
});
content = modifyRecipe(content, 'sh2', {
  rename: ['Bread Pakora','Bread Pakora + Chai',
           'பிரட் பஜ்ஜி','பிரட் பஜ்ஜி + சாய்',
           'بریڈ پکوڑا','بریڈ پکوڑا + چائے'],
});
content = modifyRecipe(content, 'sh3', {
  rename: ['Masala Boiled Eggs (Anda Chaat)','Masala Boiled Eggs (Anda Chaat) + Chai',
           'மசாலா முட்டை','மசாலா முட்டை + சாய்',
           'مسالہ انڈا چاٹ','مسالہ انڈا چاٹ + چائے'],
});
content = modifyRecipe(content, 'sh4', {
  rename: ['Chicken Cutlets','Chicken Cutlets + Chai',
           'சிக்கன் கட்லெட்','சிக்கன் கட்லெட் + சாய்',
           'چکن کٹلٹ','چکن کٹلٹ + چائے'],
});

fs.writeFileSync('meals.js', content, 'utf8');
console.log('\n✓ Done. meals.js updated.');
