with open(r'C:\Users\Syed Asrar\bachelor-meal-plan\meals.js', 'r', encoding='utf-8') as f:
    content = f.read()

NEW = r"""
{id:'lh6',type:'lunch',effort:'hard',time:45,protein:22,calories:440,emoji:'🦐',
name:'Prawn Biryani',nameTA:'இறால் பிரியாணி',nameUR:'جھینگا بریانی',
equipment:['smart pot'],nightPrep:true,
ingredients:[
  {emoji:'🦐',name:'Prawns (cleaned, medium)',nameTA:'இறால்',nameUR:'جھینگا',qty:200,unit:'g'},
  {emoji:'🍚',name:'Basmati rice',nameTA:'பாஸ்மதி',nameUR:'باسمتی',qty:0.75,unit:'cup'},
  {emoji:'🧅',name:'Onion (thinly sliced)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:2,unit:'medium'},
  {emoji:'🍅',name:'Tomato',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:1,unit:'nos'},
  {emoji:'🍶',name:'Curd (beaten)',nameTA:'தயிர்',nameUR:'دہی',qty:3,unit:'tbsp'},
  {emoji:'🌿',name:'Mint + coriander leaves',nameTA:'புதினா கொத்தமல்லி',nameUR:'پدینہ دھنیا',qty:2,unit:'tbsp each'},
  {emoji:'🫙',name:'Aachi Biryani masala + ginger-garlic paste',nameTA:'பிரியாணி மசாலா',nameUR:'بریانی مسالا ادرک لہسن',qty:1.5,unit:'tsp + 1 tsp'},
  {emoji:'🧂',name:'Salt + whole spices (bay leaf, cardamom, clove)',nameTA:'உப்பு மசாலா',nameUR:'نمک ثابت مسالا',qty:0.75,unit:'tsp + 2 each'},
],
steps:[
  {text:'Marinate prawns: curd + ginger-garlic paste + biryani masala + salt. Rest 30 min (or overnight in fridge).',timer:1800},
  {text:'Soak basmati rice 20 min. Drain.',timer:1200},
  {text:'Press **Sauté** → **Start** on Smart Pot. Add 2 tsp oil. Fry whole spices 30 sec. Fry onion until deep golden brown (6–8 min). Add tomato. Cook 2 min. Add marinated prawns. Stir 2 min. Press **Cancel**.',timer:600},
  {text:'Add drained rice on top. Add mint + coriander + 1.25 cups water (do not stir — layer it). Close lid. Press **Pressure Cook** → 5 min → **Start**.',timer:300},
  {text:'Quick release. Open carefully. Gently fluff without breaking rice. Let rest 2 min.',timer:0},
  {text:'Serve with raita (curd + chopped onion + coriander).',timer:0},
],
tip:'Prawns cook fast — do not increase pressure cooking time or they become rubbery. Frying onions until deep golden (not just soft) is the key to biryani flavor. Golden fried onion = caramelized sweetness.',
video:'prawn biryani recipe pressure cooker quick',
},

{id:'lh7',type:'lunch',effort:'hard',time:40,protein:28,calories:450,emoji:'🫔',
name:'Mutton Keema Paratha',nameTA:'ஆட்டு கீமா பராத்தா',nameUR:'بکرے کا قیمہ پراٹھا',
equipment:['induction','flat pan','smart pot'],nightPrep:true,
ingredients:[
  {emoji:'🍖',name:'Minced mutton (keema)',nameTA:'ஆட்டு கீமா',nameUR:'بکرے کا قیمہ',qty:150,unit:'g'},
  {emoji:'🌾',name:'Aashirvaad atta',nameTA:'கோதுமை மாவு',nameUR:'آٹا',qty:1,unit:'cup'},
  {emoji:'🧅',name:'Onion',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:1,unit:'small'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1,unit:'tsp'},
  {emoji:'🔴',name:'Chili + coriander + garam masala',nameTA:'மிளகாய் கொத்தமல்லி',nameUR:'مرچ دھنیا گرم مسالا',qty:0.5,unit:'tsp each'},
  {emoji:'🌿',name:'Coriander + mint leaves',nameTA:'கொத்தமல்லி புதினா',nameUR:'دھنیا پدینہ',qty:1,unit:'tbsp each'},
  {emoji:'🧂',name:'Salt + ghee',nameTA:'உப்பு நெய்',nameUR:'نمک گھی',qty:0.5,unit:'tsp each'},
],
steps:[
  {text:'Night: cook keema filling. Heat pan 1400W, add oil + onion (3 min). Add ginger-garlic + spices + mutton keema. Cook 8–10 min until dry and cooked. Add coriander + mint. Cool. Refrigerate.',timer:600},
  {text:'Morning: knead atta + salt + water to soft dough (Inalsa kneading blade **2 (High)** 60 sec). Rest 10 min. Divide into 4 balls.',timer:600},
  {text:'Roll one ball into 6-inch circle. Place 2 tbsp keema filling in center. Bring edges up and seal. Roll gently into 5-inch paratha.',timer:0},
  {text:'Cook on flat pan V-Guard 1600W: 1 min each side. Apply ghee. Flip. Press with spatula until brown spots on both sides. Repeat all 4.',timer:120},
  {text:'Serve hot with curd and green chutney.',timer:0},
],
tip:'Keema filling must be very dry (no moisture) or the paratha breaks while rolling. Seal edges firmly. Seal any cracks with a pinch of dough. Night-prepped filling makes morning assembly 15 min.',
video:'mutton keema paratha recipe stuffed',
},

{id:'lh8',type:'lunch',effort:'hard',time:50,protein:30,calories:460,emoji:'🍛',
name:'Chicken Dum (Home Style)',nameTA:'சிக்கன் தும் குழம்பு',nameUR:'چکن دم قورمہ',
equipment:['smart pot','induction'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Chicken (bone-in, 4 pieces)',nameTA:'சிக்கன்',nameUR:'مرغی',qty:300,unit:'g'},
  {emoji:'🍶',name:'Curd',nameTA:'தயிர்',nameUR:'دہی',qty:4,unit:'tbsp'},
  {emoji:'🧅',name:'Onion (fried golden)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:2,unit:'medium'},
  {emoji:'🌿',name:'Mint + coriander leaves',nameTA:'புதினா கொத்தமல்லி',nameUR:'پدینہ دھنیا',qty:2,unit:'tbsp each'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1.5,unit:'tsp'},
  {emoji:'🔴',name:'Biryani masala + chili + turmeric',nameTA:'மசாலா மிளகாய் மஞ்சள்',nameUR:'مسالا مرچ ہلدی',qty:1,unit:'tsp each'},
  {emoji:'🍋',name:'Lemon juice',nameTA:'எலுமிச்சை',nameUR:'لیموں',qty:1,unit:'tbsp'},
  {emoji:'🧂',name:'Salt + whole spices',nameTA:'உப்பு மசாலா',nameUR:'نمک ثابت مسالا',qty:1,unit:'tsp + 3 each'},
],
steps:[
  {text:'Night marination: score chicken pieces deeply. Mix curd + ginger-garlic + biryani masala + chili + turmeric + lemon + salt. Coat chicken. Refrigerate 8 hours minimum.',timer:0},
  {text:'Morning: press **Sauté** → **Start** on Smart Pot. Add 2 tsp oil. Fry whole spices 30 sec. Add sliced onion — fry until deep golden brown (7–8 min). Press **Cancel**.',timer:480},
  {text:'Add marinated chicken + all the marinade + mint + coriander + 50ml water. Layer. Close lid.',timer:0},
  {text:'Press **Meat** → 15 min → **Start**. Natural release 10 min.',timer:900},
  {text:'Open. Stir gently. Gravy should be thick and aromatic. If thin, press **Sauté** and reduce 3 min uncovered.',timer:180},
  {text:'Serve with basmati rice or naan.',timer:0},
],
tip:'Overnight marination is non-negotiable — it tenderizes the meat and infuses the spices. Deeply scoring the chicken lets marinade penetrate to the bone. The result rivals restaurant chicken dum.',
video:'chicken dum recipe home style Hyderabadi',
},

{id:'lh9',type:'lunch',effort:'hard',time:45,protein:22,calories:390,emoji:'🥟',
name:'Kuzhi Paniyaram (Chicken Stuffed)',nameTA:'குழி பணியாரம் சிக்கன்',nameUR:'کوژی پنیارم چکن',
equipment:['induction','smart pot'],nightPrep:true,
ingredients:[
  {emoji:'🍚',name:'Idli batter (ready-made)',nameTA:'இட்லி மாவு',nameUR:'اڈلی بیٹر',qty:1,unit:'cup'},
  {emoji:'🍗',name:'Minced chicken (cooked, spiced)',nameTA:'சிக்கன் கீமா',nameUR:'چکن قیمہ',qty:100,unit:'g'},
  {emoji:'🧅',name:'Onion (finely chopped)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🌶️',name:'Green chili + curry leaves',nameTA:'பச்சை மிளகாய் கறிவேப்பிலை',nameUR:'ہری مرچ کڑی پتہ',qty:1,unit:'each'},
  {emoji:'🔴',name:'Chili powder + salt + ginger-garlic',nameTA:'மிளகாய் உப்பு',nameUR:'مرچ نمک ادرک لہسن',qty:0.5,unit:'tsp each'},
  {emoji:'🛢️',name:'Oil (for the paniyaram pan)',nameTA:'எண்ணெய்',nameUR:'تیل',qty:1,unit:'tsp per hole'},
],
steps:[
  {text:'Night: cook chicken keema filling — heat pan, add oil + onion + green chili + ginger-garlic + spices + minced chicken. Cook 8 min until dry. Cool, refrigerate.',timer:480},
  {text:'Morning: mix onion + curry leaves into idli batter. The batter should be thick (pancake consistency).',timer:0},
  {text:'Heat a small round flat pan on V-Guard 1200W. Pour 0.5 tsp oil in each depression (use muffin pan or small bowls). Pour 1 tbsp batter in each.',timer:60},
  {text:'Immediately place 1 tsp chicken filling in center of each. Cover with 0.5 tbsp more batter on top.',timer:0},
  {text:'Cover with lid or plate. Cook 3–4 min until bottom sets. Flip gently with toothpick. Cook 2 min other side until golden.',timer:240},
  {text:'Serve hot with coconut chutney.',timer:0},
],
tip:'Traditional kuzhi paniyaram needs a special cast-iron paniyaram pan (₹150–200 at Chennai shops or online). Alternatively use a muffin tray on induction. The chicken filling makes it non-veg — a Chennai street food favorite.',
video:'kuzhi paniyaram recipe chicken stuffed',
},

{id:'lh10',type:'lunch',effort:'hard',time:40,protein:26,calories:420,emoji:'🐟',
name:'Chettinad Fish Curry + Rice',nameTA:'செட்டிநாடு மீன் குழம்பு',nameUR:'چیٹناڈ مچھلی کری چاول',
equipment:['smart pot','induction'],nightPrep:false,
ingredients:[
  {emoji:'🐟',name:'Fish (surmai or katla, pieces)',nameTA:'மீன்',nameUR:'مچھلی',qty:200,unit:'g'},
  {emoji:'🍚',name:'Cooked rice',nameTA:'சாதம்',nameUR:'چاول',qty:1.5,unit:'cups'},
  {emoji:'🧅',name:'Small onions (shallots)',nameTA:'சின்ன வெங்காயம்',nameUR:'چھوٹا پیاز',qty:8,unit:'nos'},
  {emoji:'🍅',name:'Tomato',nameTA:'தக்காளி',nameUR:'ٹماٹر',qty:1,unit:'nos'},
  {emoji:'🟡',name:'Tamarind paste',nameTA:'புளி',nameUR:'تمر ہندی',qty:1,unit:'tbsp'},
  {emoji:'🌰',name:'Kalpasi + star anise + marathi mokku (Chettinad spices)',nameTA:'கற்பூரவள்ளி மசாலா',nameUR:'چیٹناڈ مسالا',qty:1,unit:'pinch each'},
  {emoji:'🔴',name:'Chili powder + coriander + turmeric',nameTA:'மிளகாய் கொத்தமல்லி மஞ்சள்',nameUR:'مرچ دھنیا ہلدی',qty:1,unit:'tsp each'},
  {emoji:'🧂',name:'Salt + curry leaves + mustard',nameTA:'உப்பு',nameUR:'نمک',qty:0.75,unit:'tsp'},
],
steps:[
  {text:'Marinate fish: turmeric + chili powder + salt + lemon juice. Rest 15 min.',timer:900},
  {text:'Press **Sauté** → **Start** on Smart Pot. Add 2 tsp sesame oil. Add mustard seeds + curry leaves + Chettinad spices (kalpasi, star anise). Fry 30 sec.',timer:30},
  {text:'Add shallots. Fry until golden (3 min). Add tomato + tamarind paste + coriander + chili + salt. Cook 3 min. Press **Cancel**.',timer:360},
  {text:'Add fish pieces + 200ml water. Close lid. Press **Pressure Cook** → 4 min → **Start**. Quick release. Open carefully — fish breaks easily.',timer:240},
  {text:'If gravy is too thin, remove fish carefully, reduce gravy on **Sauté** 3 min, add fish back. Serve over rice.',timer:0},
],
tip:'Sesame oil (nallennai) is traditional for Chettinad fish curry — use it instead of sunflower oil. Kalpasi and marathi mokku are Chettinad-specific spices available at Chennai spice shops.',
video:'Chettinad fish curry recipe South Indian',
},

{id:'lh11',type:'lunch',effort:'hard',time:40,protein:24,calories:410,emoji:'🌯',
name:'Chicken Seekh Kebab Roll',nameTA:'சிக்கன் ஸீக் கபாப் ரோல்',nameUR:'چکن سیخ کباب رول',
equipment:['induction','flat pan'],nightPrep:true,
ingredients:[
  {emoji:'🍗',name:'Minced chicken (keema)',nameTA:'சிக்கன் கீமா',nameUR:'چکن قیمہ',qty:200,unit:'g'},
  {emoji:'🌾',name:'Atta (for 2 chapatis)',nameTA:'கோதுமை மாவு',nameUR:'آٹا',qty:0.5,unit:'cup'},
  {emoji:'🧅',name:'Onion (grated)',nameTA:'வெங்காயம்',nameUR:'پیاز',qty:0.5,unit:'small'},
  {emoji:'🫙',name:'Ginger-garlic paste',nameTA:'இஞ்சி பூண்டு',nameUR:'ادرک لہسن',qty:1,unit:'tsp'},
  {emoji:'🔴',name:'Kebab masala + chili + garam masala',nameTA:'மசாலா மிளகாய்',nameUR:'کباب مسالا مرچ',qty:0.5,unit:'tsp each'},
  {emoji:'🥬',name:'Cabbage (shredded) + lemon + chutney',nameTA:'முட்டைக்கோஸ் எலுமிச்சை',nameUR:'پت گوبھی لیموں',qty:2,unit:'tbsp + 1 each'},
  {emoji:'🧂',name:'Salt + egg (binder)',nameTA:'உப்பு முட்டை',nameUR:'نمک انڈا',qty:0.5,unit:'tsp + 1 nos'},
],
steps:[
  {text:'Mix keema + grated onion (squeeze out water) + ginger-garlic + all spices + salt + 1 beaten egg. Mix thoroughly. Refrigerate 30 min.',timer:1800},
  {text:'Shape into 4 long cylinders (seekh shape). Heat flat pan on V-Guard 1400W. Add 1 tsp oil. Pan-fry kebabs 3–4 min each side, turning carefully to brown all sides.',timer:240},
  {text:'Make 2 chapatis: knead atta, roll thin, cook on flat pan (V-Guard 1600W) 1 min each side with ghee.',timer:120},
  {text:'Spread green chutney on chapati. Place 2 kebabs on each chapati. Top with shredded cabbage + onion rings + lemon squeeze.',timer:0},
  {text:'Roll tightly. Wrap in foil if packing for lunch.',timer:0},
],
tip:'Squeeze all water out of grated onion before mixing — wet onion makes kebabs fall apart. Egg binds the mixture. Pan-frying gives a crust similar to tandoor. Excellent packed lunch roll.',
video:'chicken seekh kebab roll recipe home',
},

{id:'lh12',type:'lunch',effort:'hard',time:45,protein:20,calories:420,emoji:'🫓',
name:'Stuffed Paratha + Dal + Pickle',nameTA:'பூரித்த பராத்தா தால் ஊறுகாய்',nameUR:'بھرا پراٹھا دال اچار',
equipment:['smart pot','flat pan'],nightPrep:true,
ingredients:[
  {emoji:'🌾',name:'Aashirvaad atta',nameTA:'கோதுமை மாவு',nameUR:'آٹا',qty:1,unit:'cup'},
  {emoji:'🥔',name:'Potato (boiled, mashed)',nameTA:'உருளைக்கிழங்கு',nameUR:'آلو',qty:2,unit:'medium'},
  {emoji:'🌶️',name:'Green chili + coriander + cumin + chaat masala',nameTA:'பச்சை மிளகாய் சீரகம்',nameUR:'ہری مرچ دھنیا زیرہ چاٹ',qty:1,unit:'each'},
  {emoji:'🫘',name:'Toor dal (for dal side dish)',nameTA:'துவரம் பருப்பு',nameUR:'ارہر دال',qty:0.25,unit:'cup'},
  {emoji:'🧂',name:'Salt',nameTA:'உப்பு',nameUR:'نمک',qty:0.75,unit:'tsp'},
  {emoji:'🧈',name:'Ghee',nameTA:'நெய்',nameUR:'گھی',qty:2,unit:'tsp'},
  {emoji:'🫙',name:'Avakkai/mango pickle',nameTA:'மாவடு',nameUR:'اچار',qty:1,unit:'tsp'},
],
steps:[
  {text:'Night: cook dal in Smart Pot (Bean 10 min) + temper with mustard/curry leaves. Refrigerate.',timer:600},
  {text:'Night: boil potatoes (Steam 10 min). Mash with green chili + coriander + cumin + chaat masala + salt. Refrigerate.',timer:600},
  {text:'Morning: knead atta + salt + water. Divide into 4 balls. Roll each into 5-inch circle. Place 2 tbsp potato filling in center. Seal edges. Roll gently to 6-inch paratha.',timer:0},
  {text:'Cook each paratha on flat pan (V-Guard 1600W): 1 min, flip, add ghee, flip again, press with spatula, ghee other side. Golden on both sides.',timer:90},
  {text:'Reheat dal on induction (800W). Serve 2 parathas + dal + pickle on the side.',timer:180},
],
tip:'This is the classic Punjabi dhaba lunch — aloo paratha with dal and pickle. Night-prepping both filling and dal makes morning assembly 20 min. The meal is filling, satisfying, and balanced.',
video:'aloo paratha with dal recipe dhaba style',
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
    print('Lunch hard lh6-lh12 inserted (7 recipes)')
