init python:
    def JanineHasUnseenScene():
        if (GetCharValue("Janine") >= 10 and personalstats["Patience"] >= 7 and GetRelationship("Janine") not in ["Battler", "Good Boy"]):
            return "Janine1"
        return False

label Janine1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Janine"]["Events"].append("Level2SceneVer2")

scene lobby 
with Dissolve(2.0)
queue music "Audio/Music/fuschia.mp3"

show screen songsplash("Fuschia City", "Zame")

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 2.0

red @thinking "Wait... isn't that...?"

pause 1.0

show blank
show janine behind blank

pause 0.1

$ renpy.transition(None)
hide smoke
hide blank

janine @talkingmouth "You're coming with me."

red @talkingmouth "So I am. Can you just ninjutsu me over there, or is that a one-person kind of thing?"

janine @closedbrow talkingmouth "Hm. How much do you weigh?"

red @thinking "Uh... about 185, I think?"

janine @talkingmouth "Right. Can you compress yourself into a 3-foot cube?"

red @confused "Nnnno."

janine @smirkmouth "Then I guess we're walking. Hop to it."

red @talkingmouth "Sure thing."

scene stadium_empty with splitfade

pause 0.5

show janine with dis

janine @talkingmouth "So. What's your goal? Why are you here in the Battle Team?"

red @surprised "Huh? This isn't where I thought this was going."

janine @smirkmouth "Change your thoughts. That's where it's going now."

red @talkingmouth "Well... I mean, I'm kinda in the Battle Team because you opened the door so wide for me, it smacked a bunch of other people on the way."

janine @smirkmouth "Funny. Yeah, I know why {i}I{/i} wanted you in the Battle Team. But why'd you join?"

red @thinking "I want to be a Pokémon Champion."

janine @talkingmouth "Of Kanto?"

red @talkingmouth "Any region. Kanto's my home, so that'd be really cool, but... as long as I'm a Champion, I'll be happy."

janine @talkingmouth "Alright."
janine @smirkmouth "Thanks. You can go now, if you want."

red @confused "Really? You brought me all the way out here just to ask me one question?"

if (not IsBefore(1, 5, 2004)):
    janine @sad "If I'd asked Dawn what she wanted before forcing her into the team, then you wouldn't have been matched up against her."

    janine @angrybrow talkingmouth "That was a dumb move of me. I really... ugh. I really screwed up there."

    red @sadbrow happymouth "Hey, you can't beat yourself up over that forever. I know you want perfection, but..."

    janine @talkingmouth "I don't {i}want{/i} perfection. I {i}need{/i} it. And now it's permanently unattainable."

    red @sadbrow talking2mouth "Well... I'd like to say thanks for sticking up for me when all that stuff about my power came out."
    red @sad2eyes talking2mouth "Also... I probably never would've been able to make that speech if you hadn't, uh, kinda pushed me into it."

    janine @closedbrow talkingmouth "It's fine. I made a big mistake with Dawn. Two big mistakes. Forcing her into the team, then letting you two get matched up. I didn't want to make another."

    pause 1.0

    janine @talkingmouth "I've got time. ...Why don't you ask me a couple questions?"

    red @talkingmouth "Sure."

else:
    janine @talkingmouth "You want me to ask more?"

    red @talking2mouth "How about I ask you a couple, Captain? I want to know about my fearless leader."

    janine @sad "...Mm. Sure. I have time. Go ahead."

red @thinking "You also want to be a Champion, right? Why?"

janine @smirkmouth "It was either this or take over my Dad's old gym. And... I don't know."
janine @thinking "A gym leadership isn't big enough. If I was a Gym Leader, I'd be one of eight. Sixteen, actually, since the Indigo League merged."

pause 1.0

janine @smirkmouth "I told you I don't want a part of something. I want the {i}whole{/i} thing. I'm not going to be the fifth, or thirteenth, stop on some random trainer's journey."
janine @talkingmouth "I'm going to {i}be{/i} their journey. I'm going to be the one they climb the mountain to defeat."

red @surprised "Wow. That's pretty intense. But why does being number one matter so much to you?"

