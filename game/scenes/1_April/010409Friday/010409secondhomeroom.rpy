label secondhomeroom010409:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak "...and with the end of the second Industrial Revolution, new technologies were made widely available to the public, including the fossil restoration machines."
oak "Now, who can tell me which fossil was restored first?"

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak "It appears you've been.{w=0.25}.{w=0.25}.{w=0.5} saved by the bell!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

oak "Okay, students. Make sure to look over the readings online tonight.{w=0.5} I'll be posting some supplementary readings for those of you who were confused today."

redmind uniform @thinking "Based on the groaning I heard during the lecture, I think that was almost all of us."

call clearscreens from _call_clearscreens_40

show blank2 with dis

pause 1.0
hide blank2 with dis

show screen currentdate with dis

show oakbg:
    alpha 1.0
    ease 0.5 alpha 0.0

show leaf uniform embarrassed:
    alpha 0.0 xpos (400+240)/1920
    pause 0.25
    ease 0.5 xpos (550+240)/1920 alpha 1.0
    
show may uniform closedbrow sadmouth:
    alpha 0.0 xpos (750+240)/1920
    ease 0.5 xpos (900+240)/1920 alpha 1.0

may "Thank goodness.{w=0.5} After that lecture, I'm feeling kinda like a fossil myself!"

leaf -embarrassed @thinking "Yeah, I dunno how that stuff's relevant to students like us.{w=0.5} Besides, I already know all that junk about fossils."

red @closedeyes talkingmouth "Huh? You know about fossils, but you're not excited?"

if (starter_species_name in ["Tyrunt", "Archen"]):
    $ startergenderpronoun = "He's" 
    if (playerparty[0].GetGender() == Genders.Female):
        $ startergenderpronoun = "She's"
    red @thinking "I mean, just look at [starter_name]! [startergenderpronoun] a living fossil, which is pretty exciting to me."

leaf @thinking "Sure, making them alive again is cool, but getting them? Ew. [first_name], can you really see me digging around in some dusty old cave for some dumb rocks?"

show leaf surprised with dis

may @sad "Ahh~! Can we save this talk about fossils for another time? I've heard enough about it for one day."

show leaf -surprised with dis

red @happy "Right, sorry!"

red @talkingmouth "So, what're your plans now, May?{w=0.5} Heading out with Brendan?"

show leaf surprised with dis

may sadbrow happymouth "Umm, yeah. But, uh, I think that guy over there looks like he wants to have a word with you."

show may:
    alpha 1.0 xpos (900+240)/1920
    ease 0.5 alpha 0.0
show leaf:
    alpha 1.0 xpos (550+240)/1920
    ease 0.5 alpha 0.0
    
show blue uniform cocky behind may:
    alpha 0.0 xpos (720+240)/1920
    ease 0.5 alpha 1.0
    
pause 2.0

redmind "What is it now?"

show may -sadbrow -happymouth with dis:
    alpha 0.0 xpos (750+240)/1920
    ease 0.5 alpha 1.0  
show leaf -surprised with dis:
    alpha 0.0 xpos (400+240)/1920
    ease 0.5 alpha 1.0

show blue cocky:
    alpha 1.0 xpos (720+240)/1920
    ease 0.5 alpha 0.0
    
leaf @talking2mouth "Oh yeah, now that you mention it, [blue_name]'s been staring at you for a good while now."
leaf @sarcastic "I thought he was just checking out your ass, but I'm pretty sure that's not the case anymore."

may @sadbrow happymouth "Does he want something from you, or...?"

red @closedeyes talkingmouth "I don't know and I'm not interested in finding out."

leaf @happy "If you say so."

show blue cocky:
    alpha 0.0 xpos (2000+240)/1920
    pause 0.5
    ease 0.75 alpha 1.0 xpos (1450+240)/1920

red "Anyway, about today, I was thinking about visiting--"
    
blue @talkingmouth "Yo, loser!"

show blue angry with dis

red "--the academy's library since I still didn't get a chance to see if there's--"

show blue angry:
    xpos (1450+240)/1920
    ease 0.5 xpos (1400+240)/1920
    
blue @talkingmouth "Hey! I'm talking to you!"
    
red angrybrow frownmouth @talking2mouth "Oh. My mistake."

show may angry with dis

show blue angry:
    xpos (1400+240)/1920

blue "Wow, dumb {i}and{/i} deaf?{w=0.5} Just how clueless are you--"

leaf angrybrow frownmouth @angrymouth "Buddy, you've been on [first_name]'s case since day one. Give it a rest already!"

may angrybrow frownmouth @angrymouth "Yeah, what's with you?{w=0.5} He's done nothing to you!"

blue "Ugh, you two again."

blue cocky @talkingmouth "So you like hiding behind girls all day, [first_name]?{w=0.5} Can't even fight your own battles, huh?"

leaf @angrymouth "What was that?"

red @confusedeyebrows talking2mouth "For real, what do you want this time, [blue_name]?{w=0.5} Is this another one of your pointless challenges...?"

blue @talkingmouth "There's nothing pointless about this one! This time it's for {i}real!{/i} "

if WonBattle("Blue1"):
    show blue angry with dis

    red @thinking "What exactly makes this one different from last time?"

    show blue:
        xpos (1400+240)/1920
        ease 0.33 xpos (1350+240)/1920
        
    blue "This time I'm not gonna pull any punches.{w=0.5} I'll make you admit it was all luck on Tuesday!"

else:
    show blue cocky with dis
    
    red "What exactly makes this one different from the last time?"

    show blue cocky:
        xpos (1400+240)/1920
        ease 0.33 xpos (1350+240)/1920
        
    blue "This time I'm gonna make you realize that you'll always lose against me, especially in Pokémon battling!"

redmind "He really has a one-track mind when it comes to stuff like this."

show leaf:
    xpos (400+240)/1920
    pause 0.5
    ease 0.75 xpos (0+240)/1920

show may:
    xpos (750+240)/1920
    pause 0.33
    ease 0.75 xpos (300+240)/1920
    
show blue:
    xpos (1350+240)/1920
    pause 0.25
    ease 1.0 xpos (700+240)/1920
    
show flannery uniform:
    alpha 0.0 xpos (2000+240)/1920
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos (1200+240)/1920

show whitney uniform:
    alpha 0.0 xpos (2000+240)/1920
    pause 0.33
    ease 0.5 alpha 1.0 xpos (1500+240)/1920
    
flannery @talkingmouth "What's going on here, buddies?{w=0.5} You guys having a shouting contest?"

whitney @talkingmouth "If they were, [first_name]'d be losing real hard."
    
redmind @thinking "I really wish [blue_name]'s voice didn't carry so far.{w=0.5} We've already stirred up a small crowd..."

red @talking2mouth "C'mon, [blue_name], do we really have to do this {i}right now?{/i}{w=0.5} Look, can't we do this later, like--"

blue @talkingmouth "Ha! Not on your life."

show may -angry with dis:
    xpos (300+240)/1920 ypos 1080 zoom 1.0
    ease 0.75 xpos (375+240)/1920 ypos 1330 zoom 1.35

