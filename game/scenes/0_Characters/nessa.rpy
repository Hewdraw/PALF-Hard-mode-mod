init python:
    def NessaHasUnseenScene():
        if (GetCharValue("Nessa") >= 10 and personalstats["Wit"] >= 2 and GetRelationship("Nessa") != "Friend"):
            return "Nessa1"
        return False

label Nessa1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Nessa"]["Events"].append("Level2SceneVer2")

scene pool
with Dissolve(2.0)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/LoFiMaxRaidBattle.mp3", channel='music', loop=True, fadein=1.5, tight=None)

if (not IsBefore(1, 5, 2004)):
    narrator "Having texted Nessa, and arranged a time and place to meet up for your date, you make your way to the Recreation Center, where Nessa said she was hanging out by the pool."

else:
    narrator "Having texted Nessa, and arranged a time and place to meet up to talk, you make your way to the Recreation Center, where Nessa said she was hanging out by the pool." 

red @thinking "Let's see... where could she be...? Ah, there!"

show nessa with Dissolve(1.0):
    xpos 0.33 ypos 0.54 zoom 0.05

red @happy "{size=50}Hey, Nessa! Ready for our date?{/size}"

show nessa:
    linear 30.0 xpos -0.7 ypos 0.85 zoom 0.3

pause 5.0

redmind "She's... taking her time, huh?"

pause 5.0

show nessa:
    xpos -0.5 ypos 1.0 zoom 1.0
    ease 2.0 xpos 0.5

pause 2.0

red @surprised "Woah. Did I catch you as you were about to go for a swim?"

nessa @talkingmouth "Nah."

red @confused "But... your outfit?"

nessa @talkingmouth "Yeah, I just wear this."
nessa @happy "Pretty hot, right?"

red @happy "I mean... yeah."

nessa @talkingmouth "Life's too short to not be as hot as you can. I've probably only got another... what, ten years of this?"
nessa @angrybrow happymouth "I'm {i}going{/i} to milk it."

red @talkingmouth "Cool. I'm definitely not complaining."

if (not IsBefore(1, 5, 2004)):
    red @sadbrow talkingmouth "Is... your offer of a date still on the table?"

    nessa @talkingmouth "Why wouldn't it be?"

    red @sadbrow talking2mouth "I mean, the whole Frienergy thing..."

    nessa @closedbrow talkingmouth "It's whatever. Old news, at this point."

    red @surprised "Really?"

    nessa @talkingmouth "I believed your speech. Most other people probably did as well."
    nessa @talkingmouth "...Hearing Sabrina's thoughts affected me way more than anything I learned about you."

    red @confusedeyebrows talking2mouth "Ouch?"

    nessa @closedbrow talking2mouth "That's a good thing."

pause 1.0

nessa @thinking "So. Where're you taking me?"

red @happy "I actually spent a lot of time thinking about this. My first thought was a fancy restaurant, or maybe a movie."

nessa @talkingmouth "Classic. Can't go wrong with that."

red @talking2mouth "But you strike me as the kind of woman who's probably had a lot of dates like that."

nessa @talkingmouth "Can't deny it."

red @talking2mouth "So then I thought {i}really{/i} hard about what kind of date you've never been on, before..."

pause 1.0

red @happy "And I'm pretty sure I know where to take you, now."

nessa @talkingmouth "...Alright."

redmind @thinking "...Phew. It's kinda an uphill battle to excite her, isn't it?"

red @happy "Right! Let's go."

if (IsBefore(1, 5, 2004)):
    nessa @sad "Hold up."

    red @surprised "Huh?"

    nessa @talkingmouth "People are going to stare at you if you go out with me. Just making sure you're okay with that."
    nessa @sad "Some people'll respect you more. Most will just be jealous. Either way this goes, it'll give you something to talk about, though."
    nessa @talkingmouth "You still down?"

    red @talkingmouth "Totally."

    nessa @talkingmouth "Alright, let's go."

scene fields2
show clouds behind fields2:
    yalign 0.75
    ease 5.0 yalign 0.5
