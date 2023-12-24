label normalelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0

show normtype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "normal"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. NORMAL      #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call ethanevent from _call_ethanevent_12

label afternormalsetup:

if (2.1 in persondex["Instructor Lenora"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutornormal

        ">Craft items" if (3.1 in persondex["Instructor Lenora"]["ClassesKnown"]):
            jump itemcraftnormal

if (persondex["Instructor Lenora"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Lenora"]["ClassesKnown"].append(1)

    show whitney uniform at rightside with dis
    show cheren sad uniform at leftside with dis

    pause 1.0

    whitney @happymouth "Yo, [first_name]!"

    red "Hey, Whitney. You're in this class too?"

    whitney @happymouth "Heheh! You bet!"

    hide whitney at rightside with dis

    red "Hey, Cheren. Looking for something?"

    if (calDate.day == 5 and calDate.month == 4):
        cheren surprised "Ah, [first_name]. Excellent, I was looking to talk to you later, as I'm sure Bianca relayed to you."
        cheren sad "Right now, though, I find myself... preoccupied."
        cheren thinking "I haven't seen Bianca since homeroom with Professor Birch. I imagine she's gotten lost."
    else:
        cheren thinking "Some{i}one{/i}, rather. I haven't seen Bianca since homeroom with Professor Birch. I imagine she's gotten lost."
    
    show cheren surprised with dis
    
    play sound "Audio/ExitBuilding.wav"

    show bianca happy uniform:
        alpha 0.0 xpos 0
        ease 0.5 xpos 0.75 alpha 1.0
        
    bianca "I'm heeeeeeeeere!{w=0.5} Am I late?"
    cheren thinking "There you have it."

    show bianca:
        alpha 1.0 xpos 0.75
        ease 0.5 alpha 0.0

    show cheren:
        alpha 1.0 xpos 0.25
        ease 0.5 alpha 0.0

    pause 1.0

    hide whitney
    hide cheren
    hide bianca

    show lenora:
        xpos 900 alpha 0.0
        ease 0.5 xpos 800 alpha 1.0

    lenora "All right, all right. Settle down, everyone."

    if (not (calDate.month == 4 and calDate.day == 5)):
        lenora "I see we have some new faces. Let's see... Ethan and [first_name], right?"
    
    $ BecomeNamed("Instructor Lenora")

    lenora "I'm Lenora, and I'm your teacher for the {color=#0048ff}Normal-type class,{/color} which is the one you're in right now."
    lenora "I don't consider myself a very strict teacher, so I don't have many class 'rules.'"
    lenora "You can bring food, water, whatever, just as long as you clean up after yourselves."
    lenora "The only thing I won't allow are cellphones.{w=0.5} I see you kids staring at those things all day. You're gonna go blind!"
    lenora "The way I see it, you're all adults, so I shouldn't have to tell you these things."

    show lenora:
        xpos 800 alpha 1.0
        ease 0.5 xpos 700 alpha 0.0

    show lenorabg with dis

    redmind "This lady sounds a lot like my mom."
    lenora "Now, the first thing I want to do is have each of you tell the class something about yourselves."
    lenora "Who would like to go first?"
    if (not IsDate(5, 4, 2004)):
        red uniform @talkingmouth "I'll go. I'm, uh, [first_name], and I'm from Pallet Town. It's a tiny town in the Southwest of Kanto."
        ethan uniform @talkingmouth "Yeah! And, uh, I'm Ethan! I'm from New Bark Town. It's a tiny town in the Southeast of Johto."
        lenora "Oh, how cute. Seems you two have a lot in common, then. Welcome to our little Normal-type family!"

    else:
        lenora "Hmm, how about you, young lady?"

        show bianca happy uniform:
            xpos 300 ypos 2.0 alpha 0.0
            ease 0.5 xpos 300 ypos 1.0 alpha 1.0

        pause 1.0

        redmind "Good thing Bianca showed up before class started."

        show bianca_cherenintro:
            subpixel True
            alpha 0.0 xalign 0.5 zoom 1.0
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 5.0 zoom 0.75

        bianca "Okay~!"
        hide bianca
        bianca uniform "Hi everyone, I'm Bianca. I'm from the Unova region!"
        bianca happy "And so is my friend Cheren.{w=0.5} He's the super serious one over there!"
        cheren uniform angry "Don't drag me into this!"
        lenora "What a coincidence, I'm from Unova, too."
        bianca @surprisedbrow happymouth "Wow! That {i}is{/i} a coincidence!"
        lenora "Thank you, Bianca."
        lenora "Now, since your name was brought up, why don't you go next, Cheren?"
        cheren -angry "Very well."
        cheren "My name is Cheren. I hope we all get along for the coming year."

        $ renpy.pause(1.0, hard=True)

        lenora "Hmm. Anything else?"

        cheren @surprisedbrow "Pardon, ma'am?"

        lenora "I think that was a little short.{w=0.5} Why not tell us something exciting that's happened to you recently?"

        cheren @surprised "Uh... something exciting..."

        pause 1.5
        cheren thinking ".{w=0.25}.{w=0.25}."
        pause 1.5

        cheren sad "...Sorry, I can't quite think of anything."

        lenora "That's all right, dear. If you think of something, let us know!"

        hide bianca

        show bianca_cherenintro:
            alpha 1.0
            ease 1.0 alpha 0.0

        lenora "Now, who's next?"

    redmind "The atmosphere in this room is really homey.{w=0.5} I haven't felt this relaxed in a classroom in a really long time."

    hide bianca_cherenintro
elif (2.1 not in persondex["Instructor Lenora"]["ClassesKnown"] and classstats["Normal"] >= 10):#Simple World
    show lenora with dis
    if (2 not in persondex["Instructor Lenora"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        lenora "[first_name]."

        red uniform @surprised "Hm? Instructor?"

        lenora "I think you're ready to take your advancement exam for this class. It'll be a one-on-one battle."

        red @happy "Oh. Cool! Thanks. What does advancing mean for this class?"

        lenora "I'll be able to teach your Normal-types the move Simple World."

        red @thinking "Woah. That's an out-there name. What does it do?"

        lenora "It puts a terrain on the field that makes all grounded Pokémon Normal-type for five turns."

        red @surprised "Huh. I can see how that could be useful for a Normal-type. Sure, I'm ready for that."

        lenora "Good."

        $ persondex["Instructor Lenora"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora "Pick one Pokémon from your party to battle with. I'll be honest--{i}anything{/i} should be able to win this one."

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora "Alright, let's begin."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon(129, level=11, moves=[GetMove("Splash"), GetMove("Tackle")], ability="Swift Swim")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "lenora", "lenora"], reanchor=[False, False]) from _call_Battle_36
    $ gymbattles["Instructor Lenora1"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora1")):
        $ persondex["Instructor Lenora"]["ClassesKnown"].append(2.1)

        lenora "Good job. I look forward to administering your next advancement exam, too."

        $ passedclass = True
        jump aftertutorintronormal
    
    else:
        lenora "Oh, a loss. Well, you can retake the exam next time you attend this class. Just train a bit beforehand."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis
elif (3.1 not in persondex["Instructor Lenora"]["ClassesKnown"] and classstats["Normal"] >= 20):#Silk Scarf
    show lenora with dis
    if (3 not in persondex["Instructor Lenora"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        lenora "[first_name]. Do you know how to use items in battle?"

        red uniform @talkingmouth "Yep. Each of my Pokémon has a Battle Bag, too."

        lenora "Good to hear. I'll be teaching you how to make Silk Scarves, then."

        red @thinking "Silk Scarves?"

        lenora "That's right. They're a special type of scarf that boosts the power of your Normal-type moves by 10%%."

        red @happy "Nice. But I have to pass an advancement exam first, right?"

        lenora "You get it. Are you ready?"

        red @talkingmouth "Ready as I'll ever be."

        $ persondex["Instructor Lenora"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora "Pick one Pokémon from your party to battle with. [bluecolor]I'll be using a Normal-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora "Alright, let's begin."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon("Watchog", level=21, moves=[GetMove("Hypnosis"), GetMove("Crunch"), GetMove("Retaliate"), GetMove("Sand Attack")], ability="Illuminate", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "lenora", "lenora"], reanchor=[False, False]) from _call_Battle_98
    $ gymbattles["Instructor Lenora2"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora2")):
        $ persondex["Instructor Lenora"]["ClassesKnown"].append(3.1)

        lenora "Good job. I look forward to administering your next advancement exam, too."

        $ GetItem("Silk Scarf", 1, "Lenora hands you a Silk Scarf. Its fabric has a strangely cooling effect.")
        jump aftertutoring
    
    else:
        lenora "Oh, a loss. Well, you can retake the exam next time you attend this class. Just train a bit beforehand."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis
elif (4.1 not in persondex["Instructor Lenora"]["ClassesKnown"] and classstats["Normal"] >= 30):#Covet
    show lenora with dis
    if (4 not in persondex["Instructor Lenora"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        lenora "[first_name]."

        red uniform @surprised "Hm? Instructor?"

        lenora "I want to give you another advancement exam."

        red @happy "Oh, really? I feel like it's been so soon since the previous one, though."

        lenora "This class isn't meant to be hard. Because there are so many Pokémon out there that start out Normal-type, Normal is a good class to take to get a grasp of the fundamentals."

        red @talkingmouth "Well, I think it's achieving that for me."
        red @talkingmouth "What do I get if I pass this advancement exam?"

        lenora "A pat on the back. And access to the move Covet."

        red @thinking "Covet?"

        lenora "It's a Normal-type version of the move 'Thief'."

        red @surprised "Oh. I think I knew that, actually. Um... okay."

        pause 1.0

        lenora "So. Ready for the exam?"

        red @happy "Sure am!"

        $ persondex["Instructor Lenora"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora "Pick one Pokémon from your party to battle with. [bluecolor]Using a Normal-type will make this battle a lot harder on you.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora "Alright, let's begin."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon("Aron", level=31, moves=[GetMove("Iron Head"), GetMove("Rock Slide"), GetMove("Protect"), GetMove("Headbutt")], ability="Study", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "lenora", "lenora"], reanchor=[False, False]) from _call_Battle_99
    $ gymbattles["Instructor Lenora3"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora3")):
        $ persondex["Instructor Lenora"]["ClassesKnown"].append(4.1)

        lenora "Good job. After finishing this exam, that means you've beaten both a Normal-type and a Pokémon that Normal-types have trouble with."

        pause 1.0

        lenora "Oh, and a Magikarp."

        pause 0.5

        lenora "Anyway, you clearly have an understanding of the fundamentals, so future exams will be harder. I'll be using three Pokémon, and I'll expect you to bring three to bear as well."

        $ passedclass = True
        jump aftertutorintronormal
    
    else:
        lenora "Oh, a loss. Well, you can retake the exam next time you attend this class. Just train a bit beforehand."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis

else:#generic scene
    show lenora with dis
    lenora "[timeOfDay], dears! Let's all buckle down and work hard today!"
    hide lenora with dis
    show lenorabg with dis
    lenora "Now, before class begins, why don't we all say something nice that happened to us since our last class?"
    narrator "Class proceeds without incident."

return

label movetutornormal:
show lenora with dis
lenora "You'd like me to teach your Pokémon a Normal-type move? Alright. Sure. Which one?"
lenora "I can teach Simple World. That move sets a terrain for five turns that makes all normaled Pokémon become Normal-type."
if (4.1 in persondex["Instructor Lenora"]["ClassesKnown"]):
    lenora @surprisedbrow happymouth "If that's too niche for you, I can also teach Covet. It's just a Normal-type Thief. Steals the opponent's item, if you can."

label aftertutorintronormal:
$ taughtmove = None

menu:
    ">Learn Simple World":
        $ taughtmove = "Simple World"
    ">Learn Covet" if (4.1 in persondex["Instructor Lenora"]["ClassesKnown"]):
        $ taughtmove = "Covet"
    "Nevermind":
        lenora "Okay."

        if (passedclass):
            jump aftertutoring
        else:
            jump afternormalsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    lenora "Okay."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    lenora "I can't teach that Pokémon that move, sorry."

jump aftertutorintronormal

label itemcraftnormal:
show lenora with dis

lenora "Items are just as important a part of battle as anything else. When I'm out in the field, digging up fossils, I always make sure my Pokémon are wearing their Rocky Helmets."
lenora "Now, if you want to boost your Normal-type Pokémon's attack by 10%%, I recommend the Silk Scarf. They're made of a special fabric that concentrates-- well, you don't need to hear that. Just trust me, they work."

menu:    
    ">Craft Silk Scarf" if (3.1 in persondex["Instructor Lenora"]["ClassesKnown"]):
        $ GetItem("Silk Scarf", 1, "You silently plug away at a sewing machine as you sew the pieces of fabric that make up the scarf. When done, it's light, airy, and stylish.")
        jump endclasscraft
    "Nevermind":
        lenora "Fine."
        jump afternormalsetup