show leaf -angry with dis:
    xpos (0+240)/1920 ypos 1080 zoom 1.0
    pause 0.25
    ease 0.75 xpos (50+240)/1920 ypos 1330 zoom 1.35
    
$ renpy.pause(1.25, hard=True)

show blue:
    xpos (700+240)/1920

show blue angry with dis
    
may @sadbrow happymouth "It doesn't look like he's gonna take no for an answer."

red @thinking ".{w=0.25}.{w=0.25}."
red @closedeyes talking2mouth "Ugh, all right, [blue_name]. Have it your way."
red @angrybrow talking2mouth "But if I win, you stop all this crap.{w=0.5} Enough picking fights, no more badmouthing, all of it.{w=0.5} It's getting really old."

blue cocky "I have no idea what you're on about.{w=0.5}{nw}"
extend cocky @talkingmouth " Whatever, fine! Like that's gonna ever happen."

show whitney surprised with dis

blue @talkingmouth "But if I win, you admit that you'll always be a second-rate Trainer compared to me!"

leaf @sarcastic "Does this guy have an inferiority complex or just hate your guts?"

red @closedeyes talkingmouth "I...{w=0.5} really don't know."

blue angrybrow talkingmouth "If you're done whispering, hurry up and let's get this started!{w=0.5} I don't have all day!"

redmind "Yeah, alright... even though you're the one that wanted to do all this."

stop music fadeout 0.5

blue cocky @talkingmouth "Let's go!"
pause 0.1

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_41

show blank with dis:
    alpha 1.0

# FAKE BATTLE
window hide

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/KantoTrainerLoop_Rock.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["red"], ["blue"], uniforms=[True, True]) from _call_CreateSplash_1

stop music fadeout 0.25

hide blank2

show blank:
    alpha 1.0
    ease 0.5 alpha 0.0
    
show may uniform surprised:
    xpos (300+240)/1920 alpha 0.0 ypos 1330 zoom 1.35
    pause 0.2
    ease 0.5 alpha 1.0 xpos (300+240)/1920 

show leaf uniform surprised:
    xpos (0+240)/1920 alpha 0.0 ypos 1330 zoom 1.35 
    ease 0.5 alpha 1.0 xpos (-50+240)/1920

show flannery surprised:
    xpos (1200+240)/1920 alpha 0.0
    pause 0.2
    ease 0.5 alpha 1.0 xpos (1250+240)/1920

show whitney surprised:
    xpos (1500+240)/1920 alpha 0.0
    ease 0.5 alpha 1.0 xpos (1550+240)/1920
    
show blue uniform surprised:
    xpos (700+240)/1920 alpha 0.0
    pause 0.25
    ease 0.5 alpha 1.0 xpos (760+240)/1920

show screen currentdate

red uniform @confusedeyebrows talking2mouth "Wait, what? No."

blue angry "What?! What's the issue?!"

red "We're in a {i}non-combat{/i} zone. Battling here would be breaking the rules."

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.stop(channel='crowd', fadeout=0.25)

blue "God, you're such a pussy!"

red @thinking "Call me whatever you want. I'm not breaking school rules before my first week is over just to satisfy your ego."

blue @angry "Fine! We're doing this at the Battle Hall, then! Let's go already!"

hide whitney
hide flannery
with dis

show blue:
    alpha 1.0 xpos (900+240)/1920
    parallel:
        pause 0.5
        ease 0.5 alpha 0.0
    parallel:
        ease 1.0 xpos (1400+240)/1920
        
show leaf -surprised with dis:
    xpos (-50+240)/1920 ypos 1330 zoom 1.35 
    pause 0.6
    ease 1.25 xpos (500+240)/1920
    
show may -surprised with dis:
    xpos (300+240)/1920 ypos 1330 zoom 1.35 
    pause 0.4
    ease 1.75 xpos (950+240)/1920

$ renpy.pause(2.5, hard=True)

hide blue
    
leaf @talking2mouth "You're really going through with this?"

red @happy "I said I would, didn't I?"
red @talkingmouth "Besides, what he said was kinda true.{w=0.5} Tuesday was just a practice match. This one's personal."

leaf @flirt "So you're gonna whoop him so bad, that he's gonna stop messing with you?"

red @happy "That's the plan."

leaf @happy "Hehe! Sounds like an interesting time.{w=0.5} Can't wait!"
    
show hilbert uniform behind leaf:
    alpha 0.0 xpos (0+240)/1920
    ease 0.75 xpos (100+240)/1920 alpha 1.0

hilbert @talkingmouth "For a second, I didn't think you were going to accept his challenge."

red ".{w=0.25}.{w=0.25}.{w=0.25}"
red @talkingmouth "I can't tell from your expression if you think accepting his challenge was a good thing or not."

hilbert @sad "Obviously it was good. You don't get stronger unless you accept challenges."

red @closedeyes talking2mouth "Right. Well, I'm off to go kick his ass, then."

hilbert @talkingmouth "...Make sure you're prepared. I've been watching his battles. He still can't control his Pokémon like you can, but he's trained them hard, and quickly, too."

red @happy "Aw, thanks, Hilbert! Does that mean we're friends?"

hilbert @angry "You are slightly less obnoxious than him; hence my support. Push it, and I can flip sides {i}very{/i} easily."

red @angrybrow frownmouth ".{w=0.25}.{w=0.25}.{w=0.25}"
red @angrybrow talking2mouth "Thanks."

show hilbert:
    xpos (100+240)/1920 alpha 1.0
    ease 0.5 xpos (0+240)/1920 alpha 0.0

red @talkingmouth "Sorry, guys, need to drop back at the dorm first."

leaf @surprised "Huh? What for?"

red @talking2mouth "Hilbert just gave me a clue. He referred to Blue's Pokémon as 'them.' That means Blue brought another, probably one from home, and is planning to outnumber me."

may frownmouth sadbrow "Oh no... then, how can you win?"

red @thinking "It'll be tricky, that's for sure. But I think we can fight fire with fire here. I have a plan."

red @happy "If I could have your ears for a minute..."

call clearscreens from _call_clearscreens_42
show blank2 with splitfade

show stadium_empty behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg"

