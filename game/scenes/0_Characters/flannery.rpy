init python:
    def FlanneryHasUnseenScene():
        if (GetCharValue("Flannery") >= 10 and personalstats["Charm"] >= 6 and timeOfDay == "Evening" and GetRelationship("Flannery") != "Challenger"):
            return "Flannery1"
        return False

label Flannery1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Flannery"]["Events"].append("Level2SceneVer2")

scene baseball 
show flannery
with Dissolve(2.0)

$ renpy.music.queue("Audio/Music/MtPyre.mp3", channel='music', loop=True, tight=None)
    
red @talkingmouth "Hey, Flannery."

if (not IsBefore(1, 5, 2004)):
    flannery surprisedbrow frownmouth @surprisedmouth "Oh, [first_name]. Hi."

    pause 1.0

    red @sadbrow talking2mouth "Er... something wrong?"

    flannery @closedbrow talking2mouth "Nah."
    flannery -surprisedbrow -frownmouth @talkingmouth "It's just... that whole power thing..."
    flannery @sadbrow talkingmouth "How are you taking it?"

    red @sadbrow talkingmouth "Looking forward to putting the whole thing behind me. Though I kinda get the feeling I'll be feeling that one for the whole year."

    pause 1.0

    red @talking2mouth "What about you? Are we still cool?"

    flannery @talkingmouth "Yeah. I didn't believe that bull about psychic powers, anyway."
    flannery @closedbrow talkingmouth "Well... until Whitney told me that some people actually {i}can{/i} control minds. I mean, that was a shock, you know? Didn't see that one coming."
    flannery @happy "But then she explained how your power really works to me, and your speech sealed the deal."

    pause 1.0

    flannery @talking2mouth "That was pretty brave of you."

    red @sweat closedbrow talkingmouth "Thanks, I'll never be able to do it again."
    red @confusedeyebrows talking2mouth "Anyway, what're you doing? Working up a sweat at the baseball field?"

else:
    flannery @happy "Hey, guy. How're you doing?"

    red @talkingmouth "Pretty good. Working up a sweat at the baseball field?"

flannery @talking2mouth "Totally. After a couple hours of this, there's nothing better than a long shower to cool down in."
flannery @happy "Back home we always used to jump in the hot springs after a long morning of battling at the gym. You {i}really{/i} don't know how to unwind until you've been to the Lavaridge hot springs."

red @thinking "Lavaridge? Is that where you're from, then? I think you mentioned that a while ago."

flannery @happy "Yeah. Great little place. Our median age was sixty-two, but it was cozy and warm."

red @talkingmouth "Cool. You mentioned that you had 'long mornings' of battling at the gym, though? I didn't even know you had any sort of connection to a gym."

flannery @surprised "Oh, yeah, I guess I didn't mention. My grandpa was the gym leader of Lavaridge."

red @happy "Hey, that's cool."

flannery @happy "Hot, actually. We were a Fire-type gym."

red @talkingmouth "But it sounds like you battled as well? How'd that happen?"

flannery @talking2mouth "Oh, grandpa would always let me watch his battles. And if it was against a weaker trainer, he'd give me his Pokémon and let me battle in his place."

red @confused "Is that legal?"

flannery @talking2mouth "Hoenn's pretty casual about stuff like that. It was fine."

red @talkingmouth "Noticed you're using past-tense, though."

flannery @sad "Yeah... my grandpa left the gym to become an Elite Four member."

pause 1.0

flannery frownmouth @veins furious "And then left the {i}region{/i}, to go be a gym leader in another one! What the hell, old man! You took a {i}demotion{/i}, just so you could get away from me?!"

red @confusedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

flannery -frownmouth @sweat happy "Ah... ha... ha... sorry! Lost my temper there."

red @talking2mouth "So... who ran the gym after he left?"

flannery @talking2mouth "Well, me, actually. I'd had a lot of practice. I mean, I had a lot of practice battling. All the other stuff, about, like... running a gym... hiring trainers... payroll... marketing..."
flannery @sad "I kinda had to learn that on the job."

