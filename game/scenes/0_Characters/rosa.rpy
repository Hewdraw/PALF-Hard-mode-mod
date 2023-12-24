init python:
    def RosaHasUnseenScene():
        if (GetCharValue("Rosa") >= 10 and personalstats["Knowledge"] >= 4 and GetRelationship("Rosa") != "Fanboy"):
            return "Rosa1"
        return False

label Rosa1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Rosa"]["Events"].append("Level2SceneVer2")

scene city_B
with Dissolve(2.0)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/joinavenue.mp3", channel='music', loop=True, fadein=1.5, tight=None)

show screen songsplash("Join Avenue", "Zame")

$ renpy.music.play("Audio/large-crowd-talking.mp3", channel='crowd', loop=True, fadein=1.5)

narrator "While walking through Inspira city, you suddenly hear a loud hubbub coming from around the corner."

red @confusedeyebrows "Hm? What's happening here...?"

show rosa sweat happy with Dissolve(2.0):
    ease 1.5 xpos 0.7
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.3
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.9
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.1
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.5
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    repeat

rosa "Hi! Rosa here, yep! Thank you so much, all of you! I really can't thank you enough for your support!"

narrator "You suddenly spy Rosa, desperately dashing between a multitude of people who all seem to be clamoring for her attention."
narrator "She signs autographs, notebooks, one young boy's shorts..."

red @happy "Ah. Well, that's the problem with being a world-famous actress, I guess. Any time you step outside, you're going to have people clamoring for your attention."

rosa surprised "Oh! That's--"

red @confusedeyebrows frownmouth "Hm. It looks like she just saw me, and...?"

show rosa:
    ease 0.5 xpos 0.5

rosa -sweat -surprised "Alright, everyone! Sorry to end it early, but the show's over!"
rosa @talkingmouth "Got a big night of filming, so I really have to get my shopping done before then."
rosa @happy "Bodyguard? Mind clearing a path?"

redmind @confusedeyebrows frownmouth "Bodyguard? Really, me? Who would buy that?"

$ renpy.music.stop(channel='crowd', fadeout=1.0)

pause 1.0

redmind @surprisedbrow "Huh. Well, she {i}is{/i} convincing."
redmind @thinking "Right, now, what would a bodyguard say in this situation...?"

red @angrybrow talking2mouth "Uh... right you are, miss. {w=0.5}You've got an appointment. {w=0.75}With the director. {w=1.0}Of movies."

pause 1.0

show rosa happybrow frownmouth sweat with dis

pause 2.0

$ renpy.music.play("Audio/large-crowd-talking.mp3", channel='crowd', loop=True)

"Unruly Crowdmember" "\"Hey! That guy's not actually a bodyguard!\""
"Brutally Honest Crowdmember" "\"Yeah! He's just a crappy actor!\""
"Aghast Crowdmember" "\"Just... indescribably bad, actually.\""

rosa -happybrow -frownmouth -sweat @happy "Hey, hey, guys! Alright, he's not my bodyguard, but he {i}is{/i} going to help me shop. So say goodbye to your favorite Rosa, and tune in for my next movie, {i}Broken Bird{/i}, coming to theaters near you soon!"

$ PlaySound("class_groan.ogg", "crowd2")

pause 1.0

rosa @sadbrow talkingmouth "Aw, I love you guys, too! But I really need to leave now!"

$ renpy.music.stop(channel='crowd', fadeout=1.0)

narrator "It takes another ten minutes for Rosa to successfully disperse the crowd. You do your best to move them away, as well."

rosa @happy "Phew. That was fun!"

red @happy "Imagine it gets exhausting, though."

rosa @happybrow "Nah, I'm totally used to it!"

red @happy "Oh, good."

pause 2.0

rosa @sad "Aw, it's becoming an instinct. I actually meant to say 'yes, very.' But I'm so good at lying, I guess I've gotten to the point that I can't stop."
rosa @surprised "Wait... oh!"
rosa @happy "That's a super-fun idea for a character! I need to text this to my manager. Like, the heroine is forced to only tell lies? It'd probably work as a romantic comedy."
rosa @thinking "Although, depending on how we play it out, we could probably have it work as a horror." 
rosa @talkingmouth "Maybe we'll cut it two different ways--release the horror version in the East markets, and the comedy version in the Western markets?"

red @talkingmouth "So, you're involved in the writing of your movies as well?"

rosa @talkingmouth "Some of them. Usually just up to the ideation stage, though."

red @confusedeyebrows talking2mouth "Ideation?"

rosa @talkingmouth "Yeah, that's the first part of making a movie. Ideation is the stage where we think up what the script will be."
rosa @happy "After that is writing, then pre-marketing, then shooting, then post-marketing, then market research!"

