label secondhomeroom010406:

$ timeOfDay = "Evening"

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

narrator "Unfortunately, you are delayed on your way to class by more people who saw your battle with [blue_name], and you only manage to slide in right before the bell rings, leaving no time for discussion."

scene blank2

show homeroom behind blank2
    
show oakbg at dissolvein behind blank2

hide blank2 with dis

$ renpy.transition(dissolve)
show screen currentdate

play sound "Audio/BellChime.ogg"
$ renpy.pause(1.5, hard=True)

hide blank2

oak "Good work today, class.{w=0.5} You're all dismissed, but remember to do the assigned readings!"

show oakbg:
    alpha 1.0
    ease 0.5 alpha 0.0

redmind uniform @sad "Okay. Sam literally looked right at me and bolted out of the classroom. What's the issue? Did I do something wrong?"

show leaf happy uniform:
    alpha 0.0 xpos 100
    ease 0.5 alpha 1.0 xpos 700

leaf @talking2mouth "Hey, [first_name]!{w=0.33} You doing anything after class?"

hide oakbg

red "No, not really.{w=0.5} I'm guessing you want to go somewhere again?"

leaf @happybrow talking2mouth "Hehe, was I that obvious?"

leaf @flirt "You know I'm not third-wheeling with May and Brendan, so it's up to you to entertain me this afternoon!"

red @happy "Ignoring the fact that you're basically saying I'm your backup plan, I'll do my best."

show leaf -happy with dis
red @thinking "So where did you want to go?{w=0.5} The gym again? You might see Rosa."

leaf @thinking "Hmm, why don't you decide?{w=0.5} It's only fair since I chose last time."

red "All right, let's go down the map then...{w=0.5} Oh yeah, the Recreation Center isn't that far from here.{w=0.3}{nw}"
show leaf surprised with dis
extend " Doesn't that place have a swimming pool?"

leaf -surprised @talkingmouth "Uh, I guess so."

red "I wouldn't mind checking that out.{w=0.5} Swimming's pretty fun, so I might drop by some time."

show leaf happybrow happymouth blush with dis:
    xpos 700
    ease 0.5 xpos 500

leaf "...Oops! I just remembered I have to be somewhere right now!{w=0.5} Sorry, but I can't today."

show leaf fullblush with dis:
    xpos 500
    ease 1.0 xpos 200

leaf "It's super important, so I'm gonna have to bounce. Sorry!"

red "Um, that's okay.{w=0.5} You don't have to apologize if it can't be helped."

leaf "Maybe next time!{w=0.5}{nw}"


show leaf:
    xpos 200 alpha 1.0
    ease 0.5 xpos -100 alpha 0.0
    
extend " See you later!"

hide leaf

redmind @confusedeyebrows "What's with her all of a sudden?{w=0.5} I've never seen her so flustered before."
redmind @"I guess she {b}really{/b} doesn't like pools? I'm more of a billiards guy myself, but..."

redmind @happy "Oh well. Might as well check out the pool myself."

show hilda uniform:
    alpha 0.0 xpos 100
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos 500

pause 1.0

red "Hilda? What are you doing here?"

show hilda:
    alpha 1.0 xpos 500
    ease 0.7 xpos 750
    
hilda @talkingmouth "What else?{w=0.5} Hilbert-wrangling."
hilda @angrybrow talkingmouth "This {i}is{/i} his classroom, right?"

red @thinking "Yeah, but he's hiding under the desk over there."

show hilbert angry uniform:
    alpha 0.0 xpos 1700 zoom 0.5
    ease 1.25 alpha 1.0 xpos 1300 zoom 1.0

hilbert "You {i}bastard.{/i}"

$ renpy.pause(1.25, hard=True)
         
hilda "There you are.{w=0.5}{nw}"

show hilda angry with dis:
    xpos 750
    ease 0.5 xpos 800
    
extend " Were you planning on skipping out on our training regimen again?"