with slideleft

show nessa with dis

pause 1.0

nessa @surprised "The fields?"

red @happy "Yeah! There's something pretty cool that I wanted to show you."

nessa @closedbrow talkingmouth "Alright, I'm down. This is something new, at least."

show venetiaintrobgnoglow with Dissolve(1.0)

hide nessa

nessa @surprised "Woah. What's this?"

red @happy "This is a meteor crater!"
red @thinking "It's... not quite as cool as it used to be, though. It used to be glowing orange and blue, but it looks like it's not anymore."
red @talkingmouth "Still. Big hole in the ground. Kinda neat, right?"

nessa "{w=0.5}.{w=0.5}.{w=0.5}."
nessa @talking2mouth "Yeah. That's kinda neat."

show nessa behind venetiaintrobgnoglow
hide venetiaintrobgnoglow with dis

nessa @happy "Alright. I'll give you a break. You've shown me something kinda cool, and that's enough for now."
nessa @sad "I'm just glad you didn't take me to {i}another{/i} restaurant. I've had so many dates take me out for Kalosian food, I feel like I can speak the language at this point."

red @happy "Phew! It was kinda a shot in the dark, but I guess I dodged a bullet, huh?"

nessa @talkingmouth "Well, it wouldn't have been an instant turn-off, but yeah. I'm pretty used to those kinds of dates."

show nessa:
    ease 0.25 xpos 0.55 ypos 1.1
    ease 0.25 xpos 0.5 ypos 1.2

nessa @talking2mouth "Here, sit down with me. Let's chat."

show nessa:
    ypos 1.2
    ease 1.0 zoom 1.3

narrator "You sit down next to Nessa. Your legs dangle over the side of the pit."

red @talkingmouth "Mind if I ask a question?"

nessa @talkingmouth "Just ask. We're on a date."

red @thinking "Right. When we first met, you basically asked {i}me{/i} out on a date. So, why?"

nessa @talking2mouth "Fishing for compliments?"

red @thinking "Nah, just trying to figure out what you saw in me."

nessa @sad "You just seemed like a nice guy. You listened to me, you're good-looking, and you didn't stare at my chest too much."

red @sad "Is that your criteria for a nice guy?"

nessa @talkingmouth "You think I should have higher standards?"

red @happy "Nessa, you're a model. You're gorgeous, you've got to be at least a little rich, and you're a good battler, too."
red @confused "You can afford to have any standards you want, and {i}someone{/i} will rise to meet them."

nessa @talkingmouth "Yeah, maybe."
nessa @thinking "My standards for getting a second date are pretty high, though. I guess maybe my cutoff point is just later than it would be for others."

red @talkingmouth "Right."

nessa @talking2mouth "So, what's your goal here at Kobukan? What do you want to do when you graduate?"

red @thinking "I want to be a Champion. That's always been my only goal."

nessa @talking2mouth "Nice goal. I've heard it before, but you say it with conviction. Why do you want to be a Champion, though?"

red @surprised "W-why?"

nessa @talkingmouth "Yeah. Being a Champion is a short-term goal. What does being a Champion let you do?"

red @confused "Being a Champion is a {i}short-term goal{/i}? Some people spend decades trying to do that."

nessa @surprised "Oh. Yeah, I guess that's right."
nessa @sad "Guess I was just thinking of Leon."

red @thinking "Leon? Champion of Galar?"

nessa @talkingmouth "Yeah. Friend of mine."

pause 1.0

show fields2 with vpunch

red @surprised "You-- YOU'RE FRIENDS WITH LEON?!"

nessa @sad "Was. He's... busy, now. Champion stuff."

red @thinking "But, wait... Ethan told me something about Leon... isn't Leon, like, quite a bit older than you?"

nessa @talkingmouth "Yeah. He became Champion five years ago, and has never lost a battle since."

red @thinking "But you said you were a minor until recently. How could you be friends if you were so much younger than him?"

nessa @surprised "Have you ever met the guy? He's a 10-year-old in a man's body. Out of the four of us, I was the most mature, even though I was the youngest."

