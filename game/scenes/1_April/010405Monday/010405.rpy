label day010405:
call calendar(3) from _call_calendar

$ timeOfDay = "Morning"

queue music "Audio/Music/Road to Viridian City.ogg"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")

redmind uniform thinking "It's finally the first day of classes. I spent the weekend getting to know this place, so I shouldn't get lost again."
redmind happy "I'm getting goosebumps! Let's do this!"

show calem uniform:
    xpos 0.25 alpha 0.0
    ease 0.5 alpha 1.0

show ethan uniform:
    xpos 0.5 alpha 0.0
    ease 0.5 alpha 1.0

show brendan uniform:
    xpos 0.75 alpha 0.0
    ease 0.5 alpha 1.0
    
$ renpy.pause(0.5, hard=True)
    
calem "Ready to get some breakfast?"
brendan happy "Yeah! Never skip breakfast. It's the most important meal of the day."
ethan thinking "I'm pretty sure I read a headline somewhere that said that was misinfo by Big Breakfast..."
red -happy "We're heading to the main cafeteria?"
calem "You got it."
show calem surprised with dis

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu neutral_2b "Pika pika!"

red "Oh, can [pika_name] come with us?"

calem -surprised "I went ahead and checked with the front desk yesterday, and they said Pokémon must remain in their rooms or in a Poké Ball outside of the room unless authorized by the academy."
brendan @talkingmouth "So, I guess we can bring 'im as long as he stays in his Poké Ball?"
ethan @sadbrow "Not sure he'll go for that..."
show calem surprised with dis
show brendan surprised with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite1.ogg", channel="altcry", loop=None)

pikachu angry_3 "Pi-{i}ka! {/i}"

calem thinking "Perhaps not, then."
ethan happy "Yeah, some Pokémon just don't like to spend time in their Poké Balls! I tried putting my Pichu back home in a luxury ball, you know? Thought it'd be cozier."
ethan sad "Didn't do anything, and cost me a good chunk of change, too."
brendan -surprised "Dudes, that's actually pretty dope.{w=0.5} It's like you've got rogue Pokémon or something."
calem -thinking talkingmouth "It's odd. I've never heard of a Pokémon that exhibits that sort of behavior before today, and now I've heard of two."
red thinking "Maybe... it has something to do with their evolutionary line? Pichu evolves into Pikachu, after all."
brendan surprised "Woah, it does?! I thought it was a Plusle and Minun situation, where they're symbiotic, but don't evolve."
calem happy "Then I'll really blow your mind when I tell you about Raichu."

red sadeyes sadeyebrows -frownmouth "Sorry, [pika_name], but you're gonna have to stay here until I get back."
red "...Unless you want to come along in your Poké Ball?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu angry_2 "Pika...!"
show calem surprised with dis
show brendan surprised with dis
show ethan surprised with dis
    
red happy "All right, suit yourself.{w=0.5} There's some food in my drawer, but don't eat all of it at once! We'll be back after classes are over."
red angrybrow frownmouth "And don't sneak out and follow me, got that?"

pikachu happy_3 "Pika Pikachu!"

pause 2.0

show calem:
    xpos 0.25
    ease 1.0 xpos 0.4

show ethan:
    xpos 0.5
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert uniform:
    xpos -0.5
    ease 1.0 xpos 0.2

pause 2.0

red -angrybrow "Yeah?"
hilbert "We're going to the cafeteria, aren't we?"
ethan angrybrow talkingmouth "I kinda figured you wouldn't want to come."
hilbert sad "...I require food to live.{w=0.5} Didn't think I'd have to tell you that one."
calem thinking "You could go alone."
hilbert -sad @talkingmouth "I could."
brendan "...But you don't wanna?"
hilbert angrybrow @talkingmouth "The parameters I was operating under have changed. Now, I want to go to the cafeteria and eat a delicious breakfast with you. You want my life story, or can we leave it at that?"

pause 1.0

ethan happy "Well... I guess let's go, then. Good to have you with us, Happenstance!"

show hilbert:
    xpos 0.2
    ease 1.0 xpos 1.5

pause 1.0

play sound "Audio/Door_Close1.mp3"

red closedeyes sadeyebrows talkingmouth "It's, uh, it's Hilbert."
ethan surprised "Why, what'd I say?"

pause 0.75

window hide

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_2

show blank2 with dis:
    alpha 1.0
    
$ renpy.pause(2.0, hard=True)

hide ethan
hide brendan
hide hilbert
hide calem

show relichall_A behind brendan with dis:
    alpha 1.0
    
pause 1.0

$ renpy.transition(dissolve)
show screen currentdate

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0

show may uniform:
    alpha 0.0 xpos 0.5
    pause 0.5
    ease 0.5 alpha 1.0
    
$ renpy.pause(1.0, hard=True)

red "Oh, hey, May! Waiting for us long?"

show may:
    xpos 0.5
    ease 0.5 xpos 0.33

show brendan uniform:
    alpha 0.0 xpos 0.66
    ease 0.75 alpha 1.0 xpos 0.66
    
hide blank2

may happy "Nah! Good to see you again! I didn't get to see much of you over the weekend!"
red happy "Well, even if Brendan and I were running the same kinds of errands, I wasn't planning on third-wheeling the whole time!"

may "Speaking of third-wheeling...{w=0.5} you still haven't met my other roommates besides Serena, have you?"
red -happy "Hopefully we'll bump into at least a couple of them today on the way to class."
may -happy "Well, if I see any of them, I'll let you know. Oh, that reminds me, sweetheart! Have you given [first_name] your phone number?"
brendan surprised "Huh! No, I haven't. Good catch. Here, [first_name]!"
show brendan happy with dis

$ BecomeContacted("Brendan")

brendan "Hey, why don't you give [first_name] your contact info, too? That way, if my phone's turned off or whatever, he can still reach me."
may surprised "Huh? Oh, um, sure! If you're okay with that."
red "No problems here."
show brendan -happy with dis
show may happy with dis

$ BecomeContacted("May")

ethan uniform happy "Alright, let's head out! I don't know if that's my stomach or Hillenbrand growling, but it's nothing a big plate of eggs won't fix."

scene cafe with Dissolve(1.5)
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
$ renpy.pause(1.5, hard=True)

hide blank2

red uniform "Damn, this is fancy!"

show calem uniform thinking at dissolvein:
    xpos 0.166

calem "I suppose such luxuries were a tad out of reach in Pallet Town?"
red "Yeah."

show ethan uniform happy at dissolvein:
    xpos 0.333

ethan @talkingmouth "Nothing like Kalos, I bet! I heard that in Kalos, even the smallest village has a five-star restaurant!"
calem surprised "You've... heard a lot of interesting things about Kalos."
show calem -surprised with dis

show calem:
    xpos 0.166
    ease 5.0 xpos 0.07