python:
    renpy.transition(dissolve)
    leafbulbasaurobj = Pokemon(1, level=13, gender=Genders.Male, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Tackle"), GetMove("Growl"), GetMove("Vine Whip"), GetMove("Sweet Scent")], nature=Natures.Modest, ability="Chlorophyll")#Leaf's Bulbasaur
    leafhelioptileobj = Pokemon(694, level=13, gender=Genders.Female, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Pound"), GetMove("Tail Whip"), GetMove("Thunder Shock"), GetMove("Charge")], nature=Natures.Modest, ability="Solar Power")#Leaf's Helioptile
    maytorchicobj = Pokemon(255, level=10, gender=Genders.Female, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Quick Attack"), GetMove("Growl"), GetMove("Ember"), GetMove("Flame Charge")], nature=Natures.Adamant, ability="Speed Boost")#May's Torchic
    mayvenonatobj = Pokemon(48, level=13, gender=Genders.Male, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Tackle"), GetMove("Disable"), GetMove("Foresight"), GetMove("Confusion")], nature=Natures.Timid, ability="Tinted Lens")#May's Venonat
    

$ playerparty = [playerparty[0], 
    pikachuobj, 
    leafbulbasaurobj,
    leafhelioptileobj,
    maytorchicobj,
    mayvenonatobj
]

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
$ renpy.pause(1.5, hard=True)

hide blank2

scene stadium_empty

redmind "Here we are again.{w=0.5} I wonder if they're even gonna let us in after what happened last time."

show blue uniform frownmouth with dis
    
blue @talkingmouth "I had to wait around this entire time, just for you to get changed? Let's get a move on! Hurry up and ask them to let us use the arena already!"

red @talking2mouth "Why me?{w=0.5} This was {i}your{/i} idea."
      
blue @talkingmouth "The.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
    
extend @closedbrow talkingmouth " The captain said I wasn't allowed to show my face here until Battle Team sign-ups start."

show blue angry with dis

red @surprised "Janine...{w=0.5} {i}banned{/i} you from the Battle Hall?"
red @happy "Ha ha ha! Serves you right!{w=0.5} Getting all up in her face like that."
    
blue @talkingmouth "Just shut up and ask already!"
    
red @talkingmouth "But wait, this means we can't have our battle if you're not allowed in here.{w=0.5} That's a damn shame."

show blue surprised
show janine at leftside
with dis
        
janine @talkingmouth "I'm willing to make an exception."

red @happy "Janine! Big fan of your work. Saw that battle on Wednesday. Very impressive."

janine @angrybrow talkingmouth "Flattery won't get you into the team any more than that guy's self-aggrandizement will."

red @happy "Noted. Hey, how does your Venomoth have five moves?"

janine @closedbrow talkingmouth "Secret shinobi technique. Don't worry about it."

red @happy "Sure. So, are you Battle Team guys doing anything right now?"

janine @talkingmouth "No, it's just me and a couple of last year's graduates."
janine @thinking "And I heard what you were talking about.{w=0.5} I'm allowing you two an arena for your battle."

red @thinking "Really?{w=0.25} Just like that?{w=0.5} But I thought [blue_name] was banned from the Battle Hall."

janine @talkingmouth "He is, but you're not. It wouldn't be fair to kick you out because of something you didn't do."

red @happy "Hey, you're pretty nice. Thanks."
    
janine @angrybrow talkingmouth "Yeah, yeah, we're on a schedule. Come in, and we'll get you two started right away."

hide janine with dis
    
blue @talkingmouth "Nice try, trying to get out of this.{w=0.5} Unfortunately for you, there's no weaseling out of this one."
blue @happy "Now get in here and take your beating like a man!"

if WonBattle("Blue1"):

    show blue angry with dis

    red @angry "You sure are running your mouth a lot for someone that already lost to me before."
    blue @talkingmouth "I told you, I wasn't serious that time.{w=0.5} And I'll prove it to you with this battle!"
    
else:
    red @thinking "You know, there's a saying.{w=0.5}{nw}"

    extend @angry " It goes something like, 'be humble in victory, and gracious in def--'"
    
    blue @angrybrow talkingmouth "Stop quoting your dumbass old-person books, you're just stalling!{w=0.5} You that scared of getting dumpstered by me? Give me a break!"
    
show blue angry with dis

red @talking2mouth "Let's just get this over with, then.{w=0.5} This is for real, right?"

blue cocky @talkingmouth "'Bout time you got serious.{w=0.5} I'm not holding back this time!"

hide blue with dis
    
pause 1.0

show hilbert uniform:
    xpos 900 alpha 0.0
    ease 0.7 xpos 720 alpha 1.0
    
hilbert "..."

red @happy "Hey! Hilbert, you showed up."

hilbert @sad "Your grasp of the obvious is as ironclad as ever."

red @talkingmouth "Well, I'm happy you're here, even if you're not."

hilbert @closedbrow "Just beat him. There's no need for all this sentiment."

red @happy "That's the plan!"

show hilbert:
    xpos 720 alpha 1.0
    ease 0.75 xpos 1200 alpha 0.0
    
pause 1.5

hide hilbert

show leaf:
    alpha 0.0 xpos 900
    ease 0.5 xpos 750 alpha 1.0
    
leaf "You nervous?"
    
red @happy "Hey, Leaf. Thanks again for... y'know."

leaf @sarcastic "Oh, believe me, I want to see his stupid mouth shut up as much as you do. I've never seen a worse case of big fish, small pond syndrome."

red @thinking "So... you got any helpful tips for me before I dive in?"

leaf @surprised "Oh, yeah, no. You don't need helpful tips.{w=0.33} If you can't beat him now, you'll never beat him."

if WonBattle("Blue1"):
    leaf @happy "And since you already did, this is in the bag!"

else:
    leaf @happy "So this is your chance to make up for Tuesday!"

leaf flirt "I'll be cheering you on from the sidelines, and streaming the whole thing to May.{w=0.5} Now wipe that stupid look off his face and show him what you got!"

red @happy "...Well, all right then. Here goes nothing!"

show leaf -flirt with dis:
    xpos 750 alpha 1.0
    ease 0.5 xpos 800 alpha 0.0
    
$ renpy.pause(1.0, hard=True)

show blue uniform cocky:
    xpos 700 alpha 0.0
    ease 0.5 alpha 1.0

pause 0.5
    
blue "Ready for a trip to the dumpster?"

red "Yep, I got your name on the ticket right here."

stop music fadeout 1.0

blue cocky "Don't be so goddamn cocky! I've got a little trick up my sleeve this time!"

$ renpy.transition(Dissolve(3.0))
show screen currentdate

pause 7.0

red angrybrow smilemouth "Yeah. So do I."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [
    Pokemon(pokedexlookupname("Eevee", DexMacros.Id), level=7, ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Adamant, moves=[GetMove("Tackle"), GetMove("Covet"), GetMove("Quick Attack"), GetMove("Tail Whip")], gender=Genders.Male, ability="Adaptability"),#Eevee
    Pokemon(pokedexlookupname("Pidgeotto", DexMacros.Id), level=21, ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Modest, moves=[GetMove("Gust"), GetMove("Tackle"), GetMove("Pursuit"), GetMove("Twister")], evs=[0, 1, 0, 1, 0, 1], gender=Genders.Male, ability="Keen Eye", intelligence=1)])#Pidgeotto

call Battle([trainer1, trainer2], uniforms=[False, True]) from _call_Battle_7
$ gymbattles["Blue2"]  = _return

$ renpy.pause(1.0, hard=True)
    
show blue uniform angry behind blank2:
    xpos 700+240 alpha 1.0
    
$ renpy.music.queue("Audio/Music/League_Loop.ogg", channel='music', loop=True, fadein=0.5, tight=None)
play sound "Audio/Short Med Applause.ogg"

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

show red angry at Transform(xpos=0.08, yanchor=0.35)
"{color=#cf0000}[first_name]{/color} & {color=#3110dd}[blue_name]{/color}" "\"What the HELL?!\""

hide red with dis

blue "You had six Pokémon!"
red angry "You had a {i}level 21{/i} Pidgeotto!"
blue "You used someone else's Pokémon!"
red "You used a Pokémon you've been training for battle for {i}fifteen years!{/i}"
blue "That was cheating, asshole!"
red "Look who's talking, [blue_name]!"

if (WonBattle("Blue2")):
    blue "The only reason you won is because you cheated! I refuse to accept the results of this battle!"

    red "Get real! You know I wouldn't have had a chance against your Pidgeotto without borrowing my friends' Pokémon!"

    show blue angry:
        xpos 700+240
        ease 0.5 xpos 240+800

    blue frownmouth -angry @angrybrow angrymouth"That's right! You don't have a chance! Never have. Never will!"

    redmind -angry @thinking "I {i}literally{/i} just beat you."

    show leaf happy:
        xpos 240+1600 alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 240+350
            
    leaf "You did it! I knew you guys could beat him!"
    
    show leaf -happy with dis:
        alpha 1.0 xpos 240+350
    
    show blue angry at dissolveaway:
        xpos 240+800
    
    $ renpy.music.play(startercry, channel="altcry", loop=None)
    starter "[starter_species_name]!"
    
    show leaf:
        xpos 240+350
        ease 0.6 xpos 240+400
        
    show hilbert uniform:
        xpos 240+1200 alpha 0.0
        parallel:
            ease 0.75 xpos 240+1000 alpha 1.0
            
    pause 0.75
    
    show leaf:
        xpos 240+400
        
    show hilbert:
        xpos 240+1000 alpha 1.0
            
    if not WonBattle("Blue1"):
        hilbert @talkingmouth "You see what happens when you don't act like an idiot? That first battle with [blue_name] could have been avoided entirely."
        red @talkingmouth "What, by borrowing a bunch of peoples' Pokémon in class, right in front of the teacher?"
        hilbert @talkingmouth "Yes. It would have worked then, too."
        
    else:
        hilbert "I guess I have to give you some credit, [first_name]."
        
    hilbert @closedbrow "I'll admit, I didn't expect you to win." 
    hilbert @closedbrow "It also didn't occur to me that you could borrow your friends' Pokémon... I was just indicating that you should grab your Pikachu."
    hilbert @talkingmouth "You gave me a lot to think about."

    red @happy "Well, verdict?"

    hilbert @sad "If I didn't know which ones were your Pokémon, I'd think they were all yours, and you'd had them for years."
    hilbert @talkingmouth "I half suspect that you could start commanding [blue_name]'s Pidgeotto mid-battle, and it would listen to you more than it does to him."

    red @happy "Aw, thanks!"

    hilbert @angry "It's not a compliment. It's power. And while power exists, someone's going to want to take it."
    
    show hilbert sad:
        xpos 240+1000 alpha 1.0
        ease 0.75 xpos 240+1400 alpha 0.0
        
    hilbert "You were alright. That's all you'll get."
    
    show hilbert:
        alpha 0.0 xpos 240+1400
    
    show leaf:
        xpos 240+400
        ease 0.75 xpos 240+350
        
    pause 0.75
    
    show leaf:
        xpos 240+350
        
    leaf @surprised "Look at that, you even got Mr. Serious there complimenting you."
    
    red "Eh, it's Hilbert being Hilbert.{w=0.5} I've gotten pretty used to him already."
           
    if WonBattle("Blue1"):
        leaf @thinking "That's two in a row for you.{w=0.5} Think that's enough to put [blue_name] in his place?"
        
    else:
        leaf @thinking "It's one win apiece for both of you now.{w=0.5} Think that's enough to put [blue_name] in his place?"
    
    red @sadbrow talkingmouth "No chance. It's a nice dream, though."

    leaf @surprised "But a promise is a promise.{w=0.5} [blue_name] agreed to stop messing with you!"

    red @thinking "Yeah, but this is far from the first time we've had a battle where he promised to stop messing with me."
    red @happy "...But it's like one of three times that I've actually won! I swear, I used to have nightmares about that Pidgey. Well, Pidgeotto now. Apparently."
    
    show blue angry:
        alpha 0.0 xpos 240+50
        ease 0.75 xpos 240+0 alpha 1.0
            
    pause 0.75
    
    show leaf surprisedbrow frownmouth with dis
    
    blue sad "{size=28}{i}It wasn't supposed to be like this...!{/i} {/size}"
    
    red sadbrow frownmouth "..."
    redmind "He makes it really hard to feel sorry for him... like, I get that he's desperate for a win, but all his wounds are self-inflicted... or at least {b}very{/b} avoidable."
    red @talking2mouth "Hey. Blue, look, you did well, but--"
    
    pause 1.0
    
    show blue angry with dis:
        xpos 240+0
        ease 0.5 xpos 240+400
        
    show leaf surprised:
        xpos 240+350
        pause 0.2
        ease 0.5 xpos 240+1000
        
    blue angry "Don't you even think about lecturing me!{w=0.5} You actually believe you're better?"

    show blue angry:
        xpos 240+400
        
    show leaf angry:
        xpos 240+1000
    
    leaf @sarcastic "Get over yourself already! You lost the match, now quit being such an ass!"
    leaf @talkingmouth "You made a promise. You've got to honor it!"

    blue frownmouth "I have no idea what you're talking about."

    leaf "Wha-wha-what... but...{nw}"
    show stadium_empty with vpunch
    leaf angry "You promised! When you promise something, that means... it means you {i}promised!{/i}"
    
    blue angry "The hell are you on about?{w=0.5} Are you this loser's keeper or some sh--"

else:
    red "The only reason you won is because you brought in an overpowered Pidgeotto to a fight with a bunch of level fives!" 

    blue "Give me a break! You had a team three times larger than mine! You know I wouldn't have had a chance against your waves of filler without my Pidgeotto!"

    red "They're not filler, they're my friends' friends, and the only thing they did was even the odds! You were trying to trick me! {i}I{/i}, at least, knew you were going to pull something. Borrowing Pokémon at least gave me a chance!"

    show blue angry:
        xpos 700+240
        ease 0.5 xpos 240+800

    blue frownmouth -angry @angrybrow angrymouth "You don't have a chance! Never have. Never will!"

    redmind -angry frownmouth @thinking "If I'd known which Pokémon he had, I could've beat him..."

    show leaf sad:
        xpos 240+1600 alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 240+350
            
    leaf "Well... I thought you did really well. Especially you, Bulbasaur and Helioptile!"
    
    show leaf happy:
        alpha 1.0 xpos 240+350

    leaf "So don't look sad, alright, you guys?"
    
    show blue angry at dissolveaway:
        xpos 240+800
    
    $ renpy.music.play(startercry, channel="altcry", loop=None)
    starter "[starter_species_name]..."
    
    show leaf -happy with dis:
        xpos 240+350
        ease 0.6 xpos 240+400
        
    show hilbert uniform:
        xpos 240+1200 alpha 0.0
        parallel:
            ease 0.75 xpos 240+1000 alpha 1.0
            
    pause 0.75
    
    show leaf:
        xpos 240+400
        
    show hilbert:
        xpos 240+1000 alpha 1.0
            
    if WonBattle("Blue1"):
        hilbert @talkingmouth "...You should have done better. I saw that first battle you had with him. You had {i}more{/i} than enough to beat him."
        
    else:
        hilbert "I see you haven't learned anything from your first loss."
        
    hilbert @talkingmouth "You had a unique advantage here, and you squandered it. What a waste of time."

    red @sad "Unique advantage?"

    hilbert @sad "You borrowed Pokémon, right? If I didn't know which ones were yours, I'd think they were all yours, and you'd had them for years."
    hilbert @talkingmouth "I half suspect that you could start commanding [blue_name]'s Pidgeotto mid-battle, and it would listen to you more than it does to him."
    hilbert @angry "And yet you still lost."

    pause 2.0

    hilbert @angry "If you can't make use of that power, someone else will."
    
    show hilbert sad:
        xpos 240+1000 alpha 1.0
        ease 0.75 xpos 240+1400 alpha 0.0
        
    hilbert "Get better."
    
    show hilbert:
        alpha 0.0 xpos 240+1400
    
    show leaf:
        xpos 240+400
        ease 0.75 xpos 240+350
        
    pause 0.75
    
    show leaf:
        xpos 240+350
        
    leaf @surprised "...Eesh. Kinda harsh?"
    
    red "Eh, it's Hilbert being Hilbert.{w=0.5} I've gotten pretty used to him already."
           
    if WonBattle("Blue1"):
        leaf @thinking "I really thought you'd win this one after you won last time..."

        red @happy "Yeah. So did I! I just didn't see the Pidgeotto coming."
        
    else:
        leaf @thinking "I mean, I'm sure you're a good battler in other situations. Maybe it's just [blue_name] that gets under your skin?"
    
    red @sadbrow talkingmouth "I mean, as much as Blue is a jerk, he's a {i}really{/i} good trainer. He pushes his Pokémon to their absolute limit." 
    red @thinking "You could give him a Rattata, and it'd probably be a Raticate by the end of the day. Wouldn't listen to a word he said, but with that much power, does it matter?"
    red @happy "We've battled before, and I've only won, like, twice. I swear, I used to have nightmares about that Pidgey. Well, Pidgeotto now. Apparently."
    
    show blue angry:
        alpha 0.0 xpos 240+50
        ease 0.75 xpos 240+0 alpha 1.0
            
    pause 0.75
    
    show leaf surprisedbrow frownmouth with dis
    
    blue angry "{size=44}Hey! You made a promise. Remember? Snap to it, {i}inferior trainer!{/i}{/size}"
    
    red sadbrow frownmouth "..."
    redmind "...Sigh. Do I have enough pride to make a big deal of this?"
    redmind "If it was anyone else, probably, but..."
    red @talking2mouth "Alright, Blue. You beat me. Fair and square."
    
    pause 1.0
    
    show blue angry with dis:
        xpos 240+0
        ease 0.5 xpos 240+400
        
    show leaf surprised:
        xpos 240+350
        pause 0.2
        ease 0.5 xpos 240+1000
        
    blue angry "Y-yeah! I know that! You said you'd admit you'll never be a better trainer than me! So say {i}that!{/i}"

    show blue angry:
        xpos 240+400
        
    show leaf angry:
        xpos 240+1000
    
    leaf @sarcastic "Get over yourself already! You won the match, now quit being such an ass!"
    leaf @talkingmouth "[first_name] fulfilled his promise. Now leave him alone!"

    blue angry "The hell are you on about?{w=0.5} Are you this loser's keeper or some sh--"
    
lance "That's enough."

show lance:
    xpos 240+100 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.25 xpos 240+450

show janine:
    xpos 240+-50 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos 240+70

show blue surprised:
    xpos 240+400
    pause 0.1
    ease 0.75 xpos 240+870
    
show leaf surprised:
    xpos 240+1000
    ease 0.75 xpos 240+1380
    
$ renpy.pause(1.5, hard=True)

show lance:
    alpha 1.0 xpos 240+450

show janine:
    alpha 1.0 xpos 240+70

show blue surprised:
    xpos 240+870
    
show leaf surprised:
    xpos 240+1380

redmind @sadbrow frownmouth "Oh boy.{w=0.5} Well, it figures that he'd show up here, but why now?"

if not WonBattle("Blue2"):
    lance @closedbrow talkingmouth "There's no merit in gloating after a victory.{w=0.5} I will not stand for this kind of behavior in the Battle Hall!"

blue @angry "It's you..."

lance @closedbrow talkingmouth "The battle is over. Hurry up and shake hands!{w=0.5} You're inconveniencing the other Trainers."

lance @angry "That goes for everyone else, too.{w=0.5} Unless you're with the Battle Team, begone from here!"

show lance:
    xpos 240+450
    ease 0.5 xpos 240+500
    
show leaf surprised
show blue surprised behind leaf
with dis

lance "Except for you.{w=0.33} You stay."

show lance:
    xpos 240+500
    
red @surprised "...Me?"

show hilbert uniform behind leaf:
    xpos 240+1170 alpha 0.0
    ease 0.5 alpha 1.0 xpos 240+1130

hilbert @surprised "What did you do, [first_name]?"

show hilbert:
    alpha 1.0 xpos 240+1130
    
red @thinking "I guess you weren't at the Exhibition match after all. Well, I think this is going to be part two of that."

hilbert @sad "...Well, I'm bored already, so keep it to yourself."

show hilbert:
    xpos 240+1130 alpha 1.0
    ease 0.5 xpos 240+2000 alpha 0.0
    
hilbert @talkingmouth "Later."

show hilbert:
    xpos 240+2000 alpha 0.0
    
show leaf surprisedbrow frownmouth:
    xpos 240+1380 ypos 1080 zoom 1.0
    pause 0.25
    ease 0.75 xpos 240+1250 ypos 1330 zoom 1.35
    
leaf @sadbrow talking2mouth "All right, I guess I gotta go...{w=0.5} I'd stick around, but I'd rather not get on Lance or Janine's bad side."

show leaf:
    xpos 240+1250 ypos 1330 zoom 1.35
    
leaf -surprisedbrow -frownmouth @happy "I'll talk to you later!"

show leaf:
    xpos 240+1250 alpha 1.0 ypos 1330 
    ease 0.75 xpos 240+1600 alpha 0.0 

red @thinking "Yeah, see you."

show blue:
    xpos 240+870
    ease 0.75 xpos 240+1200

redmind frownmouth "Oh boy. Better buckle up for more ranting."
redmind "...Wait, Blue's still here?"

hide leaf

show blue:
    xpos 240+1200
    
lance @closedbrow "You. Over there.{w=0.5} I thought I told everyone to leave."

blue @talkingmouth "You're the supervisor of the Battle Team, right? You're Lance."

lance @angry "I won't tell you again.{w=0.33} Leave."

show blue:
    xpos 240+1200
    ease 0.5 xpos 240+1100

blue @surprised "Wait! You were watching our match, right?{w=0.5}{nw}"

show blue:
    xpos 240+1100
    
extend " I think it's pretty safe to say that I got the skills to get into the Battle Team."

show janine surprised
show blue happy
with dis

blue @talkingmouth "Janine over there won't admit it, but I'm sure you can recognize talent!"

show blue surprised
show janine -surprised
with dis

lance @talkingmouth "No."

show blue:
    xpos 240+1100
    ease 0.75 xpos 240+1200

blue @sadbrow surprisedmouth "But.{w=0.25} I just--{w=0.5}you didn't..."

show blue surprised:
    xpos 240+1200
    
lance @talkingmouth "I said, no.{w=0.5} Now get out."

janine @talkingmouth "You're not helping your case by begging us to sign you up every day, you know."
janine @talkingmouth "It's...{w=0.5}{nw}"
extend @sad " well, frankly, it's a little embarrassing."

lance @closedbrow talkingmouth "Further, I trust the judgement of the Captain of the Battle Team absolutely. If the Captain says you get in, then you do so. Similarly, if the Captain says you do not..."
lance @angrybrow talkingmouth "You do not." 
lance @talkingmouth "Do not attempt to subvert the chain of command. Regardless of my status as a Champion, I am the Battle Team's {i}Advisor.{/i}"

pause 1.5

show blue angry

pause 1.0

show blue angry:
    xpos 240+1200
    ease 0.25 xpos 240+1100
    
blue @talkingmouth "What's up with that?"

if not WonBattle("Blue2"):
    blue @talkingmouth "Are you two {i}blind?{/i}{w=0.5} I wiped the floor with [first_name]. He didn't stand a chance!"

blue @talkingmouth "You're making the biggest mistake of your life not putting me on the team right now!{w=0.5} I'm the best thing to happen to this school, so I deserve to be in here {i}now!{/i} "

lance @sadbrow talkingmouth "{i}You're{/i} supposed to be Professor Oak's grandson?"

show lance:
    xpos 240+500
    ease 1.0 xpos 240+700
    
lance "You talk big, but you're so uncertain of your own skills that you refuse to earn your spot on the team like any other student."

show lance:
    xpos 240+700

show blue angry:
    xpos 240+1100
    ease 0.5 xpos 240+1000
    
blue @angrybrow talkingmouth "You don't know a damn thing about me.{w=0.5}{nw}"

show janine angry with dis

extend " You think you're some big shot just 'cause you run things around here?"

janine @angrybrow talkingmouth "Show some respect!{w=0.5} One more word out of you and I'll have you thrown out of this building."

lance @closedbrow talkingmouth "Janine, allow me."

lance @sadbrow talkingmouth "This is the second time this week a brand-new student has presumed to make character judgements about me."
lance @angrybrow "And yet, though you are a modicum more polite, I find your words far more tiring and worthless to listen to. This is not a position a Battle Team hopeful wants to be in."
lance @sadbrow talkingmouth "Begone."

pause 1.0

show blue angry:
    xpos 240+1000
    ease 1.0 xpos 240+1200
    
blue ".{w=0.25}.{w=0.25}."

show blue:
    ease 0.5 xpos 240+1200
    
blue closedbrow angrymouth "...Erghh!"

show blue:
    xpos 240+1200 alpha 1.0
    ease 0.5 alpha 0.0 xpos 240+1500
    
$ renpy.pause(0.75, hard=True)

hide blue
    
redmind @happy "Wow, I need to start taking tips from these guys to save myself some [blue_name]-induced migraines."

show lance:
    xpos 240+700
    ease 0.75 xpos 240+950
    
show janine:
    xpos 240+70
    ease 1.0 xpos 240+350

lance @sadbrow talkingmouth "Now then...{w=0.5} our business is with you."

show lance:
    xpos 240+950
    
show janine:
    xpos 240+350

lance @talkingmouth "...You look vaguely familiar.{w=0.5} Have we met before?"

red @closedbrow happymouth "Um, well... I look pretty similar to Ethan? If you ignore our hair, anyway."

janine -angry @thinking "The kid's a new student. He's only been here for... what, five days?{w=0.5} According to Blue, his name's [first_name]."

lance @thinking "[first_name]...{w=0.5} I'm sure I've heard that name from somewhere."

red @surprised "Uh, never mind that.{w=0.5} You said you have business with me?{w=0.5}{nw}"
extend @happy " It's getting kinda late, so I'd like to get back before curfew."

janine @happymouth "Don't worry, this won't take long.{w=0.5} We just wanted to ask a few questions about your team."

if WonBattle("Blue2") == False:
    lance @talkingmouth "You commanded a team of extremely diverse Pokémon flawlessly. You may have lost that battle, but they responded to your commands with the swiftness of a Champion-trained Pokémon."
else:
    lance @talkingmouth "You commanded a team of extremely diverse Pokémon flawlessly. They responded to your commands with the swiftness of a Champion-trained Pokémon."

lance @talkingmouth "How long have you been training them for?"

janine @thinking "My Venomoth didn't get a word I was saying 'til about middle school.{w=0.5} And I've had him since I was four."

janine @talkingmouth "You must've put your team through some intense training.{w=0.5} Why haven't any of them except the Pikachu evolved yet?"

show janine surprised
show lance sadbrow
with dis

red @talkingmouth "Uh... well, actually, only the [starter_species_name] and the Pikachu are mine.{w=0.5} I borrowed the other four from my friends for this specific battle."
redmind @thinking "...Crap, that's not against the rules, is it?"
redmind @thinking "Well, whatever I say here, I can't tell them about Old Man Oak's 'Frienergy' theory. If he's right, that's something I need to keep very private."

red "And I really didn't do anything particularly special.{w=0.5} I just told them what I wanted them to do, and they listened."

show lance closedbrow
show janine thinking
with dis

redmind "...Oh, crap. That was a lie, wasn't it? I've always been awful at lying. Was that, all along, because of Old Man Oak's theory?"

pause 1.5

janine @angrybrow talkingmouth "Are you serious?"

show janine surprised
show lance angry
with dis

show blue:
    xpos 240+1700 alpha 0.0
    ease 0.5 xpos 240+1300 alpha 1.0
    
blue uniform @angry "Yeah. Four of those aren't even his! Which is totally cheating, right?"

show janine angry

show blue angry:
    xpos 240+1300 alpha 1.0
    
blue @angrybrow talkingmouth "What're you trying to pull, [first_name]?!"

show blue surprised with dis

janine @angrybrow talkingmouth "I thought I told you to keep your mouth shut!"

show blue angry:
    xpos 240+1300 alpha 1.0
    ease 0.5 alpha 0.0 xpos 240+1800
    
$ renpy.pause(1.5, hard=True)

hide blue

janine @thinking "In any case, there has to be something else.{w=0.5} Working with Pokémon, let alone battling with them, just isn't that simple."

redmind @sad "Geez. There's just no belief there. Now I'm second-guessing everything I'm saying... This ability is really complicating things."
redmind @thinking "I just wish I knew if it existed."

janine @talkingmouth "Do you use hand signals or specific vocal commands?{w=0.5} Come on, give us something to work with here."

red @sadbrow talkingmouth "I really don't know what to tell you.{w=0.5} They understand me and I can understand them. I'm starting to feel like a broken record here."

janine @thinking "Okay, these were your friends' Pokémon. Are your friends, like, Champions? Did they put them through intense training without raising their level?"

red @sadbrow talkingmouth "No... my friends are just other students. I met them, uh, last Friday."

janine @thinking "Okay... you said that Pikachu was yours, right? What about--"

lance @thinking "I should've known."

show janine surprised with dis

lance @sadbrow talkingmouth "Now I remember.{w=0.5} {i}You're{/i} the one with that runt of a Pikachu."

redmind "Oh, crap."

janine -surprised @talkingmouth "Wait, this kid?{w=0.5} He's the one that you were complaining about before?"

janine @thinking "Small world."

lance @sadbrow "I shudder to think of the time I've wasted listening to your pitiful meanderings...{w=0.5}{nw}"

extend @angrybrow talkingmouth " You had no idea what you were talking about from the beginning."

show lance angrybrow:
    xpos 240+950
    ease 0.5 xpos 240+900
    
lance @talkingmouth "They understand me and I understand them.'{w=0.5} To say such things...{w=0.25} you mock the very foundation of Kobukan Academy."

show lance:
    xpos 240+900

lance closedbrow @talkingmouth "I have nothing more to say to you."

janine @sadbrow talkingmouth "Lance, take it easy.{w=0.5} I think he was being serious."

show lance:
    xpos 240+900
    ease 0.5 xpos 240+950
    
lance @talkingmouth "If he is, and he is not intentionally wasting our time, he is direly delusional, and we have ever more reason to show him the door."
    
redmind @angrybrow frownmouth "What's his problem all of a sudden?{w=0.5} It's like his personality completely turned itself on its head when he remembered who I was."

lance @talkingmouth "I was hoping to get some information out of you, but it's clear that you're just wasting everyone's time."

show blue uniform happy:
    xpos 240+1350 alpha 0.0
    ease 0.5 alpha 1.0
    
blue "Pfft."
    
show blue sad with dis

lance @angrybrow talkingmouth "{i}Why are you still here?{/i}{w=0.5} Has anyone, ever, even once in your privileged life, told you {i}no?{/i}"

if WonBattle("Blue2"):
    lance @sadbrow talkingmouth "The grandson of Professor Oak losing to someone like him...{w=0.5} What an embarrassment."
    
    blue "...!"
    
    lance @angrybrow talkingmouth "You could have beaten him, but you lacked finesse and discipline.{w=0.5} Even with your absurd level advantage, you struggled mightily."

    lance @closedbrow talkingmouth "Your match was a travesty to watch."

else:
    lance @sadbrow talkingmouth "The grandson of Professor Oak having so much trouble with someone like him...{w=0.5} What an embarrassment."
    show lance angry
    
    blue "...!"
    
    lance @angrybrow talkingmouth "Don't think I didn't hear you mouthing off when you came in here.{w=0.5} Celebrating victory before the match even started...{w=0.5}"
    
    lance @closedbrow talkingmouth "Even with your overwhelming level advantage, it was far from a clean battle."
    

show lance thinking
show blue angry
with dis

redmind @happy "Call me immature, but even I can't stop myself from smiling at [blue_name] getting scolded like that.{w=0.5} It's sort of refreshing to see it happen to someone that's not me."

show blue angry:
    xpos 240+1350
    ease 0.25 xpos 240+1250
    
blue @angrybrow talkingmouth "You got a problem with the way I do things, I'll take you on myself!"

show janine angry

blue "Acting so high and mighty just 'cause of a few trophies.{w=0.5} Yeah, I know of your accomplishments... or lack thereof."

show lance angry
show blue cocky
with dis

blue @talkingmouth "Yeah, you might've Champed two regions, but how many tries did that take? One of the Elite Four literally died of old age before you ever beat her!"

show blue angry

play sound "Audio/Whoosh.ogg"

show janine smoke:
    alpha 1.0
    ease 0.25 alpha 0.0
show smoke as smoke1:
    alpha 0.0 xpos 240+300 yalign 3.0
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0
        
$ renpy.pause(0.5, hard=True)

show smoke as smoke2:
    alpha 0.0 xpos 240+850 yalign 3.0
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0

show lance:
    xpos 240+950
    ease 0.75 xpos 240+300

show blue surprised with dis:
    xpos 240+1250
    ease 0.25 xpos 240+1200
    
pause 0.5
    
show janine angry:
    alpha 0.0 xpos 240+850
    ease 0.25 alpha 1.0

janine @angrybrow talkingmouth "I've just had about enough of you and your {nw}"

show janine angry:
    xpos 240+850 alpha 1.0
    
show blue surprised:
    xpos 240+1200

extend "disrespect towards Lance.{w=0.5} If you don't get out of my face within the next ten seconds, we're gonna have a {i}big{/i} problem."
    
redmind @thinking "'Discretion is the better part of valor,' Blue..."

show blue angry with dis

blue "...Tch!"

blue @angrybrow talkingmouth "[first_name]! You won't always be able to rely on your friends! You'll be left alone and powerless one day--{w=0.5}and you're still just a third-rate Trainer compared to me!"

show blue angry:
    xpos 240+1200
    ease 0.25 xpos 240+1250
    
show janine angry:
    xpos 240+850
    ease 0.5 xpos 240+950

janine "Get {i}out!{/i} "
    
show blue angry:
    xpos 240+1250 alpha 1.0
    ease 0.5 xpos 240+1800 alpha 0.0

pause 1.0

hide blue

redmind "I thought I was a second-rate Trainer.{w=0.33} When did I get demoted?"

show janine -angry with dis:
    xpos 240+950
    ease 1.0 xpos 240+1000

show lance -angry with dis:
    xpos 240+300
    ease 0.5 xpos 240+500
    
lance @talkingmouth "And why haven't {i}you{/i} left yet?"
    
lance @sadbrow talkingmouth "Leave. You have no more business being here."

red @talking2mouth "On my way out."

janine @talkingmouth "Just a second, Lance.{w=0.5} I'd like a word with him myself, if you're okay with that."
    
lance @thinking "I see no point, but do what you want."

lance @talkingmouth "I'm leaving.{w=0.5} If you need me for something, you know where to find me."

show lance:
    xpos 240+500 alpha 1.0
    parallel:
        pause 0.5
        ease 0.5 alpha 0.0
    parallel:
        ease 1.0 xpos 240+0
        
$ renpy.pause(2.0, hard=True)

hide lance

show janine:
    xpos 240+1000
    ease 0.75 xpos 240+720
    
janine @happy "Phew! Now that we have some privacy, I'd like to talk a little more about you and your Pokémon."

show janine:
    xpos 240+720
    
janine @talkingmouth "You said you've only had your starter, that [starter_species_name], for a short while, but you two can understand what the other is saying without a hitch.{w=0.5} And it's the same way with your Pikachu."

janine @thinking "I mean, you're hiding something, obviously, but I don't think you're straight-up lying."

red @happy "You believe me?{w=0.33} Finally!{w=0.5} It was starting to feel like everybody in the room was against me."

janine @happy "Yeah, but, you might prefer that I didn't believe you. I mean, I'm going to try and use that. Use the heck out of it, actually."

red @surprised "U-use? What do you mean?"

janine @thinking "You said that four of your Pokémon weren't actually yours. Never trained with them before?"

red @talkingmouth "Uh, yeah."

janine @thinking "Well, that's {i}really{/i} interesting. Because if you can do that with Pokémon that are stronger than the ones you have on-hand, then we could just hand you a couple strong Pokémon and have you go to town."
janine @talkingmouth "As long as you're able to borrow, you wouldn't have to train at all... which would save us so much time..."

redmind @surprised "Uh... she's looking at me like she's a spider figuring out the best way to eat me..."
red @surprised "I'm not sure I can help {i}that{/i} much. I mean, I'm still figuring out what I can, and, y'know, {i}can't{/i} do with Pokémon."

janine @angrybrow talkingmouth "Uh, yeah. Duh. And this is how we figure it out. Test you until you break."

red @surprised "Could we stop right before that point?"

show janine:
    xpos 240+720
    ease 0.5 xpos 240+800
    
janine @thinking "You can tap out any time."

show janine:
    xpos 240+800
    ease 0.5 xpos 240+720

janine @happy "After I let you, I mean."

show janine:
    xpos 240+720

redmind @surprised "Uh... I kinda feel like something in me is awakening..."

janine @talkingmouth "Hey, you alright? You look pale."

red @talkingmouth "Yeah, it's, uh, it's just been a long day."

janine @surprised "Oh, yeah, it's getting late, right? You should probably head back."

red @happy "Right. Thanks."

pause 2.0

show janine:
    xpos 240+720
    ease 0.5 xpos 240+800
    
janine @talkingmouth "Oh, hold up.{nw}{w=0.5}" 
extend @happy " You're cool with being pushed to your absolute breaking point, right?"

menu:
    "As long as it's by you.":
        show janine blush surprised with dis

        pause 2.0
        
        janine angrybrow blush smirkmouth "You've got a lot of nerve."

        red @angrybrow talkingmouth "As I'm willing to prove in battle. Over and over."

        janine -blush -angrybrow -smirkmouth @thinking "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talkingmouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        $ ValueChange("Janine", 2, (240 + 800) /1920)

        janine angrybrow blush smirkmouth "{w=0.25}.{w=0.25}.{w=0.25}.Good boy."

    "Absolutely.":
        janine @thinking "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talkingmouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        $ ValueChange("Janine", 1, (240 + 800) /1920)

        janine @smirkmouth "Correct answer."

    "I'd rather not.":
        janine @thinking "Hm... well, there's a way where you wouldn't have to train as hard, I guess."

        janine @thinking "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talkingmouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        janine @smirkmouth "Correct answer."

janine @happy "Now, get to bed.{w=0.5} If you're not back soon, security will catch you."

redmind @thinking "Yeah, I'd have more luck escaping them if I was a pizza... at least according to Hilbert."

show janine:
    xpos 240+800
    ease 1.0 xpos 240+900

janine "Remember. April 19th. Be there."

window hide

show blank2 with dis:
    alpha 1.0

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_43

$ HealParty()
$ playerparty.remove(leafbulbasaurobj)
$ playerparty.remove(leafhelioptileobj)
$ playerparty.remove(maytorchicobj)
$ playerparty.remove(mayvenonatobj)

$ renpy.pause(3.0, hard=True)

show night at vspaz

pause 3.5

hide night

############################################################################################################################################################################################################################
#### 5. END OF DAY #########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.music.play("Audio/mediumcrowdloop.ogg", channel='crowd', loop=True, fadein=2.0)

scene lounge
show brendan:
    xpos 240+600
show may happy:
    xpos 240+900
with Dissolve(2.0)

show brendan:
    xpos 240+600 alpha 1.0
show may happy:
    xpos 240+900 alpha 1.0
    
redmind @thinking "What a day..."

show brendan
show may

redmind @thinking "I agreed to meet with Brendan and May for dinner without a second thought, but I haven't paid any attention to the conversation the entire time."

brendan @talkingmouth "How'd your day go, man?{w=0.5} You seem kinda down."

red @happy "Me? Nah, I'm fine.{w=0.33} Just a little tired. Still haven't found where to buy energy bars in this school."

may -happy @sadbrow happymouth "You've been tired a lot lately.{w=0.5} You should try and take it easy one of these days."

red @happy "Oh, believe me. I've been trying."

show brendan surprised with dis:
    xpos 240+600
    ease 0.5 xpos 240+800
    
show may:
    xpos 240+900
    pause 0.2
    ease 0.5 xpos 240+1100
    
show leaf:
    xpos 240+200 alpha 0.0
    ease 0.7 xpos 240+400 alpha 1.0
    
leaf @talking2mouth "I'll bet you're tired.{w=0.5} I'm surprised you managed to crawl out of that situation in one piece."

show brendan -surprised with dis:
    xpos 240+800
    
show may:
    xpos 240+1100
    
show leaf:
    xpos 240+400 alpha 1.0
    
leaf @flirt "Seems like you just love getting into trouble."

red @closedbrow talkingmouth "Man, trouble seeks me out. And trouble has spiky, reddish-brown hair."

leaf @happy "Well, I know what'll cheer you up!{w=0.5} What are you guys doing for the weekend?"

brendan @thinking "Oh boy, let's see... got a ton of homework for both homeroom and my electives.{w=0.5}{nw}"

extend frownmouth @surprised " Get this, we need to read three chapters and write a three-page rep--"

leaf @happy "Well, {i}I{/i} was thinking that we can go to the fields outside of school to catch some wild Pokémon!"

red @thinking "Is that even allowed?"

leaf @talkingmouth "Yep! I asked around and all of the teachers gave me the okay."

leaf @thinking "Apparently, all the Pokémon in the fields were originally imported from other regions just for the students here!"

may @happymouth "Really? They just imported Pokémon from other regions?"
may @closedbrow frownmouth "I hope they remembered to do their research on maintaining the native ecosystem..."

red @thinking "That is {i}really{/i} convenient.{w=0.5} I didn't even know importing Pokémon was a thing...{w=0.5} Or legal."

may @talkingmouth "We should invite Serena and the other guys, too.{w=0.5}{nw}"

extend @sadbrow happymouth " I bet they'd get pretty upset if they found out we forgot about them."

red @happy "Definitely. This sounds good to me!"

leaf @happy "Okay, so it's decided!{w=0.5}{nw}"

show brendan surprised with dis

extend @flirt " Let's all meet up at the entrance first thing in the morning and catch some wild Pokémon!"

may @happybrow talkingmouth "Yay! I'll be looking forward to it!"

brendan thinking "But...{w=0.5} my homework..."

redmind @happy "I should bring [pika_name] and [starter_name] with me, too.{w=0.5} Might be a good chance to see them in action against some wild Pokémon."
redmind @thinking "Speaking of which, everyone else is probably bringing their Pokémon, too.{w=0.5} Now, that'll be interesting to see..."
redmind @thinking "I should keep an eye on which Pokémon my friends might let me borrow for the upcoming Battle Team tryouts... oh, geez, I still need to tell everyone about that..."
redmind @happy "I mean, she basically invited me to apply! I guess she doesn't know about Lance's dogma. But she saw how he acted, and didn't seem to care about that, so..."

window hide

show blank2 with dis:
    alpha 1.0
    
$ renpy.music.stop(channel='crowd', fadeout=1.0)
stop music fadeout 2.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_44

$ renpy.pause(2.5, hard=True)

narrator "Your mind races, but you eventually manage to drift off into a deep, but excited, sleep."

jump day010410