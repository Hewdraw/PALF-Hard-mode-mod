init python:
    class ForeveralTypes:
        AddType = 0
        Training = 1
        AddSTAB = 2
        AddProficiency = 3
        Scaling = 4
        TurnStartStatus = 5
        FormSwap = 6
        AddAbility = 7
        Mega = 8
        MoveBoost = 9

    class FVLMacros:
        FVLName = 0
        FVLTrainer = 1
        FVLLevel = 2
        FVLType = 3
        FVLTypeData = 4
        FVLMoves = 5
        FVLDescription = 6

    def lookupforeveraldata(name, datatype):
        for entry in foreveraldex:
            if (entry[FVLMacros.FVLName] == name):
                return entry[datatype]

    foreveraldex = []
    #Name, Trainer, Level, Type, typedata, movesimparted, Description, 
    foreveraldex.append(["Clobbopus Foreveral", "Bea", 3, ForeveralTypes.AddType, ["Water"], ["Aqua Jet", "Bulk Up"], "Adds Water-type", "Clobbopus are a resilient species. They live in an element they do not control. With nothing but the strength of their fists, they fight back against a world that tries to crush them. But... perhaps it would be best if they did not fight the world that surrounds them, and learned to use it, instead?"])
    foreveraldex.append(["Tyrogue Everal", "Bea", 3, ForeveralTypes.Training, None, ["Power-Up Punch", "Low Kick"], "Using punching moves increases Defense EVs. Using kicking moves increases Attack EVs.", "Tyrogue are small Pokémon, frequently outclassed by their opponents. Yet they {i}choose{/i} weakness. They purposefully hold themselves back, such that they may become stronger when they finally evolve. The strength of a Hitmon's body is directly correlated to a Tyrogue's strength of will"])
    foreveraldex.append(["Timburr Foreveral", "Bea", 3, ForeveralTypes.AddSTAB, ["Grass"], ["Branch Poke", "Karate Chop"], "Adds Grass-type STAB", "Timburr are known to carry around large pieces of wood with them. This is not an advantage--it is a limiter. They weigh themselves down, give themselves an unnecessary burden. But some of them have learned to use those logs in combat. Isn't that fascinating? Some Timburr have managed to turn their burden into a strength"])
#
    foreveraldex.append(["Eevee Everal", "Blue", 3, ForeveralTypes.AddProficiency, ["Fire", "Water", "Electric", "Grass", "Fairy", "Dark", "Psychic", "Ice"], ["Tackle"], "Gains Proficiency from Fire, Water, Electric, Dark, Psychic, Grass, Ice, and Fairy-types", "You know why Eevee are the best? It's because they can be {i}anything{/i}, if they put the effort in. Any foe can be overcome by an Eevee, if the Eevee just tries. Heck, you could make a team of Eevee evolutions, and that'd be a pretty good team!"])
    foreveraldex.append(["Bagon Everal", "Blue", 3, ForeveralTypes.Scaling, ["Shelgon", 30], ["Aerial Ace", "Headbutt"], "Base stats scale to Shelgon at level 30", "There aren't a ton of dragons that think becoming a dumb cocoon is a good idea before they turn into a badass dragon. Bagon's one of them, though. But you got to admire its tenacity. It'll jump off cliffs, over and over, and over, to get the feeling of flying. It actually {i}works{/i} for its dream! Even if it mostly just hurts itself.."])
    foreveraldex.append(["Cramorant Foreveral", "Blue", 3, ForeveralTypes.TurnStartStatus, ["gorging"], ["Stockpile", "Swallow", "Spit Up"], "Start in Gorging Form", "Hah! I {i}love{/i} Cramorant. The way they just... {i}eat{/i} those stupid rats... it's hilarious! Of course, they never actually consume them... they try to swallow them, but they're just too big. Huh. Biting off more than you can chew with a stupid rat... why does that sound familiar?"])
