with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'r', encoding='utf-8') as f:
    content = f.read()

NEW = r"""
{id:'sh7',type:'snack',effort:'hard',time:30,protein:22,calories:280,emoji:'🍗',
name:'Chicken Tikka (Pan-Grilled)',nameTA:'சிக்கன் திக்கா',nameUR:'چکن ٹکہ',
equipment:['induction'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Boneless chicken (cubed)',nameTA:'சிக்கன்',nameUR:'مرغی',qty:200,unit:'g'},
  {emoji:'🍶',name:'Curd',nameTA:'தயிர்',nameUR:'دہی',qty:3,unit:'tbsp'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1,unit:'tsp'},
  {emoji:'🔴',name:'Kashmiri chili + chili powder + garam masala',nameTA:'கஷ்மீரி மிளகாய் மசாலா',nameUR:'کشمیری مرچ گرم مسالا',qty:1,unit:'tsp each'},
  {emoji:'🟡',name:'Turmeric + cumin powder',nameTA:'மஞ்சள் சீரகம்',nameUR:'ہلدی زیرہ',qty:0.25,unit:'tsp each'},
  {emoji:'🍋',name:'Lemon juice',nameTA:'எலுமிச்சை',nameUR:'لیموں',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.75,unit:'tsp'},
],
steps:[
  {text:'Marinate chicken: mix curd + ginger-garlic paste + all spices + lemon + salt. Add chicken cubes. Coat well. Refrigerate minimum 2 hours (overnight best).',timer:7200},
  {text:'Heat flat pan on V-Guard 1600W until smoking hot. Add 1 tsp oil.',timer:60},
  {text:'Place marinated chicken pieces in single layer. Do NOT move for 2–3 min until charred spots form on bottom.',timer:180},
  {text:'Flip each piece. Cook other side 2–3 min. Char marks should appear. Reduce to 1400W if burning too fast.',timer:180},
  {text:'Serve on a plate with raw onion rings + lemon wedge + mint chutney.',timer:0},
],
tip:'Overnight marination is the real secret. Kashmiri chili gives the iconic red color without excessive heat. Get charred (not burnt) spots by using high heat and not disturbing the chicken. Rivals restaurant tikka.',
video:'chicken tikka pan grilled recipe at home',
},

{id:'sh8',type:'snack',effort:'hard',time:35,protein:6,calories:280,emoji:'🥔',
name:'Aloo Tikki Chaat',nameTA:'உருளை டிக்கி சாட்',nameUR:'آلو ٹکی چاٹ',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🥔',name:'Potato (boiled, mashed)',nameTA:'உருளைக்கிழங்கு',nameUR:'آلو',qty:3,unit:'medium'},
  {emoji:'🌾',name:'Cornflour',nameTA:'கார்ன் மாவு',nameUR:'کارن فلور',qty:2,unit:'tbsp'},
  {emoji:'🍶',name:'Curd (whisked)',nameTA:'தயிர்',nameUR:'دہی',qty:100,unit:'ml'},
  {emoji:'🟤',name:'Tamarind chutney (ready-made)',nameTA:'புளி சட்னி',nameUR:'تمر ہندی چٹنی',qty:2,unit:'tbsp'},
  {emoji:'🌿',name:'Green chutney (coriander-mint)',nameTA:'கொத்தமல்லி சட்னி',nameUR:'ہری چٹنی',qty:2,unit:'tbsp'},
  {emoji:'🫙',name:'Chaat masala + cumin powder',nameTA:'சாட் மசாலா சீரகம்',nameUR:'چاٹ مسالا زیرہ',qty:0.5,unit:'tsp each'},
  {emoji:'🌾',name:'Sev (thin fried noodles, optional)',nameTA:'சேவ்',nameUR:'سیو',qty:2,unit:'tbsp'},
],
steps:[
  {text:'Mix potato + cornflour + chaat masala + salt. Shape into 4 flat tikkis. (See sm17 for tikki technique.)',timer:0},
  {text:'Pan-fry tikkis: heat flat pan V-Guard 1200W, 2 tsp oil, 3–4 min per side until crispy golden.',timer:480},
  {text:'Make green chutney: blend coriander + mint + green chili + salt + lemon juice in NutriPro blender.',timer:0},
  {text:'Assembly: place 2 tikkis on plate. Drizzle whisked curd generously. Add tamarind chutney + green chutney.',timer:0},
  {text:'Sprinkle chaat masala + cumin. Add sev on top if available. Serve immediately.',timer:0},
],
tip:'Tamarind chutney (Maggi or Aachi brand, ₹40/bottle) saves a lot of time. The combination of sweet tamarind + spicy green + tangy curd + crunchy tikki is what chaat is all about.',
video:'aloo tikki chaat recipe street food style',
},

{id:'sh9',type:'snack',effort:'hard',time:40,protein:16,calories:300,emoji:'🌯',
name:'Chicken Spring Rolls',nameTA:'சிக்கன் ஸ்பிரிங் ரோல்',nameUR:'چکن سپرنگ رول',
equipment:['induction','frying pan'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Chicken (shredded, cooked)',nameTA:'சிக்கன்',nameUR:'مرغی',qty:100,unit:'g'},
  {emoji:'🥕',name:'Carrot + cabbage (shredded)',nameTA:'கேரட் முட்டைக்கோஸ்',nameUR:'گاجر گوبھی',qty:0.25,unit:'cup each'},
  {emoji:'🧅',name:'Spring onion',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:2,unit:'nos'},
  {emoji:'🫙',name:'Soy sauce + ginger-garlic',nameTA:'சோயா சாஸ் இஞ்சி பூண்டு',nameUR:'سویا ساس ادرک لہسن',qty:1,unit:'tsp each'},
  {emoji:'🌾',name:'Spring roll sheets (or thin chapati)',nameTA:'ரோல் தாள்',nameUR:'رول شیٹ',qty:6,unit:'nos'},
  {emoji:'🌾',name:'Cornflour paste (for sealing)',nameTA:'கார்ன் மாவு',nameUR:'کارن فلور',qty:1,unit:'tbsp + 2 tsp water'},
  {emoji:'🛢️',name:'Oil for frying',nameTA:'எண்ணெய்',nameUR:'تیل',qty:200,unit:'ml'},
],
steps:[
  {text:'Filling: heat pan 1600W, add oil + spring onion + carrot + cabbage + ginger-garlic. Stir-fry 3 min on high. Add soy sauce + shredded chicken. Toss 1 min. Cool completely.',timer:240},
  {text:'Lay spring roll sheet flat. Place 2 tbsp filling near one end. Roll tightly — fold sides in, then roll forward. Seal edge with cornflour paste.',timer:0},
  {text:'Repeat for all 6 rolls.',timer:0},
  {text:'Heat frying pan on V-Guard **Deep Fry** preset. Add oil. Fry 4–5 rolls at a time, 3–4 min, turning until golden all over.',timer:240},
  {text:'Drain on paper. Serve with sweet chili sauce or soy dipping sauce.',timer:0},
],
tip:'Spring roll sheets from Chennai Chinese stores or frozen section of supermarkets. If unavailable, use thin homemade chapati. Fill is cooked before rolling — just need to fry the shell. Night-prep filling saves time.',
video:'chicken spring rolls recipe crispy homemade',
},

{id:'sh10',type:'snack',effort:'hard',time:35,protein:20,calories:310,emoji:'🍔',
name:'Bun Kabab',nameTA:'பன் கபாப்',nameUR:'بن کباب',
equipment:['induction'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Minced chicken (keema)',nameTA:'சிக்கன் கீமா',nameUR:'چکن قیمہ',qty:200,unit:'g'},
  {emoji:'🥚',name:'Egg',nameTA:'முட்டை',nameUR:'انڈا',qty:1,unit:'nos'},
  {emoji:'🧅',name:'Onion (grated)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🫙',name:'Ginger-garlic + garam masala + chili',nameTA:'இஞ்சி பூண்டு மசாலா',nameUR:'ادرک لہسن گرم مسالا مرچ',qty:1,unit:'tsp each'},
  {emoji:'🍞',name:'Burger bun',nameTA:'பன்',nameUR:'بن',qty:2,unit:'nos'},
  {emoji:'🫙',name:'Green chutney + sliced onion + tomato',nameTA:'சட்னி வெங்காயம்',nameUR:'ہری چٹنی پیاز ٹماٹر',qty:1,unit:'each'},
  {emoji:'🧂',name:'Salt + coriander leaves',nameTA:'உப்பு',nameUR:'نمک دھنیا',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Mix keema + grated onion (squeeze dry) + ginger-garlic + garam masala + chili + salt + beaten egg + coriander. Rest 30 min.',timer:1800},
  {text:'Shape into 2 flat round patties (size of the bun).',timer:0},
  {text:'Heat flat pan on V-Guard 1400W. Add 1.5 tsp oil. Cook patties 4–5 min each side until cooked through and golden crust forms.',timer:300},
  {text:'Toast bun halves in same pan 30 sec cut-side down.',timer:30},
  {text:'Assemble: spread green chutney on bun. Add patty + sliced tomato + raw onion rings. Top bun. Serve hot.',timer:0},
],
tip:'A classic Pakistani-inspired street burger. The egg acts as a binder — keema patties without egg will crumble. Squeeze ALL water from grated onion or the patty becomes too soft. Burger buns from Chennai bakeries.',
video:'bun kabab recipe Pakistani chicken patty',
},

{id:'sh11',type:'snack',effort:'hard',time:20,protein:10,calories:260,emoji:'🧀',
name:'Grilled Cheese Toast',nameTA:'கிரில்ட் சீஸ் டோஸ்ட்',nameUR:'گریلڈ چیز ٹوسٹ',
equipment:['induction'],nightPrep:false,
ingredients:[
  {emoji:'🍞',name:'Bread slices',nameTA:'பிரட்',nameUR:'بریڈ',qty:2,unit:'slices'},
  {emoji:'🧀',name:'Cheese slices or grated cheddar',nameTA:'சீஸ்',nameUR:'پنیر',qty:2,unit:'slices'},
  {emoji:'🧈',name:'Butter',nameTA:'வெண்ணெய்',nameUR:'مکھن',qty:1.5,unit:'tsp'},
  {emoji:'🌶️',name:'Green chili (minced) or chili flakes',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:0.5,unit:'tsp'},
  {emoji:'⚫',name:'Black pepper',nameTA:'மிளகு',nameUR:'کالی مرچ',qty:1,unit:'pinch'},
  {emoji:'🧅',name:'Onion (finely chopped, optional)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:1,unit:'tbsp'},
],
steps:[
  {text:'Spread butter on one side of each bread slice. Butter side faces OUT (toward the pan).',timer:0},
  {text:'On the inner side: place cheese slice. Sprinkle chili + pepper + onion. Close sandwich.',timer:0},
  {text:'Heat flat pan on V-Guard 1000W (medium, not high). Place sandwich butter-side down.',timer:0},
  {text:'Cook 2–3 min until bottom is golden. Press down gently with spatula. Flip carefully.',timer:180},
  {text:'Cook other side 2 min until golden and cheese is fully melted. Serve immediately.',timer:120},
],
tip:'Low-medium heat is key — high heat burns bread before cheese melts. Amul cheese slices (₹60/pack) are widely available. Add a thin slice of chicken or sliced boiled egg inside for a protein boost.',
video:'grilled cheese sandwich recipe crispy',
},

{id:'sh12',type:'snack',effort:'hard',time:30,protein:24,calories:380,emoji:'🌯',
name:'Chicken Kathi Roll',nameTA:'சிக்கன் கதி ரோல்',nameUR:'چکن کاٹھی رول',
equipment:['induction'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Boneless chicken (strips)',nameTA:'சிக்கன்',nameUR:'مرغی',qty:150,unit:'g'},
  {emoji:'🥚',name:'Egg',nameTA:'முட்டை',nameUR:'انڈا',qty:1,unit:'nos'},
  {emoji:'🌾',name:'Atta (for 2 parathas)',nameTA:'கோதுமை மாவு',nameUR:'آٹا',qty:0.5,unit:'cup'},
  {emoji:'🔴',name:'Chili powder + cumin + garam masala',nameTA:'மிளகாய் சீரகம் மசாலா',nameUR:'مرچ زیرہ گرم مسالا',qty:0.5,unit:'tsp each'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1,unit:'tsp'},
  {emoji:'🥬',name:'Cabbage + onion (shredded)',nameTA:'முட்டைக்கோஸ் வெங்காயம்',nameUR:'گوبھی پیاز',qty:2,unit:'tbsp each'},
  {emoji:'🧂',name:'Salt + lemon + chutney',nameTA:'உப்பு எலுமிச்சை',nameUR:'نمک لیموں چٹنی',qty:0.5,unit:'tsp each'},
],
steps:[
  {text:'Marinate chicken strips: ginger-garlic paste + chili + cumin + garam masala + salt + lemon. Rest 30 min.',timer:1800},
  {text:'Make paratha: knead atta + water to soft dough. Roll 2 thin parathas. Cook each on flat pan (V-Guard 1600W) 1 min each side with ghee.',timer:120},
  {text:'Cook chicken: heat pan 1400W + oil. Add chicken strips. Stir-fry on high heat 5–6 min until cooked and slightly charred.',timer:360},
  {text:'Egg coating: beat egg + pinch salt. Pour over hot paratha on pan. Flip immediately so egg side is down. Cook 30 sec.',timer:30},
  {text:'Place spicy chicken + cabbage + onion in center. Squeeze green chutney. Roll tight. Wrap in foil to hold shape.',timer:0},
],
tip:'Kolkata-style kathi roll has an egg-coated paratha (anday wala paratha) — step 4 is the key technique. The egg sticks to the paratha and becomes crispy. Excellent as a packed snack or dinner on the go.',
video:'chicken kathi roll recipe Kolkata style egg paratha',
},

{id:'sh13',type:'snack',effort:'hard',time:25,protein:16,calories:290,emoji:'🥚',
name:'Cheesy Egg Muffin',nameTA:'சீஸ் முட்டை மஃபின்',nameUR:'چیز انڈا مفن',
equipment:['smart pot'],nightPrep:false,
ingredients:[
  {emoji:'🥚',name:'Eggs',nameTA:'முட்டை',nameUR:'انڈا',qty:3,unit:'nos'},
  {emoji:'🧀',name:'Cheese (grated)',nameTA:'சீஸ்',nameUR:'پنیر',qty:3,unit:'tbsp'},
  {emoji:'🧅',name:'Onion + capsicum (finely chopped)',nameTA:'வெங்காயம் குடை மிளகாய்',nameUR:'پیاز شملہ مرچ',qty:1,unit:'tbsp each'},
  {emoji:'🌶️',name:'Green chili (minced)',nameTA:'பச்சை மிளகாய்',nameUR:'ہری مرچ',qty:0.5,unit:'nos'},
  {emoji:'⚫',name:'Black pepper + salt',nameTA:'மிளகு உப்பு',nameUR:'کالی مرچ نمک',qty:0.25,unit:'tsp each'},
  {emoji:'🛢️',name:'Oil (for greasing)',nameTA:'எண்ணெய்',nameUR:'تیل',qty:0.5,unit:'tsp'},
],
steps:[
  {text:'Beat eggs + salt + pepper. Add onion + capsicum + green chili + cheese. Mix.',timer:0},
  {text:'Grease 3–4 small steel cups or a muffin-sized steel tiffin bowl with oil. Pour egg mixture in (fill 3/4 full).',timer:0},
  {text:'Add 1.5 cups water to Smart Pot. Place greased cups on trivet inside. Close lid. Press **Steam** → 10 min → **Start**.',timer:600},
  {text:'Quick release. Open. Egg muffins should be set and puffy. Insert toothpick — if it comes out clean, done.',timer:0},
  {text:'Run knife around edges. Unmold. Serve hot.',timer:0},
],
tip:'Steam-cooked eggs become incredibly fluffy — not rubbery like microwaved eggs. Add any mix-in: mushrooms, spinach, chicken pieces. Great high-protein snack that feels like a restaurant item.',
video:'steamed egg muffin recipe fluffy protein',
},

{id:'sh14',type:'snack',effort:'hard',time:30,protein:24,calories:320,emoji:'🍗',
name:'Chicken 65',nameTA:'சிக்கன் 65',nameUR:'چکن 65',
equipment:['frying pan'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Boneless chicken (bite-sized)',nameTA:'சிக்கன்',nameUR:'مرغی',qty:200,unit:'g'},
  {emoji:'🥚',name:'Egg',nameTA:'முட்டை',nameUR:'انڈا',qty:1,unit:'nos'},
  {emoji:'🔴',name:'Chili powder + Kashmiri chili + coriander powder',nameTA:'மிளகாய் கஷ்மீரி கொத்தமல்லி',nameUR:'مرچ کشمیری دھنیا',qty:1,unit:'tsp each'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1.5,unit:'tsp'},
  {emoji:'🌾',name:'Cornflour + rice flour',nameTA:'கார்ன் மாவு அரிசி மாவு',nameUR:'کارن فلور چاول آٹا',qty:2,unit:'tbsp each'},
  {emoji:'🌿',name:'Curry leaves + green chili (for tempering)',nameTA:'கறிவேப்பிலை',nameUR:'کڑی پتہ ہری مرچ',qty:8,unit:'leaves + 2 nos'},
  {emoji:'🧂',name:'Salt + food color (red, optional)',nameTA:'உப்பு',nameUR:'نمک',qty:0.75,unit:'tsp'},
],
steps:[
  {text:'Marinate: mix chicken + beaten egg + ginger-garlic + chili powders + coriander + cornflour + rice flour + salt. Should be dry coating (no dripping). Rest 1 hour minimum.',timer:3600},
  {text:'Heat frying pan on V-Guard **Deep Fry** preset. Test oil readiness with small piece of chicken — it should sizzle instantly.',timer:120},
  {text:'Fry chicken in batches (do not overcrowd). Fry 5–6 min until golden red and crispy. Drain.',timer:360},
  {text:'Keep 1 tsp hot oil in pan on 1200W. Add curry leaves + slit green chili. Fry 20 sec. Add fried chicken pieces. Toss to coat.',timer:20},
  {text:'Serve hot immediately with lemon wedge and raw onion rings.',timer:0},
],
tip:'Chicken 65 is the most famous Indian deep-fried chicken snack. The combination of cornflour + rice flour gives the distinctively crispy light coating. Kashmiri chili gives color without heat. Do not skip the curry leaf tempering at the end.',
video:'chicken 65 recipe crispy restaurant style',
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
    print('Snack hard sh7-sh14 inserted (8 recipes)')