red @thinking "Lots of markets there."

rosa @happy sweat "Yeah, the business side of my industry gets pretty intense. I'm pretty lucky that I get to just work on movies I want to, though."
rosa @talkingmouth "A lot of actresses don't get to do that. They end up just doing coffee commercials for ten years, and then they're too old to be leading ladies."

red @thinking "Huh. How did you avoid that?"

rosa @happy "Oh, it's kinda a long and boring story. Plus, you can read the whole thing on pretty much any of my wiki pages. You sure you want to hear it?"

red @talkingmouth "You need to shop, right? Why don't you tell me while we do that?"

rosa @surprised "Oh. Um, no, I don't need to shop at all. Actually, my manager has people do that for me."
rosa @sad "Plus... it's difficult for me to figure out what I'm even allowed to buy. Most things are off-limits for me, since buying them could be seen as unsanctioned endorsement."

red @confused "Damn. Rosa, uh, forgive me for asking, but... how do you even live like this? It sounds like you're not allowed to breathe air that hasn't been approved by Pokéstar Studios."

rosa happy sweat "Oh, it's not a hassle! There aren't that many rules. And I can--"

pause 1.0

rosa -sweat angry "Gah, I did it again!"

pause 1.0

rosa -angry frownmouth @sad "Okay, no characters--just Rosa.{w=0.5} It's pretty hard sometimes. But I also get to do the best job ever, so I think it's a fair trade-off. And if it ever became too much, I could just leave."

red @talkingmouth "You really love being an actress, then?"

rosa -frownmouth @happy "I couldn't begin to imagine a better job. I love everything about it. The fame. The attention. The money."

red @surprised "Uh... I was kinda expecting you to say something..."

rosa @sad "More noble?"

red @thinking "Maybe a little bit."

rosa @happy "Hah! If I was going to be noble, I would have become a firefighter, instead of just playing one in {i}Heartburn{/i}!"
rosa @talkingmouth "Of course, you know, if interviewers ask me why I do it, I'll say it's because I want to leave something for the next generation, but..."
rosa @thinking "I mean, have you seen my films? {i}Every{/i} actor says they're doing it for the kids, but I'm not sure I want kids watching my movies."

red @talkingmouth "I did watch one of your films, actually. Leaf recommended I watch, uh, {i}Provoked{/i}. She said it was required for cultural literacy."

rosa @surprised "Oh, wow! She's a {i}really{/i} hardcore fan, then. With a strong stomach. I wonder how she even got a copy? A parents' organization started buying them up to destroy them, last I heard."

red @confused "Yeah. About that. Uh, that one scene..."

rosa @sadmouth "Yup, it was a prosthetic."

red @thinking "Oh, phew."

rosa @happy "Anyway, I don't want kids watching that, for obvious reasons. That's {i}one thing{/i} those parents got right."

red @confusedeyebrows "So, this is kinda a weird question--and tell me if I'm getting too personal--but why are you at Kobukan?"
red @thinking "It seems like everything about your time here is really restricting, and you're not getting the same experience as other students. So... why come?"

pause 1.0

rosa @sad "Well... that's kinda connected to how I became an actress."

red @happy "Aw, shucks. Guess you {i}do{/i} have to tell me the full story, then."

rosa @happy "Oh, well."
rosa @talkingmouth "It kinda happened on accident."

if (IsBefore(23, 7, 2005)):
    rosa @talkingmouth "I was just a regular, registered, Pokémon trainer five years ago. I was going on my adventure. I'd even gotten a gym badge."
    red @surprised "Wait, five years ago? Aren't you twenty?"
else:
    rosa @talkingmouth "I was just a regular, registered, Pokémon trainer six years ago. I was going on my adventure. I'd even gotten a gym badge."
    red @surprised "Wait, six years ago? Aren't you twenty-one?"

rosa "Yeah, but Unova lets you become a trainer earlier."

red @happy "Huh. Neat. How much older?"

rosa @talkingmouth "Depends on the city. Driftveil lets {i}six-year-olds{/i} have Pokémon. But they're kind of a national embarrassment."
rosa @thinking "Anyway, I got my badge, and was just about to face Roxie, the Virbank City Gym Leader. But she'd had some sort of big argument with her Dad, so I had to go patch that over for them."

red @confused ".{w=0.5}.{w=0.5}.{w=0.5}Why?"

rosa @happy "Roxie's a pretty intense rocker. When she gets angry, the only way to get it out of her system is to let her play her music for a few hours. I couldn't wait that long, so I tracked down her Dad."
rosa @sad "Well, as it happened, her Dad was a frequent extra at Pokéstar Studios. He'd just got his first starring role, and..."

