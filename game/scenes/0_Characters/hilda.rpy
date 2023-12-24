init python:
    def HildaHasUnseenScene():
        if (GetCharValue("Hilda") >= 10 and GetRelationship("Hilda") != "Caretaker"):
            return "Hilda1"
        return False

label Hilda1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Hilda"]["Events"].append("Level2SceneVer2")

scene hall_B 
show hilda
with Dissolve(2.0)
$ renpy.music.queue("Audio/Music/Nuvema2_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Nuvema2_Loop.ogg", channel='music', loop=True, tight=None)

red @talkingmouth "Hey, Hilda."

hilda @surprised "[first_name]?"
hilda @happy "Oh, shit, good to see you!"

if (not IsBefore(1, 5, 2004)):
    red @surprised "Really?"

    hilda @surprised "Uh, yeah? What do you mean, 'really'?"

    red @sadbrow talkingmouth "Well... I just meant, you know, with the whole 'powers' thing..."

    hilda @talkingmouth "Water under the bridge."
    hilda @happy "I'll be real, I was {i}kinda{/i} on the fence at first, but after you explained the whole situation during the Quarter Qlashes..."
    hilda @sadbrow talkingmouth "I mean, how could I hold it against you? It's seriously effed up what you went through. I can't believe Cheren..."

    red @sadbrow talkingmouth "Thanks for being so understanding."

    hilda @sadbrow smirkmouth "That's me. Understanding to a fault." 
    hilda @talkingmouth "Are you doing anything big right now?"

    red @talkingmouth "Not really, no. What about you?"

red @talkingmouth "What're you up to?"

if (IsBefore(1, 5, 2004)):
    $ persondex["Hilda"]["Events"].append("KetchupSpilledOnSerena")
    hilda @talkingmouth "Oh, I was just going to the Student Center. Bianca spilled a ton of ketchup on Serena's bed, so I'm going to the laundry rooms."

    red @confusedeyebrows talking2mouth "What was Bianca doing with ketchup on Serena's bed?"

    hilda @sad "Eh... the girls of Dorm 251 have agreed never to talk about it again, so I can't really tell you."

else:
    $ persondex["Hilda"]["Events"].append("KetchupSpilledOnBea")
    hilda @talkingmouth "Oh, I was just going to the Student Center. Bianca spilled a ton of ketchup on Bea's bed, so I'm going to the laundry rooms."

    red @confusedeyebrows talking2mouth "What was Bianca doing with ketchup on Bea's bed?"

    hilda @sad "Dorm 251 has agreed to never talk about it again, so I can't really tell you."

red @happy "Aw, you tease."

hilda @talkingmouth "Anyway, what's up with you? Mind if we walk and talk? I'm pretty busy."

red @talkingmouth "Oh, yeah, sure."

narrator "Hilda quickly strides ahead, and you need to speedwalk after her to keep up."

red @happy "So, what're you doing after this?"

hilda @thinking "Ugh, I don't even know."

if (IsBefore(1, 5, 2004)):
    hilda @sad "I mean, after I do the laundry, I've got to restock the dorm fridge. May likes to make sure there's always a plate of cookies on the counter, and Leaf gets moody if there isn't. So I gotta help May with the cooking."
    hilda @thinking "After that, I've gotta research cute date restaurants in Inspira for Serena. She's got some sort of plan there, didn't have time to ask."
    hilda @talkingmouth "And Bianca's been really busy helping Nate and Cheren with their own projects, so her Pokémon need some walking. Said I'd do that for her. My Aron could do with a walk, too."
    hilda @happy "And, y'know, after {i}that,{/i} I've gotta do my own studying for class. Professor Sycamore's being a real hardass, says I'm not 'applying' myself."
    hilda @sad "And after {i}that...{/i} ugh, it's been like twelve hours since I checked in on Hilbert. He's probably choked to death on his own foot by now."

