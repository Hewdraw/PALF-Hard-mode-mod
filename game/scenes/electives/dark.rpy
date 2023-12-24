label darkelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0
show darkclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "dark"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. DARK        #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call silverevent from _call_silverevent
call ethanevent from _call_ethanevent_1

label afterdarksetup:

if (2.1 in persondex["Instructor Karen"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutordark

        ">Craft items" if (3.1 in persondex["Instructor Karen"]["ClassesKnown"]):
            jump itemcraftdark

if (persondex["Instructor Karen"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Karen"]["ClassesKnown"].append(1)
    $ renpy.pause(1.0, hard=True)

    show serena uniform at rightside with dis
    show cheren uniform thinking with dis

    ethan uniform "Hey, look, Sarasvati and Chalupa are sitting there at the front!"

    red uniform "Serena and Cheren, but sure."#FIX THIS: When April 30th happens
    red @thinking "Cheren's writing something down in his notebook... and Serena has her nose in a book."

    ethan "You'd think that they'd talk to each other if they're sitting together! They're both Student Council nerds."

    red "Hey, Serena, Cheren."

    serena @happy "[first_name]! What a pleasant surprise."
    cheren -thinking "Good to see you here."

    hide cheren with dis
    hide serena at rightside with dis

    pause 1.0

    show karen:
        xpos 800 alpha 0.0
        ease 1.25 xpos 720 alpha 1.0

    $ lowerday = timeOfDay.lower()
    karen @talking2mouth "Good [lowerday], students."

    show karen:
        xpos 720 alpha 1.0

    if (not IsDate(5, 4, 2004)):
        karen @talkingmouth "I see we have some new students. Fantastic. Everyone else, please pay attention while I greet them. This will still be relevant to you."

    $ BecomeNamed("Instructor Karen")
    karen @closedbrow talking2mouth "I'm your teacher, Karen, and I'll be overseeing your {color=#0048ff}Dark-type class{/color} for this year."
    karen @talkingmouth "Let me personally welcome you to Kobukan Academy's Dark Class.{w=0.5} I'm sure you're all aware about how rigorous Kobukan's curriculum and expectations are, and my class is no exception."

    ethan @thinking "Yeah... we've heard."

    karen @angrybrow talking2mouth "Many students drop out before the second day of classes after hearing about it."
    karen @closedbrow talking2mouth "Judging by the looks on your faces, I'm assuming you won't run away from the challenge."

    pause 1.0

    karen @talking2mouth closedbrow "That's good."
    karen @happy "It takes courage to face insurmountable odds."

    hide karen with dis

    pause 0.5
    
    show karenbg behind cheren with dis

    karen "However, if you think courage alone is enough to survive the trials of this academy, then you are sadly mistaken."
    karen "Tell me, students, what is the most essential aspect of your Pokémon?"

    redmind @thinking "That question gets thrown around all the time, but I doubt there's a correct answer."

    karen "Tough question, right?"
    karen "Then let me put it this way.{w=0.5}"
    $ renpy.music.set_volume(0.0, delay=0.0, channel="ctc")

    karen "If you were going to compete at the Pokémon league, which Pokémon will you bring with you?"

    show cheren uniform with dis:
        xpos 1050 ypos 1.3

    cheren @surprisedbrow sadmouth "The strongest ones."

    if (IsDate(5, 4, 2004)):
        karen "Your name?"
        cheren @sadmouth "Cheren."

    karen "Stand up, please."

    show cheren:
        ypos 1.3 xpos 1050
        ease 0.5 ypos 1.0

    pause 0.5

    karen "And why do you think that, Cheren?"

    cheren "Why?{w=0.5} Because having the strongest Pokémon will result in the highest chance of competing with the other Trainers in the League."
    
    show serena uniform with dis:
        xpos 1400 ypos 1.3

    serena @happymouth "I agree."

    if (IsDate(5, 4, 2004)):
        karen "Oh? And what is your name?"
        serena @happy "Serena, miss."

    karen "Stand up, please, Serena."

    show serena uniform:
        ypos 1.3 xpos 1400
        ease 0.5 ypos 1.0

    serena @closedbrow happymouth "I agree with Cheren's logic."
    serena @talkingmouth "Only the most capable Trainers make it to the Pokémon League.{w=0.5} Bringing weaker Pokémon along will only serve to be a liability."

    karen "I see your reasoning, but that should not be the priority in choosing your team."
    cheren @surprised "Then is it the type of Pokémon?{w=0.5} Their nature?"
    cheren @thinking "It's impossible to plan beforehand so the only foolproof way to ensure victory is improving their performance."
    cheren @surprisedmouth "What other criteria could there possibly be?"
    show cheren surprised with dis
    show serena surprised with dis

    show silver uniform angry:
        ypos 2.0 xpos 0.25
        ease 0.2 ypos 1.0

    silver "What's wrong with you idiots? Do you guys not have a single heart between you?"
    silver "You can partner with the strongest Pokémon in the world, and it won't do shit for you if you only treat it like something to 'increase your odds.'"

    pause 2.0

    show serena sad
    show cheren sad 
    with dis

    silver angrybrow @talkingmouth "{i}A liability.{/i} How dare you."

    hide silver at leftside with dis

    pause 2.0

    karen "See me after class, please."

    pause 1.0

    hide karenbg with dis

    pause 1.0

    show cheren:
        ease 0.5 xpos 600

    show karen frownmouth with dis

    karen @closedbrow sadmouth "...Now, though your classmate's method of imparting his knowledge was unnecessarily adverse, I must stress that he {i}is{/i} correct."
    
    show cheren surprised
    show serena surprised
    with dis

    karen @angrybrow talking2mouth "You must also love and trust your Pokémon implicitly."
    karen @angrybrow talking2mouth "You must have faith in them as they have faith in you."

    show cheren sad
    show serena sad 
    with dis
    
    karen @sad "They are {i}not{/i} your tools.{w=0.5} They are your partners, your friends."

    $ renpy.pause(0.7, hard=True)
        
    karen @talking2mouth "Strong Pokémon. Weak Pokémon.{w=0.5} That is only the selfish perception of people."
    karen @talkingmouth "Truly skilled Trainers should try to win with the Pokémon that love them most."

    ethan @closedbrow talking2mouth "Huh, that feels... very quotable."

    karen @closedbrow talking2mouth "The responsibility is not all on your Pokémon.{w=0.5} They are not battling for themselves!"

    show cheren:
        xpos 600 ypos 1.0
        ease 1.5 ypos 2.0

    show serena:
        xpos 1400 ypos 1.0
        ease 1.5 ypos 2.0

    $ renpy.pause(1.0, hard=True)

    narrator "Karen scolds you for a little while longer about how flawed your mentality is."
    narrator "Silver, you note, is nodding enthusiastically every couple minutes, while most other students hang their heads in shame."

    karen @talking2mouth "That marks the end of class. We'll continue this discussion tomorrow."
    karen @angrybrow talkingmouth "And maybe, if you're lucky, we get to some talk about Dark-type Pokémon!"

    hide karen with dis
elif (2.1 not in persondex["Instructor Karen"]["ClassesKnown"] and classstats["Dark"] >= 10):#Enshroud
    show karenbg with dis
    if (2 not in persondex["Instructor Karen"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is studying hard as Karen walks around the classroom, looking over people's shoulders."

        hide karenbg with dis

        pause 1.0

        show karen with dis

        karen @talking2mouth "[first_name], right?"

        red @surprised "Oh! Um, yeah."

        karen @talkingmouth"You're doing well. I think you're ready to advance in this class."

        red @happy "Wow! Thanks, Ma'am."

        karen @sadbrow talking2mouth"...I do have one reservation, though."

        red @thinking "Uh... what's that, Ma'am?"

        karen @closedbrow talking2mouth "You need to learn how to be even a tiny bit more covert."

        red @surprised "Covert?"

        karen @talking2mouth "It's clear from your face exactly what you're going to do at every single turn of the battle."
        karen @closedbrow angrymouth "A Pokémon battle where your opponent can tell exactly what you're thinking is not one you'll win."

        red @sad "Oh. Well, I'm not sure that I can do anything about that..."
        red @happy "I, uh, I kinda wear my heart on my sleeve."

        karen @surprised "A heart's a pretty vulnerable thing to not keep enshrouded in your body."

        red @talking2mouth "Um..."

        karen @closedbrow talking2mouth "Figure it out. Otherwise your Pokémon losing their battles will be {i}your{/i} fault."

        red @surprised "N-no, I know that, I just..."

        karen @talking2mouth "When you learn to hide your intentions, for your Pokémon's sake, I'll teach them a new technique. {i}Enshroud.{/i}"

        red @thinking "I don't think I've heard that one..."

        karen @talkingmouth "My Pokémon developed it, with my guidance. It'll protect your Pokémon from harm for one turn, and raise their evasiveness one stage if the foe uses a long-ranged move."

        red @surprised "Woah! That sounds useful for stall strategies..."

        karen @closedbrow talking2mouth "There's something to be said for not charging out into battle blindly. A little time in the shadows does wonders for your odds."

        pause 1.0

        karen "Enough talk. Class, gather around. [first_name] is going to take his advancement exam."

        show serena uniform at rightside with dis

        serena @happy "Best wishes. I'm sure you'll prevail."
       
        show silver uniform at leftside with dis

        silver "Don't mess up."

        show cheren uniform at midrightside behind karen with dis

        cheren uniform "..."

        hide cheren with dis

        redmind @thinking "Some words of encouragement."

        karen @talkingmouth "I will be using one Pokémon. Choose one Pokémon from your party and pin all your hopes to them."

        $ persondex["Instructor Karen"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Ma'am, I'm ready to try my advancement exam again. Please give me another shot."

    karen @closedbrow talking2mouth "Don't disappoint your Pokémon. That's all I ask. As long as you avoid that, I'll be happy. {color=#0048ff}Dark-types will have the advantage here.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    karen @talking2mouth "Let's begin. And remember, don't make it so obvious what your next move will be."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("karen", TrainerType.Enemy, [
        Pokemon(102, level=11, moves=[GetMove("Absorb"), GetMove("Hypnosis"), GetMove("Reflect"), GetMove("Leech Seed")], ability="Chlorophyll")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_25
    $ gymbattles["Instructor Karen1"]  = _return

    show karen with dis

    if (WonBattle("Instructor Karen1")):
        $ persondex["Instructor Karen"]["ClassesKnown"].append(2.1)

        karen @talkingmouth "Your Pokémon was absolutely fantastic."
        
        red uniform @happy "And me?"

        karen @closedbrow talkingmouth "...Room for improvement."
        
        redmind @thinking "Geez."

        $ passedclass = True

        jump aftertutorintrodark
    
    else:
        pause 2.0

        hide karen with dis

        redmind uniform @thinking "Oof. Not even a word... that was an embarrassing loss. Still, at least I learned something..."

    hide karen with dis
elif (3.1 not in persondex["Instructor Karen"]["ClassesKnown"] and classstats["Dark"] >= 20):#Black Glasses
    show karen with dis
    if (3 not in persondex["Instructor Karen"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        karen @talking2mouth "[first_name], head up."

        red uniform @talkingmouth "Instructor Karen?"

        karen @talking2mouth "What I said before about hiding your intentions... you've started to be a bit more subtle."

        red @surprised "Really? I didn't even notice! I guess I was being even more subtle than I thought."

        karen @talkingmouth "Mm. You know what really helps you hide what you're doing next?"

        red @confused "Acting classes?"

        karen @happy "Actually, yes. But that's not what I'm thinking of. Glasses."

        red @confused "Huh?"

        karen @angrybrow talking2mouth "Glasses are really versatile. Just putting them on can reframe your face, giving you an entirely different appearance and vibe to other people."

        karen @happybrow talkingmouth "And Black Glasses, with dark shades, hide your eyes, preventing your opponent from knowing where you're looking. This strategy works well for Pokémon, too."

        karen @talkingmouth "A simple pair of Black Glasses can increase the power of a Dark-type Pokémon's moves by 10%%."

        red @closedbrow talking2mouth "Huh. I never would've guessed that. Do you have any I could use?"

        karen @closedbrow talking2mouth "No."

        red @talking2mouth "Oh."

        karen @talking2mouth "But if you pass this advancement exam, I'll teach you how to make them yourself."

        red @surprised "Oh! Okay! Let's do it!" 

        $ persondex["Instructor Karen"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Instructor Karen, my Pokémon and I have trained, and are ready to take the advancement exam again."

    karen @talkingmouth "I'm glad to hear it. {color=#0048ff}I'll be using a Dark-type.{/color} I trust you know how to handle them."

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    karen @talking2mouth "Time to battle, then. Don't disappoint your Pokémon with a sub-par performance."
    
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("karen", TrainerType.Enemy, [
        Pokemon("Houndour", level=21, moves=[GetMove("Bite"), GetMove("Smog"), GetMove("Howl"), GetMove("Ember")], ability="Flash Fire", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_76
    $ gymbattles["Instructor Karen2"]  = _return

    show karen with dis

    if (WonBattle("Instructor Karen2")):
        $ persondex["Instructor Karen"]["ClassesKnown"].append(3.1)

        karen @happy "Your Pokémon battled with finesse and grace."
        
        red uniform @happy "And me?"
        
        karen @talkingmouth closedbrow "...Don't go begging for compliments. It's undignified."
        
        redmind @thinking "Geez."

        $ GetItem("Black Glasses", 1, "You gained a pair of Black Glasses! You feel kinda like mafia!")

        red blackglasses @angrybrow talking2mouth "I'm on a mission. From God."

        karen @happy "Hah. Don't get ahead of yourself. You're a few challenges away from Big A noticing you."

        jump aftertutoring
    
    else:
        pause 2.0

        hide karen with dis

        redmind uniform @thinking "Oof. Not even a word... that was an embarrassing loss. Still, at least I learned something..."

    hide karen with dis
elif (4.1 not in persondex["Instructor Karen"]["ClassesKnown"] and classstats["Dark"] >= 30):#Thief
    show karen with dis
    if (4 not in persondex["Instructor Karen"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        karen @talking2mouth "[first_name]. If you wanted something from someone who was antagonistic towards you, how would you get it?"

        red uniform @confused "Huh?"

        red @thinking "Well... I suppose I'd see if I had anything they wanted, and try to work out some sort of deal."

        karen @surprised "That's a valid strategy. Say your foe isn't willing to negotiate, though."

        red @thinking "I guess I'd just have to give up?"

        karen @sad ".{w=0.5}.{w=0.5}.{w=0.5}You wouldn't try stealing it?"

        red @surprised "Woah! Steal it? Yeah, I, uh... I really don't know about that one! I don't think I'd want to steal anything... unless it was a life-or-death situation, I mean."

        karen @closedbrow talking2mouth "...I appreciate your honesty. But be careful that your earnestness does not prohibit you from thinking outside of the box."

        red @thinking "{w=0.5}.{w=0.5}.{w=0.5}."

        red @happy "Oh! You're about to give me an advancement exam, aren't you?"

        karen @surprised "How do you figure?"

        red @happy "It's just that whenever you berate the way someone does something, you end the speech by saying something like 'but I see great potential in you, and that's why I'm letting you take the exam.'"

        karen @closedbrow frownmouth "...Hm."
        karen @happybrow talkingmouth "Perhaps I also need to think outside of the box once in a while, then."
        karen @talking2mouth "You're right, I'd like you to take the level 30 advancement exam."

        karen @talking2mouth "Do well enough, and I'll teach your Pokémon the move Thief. If they can learn it, of course."

        red @talkingmouth "I'm ready to take you on now, Instructor Karen."

        $ persondex["Instructor Karen"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Instructor Karen, I've studied since the last time we fought--and now I'm more than ready to beat you."

    karen @talking2mouth "We'll see. Pick one Pokémon. {color=#0048ff}Picking a Dark-type wouldn't be a great idea this time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    karen @angrybrow talking2mouth "Battle harder than you want to. It's the only way you'll win."

    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("karen", TrainerType.Enemy, [
        Pokemon("Hitmontop", level=31, moves=[GetMove("Counter"), GetMove("Pursuit"), GetMove("Rolling Kick"), GetMove("Rapid Spin")], ability="Intimidate", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_77
    $ gymbattles["Instructor Karen3"]  = _return

    show karen with dis

    if (WonBattle("Instructor Karen3")):
        $ persondex["Instructor Karen"]["ClassesKnown"].append(4.1)

        karen @talking2mouth "Well done. Your Pokémon have managed to beat a Pokémon weak to Dark-types, a Dark-type, and a Pokemon that was strong against Dark-types."
        karen @closedbrow talking2mouth "You've obviously mastered the basics. Future battles will be tougher, and I will be using three Pokémon. I expect you to rise to the challenge."
        karen @closedbrow "..."
        karen @happy "You should be proud of where you are now, though."

        $ passedclass = True

        jump aftertutorintrodark
    
    else:
        pause 2.0

        hide karen with dis

        redmind uniform @thinking "Oof. Not even a word... that was an embarrassing loss. Still, at least I learned something..."

    hide karen with dis

else:#generic scene
    show karen with dis
    $ lowerday = timeOfDay.lower()
    karen @closedbrow talkingmouth "Good [lowerday], students."
    karen @talking2mouth "The Dark type is one that excells in dirty tricks. In fighting underhandedly. And sometimes, that's the only way to correct injustice. Let's talk about this..."
    hide karen with dis
    show karenbg with dis
    narrator "Class proceeds without incident."

return

label movetutordark:
show karen with dis
karen @angrybrow talking2mouth "If you want your Pokémon to learn something new for you, you'd better learn something new for them. 'Learning a move' is a two-way street."
karen @talkingmouth "I can teach Enshroud, which is a move that protects your Pokémon for a turn, and raises their evasion by one stage if the opponent doesn't make contact."
if (4.1 in persondex["Instructor Karen"]["ClassesKnown"]):
    karen @closedbrow talkingmouth "I can also teach you the technique Thief. If your opponent is holding an item, and your Pokémon isn't, your Pokémon can take their item. You have to give items back at the end of battle, though."

label aftertutorintrodark:
$ taughtmove = None

menu:
    ">Learn Enshroud":
        $ taughtmove = "Enshroud"
    ">Learn Thief" if (4.1 in persondex["Instructor Karen"]["ClassesKnown"]):
        $ taughtmove = "Thief"
    "Nevermind":
        karen @talking2mouth "Fine. What next?"

        if (passedclass):
            jump aftertutoring
        else:
            jump afterdarksetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    karen @talking2mouth "Fine. What next?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    karen @angrybrow talking2mouth "Don't ask your Pokémon to do something impossible. This Pokémon can't learn [taughtmove]."

jump aftertutorintrodark

label itemcraftdark:
show karen with dis

karen @talking2mouth "Tools are an important part of any battle. Only a fool walks into a fight empty-handed."
karen @closedbrow talkingmouth "I've taught you how to craft the Black Glasses. They'll boost your Dark-type moves by 10%%."

menu:    
    ">Craft Black Glasses" if (3.1 in persondex["Instructor Karen"]["ClassesKnown"]):
        $ GetItem("Black Glasses", 1, "You craft the Black Glasses using tinted glass. You feel like Mafia.")
        jump endclasscraft
    "Nevermind":
        karen @talking2mouth "Fine. What next?"
        jump afterdarksetup