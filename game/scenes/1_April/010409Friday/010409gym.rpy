label gym010409:

############################################################################################################################################################################################################################
#### 3. GYM: BATTLE DEMO ###################################################################################################################################################################################################
############################################################################################################################################################################################################################    

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 450

alder "And that concludes the lecture!"

pause 2.0

alder norm @norm2 "[first_name]. May I have a word?"

red uniform @talkingmouth "Sure thing, Professor."

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
alder happy @happy2 "I've noticed that your [starter_species_name] is getting stronger. Good job!"

$ startergenderpronoun = "he's" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "she's"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "they're"
red @happy "Oh! Uh, thank you, Sir. I don't feel like [startergenderpronoun] any stronger, though."

bruno norm @norm2 "It will be. It has experience now. Soon, it'll be able to make use of it."
alder @happy2 "Right! A few more classes, a bit more studying... And you'll be right there. Speaking of, your assigned partner today is..."

hide alder
hide bruno 
with dis

show nate uniform with dis

red @happy "Hi, Nate!"

$ firstletter = first_name[0]
nate @happybrow "[firstletter]! I wanna see how you battle. Show me a good one, huh?"
red @angrybrow happymouth "I'll do my best. But Bianca's not going to be here to help you out this time."
nate happymouth "Believe me, I'm not going to need that! When my team gets into gear, we take out the trash!"
red @confusedeyebrows frownmouth "...Wait, what's with that grin?"

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("nate", TrainerType.Enemy, [
    Pokemon(568, level=5, gender=Genders.Female, ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Impish, moves=[GetMove("Pound"), GetMove("Poison Gas")], ability="Aftermath"),#Trubbish
    Pokemon(599, level=5, gender=Genders.Unknown, ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Adamant, moves=[GetMove("Vise Grip")], ability="Clear Body")])#Klink

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_6
$ gymbattles["Nate1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show nate uniform at rightside with dis

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

python:
    klinkfainted = False
    for mon in trainer2.GetTeam():
        if (mon.GetHealth() == 0):
            klinkfainted = True
    
if (not klinkfainted):
    nate @closedbrow happymouth "Aw... you missed my pun! See, my second Pokemon was a Trubbish. Get it? Gears? Trash?"

red uniform frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talking2mouth "Did you think that was funny?"

nate happy "Yes, absolutely! The expression on your face as you realized... hahahahaha!"

red @talkingmouth "Tell me you didn't create that team just to make that pun."

nate -happy @talkingmouth "Nah, I wouldn't go {i}that{/i} far. I made the team, {i}then{/i} thought up the pun."

red @talking2mouth "That's...{w=0.5} very slightly better."

if (WonBattle("Nate1")):
    nate @angrymouth closedbrow "Anyway, I'm kinda annoyed at myself for losing... but, hey, these are brand-new Pokémon."

    nate @happy "So, what's your secret? You were in perfect sync with your 'mon the whole time! No way that's your school-given starter, right?"

    red @closedeyes talkingmouth "Man, you wouldn't believe me if I told you my secret."

    nate @talkingmouth "That's cool. Some secrets just gotta stay that way, right? I respect that."

    $ ValueChange("Nate", 3, 0.75)

    nate @talkingmouth "See you 'round, [firstletter]."

else:
    nate @angrymouth closedbrow "Anyway, that was a good battle. Train up a bit for next time. Didn't even get to bust out my secret strats this time..."

    red @angrybrow talking2mouth "Believe me, I will. I'm not losing to you again."

    nate @happy "Looking forward to it, [firstletter]!"

jump lunchtransition