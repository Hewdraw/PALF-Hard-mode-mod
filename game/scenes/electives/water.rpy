label waterelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0

show waterclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show waterglow1:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 1.5
        repeat
show waterglow2:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        pause 0.5
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 1.0
        repeat
show waterglow3:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        pause 1.0
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 0.5
        repeat

############################################################################################################################################################################################################################
#### 13. WATER       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

$ location = "water"
$ passedclass = False

call ethanevent from _call_ethanevent_17
call nessaevent from _call_nessaevent_1
call skylaevent from _call_skylaevent_1

label afterwatersetup:

if (2.1 in persondex["Instructor Wallace"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorwater

        ">Craft items" if (3.1 in persondex["Instructor Wallace"]["ClassesKnown"]):
            jump itemcraftwater

if (persondex["Instructor Wallace"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Wallace"]["ClassesKnown"].append(1)
    $ renpy.pause(1.0, hard=True)

    show misty uniform angry:
        xpos 0.25 alpha 0.0
        ease 0.5 alpha 1.0

    $ renpy.pause(1.0, hard=True)

    redmind "Well, it's a familiar face, but she doesn't seem very excited to see me."
    redmind "Let's see... is there someone else?"

    hide misty at leftside with dis

    pause 1.0

    play sound "Audio/ExitBuilding.wav"

    show wallace with dis:
        xpos 1200
        ease 0.5 xpos 660
        
    wallace @happy "Hello, my wonderful students!"

    redmind surprised "That almost gave me a heart attack!{w=0.5} This guy knows how to really make an entrance."
    redmind -surprised "Maybe Whitney took some lessons from him."
    redmind @thinking "And what the heck is this guy wearing? This has got to be against the school dress code!"

    show wallace:
        xpos 660 alpha 1.0
        ease 0.5 xpos 600 alpha 0.0

    show wallacebg with dis

    if (not IsDate(4, 5, 2004)):
        wallace @surprised "Ooooh? Looks like we've got a couple new students to join us! Let's see... your names are Ethan and [first_name], right? Splendid, just splendid!"
        wallace @happy "I'm Wallace, and I welcome both of you to your first {color=#0048ff}Water class{/color} at Kobukan Academy!"
    else:
        wallace @happy "I'm Wallace, and I welcome you all to your first {color=#0048ff}Water class{/color} at Kobukan Academy!"
    
    $ BecomeNamed("Instructor Wallace")
    wallace @talkingmouth "And you didn't hear this from me, but Water really is the best type compared to the others. After all, the world is made up of over 70 percent water!"
    wallace "Well? Aren't you all just bedazzled by being here?{w=0.3} I know I am!"

    pause 1.0
    ethan uniform surprised "How are we supposed to react to all this?"

    if (not IsDate(4, 5, 2004)):
        wallace "I see eagerness has stunned you two."
    else:
        wallace "I see eagerness has stunned you all."

    wallace "If you won't talk, then I shall make you!"
    wallace "Hmm.{w=0.25}.{w=0.25}.{w=0.25} YOU!"

    narrator "Wallace flamboyantly points straight at Nessa."

    show nessa uniform:
        alpha 0.0 xpos 500
        ease 0.5 alpha 1.0

    nessa "..."

    nessa @talkingmouth "Um, are you pointing at me?"
    
    if (not IsDate(4, 5, 2004)):
        wallace "Yes, Nessa! Stand up and introduce yourself to the new students."
        redmind "Didn't he kind of just do that for her...?"
    else:
        wallace "Yes, you! Stand up and introduce yourself."

    nessa @talkingmouth "Uh, okay..."
    nessa @closedbrow "But, like, we already know each other."
    
    nessa @talkingmouth "I'm Nessa. I'm from Hulbury, in Galar."
    nessa @talkingmouth "I specialize in Water-type Pokémon. I also work as a model." 
    nessa @sadbrow "Sometimes."
    wallace "Oh, really? I have a mild interest in modeling, too.{w=0.5} And {i}why{/i} are you in this class?"

    pause 1.5

    nessa @surprised "{cps=26}...because I want to learn more about Water Pokémon?{/cps}"
    wallace "Wonderful! Anything else?"
    nessa @talkingmouth closedbrow "...No, I think I'm good."
    
    show nessa uniform:
        alpha 1.0 xpos 500 ypos 1.0
        ease 0.5 ypos 2.0 alpha 0.0

    wallace "Very good, Nessa!"

    if (not (calDate.month == 4 and calDate.day == 5)):
        wallace "So, you see, now, the essence of what this class is about, new fish!"
        red "Learning about Water-type Pokémon?"
        wallace "Yes! But also, so much more!"
    else:
        wallace "Brilliant start..."
    wallace "Now.{w=0.25}.{w=0.25}.{w=0.25} YOU!"

    narrator "Wallace proceeds to go down the entire roster and makes everyone introduce themselves."
    narrator "Nothing of value is accomplished, and you sit around awkwardly for an hour."

    pause 1.0

    wallace "...Well! I hope you've all learned the importance of class participation!"
    wallace "All right, that is all the time we have for today.{w=0.5} But tomorrow, I expect you all to be much more energetic."
    wallace "Class dismissed!"
elif (2.1 not in persondex["Instructor Wallace"]["ClassesKnown"] and classstats["Water"] >= 10):#Healing Spring
    show wallace with dis
    if (2 not in persondex["Instructor Wallace"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "You're working hard on your studying when you notice Instructor Wallace is standing in the middle of the class, tapping his foot impatiently."

        redmind uniform @thinking "Looks like something's biting at the teacher. Maybe I should ask?"

        red @happy "Instructor Wallace? Is something wrong?"

        wallace @talkingmouth "It most certainly is! We've been taking these classes for far too long, and yet the number of people who've requested advancement is painfully low!"

        red @thinking "Maybe some students didn't know what advancement was?"

        wallace @sadbrow talkingmouth "Well, then they should've asked!"

        red @happy "Just playing devil's advocate here, but if someone asked, y'know, 'is there anything more to this class,' and you said no, that would be pretty embarrassing." 
        
        wallace @angry "Oh, embarrassment, shmembarrassement! I care less if you learn {i}anything{/i} about Water-types than I do that you learn embarrassement isn't real."

        red @surprised "Sir?"

        wallace @happy "Put yourself out there, darlings! Ask for those raises! Take up new hobbies! Wear what you want!"

        wallace @talkingmouth "{i}Anything{/i} but drowning under the suffocating weight of 'what if!'"

        red @talkingmouth "Well... can I advance in this class, yet?"

        wallace @happy "No."

        pause 2.0

        red @thinking "Huh, you're right, that's not so bad."

        wallace @happy "There we go, then! Why, yes, of course you can. But, first, you get to engage in a one-on-one battle with a former National Champion of the Hoenn Region!"

        wallace @talkingmouth "Aren't you lucky?"

        red @happy "Pretty lucky, yeah. But I look forward to facing you at your full strength one day."

        wallace @talkingmouth "Splendid! As for now, winning this battle will allow me to teach you 'Healing Spring'!" 
        wallace @sad "Personally, I'd like to teach you all my techniques immediately, but the school requires you show some competency before I start handing out the Champion-level moves."

        red @thinking "Healing Spring. I don't think I've heard of that one. Did you invent it?"

        wallace @happy "Certainly did! It's a glorious shower of healing waters that sets up rain and makes the user recover a little health every turn."

        red @happy "Cool. It's a better Rain Dance."

        wallace @happy "You get it? Fabulous! Now, let's dazzle the class with our battle!"

        $ persondex["Instructor Wallace"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @talkingmouth "Pick one Pokémon to use against me. Lucky for you, I'm not allowed to use my actual team, so {color=#0048ff}I recommend picking a Water-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Dance, water, dance!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon(111, level=11, moves=[GetMove("Tackle"), GetMove("Tail Whip"), GetMove("Smack Down"), GetMove("Bulldoze")], ability="Lightning Rod")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_41
    $ gymbattles["Instructor Wallace1"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace1")):
        $ persondex["Instructor Wallace"]["ClassesKnown"].append(2.1)

        wallace @happy "Dazzling! Take it from a former Champion! Keep that up and you'll be at my level eventually!"

        $ passedclass = True
        jump aftertutorintrowater
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis
elif (3.1 not in persondex["Instructor Wallace"]["ClassesKnown"] and classstats["Water"] >= 20):#Mystic Water
    show wallace with dis
    if (3 not in persondex["Instructor Wallace"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "You are studying hard in class when you notice that Instructor Wallace has, in an uncharacteristically subtle move, managed to sneak up next to you."

        red uniform @surprised "Instructor? Is there something I can do for you?"

        wallace @happy "Well, certainly, darling. A little birdie told me that you want to be a Pokémon Champion!"

        red @talkingmouth "That's right, Sir. It's what I've wanted, more than anything else. Ever."

        wallace @talkingmouth "Well, then, why?"

        red @thinking "That's something a lot of people ask me. And I think I give a different answer to every single person."

        red @sadbrow happymouth "I've just got so many reasons that I can't narrow it down to just one."

        wallace @happy "Hm... well, that's fair."

        red @talkingmouth "What about you, Instructor Wallace? Why did you want to be a Champion?"

        wallace @talkingmouth "Well, I was already the Champion of contests in Hoenn. And I happened to hear some so-called 'fans' of mine at an autograph signing that were disparaging my battle performance!"

        red @confused "Huh?"

        wallace @angry "Yes, can you believe it? They thought I only had the skills to dazzle, and entertain! As though I was some limp-wristed fop unable to punch back just as hard as my fashion sense hits!"

        red @surprised "Uh..."

        wallace @surprised "Well, when I heard that, I was, of course, incensed! And not the nice-smelling kind they burn on Mt. Pyre."
        wallace @closedbrow talkingmouth "The champion of the region at the time, Steven Stone, is a good friend of mine. I happened to know that his party was rather poorly matched against mine, so I simply waltzed through the Elite Four and dethroned him!"
        wallace @happy "Really, it was quite simple. I don't know why more people don't become Champion for a while. It's a gorgeous story."

        red @surprised "So... wait... you became Champion out of spite?"

        wallace @happy "Well, there was a little bit about proving to myself I could do it, and kicking Steven-boy out of his funk, but yes, it was mostly spite."

        red @talking2mouth "Huh."

        wallace @talkingmouth "Of course, as I'm sure you know, I didn't keep the position for very long. Steven is, with all fair credit to him, a far better battler than I am. With time to prepare, he easily took back the championship."
        wallace @happy "But I believe I made my point sufficiently. To myself, to my beloved Hoenn, and to those two buttheads who doubted me."

        red @sweat talkingmouth "Uh, yeah. Wow. I'll say."

        wallace @talkingmouth "But enough about me! (Though that is my favorite topic.) You've been doing splendidly in this class, [first_name], and I think it's about time I commend you for that."
        wallace @happy "What do you think about taking an advancement exam? If you pass, you'll be privvy to one of my {i}personal{/i} Mystic Waters, which boost Water-type attacks by 10%%!"

        red @happy "I'm excited! Let's do this."

        $ persondex["Instructor Wallace"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Instructor Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @happy "Glorious! {color=#0048ff}Pick one Pokémon to use against my Water-type!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Dance, water, dance!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon("Milotic", level=21, moves=[GetMove("Tackle"), GetMove("Tail Whip"), GetMove("Smack Down"), GetMove("Bulldoze")], ability="Cute Charm", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_109
    $ gymbattles["Instructor Wallace2"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace2")):
        $ persondex["Instructor Wallace"]["ClassesKnown"].append(3.1)

        wallace @happy "Dazzling! Take it from a former Champion! Keep that up and you'll be at my level eventually!"

        $ GetItem("Mystic Water", 1, "Instructor Wallace flamboyantly tosses a Mystic Water your way. You're unsure where he was keeping it. His outfit clearly does not have pockets.")

        jump aftertutoring
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis
elif (4.1 not in persondex["Instructor Wallace"]["ClassesKnown"] and classstats["Water"] >= 30):#Aqua Jet
    show wallace with dis
    if (4 not in persondex["Instructor Wallace"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        wallace @happy "[first_name]-boy! How are you doing in this class?"

        red uniform @thinking "Well enough, I think, Instructor. Um... I'm having a good time, at least. And I think I'm learning things, too."

        wallace @talkingmouth "Well, that's good to hear! I was concerned, given that I was a Contest Champion, {i}and{/i} a Battle Champion, that perhaps I wouldn't make a {i}fabulous{/i} teacher as well!"
        wallace @happy "It's {i}dazzling{/i} to see that my concerns were unfounded."

        red @confused "Uh... yeah."

        redmind @thinking "This guy has some impressive self-confidence."

        wallace @talkingmouth "Tell me, did I ever tell you why I decided to become a teacher?"

        red @thinking "No, Instructor, I don't think you did."

        wallace @happy "Well, pull up a chair, and sit yourself down! I've got a delicious little scandal to share."

        red @surprised "Oh! Really? I mean, I'm already sitting down, but I'd like to hear this!"

        wallace @talkingmouth "Well, as I already told you, I decided to become Champion when my good friend Steven was in a rut."
        wallace @happy "I'd retired from my illustrious career as a Contest Coordinator, and was the eighth gym leader of Hoenn at the time."
        wallace @talkingmouth "Well, after becoming Champion, my old mentor, and good friend, Juan, took my gym over for me. Meanwhile, my very own niece, who I'm incredibly proud of, by-the-by, had become the new Contest Champion."
        wallace @happy "That's, ah, 'worldwide' Contest Champion, by the by."

        red @happy "Impressive!"

        wallace @talkingmouth "Yes, so, I was quite glad that my friends and family had managed to fill the gaping holes my presence left, but that did mean that I was somewhat out of roles to fill when Stevey-boy ousted me from the Championship position."

        pause 1.0

        red @confused "So... you became a teacher?"

        wallace @happy "Exactly! Look at me. I'm far too young and gorgeous to retire yet. I could, certainly. I have a tremendous number of beach houses that I can hear calling my name right now." 
        wallace @talkingmouth "I even rent a villa from the Champion of Sinnoh, I'll have you know."
        wallace @happy "But retirement would not suit me. I am the river. Ever moving on, taking new forms, new shapes, and dragging everything that fills into my presence along with me."

        red @talkingmouth "And... we, your students, are the stuff in the river?"

        wallace @happy "Quite so! And how lucky you are to be that."

        red @confused "Right..."

        wallace @talkingmouth "Oh, you may be doubtful, but there's no denying that I've been a fabulous teacher thus far. If I hadn't, you wouldn't be ready to advance in this class!"

        pause 1.0

        wallace @happy "And, of course, you are."

        red @talkingmouth "Uh, yeah. Sure. What do I get from advancing?"

        wallace @happy "Aqua Jet, [first_name]-boy! It's not exactly a Champion-level move, but for the majority of slow, bulky, Water-types, the ability to hit something faster, first, is too good to turn down!"
        
        red @talkingmouth "I'll take it. I'm ready to battle now."

        $ persondex["Instructor Wallace"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @happy "Brilliant! Then Pick one Pokémon to use! {color=#0048ff}But don't use a Water-type this time. Things'll turn out poorly if you do!~{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Dance, water, dance!"

    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon("Sunflora", level=31, moves=[GetMove("Giga Drain"), GetMove("Worry Seed"), GetMove("Leech Seed"), GetMove("Ingrain")], ability="Early Bird", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_110
    $ gymbattles["Instructor Wallace3"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace3")):
        $ persondex["Instructor Wallace"]["ClassesKnown"].append(4.1)

        wallace @happy "Dazzling! Take it from a former Champion! Keep that up and you'll be at my level eventually!"
        wallace @talkingmouth "Because you've beaten a Water-type, a Pokémon that easily defeats Water-types, and a Pokémon that Water-types have no trouble trouncing, future exams will be a bit harder."
        wallace @happymouth "Of course, I won't be using my {i}actual{/i} team, there's no fear of that, buuuuut I {i}will{/i} be using three Pokémon. So don't get swept awaaaaay!~"

        $ passedclass = True
        jump aftertutorintrowater
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis

else:#generic scene
    show wallace with dis
    wallace @happy "[timeOfDay], my fabulous students! Today, let's all conduct ourselves with elegance and decorum."
    hide wallace with dis
    show wallacebg with dis
    wallace "Please open your textbooks to page... oh, I'm falling asleep already. Nevermind, let's all go to the pool!"
    narrator "Class proceeds without incident."

return

label movetutorwater:
show wallace with dis
wallace @surprised "Oh-ho, you want your Pokémon to learn moves directly from a Champion? Well, at Kobukan, you can do that!"
wallace @happy "I can teach Healing Spring, which causes it to rain for five turns, and restores a little health to the user every turn."
if (4.1 in persondex["Instructor Wallace"]["ClassesKnown"]):
    wallace @talkingmouth "But still tactics aren't for everyone, darling. If you want to surge out of the gate like a rush of water, try Aqua Jet! It {i}always{/i} hits first."

label aftertutorintrowater:
$ taughtmove = None

menu:
    ">Learn Healing Spring":
        $ taughtmove = "Healing Spring"
    ">Learn Aqua Jet" if (4.1 in persondex["Instructor Wallace"]["ClassesKnown"]):
        $ taughtmove = "Aqua Jet"
    "Nevermind":
        wallace @sad "Don't back out now, darling!"

        if (passedclass):
            jump aftertutoring
        else:
            jump afterwatersetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        wallace @sad "Don't back out now, darling!"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    wallace @sad "Oh, darling, there are some things not even a Champion can do. That Pokémon simply can't learn [taughtmove]."

jump aftertutorintrowater

label itemcraftwater:
show wallace with dis

wallace @talkingmouth "Inner beauty is one thing, but true stars know how to accentuate their outsides with glimglams galore!"
wallace @happy "A Mystic Water--which comes in stylish pendant form--boosts the power of Water-type moves by 10%%! My Champion team held a few back in the day."

menu:    
    ">Craft Mystic Water" if (3.1 in persondex["Instructor Wallace"]["ClassesKnown"]):
        $ GetItem("Mystic Water", 1, "You polish, shine, buff, and round an aquamarine gem to perfection. Wallace compliments your craftsmanship.")
        jump endclasscraft
    "Nevermind":
        wallace @happy "Come back anytime, darling!"
        jump afterwatersetup
