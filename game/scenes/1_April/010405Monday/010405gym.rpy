label gym010405:

$ timeOfDay = "Noon"

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

$ renpy.pause(1.0, hard=True)

ethan uniform "So this is the gymnasium.{w=0.5} I wonder if this is an official gym sanctioned by the Pokémon League?"
red uniform "Most likely not. I didn't read anything about that on the website when I was doing my research."
red @thinking "I think it's safe to assume it's just another fancy room in the academy's collection.{w=0.5} Though, other than some old banners lining the walls, this place is barren compared to the others."
ethan @surprised "Old banners?! Dude, those are Champion pennants! They're only given to winners of {i}at least{/i} national tournaments!"
red @happy "Yeah, but they're just banners. If it was the actual Champions hanging up there, then maybe I'd be impressed."

pause 2.0

red @sad "That didn't sound the way I thought it was going to."
ethan @thinking "Yeah, let's just... ignore that..."

hide blank2

show brendan uniform happy:
    xpos (1/6) alpha 0.0
    ease 0.5 alpha 1.0

show may uniform happy:
    xpos (2/6) alpha 0.0
    pause 0.25
    ease 0.5 alpha 1.0

show leaf uniform flirt behind may:
    xpos (3/6) alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

show calem uniform happy behind leaf:
    xpos (4/6) alpha 0.0
    pause 1.0
    ease 0.5 alpha 1.0

show hilbert uniform sad:
    xpos (5/6) alpha 0.0
    pause 1.25
    ease 0.5 alpha 1.0

ethan "Hey, look, there's the rest of the gang!"
red "With all of them together like that, they really make the room seem a lot livelier."

show brendan:
    xpos (1/6) alpha 1.0
    ease 0.5 alpha 0.0

show may:
    xpos (2/6) alpha 1.0
    ease 0.5 alpha 0.0

show leaf:
    xpos (3/6) alpha 1.0
    ease 0.5 alpha 0.0

show calem:
    xpos (4/6) alpha 1.0
    ease 0.5 alpha 0.0

show hilbert:
    xpos (5/6) alpha 1.0
    ease 0.5 alpha 0.0

show misty uniform:
    xpos (4.5/6) alpha 0.0
    pause 0.25
    ease 0.5 alpha 1.0

red "Oh, and there's Misty...{w=0.5} Hopefully she's feeling a bit better since I last saw her."
ethan "What's her story?"
red @happy "Wish I knew."

if (getElective("Water") > 5 or getElective("Ice") > 5):
    red "I learned more from our elective together than I did before."

show misty:
    xpos (4.5/6) alpha 1.0
    ease 0.5 alpha 0.0

hide calem
hide cheren
hide hilda
hide hilbert
hide brendan
hide leaf
hide may

show flannery uniform:
    xpos (1/6) alpha 0.0
    ease 0.5 alpha 1.0

show whitney uniform happy:
    xpos (2/6) alpha 0.0
    pause 0.25
    ease 0.5 alpha 1.0

show gardenia uniform cocky:
    xpos (4/6) alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

show sabrina uniform behind gardenia:
    xpos (5/6) alpha 0.0
    pause 0.75
    ease 0.5 alpha 1.0

show skyla uniform:
    xpos 850 alpha 0.0
    pause 1.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.3 xpos 950
        ease 0.3 xpos 900
        pause 0.3
        ease 0.3 xpos 870
        ease 0.3 xpos 920
        
show text "{size=70}{b}?{/b}{/size}":
    xpos 1200 ypos 400 alpha 0.0 zoom 1.0
    pause 2.5
    parallel:
        ease 0.5 alpha 1.0
        pause 1.0
        ease 0.5 alpha 0.0
    parallel:
        ease 2.5 xpos 1120 ypos 300 rotate 30 zoom 1.5

$ renpy.pause(1.5, hard=True)

ethan "Man, this is a huge class.{w=0.75} I can actually recognize a few faces now!"

show flannery:
    xpos (1/6) alpha 1.0
    ease 0.5 alpha 0.0

show whitney:
    xpos (2/6) alpha 1.0
    ease 0.5 alpha 0.0

show gardenia:
    xpos (4/6) alpha 1.0
    ease 0.5 alpha 0.0

show sabrina:
    xpos (5/6) alpha 1.0
    ease 0.5 alpha 0.0

show skyla:
    xpos 920 alpha 1.0
    ease 0.5 alpha 0.0

show blue uniform:
    xpos 150 alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