#
    foreveraldex.append(["Swablu Everal", "Dawn", 3, ForeveralTypes.AddProficiency, ["Dragon", "Fairy"], ["Fairy Wind", "Dragon Rage"], "Gains Proficiency from Dragon and Fairy-types", "U-um... I really like Swablu... because, um, they're... I mean, they're really cute. And the way they hum is so... but, you know? They can become really strong. And they're never afraid to sing. They don't worry about if they sing well, or not well... they just {i}do{/i} it. That's... I want to be like that"])
    foreveraldex.append(["Ninetales Diveral", "Dawn", 3, ForeveralTypes.FormSwap, [38, 38.1], ["Flame Burst", "Icy Wind"], "Swap between Alolan/Kantonian Forms", "Ninetales is a really beautiful Pokémon. And... with every beautiful thing, some people are going to try and take advantage of that. So Ninetales can curse people for a thousand years. It can protect its beauty, and make sure no-one hurts it... I think that's really cool. And, um, hot, too. N-n-not that I find the Pokémon hot! It was a temperature joke! {size=30}I'm sorry.{/size}"])
    foreveraldex.append(["Cryogonal Foreveral", "Dawn", 3, ForeveralTypes.AddAbility, ["Prism Armor"], ["Barrier", "Amnesia"], "Grants Prism Armor", "Cryogonal's a snowflake... and, um, you know what people say about Snowflakes... that they can melt, and... you know. They're not {i}really{/i} special. But Cryogonal's a really strong Pokémon, you know? It's got really good defenses, actually. Well, special defenses. And it's got good special attack. So... I guess it {i}really is{/i} a special snowflake"])
#
    foreveraldex.append(["Darumaka Diveral", "Flannery", 3, ForeveralTypes.FormSwap, [554, 554.1], ["Ember", "Powder Snow"], "Swap between Unovan/Galarian Forms"])
    foreveraldex.append(["Magby Everal", "Flannery", 3, ForeveralTypes.Scaling, ["Magmar", 30], ["Ember", "Smog"], "Base stats scale to Magmar at level 30"])
    foreveraldex.append(["Cubone Everal", "Flannery", 3, ForeveralTypes.AddProficiency, ["Fire", "Ghost"], ["Shadow Punch", "Flame Charge"], "Gains Proficiency from Ghost and Fire-types"])
