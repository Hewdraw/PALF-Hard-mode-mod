label psychicelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0

show psychtype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

############################################################################################################################################################################################################################
#### 13. POISON    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

$ location  = "psychic"
$ passedclass = False

call sabrinaevent from _call_sabrinaevent_1
call rosaevent from _call_rosaevent_2
call ethanevent from _call_ethanevent_14
call tiaevent from _call_tiaevent_1

label afterpsychicsetup:

if (2.1 in persondex["Instructor Will"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorpsychic

        ">Craft items" if (3.1 in persondex["Instructor Will"]["ClassesKnown"]):
            jump itemcraftpsychic

if (persondex["Instructor Will"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Will"]["ClassesKnown"].append(1)
    $ renpy.pause(1.0, hard=True)

    show will:
        xpos 800 alpha 0.0
        ease 0.7 xpos 750 alpha 1.0

    will @happy "Salutations, my students! Welcome to your {color=#0048ff}Psychic class.{/color}"

    if (not (calDate.month == 4 and calDate.day == 5 and calDate.year == 2004)):
        will @surprised "New students? Wait, don't tell me... Ethan and [first_name]!"

    if (not IsBefore(26, 4, 2004) or (calDate.day == 26 and calDate.month == 4 and calDate.year == 2004 and timeOfDay == "Evening")):
        red @talkingmouth "Um... yeah, Instructor Will. We've met."

        will @surprised "So we have! Then let me introduce myself to Ethan here."

    $ BecomeNamed("Instructor Will")
    will @happy "Allow me to introduce myself.{w=0.5} I am the Great Will, your teacher!"

    hide will with dis

    pause 1.0

    show willbg with dis

    will "For this class, we will not only be learning about Psychic Pokémon, but we will also be training your innate psychic powers as well!"

    ethan uniform "Our.{w=0.25}.{w=0.25}.{w=0.25} psychic powers?"
    ethan thinking "I think my Dad got me meds for those..."

    will "Unbeknownst to most, every living being in the world has psychic potential."
    will "The power is just hidden away.{w=0.5} And it will be my job to bring it out of you to increase your natural focus."
    will "If your focus is too weak, your telepathic bond with your Pokémon will be severed easily."
    will "You must become familiar with ESP and your Pokémon will become undefeatable!"
    will "As you can see, I am quite the capable esper."

    show book1 as book_A:
        subpixel True
        alpha 0.0 zoom 0.05 xpos 900 ypos 460
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.4 ypos 450
            ease 0.4 ypos 460
            repeat
    show book1 as book_B:
        subpixel True
        alpha 0.0 zoom 0.04 xpos 980 ypos 450 rotate 12
        parallel:
            pause 0.25
            ease 0.5 alpha 1.0
        parallel:
            ease 0.3 ypos 440
            ease 0.3 ypos 450
            repeat
    show book2:
        subpixel True
        alpha 0.0 zoom 0.04 xpos 920 ypos 470 rotate 12
        parallel:
            ease 0.75 alpha 1.0
        parallel:
            ease 0.5 ypos 480
            ease 0.5 ypos 470
            repeat
    show calc:
        subpixel True
        alpha 0.0 zoom 0.05 xpos 990 ypos 470 rotate 12
        parallel:
            pause 0.2
            ease 0.4 alpha 1.0
        parallel:
            ease 0.4 ypos 460
            ease 0.4 ypos 470
            repeat

    $ renpy.pause(1.5, hard=True)

    ethan happy "Wow, that's really cool.{w=0.5} And a bit terrifying."

    play sound "Audio/Scattered Applause.ogg"

    show bianca happy uniform at rightside with dis

    bianca "Incredible, Instructor Will! Not even my little Moony can do that!"

    will "Thank you, thank you!"

    hide bianca at rightside with dis

    show book1 as book_A:
        ypos 460 alpha 1.0
        ease 0.3 ypos 490 alpha 0.0
    show book1 as book_B:
        ypos 450 alpha 1.0
        pause 0.15
        ease 0.3 ypos 490 alpha 0.0
    show book2:
        ypos 470 alpha 1.0
        pause 0.1
        ease 0.3 ypos 490 alpha 0.0
    show calc:
        ypos 470 alpha 1.0
        pause 0.2
        ease 0.3 ypos 490 alpha 0.0

    will "If you want to achieve this level of telekinesis, you must first understand the steps to ESP."
    will "The first step to using ESP is to practice meditation.{w=0.5} And to meditate efficiently, you must have solid concentration."
    will "In order to have solid concentration, you must rid your mind of distractions."
    will "Distractions come in many shapes and forms, but mostly they are..."
    
    hide book1 as book_A
    hide book1 as book_B
    hide book2
    hide calc

    ethan "This all sounds like a load of baloney to me."
    red @angrybrow "Dude, he just lifted a bunch of books into the air in front of us."
    ethan "Eh, he's probably got an Espeon hidden under that desk."

    will "...Now, for our first exercise, I want you all to close your eyes and concentrate all your thoughts on one thing.{w=0.5} It doesn't matter what, as long as it's the only thing you're thinking about."
    will "This way, you can attune yourselves to your natural focus and bring out your inner telekinetic powers!"

    show blank2 as blank_A with transeye

    window hide
    pause 1.5

    play sound "Audio/Whoosh.ogg"
    pause 1.0

    redmind "Eh? What was that...?"

    window hide

    pause 1.0

    hide blank2 as blank_A with transeye2

    will "...Right, that's enough of that for now. Open your eyes, students!"
    will "Let's move on to basic telepathy theory, shall we?"

    narrator "In between the various mental exercises, you manage to learn more about Psychic-types."

    will "Oh, time's up, already?"
    will "That's okay, we'll continue next time! We can only keep getting better from here!"

    red "This has to be one of the weirdest classes I've ever been in."
    ethan happy "Sure, but at least it's not boring!"

    hide will
elif (2.1 not in persondex["Instructor Will"]["ClassesKnown"] and classstats["Psychic"] >= 10):#Clear Mind
    show will with dis
    if (2 not in persondex["Instructor Will"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "Psychic class is in full swing, with Instructor Will enthusiastically extolling the virtues of Psychic-types, when, suddenly..."

        will @talkingmouth "[first_name]! I require a volunteer for a demonstration."

        red uniform @surprised "Huh? A demonstration?"

        will @happy "Yes, indeed! By reading your mundane euthymic brainwaves, I am certain that you think you are ready for the advancement exam!"

        redmind @confusedeyebrows frownmouth "Huh? I wasn't thinking that at all. And now I feel kinda insulted."

        will @surprised "And now you feel insulted!"

        pause 1.0

        red @talking2mouth "Your powers are incomparable, Instructor."

        will @happy "So say all to the Great Will!"

        will @angrybrow happymouth"But I do not ask for your assistance in this demonstration for naught! I will bestow upon you the ultimate Psychic technique--{i}Clear Mind!{/i}"

        red @talkingmouth "I mean, you're the instructor, so you can just {i}make{/i} me help, but sure, I'm down. What does Clear Mind do?"

        will @thinking "You can target any Pokémon on the field with it, and it will remove their status conditions, and reset their stat changes!"

        will @happy "A perfectly balanced tool for offensive or defensive use!"

        red @thinking "Okay, that's pretty good, yeah."
        red @talkingmouth "So this demonstration is..."

        will @happy "I knew you would ask! It is a one-on-one battle."

        red @happy "Alright. Let's do this, then!"

        $ persondex["Instructor Will"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "Hahaha! I foresaw this battle! Send out your Pokémon, and roll the dice of fate! {color=#0048ff}A Psychic-type will give you the best odds here!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "May the odds be ever in your favor!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon(453, level=11, moves=[GetMove("Poison Sting"), GetMove("Mud-Slap"), GetMove("Astonish"), GetMove("Taunt")], ability="Anticipation")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_102
    $ gymbattles["Instructor Will1"] = _return

    show will with dis

    if (WonBattle("Instructor Will1")):
        $ persondex["Instructor Will"]["ClassesKnown"].append(2.1)

        will @happy "Hahaha! Exactly as I predicted!"

        $ passedclass = True
        jump aftertutorintropsychic
    
    else:
        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "Still, I foresee that you will come back again... and truly show your strength then!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis
elif (3.1 not in persondex["Instructor Will"]["ClassesKnown"] and classstats["Psychic"] >= 20):#Twisted Spoon
    show will with dis
    if (3 not in persondex["Instructor Will"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        will @happy "[first_name]! How are your psychic powers developing?"

        red uniform @surprised "I am thankful every day, Instructor Will, that I don't need to have psychic powers to pass this class' exams."

        pause 1.0

        will poutmouth @talking2mouth "Well... yes, that's true."

        pause 2.0

        will -poutmouth @closedbrow talking2mouth "But it doesn't {i}hurt.{/i}"

        red @talkingmouth "Hm... well, I think I'm getting something, actually..."

        will @surprised "Oh? Are you?"
        will @happy "Are you really? Fantastic! We might make an Esper out of you yet!"

        pause 1.0

        red @thinking "You're thinking that you want to give me this class' advancement exam, right?"

        pause 1.0

        will @poutmouth closedbrow "Eh, fine."

        will @happy "Pass this class, and I will demonstrate to you the utmost psychic powers that allow me to create the ultimate tool of the Esper--the Twisted Spoon! This item boosts the power of your Psychic-type moves by a tremendous 10%%!"

        red @talkingmouth "Can't wait to earn it. In fact, I don't need to. Let's battle!"

        $ persondex["Instructor Will"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "Hahaha! I foresaw this battle! Send out your Pokémon, and roll the dice of fate! {color=#0048ff}I will be using an illustrious Psychic-type for this bout!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "May the odds be ever in your favor!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon("Natu", level=21, moves=[GetMove("Night Shade"), GetMove("Confuse Ray"), GetMove("Peck"), GetMove("Psyshock")], ability="Magic Bounce", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_103
    $ gymbattles["Instructor Will2"]  = _return

    show will with dis

    if (WonBattle("Instructor Will2")):
        $ persondex["Instructor Will"]["ClassesKnown"].append(3.1)

        will @happy "Hahaha! Exactly as I predicted!"

        $ GetItem("Twisted Spoon", 1, "Instructor Will produces a regular spoon and bends it before proudly presenting it to you. You're pretty sure he just bent it with his thumb.")

        jump aftertutoring
    
    else:
        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "Still, I foresee that you will come back again... and truly show your strength then!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis
elif (4.1 not in persondex["Instructor Will"]["ClassesKnown"] and classstats["Psychic"] >= 30):#Psybeam
    show will with dis
    if (4 not in persondex["Instructor Will"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        will @talkingmouth "[first_name]! I hear your thoughts! And what you want is... a Psychic move that can deal damage?"

        pause 1.0

        red uniform @thinking "I... guess so? Like, in the abstract? Clear Mind is useful, but it can't damage."

        will @happy "Fantastic news for you, my Student! The Great Will has looked into the future, and sees a reality where that {i}is{/i} the case!"

        pause 1.0

        red @thinking "Do I just have to pass an advancement exam?"

        will @surprised "Oh? You may have something prescient about you, too! Yes, pass an advancement exam, and unlock the forbidden power of 'Psybeam!'"

        redmind @thinking "Forbidden power? It's not {i}that{/i} good a move."

        will @happy "Not only can it do damage, it can also confuse! Not even Psychic can do that!"

        red @happy "Fair enough. I'm ready to battle you for it, then."

        $ persondex["Instructor Will"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "Hahaha! I foresaw this battle! Send out your Pokémon, and roll the dice of fate! {color=#0048ff}But if you use a Psychic-type, you're rolling against loaded die!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "May the odds be ever in your favor!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon("Murkrow", level=31, moves=[GetMove("Taunt"), GetMove("Assurance"), GetMove("Night Shade"), GetMove("Wing Attack")], ability="Prankster", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_104
    $ gymbattles["Instructor Will3"]  = _return

    show will with dis

    if (WonBattle("Instructor Will3")):
        $ persondex["Instructor Will"]["ClassesKnown"].append(4.1)

        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "With this, you have beaten one Psychic-type, a Pokémon that's strong against Psychic types, and one that's weak to Psychic-types!"
        will @happy "In future lessons, then, I shall unveil even more of my aesome abilities, and use {i}three{/i} Pokémon at once! I do hope you're prepared in kind..."

        $ passedclass = True
        jump aftertutorintropsychic
    
    else:
        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "Still, I foresee that you will come back again... and truly show your strength then!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis


else:#generic scene
    show will with dis
    will @happy "Salutations, students! Today, we will hone our psychic powers while learning about Psychic Pokémon!"
    will @talkingmouth "You're permitted to close your eyes for meditative purposes{w=0.5}{nw}"
    extend @angry "--but no falling asleep during the lectures!"
    hide will
    show willbg 
    with dis
    narrator "Class proceeds without incident."
return

label movetutorpsychic:
show will with dis
will @talkingmouth "You want the Great Will to teach your Pokémon a new Psychic-type move? Very well! I deign to do so!"
will @happy "Do you want to learn Clear Mind? This move will remove the status effects and stat changes of any Pokémon on the field!"
if (4.1 in persondex["Instructor Will"]["ClassesKnown"]):
    will @angrybrow happymouth "Psybeam allows you to use your psychic powers offensively! Bring to bear the might of the telekinetic force!!"

label aftertutorintropsychic:
$ taughtmove = None

menu:
    ">Learn Clear Mind":
        $ taughtmove = "Clear Mind"
    ">Learn Psybeam" if (4.1 in persondex["Instructor Will"]["ClassesKnown"]):
        $ taughtmove = "Psybeam"
    "Nevermind":
        will @surprised "Not yet ready to change your fate?"

        if (passedclass):
            jump aftertutoring
        else:
            jump afterpsychicsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        will @surprised "Not yet ready to change your fate?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    will @happy "Hahaha! Not even the Great Will can teach that Pokémon [taughtmove]!"

jump aftertutorintropsychic

label itemcraftpsychic:
show will with dis

will @happy "A great Psychic often relies on physical props to demonstrate his Psychic powers to his captive audience! Why don't you see what I have in store?"
will @angrybrow happymouth "This Twisted Spoon is a splendid example. After bending it with naught but my mind, it will boost the power of all Psychic-type moves by 10%%!"

menu:    
    ">Craft Twisted Spoon" if (3.1 in persondex["Instructor Will"]["ClassesKnown"]):
        $ GetItem("Twisted Spoon", 1, "You 'ooh' and 'aah' at Instructor Will's performance, until, after about an hour's worth of concentration, he produces a single Twisted Spoon for you. (You're pretty sure he bent it with his thumb.)")
        jump endclasscraft
    "Nevermind":
        will @surprised "I did not foresee this!"
        jump afterpsychicsetup