show brendan uniform happy at dissolvein:
    xpos 0.499

brendan "Hey, May, look! They've got Basculin tartare!"

show may uniform sadbrow at dissolvein:
    xpos 0.666

may "...Yeah, but you're a vegetarian, sweetie."
brendan happybrow angrymouth "Er... Of course! I didn't forget. It's just... {i}Basculin{/i} tartare! Swanky!"
show may happy with dis

show hilbert uniform sadbrow angrymouth at dissolvein:
    xpos 0.833

hilbert "{size=30}Damn it, where {i}is{/i} she? Come on out, you...{/size}"

redmind confusedeyebrows frownmouth "What's {i}that{/i} about?"
show hilbert -sadbrow -angrymouth with dis

show calem:
    xpos 0.07 xzoom 1.0
    ease 0.5 xzoom -1.0

pause 1.5
    
calem "Oh, look who's joining us this morning."

show calem:
    xpos 0.07 xzoom -1
    ease 0.5 xpos (2.0/7.0)

show ethan:
    xpos 0.333
    ease 0.5 xpos (3.0/7.0)

show brendan:
    xpos 0.499
    ease 0.5 xpos (4.0/7.0)

show may:
    xpos 0.666
    ease 0.5 xpos (5.0/7.0)

show hilbert:
    xpos 0.833
    ease 0.5 xpos (6.0/7.0)

show serena uniform:
    xpos -0.5
    ease 1.0 xpos (1.0/7.0)

pause 1.5

ethan happy "Wait, wait, don't tell me. You're going to say 'personal space,' right, Calem?"
calem -surprised "I was going to, yes, but now it seems redundant to do so."

redmind "Hmm... Serena. Calem talked with her a few times during the weekend, but it seems he's still treating her with obvious forced casualness."
redmind "I'll add that to my list of 'things to ask about when we're closer.'"

red -confusedeyebrows -frownmouth "Morning, Serena."
serena "Good morning, [first_name]. Now, don't you look dashing in your new uniform?"
calem surprised "!"
calem -surprised happymouth "Yes, doesn't he? It fits very well on him, I daresay."
serena sadbrow "Ah, well, it's certainly a new look. Perhaps I've just grown accustomed to seeing {i}you{/i} like this."
calem angrybrow -happymouth "...Yes, perhaps."

pause 2.0

redmind @confusedeyebrows frownmouth "...What the hell kinds of mind games are these two playing?"

hilbert @talkingmouth "Hey. Is your dormmate Hilda around?"
serena @surprised "Oh? No, I don't believe so. She said she was looking for someone."
ethan surprised "Uh-oh!"
show may surprised with dis
brendan surprised "What is it, dude?"
ethan thinking "Every time we talk about someone, they show up. So Hilda'll probably be here any second."
hilbert angry "Don't be superstitious."
ethan happy "It's not that, man, I just don't think we can {i}physically{/i} fit any more people here."
hilbert sad ".{w=0.5}.{w=0.5}.{w=0.5}"
hilbert -sad "You're right. I'll grab us a table."

show hilbert:
    xpos (6.0/7.0)
    ease 1.0 xpos 1.5

ethan "I'll go with him and make sure he doesn't start a fight."

show ethan:
    xpos (3.0/7.0)
    ease 1.0 xpos 1.5

show may happy with dis
brendan happy "I dunno about you guys, but I'm going to get some grub!"

show brendan:
    xpos (4.0/7.0)
    ease 1.0 xpos -0.5

show may:
    xpos (5.0/7.0)
    ease 1.0 xpos -0.5

pause 2.0

serena "Well, now that your friends have stepped away for a moment, perhaps we could talk?"

show calem: 
    xzoom -1 xpos (2.0/7.0)
    ease 0.2 xpos 0.75 xzoom 1

show serena:
    xpos (1.0/7.0)
    ease 1.0 xpos 0.25

calem "Yes, we can do that."

redmind @thinking "Oof, cold."
redmind @surprised "Wait. His friends haven't stepped away! I'm right here!"

serena sad "...It's about..."
show calem thinking with dis
serena "..."
serena -sad "About the Student Council."
calem surprised "Oh?"

stop music fadeout 1.5
queue music "Audio/Music/Waltz of the Sea.mp3"

serena "We've done leadership work before, right, Calem?{w=0.5} Having membership in the Kobukan Student Council on our resumes would look really, really good to future employers."
calem @thinking "Hm. I'm not aware of the specifics, but I've heard that Kobukan's Student Council is extremely hard to get into."
show calem surprised with dis
serena @thinking "Yes, we'd only have a month to campaign." 
serena "But we've certainly bested greater odds together before."
serena @sadbrow "Remember Professor Sycamore's internship, and how hard we worked on getting you that?"
calem happy "True! I never would have managed to snag that without your ceaseless support."
serena @thinking "In any case, I think we should go for it. Since we only have a month to campaign, if we fail, well... there's not a lot of time lost, at least."
calem thinking "True. This would be a significant time commitment, far more so if we win, but perhaps it's something to look into."
serena pout "Well... we kinda have to decide now. It's our third day here. That 'Cheren' guy has already put up posters across half the school, and is giving speeches in the courtyard."
calem sad "Yes, well... given the policies he espouses, I wouldn't be surprised if the school's administration shoots him dead before the weekend."
serena happy "We might want to be a {i}bit{/i} less radical, to maintain our electability."
calem -sad "Yes, a bit."
serena "..."
calem "..."
serena pout "Well?"
calem sad "I'm... unsure. I truly need a bit more time to decide. Can you give me until tomorrow?"
serena "..."
serena -pout "Okay! But you {i}will{/i} answer me tomorrow, right?"
calem thinking "I swear it."
serena "Alright! Let's meet up here tomorrow morning and figure this out, then. Bye, Calem! Bye, [first_name]!"