#
    foreveraldex.append(["Snorunt Everal", "Hilbert", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Hex", "Powder Snow"], "Gains Proficiency from Ghost-type. Male Snorunt can become Froslass"])
    foreveraldex.append(["Dhelmise Foreveral", "Hilbert", 3, ForeveralTypes.MoveBoost, ["Anchor Shot"], ["Aqua Jet", "Aqua Cutter"], "Boosts Anchor Shot. Power: 80 -> 90. Effect: Prevents opponent from switching. {i}Also lowers the opponent's Speed and Attack by one stage.{/i}"])
    foreveraldex.append(["Piplup Everal", "Hilbert", 3, ForeveralTypes.AddProficiency, ["Steel"], ["Bubble", "Mirror Shot"], "Gains Proficiency from Steel-type"])
#
    foreveraldex.append(["Varoom Everal", "Hilda", 3, ForeveralTypes.AddProficiency, ["Fairy", "Dark", "Fighting", "Fire"], ["Low Sweep", "Flame Charge"], "Gains Proficiency from Fairy, Dark, Fighting, and Fire-types"])
    foreveraldex.append(["Aron Foreveral", "Hilda", 3, ForeveralTypes.AddAbility, ["Filter"], ["Iron Defense", "Metal Claw"], "Grants Filter"])
    foreveraldex.append(["Trubbish Foreveral", "Hilda", 3, ForeveralTypes.Scaling, ["Garbodor", 36], ["Discard", "Camouflage"], "Base stats scale to Garbodor at level 36"])
#
    foreveraldex.append(["Nidoran Diveral", "Janine", 3, ForeveralTypes.FormSwap, [29, 32], ["Swagger", "Flatter"], "Swap between Male/Female Forms"])
    foreveraldex.append(["Seviper Foreveral", "Janine", 3, ForeveralTypes.MoveBoost, ["Poison Tail"], ["Brick Break", "Poison Tail"], "Boosts Poison Tail. Power: 50 -> 65. Effect: High crit rate. 10% chance to poison. {i}Creates Toxic Spikes. Double power on Normal-types.{/i}"])
    foreveraldex.append(["Falinks Foreveral", "Janine", 3, ForeveralTypes.AddAbility, ["Simple"], ["No Retreat", "Power-Up Punch"], "Grants Simple"])
#
    foreveraldex.append(["Bidoof Everal", "Professor Cherry", 3, ForeveralTypes.AddProficiency, ["Water"], ["Water Gun", "Super Fang"], "Gain Proficiency from Water-type"])
    foreveraldex.append(["Sunkern Everal", "Professor Cherry", 3, ForeveralTypes.Scaling, ["Arceus", 100], ["Sunny Day", "Mega Drain"], "Base stats scale to Arceus at level 100"])
    foreveraldex.append(["Zigzagoon Diveral", "Professor Cherry", 3, ForeveralTypes.FormSwap, [263, 263.1], ["Headbutt", "Bite"], "Switch between Hoennese/Galarian Forms"])
#
    foreveraldex.append(["Drampa Foreveral", "Leaf", 3, ForeveralTypes.AddAbility, ["Friend Guard"], ["Dragon Rage", "Return"], "Grants Friend Guard"])
    foreveraldex.append(["Tynamo Everal", "Leaf", 3, ForeveralTypes.Scaling, ["Eelektrik", 39], ["Bounce", "Dive"], "Base stats scale to Eelektrik at level 39"])
    foreveraldex.append(["Mareep Everal", "Leaf", 3, ForeveralTypes.AddProficiency, ["Dragon"], ["Dragon Breath", "Cotton Guard"], "Gain Proficiency from Dragon-type"])
#    
    foreveraldex.append(["Larvesta Everal", "May", 3, ForeveralTypes.Scaling, ["Volcarona", 59], ["Flame Charge", "Bug Bite"], "Base stats scale to Volcarona at level 59"])
    foreveraldex.append(["Heracross Megaveral", "May", 3, ForeveralTypes.Mega, ["Heracronite", 214.1], ["Arm Thrust", "Pin Missile"], "Generates Heracronite at start of turn"])
    foreveraldex.append(["Burmy Everal", "May", 3, ForeveralTypes.AddProficiency, ["Steel", "Grass", "Rock", "Flying"], ["Shore Up", "Quiver Dance"], "Gains Proficiency from Steel, Grass, Rock, and Flying classes"])
#
    foreveraldex.append(["Wooper Diveral", "Misty", 3, ForeveralTypes.FormSwap, [194, 194.1], ["Sludge", "Bubble Beam"], "Switch between Johtonian/Paldean Forms"])
    foreveraldex.append(["Frillish Everal", "Misty", 3, ForeveralTypes.Scaling, ["Jellicent", 40], ["Hex", "Will-O-Wisp"], "Base stats scale to Jellicent at level 40"])
    foreveraldex.append(["Castform Foreveral", "Misty", 3, ForeveralTypes.AddProficiency, ["Fire", "Ice", "Water"], ["Sunny Day", "Rain Dance", "Hail"], "Gain Proficiency from Fire, Ice, and Water-types"])
#
    foreveraldex.append(["Bonsly Everal", "Nessa", 3, ForeveralTypes.AddType, ["Grass"], ["Branch Poke", "Ingrain"], "Adds Grass-type"])
    foreveraldex.append(["Binacle Foreveral", "Nessa", 3, ForeveralTypes.AddAbility, ["Sap Sipper"], ["Bug Bite", "Sludge"], "Grants Sap Sipper"])
    foreveraldex.append(["Wishiwashi Foreveral", "Nessa", 3, ForeveralTypes.AddAbility, ["Swift Swim"], ["Shore Up", "Fillet Away"], "Grants Swift Swim"])
#
    foreveraldex.append(["Joltik Everal", "Rosa", 3, ForeveralTypes.Scaling, ["Galvantula", 36], ["Bug Bite", "Electroweb"], "Base stats scale to Galvantula at level 36"])
    foreveraldex.append(["Kricketot Foreveral", "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Uproar", "Sing"], "Adds Normal-type"])
    foreveraldex.append(["Kricketune Foreveral", "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Boomburst", "Perish Song"], "Adds Normal-type"])