pause 2.0

hilbert sad "I was...{w=0.5} planning on it, yes."

show hilda:
    xpos 800
    ease 0.5 xpos 850
    
hilda -angry "Well, now you're not.{w=0.5} You know what happens when you go too long without exercise!"

red "What's this about a regimen?"

show hilda:
    xpos 850
    ease 0.75 xpos 750

hilda sad "Ugh. Where to begin."
hilda closedbrow "Hilbert's got this... 'dream' that he obsesses over. And because he's so obsessed, he forgets to eat, or sleep, or drink..."
hilda angry "Or exercise. Which is why Hilbert will fall asleep in the middle of a conversation he's bored of. Because he's got the stamina of a Cleffa."

hilbert "{size=30}Or maybe I just fall asleep in the middle of boring conversations because they're boring?{/size}"

red "You're a good friend."

hilda sad "No, but I am a good mother, for whatever that's worth."

menu:
    "You're a hot mom.":
        show hilda surprised
        show hilbert surprised
        with dis

        red "You're a hot mom."

        pause 1.5

        $ ValueChange("Hilda", 1, 750.0/1920.0)

        hilda happy "Damn, playboy. You say that to all the teenage single moms out there?"

        red "Funnily enough, you're the only one I've met."

    "...":
        pass

    "Seems like you're being a bit hard on Hilbert.":
        show hilda surprised
        show hilbert surprised
        with dis

        $ ValueChange("Hilda", -2, 750.0/1920.0)
        hilda "I... literally can't even begin to describe how goddamn wrong you are about that."

        $ ValueChange("Hilbert", 1, 1300.0/1920.0)

hilbert sad "Ugh."

show hilbert:
    xpos 1300 alpha 1.0
    ease 0.5 alpha 0.0

hilda angry "Hey! You better be heading to the goddamn recreation center, Hilbert!"

hilbert "I am! Get off my case!"

show hilda -angry with dis

pause 1.0

red "So, you're going to the Recreation Center, too?{w=0.5} I was planning on checking the place out."

hilda "Then let's go together. Ready?"

red "Ready as I'll ever be!"

show hilda:
    xpos 750 alpha 1.0
    ease 1.0 xpos 100 alpha 0.0
    
$ renpy.pause(0.5, hard=True)
    
stop music fadeout 1.5
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_19

window hide

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)

play music "Audio/Music/Beyond2.ogg" loop fadein 1.0
show map behind blank2

hide homeroom
hide hilbert

$ renpy.transition(dissolve)
show screen currentdate

hide hilda
hide blank2 with splitfade
pause 0.5

hilda uniform happy "Hilbert and I will be over by the courts.{w=0.5} Would you like to join us?"

red "Nah, I was planning on checking out the pools.{w=0.5} Thanks for the offer, though."

hilda -happy "All right, have fun.{w=0.5} We'll be done in about two hours, but if you're finished before us, you can take off."

red "Okay, sounds good.{w=0.5} See you later!"

hide hilda

stop music fadeout 1.0
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_20

show blank2 with splitfadefast
$ renpy.pause(1.0, hard=True)
hide map

play music "Audio/Music/Ocean Waltz_Start.ogg" noloop
queue music "Audio/Music/Ocean Waltz_Loop.ogg"

show pool behind blank2

$ renpy.transition(dissolve)
show screen currentdate
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

redmind "This pool's enormous! Reminds me of the one in the gym at Cerulean City."
redmind "With a pool this fancy, I figured there'd be students all over the place, but there's nobody in here.{w=0.5} Though, I'm sure when clubs start, the swim team's gonna take over."

show misty with dis:
    xpos 800
    ease 0.75 xpos 700

redmind "Wait, I see Misty kneeling over by the side of the pool.{w=0.5} It looks like she's inspecting the water with her hand."

red "Hey. Checking the water temperature?"

misty surprised "WAH!"
            