menu:
    "Bye, Serena.":
        red @happy "Bye, Serena."
        redmind @thinking "Oh, so she {i}did{/i} know I was here. I was starting to wonder..."
       
    "Wait, count me in!":
        $ council_campaigning = True
        red @angrybrow happymouth "Wait, count me in!"
        show calem surprised with dis
        show serena surprised with dis
        red "Calem might need some more time, but I sure don't. I want to join you two on the Student Council."
        
        $ ValueChange("Serena", 1, 0.25, False)
        $ ValueChange("Calem", 1, 0.75)

        pause 1.5
        
        calem "Oh? Do you have... any experience with this sort of work?"
        show serena -surprised with dis
        red @happy "Man, I come from Pallet Town. You know I don't."
        red "But I'm ready to learn. I've got a month, right?"
        serena @sadbrow happymouth "Well... it'll be tricky. But I'm happy to help you, if you would accept my tutelage."
        calem thinking "Hm. You do have the sort of self-confidence and appeal that could make you popular amongst the student body, if we could refine your positions somewhat."
        red @happy "Yeah. I get that I have a month of campaigning ahead, and, honestly, I'm not even sure where to begin. Any tips from you two?"
        calem "Well... I'd try to get the ear of the current Student Council. {color=#0048ff}If you can get the previous council's endorsement, you're almost guaranteed to get in.{/color}"
        serena @thinking "There's also canvassing. {color=#0048ff}Going from student to student and engaging them directly on your positions.{/color}"
        calem @thinking "As a last resort, you can rely on inherent popularity. {color=#0048ff}Anything that puts you in the public eye, good or bad, raises your odds.{color=#0048ff}"
        red @surprised "Wait, good {i}or{/i} bad?"
        calem @sad "Unfortunately. That's politics."
        serena "Anyway, what a pleasant surprise this is. You didn't seem like the kind of guy who'd want to be involved with something like that."
        calem @happy "[first_name] is full of surprises!"
        calem "Oh, if you two are definitely going to be working on Student Council matters together, you should exchange contact information."
        serena @sad "..."
        serena "Yes, of course."
        redmind "Hm. Did I imagine, that, or...?"

        $ BecomeContacted("Serena")
        
        serena "Splendid. I look forward to talking with you two about our meteoric rise to Student Councilhood. Calem, [first_name]."

show serena at dissolveaway:
    xpos 0.25

show calem:
    xpos 0.75
    ease 1.0 xpos 0.5

pause 2.0

menu:
    "What's your problem?":
        red @angry "What's your problem?"
        calem surprised "Huh?"
        red frownmouth "She's nice, gorgeous, and obviously head over heels for you. You treat her like she's a nuisance."
        red talking2mouth "And I know you like girls, so why not her?"

        $ ValueChange("Calem", -1, 0.5)

        calem angry "I apologize, but I simply will not discuss this with you."

        red closedeyes "{i}Sigh{/i}... Fine. I can tell this is a sore point you've been wrestling with for much longer than you've known me. Still. Get it together."
        calem -angrymouth "{cps=*0.2}I appreciate the advice.{/cps}"
        calem -angrybrow "Shall we go?"
       
    "She seems nice.":
        red happy "She seems nice."
        calem sad "She is. Far nicer than I deserve."
        calem "..."
        calem -sad "Well, enough of that. Shall we go?"

    "You alright?":
        red sadeyebrows sadeyes "You alright?"
        
        calem sad "...I'm wrestling with whether or not I should join Student Council.{w=0.5} I certainly want to, but I'd spend almost every day with her..."
        calem angrybrow "And it's pretty clear that's what she wants."
        red "You don't want that?"
        calem happy "I'm...{w=0.5} no longer sure what I want, to be honest!"
        $ ValueChange("Calem", 1, 0.5)
        calem -happy "But I appreciate you being my sounding board while I figure it out."
        calem "Well, enough of that. Shall we go?"

red "Yeah, let's go get breakfast with the others."

if council_campaigning:
    redmind thinking "Now that I'm trying to get on the Student Council, I should also tell Cheren. Maybe we could exchange tips!"

scene cafe with Dissolve(1.5)

show bianca uniform with dis

bianca "..."
redmind uniform "..."

show bianca:
    ypos 1.0 zoom 1.0
    ease 0.2 ypos 1.05 zoom 1.1

redmind @confusedeyebrows "...?"

show bianca:
    ypos 1.05 zoom 1.1
    ease 0.2 ypos 1.1 zoom 1.2

calem uniform "She's approaching you."
red @closedeyes talking2mouth "Yeah, got it, thanks."

show bianca:
    ypos 1.1 zoom 1.2
    ease 0.2 ypos 1.15 zoom 1.3

redmind @surprised "Why am I sweating so much...?"

show bianca:
    ypos 1.15 zoom 1.3
    ease 0.2 ypos 1.2 zoom 1.4

red talking2mouth "Hey, uh, can I help you?"

$ BecomeNamed("Bianca")
bianca happy "Hi! I'm Bianca. Cheren told me to go find the 'handsome guy in the red hat.'"

red @surprised "Er..."

bianca -happy "So of course, I thought that was you, but before that I thought it was the other guy in the red hat but he just scowled at me and then I thought maybe it was the other other guy in the red hat, but then he said--"
bianca happy "--he had no idea who Cheren was so now I'm asking you and I really hope you're the one because I'm getting really flustered talking to all these cute guys with red hats!"

show calem uniform surprised at dissolvein:
    xpos 0.25

calem "Wait... why didn't you ask me?"

show bianca:
    ypos 1.2 zoom 1.4 xpos 0.5
    ease 1.0 ypos 1.0 zoom 1.0 xpos 0.75

bianca happy "Oh, you're cute, really, but I think Cheren was looking for a student, not a Professor!"

show calem deadbrow surprisedmouth at monochrome with vpunch:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0    

calem "I'm... I'm eighteen..."

show calem at monochrome:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0

show bianca:
    ypos 1.0 zoom 1.0 xpos 0.75
    ease 1.0 ypos 1.2 zoom 1.4 xpos 0.5

bianca "Anyway, are you [first_name], because Cheren's impatient, and red hat number one is at our table arguing with my dormmate Hilda and--"
red surprised "Wait, did you say Hilda?"
bianca surprised "Oh, you know her?"
red thinking "Well, I know {i}of{/i} her. She's the only thing that scares Hilbert, apparently."
red surprised "Uh, Hilbert is red hat number one."
bianca -surprised "Okay.{w=0.5}.{w=0.5}.{w=0.5} So are you [first_name]?"
red happy "Oh, yeah! Does Cheren need me now? I was just about to get some food and sit with my dormmates."
bianca @talkingmouth "Nope, he just wanted me to give you a message!"
redmind thinking "What, like a Mafia Don? '[first_name] sleeps with da fishes...'"
bianca @talkingmouth "The message is: 'I'd like to talk to you after school. Please meet me here.'"
red -thinking ".{w=0.5}.{w=0.5}.{w=0.5}That's it?"
bianca @talkingmouth "Yep!"
red happy "Uh, alright, then! I'll be at the cafeteria later."
bianca happy "Mission accomplished!"

show bianca:
    xpos 0.5 ypos 1.2 zoom 1.4
    ease 2.0 xpos 1.5 ypos 1.0 zoom 1.0

redmind ".{w=0.5}.{w=0.5}.{w=0.5}I can't tell if this is just what it's like in the city, or if there's something about me that just attracts peculiar characters."
redmind "Maybe I'm the weird one?"

show blank2 with dis

pause 2.0

red happy "Hey guys!"
ethan uniform "Buddy! What was the holdup? Calem returned a bit ago. He looks a bit shell-shocked."
red "Just talking to another student. Hey, didn't you say you were going to stop Hilbert from getting into any fights?"
ethan surprised "What?! I thought I did! He was here just a moment ago!"
red @thinking "Well, I happen to know that this 'Hilda' person he's so terrified of has made contact. Guess it makes sense he couldn't hide for more than four days."

