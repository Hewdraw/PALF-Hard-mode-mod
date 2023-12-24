label gym010406:

$ timeOfDay = "Noon"

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

show alder norm2:
    xpos 0.66 alpha 0.0
    ease 0.75 alpha 1.0

show bruno think:
    xpos 450 alpha 0.0
    pause 0.25
    ease 0.75 alpha 1.0

alder "Welcome back, everyone.{w=0.5} Are you all ready for a productive day here in the gym?"
alder happy2 "Well, it really doesn't matter if you are, because you're gonna have one whether you like it or not.{w=0.5} That's what the school pays us to make you do, ha ha!"
alder norm2 "I'll bet all of you are wondering just exactly what I'm talking about."
alder spunky2 "Well, I'll show you."

show bruno think:
    xpos 450
    ease 0.7 xpos 200

show alder norm2:
    xpos 0.66
    ease 0.5 xpos 600
    
alder "Come on out!"

show alder norm:
    xpos 600

$ renpy.music.play("Audio/Pokemon/Volcarona_Ball.ogg", channel="altcry", loop=None)

image volcarona:
    "Pokemon/637.webp"

show volcarona at pokeball behind alder:
    xpos 800 + 800 ypos 1080 zoom 1.8

$ renpy.pause(1.0, hard=True)

show volcarona:
    subpixel True
    zoom 1.8 ypos 1080 xpos 800 + 800
    block:
        parallel:
            ease 1.0 ypos 900
            ease 1.3 ypos 1040
            ease 0.9 ypos 930
            ease 1.5 ypos 1080
            ease 1.2 ypos 905
            ease 1.4 ypos 1160
        parallel:
            ease 0.8 xpos 750 + 800
            ease 1.4 xpos 825 + 800
            ease 1.1 xpos 860 + 800
            ease 1.6 xpos 830 + 800
            ease 1.25 xpos 775 + 800
            ease 1.3 xpos 800 + 800
        repeat

show bruno think:
    xpos 200

pause 1.0

blue uniform surprised "A Volcarona--?!"

hilbert uniform @talkingmouth "As expected from one of the previous World Champions..."

bianca uniform "Wow--!{w=0.5} {cps=200}That's so cool! Oh gosh, look at its wings, they're, like, the prettiest things I've ever seen!{/cps}{w=0.4}"
show alder happy with dis
bianca @happy "Can I take a picture real quick?"

may uniform angrybrow ".{w=0.2}.{w=0.2}.{w=0.2}I'm going to get a Volcarona."

alder norm2 "Settle down, class, I'm only using her as a demonstration."
alder norm2 "Bruno, bring out the dummy."
show alder norm with dis

show bruno norm:
    xpos 200 alpha 1.0
    ease 0.5 xpos -100 alpha 0.0

pause 1.5

show balloonbot:
    subpixel True
    alpha 0.0 yalign 0.5 xpos -0.5#    xalign -2.0
    parallel:
        ease 0.9 xpos 0.05
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

show bruno norm:
    xpos -100 alpha 0.0
    parallel:
        ease 0.75 xpos 200
    parallel:
        ease 0.5 alpha 1.0

pause 1.0

show bruno norm2:
    alpha 1.0 xpos 200

show balloonbot:
    alpha 1.0
    block:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

bruno "Is this good?"
show bruno norm with dis
alder norm2 "That's perfect."
show alder norm

calem uniform @surprised "A balloon bot?{w=0.5} Are we Super Training today?"

hide ethan
ethan uniform @thinking "'Super Training?'{w=0.5} That sounds like something straight out of a video game."

alder happy2 "Ha ha, no, not today. It's still too early in the semester for that.{w=0.5}{nw}"
extend alder norm2 " Today, it'll be something a little simpler."
show alder norm with dis

ethan @surprised "So Super Training is a real thing...?"

show bruno think with dis
alder happy2 "Let's get started!"

hide alder          
hide bruno
hide volcarona
hide balloonbot
with dis

$ aldervolcaronaobj = Pokemon(pokedexlookupname("Volcarona", DexMacros.Id), ivs=[31, 14, 31, 31, 31, 31], evs=[0, 0, 4, 252, 252, 0], nature=Natures.Timid, gender=Genders.Female, level=85, moves=[GetMove("Bug Buzz"), GetMove("Quiver Dance"), GetMove("Flamethrower"), GetMove("Hurricane")], item="Heavy-Duty Boots", ability="Flame Body")

$ trainer1 = Trainer("alder", TrainerType.Player, [aldervolcaronaobj])
$ trainer2 = Trainer("bruno", TrainerType.Enemy, [Pokemon(pokedexlookupname("Balloon Bot", DexMacros.Id), level=70, moves=[GetMove("Splash")], gender="Unknown")])

call Battle([trainer1, trainer2], customexpressions=["alder", "alder spunky2", "bruno", "bruno angry3"], reanchor=[False, True], gainexp=False) from _call_Battle_1

stop music fadeout 1.0
pause 1.0

show alder norm3 with dis:
    xpos 0.75

show bruno think with dis:
    xpos 450

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

$ _game_menu_screen = "game_menu"

hide blank2

show alder norm4
alder "Now... who was it that said 10-year-olds can get by here.{w=0.25}.{w=0.25}.{w=0.7}{nw}"

extend happy2 " Ah-ha, there you are."

show alder norm:
    xpos 0.66
    ease 0.75 xpos 600

show bruno norm:
    xpos 450
    ease 1.0 xpos 50

show blue uniform:
    alpha 0.0 xpos 1500
    ease 0.5 alpha 1.0 xpos 1370