janine @thinking "...I come from a small city. A city, sure, but a small one. After they closed the Safari Zone, the only thing that city had was its gym, and its most famous gym leader left to join the Elite Four."
janine @talkingmouth "Pretty much since I was a kid, I knew my future was set. I could have taken that gym leader position easily. But I also have {i}every{/i} possible advantage."
janine @smirkmouth "I'm the daughter of an Elite Four member. I called a two-time Regional Champion uncle. Before the Safari Zone closed down, it made my Dad a ton of money, so we lived very comfortably."
janine @closedbrow talkingmouth "Oh, and I'm the heiress to the ancient shinobi techniques of Ransei."

red @confused "Beg pardon?"

janine @talkingmouth "The point is, I literally don't have a single reason why I shouldn't be able to be number one. I have no weakness. {i}Nothing{/i} is holding me back."
janine @happy "That answer your question, [first_name]?" 
janine @happy "I'll be number one because I have no reason not to be. And I'm not going to stop at Number One in Kobukan. I'll defeat Lance, too, and become the first three-time Regional Champion. Then I'm going for World Champion."

red @happy "You sound like [blue_name]."

janine @sad "Ugh... yeah. Don't tell anyone, but I saw a lot of myself in him."

red @closedbrow "I've got a question, though. You said you called Lance 'uncle?'"

if (not IsBefore(1, 5, 2004)):
    red @talking2mouth "He mentioned that when he was yelling at me during the Quarter Qlashes, but I didn't think much of it at the time."

janine @talkingmouth "Yeah. He actually visited Fuschia a lot when I was younger." 
janine @thinking "When I was younger, I thought he was just visiting because he had a crush on my Aunt Aya. But he later told me he actually visited because he was trying to get my Dad to leave his gym position and join the Elite Four."

red @happy "So he did?"

janine @happy "Hah! No! No way. My Dad turned him down for years. {i}Years.{/i}"

red @thinking "But... isn't Koga a member of the Indigo Elite Four now?"

janine @talkingmouth "Well, not right {i}now.{/i} He's taking a quick break to teach at this school. But he is, yeah."

red @talking2mouth "So what changed?"

janine @talkingmouth "Nothing, really. Lance just asked enough that my Dad gave in."

red @happy "Woah. That worked?"

janine @talkingmouth "He asked every day. No matter {i}what{/i}. Rain, shine, no matter where Lance started his day, at 5 PM, he would show up at my family's door. We had him over for dinner a lot."
janine @happy "I think what made my Dad eventually cave was Lance became... well, my friend. I was a third his age, but he liked my determination, and I thought he was the coolest guy ever. He was so kind."

pause 1.0

show janine sad with dis

pause 1.0

red @sad "What happened?"

janine @talkingmouth "I'm not sure there's anything specific I can point at and say 'that's when Lance changed.'"

janine @talkingmouth "He just got beaten down by losing so often, I think. I mean, he's one of the top five strongest trainers in the world. But he had to lose so many times to get there... I wonder if it was worth it."
janine @thinking "I wonder if {i}he{/i} wonders if it was worth it."

pause 1.0

red @talkingmouth "I'm kinda surprised you're so... open."

janine -sad @talkingmouth "Hm?"

red @happy "Like, you're pretty terse during practices. And you're kinda an intimidating woman, you know? But you're just telling me all this stuff about you."
red @confusedeyebrows talkingmouth "I guess the whole 'you will obey' persona is just to keep us in line?"

janine @happy "Oh! Yeah, I see what you mean. {w=0.5}Hah {w=0.5}hah."

show janine blush with dis:
    ease 0.5 ypos 1.2 zoom 1.3

janine @smirkmouth "But let me be very clear. I'm {i}choosing{/i} to be open with you. Because I think you're a good listener. And not a word of this conversation will leave this battle hall."

pause 1.0

janine @smirkmouth "Oh, also. You {i}will{/i} obey. Okay?"

narrator "Although the butterflies in your stomach seem all but ready to burst out at a moment's notice, you're cognizant that this moment could very easily define your future relationship with Janine."