red "Looks like [blue_name]'s sitting alone. Kinda surprising. I'd've thought he would have tried to surround himself with people by now."
ethan "You know that guy?"
red "Yeah. We have a history."
ethan @thinking "Oh, you dated?"
red @happy "Hah! No, I still have some dignity. Trust me, his personality is {i}not{/i} worth it."
ethan @happy "I dunno, I feel like my standards could learn to limbo for that guy..."

pause 1.0

red @angrybrow frownmouth "Ethan."
ethan @surprised "Uh? So serious, all of a sudden..."
red @thinking "I'm saying this in {i}full seriousness.{/i} Don't do that to yourself."
ethan "Alright! I'll take your word for it."

hide flannery
hide whitney
hide gardenia
hide sabrina
hide skyla
hide text

show blue:
    xpos 150 alpha 1.0
    ease 0.5 alpha 0.0

red "Anyway, let's go sit over by the gang.{w=0.5} Don't want to end up like Mr.-Too-Cool-For-Friends."

$ renpy.pause(1.0, hard=True)

hide blue

show bruno:
    xpos 200 alpha 0.0
    parallel:
        ease 1.25 xpos 450
    parallel:
        ease 0.75 alpha 1.0

show alder happy2 behind bruno with dis:
    xpos 0.75

alder "Yes, right. Settle down."

$ renpy.music.stop(channel='crowd', fadeout=1.5)

red "Are these guys our teachers?{w=0.5} The guy on the left definitely looks like one..."

show bruno think:
    xpos 450 alpha 1.0

ethan "But the other guy looks like one of those mountain hermits you hear about on TV."

$ BecomeNamed("Alder")
$ BecomeNamed("Bruno")
alder "Welcome to gym class!{w=0.5} I'm Alder and he's Bruno."
alder @happy2 "We'll be your instructors for this year."
alder "Now I bet you're all wondering what you'll actually be doing in this class.{w=0.5} Well, it'll be just like the other gym classes you've probably taken in your other schools."    
alder "Except we're not going to make you change into shorts and play sports.{w=0.5} In this school, we focus more on training Pokémon, not your bodies."    
alder happy2 "But training your body is important too, ha ha!"

pause 1.5

alder -happy2 "Ahem. Anyway, the real reason why this school has a gym class like this is to prepare you kids for the real Pokémon Gyms after you graduate.{w=0.5} At least for those interested in tackling the League."
alder "Can any of you tell me why Gyms exist in the first place?"

hide alder 
hide bruno 
with dis

show cheren uniform:
    xpos 770 alpha 0.0
    ease 0.5 alpha 1.0 xpos 720
        
show hilda uniform behind cheren:
    xpos 1250 alpha 0.0
    ease 0.5 alpha 1.0 xpos 1200
    
show serena uniform behind cheren:
    xpos 300 alpha 0.0
    ease 0.5 alpha 1.0 xpos 350

cheren "Gyms were created to weed out the skilled Trainers from the mediocre Trainers.{w=0.5} If we didn't have Gyms, any trainer could directly attempt to challenge the league, overwhelming its resources."
    
serena "Or perhaps they at least limit the number of people that think they'd make good Pokémon Trainers?"

hilda sad "Not from what I've seen..."

show hilda:
    alpha 1.0 xpos 1200
    ease 0.5 alpha 0.0
    
show cheren:
    alpha 1.0 xpos 720
    ease 0.5 alpha 0.0
        
show serena:
    alpha 1.0 xpos 350
    ease 0.5 alpha 0.0

show misty uniform angry:
    xpos 1150 alpha 0.0
    ease 0.5 xpos 1050 alpha 1.0

misty "That's dumb.{w=0.5} Gyms are just a pain in the ass."
show misty surprised with dis

show brendan uniform:
    xpos 350 alpha 0.0
    ease 0.5 xpos 450 alpha 1.0

brendan surprised "Nuh-uh! Do you even know how much bench press equipment costs?{w=0.5} You'd need to use that thing for like a decade before it starts paying for itself!"

misty angry "I'm talking about Pokémon Gyms, you idiot!"
    
show misty angry:
    alpha 1.0 xpos 1050
    ease 0.5 alpha 0.0
    
show brendan:
    alpha 1.0 xpos 450
    ease 0.5 alpha 0.0            

show alder with dis:
    xpos 0.75
        
show bruno:
    alpha 0.0 xpos 400
    ease 0.5 alpha 1.0 xpos 450

alder "Right, very good guesses...{w=0.5} but the main purpose of a Gym is to allow Trainers who are less experienced to test their skills against more experienced ones on even footing."

hide cheren
hide hilda
hide serena
hide brendan
hide misty

show alder happy2:
    xpos 0.66 alpha 1.0
    
show bruno:
    xpos 450 alpha 1.0

alder "And that is what we're going to be doing in this class."