pause 1.0

brendan uniform angrymouth closedbrow "Dudes! Don't want to rush you, but homeroom's pretty soon."
may uniform surprised "Oh, shoot, you're right! Guess I'd better cram the rest of this down before we go..."
ethan "Hey, could you, like, put a piece of toast in your mouth and run to class?"
may frownmouth sadbrow "...I could, but I don't really see why? I have time to finish it here."
ethan sadbrow happymouth "Uh... nevermind!"

pause 1.0

hide calem

red "Hey, Calem, will you be okay?"
calem uniform sad "{size=30}I'm eighteen. Not old. My hair is naturally grey. I'm eighteen. Not old. My hair is naturally grey.{/size}"
red confusedeyebrows "Riiiiight. Well, uh, we gotta go. Make sure you come with us, okay?"
calem surprised "Huh?" 
calem sad "Oh, yes. Of course. Just give me a bit."

pause 1.0

red happy "Alright, let's go! Last one to the homeroom assignment board is a BAD EGG!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_3
scene blank2 with dissolve

$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
play music "Audio/Music/Beyond.ogg" loop fadein 3.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

scene academyold with Dissolve(2.0)

$ renpy.pause(2.0, hard=True)

hide blank2
hide cafe

show academy:
    xpos 0 ypos 0 zoom 0.625
    ease 3.0 zoom 1.0 xpos -700 ypos -575

$ renpy.pause(3.0, hard=True)

red uniform @surprised "Wow, this area of the campus is amazing!"

show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 1.0 zoom 1.1 xpos -730 ypos -300
$ renpy.pause(1.2, hard=True)

red "See what it says on the facade there?"
red @angrybrow "'Kobukan Academy.'"
red "Supposedly, this building has been around for nearly a century.{w=0.5} It's hard to believe. The condition of this place makes it seem like it was built yesterday."

show academy:
    zoom 1.1 xpos -730 ypos -300
    ease 1.0 zoom 1.05 xpos -730 ypos -300
$ renpy.pause(1.0, hard=True)

red @talkingmouth "I'm having a difficult time imagining that this is what I'll be looking at each day from now on."

show academy:
    zoom 1.05 xpos -730 ypos -300
    ease 1.5 zoom 1.0 xpos -700 ypos -575
$ renpy.pause(2.0, hard=True)

red @happy "Not that I'm complaining.{w=0.5} I'm just excited to be here. {w=0.5}Same as you guys, right?"

pause 1.0
show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 0.5 zoom 0.9 xpos -800 ypos -450
pause 1.0
show academy:
    zoom 0.9 xpos -800 ypos -450
    ease 0.75 zoom 0.85 xpos -100 ypos -350
pause 2.0
show academy:
    zoom 0.85 xpos -100 ypos -350
    ease 1.0 zoom 1.0 xpos -700 ypos -525
$ renpy.pause(2.0, hard=True)

redmind @thinking "Huh. I guess I ran a bit too quickly."
redmind @happy "Eh, whatever. I need to get inside and check the homeroom assignments."

show academy:
    zoom 1.0 xpos -700 ypos -525
    ease 4.0 zoom 1.4 xpos -600 ypos -600