narrator "{color=#0048ff}Anything less than enthusiastic, verbal, consent will probably get Janine to back off.{/color}"

menu:
    "Yes, Ma'am.":
        janine @angry "Tch. You really don't listen, do you? What {i}am{/i} I going to have to do to make you remember?"

        show janine:
            ease 0.5 ypos 1.3 zoom 1.4

        janine @smirkmouth "I'm not a Ma'am. If you really can't bear to call me by my name, how about... 'Miss'?"

        red @surprised "{size=25}Yeahsurethatseemsfinemiss.{/size}"

        pause 1.0

        janine @smirkmouth "Right answer."

    ">Sputter frantic, flustered gibberish.":
        janine @smirkmouth "Cute, but I think you probably meant to say 'yes, Miss'?"

        menu: 
            "Yes, Miss.":
                pause 1.0

                janine @smirkmouth "Right answer."

            "No, I don't think so.":
                $ janinedomming = False
                janine @surprised "Oh, seriously? My bad. Kinda disappointing, but I'll back off."

    "Could you not do that?":
        $ janinedomming = False
        janine @surprised "Oh, seriously? My bad. Kinda disappointing, but I'll back off."

show janine -blush with dis:
    ypos 1.0 zoom 1.0

janine @closedbrow talkingmouth "Anyway, it's not really a persona. It's just... well, it's who I am."
janine @smirkmouth "My first year as Battle Team leader. Do you remember how many team members I said I had?"

red @thinking "Sixty-two, right?"

if (janinedomming):
    janine @blush smirkmouth "You were paying attention. Good boy."

else:
    janine @talkingmouth "Yeah, that's right."

janine @talkingmouth "I accepted a ton of people into the Battle Team. Pretty much because I was too afraid to turn anyone down. And I just picked whoever I thought were the strongest battlers."
janine @closedbrow talkingmouth "...Which, looking back on it, was pretty much the people who talked about being the strongest the most."

red @confused "Eesh."

janine @talkingmouth "Yeah. Imagine sixty-two [blue_name]s, who all think they know how to run the team, all of them convinced that they're the only one on the team who matters."

red @surprised "How did you survive?"

janine @talkingmouth "I stopped giving them choices."

red @confused "Seriously? There's gotta be more to it than that."

janine @smirkmouth "No, I'm serious. I treated the team like it was a democracy that first year, and that was the biggest mistake I could have made."
janine @closedbrow "{i}I'm{/i} in charge. {i}I{/i} make the decisions. If I know what's best for someone, I'm not going to sit on my hands and let them make a mistake."
janine @smirkmouth "Actually, my Dad was the one who told me to, uh... well, basically, remember I was in charge. I tried too hard to make everyone happy. Then he just sat me down and said..."
janine @koga "Janine! My daughter! Shinobi Heiress! You must not let yourself be cowed by the masses! You must cut through their awful opinions like a {i}shuriken!{/i}"
janine @happy "I mean, at the time I was kinda an edgy teen, so I didn't really--"

red @surprised "WHAT THE HELL WAS THAT?!"

janine @talkingmouth "Huh?"

red @surprised "Your face! It just--it became--you looked--"

if (janinedomming):
    janine @blush talkingmouth "Stop stuttering."

pause 1.0

red @thinking "Sorry. What I meant to say was you, uh, you looked {i}exactly{/i} like your father there."

janine @smirkmouth "Oh, that? Basic kunoichi disguise technique. Don't worry about it."

red @talkingmouth "Uh... even if I try, I think I'm going to see that in my nightmares."

janine @closedbrow "Get over it."

red @sadbrow talking2mouth "I... yeah. Okay."

pause 1.0

red @talkingmouth "So it was your Dad who told you to stop giving the other Battle Team members choices?"

janine @talkingmouth "Kind of. What he really said was that I needed to have more confidence in my own, but it was the same outcome, really."

red @happy "So, you've got a good relationship with him?"

janine @happy "Yeah, good enough. I mean, we butt heads all the time, but he's the one who laid out the red carpet for me." 
janine @talkingmouth "He's a bit disappointed I'm not trying to be the new Fuschia Gym Leader, but he can't exactly fault me for aiming higher."