$ renpy.pause(1.0, hard=True)

show bruno think with dis
alder norm3 "Hmm..."
alder norm2 "Oh, that's right!{w=0.5} You're the one interested in joining the academy's Battle Team."

show blue angry with dis

alder "Are you serious about that, boy?"
show alder norm with dis

show bruno norm with dis

blue @talkingmouth angrybrow "Yeah, that's right!{w=0.5} Why wouldn't I be?"

blue @happybrow "It's obviously the perfect stepping stone for me and becoming World Champion!"
show blue -angry with dis

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=0.5)
pause 1.5

alder "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend norm2 " so that's your goal.{w=0.5} World Champion."

alder norm "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend happy2 " I'm sorry, there's a whole lot of you in this class and I haven't memorized everyone's names yet."

alder norm2 "You are?"
show alder norm with dis

blue @talkingmouth "Blue."

redmind uniform "I'm surprised he didn't include his last name.{w=0.5} I bet it could've at least triggered some response from Alder or Bruno."

alder norm2 "You! In the red hat!"
show alder norm with dis

red "H-Huh?"

calem uniform "He's definitely not looking at me."
hilbert uniform "Nor me."
bianca happy uniform "Right? It's confusing, isn't it?"

red "Uh, Sir?"

show blue surprised with dis

alder happy2 "Yes! Yes, you.{w=0.5}{nw}"    
extend norm2 " What's your name?"
show alder norm with dis

show blue -surprised with dis

red "Uh, [first_name]. [first_name] [last_name]."

show blue surprised with dis
alder happy2 "[first_name]!{w=0.6} Why don't you and Blue have a spar right here in front of your fellow classmates?"
show alder happy with dis

show blue happybrow with dis

red surprised "What?"

show bruno think with dis
alder happy2 "You heard me."
show alder happy with dis

show blue:
    xpos 1370
    ease 0.5 xpos 1300

blue @happy "Perfect!{w=0.5} I've been waiting for this!"
show blue -happy with dis
    
ethan uniform surprised "Oh, geez, Alder's really going to make you do it? Guess he doesn't know about your history with [blue_name]."
ethan happy "Still, you've got this!"

calem uniform happy "Good luck, [first_name]. I trust in your ability."
brendan uniform happy "Kick his ass, bro!"
may uniform happy "We're all cheering for you!"
hilbert uniform angrybrow "Don't you dare disgrace our dorm."
serena uniform happymouth closedbrow "Please, give us a show."
leaf uniform "First battle of the new school year? You better make this count."
leaf flirt "No pressure."

ethan -happy "You wanna borrow my [species_name], [first_name]?"

red "I...{w=0.5} think I can handle this."

ethan happy "You're the boss!"

show alder happy:
    alpha 1.0 xpos 600
    ease 0.5 alpha 0.0            
show bruno think:
    alpha 1.0 xpos 50
    ease 0.5 alpha 0.0
show blue:
    alpha 1.0 xpos 1300
    ease 0.5 alpha 0.0
    
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [Pokemon(pokedexlookupname("Eevee", DexMacros.Id), level=5, ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Adamant, moves=[GetMove("Tackle"), GetMove("Covet"), GetMove("Tail Whip"), GetMove("Growl")], gender=Genders.Male, ability="Adaptability")])#Eevee

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_2
$ gymbattles["Blue1"] = _return

show blank2:
    alpha 1.0

stop music fadeout 1.0
pause 1.0

show alder norm behind blank2:
    alpha 0.0 xpos 600
    ease 0.5 alpha 1.0

show bruno norm behind blank2:
    alpha 0.0 xpos 50
    ease 0.5 alpha 1.0
    
if WonBattle("Blue1"):
    show blue uniform angry behind blank2:
        alpha 0.0 xpos 1300
        ease 0.5 alpha 1.0
else:
    show blue uniform behind blank2:
        alpha 0.0 xpos 1300
        ease 0.5 alpha 1.0

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)


hide blank2

if WonBattle("Blue1"):
    show blue:
        alpha 1.0 xpos 1300
        ease 0.5 xpos 1400

    blue @talkingmouth "N-No way!{w=0.5} I was just careless!"
    red uniform @happy "Great job, [starter_name]!"

else:
    show blue:
        alpha 1.0 xpos 1300
        ease 0.5 xpos 1400

    blue @talkingmouth "Yeah! Am I great or what?"
    red uniform @sad "Oh, no... I'm sorry, [starter_name]."

alder happy2 "Nicely done! That was a good battle.{w=0.5}{nw}"
extend norm2 " You both should be proud of yourselves and your Pokémon."

alder "Speaking of which, let's get them fixed up."
show alder norm with dis

pause 0.5

$ renpy.music.set_volume(0.0, delay=0.0, channel="music")
play sound "Audio/recovery.ogg"
$ HealParty()
pause 2.5
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show alder norm2:
    ease 0.5 xpos 0.75

show bruno norm:
    xpos 50
    pause 0.5
    ease 1.0 xpos 450


hide blue with dis

alder "Once again, thank you, Blue and [first_name], for showing us a fine Pokémon battle.{w=0.5}{nw}"

extend norm2 " The Pokémon certainly looked like they were enjoying themselves."

alder "Remember to always keep this in mind. Pokémon battles aren't just about winning.{w=0.5} What matters most is how you and your Pokémon work together as a team."
show alder norm with dis

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show bruno think with dis
alder happy2 "And that'll be all for today.{w=0.5} Enjoy the rest of your day!"
show alder norm with dis

show blank2 with dis:
    alpha 1.0

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_17 

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

jump lunch010406