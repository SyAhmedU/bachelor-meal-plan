import re

with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'r', encoding='utf-8') as f:
    content = f.read()

NEW = r"""
{id:'bs9',type:'breakfast',effort:'simple',time:15,protein:10,calories:250,emoji:'🍚',
name:'Idli + Quick Sambar',nameTA:'இட்லி சாம்பார்',nameUR:'اڈلی سمبر',
equipment:['smart pot'],nightPrep:false,
ingredients:[
  {emoji:'🍚',name:'Ready-made idli batter',nameTA:'இட்லி மாவு',nameUR:'اڈلی بیٹر',qty:250,unit:'ml'},
  {emoji:'🫙',name:'MTR/Aachi instant sambar mix',nameTA:'சாம்பார் பொடி',nameUR:'سمبر مکس',qty:1,unit:'sachet'},
  {emoji:'🛢️',name:'Sunflower oil (for greasing)',nameTA:'எண்ணெய்',nameUR:'تیل',qty:0.5,unit:'tsp'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.25,unit:'tsp'},
],
steps:[
  {text:'Add 1.5 cups water to Smart Pot inner pot. Grease a small steel tiffin/bowl with oil. Pour batter in (fills 4 idli portions).',timer:0},
  {text:'Place greased bowl on a trivet inside Smart Pot. Close lid. Press **Steam** → adjust to 12 min using Min▲ → press **Start**.',timer:720},
  {text:'While steaming: pour sambar sachet + 200ml water into AGARO kettle. Knob → **II (High)**. Let boil 3 min. Knob → **I (Low)**.',timer:180},
  {text:'Quick release Smart Pot. Dip spoon in water and scoop out idlis. Serve 4 idlis with hot sambar.',timer:0},
],
tip:'ID Fresh or Sakthi idli batter is at any Chennai supermarket. MTR ready sambar sachet is ₹10. Batter at room temp gives fluffier idli than cold batter.',
video:'idli in electric pressure cooker steam',
},

{id:'bs10',type:'breakfast',effort:'simple',time:12,protein:7,calories:210,emoji:'🌾',
name:'Plain Poha (Aval Upma)',nameTA:'அவல் உப்மா',nameUR:'پوہا اوپما',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🌾',name:'Poha (flattened rice)',nameTA:'அவல்',nameUR:'پوہا',qty:1,unit:'cup'},
  {emoji:'🧅',name:'Onion',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'medium'},
  {emoji:'🌶️',name:'Green chili',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🌰',name:'Roasted peanuts',nameTA:'வேர்க்கடலை',nameUR:'مونگ پھلی',qty:2,unit:'tbsp'},
  {emoji:'🟡',name:'Turmeric',nameTA:'மஞ்சள்',nameUR:'ہلدی',qty:0.25,unit:'tsp'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.5,unit:'tsp'},
  {emoji:'🍋',name:'Lemon juice',nameTA:'எலுமிச்சை',nameUR:'لیموں',qty:1,unit:'tsp'},
],
steps:[
  {text:'Rinse poha in a strainer under running water 2–3 times. Squeeze gently. Add salt + turmeric. Rest 5 min to soften.',timer:300},
  {text:'Heat flat pan on V-Guard 1200W. Add 1 tsp oil. Add peanuts, stir 20 sec. Add sliced onion + green chili.',timer:20},
  {text:'Sauté onion 2 min on 1200W until soft. Add softened poha. Mix gently. Reduce to 800W. Cook 1 min.',timer:120},
  {text:'Squeeze lemon juice. Toss once. Serve hot. Pairs well with chai.',timer:0},
],
tip:'Different from Egg Poha — this vegetarian version is lighter. If poha is too dry, sprinkle 2 tbsp water while mixing. Add grated coconut on top for a Chennai touch.',
video:'poha recipe south indian style aval upma',
},

{id:'bs11',type:'breakfast',effort:'simple',time:5,protein:13,calories:330,emoji:'🍌',
name:'Banana Peanut Butter Toast',nameTA:'வாழை வேர்க்கடலை டோஸ்ட்',nameUR:'کیلا مونگ پھلی ٹوسٹ',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🥜',name:'Peanut butter',nameTA:'வேர்க்கடலை வெண்ணெய்',nameUR:'مونگ پھلی مکھن',qty:2,unit:'tbsp'},
  {emoji:'🍌',name:'Banana',nameTA:'வாழைப்பழம்',nameUR:'کیلا',qty:1,unit:'nos'},
  {emoji:'🍯',name:'Honey',nameTA:'தேன்',nameUR:'شہد',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Spread 1 tbsp peanut butter on each bread slice.',timer:0},
  {text:'Slice banana into rounds. Layer over peanut butter.',timer:0},
  {text:'Drizzle honey. Eat immediately. Pair with a glass of milk or chai.',timer:0},
],
tip:'No cooking needed — fastest protein breakfast. Natural peanut butter (just peanuts, no sugar) gives more protein. Add a pinch of cinnamon for flavour. Works as pre-gym fuel.',
video:'peanut butter banana toast quick breakfast',
},

{id:'bs12',type:'breakfast',effort:'simple',time:5,protein:9,calories:280,emoji:'🥣',
name:'Cornflakes Milk Bowl',nameTA:'கார்ன்ஃபிளேக்ஸ் பால் கிண்ணம்',nameUR:'کارن فلیکس دودھ باؤل',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🌾',name:'Cornflakes (Kellogg\'s)',nameTA:'கார்ன்ஃபிளேக்ஸ்',nameUR:'کارن فلیکس',qty:1,unit:'cup'},
  {emoji:'🥛',name:'Full-fat milk',nameTA:'பால்',nameUR:'دودھ',qty:200,unit:'ml'},
  {emoji:'🍌',name:'Banana (sliced)',nameTA:'வாழைப்பழம்',nameUR:'کیلا',qty:0.5,unit:'nos'},
  {emoji:'🍯',name:'Honey or sugar',nameTA:'தேன்',nameUR:'شہد',qty:1,unit:'tsp'},
],
steps:[
  {text:'Pour milk into AGARO kettle. Knob → **II (High)**. Heat 3–4 min until hot (steam rises, bubbles at edges). Knob → **Off**.',timer:240},
  {text:'Pour cornflakes in bowl. Pour warm milk over. Add banana slices + honey. Eat right away before it gets soggy.',timer:0},
],
tip:'Cold milk version: skip heating, pour straight from fridge. Add 4–5 dates or a handful of raisins for extra iron. Kellogg\'s cornflakes available at Nilgiris, D-Mart.',
video:'cornflakes milk breakfast quick easy',
},

{id:'bs13',type:'breakfast',effort:'simple',time:5,protein:8,calories:180,emoji:'🍶',
name:'Curd Fruit Bowl',nameTA:'தயிர் பழ கிண்ணம்',nameUR:'دہی پھل باؤل',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🍶',name:'Fresh curd',nameTA:'தயிர்',nameUR:'دہی',qty:200,unit:'ml'},
  {emoji:'🍌',name:'Banana',nameTA:'வாழைப்பழம்',nameUR:'کیلا',qty:1,unit:'nos'},
  {emoji:'🍇',name:'Grapes or pomegranate',nameTA:'திராட்சை',nameUR:'انگور',qty:10,unit:'nos'},
  {emoji:'🍯',name:'Honey',nameTA:'தேன்',nameUR:'شہد',qty:1,unit:'tsp'},
  {emoji:'🌰',name:'Mixed nuts (crushed)',nameTA:'கலந்த கொட்டை',nameUR:'مکس گری',qty:1,unit:'tbsp'},
],
steps:[
  {text:'Spoon curd into bowl. Beat smooth.',timer:0},
  {text:'Slice banana. Add banana + grapes (or papaya, apple, pomegranate — whatever is seasonal).',timer:0},
  {text:'Drizzle honey. Scatter crushed nuts. Eat immediately.',timer:0},
],
tip:'Aavin curd (₹30/200g) is the best in Chennai. Buy fresh daily from supermarket or local shop. Pomegranate adds iron + crunch. Works as post-workout recovery too.',
video:'curd fruit bowl healthy breakfast',
},

{id:'bs14',type:'breakfast',effort:'simple',time:7,protein:11,calories:270,emoji:'🥛',
name:'Dates + Nuts + Warm Milk',nameTA:'பேரீச்சம்பழம் கொட்டை பால்',nameUR:'کھجور گری دودھ',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🥛',name:'Full-fat milk',nameTA:'பால்',nameUR:'دودھ',qty:300,unit:'ml'},
  {emoji:'🫘',name:'Dates (Ajwa or Medjool)',nameTA:'பேரீச்சம்பழம்',nameUR:'کھجور',qty:5,unit:'nos'},
  {emoji:'🌰',name:'Almonds',nameTA:'பாதாம்',nameUR:'بادام',qty:6,unit:'nos'},
  {emoji:'🥜',name:'Cashews',nameTA:'முந்திரி',nameUR:'کاجو',qty:4,unit:'nos'},
  {emoji:'🌿',name:'Cardamom powder',nameTA:'ஏலக்காய்',nameUR:'الائچی',qty:1,unit:'pinch'},
],
steps:[
  {text:'Pour milk into AGARO kettle. Knob → **II (High)**. Heat 4 min until hot and steaming.',timer:240},
  {text:'Meanwhile pit + chop dates. Roughly crush almonds + cashews.',timer:0},
  {text:'Pour hot milk into large glass. Add dates + nuts + cardamom pinch. Stir. Drink hot.',timer:0},
],
tip:'Soak almonds overnight in water and peel in morning — easier to digest. Traditional morning drink for energy before salah/gym. High in iron, calcium, and healthy fat.',
video:'dates almonds milk morning drink desi',
},

{id:'bs15',type:'breakfast',effort:'simple',time:10,protein:15,calories:350,emoji:'🍜',
name:'Masala Maggi + Egg',nameTA:'மசாலா மேகி முட்டை',nameUR:'مسالا میگی انڈا',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🍜',name:'Maggi noodles (1 pack)',nameTA:'மேகி நூடுல்ஸ்',nameUR:'میگی نوڈلز',qty:1,unit:'pack'},
  {emoji:'🥚',name:'Egg',nameTA:'முட்டை',nameUR:'انڈا',qty:1,unit:'nos'},
  {emoji:'🧅',name:'Small onion (diced)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:1,unit:'small'},
  {emoji:'🌶️',name:'Green chili (sliced)',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🫙',name:'Maggi masala tastemaker',nameTA:'மசாலா',nameUR:'مسالا',qty:1,unit:'sachet'},
],
steps:[
  {text:'Fill AGARO kettle with 350ml water. Knob → **II (High)**. Bring to full boil (5 min).',timer:300},
  {text:'Add broken Maggi noodles + tastemaker sachet + onion + green chili to boiling water. Knob → **I (Low)**. Cook 2 min, stirring occasionally.',timer:120},
  {text:'Crack egg into kettle. Stir immediately to scramble it into the noodles. Wait 1 min. Knob → **Off**.',timer:60},
  {text:'Pour into bowl. Eat hot. Squeeze lemon if available.',timer:0},
],
tip:'Maggi is ₹14/pack at any Chennai kirana. Do not overcook — remove while noodles are slightly firm. Add grated carrot or peas for nutrition. Excellent quick post-gym breakfast.',
video:'maggi noodles egg kettle recipe easy',
},

{id:'bs16',type:'breakfast',effort:'simple',time:8,protein:14,calories:270,emoji:'🥚',
name:'Hard Boiled Eggs + Buttered Bread',nameTA:'வேகவைத்த முட்டை வெண்ணெய் பிரட்',nameUR:'ابلا انڈا مکھن روٹی',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🥚',name:'Eggs',nameTA:'முட்டை',nameUR:'انڈا',qty:2,unit:'nos'},
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🧈',name:'Butter',nameTA:'வெண்ணெய்',nameUR:'مکھن',qty:1,unit:'tsp'},
  {emoji:'🧂',name:'Salt + black pepper',nameTA:'உப்பு மிளகு',nameUR:'نمک کالی مرچ',qty:0.5,unit:'tsp each'},
],
steps:[
  {text:'Place 2 eggs in AGARO kettle. Cover with cold water (water level just above eggs). Knob → **II (High)**.',timer:0},
  {text:'Boil: soft-boiled = 6 min, hard-boiled = 10 min from when bubbling starts. Knob → **Off**.',timer:600},
  {text:'Transfer eggs to cold water 1 min. Peel. Slice in half. Season with salt + pepper.',timer:60},
  {text:'Spread butter on bread. Serve eggs on side. Eat together.',timer:0},
],
tip:'Fastest protein breakfast — no pan needed. For egg salad variation: mash eggs with butter + salt + pepper, spread on bread. Two eggs give 12g protein before anything else.',
video:'hard boiled eggs in kettle easy method',
},

"""

marker = '];\n\nwindow.__PANTRY__'
pos = content.find(marker)
if pos == -1:
    print('ERROR: marker not found')
else:
    content = content[:pos] + NEW + content[pos:]
    with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Batch 1 done — breakfast simple bs9-bs16 inserted')
