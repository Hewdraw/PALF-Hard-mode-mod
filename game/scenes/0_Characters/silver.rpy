init python:
    def SilverHasUnseenScene():
        if (GetCharValue("Silver") >= 10 and personalstats["Courage"] >= 5 and GetRelationship("Silver") != "Friend"):
            return "Silver1"
        return False

label Silver1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Silver"]["Events"].append("Level2SceneVer2")

scene abandonedhouse
with Dissolve(2.0)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)

show roughneck at night with dis

red night "...Hey."

roughneck @angry "You here to talk to the boss?"

red "Sure am. Mind letting him know I'm here?"

roughneck @angry "Tch."

hide roughneck with dis

narrator "You've come back to the city to talk with Silver, carefully retracing your steps until you find your way to the abandoned house that Silver lives in."

show silver angry at night with dis

silver "The hell do you want?"

red @confusedeyebrows "...Um. To talk?"

silver -angry @sad "Right. Sorry. Force of habit."

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/DontEverForget.mp3", channel='music', loop=True, fadein=1.5, tight=None)

pause 1.0

silver @talkingmouth "Well. What do you want to talk about?"

red @talkingmouth "I want to talk about you."

pause 1.0

silver @sad "There's nothing to say."

if (not IsBefore(1, 5, 2004)):
    silver @talkingmouth "If it's about the mind-powers stuff... whatever. I'm obviously outnumbered when it comes to not trusting you." 
    silver @closedbrow talkingmouth "Anyway, my position in the disciplinary committee lets me make sure you don't get too powerful."

    pause 1.0

    silver @happymouth "Remember, if I see you trying to start your own little gang, there's a Crobat with your name on it."

    red @confused "Noted. Terrifying. But that wasn't what I wanted to talk about at all."

    silver @thinking "Yeah? What, then?"

red @confused "Silver. You live in the city, in a run-down shack, hiding from the cops, with twenty older guys who all treat you like you're their boss."

pause 1.0

silver @closedbrow talkingmouth "...Yeah."

red @happy "Can you honestly tell me there's no story there?"
red @talkingmouth "If you say that, I'll believe you. But I don't think you're going to say that."

pause 1.0

silver @sad "Fine. There's a story. But I'm not telling it."

red @confused "Why not?"

silver @angry "Well, aren't you all goddamn nosy all of a sudden!"

red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

silver @sad "Sorry."

red @talking2mouth "Silver, I just want to get to know you. In a stadium of hundreds of people, you were the only person who stood up to help me when Lance was being a dick."
red @talking2mouth "I want to know why. {i}Why{/i} you helped me. What gave you the motivation to."
red @happy "I want to know {i}who{/i} helped me. Who the Silver that stood up and acted as my shield was...{w=0.5} {i}is.{/i}"

silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."
silver @happymouth "Well, don't you think you're important?"

red @surprised "Huh?"

if (IsBefore(1, 5, 2004)):
    silver @talkingmouth "I wasn't doing it for you. You seem like a nice guy. You'd probably deserve it, if I did defend you."
else:
    silver @talkingmouth "I wasn't doing it for you. Powers aside, you're nice enough, and you'd probably deserve it if I {i}did{/i} do it for you."

silver @angry "But I was doing it for your Pikachu."

if (IsBefore(1, 5, 2004)):
    $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Pika?"

else:
    $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
    libpikachu @surprisedbrow frownmouth "Pika?"

silver @angrybrow sadmouth "My entire life, I've heard weak men blame others for their incompetence." 
silver @sad "People just can't take any goddamn {i}responsibility{/i} for their own failure."
silver "I'm... better, now. But the life I lived before... when I lived with my Dad..."

pause 1.0

silver @sad "Some mistakes you can't roll back."
silver @closedbrow "But I can dream. And work as hard as I can to bury my past in the new me."

pause 1.0

silver @sad "And... I don't want others making the same mistakes I have. So... when I see or hear a trainer blame a Pokémon for their failure..."
silver @angry "I need to let them know what they're doing wrong."

pause 1.0

red @surprised "Wait, you were trying to {i}help{/i} Lance?!"

silver @angry "I think we've established at this point that I'm not exactly the picture of eloquence! Yes, I was trying to help the bastard."

red @talkingmouth "...You might want to work on your communication skills."

silver @sad "If that's really all you came here to tell me, you can piss off back to the campus, now."

red @sadbrow happymouth "C'mon, Silver. Work with me, here."

silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}.You're a patient guy."

red @happy "One of my many positive qualities."

if (IsBefore(1, 5, 2004)):
    silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. You agreed to beat up my goons. Not sure what else we can do for each other."
   
    red @talkingmouth "Well, if we're going to be on the Battle Team together, we could stand to learn a little bit more about each other, right?"