red @confused "Okay, surely dropping your gym duties in the hands of a child isn't legal."

flannery @sad "I mean, I was fourteen."

pause 1.0

flannery @closedbrow talkingmouth "Nah, that doesn't make it better, does it?"
flannery @thinking "Yeah, it wasn't {i}technically{/i} legal, but, again... people in Hoenn are cool about it."

red @talking2mouth "What about school?"

flannery @talking2mouth "Oh, I was homeschooled."

pause 1.0

flannery @surprised "Oh, but, uh, I'm not one of those religious wackos! Like, I believe in evolution, and I know Arceus is just a Pokémon, not a god."
flannery @sweat happy "I was just homeschooled 'cause the nearest school was miles away, down a rocky mountain path."
flannery @talking2mouth "It was just convenience, honest. I'm pretty darn sure that I don't believe any out-there stuff."

red @happy "Well, hey, it's good to make contact with a country girl. I figured everyone in this school was a city slicker."

if (GetRelationshipRank("Serena") > 0):
    red @thinking "Or pretending to be a city slicker, anyway."

flannery @talking2mouth "Yeah. So I've kinda been holding the fort down for a few years. My grandpa still gets paychecks from the league for running the gym, but he just forwards them to me."

flannery @happy "I made enough money from them that I could afford to go here. So that's what's happening!"

red @confused "At the risk of you saying 'people in Hoenn are cool' again, is it alright to just have a gym shut down for a year? Won't there be a huge bottleneck of trainers to fight your gym?"

flannery @thinking "Nah. The average trainer's journey takes fifteen years, after all. A year of waiting isn't that much."
flannery @happy "Besides, in Hoenn, battling's kinda secondary to contests. The Hoenn League focuses most of their attention there."

red @surprised "Really? That's wild to hear. Can you tell me more about that?"

flannery @talking2mouth "Well, contests have always been big in Hoenn. They were invented there. Then we had a Champion who was, before he became Champion, a famous contest star."
flannery @thinking "Um... what was his name... Wal... Walhart? Walmart? Waluigi?"

if (2 in persondex["Instructor Wallace"]["ClassesKnown"]):
    red @surprised "Are you talking about Instructor {i}Wallace?{/i}"

    flannery @happy "Oh, yeah, that's the guy! But why do you call him 'Instructor?' It's not like he goes here."

flannery @talking2mouth "Anyway, he was super-famous on the contest circuit before he became Champion. So that gave contest coordinating even more of a spotlight."
flannery @happy "People really loved him. And, oh my god, you wouldn't believe it, he was {i}so{/i} pretty."

if (1 in persondex["Instructor Wallace"]["ClassesKnown"]):
    red @thinking "Yeah... no, I believe it. I could grate cheese on those abs."

flannery @thinking "But he, uh, was defeated in, like, six months. By the Champ he'd just unseated, actually."
flannery @sweat happy "So... the tabloids love figuring out what happened there. Personally, I think that they were dating, and just switched positions so they could both put 'National Champion' on their resumes."

red @happy "Right. Do you have {i}any{/i} evidence for that?"

flannery @angrybrow happymouth "Do binders full of fanfiction count as evidence?"

red @closedbrow talkingmouth "Well, it's more evidence than {i}empty{/i} binders, I guess."

pause 1.0

red @thinking "Wait, did you write the fanfic, or just consume it?"

flannery @happy "Heh heh. I don't mean to brag, but I'm a pretty prolific writer. Whitney often asks me to write slashfic for her. And anything I write is {i}guaranteed{/i} to be hot."
flannery @tired "...Of course, I usually end up staying up all night writing, and then I crash {i}hard{/i} in the morning. And then Whitney makes fun of me for that."
flannery @veins angry "It's, like, girl, c'mon! I'm writing {i}your{/i} slashfic! Have a little empathy! And maybe a cup of coffee?"

red @happy "Heh. You two are funny. How'd you meet?"

