with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'r', encoding='utf-8') as f:
    content = f.read()

NEW = r"""
{id:'ss7',type:'snack',effort:'simple',time:5,protein:2,calories:40,emoji:'🥛',
name:'Masala Buttermilk (Chaas)',nameTA:'மோர்',nameUR:'مسالا لسی',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🍶',name:'Curd',nameTA:'தயிர்',nameUR:'دہی',qty:100,unit:'ml'},
  {emoji:'💧',name:'Cold water',nameTA:'தண்ணீர்',nameUR:'پانی',qty:200,unit:'ml'},
  {emoji:'🌿',name:'Roasted cumin powder',nameTA:'சீரகப்பொடி',nameUR:'بھنا زیرہ',qty:0.25,unit:'tsp'},
  {emoji:'🧂',name:'Salt + black salt',nameTA:'உப்பு',nameUR:'نمک کالا نمک',qty:0.25,unit:'tsp each'},
  {emoji:'🌿',name:'Mint leaves (crushed)',nameTA:'புதினா',nameUR:'پدینہ',qty:3,unit:'leaves'},
],
steps:[
  {text:'Beat curd smooth. Add cold water + salt + black salt + cumin powder. Whisk vigorously or shake in bottle.',timer:0},
  {text:'Add crushed mint leaves. Pour over ice if available. Drink immediately.',timer:0},
],
tip:'Masala chaas is the perfect post-meal digestive and summer coolant in Chennai heat. Black salt is sold at spice shops (₹20 small pack). Better than any packaged drink — zero sugar, probiotic.',
video:'masala chaas buttermilk recipe easy',
},

{id:'ss8',type:'snack',effort:'simple',time:3,protein:2,calories:30,emoji:'🥒',
name:'Cucumber Chaat',nameTA:'வெள்ளரி சாட்',nameUR:'کھیرا چاٹ',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🥒',name:'Cucumber',nameTA:'வெள்ளரிக்காய்',nameUR:'کھیرا',qty:1,unit:'medium'},
  {emoji:'🍋',name:'Lemon juice',nameTA:'எலுமிச்சை',nameUR:'لیموں',qty:1,unit:'tsp'},
  {emoji:'🫙',name:'Chaat masala',nameTA:'சாட் மசாலா',nameUR:'چاٹ مسالا',qty:0.5,unit:'tsp'},
  {emoji:'🔴',name:'Chili powder',nameTA:'மிளகாய் பொடி',nameUR:'لال مرچ',qty:1,unit:'pinch'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:1,unit:'pinch'},
],
steps:[
  {text:'Peel and slice cucumber into sticks or rounds.',timer:0},
  {text:'Sprinkle chaat masala + chili powder + salt. Squeeze lemon. Toss and eat.',timer:0},
],
tip:'Cheapest snack in Chennai — cucumber is ₹10–15/piece. Extremely hydrating (96% water). Chaat masala is the key — transforms plain cucumber into something craveable. Zero calories, high satisfaction.',
video:'cucumber chaat recipe simple healthy snack',
},

{id:'ss9',type:'snack',effort:'simple',time:2,protein:4,calories:180,emoji:'🫘',
name:'Dates + Mixed Nuts',nameTA:'பேரீச்சம்பழம் கொட்டைகள்',nameUR:'کھجور مکس گری',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🫘',name:'Dates (Ajwa or Medjool)',nameTA:'பேரீச்சம்பழம்',nameUR:'کھجور',qty:4,unit:'nos'},
  {emoji:'🌰',name:'Almonds',nameTA:'பாதாம்',nameUR:'بادام',qty:6,unit:'nos'},
  {emoji:'🥜',name:'Cashews',nameTA:'முந்திரி',nameUR:'کاجو',qty:4,unit:'nos'},
  {emoji:'🌰',name:'Walnuts (optional)',nameTA:'அக்ரோட்',nameUR:'اخروٹ',qty:2,unit:'halves'},
],
steps:[
  {text:'Pit dates if needed. Arrange dates + nuts on a plate or in small container.',timer:0},
  {text:'Eat 1 date + 2–3 nuts at a time. Do not snack on nuts alone — combine with dates for balanced energy.',timer:0},
],
tip:'Dates + nuts is the original Muslim sunnah snack — high in iron, magnesium, and healthy fat. Buy Ajwa dates from Chennai dry fruit shops (Sowcarpet area). Keep a small box at your study desk.',
video:'dates nuts healthy snack Muslim',
},

{id:'ss10',type:'snack',effort:'simple',time:5,protein:5,calories:150,emoji:'🍎',
name:'Apple + Peanut Butter',nameTA:'ஆப்பிள் வேர்க்கடலை',nameUR:'سیب مونگ پھلی',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🍎',name:'Apple',nameTA:'ஆப்பிள்',nameUR:'سیب',qty:1,unit:'medium'},
  {emoji:'🥜',name:'Peanut butter',nameTA:'வேர்க்கடலை வெண்ணெய்',nameUR:'مونگ پھلی مکھن',qty:1.5,unit:'tbsp'},
],
steps:[
  {text:'Wash and slice apple into wedges. Remove core.',timer:0},
  {text:'Dip each apple slice into peanut butter and eat.',timer:0},
],
tip:'Classic protein + fiber combination. The crunch of apple + creaminess of peanut butter is satisfying. Simulated apple is available year-round in Chennai supermarkets. Natural PB has more protein than flavored brands.',
video:'apple peanut butter snack healthy',
},

{id:'ss11',type:'snack',effort:'simple',time:3,protein:3,calories:120,emoji:'🍞',
name:'Toast + Jam',nameTA:'டோஸ்ட் ஜாம்',nameUR:'ٹوسٹ جام',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🍓',name:'Fruit jam (strawberry/mango)',nameTA:'ஜாம்',nameUR:'جام',qty:2,unit:'tsp'},
  {emoji:'🧈',name:'Butter',nameTA:'வெண்ணெய்',nameUR:'مکھن',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Place bread on flat pan on V-Guard 1200W. Toast 45 sec each side until golden.',timer:90},
  {text:'Spread butter (while hot). Add jam on top. Eat warm.',timer:0},
],
tip:'Kissan or Mapro jam available at all Chennai supermarkets. For more protein, add peanut butter under the jam. Simple evening snack with chai. Mango jam during season is exceptional.',
video:'toast and jam easy snack',
},

{id:'ss12',type:'snack',effort:'simple',time:2,protein:9,calories:160,emoji:'🌰',
name:'Roasted Chana + Jaggery',nameTA:'வறுத்த கடலை வெல்லம்',nameUR:'بھنا چنا گڑ',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🌰',name:'Roasted chana (Bengal gram)',nameTA:'பொட்டுக்கடலை',nameUR:'بھنا چنا',qty:0.5,unit:'cup'},
  {emoji:'🟤',name:'Jaggery (small piece)',nameTA:'வெல்லம்',nameUR:'گڑ',qty:1,unit:'small piece'},
  {emoji:'🧂',name:'Salt + chili powder (optional)',nameTA:'உப்பு மிளகாய்',nameUR:'نمک مرچ',qty:1,unit:'pinch each'},
],
steps:[
  {text:'Mix roasted chana + a pinch of salt + chili powder in small cup.',timer:0},
  {text:'Alternate biting chana and jaggery. The sweetness of jaggery + saltiness of chana is the combination. Do not mix together.',timer:0},
],
tip:'Roasted chana is sold at every Chennai kirana store (₹20–30/100g). High in protein and fiber. Traditional Tamil snack eaten in the evening with tea. Jaggery prevents sugar crash.',
video:'roasted chana pottukadalai snack Tamil',
},

{id:'ss13',type:'snack',effort:'simple',time:3,protein:1,calories:45,emoji:'🥥',
name:'Coconut Water + Banana',nameTA:'தேங்காய் நீர் வாழைப்பழம்',nameUR:'ناریل پانی کیلا',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🥥',name:'Tender coconut',nameTA:'இளநீர்',nameUR:'کچا ناریل',qty:1,unit:'nos'},
  {emoji:'🍌',name:'Banana',nameTA:'வாழைப்பழம்',nameUR:'کیلا',qty:1,unit:'nos'},
],
steps:[
  {text:'Ask the coconut vendor to cut and open tender coconut.',timer:0},
  {text:'Drink coconut water with straw. Scrape soft coconut flesh with spoon. Eat with a banana.',timer:0},
],
tip:'Tender coconuts are sold on every Chennai street corner (₹30–50 each). The best post-workout electrolyte drink — natural potassium, magnesium, and sodium. Way better than commercial sports drinks.',
video:'coconut water benefits health',
},

{id:'ss14',type:'snack',effort:'simple',time:5,protein:8,calories:200,emoji:'🥛',
name:'Chocolate Milk',nameTA:'சாக்லேட் பால்',nameUR:'چاکلیٹ دودھ',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🥛',name:'Full-fat milk',nameTA:'பால்',nameUR:'دودھ',qty:300,unit:'ml'},
  {emoji:'🍫',name:'Cocoa powder or Bournvita/Horlicks',nameTA:'கோகோ',nameUR:'کوکو',qty:1.5,unit:'tbsp'},
  {emoji:'🍯',name:'Honey or sugar',nameTA:'தேன் சர்க்கரை',nameUR:'شہد چینی',qty:1,unit:'tsp'},
],
steps:[
  {text:'Pour milk into AGARO kettle. Knob → **II (High)**. Heat 4 min until hot.',timer:240},
  {text:'In mug: mix cocoa powder + honey/sugar + 2 tbsp warm water into smooth paste. Pour hot milk over while stirring.',timer:0},
  {text:'Stir vigorously until frothy. Drink hot.',timer:0},
],
tip:'Use raw cacao powder for higher antioxidants (available at health stores). Bournvita or Boost work well. Adding 1 tsp of peanut butter makes this a mini protein drink. Post-evening workout recovery.',
video:'hot chocolate milk easy recipe',
},

{id:'ss15',type:'snack',effort:'simple',time:3,protein:6,calories:170,emoji:'🥤',
name:'Sweet Lassi',nameTA:'இனிப்பு லஸ்ஸி',nameUR:'میٹھی لسی',
equipment:['blender'],nightPrep:false,
ingredients:[
  {emoji:'🍶',name:'Curd',nameTA:'தயிர்',nameUR:'دہی',qty:150,unit:'ml'},
  {emoji:'🥛',name:'Cold milk',nameTA:'பால்',nameUR:'دودھ',qty:100,unit:'ml'},
  {emoji:'🍯',name:'Sugar or honey',nameTA:'சர்க்கரை தேன்',nameUR:'چینی شہد',qty:2,unit:'tsp'},
  {emoji:'🌿',name:'Cardamom powder',nameTA:'ஏலக்காய்',nameUR:'الائچی',qty:1,unit:'pinch'},
  {emoji:'🌹',name:'Rose water (optional)',nameTA:'ரோஜா நீர்',nameUR:'گلاب جل',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Add curd + milk + sugar + cardamom + rose water to NutriPro blender.',timer:0},
  {text:'Blend 20 sec until frothy. Pour into glass. Serve cold.',timer:20},
],
tip:'Lassi is the original Indian protein drink. For mango lassi (seasonal): blend 3 tbsp mango pulp with curd + milk + sugar. Aavin curd makes the richest lassi. Serve over ice cubes.',
video:'sweet lassi recipe easy Indian',
},

{id:'ss16',type:'snack',effort:'simple',time:3,protein:3,calories:130,emoji:'🍪',
name:'Rice Crackers + Peanut Butter',nameTA:'அரிசி பிஸ்கட் வேர்க்கடலை',nameUR:'رائس کریکر مونگ پھلی',
equipment:[],nightPrep:false,
ingredients:[
  {emoji:'🍪',name:'Rice crackers / Ritz crackers',nameTA:'பிஸ்கட்',nameUR:'کریکر',qty:6,unit:'nos'},
  {emoji:'🥜',name:'Peanut butter or cheese spread',nameTA:'வேர்க்கடலை வெண்ணெய்',nameUR:'مونگ پھلی مکھن',qty:1,unit:'tbsp'},
],
steps:[
  {text:'Spread peanut butter or cheese on each cracker.',timer:0},
  {text:'Eat immediately.',timer:0},
],
tip:'Any cracker from Chennai supermarkets works. Protein Wafers by Saffola or Unibic multi-grain biscuits add some nutrition. Quick desk snack — no prep, no washing up.',
video:'crackers peanut butter snack easy',
},

{id:'ss17',type:'snack',effort:'simple',time:3,protein:25,calories:200,emoji:'🥤',
name:'Protein Shake',nameTA:'புரோட்டீன் ஷேக்',nameUR:'پروٹین شیک',
equipment:['blender'],nightPrep:false,
ingredients:[
  {emoji:'🥛',name:'Full-fat milk',nameTA:'பால்',nameUR:'دودھ',qty:300,unit:'ml'},
  {emoji:'🥜',name:'Peanut butter',nameTA:'வேர்க்கடலை வெண்ணெய்',nameUR:'مونگ پھلی مکھن',qty:1.5,unit:'tbsp'},
  {emoji:'🍌',name:'Banana',nameTA:'வாழைப்பழம்',nameUR:'کیلا',qty:1,unit:'nos'},
  {emoji:'🍫',name:'Cocoa powder',nameTA:'கோகோ',nameUR:'کوکو',qty:1,unit:'tsp'},
  {emoji:'🍯',name:'Honey',nameTA:'தேன்',nameUR:'شہد',qty:1,unit:'tsp'},
],
steps:[
  {text:'Add all ingredients to NutriPro blender. I/O switch → **On**. Blend 20–25 sec until smooth.',timer:25},
  {text:'Pour into glass. Drink immediately.',timer:0},
],
tip:'If you have whey protein, add one scoop for 48g protein per shake. Without protein powder, this is 25g protein from peanut butter + milk + banana — still excellent for muscle building. Drink within 30 min of workout.',
video:'homemade protein shake no powder recipe',
},

{id:'ss18',type:'snack',effort:'simple',time:5,protein:5,calories:220,emoji:'🍯',
name:'Bread + Butter + Honey',nameTA:'பிரட் வெண்ணெய் தேன்',nameUR:'بریڈ مکھن شہد',
equipment:['kettle'],nightPrep:false,
ingredients:[
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🧈',name:'Butter',nameTA:'வெண்ணெய்',nameUR:'مکھن',qty:1,unit:'tsp'},
  {emoji:'🍯',name:'Honey',nameTA:'தேன்',nameUR:'شہد',qty:1,unit:'tsp'},
  {emoji:'🥛',name:'Chai or milk',nameTA:'சாய் பால்',nameUR:'چائے دودھ',qty:1,unit:'cup'},
],
steps:[
  {text:'Toast bread lightly (optional — hold near kettle steam for 30 sec or eat fresh).',timer:0},
  {text:'Spread butter. Drizzle honey. Pair with hot chai made in kettle.',timer:0},
],
tip:'Classic simple snack — nothing beats warm bread + butter + honey with chai. Use real honey (not sugar syrup). The combination of fat + carbs + natural sugar gives quick sustained energy.',
video:'bread butter honey snack easy',
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
    print('Snack simple ss7-ss18 inserted (12 recipes)')