show rosa happybrow frownmouth sweat with dis

pause 1.0

red @surprised "Eesh. That bad?"

rosa -happybrow -frownmouth -sweat @talkingmouth "He wasn't going to be winning any Pokéys, I can tell you that much."
rosa @thinking "He actually handled the disaster that was his first movie with dignity. Like, he was really good about it."
rosa @sad "Anyway, I just happened to be in the area when the director, who I think was a bit frantic to get people to forget Pop Roxie's movie, grabbed me and asked if I wanted to be a star."

red @surprised "Uh-oh."

rosa @happy "Yeah, not a good start, is it? But I didn't have to do anything weird. They were actually shooting a music video there for Piers' song, 'Black2/White2.'"
rosa @talkingmouth "They just wanted me to stand in the background, but a bunch of people on the internet saw my hair, and wanted to know who I was."

red @thinking "Your hair?"

rosa @happy "Yeah, it's kinda my trademark. I always wear it like this, even before I became known for wearing it like this."

red @happy "Huh. What was the original reason?"

rosa @happy "Mmm... that's a secret. And you won't find that on any of my wiki pages, either."

red @talkingmouth "Ooh. Mysterious."

rosa @talkingmouth "Anyway, I was about to go back to Virbank and challenge Roxie--the music video only took three days to shoot--but there were a few other jobs for extras at the studios, and since I was on-set, they just re-hired me."
rosa @happy "And by the time those extra positions were done with, Piers' band's video page was just drowned in comments asking about 'Yankee Buns'."
rosa @talkingmouth "Well, Mr. Deeoh, the director, wanted to capitalize on my popularity, so he put me in a couple more videos. And then a few longer-form documentaries."
rosa @happybrow sadmouth "Luckily, as I became more popular, I lost the 'Yankee Buns' nickname. But my Galarian fans still call me that, mostly. I try not to go to Galar too often."
rosa @thinking "Anyway, after that, I started getting bigger and bigger roles, and..."
rosa @sad "Well, now it's like this." 
rosa @happy "It's Rosa! World-famous star, stealer of hearts, and putter of butts in seats!"

pause 1.5

rosa @talkingmouth "And that's my story." 
rosa @happy sweat "But, for real, the people on my wikis do a much better job of telling it. I think the mods on MovieWiki are all English PhDs."

red @talkingmouth "Maybe. But it's cool to hear it from the source."

rosa @happy "Anyway, does that answer your question?"

red @talking2mouth "Actually, it answered pretty much every question except the one I asked."

rosa @surprised "Eh?"

red @talkingmouth "Why are you {i}here?{/i} At Kobukan? You've explained how you got started as an actress, but, if anything, that just makes me wonder why you're trying to become a trainer even more."

pause 1.0

rosa @talkingmouth "Well. I'm kinda... it's kinda embarrassing to admit this. But, um..."
rosa @sadbrow sweat happymouth "I didn't mean to become so famous, and get all this attention and money and movies and stuff. It was kinda an accident."
rosa @sadbrow sweat happymouth "Maybe it's silly of me, but in my head, I still think of myself as a trainer first, and an actress second. This whole... world-famous star thing... is just a sidequest. A scene that'll be cut in the biography of my life."

pause 1.0

red @sad "Wow."

rosa @surprised "N-now, I'm not sure that, um, you know. That I can actually still be a trainer. I'm {i}very{/i} out of practice."
rosa @happy "You, in gym class, were the first fight I've had in a long time where you were genuinely trying to beat me."
rosa @talkingmouth "Honestly, I was kinda surprised when I hit your Pokémon, and there weren't any blood packets squirting off of them. I'm so used to pretending to be a trainer, that..."

pause 2.0

rosa @happy "Well. I'm here at Kobukan, because I want to find out for myself if I can still be a trainer." 
rosa @thinking "Or if I've just flipped the script, and have to play this new role forever now."

pause 1.0

rosa @happy "Which wouldn't be a bad thing, of course! I mean, world-famous actress? You're never going to hear me complain about that."
rosa @talkingmouth "It'd just be... {i}so{/i} awesome... if I could be both a brilliant trainer and a famous actress."

red @talkingmouth "Well, we know it's possible."

rosa @talkingmouth "Yeah. Diantha's a huge idol of mine. I'd die if I could meet her someday. Actually, I got into Psychic-types because of her Mega Gardevoir."
rosa @happy "I'd say that's probably the {i}most{/i} iconic Pokémon in the world."

red @happy "Guess I've got one more question, then, and I don't think the wiki will answer this one for me."