show alder:
    alpha 1.0 xpos 0.75
    ease 1.0 xpos 0.5
    
show bruno:
    alpha 1.0 xpos 450
    ease 1.25 xpos 150

show leaf uniform:
    xpos 1400 alpha 0.0
    ease 0.5 xpos 1360 alpha 1.0

leaf "Wait, you're telling us we're gonna be Pokémon battling in this class?"

show leaf:
    xpos 1360 alpha 1.0

alder "Precisely! Everyone will have at least one battle a day. Though we won't be diving into that right away."

alder spunky2 "First, we need to review the basics.{w=0.5} You're all so busy trying to learn new things that sometimes you forget the most rudimentary skills."

leaf surprised "What, are you going to teach us how to catch Pokémon or something?"

show bruno think with dis
alder happy2 "Yes, that's a very important part of the curriculum!"

leaf sadmouth "Sheesh..."

show leaf:
    xpos 1360 alpha 1.0
    ease 0.5 xpos 1400 alpha 0.0

alder -happy2 "Even if some of you think you have everything you need to know about Pokémon battling, trust me when I say you don't."

alder happy2 "We've been in this field a lot longer than you have and even {i}we{/i} still don't have it down perfectly, ha ha!"
show alder happy with dis

hide leaf

show blue uniform angry:
    xpos 1400 alpha 0.0
    ease 0.5 alpha 1.0

redmind @thinking "As I expected, [blue_name] seems a bit irked by what Alder just said."
redmind @sad "I hope he doesn't make a scene like he did in homeroom."

hide blue with dis

show alder happy2:
    alpha 1.0 xpos 0.5
    ease 1.0 xpos 0.75
        
show bruno:
    alpha 1.0 xpos 150
    ease 1.25 xpos 450

alder -happy2 "Oh, excuse me for rambling on like that."        
alder "Uhhhh, Bruno!{w=0.5} Why don't you tell them more about this class?"
bruno think2 "Very well."

show bruno:
    xpos 450
    ease 1.0 xpos 900
    pause 0.25
    ease 0.75 xpos 300
    
bruno norm2 "This gym was first and foremost designed to be a training ground for students, and as such, it is available for free use after class hours."

bruno "Just bring your student ID and you receive unlimited access to its facilities."
bruno "In addition to the exercise machines available, the gym also contains several battle simulators to allow students to experience what a live Pokémon match would feel like in real-time."

show alder:
    alpha 1.0 xpos 0.75
    ease 1.0 xpos 0.5
    
show bruno:
    alpha 1.0 xpos 300
    ease 1.25 xpos 0

show calem uniform:
    xpos 1500 alpha 0.0
    ease 0.5 xpos 1450 alpha 1.0
    
calem "Excuse me, 'simulators?'{w=0.5} Are you're saying there {i}won't{/i} be any live Pokémon matches here?"
    
bruno @surprised2 "Incorrect. We will hold live matches every class. On your own time, you may also hold battles here, if you wish, but most take place in the Battle Hall."
bruno "However, the members of the Battle Team have priority to use the Battle Hall."

show calem:
    xpos 1450 alpha 1.0
    ease 0.5 xpos 1500 alpha 0.0
        
show blue:
    xpos 1450 alpha 0.0
    ease 0.5 xpos 1400 alpha 1.0

blue -angry "What's the Battle Team about?"

bruno "Our school has a competitive battling team for students who wish to take their Pokémon training to the next level."

bruno think "It's a very selective club, so don't think about signing up so quickly."

blue "Oh, yeah?{w=0.5} What does it take to get in there?"

bruno think2 "Impeccable grades. A strong team."

blue @talkingmouth "Ha! That's easy!"

bruno "I was not finished. You must also have the vote of your fellow team members. Finally, you must bring something to the team that no-one else does."

blue @happy "What, like being completely undefeated?"

alder norm2 "Be careful of what you say.{w=0.5} Arrogance and strength do not go hand in hand." 

blue @happy "I'm telling you, it'll be a piece of cake.{w=0.5} Who's in charge of the team?"

lance "I am."

show lance:
    xpos 1200 alpha 0.0 zoom 1.15
    pause 0.5
    ease 0.75 xpos 600 alpha 1.0 zoom 1.0


pause 1.5

hide calem

calem uniform @surprised "H-huh?"

red "Wait, who is this guy? He looks familiar."
$ BecomeNamed("Lance")
ethan @surprised "Dude! Don't you watch {i}any{/i} TV?! That's Lance! He's the Indigo League Champion! {i}Our{/i} League, dude!"
red @happy "Then I guess [blue_name] should watch his mouth around him."
    
lance @talkingmouth "Being accepted to the Battle Team is one of the highest honors a student can receive in this school.{w=0.5} It is not to be taken lightly."