flannery @talking2mouth "Online, actually. I'd spend about hours every day cooling off in the hot springs after a morning full of battles."
flannery @happy "While I was doing that, I used to work on stories and fanfics and stuff that I'd post online. Whitney was a big fan, and she actually commissioned a few fics from me."
flannery @talking2mouth "Well, one thing lead to another, and we started chatting. Met up a couple times IRL. And then we found out we'd both be attending Kobukan Academy, and... that's pretty much our story."

red @happy "Sounds like a {i}very{/i} devious plan to get free commissions from you."

flannery @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
flannery @thinking "Nah, she wouldn't. Probably."

red @happy "What? Of course she wouldn't!"

if (persondex["Whitney"]["Value"] < 150):
    flannery @happy "Hey, you don't know her as well as I do!"

flannery @talkingmouth "Girl's sneaky. For real."

red @talkingmouth "Well, it's good that you've got a friend to keep you centered in the mornings."

pause 1.0

flannery frownmouth @sad "...Yeah."

pause 1.0

red @sad "Something wrong?"

flannery @sad "I mean... you know how I am in the mornings. I want to {i}not{/i} be that way. But none of the stuff I've tried works."
flannery @tired "Herbal teas, therapy, sleeping more, even really long showers in the morning... and I'm pretty sure that hypnotist wasn't an actual Esper."

pause 1.0

show flannery surprised with dis

red @thinking "Hm... you know, we don't get to have too many conversations like this, where you're just a chill, normal, woman, do we?"

pause 1.0

flannery -surprised @happy "Hah, now, see, if it was morning time, I'd kick your dick in for saying that!"

$ lowertimeofday = timeOfDay.lower()
red @thinking "Hence why I waited until [lowertimeofday]."

flannery @talking2mouth "Alright, smart aleck. Yeah, we don't get a whole lot of opportunities to talk like this. What's your point?"

show flannery surprised with dis

red @happy "No point. Just saying I like it."

pause 1.0

flannery @happy "Dude, cool down! You really had me going there for a moment."

red @talkingmouth "I'm serious. You're actually pretty cool. I want to see more of this Flannery."

pause 1.0

flannery -surprised frownmouth @sad "Yeah... so do I." 

pause 1.0

flannery @talkingmouth "...I'm open to suggestions."

pause 1.0

red @closedbrow talkingmouth "Well, uh..."

pause 1.0

red @confused "You mentioned that you used to stay up late writing a lot. Do you still do that?"

flannery @thinking "Yeah, most nights. I mean, Kobukan Academy, right? I've got {i}so much{/i} material to work with."

red @talkingmouth "Okay, so that's not great. Kobukan takes a lot out of us. Maybe you need to {i}not{/i} do that?"

flannery @sad "...I guess I could try. But without the hot springs, writing's the only thing I can do to cool off."

red @talkingmouth "Right... and I guess you don't really have time to do it other than right before bed?"

flannery @talkingmouth "No. I mean, you know how busy we are with studying and training and stuff."

red @thinking "Yeah, I definitely get ya."
red @talkingmouth "Okay. What about the hot springs? Maybe they were a bigger, more important, part of your cooling-off period than we thought?"

flannery @talking2mouth "Man, you're going to have to be more creative than that. I've thought of everything you can think of, I promise. The long showers in the morning were to try and replicate the hot springs."

if (not IsBefore(17, 4, 2004)):
    flannery @thinking "Although I stopped doing that after Tia moved in, since she sleeps even later than I do."

    flannery @talkingmouth "Still. I don't think that's it."

red @talkingmouth "Okay... well, I've got one more idea."

flannery @sadbrow happymouth "I'll take anything."

red @thinking "You mentioned that when you were running the Lavaridge Gym, your battles were in the morning. Does that mean you closed the gym in the afternoon?"

flannery @talkingmouth "Yeah. We closed at noon, sharp. It was a bit of an early close, but the gym wasn't ever very busy, and if I was going to get eight hours of schooling, I needed to close early."