else:
    hilda @sad "I mean, after I do the laundry, I've got to restock the dorm fridge. Hilbert and Bea both have insane sweet tooths, so any time I look away from the fridge for half a second, all the food disappears."
    hilda @thinking "After that, I've gotta do some research into Unovan mythology with Nate. He's got this project he's working on, and I promised I'd help."
    $ aron_name = hildaaronobj.GetNickname()
    hilda @talkingmouth "And Bianca's been really busy helping Nate with that project I mentioned, so her Pokémon need some walking. Said I'd do that for her. My [aron_name] could do with a walk, too."
    hilda @happy "And, y'know, after {i}that,{/i} I've gotta do my own studying for class. Professor Sycamore's being a real hardass, says I'm not 'applying' myself."
    hilda @sad "And after {i}that...{/i} ugh, it's been like twelve hours since I checked in on Hilbert. He's probably choked to death on his own foot by now."

red @thinking "Hm."

pause 2.0

red @happy "Hey, my running shoes are getting pretty old. Do you think you could grab a new pair for me next time you're in Inspira?"

hilda @happy "Sure, what size are you?"

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

hilda frownmouth @closedbrow sadmouth "Ah. That was, uh, a joke, then?"

red @thinking "More like a point. I haven't really known you for that long, Hilda, but doesn't your schedule seem {i}very{/i} full?"

hilda @sad "I mean, yeah, it is... but so what? I can handle it."

red @thinking "It just seems to me... putting this delicately... that most of your to-do list is for other people."

hilda @thinking "I can still handle it, though."

red @confusedeyebrows talkingmouth "I don't doubt that. But do you really need to? Pretty sure your roommates could handle their own chores."

hilda @sad "Yeah, probably."

red @happy "Right? So how about the next time they ask you to do something, you remind them of the {i}last{/i} time you did something for them?"

hilda @happy "Ah, yeah, nah, that won't work. They don't actually ask me to do this stuff for them."

red @thinking "What do you mean?"

hilda @talkingmouth "I, uh... I just do it. 'Cause they want it done, and it needs to be done. So I just do it."

redmind @thinking "Oh, boy. So this is a self-inflicted lifestyle, then."
redmind @thinking "I guess it makes sense. Hilda's not the kind of woman who's a pushover, and can be forced to do things."
redmind @thinking "More like she pushes other people over, and forces them to let her do things."

red @confusedeyebrows "Wow. You've got a pretty intense sense of responsibility."

hilda @sad "More like obligation."

red @talkingmouth "Hey, speaking of obligation, what's up with you and Hilbert?"

hilda @surprised "What? I... "
hilda @thinking "Eh, what the hell. I guess it's fine."

if (not IsBefore(1, 5, 2004)):
    hilda @smirkmouth "After all, if you wanted this info, your mind powers could just take it from me, right?"

    red @closedbrow talking2mouth "Not in the slightest."

hilda @talkingmouth "Basically, Hilbert and I were raised together. His parents were often gone, doing missions for this Pokémon-rights organization they were part of."

red @thinking "Sounds noble."

hilda @thinking "Yeah, it was. Anyway, I took care of him, since I was already used to taking care of my Dad."

red @surprised "Aren't you the same age? You and Hilbert I mean, not your Dad."

hilda @happy "Almost. I'm nineteen, he's eighteen. But girls mature faster than boys--and even for a boy, he's hopeless."

red @angrybrow frownmouth "I resemble that remark."

hilda @thinking "Right, so where was I... oh, yeah, I took care of him." 
hilda @talkingmouth "He'd go out and train, and I'd stay home and cook, put his clothes out, made sure he did his homework."
hilda @thinking "I mean, I never thought it'd be a long-term thing. One day, I figured, he'd grow up into, y'know, a 'proper young man' who could handle his own dirty underwear."
hilda @talkingmouth "Or his parents would come back from their missions and just stay with their damn kid."

pause 2.0

hilda @sad "...But that never happened."

red @surprised "Wait, which one? Hilbert never grew up, or his parents never came back from their missions?"

hilda @closedbrow talkingmouth "Both."

hilda @sad "Guess it's not really his fault. I mean, he was practically raised by another kid. How do you {i}really{/i} grow up in an environment like that? The guy still wants to eat ice cream for every meal."