red @thinking "Wait... four of you?"

nessa @talkingmouth "Yeah. Our group of friends. We used to call ourselves the Galarian Stars."
nessa @sad "I was the youngest. The sensible one, the one who kept us all grounded."
nessa @talkingmouth "Then there was Raihan. He always used to call me 'Lil Nessie.' An arrogant blowhard, but... he lifted you up. Butted heads with Leon every chance he got."
nessa @thinking "Sonia was next. She was the granddaughter of a Pokémon Professor. Bit of a ditz, no self-esteem, but the smartest girl I know."
nessa @talkingmouth "And... Leon was the oldest of us. He was pants with directions, but wherever he looked, he saw the stars, and followed them."

red @happy "Sounds like a good group of friends."

nessa @happy "We were inseparable. Went everywhere together, did everything. We all knew we would become Champions." 
nessa @talkingmouth "They were just all waiting for me to become eighteen, then we'd take the Gym Challenge together."

pause 1.0

show nessa sad with dis

pause 1.0

red @sad "...But?"

nessa "Leon got an endorsement from a bigwig in Galar. The Chairman of the entire league. It was a once-in-a-lifetime opportunity."
nessa -sad @talkingmouth "I wasn't going to ask him to wait for me, obviously. So we changed the plan."
nessa @thinking "Well, Leon became Champion within the year."
nessa @talkingmouth "When a new Galarian Champion is crowned, they usually immediately endorse the person they feel is most likely to unseat them. It's a tradition."
nessa @thinking "So Leon endorsed Raihan, of course. Raihan apologized to Sonia and I, but set off on his challenge."

red @talking2mouth "He didn't make it to Champion, though."

nessa @talkingmouth "No. But he managed to make it right up to the league, eventually securing the eighth major league gym leader spot."
nessa @talkingmouth "So, at that point, we figured that he could endorse Sonia, and then Sonia could endorse me."

pause 1.0

nessa @talkingmouth "Sonia couldn't make it. She dropped out after the fifth gym."

red @surprised "Oh, geez!"

nessa @talkingmouth "We knew that the fifth Gym Leader was retiring soon, so we thought maybe Sonia could take over there, like Raihan did the eighth."
nessa @talkingmouth "Trainer schools aren't really a thing in Galar. Most trainers just start their journeys and learn as they go. But we learned about Kobukan Academy, and heard it was a great place to get practical experience."

if (IsBefore(20, 4, 2004)):
    nessa @talkingmouth "So Leon paid for her to go to Kobukan. She was here just last year, actually."

    red @happy "Oh, really? That's awesome! How'd she do?"

    nessa frownmouth @sad "She dropped out of that, too."

    red @surprised "...Huh?"

    nessa @talkingmouth "Yeah. She sent each of us hand-written letters apologizing for her failures, and then cut communications with us. Doesn't even respond to our texts."
    nessa @sad "God knows where she's gone."

    red @sad "Oh... I'm sorry to hear that."

else:
    nessa @talkingmouth "So Leon paid for her to go to Kobukan. And... well, you already know. She dropped out of that, too."
    nessa @talkingmouth "She sent each of us hand-written letters apologizing for her failures, and then cut communications with us. Didn't even respond to our texts."
    nessa @sad "We all thought we'd never see her again until I saw her in the lunch hall."

    red @sad "But at least you've made contact again, right?"

nessa @talkingmouth "Yeah. Well, I figured I wasn't going to be getting an endorsement any time soon from either Leon or Raihan, so I'd just try my own hand at this Kobukan thing."

red @surprised "Why wouldn't they endorse you?"

nessa @talkingmouth "I was a public figure, so were they. It was common knowledge that we were all friends before Leon ever became Champion."
nessa @thinking "Wouldn't look good if the Champion was endorsing unproven trainers, just 'cause they were friends." 
nessa @talkingmouth "Raihan could {i}always{/i} hold his own against Leon."
nessa @talking2mouth "Sonia, despite her crippling insecurities, also knew more about the intricacies of battle than I think Leon does, even now."

