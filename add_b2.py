with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'r', encoding='utf-8') as f:
    content = f.read()

NEW = r"""
{id:'bm12',type:'breakfast',effort:'medium',time:20,protein:12,calories:310,emoji:'🫓',
name:'Plain Dosa + Coconut Chutney',nameTA:'தோசை தேங்காய் சட்னி',nameUR:'ڈوسہ ناریل چٹنی',
equipment:['flat pan','blender'],nightPrep:false,
ingredients:[
  {emoji:'🍚',name:'Ready-made dosa batter',nameTA:'தோசை மாவு',nameUR:'ڈوسہ بیٹر',qty:3,unit:'ladles'},
  {emoji:'🥥',name:'Fresh coconut (grated)',nameTA:'தேங்காய்',nameUR:'ناریل',qty:3,unit:'tbsp'},
  {emoji:'🌶️',name:'Green chili',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🫚',name:'Roasted chana dal',nameTA:'பொட்டுக்கடலை',nameUR:'بھنا چنا',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.5,unit:'tsp'},
  {emoji:'🌿',name:'Curry leaves',nameTA:'கறிவேப்பிலை',nameUR:'کڑی پتہ',qty:4,unit:'leaves'},
],
steps:[
  {text:'Chutney: blend coconut + green chili + roasted chana + salt + 3 tbsp water in NutriPro blender. Pulse 3–4 times, then blend 20 sec. Pour into bowl.',timer:0},
  {text:'Heat flat pan on V-Guard 1600W. Sprinkle few drops water — if it sizzles away, pan is ready. Reduce to 1200W.',timer:60},
  {text:'Pour one ladle batter in center. Quickly spread in circular motion outward to thin crepe (use back of spoon).',timer:0},
  {text:'Drizzle 0.5 tsp oil around edges. Cook 1–2 min until underside is golden and edges lift. Fold and serve. Repeat for 2 more dosas.',timer:90},
  {text:'Heat 1 tsp oil in small pan on 1200W. Add mustard seeds (optional). Add curry leaves. Pour tadka over chutney.',timer:30},
],
tip:'Buy Sakthi or ID Fresh dosa batter. Batter at room temp spreads better. Pan must be very hot before pouring batter. Wipe pan with half onion between dosas to prevent sticking.',
video:'plain dosa recipe crispy thin south indian',
},

{id:'bm13',type:'breakfast',effort:'medium',time:20,protein:10,calories:280,emoji:'🥞',
name:'Vegetable Uttapam',nameTA:'வெஜிடபிள் உத்தப்பம்',nameUR:'سبزی اتاپم',
equipment:['flat pan'],nightPrep:false,
ingredients:[
  {emoji:'🍚',name:'Idli/Dosa batter',nameTA:'இட்லி மாவு',nameUR:'بیٹر',qty:3,unit:'ladles'},
  {emoji:'🧅',name:'Onion (finely chopped)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'nos'},
  {emoji:'🍅',name:'Tomato (finely chopped)',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:0.5,unit:'nos'},
  {emoji:'🌶️',name:'Green chili (sliced)',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🌿',name:'Coriander leaves',nameTA:'கொத்தமல்லி',nameUR:'دھنیا',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.25,unit:'tsp'},
],
steps:[
  {text:'Mix chopped onion + tomato + green chili + coriander + salt in a small bowl.',timer:0},
  {text:'Heat flat pan on V-Guard 1400W. Sprinkle water — if it evaporates instantly, pan is ready.',timer:60},
  {text:'Reduce to 1000W. Pour thick ladle of batter. Do NOT spread thin — leave it thick (2–3 cm). Immediately scatter vegetable mix on top.',timer:0},
  {text:'Drizzle oil around edges. Cover with lid. Cook 3–4 min until top sets and bottom is golden.',timer:240},
  {text:'Flip carefully. Cook 1 min on other side. Serve with coconut chutney or sambar.',timer:60},
],
tip:'Uttapam is thicker than dosa — do not try to thin it. Use leftover idli batter (day 2–3 batter makes better uttapam). Top variations: only onion, or onion+tomato+capsicum.',
video:'vegetable uttapam recipe south indian',
},

{id:'bm14',type:'breakfast',effort:'medium',time:15,protein:8,calories:260,emoji:'🍞',
name:'Bread Upma',nameTA:'பிரட் உப்மா',nameUR:'بریڈ اوپما',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:4,unit:'slices'},
  {emoji:'🧅',name:'Onion',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:1,unit:'medium'},
  {emoji:'🍅',name:'Tomato',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:1,unit:'small'},
  {emoji:'🌶️',name:'Green chili',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🟡',name:'Turmeric + salt',nameTA:'மஞ்சள் உப்பு',nameUR:'ہلدی نمک',qty:0.25,unit:'tsp each'},
  {emoji:'🌿',name:'Curry leaves',nameTA:'கறிவேப்பிலை',nameUR:'کڑی پتہ',qty:4,unit:'leaves'},
  {emoji:'🍋',name:'Lemon juice',nameTA:'எலுமிச்சை',nameUR:'لیموں',qty:1,unit:'tsp'},
],
steps:[
  {text:'Break bread slices into small pieces (1-inch chunks). Set aside.',timer:0},
  {text:'Heat flat pan on V-Guard 1200W. Add 1.5 tsp oil. Add mustard seeds (optional). Add curry leaves + sliced onion + green chili.',timer:0},
  {text:'Sauté onion 2 min until soft. Add chopped tomato + turmeric + salt. Cook 1 min until tomato softens.',timer:120},
  {text:'Add bread pieces. Toss gently to coat with masala. Cook 2 min on 1000W. Squeeze lemon. Serve immediately.',timer:120},
],
tip:'Use 2-day-old bread — fresh bread becomes too mushy. Works great with leftover bread that would go stale. Can add a beaten egg while sautéing onion for extra protein.',
video:'bread upma recipe south indian breakfast',
},

{id:'bm15',type:'breakfast',effort:'medium',time:20,protein:14,calories:290,emoji:'🫓',
name:'Besan Cheela (Gram Flour Pancake)',nameTA:'கடலை மாவு சேலா',nameUR:'بیسن چیلہ',
equipment:['flat pan'],nightPrep:false,
ingredients:[
  {emoji:'🌾',name:'Besan (gram flour)',nameTA:'கடலை மாவு',nameUR:'بیسن',qty:0.5,unit:'cup'},
  {emoji:'🧅',name:'Onion (finely chopped)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🍅',name:'Tomato (finely chopped)',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:0.5,unit:'small'},
  {emoji:'🌶️',name:'Green chili (chopped)',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:1,unit:'nos'},
  {emoji:'🌿',name:'Coriander leaves',nameTA:'கொத்தமல்லி',nameUR:'دھنیا',qty:1,unit:'tbsp'},
  {emoji:'🔴',name:'Chili powder + ajwain',nameTA:'மிளகாய் பொடி',nameUR:'لال مرچ اجوائن',qty:0.25,unit:'tsp each'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Mix besan + onion + tomato + green chili + coriander + chili powder + ajwain + salt in bowl. Add water gradually to make smooth pourable batter (no lumps). Rest 5 min.',timer:300},
  {text:'Heat flat pan on V-Guard 1200W. Grease lightly with oil. Pour half the batter. Spread to medium-thick circle (like thick dosa).',timer:0},
  {text:'Drizzle oil around edges. Cook 2–3 min until underside is golden brown and top looks dry.',timer:150},
  {text:'Flip carefully. Cook 1–2 min other side. Repeat for second cheela. Serve with coriander chutney or ketchup.',timer:90},
],
tip:'Besan cheela is high-protein and gluten-free. Batter should be like dosa batter — thick but pourable. Can add grated paneer or an egg to the batter for more protein.',
video:'besan cheela recipe high protein breakfast',
},

{id:'bm16',type:'breakfast',effort:'medium',time:20,protein:9,calories:240,emoji:'🫓',
name:'Rava Dosa (Crispy Instant)',nameTA:'ரவா தோசை',nameUR:'سوجی ڈوسہ',
equipment:['flat pan'],nightPrep:false,
ingredients:[
  {emoji:'🌾',name:'Semolina (rava/suji)',nameTA:'ரவை',nameUR:'سوجی',qty:0.25,unit:'cup'},
  {emoji:'🌾',name:'Rice flour',nameTA:'அரிசி மாவு',nameUR:'چاول کا آٹا',qty:0.25,unit:'cup'},
  {emoji:'🌾',name:'Maida (all-purpose flour)',nameTA:'மைதா',nameUR:'میدہ',qty:2,unit:'tbsp'},
  {emoji:'🧅',name:'Onion (finely chopped)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🌶️',name:'Green chili + cumin seeds',nameTA:'பச்சை மிளகாய் சீரகம்',nameUR:'ہری مرچ زیرہ',qty:0.5,unit:'tsp each'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Mix rava + rice flour + maida + salt + cumin + green chili + onion. Add 300ml water to make very thin, watery batter (thinner than normal dosa batter). Rest 10 min.',timer:600},
  {text:'Heat flat pan on V-Guard 1600W until smoking hot. This is key — pan must be very hot. Reduce to 1200W.',timer:60},
  {text:'Stir batter (rava settles). Pour from a height in circular pattern — do NOT spread with spoon. The thin batter spreads on its own.',timer:0},
  {text:'Drizzle oil. Cook 3–4 min until golden and crispy. Edges lift. Serve with coconut chutney. Rava dosa is not flipped.',timer:240},
],
tip:'Batter must be very thin (like buttermilk consistency). Very hot pan gives the signature netted, crispy texture. Do not flip — only cook one side. Eat immediately as it loses crispiness.',
video:'rava dosa crispy instant recipe',
},

{id:'bm17',type:'breakfast',effort:'medium',time:20,protein:28,calories:380,emoji:'🥪',
name:'Chicken Sandwich (Grilled)',nameTA:'சிக்கன் சாண்ட்விச்',nameUR:'چکن سینڈوچ',
equipment:['smart pot','flat pan'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Boneless chicken breast',nameTA:'சிக்கன்',nameUR:'مرغی',qty:100,unit:'g'},
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🥬',name:'Cabbage (shredded)',nameTA:'முட்டைக்கோஸ்',nameUR:'پت گوبھی',qty:2,unit:'tbsp'},
  {emoji:'🍅',name:'Tomato (sliced)',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:2,unit:'slices'},
  {emoji:'🫙',name:'Mayonnaise or butter',nameTA:'மயோனீஸ்',nameUR:'مایونیز',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt + pepper + chili powder',nameTA:'உப்பு மிளகு',nameUR:'نمک مرچ',qty:0.5,unit:'tsp each'},
],
steps:[
  {text:'Night prep: boil chicken in Smart Pot. Press **Steam** → 10 min → **Start** with 100ml water. Shred with fork after cooling. Mix with salt + pepper + chili powder. Refrigerate.',timer:600},
  {text:'Morning: spread mayo/butter on both bread slices.',timer:0},
  {text:'Layer shredded chicken + cabbage + tomato slices between bread.',timer:0},
  {text:'Press sandwich together. Grill on flat pan on V-Guard 1200W — press down with spatula, 1 min each side until golden marks appear.',timer:120},
],
tip:'Cook chicken night before and refrigerate — saves 15 min in morning. Use leftover boiled chicken from dinner. Add green chutney or ketchup inside for more flavour.',
video:'chicken sandwich grilled breakfast protein',
},

{id:'bm18',type:'breakfast',effort:'medium',time:15,protein:10,calories:270,emoji:'🍄',
name:'Mushroom Egg Toast',nameTA:'காளான் முட்டை டோஸ்ட்',nameUR:'مشروم انڈا ٹوسٹ',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🍄',name:'Button mushrooms (sliced)',nameTA:'காளான்',nameUR:'مشروم',qty:6,unit:'nos'},
  {emoji:'🥚',name:'Egg',nameTA:'முட்டை',nameUR:'انڈا',qty:1,unit:'nos'},
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🧅',name:'Garlic (minced)',nameTA:'பூண்டு',nameUR:'لہسن',qty:2,unit:'cloves'},
  {emoji:'🧂',name:'Salt + black pepper',nameTA:'உப்பு மிளகு',nameUR:'نمک کالی مرچ',qty:0.5,unit:'tsp each'},
  {emoji:'🌿',name:'Coriander or parsley',nameTA:'கொத்தமல்லி',nameUR:'دھنیا',qty:1,unit:'tbsp'},
],
steps:[
  {text:'Heat flat pan on V-Guard 1200W. Add 1 tsp oil. Add minced garlic, sauté 20 sec.',timer:20},
  {text:'Add sliced mushrooms. Cook on 1400W, stirring, until mushrooms shrink and turn golden (3–4 min). Season with salt + pepper.',timer:240},
  {text:'Push mushrooms to one side. Crack egg into pan. Scramble or fry to preference. Mix with mushrooms. Top with coriander.',timer:90},
  {text:'Place bread slices on pan for 30 sec each side to toast lightly. Serve mushroom egg mixture on toast.',timer:60},
],
tip:'Button mushrooms from Chennai supermarkets (₹80–100/200g). Cook mushrooms on high heat — they release water, then get golden. Mushrooms are a meat substitute rich in Vitamin D.',
video:'mushroom egg toast breakfast recipe',
},

{id:'bm19',type:'breakfast',effort:'medium',time:20,protein:18,calories:340,emoji:'🥔',
name:'Aloo Poha Cutlet',nameTA:'உருளை அவல் கட்லட்',nameUR:'آلو پوہا کٹلٹ',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🥔',name:'Potato (boiled, mashed)',nameTA:'உருளைக்கிழங்கு',nameUR:'آلو',qty:1,unit:'medium'},
  {emoji:'🌾',name:'Poha (soaked)',nameTA:'அவல்',nameUR:'پوہا',qty:0.25,unit:'cup'},
  {emoji:'🧅',name:'Onion (finely chopped)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🌶️',name:'Green chili + ginger (minced)',nameTA:'பச்சை மிளகாய் இஞ்சி',nameUR:'ہری مرچ ادرک',qty:0.5,unit:'tsp each'},
  {emoji:'🌿',name:'Coriander leaves',nameTA:'கொத்தமல்லி',nameUR:'دھنیا',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt + chaat masala',nameTA:'உப்பு',nameUR:'نمک چاٹ مسالا',qty:0.5,unit:'tsp each'},
],
steps:[
  {text:'Boil potato in Smart Pot: Press **Steam** → 8 min → **Start**. Peel and mash. Soak poha in 2 tbsp water 5 min, squeeze dry.',timer:480},
  {text:'Mix mashed potato + squeezed poha + onion + green chili + ginger + coriander + salt + chaat masala. Shape into 4 flat oval patties.',timer:0},
  {text:'Heat flat pan on V-Guard 1200W. Add 2 tsp oil. Place cutlets. Shallow fry 2–3 min each side until golden and crispy.',timer:180},
  {text:'Serve hot with ketchup or green chutney.',timer:0},
],
tip:'Cook potato night before. Soaked poha acts as a binder — do not skip. If cutlets break while flipping, refrigerate raw patties 15 min to firm up. Makes 4 cutlets.',
video:'aloo poha cutlet recipe crispy',
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
    print('Batch 2 done — breakfast medium bm12-bm19 inserted')