else:
    silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. And we all know how well that worked. Not sure what else we can do for each other."

    red @talkingmouth "What you did to help me out that day... I mean, it was kinda crazy. It probably would have worked, if Cheren hadn't... you know. Where'd you come up with that? Staging an attack on the school?"

    silver @sad "{w=0.5}.{w=0.5}.{w=0.5}."

silver @closedbrow talkingmouth "I've talked enough. Tell me more about yourself."

red @happy "Sure! So, I'm from a little town called Pallet Town, in southwest Kanto. My Pikachu here is called [pika_name], and he was my first friend."
red @thinking "Um... I lived with my Mom my whole life. My father wasn't in the picture... he left when I was very young. We were pretty poor. Not 'cause he left, even before that."

pause 1.0

silver @talkingmouth "What kind of place was Pallet Town?"

red @happy "Small!"
red @talkingmouth "Peaceful, though. The people were kind. The grass was green, and the ocean was just south of us. And everyone knew everyone."

pause 1.0

red @sad "The one bad thing was... well, everyone knew everyone. It would be pretty much impossible to get a fresh start, there. Anything you do sticks with you until you move away."

silver @talkingmouth "Mm. I get that."
silver @sad "I grew up in Kanto as well, actually. In Celadon."

red @happy "Really? Huh! I would've thought Celadon would be big enough to find a new start wherever you turned."

silver @angrybrow happymouth "Not when you never leave your... {i}house.{/i} I probably got fresh air three times for the first twelve years of my life."
silver @talkingmouth "And one of those times was when we were evacuating the building. Alarms flashing, cops pulling up... heh."

red @surprised "Geez! Sounds intense. Was there a fire?"

silver @sad "Something like that."
silver @talkingmouth "...So, your Pokémon have always trusted you, huh?"

red @happy "Pretty much. I mean, I've had [pika_name] for a long time, but I think he trusted me when we first met."

silver @sad "And you don't have... you don't have any skeletons in your closet? No memories you want to bury in the dark?"

red @confused "Uh... no."

if (not IsBefore(1, 5, 2004)):
    red @talkingmouth "Well, there {i}was{/i} the whole Frienergy thing, but... that's off my chest now, so... besides that, I don't think so."

silver @thinking "Damn."

red @confused "Damn? Why?"

silver "{w=0.25}.{w=0.25}.{w=0.25}."

silver @talkingmouth "You... are good."

red @happy "Aw, thanks."

silver @angry "Shut up. I mean you're {i}good.{/i}"
silver @thinking "You're kind, you know all kinds of shit about Pokémon, you're a great battler, you're fit, and you can make friends with anyone."

red @talkingmouth "Wow. Are you just writing my dating website profile for me? Make sure to note I like guys, too."

silver @sad "Ugh... of course you do."
silver @talkingmouth "Look, no-one has all that unless they're trying to make up for something. There's gotta be something in your past. {i}Something.{/i}"
silver @angry "Like, you used to be a fatass who didn't know anything about Pokémon, and you had no friends, right?"

red @thinking "Well... there was a time when I didn't have any friends, yeah. After that, I definitely became a lot more social."
red @talkingmouth "Or at least a lot more willing to take risks. Socially."

silver smilemouth @talkingmouth "Hmph. Knew it."

red @happy "Hey, is that a smile?"

silver @talkingmouth "Yeah. It's a hell of a relief to hear that you aren't as perfect as I thought you were. What's this all in service of, anyway?"

red @thinking "Huh?"

silver @sad "Why bother being everything you are? It'd be so much easier to just... hide away, right? Be mediocre. Fade into the background."

red @thinking "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "I want to be a Champion."

silver -smilemouth @talkingmouth "...So? Not like you need friends to do that. Look at Lance. Bastard's done it twice, and what does he have going for him, besides an overcompensatory hairstyle?"

red @sadbrow happymouth "Maybe he doesn't need friends. But I do."

silver @closedbrow sadmouth "Psh."

red @happy "I'm serious. I'm nothing without my friends. And I'm not being modest. I freeze up. I can't speak for myself. I can barely remember anything about Pokémon, and everything I know about battling goes out the window."
red @thinking "I spent four years in Pallet Town without any friends, and..."
red @sadbrow happymouth "Well, I can barely remember anything I did then. I think I was kinda just in a dull haze."

if (not IsBefore(1, 5, 2004)):
    silver @sad "So... like up there on the stage, then..."

silver @talkingmouth "...Well, you need to get over that."

red @angry "Oh, gee, thanks. Wish I'd thought of that."

silver @thinking "If you can't do it for yourself, do it for your Pokémon. They're relying on you. And if you can leave this world with at least one Pokémon you haven't disappointed, then you've won."

red @talkingmouth "What about one human?"

silver @sad "Yeah, that's... not going to happen."

