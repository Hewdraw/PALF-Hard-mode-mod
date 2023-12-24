label wildarea(newloc):

stop music fadeout 2.5

$ location = newloc

if (location == "fields"):
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
    show blank2 as blackground behind map
elif (location == "alley"):
    $ renpy.music.queue("audio/music/alley.mp3", channel='music', loop=None)
    show abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)
    show blank2 as blackground behind map
elif (location == "seaport"):
    $ renpy.music.queue("audio/music/seaport.mp3", channel='music', loop=None)
    scene seaport with Dissolve(2.0)
    show blank2 as blackground behind map

show screen currentdate
hide blackground
with dissolve
    
label afterwildareasetup:
$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)
if (not trainer1.HasMons()):
    narrator "You quickly sprint back to campus, protecting your hurt and fainted Pokemon from further harm."
    $ location = "school"
else:
    $ subtitle = ""
    if (wildcount != 0):
        $ subtitle = " Consecutive battles won: {}".format(wildcount)

    menu:
        "{b}>Go Exploring!{/b}[subtitle]":
            $ GenerateRandomEvent(location)
            call wildarea(location) from _call_wildarea_1

        ">Head back to campus":
            narrator "Are you sure you want to head back to campus? Doing so will end this free time."

            if (wildcount != 0):
                $ expvalue = 5
                if (location == "alley"):
                    $ expvalue = 9
                elif (location == "seaport"):
                    $ expvalue = 12
                $ exptotal = math.floor(pow(expvalue, 3) / 25 * min(3, (1 + wildcount / 10)))
                narrator "You have won [wildcount] consecutive battles, so your party will gain [exptotal] experience each. (There are no bonuses after 20 consecutive battles.)"

            menu:
                "Yes, I'm sure.":
                    call clearscreens from _call_clearscreens_64
                    python:
                        if (wildcount != 0):
                            for mon in playerparty:
                                mon.GainExperience(exptotal)
                        if (wildcount > highestwildcount):
                            highestwildcount = wildcount
                        wildcount = 0
                        location = "school"
                    show screen currentdate with dis
                    pass

                "Never mind.":
                    jump afterwildareasetup
return

init python:
    def GrabFromEncounterPool(encounterpool):
        encounterlist = []
        encountermax = 0
        for entry in encounterpool.keys():
            encounterlist.append((encountermax, entry))
            encountermax += encounterpool[entry]
        encounterlist.append((9999, 0))
        
        randnum = RandInt(0, encountermax)
        for i in range(len(encounterlist)):
            if (randnum <= encounterlist[i + 1][0]):
                return encounterlist[i][1]

    def GenerateRandomEvent(location):
        global sidemonnum
        global activerepel
        global repelstepsleft
        #events = []
        #generate more random events through this
        encounterpool = {}
        levelrange = range(3, 10)
        if (location == "fields"):
            encounterpool = {
                263: 10,
                155: 3,
                399: 10,
                191: 10,
                835: 10,
                133: 1,
                919: 10,
                406: 7,
                29: 7,
                32: 7,
                333: 7,
                307: 7,
                401: 10,
                111: 5,
                710: 5,
                659: 10,
                967: 3,
                777: 7,
                764: 7
            }
        elif (location == "alley"):
            levelrange = range(6, 12)
            encounterpool = {
                431: 10,
                725: 1,
                767: 10,
                412.2: 10,
                81: 10,
                351: 1,
                559: 7,
                568: 10,
                104: 7,
                629: 7,
                677: 7,
                917: 10,
                744: 3,
                353: 10,
                88.1: 10,
                714: 5,
                965: 5,
                439: 5
            }
        elif (location == "seaport"):
            levelrange = range(9, 15)
            encounterpool = {
                190: 10,
                58: 7,
                223: 10,
                781: 1,
                602: 3,
                131: 1,
                852: 7,
                690: 7,
                194.1: 10,
                580: 10,
                976: 5,
                595: 7,
                688: 10,
                592: 5,
                592.1: 5,
                318: 7,
                885: 3,
                393: 3,
                183: 10
            }
        trainer1 = Trainer("red", TrainerType.Player, playerparty)
        newpokemonnum = GrabFromEncounterPool(encounterpool)
        newpokemon = Pokemon(newpokemonnum)
        minlevel = levelrange[0]
        maxlevel = levelrange[len(levelrange) - 1]
        if (activerepel == "Repel"):#Pokemon in the lower half of the level range won't show up
            levelrange = range(math.floor(minlevel + (maxlevel - minlevel) / 2), maxlevel)
        elif (activerepel == "Super Repel"):
            levelrange = [maxlevel]#Pokemon that appear will be at the maximum level
        elif (activerepel == "Max Repel"):
            levelrange = range(max(maxlevel, GetHighestLevel() - 6), max(maxlevel + 1, GetHighestLevel()))#Pokemon will appear up to your highest-leveled 'mon

        newpokemon.UpdateLevel(RandomChoice(levelrange))
        newpokemon.Heal()
        sidemonnum = newpokemonnum
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [newpokemon], isPokemon=True)

        repelstepsleft -= 1
        if (repelstepsleft == 0):
            activerepel = None

        renpy.call("Battle", [trainer1, trainer2], healParty=False, specialmusic=("Audio/Music/RBY_Pokemon_Start.ogg", "Audio/Music/RBY_Pokemon_Loop.ogg"))