red @happy "Well... there's gotta be a connection there, right? Maybe, like, your body remembers the stress of the battles in the gym every morning, and it won't let you calm down and realize there's no threat."

flannery @surprised "Dude. Are you seriously suggesting I've got PTSD from {i}Pokémon{/i} battling? In an official gym? In what was basically {i}my{/i} gym? In my hometown? Surrounded by my family friends?"

red @sad "Er... I was a lot more confident in my theory before all those question marks..."

flannery @talking2mouth "Nah, it's not that. Maybe I'm literally just the {i}worst{/i} at mornings."

red @talkingmouth "Maybe... maybe. Mind if I do some research into this?"

flannery @surprised "Huh?"

red @talkingmouth "I really want to see if I can help you. And I'm curious, anyway. You're almost a completely different person in the mornings. I want to know what that's about."

flannery @thinking "I mean... yeah, I guess you can do some research. If you can even manage to find the time with how crazy Kobukan runs us. Wait, what kind of research?"

flannery @angry "You aren't going to do anything weird, are you?"

red @confused "I mean... maybe? I have no idea what I'm going to do. I was planning on just going on the internet and searching up 'girl wakes up angry and gets calm in afternoons why?'"

flannery @tired "Ugh, don't do that. If you say I'm a girl, they'll say it's some hormonal bullshit, or that it's my period or something. That's what all the doctors say."

redmind @thinking "...Don't ask. {b}Do not ask.{/b}"

red @confused "Are you sure it's not that?"

redmind @thinking "Damn it."

show flannery:
    ease 0.5 ypos 1.2 zoom 1.3

flannery furious "Yes, I'm sure it's not that! And you can take your casual misogyny and shove it right up your ass!"

red @surprised "W-w-wait! I'm not sexist! Some of my best friends are women!"

show flannery surprised with dis:
    ypos 1.2 zoom 1.3
    pause 1.0
    ease 0.5 ypos 1.0 zoom 1.0

pause 1.5

flannery -surprised frownmouth @talkingmouth "Uh... that doesn't work in this situation."

red @closedbrow talkingmouth "Yep. Yep, I see that now."

red @talkingmouth "But, seriously. I want to help you. Obviously, there's not a whole lot I can do--I'm just a student. But what I {i}can{/i} do, I will."

flannery @happy "Thanks." 
flannery -frownmouth @sweat sadbrow happymouth "Uh... I'd also like to say... that I probably won't be as responsive to your help in the mornings. So maybe don't mention that you're helping me until after lunch."

red @happy "Won't make that mistake again!"

flannery @talking2mouth "Thanks for your patience. You're pretty cool, no matter what Whitney says about you."

red @surprised "What?"

if (persondex["Whitney"]["Value"] > persondex["Tia"]["Value"]):
    flannery @happy "Hah, just kidding! Actually, she's been talking a lot about you. In a good way. So, y'know, there's that."

    $ ValueChange("Whitney", 3, -0.5)

    narrator "You gained three points with Whitney!"

else:
    flannery @happy "Hah, just kidding! Actually, she's been really appreciating how much attention you've been giving Tia. Tia's been really happy recently."

    $ ValueChange("Tia", 3, -0.5)

    narrator "You gained three points with Tia!"

red @talkingmouth "Good to know."

red @talkingmouth "I'll, uh, get back to you as soon as I have any leads on what might be happening."

flannery @happy "Cool. Thanks, man. Don't stress yourself out over it, though. But if you actually figure out why I turn into a raging morningzilla, I'll give you an unlimited pass to the Lavaridge Hot Springs."

red @happy "Heh. Well, now I've {i}gotta{/i} figure it out. I'm coming for that pass! It's a challenge, now!"

flannery @happy "Heh. I've been an acting Gym Leader long enough to know what to say to that."

flannery angrybrow happymouth "Bring it on, {color=#0048ff}challenger!{/color}"

$ persondex["Flannery"]["Relationship"] = "Challenger"
$ persondex["Flannery"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Flannery evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Challenger{/color}'!"

return