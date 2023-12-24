label poisonelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0

show poisontype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "poison"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. POISON    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call nateevent from _call_nateevent_1
call silverevent from _call_silverevent_1
call hildaevent from _call_hildaevent
call erikaevent("Poison") from _call_erikaevent
call ethanevent from _call_ethanevent_13

label afterpoisonsetup:

if (2.1 in persondex["Instructor Koga"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorpoison

        ">Craft items" if (3.1 in persondex["Instructor Koga"]["ClassesKnown"]):
            jump itemcraftpoison

if (persondex["Instructor Koga"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Koga"]["ClassesKnown"].append(1)
    $ renpy.pause(3.0, hard=True)

    red uniform thinking "I wonder where the teacher is?"
    ethan uniform happy "Did you know that if the teacher isn't here in fifteen minutes, you're legally allowed to leave?"
    red -thinking "Well, yeah. There's no law saying we can't leave before fifteen minutes, either."
    red @confusedeyebrows "Although... I guess maybe Kobukan might have something weird like that? Probably not, though."

    stop music fadeout 0.5
    play sound "Audio/Whoosh.ogg"

    show koga with dis:
        alpha 0.3 matrixcolor TintMatrix("#424243")
        ease 1.0 alpha 1.0 matrixcolor TintMatrix("#fff")
    show smoke:
        alpha 0.0 xpos 0.5 yalign 3.0
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0

    $ renpy.pause(1.0, hard=True)

    show koga thinking with dis

    play music "Audio/Music/Kimono_Start.ogg" noloop
    queue music "Audio/Music/Kimono_Loop.ogg"

    red @surprised "Whoa!"

    ethan @surprised "Was this guy here the whole time?!"
        
    koga @talkingmouth "Welcome to the {color=#0048ff}Poison class,{/color} children!"
    $ BecomeNamed("Instructor Koga")
    koga @talkingmouth "I am your instructor, Koga!"

    play sound "Audio/Whoosh.ogg"
    
    show koga:
        alpha 1.0 matrixcolor TintMatrix("#fff")
        ease 1.0 alpha 0.0 matrixcolor TintMatrix("#424243")
    show smoke:
        alpha 0.0 xpos 700 yalign 3.0
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0

    $ renpy.pause(1.0, hard=True)

    show kogabg:
        alpha 0.0 yalign 1.0 xalign 0.5
        pause 0.5
        ease 0.5 alpha 1.0

    $ renpy.pause(2.0, hard=True)

    ethan surprised "What is this guy, some kind of ninja?"

    hide koga
    hide smoke
    hide smokey

    koga "I am not only a master of Poison-type Pokémon, but also a master of ninjutsu!"

    ethan thinking "Of course..."

    koga "You are here because you expect me to teach you about Poison Pokémon.{w=0.5} In that, you are correct."
    koga "But that is not all I will teach you!"
    koga "I shall teach you the importance of the human and Pokémon mind, and how easy they are to manipulate!"
    koga "Let me start this class with a simple question to you."
    koga "What makes a Pokémon strong?"

    ethan "This sounds like a trick question, but it's gotta be--"

    "Rude Student" "\"The Pokémon's level, duh!\""
    "Rude Student" "\"Is that even a real question?\""

    koga "Fwahahaha! And how can you be so sure?"

    "Rude Student" "\"What? Its combat potential will be higher, obviously!\""
    "Rude Student" "\"How can you be a teacher and not know that?\""
    "Rude Student" "\"Speaking of which, what kind of teacher is late to class?{w=0.5} I thought this was an elite university!\""

    show kunai:
        alpha 1.0 zoom 0.0 xpos 900 ypos 460
        ease 0.3 zoom 0.6 xpos 2000 ypos 640
    pause 0.15
    play sound "Audio/LightTap.ogg"

    $ renpy.pause(0.5, hard=True)
    ethan @surprised "Holy shuriken!"
    red @thinking "I think that was a Kunai, actually."

    "Rude Student" "\"...!\""

    hide kunai

    show poisclass:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 2
        parallel:
            yalign 0.0
            ease 0.03 ypos -25
            ease 0.03 ypos 25
            ease 0.03 ypos 0
            repeat 2

    koga "FOOL! If you understood Pokémon then you would have understood why I remained hidden!"
    koga "Can anyone guess why?"
    koga "I'll give you a hint:{w=0.5} it is more important than strength, technique, skill... all of that!"

    hide poisclass
    pause 1.5

    koga "Nobody knows? Well, then..."

    show hildaintro:
        subpixel True
        alpha 0.0 xalign 0.5 zoom 1.0
        parallel:
            ease 1.5 alpha 1.0
        parallel:
            ease 5.0 zoom 0.75


    hilda uniform "Is it knowing your opponent before the encounter?"

    koga "Go on."

    hilda @talkingmouth "Like, you analyze their weak points and capabilities beforehand so you don't have to make things up on the fly."

    pause 1.0

    koga "...YOU!"

    hilda @surprised "Wh-what?"

    if (IsDate(5, 4, 2004)):
        koga "What is your name?"

        hilda "Hilda, Sir."

    koga "Explain your thinking, Hilda!"

    hilda "It's really self-explanatory.{w=0.5} If you engage a Pokémon or a Trainer without knowing anything about them, you're immediately putting yourself at a disadvantage."
    hilda "It's Pokémon battling 101."

    koga "Hilda is correct!"

    show hildaintro:
        alpha 1.0
        ease 1.0 alpha 0.0

    koga "Pokémon are not merely about brute strength!{w=0.5} You must understand your opponent's strengths, weaknesses, their mentality."
    koga "If you know these things, even the weakest Pokémon can defeat the strongest!"
    koga "On the field, you must exploit every possible advantage you can get!"
    koga "If there are none in sight, then you must make them yourself."
    koga "Confusion... poison... sleep...{w=0.5} all tools to gain the upper hand, and all signature tools of Poison-type Pokémon."
    koga "You shall learn soon enough!"

    hide hildaintro

    ethan happy "This guy is making it sound like we're going to assassinate someone rather than just study Pokémon."
    red "Yeah... but why do you look so happy about that?"

    pause 2.0

    narrator "Koga lectures on the many ways the weak may uproot the strong."

    pause 2.0

    koga "Ah! Has it been one hour already?"
    koga "Very well, you are dismissed!"

    hide koga
elif (2.1 not in persondex["Instructor Koga"]["ClassesKnown"] and classstats["Poison"] >= 10):#Bad Breath
    show koga with dis
    if (2 not in persondex["Instructor Koga"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "You're busy studying the anatomy of a wide array of Pokémon, when Instructor Koga suddenly materializes next to you."

        koga smilemouth @happy "Fwahahaha! You are progressing well within your studies!"

        red @happy "Thanks, Instructor."

        koga @talking2mouth "I pose a question to you, now--why do I have you studying Pokémon anatomy?"

        red @thinking "Hm... well, you have us studying Poison-types because that's what you're paid to do. But you have us studying the other types as well, because..."
        red @talkingmouth "Understanding other types gives us a better idea of how to shut down their capabilities, I think. Is that right?"

        koga @happy "Fwahaha! You are very astute, my pupil. Yes, that's right."
        koga @talkingmouth "When you understand your opponent's strengths, you understand how to make them weak." 
        koga @thinking "Never assume you're prepared for a fight because you're confident in your {i}own abilities.{/i}"
        koga @talking2mouth "You must also be confident in your knowledge of your opponent's abilities. It is knowledge and preparation that wins battles, not brute strength."

        red @angrybrow talkingmouth "I agree completely."

        koga @talkingmouth "Hm! Then you are ready to advance in this class."

        red @surprised "Oh, really? So, you can teach me some new stuff?"

        koga @closedbrow talking2mouth "Yes. The ultimate debilitating effect, created by practitioners of Ninjutsu years ago. {i}Bad Breath.{/i}"

        red @thinking "What does that do?"

        koga @closedbrow talking2mouth "If the opponent can be badly poisoned, it will be. If the opponent cannot, it will be paralyzed. And if it cannot be paralyzed, it will be confused."

        red @surprised "Woah?! A move with multiple effects?! How does that work?"

        koga @closedbrow talking2mouth "It is a secret shinobi technique. Do not worry about it."

        red @thinking "That sounds familiar."

        koga @angry "I will now administer the advancement exam--a one-on-one battle against me, a ninja master! Are you prepared?"

        red @happy "Absolutely, Sir!"

        $ persondex["Instructor Koga"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "The battle's outcome is decided as soon as you choose your Pokémon. Now, which will it be? {color=#0048ff}A Poison-type will excel in this conflict.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @angry "Attack with all you have!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon(546, level=11, moves=[GetMove("Absorb"), GetMove("Fairy Wind"), GetMove("Stun Spore")], ability="Prankster")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "koga", "koga angry"], reanchor=[False, True]) from _call_Battle_37
    $ gymbattles["Instructor Koga1"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga1")):
        $ persondex["Instructor Koga"]["ClassesKnown"].append(2.1)

        koga @happy "I am proud. You have clearly learned well. Fwahahaha! Fine, I will teach you my technique!"

        $ passedclass = True
        jump aftertutorintropoison
    
    else:
        koga @sad "Ah."
        koga @talkingmouth "An unexpected outcome. I am certain you will return to remedy this, however! Do not let up on your training!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis
elif (3.1 not in persondex["Instructor Koga"]["ClassesKnown"] and classstats["Poison"] >= 20):#Poison Barb
    show koga with dis
    if (3 not in persondex["Instructor Koga"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        koga @happy "Fwahahaha! You, [first_name]! Tell me, what are the seven tools of the bandit?"

        red uniform @surprised "I am absolutely certain that you have never told us that."

        koga @closedbrow talking2mouth "Clearly. If I already knew the answer, I wouldn't be asking you!"

        red @surprised "Um."

        pause 1.0

        red @thinking "Just... going on a limb here... a knife, a lockpick, a screwdriver, a chisel, a corkscrew, and a cyanide capsule?"

        koga @angry "That is only six tools!"

        red @thinking "Well, yeah, the seventh one is a secret."

        pause 1.0

        koga @happy "You are wise beyond your years, [last_name]-san. I see my daughter was not incorrect to place you within her Battle Team."

        red @surprised "Oh, right! I completely forgot you were Janine's Dad. Um, can I ask you questions about her?"

        koga @closedbrow talking2mouth "Hm... I will permit this. I am her father, after all, and it is my ninja duty to share embarrassing baby stories about her."

        red @surprised "Do you have pictures?"

        koga @happy "Many pictures, yes. Photography is one of the ninja arts."

        red @happy "So... we're in class, now, but can I, like, come to your office hours and we can gossip?"

        koga @closedbrow talking2mouth "This is acceptable."

        show koga with vpunch

        koga @angry "However! Before I am to share this confidential information, I would ask you to prove yourself worthy of it!"

        red @thinking "Would passing another class advancement exam qualify?"

        koga @closedbrow talking2mouth "Yes. And, in doing so, I will teach you how to make the secret Ninja artifact--the Poison Barb! It will increase the power of your Poison-type moves by 10%%!"

        red @happy "Cool."

        red @talkingmouth "I'm ready now, Sensei."

        pause 1.0

        show koga closedbrow talking2mouth with dis

        "{color=#5f3869}Sensei Koga{/color}" "Please do not call me Sensei. I'm not that weeaboo, Marshal. Just 'Instructor' works fine, thank you."

        show koga -closedbrow -talking2mouth with dis

        red @sweat happy "Oops! Noted."

        $ persondex["Instructor Koga"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "Pick, then, the Pokémon you will be using in this trial of Ninjutsu. [bluecolor]I will be relying on the insidious powers of the Poison-type, myself.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @angry "Attack with all you have!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon("Venonat", level=21, moves=[GetMove("Psybeam"), GetMove("Poison Powder"), GetMove("Supersonic"), GetMove("Venoshock")], ability="Compound Eyes", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "koga", "koga angry"], reanchor=[False, True]) from _call_Battle_100
    $ gymbattles["Instructor Koga2"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga2")):
        $ persondex["Instructor Koga"]["ClassesKnown"].append(3.1)

        koga @happy "I am proud. You have clearly learned well. Fwahahaha! Fine, I will teach you my technique!"

        $ GetItem("Poison Barb", 1, "Koga snaps his fingers and, in a puff of smoke, a Poison Barb appears in your hands.")
        
        jump aftertutoring
    
    else:
        koga @sad "Ah."
        koga @talkingmouth "An unexpected outcome. I am certain you will return to remedy this, however! Do not let up on your training!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis
elif (4.1 not in persondex["Instructor Koga"]["ClassesKnown"] and classstats["Poison"] >= 30):#Venoshock
    show koga with dis
    if (4 not in persondex["Instructor Koga"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        koga @happy "Fwahahaha! [first_name], I would ask you a question!"

        red @confused "Is it another thing I don't know the answer to, like your tools of the bandit question?"

        koga @closedbrow talking2mouth "No, this one is something I believe you have the power to understand by yourself."

        koga @talkingmouth "I have told you what strength is, yes?"

        red @talkingmouth "Yes. You've said it's versatility."

        koga @happy "Correct. Versatility, and the ability to capitalize on an opponent's weakness."

        koga @angry "What, then, is 'weakness', beyond something to be capitalized on?"

        red @thinking "That's a tough one. If strength is versatility, then it'd be easy for me to say that weakness is just its opposite. Single-mindedness, or something like that."
        red @confused "But that feels a bit too easy for this class. All your questions are trick questions, with, like, three layers of trickery to them."

        koga @happy "You have picked up on that, then! Good. You learn well."

        red @thinking "Right..."
        red @confused "So, I guess my final answer is... uh... also versatility."

        koga @surprised "Oh?"

        red @thinking "Well, not versatility {i}itself.{/i} But the answer is versatile. Like, weakness isn't one specific thing that you can seek out and utilize in every single foe."
        red @talking2mouth "Every foe has a different weakness. Right?"

        pause 1.0

        koga closedbrow frownmouth @closedbrow talking2mouth "Hm."

        pause 1.0

        red @sweat happy "Uh... Instructor Koga? You're not giving me much to go on here."

        koga happy @happy "Your answer is correct enough."
        koga @talkingmouth "You are right, that every foe has a different weakness. So you cannot exploit every weakness the same way." 
        koga @closedbrow talking2mouth "I would contend that there are some things that almost all weaknesses share, as common traits, but perhaps that is an advanced lesson."

        red @thinking "Advanced lesson... oh, so can I take the advancement exam?"

        koga @talkingmouth "Yes. Passing it will grant you the ability to teach your Pokémon the move Venoshock. I'm sure I don't have to tell you that its power doubles when used on a poisoned foe."

        red @talking2mouth "No, Sir, you don't. I'm ready to take the exam now."

        $ persondex["Instructor Koga"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "Good. Now, pick your Pokémon. [bluecolor]I recommend not picking a Poison-type for this fight.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @angry "Attack with all you have!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon("Bronzor", level=31, moves=[GetMove("Extrasensory"), GetMove("Safeguard"), GetMove("Hypnosis"), GetMove("Gyro Ball")], ability="Levitate", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "koga", "koga angry"], reanchor=[False, True]) from _call_Battle_101
    $ gymbattles["Instructor Koga3"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga3")):
        $ persondex["Instructor Koga"]["ClassesKnown"].append(4.1)

        koga @happy "I am proud. You have clearly learned well. Fwahahaha! Fine, I will teach you my techniques!"

        koga @talkingmouth "You have now beaten a Pokémon that is strong against the Poison-type, one that struggles against the Poison-type, and, of course, a Poison-type itself!"
        koga @closedbrow talking2mouth "As you have mastered the basics, future battles in this class will utilize three Pokémon, instead of merely one."

        $ passedclass = True
        jump aftertutorintropoison
    
    else:
        koga @sad "Ah."
        koga @talkingmouth "An unexpected outcome. I am certain you will return to remedy this, however! Do not let up on your training!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis

else:#generic scene
    show koga with dis
    koga @happy "Fwahahaha! Are you prepared to deepen your mastery of the tricks of Poison-type Pokémon?"
    hide koga with dis
    show kogabg with dis
    koga "The key to a Pokémon's power is versatility! From four moves, you must develop a dozen techniques! Now..."
    narrator "Class proceeds without incident."

return

label movetutorpoison:
show koga with dis
koga @talkingmouth "A Poison-type Pokémon's arsenal is not complete without powerful techniques. Which would you like to learn?"
koga @talkingmouth "I can teach Bad Breath, which will attempt to badly poison, paralyze, and confuse a foe, if the prior status cannot be applied."
if (4.1 in persondex["Instructor Koga"]["ClassesKnown"]):
    koga @happy "Follow it up with a lethal Venoshock! This move doubles in power on a poisoned foe!"

label aftertutorintropoison:
$ taughtmove = None

menu:
    ">Learn Bad Breath":
        $ taughtmove = "Bad Breath"
    ">Learn Venoshock" if (4.1 in persondex["Instructor Koga"]["ClassesKnown"]):
        $ taughtmove = "Venoshock"
    "Nevermind":
        koga @surprised "Indecisiveness must be cut out of the winning trainer."

        if (passedclass):
            jump aftertutoring
        else:
            jump afterpoisonsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        koga @surprised "Indecisiveness must be cut out of the winning trainer."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    koga @closedbrow talking2mouth "Teaching that Pokémon [taughtmove] is beyond even my abilities."

jump aftertutorintropoison

label itemcraftpoison:
show koga with dis

koga @talkingmouth "The ninjas of Ransei developed many items they used to bolster their powerful Shinobi techniques. I impart this knowledge unto you now, with the understanding you will never use them on another man."
koga @closedbrow talking2mouth "The Poison Barb inflicts lethal poison that renders a victim comatose within seconds. However, for a Pokémon, it boosts their Poison-type moves' power by 10%%."

menu:    
    ">Craft Poison Barb" if (3.1 in persondex["Instructor Koga"]["ClassesKnown"]):
        $ GetItem("Poison Barb", 1, "You tease a Mareanie for an hour straight until it gets mad enough at you to spit out a poisonous barb, which you quickly grab with protective gloves.")
        jump endclasscraft
    "Nevermind":
        koga @talkingmouth "Acceptable. Some of these items should really stay secret..."
        jump afterpoisonsetup