bruno @norm2 "Lance.{w=0.5} How long have you been standing there?"

lance @talkingmouth "I was just passing by.{w=0.5} It's been a while, Bruno. Alder."

alder happy2 "Ha! It has indeed."

alder -happy2 "Oh, where are my manners?{w=0.5} Students, this is Lance, the advisor of the Battle Team."

lance @talkingmouth "Pleased to meet you all."
lance @thinking "So these are the new students that just came in?{w=0.5} They look quite capable."
lance @closedbrow talkingmouth "I expect great things from all of you.{w=0.5} When I was a new student at this school, I--"

show blue:
    xpos 1400
    ease 0.3 xpos 1350
    
blue cocky "Hey, you're the guy running the Battle Team?"

lance @angrybrow talkingmouth "...Yes. And you should heed the advice of Alder and Bruno."

show bruno think with dis

show blue angry with dis

lance @closedbrow talkingmouth "For someone currently at your level, it'd be impossible to get in."

show alder 

show blue:
    xpos 1350
    ease 0.5 xpos 1400
    
blue angry "...What did you say?"

redmind "Here we go..."
    
blue @talkingmouth "Just because you're some bigshot Champion doesn't mean you can look down on me!"

lance @closedbrow talkingmouth "I am not a 'bigshot Champion,' nor am I looking down on you.{w=0.5} I am simply stating the facts."

lance @talkingmouth "...Anyway, I'm in a hurry.{w=0.5} I have business to attend to and I cannot be late."

alder "All right. It was good seeing you again, Lance."
lance @talkingmouth "Likewise. Take care, Alder. Bruno."

show lance:
    alpha 1.0 xpos 600 zoom 1.0
    ease 0.75 alpha 0.0 xpos 1200 zoom 1.25

pause 0.5

blue angry "Is this guy really just gonna walk out without saying anything else?"

hide lance

red "He has to learn to take it easy one of these days..."

show blue:
    xpos 1400 alpha 1.0
    ease 0.5 xpos 1500 alpha 0.0

alder happy2 "You heard him!{w=0.5} The Battle Team is serious business!"

hide blue

alder "After all, it wasn't luck that our school has produced the most World Champions, Elite Four members, and holds the record for most wins at the National Tournament."
alder happy2 "You heard right!{w=0.5} The top students represent Kobukan Academy and face off against students from other schools during the Pokémon League season."

show bianca uniform happy:
    xpos 1450 alpha 0.0
    ease 0.5 xpos 1360 alpha 1.0

bianca "Oh, my gosh, that sounds sooooo cool! ♪"
bianca -happy "But I think I'd faint from stage fright if I had to do something like that in front of all those people!"
    
show cheren uniform thinking:
    xpos 1800 alpha 0.0
    ease 0.5 xpos 1680 alpha 1.0

cheren "You do know that you have to get {i}on{/i} the team first to even consider doing something like that, right?"

show bianca:
    xpos 1360 alpha 1.0
    ease 0.5 xpos 1160 alpha 0.0
        
show cheren:
    xpos 1680 alpha 1.0
    ease 0.5 xpos 1800 alpha 0.0

alder "But anyway, you shouldn't worry about things like that."
alder "There are much more important things to take care of, after all."

show bruno think with dis
alder happy2 "Like graduating on time, heh heh!"

pause 1.5

alder -happy2 "Hmm, I suppose we can move on to the weight machines.{w=0.5} Bruno, would you mind giving the students a little demo?"

bruno think2 "Not at all."

show bruno think:
    alpha 1.0
    ease 0.5 alpha 0.0
    
$ renpy.music.play("Audio/Weights.ogg", channel='misc', loop=True, fadein=1.0)

narrator "After about thirty minutes of watching Bruno go through every machine without breaking a sweat, you realize that maybe you should look after your body a bit more."
    
window hide
$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

alder happy2 "Okay, that's enough for one day, students."
show bruno think with dis

alder "Next class, we'll talk about the basics of Pokémon battling and how to deal with Pokémon in the wild."

show bruno with dis:
    alpha 1.0
    
bruno think2 "It'll be review, but don't underestimate the intricacies of the basics."

alder "Right.{w=0.5} Well then, so long, students! Enjoy the rest of your day."

hide alder
hide bruno
show blank2
with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_8

ethan "Looks like... next on our schedule is lunch! I gotta handle something at the office, so you head on without me, alright?"

red "Sure thing. Take care."

hide bruno
hide alder
hide shauna
hide bianca
hide cheren

window hide
stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

show cafe behind blank2
show afternoon at vspaz
    
pause 3.5

jump lunch010405