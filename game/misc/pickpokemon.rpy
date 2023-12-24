label PickPokemon(choices):#can be a list of ids, or the string "all", or a string of a "Type", or a string of "electives"
    $ beenthrough = False
    hide blank2
    show blank2:
        alpha 0.0
        ease 0.5 alpha 0.8

    label startchoice:

    python:
        alllist = [ 506, 206, 531, 4, 554, 631, 258, 194, 746, 387, 548, 556, 179, 170, 479, 363, 361, 615, 532, 447, 214, 41, 747, 336, 328, 529, 618, 396, 198, 357, 280, 79, 561, 540, 290, 213, 246, 566, 774, 607, 200, 778, 551, 215, 302, 371, 696, 780, 304, 597, 227, 669, 742, 303]
        if (choices != "every"):
            if (not beenthrough):
                if (choices == "all"):
                    choices = alllist
                elif (choices in starters.keys()):#if a "Type" string is passed in
                    choices = starters[choices]
                elif (choices == "electives"):
                    choices = list(starters[getRankStat(0)]) + list(starters[getRankStat(1)])
            
                random.shuffle(choices)
                choices = choices[0:3]
        else:
            choices = alllist

        beenthrough = True

    call screen pickpokemon(choices, _with_none=False) with dissolve
    $ pkmnid = _return
    with dissolve
    hide blackground
    $ pkmnname = pokedexlookup(pkmnid, DexMacros.Name)
    "You chose [pkmnname]?"

    menu:
        ">Yes.":
            return pkmnid

        ">No.":
            jump startchoice