$ renpy.pause(1.0, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_4

scene blank with Dissolve(1.0)
play sound "Audio/ExitBuilding.wav"

stop music fadeout 2.25
$ renpy.music.stop(channel='crowd', fadeout=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
scene academyhall with Dissolve(1.5)

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank
hide academy
hide academyold

redmind uniform "There's a cluster of students gathered by a bulletin board.{w=0.5} That must be the homeroom list."

window hide
show academyhall_blur with dis:
    alpha 1.0

show class_assign:
    alpha 0.0 xalign 0.5 ypos -50
    ease 1.0 alpha 1.0

show text "{font=fonts/consola_0.ttf}{color=#000000}{size=15}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 0.0 xanchor 188 ypos 634
    ease 1.0 alpha 0.7

$ renpy.pause(2.0, hard=True)

redmind surprised "{w=0.5}.{w=0.5}.{w=0.5}."
redmind "Wait. Oak?"
redmind "Professor Oak? Like Old Man Oak? Like my neighbor? Like [blue_name]'s grandpa?!"
redmind "He teaches here?! The faculty page of the website didn't say anything about this!"
redmind angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
redmind angrybrow "And... why is my name in a different font? It looks like someone just sharpied my name in..."

blue uniform "Well, well, well!"

show academyhall_blur:
    alpha 1.0
    ease 0.5 alpha 0.0
show class_assign:
    alpha 1.0
    ease 0.5 alpha 0.0
show text "{font=fonts/consola_0.ttf}{color=#000000}{size=15}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 1.0 xanchor 188 ypos 634
    ease 0.5 alpha 0.0

red ".{w=0.25}.{w=0.25}."

show blue with dis:
    xpos 1600
    ease 0.75 xpos 700

play music "Audio/Music/RivalTune.mp3" noloop
$ renpy.music.queue("Audio/Music/Road to Viridian City.ogg", channel='music', loop=True, fadein=4.0, tight=None)

$ renpy.pause(0.75, hard=True)

hide class_assign
hide academyhall_blur
hide text
    
blue @angry "I said, WELL, WELL, WELL!"
red "I heard you the first time."
blue @angrybrow happymouth "At least look at me when you're talking to me!"
blue @happy "But, wow, you actually got here before the bell!{w=0.5} Still slower than me, but that's natural."
redmind -angrybrow @confusedeyebrows "In what world have I {i}ever{/i} been slower than you?"
blue @closedbrow "So?{w=0.5} Which class are you in?"
show blue surprised with dis
red frownmouth "Your grandpa's, according to this.{w=0.5} You could've told me Old Man Oak was working here! I would've seen if he could pull some strings."
blue "Gramps'? Are you serious?"
blue sad "Why?{w=0.5} I thought I told him to--"
$ renpy.pause(1.0, hard=True)
blue angry "Ah, who cares?" 
blue closedbrow -angrymouth "Now I have a front row seat to watch you bomb in class!"
leaf uniform "Oh! You're all with Professor Oak?"

redmind surprised "That voice..."

show blue surprised:
    xpos 700
    ease 0.5 xpos 450

show leaf uniform:
    alpha 0.0 xpos 1800 
    ease 0.75 xpos 970 alpha 1.0
    
$ renpy.pause(0.75, hard=True)

show blue surprised:
    xpos 450

show leaf:
    xpos 970 alpha 1.0

red "Oh? Hey, uh, you!"
leaf "Long time, no see!"
leaf happy "Did you get lost on the way here?"
show blue angry with dis
red -surprised "Hey, give me a break, I thought we were done with that.{w=0.5} Didn't you say you had fun?"
leaf flirt blush "Hey, don't get it twisted.{w=0.5} I had lots of fun!"
show leaf -blush surprised with dis
blue "You know this windbag?"
leaf angrybrow talkingmouth "Uh, excuse me.{w=0.5} Don't interrupt a girl when she's talking to her friend."
show leaf surprised with dis
blue @talkingmouth "Yeah, right. I bet you don't even know his name."

pause 1.0

leaf embarrassed "Obviously it's..."

window hide
pause 1.5

leaf ".{w=0.25}.{w=0.25}."

show leaf at getcloser:
    xpos 970
    ease 0.9 xpos 840
    
$ renpy.pause(0.9, hard=True)

redmind "Huh. I can smell her perfume."
leaf flirt blush "{size=30}Psst, what's your name again?{/size}"

redmind "Uhhh, way too close for comfort."

red "{size=30}It's, uh, [first_name] [last_name].{/size}"
red "{size=30}And, uh, I'm a firm believer in personal space!{/size}"

show leaf at getfurther:
    xpos 840
    ease 0.9 xpos 970

leaf happy "Ah, yeah! [first_name]!{w=0.4} We're besties! Always been!"
blue closedbrow angrymouth "You're not fooling anybody!"
leaf surprised "Wait...{w=0.5} [first_name]?"
leaf happybrow talkingmouth "[first_name]! Oh, you're [first_name]!{w=0.5} You're friends with May, right?"
red "You know May?"
leaf -happybrow -talkingmouth "I would hope so. Being her dormmate and all."
red thinking "Okay... I've met Bianca, Serena, and May... so, flipping the coin of probability..."
red -closedeyes -frownmouth "You're Leaf?"
$ BecomeNamed("Leaf")
leaf happy "That's my name!"
blue surprisedbrow angrymouth "My god--you better cut the crap.{w=0.5} Your acting is so bad that it's pissing me off!"
red "Give it a rest, [blue_name]. I know who Leaf is."
red "I ran into her on our first day here and she helped me out of a tough spot.{w=0.5} We were both short on time so we forgot to introduce ourselves--"
show leaf surprised with dis
blue closedbrow "Like I give a Rattata's ass what happened!"
pause 0.7
blue angrybrow frownmouth "Ugh, you two have wasted my time enough today. I've got places to go and things to do."
blue happybrow angrymouth "Smell ya later!"

show blue:
    alpha 1.0 xpos 450
    parallel:
        ease 0.65 xpos 1000
    parallel:
        ease 0.5 alpha 0.0

$ renpy.pause(2, hard=True)
    
leaf @talkingmouth "{i}Smell ya?{/i}{w=0.5} What does that even mean?"

hide blue

red "It's Blue... or as I'd like to call him, '[blue_name].'{w=0.5} He's said that for as long as I've known him.{w=0.25} And I've known him for a long time."
red @closedeyes talking2mouth "Not that I'm particularly proud about it."
leaf flirt "So he's been smelling you for a long time?{w=0.5} What a creep."
red @angrybrow frownmouth "No! That's not how it works!"
leaf happy "Ha ha ha!{w=0.5} Let's go, [first_name], we'll be late for our first class!"

window hide

show leaf happy:
    alpha 1.0 xpos 970
    parallel:
        ease 0.5 xpos 1120
    parallel:
        ease 0.5 alpha 0.0
        
$ renpy.pause(1.5, hard=True)

redmind "Leaf, huh?{w=1} And [blue_name].{w=1} And me.{w=0.5} In the same room for the next two hours."

hide leaf

redmind "Every day for the next year."
redmind ".{w=0.25}.{w=0.25}."
redmind "This is going to be quite the year."

window hide

show academyhall:
    subpixel True
    zoom 1.0 xpos 960 ypos 1080
    ease 3.5 zoom 1.5 xpos 850 ypos 1320
$ renpy.pause(1.0, hard=True)

show blank2 with dis:
    alpha 1.0

$ renpy.pause(1.0, hard=True)
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_5
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg:
    xpos 2500

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank2
hide academyhall

show leaf happy uniform:
    alpha 0.0 xpos 430
    ease 0.5 xpos 550 alpha 1.0

show may happy uniform:
    alpha 0.0 xpos 1120
    pause 0.5
    ease 0.5 xpos 1000 alpha 1.0

leaf "May! I can't believe we're in the same homeroom!"

show leaf:
    xpos 550 alpha 1.0

show may:
    xpos 1000 alpha 1.0

red uniform "These coincidences are just piling up today."

may @talkingmouth "Small world!{w=0.5}"
may -happy "[first_name], I see you and Leaf finally got acquainted!"
leaf flirt "May, do you remember the guy I told you about when we first met?"
show may surprised with dis
leaf happy "Turns out you knew him all along."
may sadbrow -surprisedmouth "Oh, [first_name]. Since you ran ahead without us after breakfast, now I can believe how you got lost on the first day."
may happy "That's okay, a strong sense of adventure is a good thing!"
red closedeyes talking2mouth "I'll never be able to live this down, will I?"
show may -happy with dis
leaf blush happybrow talking2mouth "A boy, stranded in the forbidden territory of the terrible cheer squad. Sensing impending doom, he picked his poison and sought refuge in the abyssal bathroom of the fairer sex." 
leaf "It was then a beautiful maiden, a girl he knew nothing about, happened to stumble upon him at the right time, pulling him into the light and guiding him to sanctuary."
show leaf -blush happy with dis
show may happy with dis
red @angrybrow frownmouth "Thank you for the epic summary."

if leafwindowjump == True:
    red @angrybrow frownmouth "And you're the one who {i}forced{/i} me into the bathroom!{w=0.5} I liked my window idea."
else:
    pass

show leaf flirt blush:
    xpos 550 ypos 1080
    ease 0.5 ypos 1120 xpos 530
    pause 1.0
    ease 0.5 ypos 1080 xpos 550

pause 1.0

redmind "A curtsy? She's so unbelievably smug."
show leaf -flirt -blush with dis
show may -happy with dis
red -closedeyes -talkingmouth "Since you're here, May, I'm assuming Brendan's in another class?"
may "Brendan's in Class 1-A next door."
leaf thinking "Oh, in your Dad's."
show leaf surprised with dis
show may surprised with dis
oak "You should tell your father, Miss Birch,{nw}"

show oak:
    xpos 150 alpha 0.0
    ease 1.5 xpos 300 alpha 1.0

show leaf:
    xpos 550
    ease 0.65 xpos 800

show may:
    xpos 1000
    ease 0.75 xpos 1200

extend " that his recent article regarding the pros and cons of invasive Bug Pokémon as biological control has been well-received.{w=0.5} I'm impressed."

show oak:
    xpos 300 alpha 1.0

show leaf:
    xpos 800

show may:
    xpos 1200

red happy "Sam!"
oak "Hello, lad. Great to see you've settled in nicely here."
red "Sam, what's going on? Why am I here? Why are you teaching? Why didn't you tell me that you'd be working at Kobukan? How--"
oak @angrybrow "[first_name]. There's a time and place for everything, but not now."
red thinking "Ugh... I've heard that before."
oak @closedeyes "Also... in front of other students, Professor Oak, if you please."
red surprised "Oh! Uh, yeah, of course. Sorry, Sam-- I mean, Oak! Professor Oak."
show leaf -surprised with dis
oak @happy "Anyway, Miss Birch, on the topic of your father...?"
may sadbrow talkingmouth "Oh! Right. I guess Dad's work in the field's been paying off."
may "For the last couple years, if it's not a swarm of Beedrill chasing him around, it'd be Ariados or the occasional Scyther."
oak "Ah, are you well-versed in Bug-types, May? I assume you've gained a lot of experience while assisting with your father's work."
may happy "Yeah! I didn't like them at first, but I'm planning on taking the Bug-type Elective.{w=0.5} I'd like to go to Unova someday, too. I heard they have really powerful Bug-types there!"
oak "I see.{w=0.5} So what Pokémon types will the three of you be focusing on this year?"
$ KnowClasses("May", ["Bug", "Fire", "Fighting"])
may -happy talkingmouth "Well, there's Bug. But I'm also planning on taking Fire and Fighting!"
$ KnowClasses("Leaf", ["Grass", "Electric", "Dragon"])
leaf "Grass, Electric, and Dragon over here."
oak @happy "Solid choices! Varied and versatile. And you, lad?"
red -surprised "I'm uh, I'm not planning on specializing. I'm just going to take classes that help the Pokémon I can get my hands on."
oak @angrybrow surprisedmouth ".{w=0.5}.{w=0.5}.{w=0.5}"
redmind sad "Oh, crap, did I say the wrong thing?"
oak @happyeyes "Of course you are. Of {i}course{/i} you are."
oak @happy "Lad, you never fail to impress me. You're a Champion, if I've ever seen one."
red @surprised "Uh..."
red "Thanks, Professor Oak. Does that mean it's the right decision?"
oak @angrybrow happymouth "I couldn't possibly tell you that, [first_name]. But it's the one you've made."
red @thinking "Uh... yeah, I guess so."
oak @thinking "Still, I would recommend that, for now, at least, [bluecolor]you focus on at least one type. You may find it hard to train up your Pokemon if you spread yourself too thin!{/color}"
oak "Well, excellent choices all around!{w=0.5} Now, I hope all of you are ready.{w=0.5} The bell will ring soon, so go ahead and find yourselves a seat."

show oak at dissolveaway:
    xpos 300

window hide

hide oak
with dissolve

show may surprised with dis
leaf angry "Okay, what the {i}hell{/i}, 'lad?' You're on a firstname basis with our homeroom teacher?!"
red thinking "Well, normally I call him Old Man Oak, but I don't call him that to his face."
leaf closedbrow talkingmouth "We are {i}not{/i} done talking about this. For now, though.{w=0.5}.{w=0.5}.{w=0.5}" 
leaf -closedbrow -talkingmouth "Let's sit together, May."
leaf flirt blush "Sorry, [first_name], but since you'll be hopping around classes like a Spoink, I bet we'll have plenty of chances to bond later!~"

show leaf happy:
    alpha 1.0 xpos 800
    ease 0.5 xpos 700 alpha 0.0

$ renpy.pause(1.25, hard=True)

show may angrybrow happymouth:
    xpos 1200
    ease 0.65 xpos 880

$ renpy.pause(0.65, hard=True)

may angrybrow talkingmouth"Sooo... what do you think of Leaf, [first_name]?"
    
hide leaf

red sadeyebrows sadeyes -frownmouth "Absolutely charming."
may @happybrow talkingmouth "Hehe, she's a lot of fun to be around!"
may "Come sit by us!"

show may:
    alpha 1.0 xpos 880
    ease 0.5 xpos 780 alpha 0.0

$ renpy.pause(1.0, hard=True)

hide may

red happy "Well, I sure as hell won't be sitting by [blue_name]."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_6
show blank2 with splitfade
$ renpy.pause(0.5, hard=True)
play sound "Audio/BellChime.ogg"
show morning at vspaz  
pause 3.5
show oakbg with dis
hide blank2 with splitfade
$ renpy.music.set_volume(1.0, delay=1.00, channel="music")
$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.0, hard=True)
hide morning

oak "Good morning, and welcome to your first class at Kobukan Academy!"
oak "I'll be your teacher for this homeroom. You can call me Oak, but most people simply call me the Pokémon Professor."
oak "This world is inhabited by creatures we call Pokémon.{w=0.5} People and Pokémon live together by supporting each other..."

window hide
pause 1.5

oak "...I think I could skip this part. You are all smart enough to know what Pokémon are."

"Excited Student" "\"I can't believe we're hearing Professor Oak talk right in front of us. The man's a legend!\""
"Gossiping Student" "\"I know! My dad's a huge fan of his. He's got all his encyclopedias, A to Z!{w=0.5} Oh man, he's gonna flip when I tell him I'm in his class!\""

redmind surprised "Even outside of Kanto everyone knows him."
redmind thinking "I didn't know he was looked up to by so many people.{w=0.5} He's like a superhero to them."
redmind happy "But to me, he's just my neighbor."

oak "Now, something you need to know about this class is that it's extremely important for your final grade."
oak "Last year, everyone who failed to pass this class also failed to graduate."

"Shocked Student" "\"Holy crap!\""
"Gossiping Student" "\"All of a sudden I don't feel like being in this class anymore...\""

redmind thinking "Ugh... so if there's one class I absolutely can't screw up, it's this one."

oak "Yes, this class is challenging, but if you put in the work and keep at your studies, you should pass with flying colors."
oak "My job is not to assign you failing grades.{w=0.5} But my job is not to coddle you either."
oak "My job is to make sure you graduate this school with the knowledge and skills to excel in the Pokémon world."
oak "Which brings me to my next point."
oak "As you all know, Kobukan is a very selective school, and it demands you to give your best at all times, or you will be surpassed by your peers."
oak "{color=#0048ff}The graduation rate for this school is fixed at eighty percent.{/color}{w=0.5} It is not for the weak-willed or unmotivated!"

"Crushed Student" "\"You gotta be kidding me!\""
"Cynical Student" "\"Is this a joke?!{w=0.5} What kind of school life is this?!\""

redmind @sadeyes sadeyebrows -frownmouth "Sounds like some people didn't read the website... but I didn't pick up a brochure, so I guess we all have our blind spots."

show may surprised uniform:
    xpos 0.25 ypos 1.3 alpha 0.0 zoom 1.35
    ease 0.5 alpha 1.0

show leaf surprised uniform:
    xpos 0.75 ypos 1.3 alpha 0.0 zoom 1.35
    ease 0.5 alpha 1.0

pause 1.0

redmind "I guess Ethan wasn't the only person I know who didn't know this."

show leaf:
    alpha 1.0 xpos 0.75 ypos 1.3 zoom 1.35
    ease 0.5 alpha 0.0

show may:
    alpha 1.0 xpos 0.25 ypos 1.3 zoom 1.35
    ease 0.5 alpha 0.0

show blue smilemouth uniform:
    xpos 0.5 alpha 0.0
    ease 0.5 alpha 1.0

pause 1.0

redmind "Of course. Blue isn't phased at all."

hide leaf
hide may

show blue:
    alpha 1.0
    ease 0.5 alpha 0.0

show hilbert uniform:
    xpos 1200 alpha 0.0
    ease 0.5 alpha 1.0

pause 1.0
    
redmind "And I didn't realize at first, but Hilbert's in this class, too.{w=0.5} He already knew, of course. He isn't surprised."

show hilbert:
    alpha 1.0 xpos 1200
    ease 0.5 alpha 0.0

oak "Ahem, yes. I just wanted to clear that up."

hide blue
hide hilbert

oak "Now, are any of you interested in competing in the Pokémon League after you graduate? Just by a show of hands."

redmind "A few dozen hands... Blue, Hilbert, Leaf..."
redmind @surprised "Oh! I should put my hand up, too!" 

oak "Take a good look around."

window hide
pause 1.5

oak "Now, everyone in the two middle sections, put your hands down."

redmind "There are fewer than ten students left with their hands raised.{w=0.5} I think I know where this is going."

oak "That's the percentage of those who will actually {i}qualify{/i} for the Pokémon League. And it is even less for those who can {i}make{/i} it there."
oak "Now, don't let it discourage you. Let's start with some--"

window hide
pause 1.0

redmind "Professor Oak's staring at something.{w=0.5} Or someone."

oak "Yes, did you have a question?"

show blue closedbrow happymouth uniform:
    xpos 900 alpha 0.0
    ease 0.5 alpha 1.0

blue "Hah! I'm just gonna say this right now for all you quitters in this room!"
blue angrybrow talkingmouth "I'm gettin' to the Pokémon League and there's no chance in hell that I'm not!"

redmind "God, why does he always have to be like this?{w=0.5} It hasn't been ten minutes since class started and he's already trying to start something."
redmind "He tries so hard to be cool and fails so hard at it that it's sickening."

blue "I'm not stopping until I wipe the floor with every single regional Pokémon League Champion! You're looking at the next World Champion!"

oak "Please, sit down--"
oak "Erm, what was your name again?"
blue surprised "Wha-? Gramps, it's me!"
oak "Yes, I know it's you! But what was..."
show blue angrymouth with dis
red happy "It's [blue_name]!"
leaf happy uniform "Oh my god, did you actually just say that?! Balls, [first_name]!"
oak "Er, that's right! Anyway, sit down!"
blue angry "Man, what a load of...{w=0.5} can't believe..."

pause 1.0

may uniform sad "[blue_name]'s really glaring at you..."
red happy "Yeah, well, when he gets like this, it's best to just grin and give him a thumbs-up!"
show blue angrybrow talkingmouth with dis
redmind "That just made him madder.{w=0.4} I'm liking this class already."

show blue:
    alpha 1.0 xpos 900
    ease 0.5 alpha 0.0

oak "Right then. I think that's enough talking.{w=0.5} I'll take roll now while you're all in a good mood."

hide blue

oak "May.{w=0.5} Is May here?"

show may happy:
    xpos 250 ypos 1.3 alpha 0.0 zoom 1.35
    ease 0.5 alpha 1.0

may "Present!"

show may:
    alpha 1.0 xpos 250 ypos 1.3 zoom 1.35
    ease 0.5 alpha 0.0

oak "There you are."
oak "Hilbert?"

hide may

show hilbert uniform:
    xpos 1200 alpha 0.0
    ease 0.5 alpha 1.0

hilbert "Here."

show hilbert:
    alpha 1.0 xpos 1200
    ease 0.5 alpha 0.0

oak "Okay.{w=0.25} Now, Whitney?"

window hide
hide hilbert
pause 1.5

oak "Whitney, are you here?"
oak "Hm. Absent on the first d--"

whitney uniform @surprised "{cps=20}{size=26}W{/size}{size=28}W{/size}{size=30}W{/size}{size=32}A{/size}{size=34}A{/size}{size=36}AA{/size}{size=38}AA{/size}{size=40}AI{size=42}I{/size}{size=38}I{/size}{size=46}I{/size}{size=48}I{/size}{size=50}T{/size}{size=52}T!!{/size}{/cps}"

window hide
play sound "Audio/ExitBuilding.wav"

show whitney surprisedbrow sadmouth uniform:
    xpos 2000 ypos 1.1 alpha 0.0 rotate 10
    ease 0.4 xpos 500 alpha 1.0
    ease 0.5 xpos 300
    pause 0.5
    ease 0.5 xpos 500 ypos 1.2 rotate 0
    
$ renpy.pause(2.0, hard=True)

redmind -happy "Huh? Who's that redhead who just came rolling in? I guess that's Whitney?"
$ BecomeNamed("Whitney")
show whitney happy with dis
redmind thinking "And now she's posing like she just finished an acrobatic stunt at the Pokéathlon."
whitney "Here I am!{w=0.5} I'm not late, I was just waiting for the perfect time to make my grand entrance!"

show whitney:
    xpos 500 zoom 1.0
    ease 0.4 xpos 340 ypos 1.2 zoom 1.3
    pause 0.3
    ease 0.15 ypos 1.3

redmind "She calmly sits down in the empty chair in front from me like nothing happened."
redmind "I have to say, I'm impressed with her ability to keep a straight face after that performance."

show whitney:
    xpos 340 ypos 1.3 zoom 1.3
    
whitney @talkingmouth "Please continue."
oak "All right, I'll mark you on-time.{w=0.5} But no more of that, do you understand?"
whitney @smilemouth "Yessir! You can count on me!"

show whitney:
    alpha 1.0 xpos 340 ypos 1.3
    ease 0.5 alpha 0.0

oak "Very good.{w=0.5} Now, Flannery?"

hide whitney

$ BecomeNamed("Flannery")
flannery tired uniform "{cps=22}I'm.{w=0.25}.{w=0.25}.{w=0.5} here...!{/cps}"

show flannery -tired tiredbrow frownmouth uniform:
    alpha 0.0 xpos 0 ypos 1.9 zoom 1.2
    parallel:
        ease 0.75 alpha 1.0
    parallel:
        ease 0.75 xpos 200 ypos 1.3 zoom 1.1
        ease 1.25 xpos 500 ypos 1.1 zoom 1.0
        
$ renpy.pause(2.0, hard=True)

flannery @talkingmouth "Sorry... I'm not a big fan of mornings..."
oak "Fan or not, try and get to class on time from now on."
oak "I'll mark you on-time, too."
flannery @talkingmouth "Yeah... okay."

show flannery tired:
    xpos 500 ypos 1.1 zoom 1.0
    ease 1.5 xpos 1200 ypos 1.1 zoom 1.35
    pause 0.5
    ease 0.4 ypos 1.2
    
$ renpy.pause(2.5, hard=True)

redmind "She's... kinda intimidating. Reminds me of one of those biker gang chicks that hang out West of Celadon City."

pause 1.0

show flannery:
    xpos 1200 ypos 1.2 alpha 1.0
    ease 0.5 alpha 0.0

redmind "Anyway, now that she's sitting next to me, I've got May to my left, Flannery to my right, Whitney in front of me, and behind me is..."

show dawn uniform with dis:
    alpha 1.0

pause 1.0

redmind "Another cute girl."
redmind @sad "Is this some kind of social experiment? Invite a ridiculously unqualified student to Kobukan, but surround them by attractive women, so they can't focus at all?"

show dawn:
    alpha 1.0
    ease 0.5 alpha 0.0

redmind @happy "Well, it's a good thing whoever was setting this up didn't know I find guys hot, too."

pause 1.0

show flannery tired uniform:
    xpos 1200 ypos 1.2 alpha 0.0
    ease 0.5 alpha 1.0

pause 1.0

redmind -thinking "...Oh, right, Flannery just sat down. Looks like she's staring at me--does she expect me to say anything? Or maybe her eyes are just glassy from tiredness?"

menu:
    "Rough morning, huh?":
        red sadeyes sadeyebrows talking2mouth "Rough morning, huh?"
        
        flannery angrybrow frownmouth "Who wants to know?"

        red surprisedeyes surprisedeyebrows "Uh, I just thought that, you know, you kind of looked tired?"
        red -surprisedeyebrows closedeyes "Not anymore, though."

        show flannery angrymouth:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery "How about you mind your own business?{w=0.5} I don't remember asking for your opinion on anything."

    "Want some coffee?":        
        red "Want some coffee?{w=0.5}" 
        red "I picked some up earlier this morning."
        flannery angrybrow frownmouth "Are you talking to {i}me?{/i}"
        red surprisedeyes surprisedeyebrows talking2mouth "...I'm sensing I said something wrong?"
        flannery angrymouth "Do I look like a charity case to you?"
        $ ValueChange("Flannery", -1, 0.66)

        red "No! You look really tired so I thought--"
        flannery furiousbrow "You thought what?{w=0.5} That you think I'd want your handouts?"
        
        show flannery:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery furiousmouth  veins "Why don't you take that coffee of yours, and shove it up your--"

    ">Say nothing.":        
        redmind "On second thought, maybe I shouldn't. With that glare... discretion is the better part of valor, and all that."
        redmind "Unrelatedly... doesn't her hair break some kind of school code?{w=0.5} It's gotta be at least a couple of feet across."
        show flannery angrybrow frownmouth with dis
        redmind "How does she get it to stay up like that anyway?{w=0.5} I can't imagine the amount of hairspray she uses."
        flannery angrymouth "You got a problem, pal?"
        red "Wha?"
        flannery furiousbrow "What the hell are you staring at me for?"
        red surprisedeyes surprisedeyebrows talking2mouth "Uh, nothing in particular. Just, wondering how you got your hair like.{w=0.25}.{w=0.25}.{w=0.5} that."
        flannery furiousmouth "Like {i}what?{/i} "
        red "You know...{w=0.5} like..."

        show flannery:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery veins "You making fun of my hair?! I'll mess you up!"

hide whitney

show whitney happy uniform:
    alpha 0.0 xpos 685 ypos 1.2 zoom 1.25
    ease 0.5 alpha 1.0

whitney "Chill out, Flan!{w=0.5} I'm sure he didn't mean anything by it."

red closedeyes talking2mouth -surprisedeyebrows "Yes, thank you!"
whitney -happy "It's the first day."
whitney @sadbrow "You should keep it a little on the DL, girl."

show flannery:
    xpos 1140 ypos 1.2
    ease 0.6 xpos 1200
    
flannery -veins angrybrow frownmouth "Psh."

show flannery:
    alpha 1.0 xpos 1200 ypos 1.2
    ease 0.5 alpha 0.0

pause 1.0

show red:
    xpos -1.0

whitney @talkingmouth "You'll have to ease up on Flannery.{w=0.5} She's a little rough around the edges in the morning."
hide red
red uniform "I understand. Morning isn't exactly my favorite time of day either."
whitney angrybrow happymouth "Heh, we were almost late 'cause Flan slept through all of her alarm clocks!"

show flannery thinking:
    alpha 0.0 xpos 1200 ypos 1.2
    ease 0.5 alpha 1.0

flannery "They don't work, Whitney. I don't know how many times I have to tell you."

pause 1.5

show flannery surprised with dis
whitney happy "I think it's because your snore is louder than the clocks."
flannery furious veins "I do NOT snore!"
flannery angrybrow -veins furiousmouth "Hey, what're you smirkin' at?{w=0.5} I don't snore, you hear me?!"
red "I believe you.{w=0.5} So you're Whitney, and you're Flannery."
red "I'm [first_name]."
whitney -happy "Nice to meet ya, [first_name]!"

if persondex["Flannery"]["Value"] != -1:
    flannery thinking "Yeah. Sorry about... getting on your case earlier."

    red "Don't worry about it."

show flannery surprised with dis
show whitney surprised with dis
oak "Keep it down back there!"

show flannery:
    alpha 1.0 xpos 1200 ypos 1.2
    ease 0.5 alpha 0.0

show whitney:
    alpha 1.0 xpos 685 ypos 1.2 
    pause 0.25
    ease 0.5 alpha 0.0

stop music fadeout 1.5

redmind angrybrow frownmouth "Alright, really gotta buckle down and focus, now..."
show red:
    xpos -1.0

$ renpy.music.queue("Audio/Music/ViridianCity_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianCity_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(0.75, hard=True)

hide whitney
hide flannery

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis:
    alpha 1.0

play sound "Audio/BellChime.ogg"
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_7

pause 2.0

narrator "The rest of your class passes without incident."
narrator "It's now time to pick the elective you're going to go to."

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

narrator "[bluecolor]It's important to remember two things. Taking an elective class raises your proficiency, and your proficiency in a type is equal to the highest level a Pokémon you own can level up to.{/color}"

narrator "[bluecolor]Pokémon already above that level cap will not be de-leveled, but they also cannot level up.{/color}"

narrator "[bluecolor]For that reason, it is advisable to focus on at least one type, for a while. It will be, however, a while longer before your Pokémon begin gaining experience from battles.{/color}"

jump PickElective