pause 1.0

nessa @sad "And I looked good in a bikini."

pause 1.0

nessa @talkingmouth "The chain could've worked, though. Leon, through Raihan, through Sonia, to me, would have been enough degrees of separation."

pause 1.0

nessa @sad "But the chain broke."

pause 1.0

nessa closedbrow angrymouth "But we wouldn't have {i}had{/i} to rely on the chain if everyone had just {i}waited.{/i} If they'd just been {i}patient,{/i} if they'd just thought long-term about this... about {i}any{/i} of this..."

red @sad "...I'm sorry."

nessa -closedbrow -angrymouth frownmouth @talkingmouth "...Yeah. So... that's kinda the state of the Galarian Stars, now."
nessa @talkingmouth "One got everything he wanted. One is still fighting for it. One disappeared. And I'm just starting my journey after everyone I care about is already finished."

red "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "Are you sure?"

nessa @talkingmouth "What do you mean?"

red @talkingmouth "Like, are you sure they're finished?"

nessa @thinking "Um... pretty sure. Leon didn't really have a goal beyond becoming Champion."
nessa @talkingmouth "Raihan's going to try and beat him, but that's kinda never happening."

if (IsBefore(20, 4, 2004)):
    nessa @sad "And Sonia's already failed twice. She's probably taken a research job somewhere, and is planning on never coming back to Galar again."
else:
    nessa @sad "And Sonia's already failed twice. I haven't asked her about it, but I don't think she's ever planning on coming back to Galar again."

red @talkingmouth "...I don't think those sound like 'endings.'"

nessa @surprised "How are they not?"

red @happy "Well, maybe Leon continues to be undefeated for years. Does Raihan's story stop being told just 'cause he doesn't change that?"

nessa @surprised "I guess not?" 
nessa -frownmouth @talkingmouth "But I don't know who'd bother telling it. 'News flash: Nothing has changed.' Boring, right?"

red @talking2mouth "Nessa, I {i}firmly{/i} believe the most important part of the adventure is the journey. Not the destination."
red @thinking "I know you think the only 'run' that matters is the 'long run'..."
red @happy "But I run every day. And I don't really care how much distance I cover, in total. All that matters is that I ran."

pause 1.0

nessa @talkingmouth "...So you're disagreeing with me?"

red @sadbrow talkingmouth "Guess I am."

nessa @happy "Good. Most dates just yes-man their way through."
nessa @talkingmouth "Of course, most dates don't hear the whole Galarian Star shpiel..."
$ lowertime = timeOfDay.lower()
nessa @sad "Guess I'm off my game. It's been a weird [lowertime]."

red @talkingmouth "I don't think you guys are done. I don't think {i}any{/i} of you are done."
red @happy "I mean, you said you wanted to be a trainer because you were afraid that modeling wouldn't last for you, right?"
red @talkingmouth "Every end is a new beginning. So maybe the Galarian Stars' collective dream burned out."
red @happy "Sounds to me like you're all still pursuing your individual dreams."
red @happy "Can't believe I'm saying this, but you should try seeing things a bit more long-term. For your friends, at least."

pause 1.0

red @talking2mouth "But you should totally try living in the moment more, too."

nessa @talkingmouth "I'll think on that."

red @happy "Cool. So what're my chances of another date?"

nessa @thinking "...Well, I liked our conversation. Let's actually {i}do something{/i} next time, though."

red @talkingmouth "Fair enough. I'll start brainstorming now."
red @thinking "So... one date down, that wasn't a complete disaster. What does that make us?"

nessa @thinking "...Mm. You're a {color=#0048ff}friend.{/color}"

red @surprised "Wait, you'll date someone before you befriend them?"

nessa @happy "Anything to open the door. Even a model has to try to grab people's interest, you know?"

red @happy "Well. Color me interested."

$ persondex["Nessa"]["Relationship"] = "Friend"
$ persondex["Nessa"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Nessa evolve from '{color=#0048ff}Date{/color}' to '{color=#0048ff}Friend{/color}'!"

return