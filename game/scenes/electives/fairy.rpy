label fairyelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0

show fairytype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show fairyglow:
    alpha 0.75 xalign 0.5 yalign 1.0
    block:
        ease 2.25 alpha 0.5
        ease 1.8 alpha 1.0
        repeat
show fairylights:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "fairy"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. FAIRY       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call dawnevent from _call_dawnevent_1
call soniaevent from _call_soniaevent_1
call ethanevent from _call_ethanevent_4

label afterfairysetup:

if (2.1 in persondex["Instructor Valerie"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorfairy

        ">Craft items" if (3.1 in persondex["Instructor Valerie"]["ClassesKnown"]):
            jump itemcraftfairy

if (persondex["Instructor Valerie"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Valerie"]["ClassesKnown"].append(1)
    $ renpy.pause(1.0, hard=True)

    show whitney uniform happy with dis

    red uniform "Hey, Whitney. You're in this class, too?"

    whitney -happy "Yep, you bet! And it's so cool to see you two here!"
    ethan uniform happy "Hey, we're happy to be here, Whitley."
    whitney "You know, you two are the only guys I've ever met who are interested in Fairies!"

    red @confusedeyebrows "Huh? What do you..."
    red @surprised ".{w=0.5}.{w=0.5}.{w=0.5}"

    red @thinking "Wait. There's only one other guy in this class."
    ethan @surprised "Dude! Whatever the opposite of a sausage party is--we found it!"

    red @surprised "Wait a minute... "

    show calem uniform at rightside with dis:
        zoom 0.8

    red "Calem?"

    whitney "Oh, you know that guy? Yeah, he's... uh..."
    show calem happy with dis

    whitney happy "It's pretty clear he's just here for our teacher."

    show calem:
        zoom 0.8 xpos 0.75
        ease 0.2 zoom 1.0 xpos 0.75

    calem @thinking "In my defense, I didn't know the teacher, nor demographics, of this class before I joined." 
    calem @happy "I merely {i}suspected{/i} that there would be a lot of attractive women, and few men."

    whitney sad "Dude... that's what you say in your {i}defense{/i}?"

    calem sad "Point taken. I'll retreat now."

    hide calem at rightside with dis

    pause 1.0

    red "Well, I'm sure he wouldn't have stuck around if the class wasn't a good one. Looking forward to it."

    play sound "Audio/GenericDoorOpen.ogg"

    whitney happy "Oh, there's our teacher!"

    hide whitney with dis

    pause 0.75

    hide whitney

    show valerie with dis
    pause 2.0

    red "{i}She's our instructor?{/i}"

    ethan "Her clothes make her look like some kind of giant Butterfree.{w=0.5} Almost like she's gliding on something."

    show dawn uniform at leftside with dis:
        zoom 0.8

    $ BecomeNamed("Instructor Valerie")
    dawn happy "Oh, you see it too, right? That's Valerie's trademark! Each of her designs are inspired by Pokémon."
    
    red "A fashion designer, huh?"

    dawn -happy "Yeah. She's super-famous in all the regions, not just Kalos. I really respect her as an artist."

    hide dawn at leftside with dis
    
    ethan @happy "Not really my thing, but I can tell it's impressive!"

    hide valerie with dis

    pause 1.5

    show valeriebg with dis

    pause 1.5

    if (not (calDate.month == 4 and calDate.day == 5)):
        valerie "Oh, we have... many new students today? What serendipitous timing, right as I planned to debut a new garment..."

    valerie "Hello, young students.{w=0.5} My name is Valerie."
    valerie "I will be your instructor for the {color=#0048ff}Fairy course{/color} this semester."

    "Passionate Student" "\"It's really Valerie!{w=0.5} I think I'm gonna faint!\""
    "Fawning Student" "\"I can't believe it, but she's even prettier in person!\""
    "Squealing Student" "\"AHHH! I want one of her outfits SO BAD!!!\""

    red @surprised "Geez, Dawn wasn't kidding. Is everyone but us a fan of her?"
    ethan @thinking "I'll never understand girls and their fashion sense."

    pause 1.5

    valerie ".{w=0.25}.{w=0.25}."

    pause 1.5

    red ".{w=0.25}.{w=0.25}."

    pause 2.0

    valerie ".{w=0.25}.{w=0.25}."

    pause 2.0

    ethan @surprised "...Why is it so quiet all of a sud--"

    show classroom at vpunch
    show dawn uniform angry at leftside
        
    dawn "Shhh! Valerie is inspecting someone!"

    hide dawn at leftside with dis

    show valerie with dis

    hide valeriebg with dis

    red "Huh?"

    pause 2.0

    valerie "..."

    show valerie with dis

    $ renpy.pause(2.0, hard=True)

    valerie @talkingmouth "I like your bow."
    show valerie happybrow with dis

    "Fashionable Student" "\"{cps=10}M-m-m{/cps}-ME?!\""

    valerie @happymouth "Yes. The pastel blue on the end is like a Sylveon.{w=0.5} Her feelers are wrapped gently around the arm of her dear Trainer."
    valerie -happybrow @talkingmouth "Just as she is gentle, a bow must also convey a loving touch."

    red "'She?' Sylveon are 87.5 percent male."

    "Fashionable Student" "\"Oh, my god.{w=0.25} Oh, my god, oh, my god, I'm going to faint.{w=0.25} I'm going to--"

    play sound "Audio/Body Crash.ogg"

    pause 2.0

    ethan @thinking "Well, I'm already hopelessly lost. At least the girls can understand her fashion babble."
    red @happy "Seems like an opportunity, to me."
    ethan "Oh, yeah?"
    red "Sure. If you need help, then there's plenty of people to ask, right?"

    narrator "The rest of the class was spent on watching Valerie go down the line, commenting on every student's hair accessories and outfits."

    show valerie happy with dis

    hide dawn
    hide whitney

    narrator "Though you were certain she was gonna take a jab at some of the male class members' lack of fashionable distinction, she made sure to compliment all three of you."

    show whitney uniform surprised at rightside with dis

    show dawn uniform surprised at leftside with dis

    narrator "Whitney and Dawn seem to have done very well, as Valerie complimented them both."

    hide whitney at rightside with dis

    hide dawn at leftside with dis

    show valerie -happy with dis

    $ renpy.pause(2.0, hard=True)

    show valerie:
        xpos 700

    valerie @surprised "Oh, my goodness."
    valerie @happy "Forgive me.{w=0.5} I was so captivated I lost track of the time."

    hide valerie with dis

    pause 1.0

    show valeriebg with dis

    valerie "Farewell, my darling Beautifly.{w=0.5} Make sure to flutter to your next classes safely."

    hide valerie
elif (2.1 not in persondex["Instructor Valerie"]["ClassesKnown"] and classstats["Fairy"] >= 10):#Ardent Gaze
    show valerie with dis
    if (2 not in persondex["Instructor Valerie"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is working collaboratively on creating a dress woven out of Swirlix threads. Work is nearly complete, when..."

        valerie @happy "My, yes."

        red uniform @happy "Instructor Valerie? Did I do something?"

        valerie @talkingmouth "I have been thinking about who would best model this dress, when it's completed."

        red @happy "Oh, I'm flattered, but I don't think I'd fill it out the right way."

        valerie @talking2mouth "Certainly not."

        redmind @thinking "Ow. Didn't expect such rapid agreement."

        show ethan uniform at leftside 

        valerie @talkingmouth "You have a lovely figure, but you're a tad too broad-shouldered and tall. If you didn't run so much, perhaps..."

        ethan @happy "Wait, does that mean you were looking at me?"

        valerie @happy "I was looking at anyone with the will and desire to dazzle, my darling Beautifly."

        ethan @happy "Hey, I've got will and desire! I'll turn heads!"

        show calem uniform at rightside

        calem @talkingmouth "That you most certainly will. I suppose I'm lost as to the purpose of this lesson, though we've been working on it for a while." 
        calem @thinking "I don't think I've actually learned anything new about Fairy-types?"

        valerie @sad "Perhaps you just aren't learning what you expected to learn?"

        calem @talkingmouth "I... I have legitimately no idea how to respond to that."

        valerie @happy "Oh ho ho.~ Sweet Calem, the fairy type is not one that is directed toward some ultimate goal."

        valerie @thinking "It spreads out in all directions, trying a little bit of everything."

        calem @angrybrow talkingmouth "What does that mean, without metaphor?"

        valerie @talkingmouth "It means that life is to be lived, not directed. A steel spike will drive. A poison will corrupt. A dragon will rampage."

        ethan @thinking "And fairies...?"

        valerie @happy "Fairies simply {i}are.{/i}"

        valerie @talkingmouth "A Fairy will live about its day as it pleases. Unconcerned with endpoints or timetables."

        calem @angrybrow talkingmouth "I must insist we get even a modicum of applicable battle advice."

        show calem surprised with dis

        valerie @talkingmouth "Have fun."

        pause 2.0

        calem -surprised @surprised "...That's your advice? But what about power? What about skill? What about strategy?"

        red @thinking "I mean... I kinda see where Instructor Valerie is coming from."

        calem @surprised "[first_name]? Not you too."

        red @thinking "Fairy Pokémon are whimsical, y'know? If you force 'em to battle a certain way, they just won't be as strong as if you let them have fun." 
        red @happy "I mean, that's kinda true for all Pokémon."

        valerie @happy lightblush "True for people, too. Wear dresses. Drink tea. Sweat. Eat mushrooms. Sleep in the grass. Lick salt."

        ethan @surprised "That's the weirdest to-do list I've ever heard."

        valerie @sad "Nothing great was ever accomplished by someone who didn't have fun doing it."
        valerie @happy "But it doesn't matter, even, if you never accomplish anything great. Life is greatness. Fun is greatness. And play is the greatest."

        calem @sad "...I don't know that I'll ever be able to do that."

        valerie @happy "Then it's very, very good that you chose to take this class. Because I will now attempt to teach you."

        calem @surprised "Uh..."

        valerie @talking2mouth "Perhaps we could begin by having you be the model for this dress? And after that, I think I have some tea around here..."

        calem @sad "It is no exaggeration to say I would rather die than let the possibility of a picture of me in a cotton-candy dress exist."

        ethan @happy "I'm down! And I won't even eat any of it!"

        red @happy "Yeah, Ethan'd look cute."

        valerie @happy "You make a compelling argument."

        valerie @talkingmouth "How about I give you this class' advancement exam--a one-on-one battle--and if you succeed, then I will let your friend be the dress' first model?"

        red @happy "Sure! Sounds good!"

        show ethan surprised at getcloser, leftside with dis

        ethan "Dude! You {i}have{/i} to win this for me!"

        red @surprised "Wow, that's passion. I mean, I'll do my best."

        show ethan happy at getfurther, leftside with dis

        valerie @talkingmouth "Oh. Yes. If you win, then you'll also get access to the move {i}Ardent Gaze{/i}. A client of mine developed it, then taught it to me."

        red @thinking "Huh? What does that do?"

        valerie @happy "Oh, it infatuates the foe."

        calem @talkingmouth "If?"

        valerie @talkingmouth "No. No ifs."

        calem @surprised "How my boundaries are expanding..."

        $ persondex["Instructor Valerie"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Valerie, I've done a bit more studying since the last time we fought--and now I'm ready to get Ethan in that dress!"

    valerie @talkingmouth "If you're ready, please pick one Pokémon to face me. {color=#0048ff}A Fairy-type will shine most dazzlingly here.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    valerie @happy "Let's have fun with this."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("valerie", TrainerType.Enemy, [
        Pokemon(559, level=11, moves=[GetMove("Payback"), GetMove("Low Kick"), GetMove("Leer"), GetMove("Headbutt")], ability="Intimidate")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_28
    $ gymbattles["Instructor Valerie1"]  = _return

    show valerie with dis

    if (WonBattle("Instructor Valerie1")):
        $ persondex["Instructor Valerie"]["ClassesKnown"].append(2.1)

        valerie @happy "Well done. I can tell you had fun."

        ethan uniform @sadbrow happymouth "Aaaaand?"

        valerie @talkingmouth "And I'm sure Ethan will look fantastic when the dress is completed."

        ethan @happy "Yes!"

        $ passedclass = True

        jump aftertutorintrofairy
    
    else:
        valerie @happy "Don't be sad. That was a fun battle."

        ethan uniform sad "Oh no..."

        valerie @talkingmouth "Fear not. The dress still requires a bit more time until it's finished. I'm certain [first_name] will win before then."

        red uniform @sadeyes sadeyebrows talkingmouth "Sorry, Ethan. I'll do better next time."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide valerie with dis
elif (3.1 not in persondex["Instructor Valerie"]["ClassesKnown"] and classstats["Fairy"] >= 20):#Pink Bow
    show valerie with dis
    if (3 not in persondex["Instructor Valerie"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        valerie @happy "[first_name]?"

        red uniform @happy "Instructor Valerie?"

        valerie @talkingmouth "I'd like to move you up a class. Are you ready to take the class' advancement exam?"

        red @surprised "Oh! Oh, yeah, definitely. What do I get if I move up in a class?"

        valerie @surprised "'Get?'"

        red @talkingmouth "Yeah. Like, every time I advance a rank in a class, I, um, like get some kinda reward, right?"

        valerie @talkingmouth "Yes, that's right. But you already have the skills you need."

        red @confused "Um... the power to believe in myself?"

        valerie @closedbrow talkingmouth "That's important, but no. I was talking about dextrous fingers and the ability to weave cloth."
        valerie @talkingmouth "I've seen how you've been working on our various projects in this class, and you definitely have the skills necessary to craft a simple Pink Bow now."

        red @thinking "Oh, okay. What does a Pink Bow do?"

        valerie @talkingmouth "It's a lovely accent piece that goes well with aqua and pastel yellow."

        pause 1.0

        valerie @talkingmouth "Also, it boosts the power of your Fairy-type moves by 10%%."

        red @happy "Ah!"

        valerie @happy "If you pass this advancement exam, I'll give you one to base your design off of. And I'll let you make more of them in class."

        valerie @talkingmouth "How does that sound?"

        red @talkingmouth "Sounds great, Instructor!"

        $ persondex["Instructor Valerie"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Instructor Valerie, I've done a bit more studying since the last time we fought, and now I'm ready to take the advancement exam."

    valerie @talkingmouth "If you're ready, please pick one Pokémon to face me. {color=#0048ff}I will be using a Fairy-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    valerie @happy "Let's have fun with this."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("valerie", TrainerType.Enemy, [
        Pokemon("Sylveon", level=21, moves=[GetMove("Swift"), GetMove("Baby-Doll Eyes"), GetMove("Quick Attack"), GetMove("Disarming Voice")], ability="Cute Charm", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_82
    $ gymbattles["Instructor Valerie2"]  = _return

    show valerie with dis

    if (WonBattle("Instructor Valerie2")):
        $ persondex["Instructor Valerie"]["ClassesKnown"].append(3.1)

        valerie @happy "Well done. You've very much earned this little item. I hope you can wear it with pride."

        red @happy "Me? Um... yeah, I think I'll... pass."

        valerie @talkingmouth "Oh, well. Keep it in mind, at least."

        $ GetItem("Pink Bow", 1, "Instructor Valerie tenderly places the bow in your palm while glancing meaningfully at your head.")

        jump aftertutoring
    
    else:
        valerie @happy "Don't be sad. That was a fun battle."

        red uniform @sad "Aw, man..."

        valerie @talkingmouth "Don't worry, my Beautifly. You'll have plenty more chances to try the exam. Loss doesn't mean defeat."

        redmind @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide valerie with dis
elif (4.1 not in persondex["Instructor Valerie"]["ClassesKnown"] and classstats["Fairy"] >= 30):#Draining Kiss
    show valerie with dis
    if (4 not in persondex["Instructor Valerie"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "You're diligently bent over an Aromatisse, tickling its nose to get it to exhale some of its valuable perfume, when you notice Professor Valerie has been standing behind you, looking over your shoulder for a while."

        red @talkingmouth "Instructor Valerie?"

        valerie @happy "I was just thinking of what a good job you're doing."

        red @talkingmouth "Aw, thanks. Still got a way to go, though. I'm getting too much of the perfume on my fingers."

        pause 1.0

        valerie sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        pause 0.5

        red @confused "Um... did I say something wrong?"

        valerie @talkingmouth "Of course not, my darling. It's just... men often have difficulty accepting compliments, don't they?"

        red @closedbrow talking2mouth "Uh... I never really thought about that before..."

        valerie @closedbrow talking2mouth "Society always says men must keep forging on. They must keep working, harder, and faster. There's no time to play... there's no room for contentedness."

        red @talking2mouth "I mean, I think {i}some{/i} parts of society are probably like that. I've never felt especially rushed along, though."

        valerie @surprised "Isn't your goal to become a Pokémon Champion?"

        red @talking3mouth "Sure. But that's just... well, I want to be a Champion because {i}I{/i} want to. Not because society forced me to."

        pause 0.5

        red @confused "I mean, I think. I dunno. I guess, if society {i}did{/i} force me into it, I probably wouldn't know?"

        valerie -sadbrow -frownmouth @happy "I'm very glad that you've been spared from the meanness of life, then."

        red @talkingmouth "Thank you. And, um, thank you for the compliment earlier. I guess I probably could've avoided all this if I'd just accepted the compliment."

        valerie @talkingmouth "But then we would have missed out on this delightful conversation."

        red @thinking "Yeah. I guess. It's hard to know what the paths you didn't take might have lead to."

        valerie @surprised "Oh!"

        red @surprised "Huh?"

        valerie @happy "That's very wise, [first_name]. In fact, I think you should take the advancement exam."

        redmind @confused "Huh? Just quoting one of my grandpa's old platitudes got me into the advancement exam?"

        valerie @talkingmouth "If you pass this exam, I will be more than happy to tutor your Pokémon in the usage of the move Draining Kiss."

        red @talkingmouth "Hm... is there a metaphor to that? Like... love is draining, or something?"

        valerie @sadbrow talking2mouth "If there {i}is{/i} a metaphor, it might be best not to dig too deeply for it."

        red @talkingmouth "Right, I see what you mean."

        $ persondex["Instructor Valerie"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Instructor Valerie, I've done a bit more studying since the last time we fought, and now I'm ready to take the advancement exam."

    valerie @talkingmouth "If you're ready, please pick one Pokémon to face me. {color=#0048ff}I would not recommend using a Fairy-type in this instance.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    valerie @happy "Let's have fun with this."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("valerie", TrainerType.Enemy, [
        Pokemon("Varoom", level=31, moves=[GetMove("Iron Head"), GetMove("Screech"), GetMove("Headbutt"), GetMove("Sludge")], ability="Overcoat", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_83
    $ gymbattles["Instructor Valerie3"]  = _return

    show valerie with dis

    if (WonBattle("Instructor Valerie3")):
        $ persondex["Instructor Valerie"]["ClassesKnown"].append(4.1)

        valerie @happy "Well done. Your skill with Pokémon is genuinely one of the best I've seen in many years."

        red uniform @happy "Ah, I'm sure it wasn't--"

        pause 1.0

        red @talkingmouth "Uh, thank you. Thank you is what I meant to say."

        valerie @talkingmouth "Well done."

        $ passedclass = True

        jump aftertutorintrofairy
    
    else:
        valerie @happy "Don't be sad. That was a fun battle."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide valerie with dis

else:#generic scene
    show valerie with dis
    valerie @talkingmouth "Greetings, my darling Beautifly. Prepare yourselves for a magical experience as we delve deeper into the Fairy type."
    valerie @happy "...But before we do that, I'd like to mention that you're all looking resplendent today. Yes, especially you."
    hide valerie
    show valeriebg 
    with dis
    narrator "Class proceeds without incident."

return

label movetutorfairy:
show valerie with dis
valerie @talkingmouth "Moves are like a Pokémon's wardrobe. So, what would you like me to add to yours?"
valerie @happy "I can teach Ardent Gaze, which is a move that infatuates the foe."
if (4.1 in persondex["Instructor Valerie"]["ClassesKnown"]):
    valerie @closedbrow talkingmouth "If you want to go more on the offensive, then you could try out Draining Kiss. It damages {i}and{/i} heals. Quite useful."

label aftertutorintrofairy:
$ taughtmove = None

menu:
    ">Learn Ardent Gaze":
        $ taughtmove = "Ardent Gaze"
    ">Learn Draining Kiss" if (4.1 in persondex["Instructor Valerie"]["ClassesKnown"]):
        $ taughtmove = "Draining Kiss"
    "Nevermind":
        valerie @sad "Oh... perhaps none of these designs caught your eye?"

        if (passedclass):
            jump aftertutoring
        else:
            jump afterfairysetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    valerie @sad "Oh... perhaps none of these designs caught your eye?"
elif (MonCanLearn(newmon, taughtmove)):
    $ playerparty[newindex].LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    valerie @sad "I'm sorry, this Pokémon is made of a cloth that I don't believe I can tailor."
    
jump aftertutorintrofairy

label itemcraftfairy:
show valerie with dis

valerie @happy "Ah... craft. You can use them to spice up your Pokémon's appearance. But there are some practical applications, too."
valerie @closedbrow talkingmouth "A simple pink bow, in addition to being a lovely accent piece, increases the power of your Pokémon's Fairy-type moves by 10%%. It does the same thing for humans, too."

menu:    
    ">Obtain Pink Bow" if (3.1 in persondex["Instructor Valerie"]["ClassesKnown"]):
        $ GetItem("Pink Bow", 1, "You quickly sow a pink bow. You mentally remind yourself to help your Mom with the sewing more when you get home, now that you've gotten good at it.")
        jump endclasscraft
    "Nevermind":
        valerie @sad "Perhaps you couldn't find something that complimented your wardrobe, then?"
        jump afterfairysetup