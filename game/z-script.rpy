# The game starts here.
label start:
$ _game_menu_screen = "game_menu"
$ yvalue = 1.0

jump prologue

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

scene bg room

# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

show red angry uniform

show mom angryeyes angryeyebrows sadmouth at leftside

show oak angrybrow happymouth at rightside

# These display lines of dialogue.

e "You've created a new Ren'Py game."

e "Once you add a story, pictures, and music, you can release it to the world!"

label testbattle:
$ newparty = [Pokemon("Sneasel", level=50, moves=[GetMove("Infestation"), GetMove("Power-Up Punch"), GetMove("Bullet Seed"), GetMove("No Retreat")], ability="Gorilla Tactics", foreverals=["Comfey Foreveral"]), 
    Pokemon("Meditite", level=1, moves=[GetMove("Confusion"), GetMove("Karate Chop"), GetMove("Splinter Shield"), GetMove("Ingrain")], foreverals=["Meditite Everal"]),
    Pokemon(25.2, nickname="Mimikyu", moves=[GetMove("Confusion"), GetMove("Karate Chop"), GetMove("Shadow Sneak"), GetMove("Round")], foreverals=["Meditite Everal"]),
    Pokemon(774, nickname="Minior3", moves=[GetMove("Teleport"), GetMove("Leech Seed"), GetMove("Uproar"), GetMove("Mist")]),
    Pokemon(568, level=3, gender=Genders.Female, moves=[GetMove("Pound"), GetMove("Poison Gas")], ability="Aftermath")]

$ trainer1 = Trainer("red", TrainerType.Player, newparty, number=1)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [Pokemon(pokedexlookupname("Tyrunt", DexMacros.Id), moves=[GetMove("Splash")], ability="Mold Breaker", level=100, intelligence = 1)])

call Battle([trainer1, trainer2], currentWeather=("sunny", 3)) from _call_Battle_11

red "End of battle."

# This ends the game.

return

label randombattle:

if (not persistent.testwarning):
    narrator "This testing feature may contain massive spoilers for game content, including characters and Pokémon. Are you sure you want to use it?"

    menu:
        "Yes, and don't warn me again.":
            $ persistent.testwarning = True
            pass

        "Never mind.":
            return

show stadium_empty

show screen abortbattletester

python:
    testbattle = True
    random.seed()
    numallies = random.randint(1, 3)
    numfoes = random.randint(1, 3)
    allynums = (1 if numallies != 1 else random.randint(1, 3))
    foenums = (1 if numfoes != 1 else random.randint(1, 3))
    trainers = []

    for i in range(numallies):
        teamnumber = random.randint(1, 6)
        newteam = []
        for i in range(teamnumber):
            newteam.append(Pokemon(random.choice(GetAllPokemonIn()), level = random.choice(range(5, 15))))
        random.seed()
        newtrainer = Trainer(random.choice(list(classdex.keys())).lower(), (TrainerType.Player if len(trainers) == 0 else TrainerType.Ally), newteam, allynums)
        trainers.append(newtrainer)

    for i in range(numfoes):
        teamnumber = random.randint(1, 6)
        newteam = []
        for i in range(teamnumber):
            newteam.append(Pokemon(random.choice(GetAllPokemonIn()), level = random.choice(range(5, 15))))
        random.seed()
        newtrainer = Trainer(random.choice(list(classdex.keys())).lower(), TrainerType.Enemy, newteam, foenums)
        trainers.append(newtrainer)

call Battle(trainers, gainexp=False) from _call_Battle_42

$ testbattle = False

red "End of battle."

return