#
    foreveraldex.append(["Misdreavus Everal", "Sabrina", 3, ForeveralTypes.Scaling, ["Mismagius", 50], ["Mean Look", "Perish Song"], "Base stats scale to Mismagius at level 50"])
    foreveraldex.append(["Meditite Everal", "Sabrina", 3, ForeveralTypes.Training, None, ["Karate Chop", "Confusion"], "Using fighting moves increases Attack EVs. Using psychic moves increases Special Defense EVs"])
    foreveraldex.append(["Litwick Foreveral", "Sabrina", 3, ForeveralTypes.AddAbility, ["Shadow Tag"], ["Will-O-Wisp", "Hex"], "Grants Shadow Tag"])
#
    foreveraldex.append(["Rhyhorn Foreveral", "Serena", 3, ForeveralTypes.AddAbility, ["Speed Boost"], ["Bulldoze", "Accelerock"], "Grants Speed Boost"])
    foreveraldex.append(["Sandile Foreveral", "Serena", 3, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Fire Fang", "Thunder Fang"], "Grants Strong Jaw"])
    foreveraldex.append(["Litten Everal", "Serena", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Flame Burst", "Bite"], "Gain Proficiency from Dark-type"])
#
    foreveraldex.append(["Zubat Foreveral", "Silver", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Parting Shot"], "Grants Regenerator"])
    foreveraldex.append(["Absol Megaveral", "Silver", 3, ForeveralTypes.Mega, ["Absolite", 359.1], ["Night Slash", "Spirit Break"], "Generates Absolite at start of turn"])
    foreveraldex.append(["Grimer Diveral", "Silver", 3, ForeveralTypes.FormSwap, [88, 88.1], ["Sludge", "Bite"], "Swap between Kantonian/Alolan forms"])
#    
    foreveraldex.append(["Ducklett Foreveral", "Skyla", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Flip Turn"], "Grants Regenerator"])
    foreveraldex.append(["Lapras Gigaveral", "Skyla", 3, ForeveralTypes.Mega, ["Minigiga Laprastar", 131.1], ["Aurora Veil", "Hail"], "Generates Minigiga Laprastar at start of turn"])
    foreveraldex.append(["Nymble Everal", "Skyla", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Parting Shot", "U-turn"], "Gain Proficiency from Dark-type"])
#
    foreveraldex.append(["Yamper Foreveral", "Sonia", 3, ForeveralTypes.AddAbility, ["Fluffy"], ["Bite", "Attract"], "Grants Fluffy"])
    foreveraldex.append(["Comfey Foreveral", "Sonia", 3, ForeveralTypes.MoveBoost, ["Floral Healing"], ["Ingrain", "Wish"], "Boosts Floral Healing. Effect: Heals an ally 50% of their health, or 66% on Grassy Terrain. {i}Also heals the user, and clears status conditions on both{/i}"])
    foreveraldex.append(["Togedemaru Foreveral", "Sonia", 3, ForeveralTypes.AddAbility, ["Rough Skin"], ["Spiky Shield", "Wide Guard"], "Grants Rough Skin"])
#
    foreveraldex.append(["Noibat Foreveral", "Tia", 3, ForeveralTypes.AddSTAB, ["Normal"], ["Uproar", "Sing"], "Grants Normal-type STAB"])
    foreveraldex.append(["Mime Jr. Everal", "Tia", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Draining Kiss", "Powder Snow"], "Gain Proficiency from Ice-type"])
    foreveraldex.append(["Mr. Mime Diveral", "Tia", 3, ForeveralTypes.FormSwap, [122, 122.1], ["Draining Kiss", "Powder Snow"], "Swap between Kantonian/Galarian forms"])
#
    foreveraldex.append(["Munchlax Foreveral", "Whitney", 3, ForeveralTypes.AddAbility, ["Harvest"], ["Slack Off", "Uproar"], "Grants Harvest"])
    foreveraldex.append(["Happiny Everal", "Whitney", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Seismic Toss", "Soft-Boiled"], "Grants Regenerator"])
    foreveraldex.append(["Audino Megaveral", "Whitney", 3, ForeveralTypes.Mega, ["Audinite", 531.1], ["Aqua Ring", "Grassy Terrain"], "Generates Audinite at start of turn"])