red @happy "I dunno. I think you can do it."

silver @happymouth "Then prepare to be disappointed."

pause 1.0

red @confused "Was that a joke?"

silver @smilemouth "Are you so surprised? I'm a funny guy."

red @happy "I'm kinda surprised, yeah! I didn't know you told jokes."

silver @talkingmouth "...Most people don't get them. My humor's a bit dry."

red @talkingmouth "Well, what's your dream? International comedian?"

silver @thinking "...Whenever I close my eyes at night, I only ever have one dream." 
silver @sad "And I dream of an absolution."

if (IsBefore(3, 6, 2004)):
    red @happy "...C'mon. You're, what, eighteen?"

    silver @talkingmouth "Seventeen."
else:
    red @happy "...C'mon. You're eighteen."

red @happy "What do you have to be absolved of?"

silver @angry "Are you so privileged that you think just because you've never had a nightmare, they don't exist?"

pause 1.0

silver @closedbrow "I've got a lot of nightmares in my dream journal, red. I can't tear out those pages. I can only keep writing."

pause 1.0

silver @talkingmouth "So that's my dream. I'll never be able to forget what I was. But if I can outweigh it, then maybe I can die happy."

red @thinking "Hm."
red @talkingmouth "So, your first step in this absolution is to try and rehabilitate your father's former employees."

silver @talkingmouth "Yeah, these idiots."

red @confused "...That's not normally the kind of thing the son of a CEO has to do, even if his Dad's company fails {i}really{/i} hard."

silver @happymouth "Yeah, well, my Dad's company was always a {i}family{/i} business. Like he liked to remind me."

red @thinking "What's your end-goal with these guys?"

silver @surprised "Huh?"

red @thinking "Like, what's your rehabilitation plan? What goalposts are you setting? How long do they have? What's your exit strategy?"

silver @angry "I yell at them when they act up."

red @talking2mouth "Not much of a plan."

silver @thinking "No, not much of one."
silver @sad "I guess I'm just kinda hoping that... one day... they'll just wander away, and not be my problem anymore."
silver @thinking "Maybe when I'm not looking, they'll get a long-term job somewhere. Maybe even buy an apartment and leave."

pause 1.0

silver @talkingmouth "They bring me a lot of money. I don't ask where it comes from. I just try to invest it--get it out of this house--as soon as I can."

silver @smilemouth "Here, take a wad."

play sound "audio/Get.ogg"

$ money += 5000

narrator "Silver tosses you a brown paper bag filled with $5,000."

red @surprised "W-woah. I don't really like to accept money from... wait, where'd this come from?"

silver @sad "Didn't you hear? I said I don't ask where it comes from."

pause 1.0

silver @sad "It's more likely they'll try to rob a cop and get put away for a couple years. Still not my problem."

red @thinking "You've been talking a lot about how your Dad's employees are... well, criminals. And I first met them when they stole Tia's hat."

pause 1.0

silver @talkingmouth "Yeah."

red @sadbrow happymouth "What... kind of business did your Dad run, exactly?"

pause 1.0

silver @talkingmouth "Let me put it this way."
silver @sad "When he did well, he was the only one who was happy about it. And when he went 'out of business...' well, no-one cared."

red @talkingmouth "...Silver."

silver @sad "He was a bastard, but he was the only one who knew how to handle these people. And they're disappointed in me, because I'm not as cruel or tough as he was."
silver @talkingmouth "Isn't that fucked up?"

red @sadbrow happymouth "...You have trouble enforcing discipline, huh?"

silver @thinking "Yeah, you could say that."
silver @sad "I mean, some of these guys knew me when I was in diapers. The fact they live in my house now doesn't change that."

red @thinking "Do you think you could use some help with your job here, then?"

silver @talkingmouth "Well, yeah. But you're already helping, by coming here to beat them up every once in a while."

red @talkingmouth "Glad I could be your {color=#0048ff}enforcer{/color}, then!"

silver @sad "I don't want that."

red @surprised "Huh?"

silver @sad "Everything about my life is drenched in violence, and authority, and shouting, and absolution, and painful memories."
silver @talkingmouth "I don't want to drag anyone--you--into that."

pause 1.0

silver @sad "I don't need an enforcer. I don't need {i}more{/i} people who want to beat up others on my behalf. I just need a..."

pause 2.0

red @sad "Silver?"

silver @closedbrow sadmouth "{size=30}I just need a {color=#0048ff}friend.{/color}{/size}"

pause 2.0

silver @surprisedbrow sadmouth "{size=30}Please?{/size}"

red @happy "Silver. Did you really need to ask? C'mon. I wouldn't have come out here if I didn't want to be your friend."

silver @smilemouth "...Thank you."

$ persondex["Silver"]["Relationship"] = "Friend"
$ persondex["Silver"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Silver evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

return