show misty angry with dis:
    xpos 700
    ease 0.5 xpos 620

misty @talkingmouth "You again!"
misty "Are you trying to kill me?!{w=0.5} Don't scare me like that!"

red @talkingmouth "Uh... I just asked a question? It's not like I was sneaking up on you."

misty angry ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend sadbrow "I might have overreacted."

misty -sadbrow @thinking "Er, sorry for...{w=0.5} snapping at you like that."

red @talkingmouth "No worries.{w=0.5} Let's start over."
red @talking2mouth "So what were you doing just now?{w=0.5} I'm guessing you weren't about to take a dip, in that expensive Cerulean outfit."

misty @thinking "Yeah, no. I was checking if the pool's Pokémon-safe.{w=0.5} That's how you can tell if it's a good pool or not."

red @talking2mouth "Oh, yeah? What makes a pool safe for Pokémon?"

misty @talking2mouth "Basically, no harsh chemicals or cleaners. A lot of Pokémon keep their eyes open underwater, and some absorb water through their skin."
misty @happy "They don't want strong acids or bases getting into their body. It's not enough to kill 'em, but a Wooper could fall seriously sick from that."
misty @thinking "Well, Johtonian Wooper could. Paldean Wooper could probably filter them. Different gill structures."

red @talking2mouth "You seem pretty knowledgeable. You have a lot of experience with water types?"

misty @angrybrow talkingmouth "Doesn't everyone? They're {i}everywhere.{/i}{w=0.5} They're the most common type."

red @happy "That's a deflection."

pause 1.0

misty surprised "Uh, no it's--"

brock "{size=40}{i}-choo!{/i}{/size}"

show pool_corner

pause 1.0

show tinybrock behind pool_corner:
    subpixel True
    xpos 150 ypos 620
    ease 1.0 xpos 110 ypos 600

$ renpy.pause(1.5, hard=True)

misty angrybrow @talkingmouth "Who's--"

brock "Uhhhh.{w=0.25}.{w=0.25}."

misty "What are you doing hiding behind that wall?{w=0.5}{nw}"

extend angry " Were you eavesdropping on us?"

show tinybrock:
    subpixel True
    xpos 110 ypos 600
    ease 0.5 xpos 105 ypos 570

brock "Nngh! W-wait!{w=0.33} It's not what it looks like..."

misty @talkingmouth "Well, what does it look like?{w=0.5} 'Cause to me,{nw}"
extend " it looks like you were waiting for.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend @surprised sweat " for.{w=0.25}.{w=0.25}."

pause 1.5

show misty:
    xpos 620
    ease 0.25 xpos 800

misty angry "...Were you spying on me?!{w=0.5} You thought I was gonna hop in the pool or something?!"

show misty surprised with dis:
    xpos 800

brock "Uhhhhh.{w=0.25}.{w=0.25}."

pause 1.5

brock "Heh."

show tinybrock:
    subpixel True
    xpos 105 ypos 570
    ease 0.2 xpos -100 ypos 575

misty surprisedbrow angrymouth "HEY! Get back here!"

show misty:
    xpos 800 alpha 1.0
    parallel:
        ease 0.4 alpha 0.0
    parallel:
        ease 0.4 xpos -150

red @surprised "Wait!"
redmind "Too late.{w=0.5} Damn, she runs fast."
redmind @thinking "I think that's enough of inspecting the pool for one day.{w=0.5} I'll come back when things aren't so weird."

window hide

show blank2 with dis:
    alpha 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_21

stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

show night at vspaz

hide misty
hide tinybrock
hide pool_corner
hide pool

pause 3.5

############################################################################################################################################################################################################################
#### END OF DAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate


play sound "Audio/Door_Open1.mp3"
scene dorm_B norm with Dissolve(2.0)

hide blank2
hide night

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika pika!"

red uniform "Hey! I'm back."

show brendan at leftside with dis

brendan "Hey, dude! Welcome back."

show calem at rightside with dis