red @surprised "Uh..."

hilda @closedbrow talkingmouth "Actually, he got worse. Like, he was always single-minded, but now he's just obsessive as hell about his 'dream.'"
hilda @angrybrow talkingmouth "Like, he doesn't even care if he eats or sleeps, because all he can think about is that damn dream of his. I sometimes wish I had a Munna I could just slam on his head and {i}eat{/i} that dream out of him!"
hilda angry "And, y'know, it's one thing to have a goal and a plan to get there, but he sees the world like a child! It's all black and white with him, there's absolutely no grey!"
hilda "He completely ignores truth in pursuit of his ideals! He thinks that just because he wants something more than anything else, it'll just {i}happen{/i} for him! That he doesn't have to work for it!"

red @sadbrow talking2mouth "...Maybe that's because he's never had to work for anything? Because you've always done it for him?"

hilda "{w=0.25}.{w=0.25}.{w=0.25}."

hilda -angry frownmouth @sad "Shit, I don't know. Maybe. But if so, what the hell can I do about it? I can't just stop, even if I wanted to. He needs help."

redmind @thinking "It seems to me more like he's {i}desperately{/i} trying to get away from you... but what do I know?"

red @thinking "Well... maybe you could work on saying 'no' more often to your non-Hilbert friends? So you're only running the life of one other person?"

hilda @angrybrow talkingmouth "...No."

red @happy "Hey, that's a good start!"

hilda @thinking "Uh, no, I'm saying 'no' to you saying I should say 'no' more often."

red @surprised "...Oh."

hilda @sad "Like, I appreciate what you're trying to do, but this is who I am, and how I've been for nineteen years."
hilda @happy "It's gonna take a shitload more than a pep talk with a hot farmboy to get me to just {i}stop{/i} all that. This isn't some kinda cheesy greeting card company movie."

red "{w=0.25}.{w=0.25}.{w=0.25}."

red @happy "Then a shitload you shall receive."

hilda @surprised "Eh?"

red @talkingmouth "I've got some free time today. And if I can't stop you from taking care of everyone else, I can at least take care of you."

hilda @surprised "I have no idea what you're talking about."

red @happy "You will, though. Seeya later?"

hilda @surprised "Uh... sure?"

call clearscreens from _call_clearscreens_26

scene hall_A2:
    zoom 0.7
with Dissolve(2.0)

$ oldparty = copy.copy(playerparty)
$ oldmoney = money