red @talkingmouth "...What about your Mom?"

janine @talkingmouth "Killed by a rival ninja clan."

red @surprised "WHAT?"

if (janinedomming):
    janine @blush happy "Oh, you are {i}fun{/i} to tease."

else:
    janine @happy "God, you're too easy."

janine @talkingmouth "Nah, my Mom wasn't really in the picture. Aunt Aya kinda hinted that my Dad might not have been married when I was born, so, yeah. Never knew her. Never cared, really."

red @talkingmouth "And what about Lance? Sounds like he was almost family to you. What does he think about you attempting to be World Champ? Everyone knows he wants that, too, and he's been trying for a long time."

janine @sad "...He's fine with it."

pause 1.0

red @talkingmouth "Huh. I guess I finally hit the wall."

janine @surprised "Run that by me again?"

red @talkingmouth "I've been asking more and more personal questions, just {i}waiting{/i} for you to eventually shut me down. And this is the first question I've asked that I don't think you're being entirely straight with me about."

if (janinedomming):
    janine surprised "Wait... you've been waiting for me to shut you down?"

    red @talkingmouth "Yeah, just testing my boundaries. Seeing what I can get away with, you know."

    pause 1.0

    janine -surprised happyneutralmouth blush @smirkmouth "Well. {w=0.5}Isn't that {i}interesting{/i}."

    janine @closedbrow "Just out of curiosity, what made you think you could get away with {i}that{/i}?"

    red @talkingmouth "It was less a 'I want to see if I can get away with this' and more a 'I want to see what happens if I {i}don't{/i} get away with this."

    janine @happy "Ah... it's {i}very{/i} refreshing, finally meeting someone who can just play the game and be honest about it."

    janine @smirkmouth "Let me just set expectations here. You get this Battle Team into the National Tournament, you do anything I tell you to, and you get...?"

    red @happy "To spend time with you?"

    pause 1.0

    janine -blush -happyneutralmouth @smirkmouth "Hm. You're almost too cute. I'd feel guilty, if I tore into you like I want to."

    red @surprised "What?"

    janine @closedbrow talkingmouth "I don't think you're ready for this just yet."

    red @sad "Oh..."

    janine @smirkmouth "Mmm... let me rephrase. I don't think you {i}deserve{/i} this just yet."

    red @talkingmouth "Oh! Okay. Much more into that."

    janine @talkingmouth "You be a good boy and win me some more battles, okay?" 
    janine @blush smirkmouth "And if you do that... I'll give you your reward."

    pause 1.0

    red @confused "I just, I like to track my progress. Can you, uh, make clear the number of battles I need to win to make that happen?"

    janine @happy "Oh, you'll know. And you'll know when I let you know, and not a moment before. Understood?"

    red @happy "Yes, Miss."

    janine @happy "Hmhmhmhm."

    janine @blush smirkmouth "{color=#0048ff}Good boy.{/color}"

    $ persondex["Janine"]["Relationship"] = "Good Boy"
    $ persondex["Janine"]["RelationshipRank"] = 1

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    play sound "audio/sav.wav"
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with Janine evolve from '{color=#0048ff}Tool{/color}' to '{color=#0048ff}Good Boy{/color}'!"

else:
    janine @smirkmouth "Hm. Aren't you perceptive. I hope you keep that up in your battles."

    red @talking2mouth "I'll do my best. I'm really going to try to win."

    janine @talkingmouth "I ask for nothing less."

    red @confused "Uh... do you mean 'more'?"

    janine @happy "How about you just handle the battling, and leave the figuring out who-means-what to me?"

    red @closedbrow talking2mouth "Jeez. Alright."

    janine @blush smirkmouth "Now, shouldn't you get back to training? I don't want my precious {color=#0048ff}battler{/color} resting on his laurels, after all. "

    $ persondex["Janine"]["Relationship"] = "Battler"
    $ persondex["Janine"]["RelationshipRank"] = 1

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    play sound "audio/sav.wav"
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with Janine evolve from '{color=#0048ff}Tool{/color}' to '{color=#0048ff}Battler{/color}'!"

return