calem "Welcome back."
    
calem @thinking "[pika_name] was waiting by the door for you again.{w=0.5} I've never seen a Pokémon so eager to welcome back its owner before."

red "What can I say?{w=0.5} I guess we're just really good friends, right, buddy?"
    
pikachu happy_3 "Pikachu~!"
    
calem @surprised "..."

calem @talkingmouth "Just curious, [first_name], but do you always talk to [pika_name] like that?"

red "Like what?"

brendan @talkingmouth "It's, like, uh, you figure he understands what you're saying."

calem @thinking "I've noticed it before, with [starter_name], too, but it seems to me that... you actually understand each other?"
    
red "Well... yeah. I mean, I don't get everything, but there's tone of voice, body language, facial expressions."

show calem surprised with dis
show brendan surprised with dis

pause 1.0

calem -surprised @talkingmouth "You get those from [starter_name], too?"

brendan -surprised @thinking "Dude, you're something else..."
    
red @sadeyes confusedeyebrows "Is it really that weird?{w=0.5} I haven't met many Pokémon Trainers before, so I've always assumed they were like me and [pika_name]."
red @happy "Maybe it's because [pika_name] and I have been together since I was a kid?"

calem @talkingmouth "No, I don't think that's it.{w=0.5} That wouldn't explain [starter_name], who you just got, and my Pokémon and I have a history, too."

red @talking2mouth "You have a Pokémon from home, too?"

calem @talkingmouth "Yes, my Flabébé.{w=0.5} She was a gift from my parents after one of their overseas events when I was in grade school."
calem @happy "Though she's not much for companionship, she refuses to listen to anyone but me.{w=0.5} The days are a little less monotonous with her around."

brendan @talkingmouth "Yeah, and I've had my Shroomish since I was a little kid.{w=0.5} May and I caught him together right in Petalburg Woods when we were visiting my dad."

brendan @happy "Ha ha, we had no idea what a Shroomish was, but we just had to have our own Pokémon.{w=0.5} It took us days to decide who got to keep him!"

red "Huh. It's cool that you two have stories like that. One day, my neighbor invited me over, and just handed me [pika_name].{w=0.5} I don't really have a story like you guys. Actually, I can barely remember that day."
    
brendan @angrybrow happymouth "C'mon, you can't think that!{w=0.5} Everybody's got a story to tell. How I got my Pokémon shouldn't affect anyone else."

calem @talkingmouth "Yes, that's nonsense. No two human-Pokémon pairs are the same.{w=0.5} Our bonds are special, and that's what makes our relationship with Pokémon something to be treasured."
    
calem @thinking "How two vastly different creatures can understand and trust each other so implicitly...{w=0.5} it's truly a marvel of the world. Excuse my poetic turn of phrase."

play sound "Audio/vibrate.ogg"
pause 1.5

calem @talkingmouth "Oh, that's me. It's getting late, so I'll be heading to bed.{w=0.5} Don't stay up too late, Brendan, [first_name].{nw}"
    
extend happy " They say staying up late is bad for your skin."

brendan "Yeah. Gotta get up early for my morning run.{w=0.5} Night, you two!"
    
hide brendan at leftside with dis
    
hide calem at rightside     with dis

red "All right, good night, guys."
red "You guys should sleep, too.{w=0.5} I'll head to bed soon."

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu neutral_2 "Pika!"

$ renpy.music.play(startercry, channel="altcry", loop=None)

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
$ starter_fragment = starter_species_name[:3]
starter "[starter_fragment]!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_22

show blank2 with dis:
    alpha 1.0

redmind "But before that, I need to review my classwork!{w=0.5} I still don't know how I'm going to pay for this... so I think my best bet right now is to just do my work as well as I can!"
redmind "I'm sure there's some scholarship money in it for a top student... or at least I hope there is."

stop music fadeout 1.0
$ renpy.pause(0.5, hard=True)

jump day010407