$ money = 724395
if ('hildaaronobj' not in globals()):
    $ hildaaronobj = Pokemon(304, level=12, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Metal Claw"), GetMove("Rock Tomb")], item="Sitrus Berry", gender = Genders.Male, nature=Natures.Relaxed, ability="Sturdy")
$ playerparty = [hildaaronobj]

$ hildaaronobj.Heal()

show screen currentdate

narrator "A few hours pass. Eventually, Hilda arrives back at her dorm, cookie-making groceries and clean laundry in tow."

hilda @closedbrow talkingmouth "Ah, shit, I can't carry all this and open the door... Aron!"

play sound "Audio/Pokemon/Ball sound.ogg"

$ renpy.music.queue("Audio/Pokemon/Cries/{}.wav".format(sidemonnum), channel="altcry", loop=None)
$ sidemonnum = hildaaronobj.GetId()
$ aron_name = hildaaronobj.GetNickname()
sidemon "[aron_name]!"

hilda @sadbrow happymouth "Yeah, hi, sweetie. I know, I haven't taken you on a walk in forever. Would you mind helping me carry these bags?"

$ renpy.music.queue("Audio/Pokemon/Cries/{}.wav".format(sidemonnum), channel="altcry", loop=None)

if (sidemon == 304):
    sidemon "A... ron..."
elif (sidemon == 305):
    sidemon "Lai... ron..."
elif (sidemon == 306):
    sidemon "Agg... ron..."

hilda @angry "Hey! I could use some goddamn help here! I..."

pause 2.0

hilda surprised "What's that smell?"

show red with dis: 
    xpos 0.0
    ease 0.5 xpos 0.5

pause 2.0

hilda surprised "[first_name]? What the hell were you doing in my dorm?"

red @happy "Not much. Need some help with those bags?"

hilda @angry "What? No! Answer the goddamn question!"

red @thinking "Mm. I would, but..."

red @happy "I'm trying this new thing where I say 'no' to my friends. So... no!"

play sound "Audio/fading_footsteps.ogg"

show red:
    ease 0.25 xpos 1.5

hilda angry "Hey! Get back, you bastard! Answer me!"

hilda "{w=0.25}.{w=0.25}.{w=0.25}."

hilda sad "What the hell...?"

$ renpy.music.queue("Audio/Pokemon/Cries/{}.wav".format(sidemonnum), channel="altcry", loop=None)

if (sidemon == 304):
    sidemon "Aronnnn...?"
elif (sidemon == 305):
    sidemon "Laironnnn...?"
elif (sidemon == 306):
    sidemon "Aggronnnn...?"

hide hilda 
show dorm_A
with dis

narrator "Hilda slowly pushes open the door, and the strong scent of freshly-baked cookies quickly assails her."

if (IsBefore(1, 5, 2004)):
    show leaf at midrightside with dis
    show may at farrightside with dis
    show serena at midleftside with dis
    show bianca at farleftside with dis

    bianca "Heyyyyy, Hilda! Welcome back!"

    hilda @surprised "...What the hell happened here?"

    leaf @talkingmouth "Oh, [first_name] dropped by."

    hilda @angry "I can tell that! What did he {i}do{/i}?"

    may @happy "Oh, he brought a bunch of groceries we needed! And he helped me bake and restock the cookie plate."
    leaf @thinking "Thank god. I was minutes away from a total cookie-less meltdown."
    serena @happy "Yes, he was quite charming. He also helped me research restaurants in Inspira. We found a couple together that should suit my plans quite nicely."
    bianca @happy "Yeah! And he took my little Moony on a walk while I was helping Cheren put up posters! I think she really liked being able to stretch her legs!"
    leaf @sarcastic "Munna? Walk? Legs?"
    serena @thinking "Oh, and he said he checked in on Hilbert. And that Hilbert has not, ah, 'choked to death on his own foot.' Apparently, he took Hilbert out for ice cream."

else:
    show bea at leftside
    show bianca at farrightside
    show nate at midleftside 
    with dis

    bianca "Heyyyyy, Hilda! Welcome back!"

    hilda @surprised "...What the hell happened here?"

    bea @talkingmouth "[first_name] dropped by."

    hilda @angry "I can tell that! What did he {i}do{/i}?"

    bea @happy "He brought many groceries that we were running low on. The cookie jar has been replenished, thankfully."
    nate @happy "Yeah, and while he was here, he helped me find {i}just{/i} the piece of information on Unovan legends I was looking for. Guess you could call him my own genie, huh?"
    bianca @happy "Yeah! And he took my little Moony on a walk while I was helping Nate with his research! I think she really liked being able to stretch her legs!"
    bea @surprised "Munna? Walk? Legs?"
    nate @thinking "Oh, and he said he checked in on Hilbert. And that Hilbert didn't, uh, 'choke to death on his own foot.' Guess he took Hilbert out for ice cream?"


$ ValueChange("Hilbert", 3, -0.5)

narrator "Hilda hears a 'ping' somewhere in her subconscious, as she suspects [first_name] has just gained three 'points' with Hilbert."
narrator "...Whatever that means." 

hilda @veins angry ".{w=0.5}.{w=0.5}.{w=0.5}That's. Very. Generous. Of. Him."

bianca @happy "Right? It's so cool he just decided to do all this stuff for us for no reason!"

pause 2.0

hilda @thinking "{i}(That bastard. I'm going to kill him. What does he think he is, my... {color=#0048ff}caretaker{/color}?){/i}"

$ money = oldmoney
$ playerparty = oldparty

$ persondex["Hilda"]["Relationship"] = "Caretaker"
$ persondex["Hilda"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Hilda evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Caretaker{/color}'!"

return