rosa @happy "Oh, yeah? I think the guys on WikiHair know me better than I know myself, but go ahead."

red @thinking "If you didn't actually come out here to shop, why {i}did{/i} you come out here?"

rosa @sweat happybrow sadmouth "Oh. Um... actually, I was trying to get away from my fans. There's a big group of them back on campus, and..."
rosa @happy sweat "I love them, of course. And everything they do. But every time I meet one, they act like it's the most important day of their life."
rosa @happy "I tell them I'm really nothing special when I'm not in front of a green screen, but I also don't want to ruin their mental image of me, so..."
rosa @talkingmouth "Sometimes it's nice to just get lost in the crowd once in a while."

red @confused "Looks like you didn't do too well this time, though."

rosa @thinking "It would probably be easier to blend in if I wore my hair differently..."
rosa @angrybrow happymouth "But that's {i}just not happening.{/i}"

red @happy "I bet your hair is the source of your powers. If your hair is cut, you lose your ability to act, right?"

rosa @happy "Haha! Maybe!"
rosa @thinking "Actually, my hair is pretty heavily insured. I think the studio actually {i}does{/i} think my hair is the source of my power."
rosa @thinking "Hm... that'll mess with the timeskip design we had planned for {i}Broken Bird{/i}. But they can probably cut it out in post."

pause 1.0

red @happy "Hey, you know Leaf?"

rosa @thinking "Hm? Oh, yeah. She's a big fan of mine, right?"

red @talkingmouth "Yeah. Would it be alright if I told her about this conversation? I think she'd be really interested in hearing a personal story like this."

rosa @happy "Oh, go ahead! And thanks for asking. A lot of people think that they can just tell anyone any part of a public figure's life."

red @happy "Cool."

$ ValueChange("Leaf", 3, -0.5)

narrator "Later, you will tell Leaf about this encounter. Though it's a story she heard before, she grills you on the details for hours. You gained three points with Leaf!"

pause 1.0

rosa @happy "Hey, is it cool if I ask {i}you{/i} a question?"

red @surprised "Sure. Be my guest. But what could a star like you want to ask someone like me?"

rosa @sadmouth "When you were pretending to be my bodyguard... I've never seen someone so bad at acting."
rosa @thinking "It's like... like you conveyed the idea that you were trying to trick people into thinking you were a bodyguard way more than you did the idea that you actually {i}were{/i} one."
if (not IsBefore(1, 5, 2004)):
    rosa @thinking "Is that because of your empathy power? Or are you just a {i}really{/i} terrible actor?"

red @angrybrow talking2mouth "Hey. Kinda offended. I was playing a role I had absolutely no rehearsal for. What would even make you think I could pretend to be a bodyguard, anyway?"

rosa @talkingmouth "Well, you're tall, fit, and you've got a ferocious attack Pikachu on your heels."

red @confused "Ferocious attack Pikachu?"

if (IsBefore(1, 5, 2004)):
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu cocky "Pika!"
else:
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    libpikachu angryeyes happymouth "Pika!"

rosa @happy "Yep!"

if (IsBefore(1, 5, 2004)):
    red @talkingmouth "Well. I guess I'm just really, really, {i}really{/i} bad at acting."

else:
    red @talkingmouth "I think it might be, partially, my Frienergy. But I think the other part is... well, I'm just really, really, {i}really{/i} bad at acting."

rosa @talkingmouth "I could give lessons!"

red @surprisedeyes surprisedeyebrows talkingmouth "Really? Why? Of all the things that your manager could not let you do, that feels like it makes the most sense."

rosa @sweat happy "Well... I might not be {i}allowed{/i} to, technically..."

if (not IsBefore(1, 5, 2004)):
    rosa @talkingmouth "Maybe it's just part of your power, but I feel comfortable around you."
    
else:
    rosa @talkingmouth "I just like talking with you."

rosa @sweat happymouth "You don't freak out over me, which is... actually pretty rare. And pretty cool, too."

red @talkingmouth "Maybe I'll start freaking as I watch more of your movies."

rosa @thinking "Hope not!"

red @talkingmouth "I gotta say, though. You're pretty bad at getting away from your fans."

rosa @surprised "Huh?"

red @talkingmouth "Because, at some point during this conversation, you turned me into one. Hope that doesn't ruin anything."

rosa @sadbrow happymouth "Not at all. As long as you're not the weird kind of fan who obsesses over my feet." 

red @thinking "As far as I can tell, I don't have a foot thing."

rosa @happy "Then welcome to the show, {color=#0048ff}fanboy{/color}!"

$ persondex["Rosa"]["Relationship"] = "Fanboy"
$ persondex["Rosa"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Rosa evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Fanboy{/color}'!"

return