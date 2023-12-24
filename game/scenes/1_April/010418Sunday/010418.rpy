label day010418:
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_13 

$ HealParty()

stop music

scene blank2
show morning at vspaz

pause 3.5

queue music "Audio/Music/Road to Viridian City.ogg"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red @happy "Good morning, world!"

hilbert @angry "It. {w=0.5}Is. {w=0.5}Seven. {w=0.5}Thirty."

red @surprisedeyes surprisedeyebrows talking2mouth "{size=25}Good morning, world.{w=0.5} Except Hilbert.{/size}"

show calem at leftside with dis

calem @talkingmouth "{size=25}Good morning, [first_name]. Are you occupied today?{/size}"

red @talkingmouth "{size=25}Why, something I can do for you?{/size}"

calem @talkingmouth "{size=25}Rather, I just wanted to make sure you didn't forget about your own attempts at the Student Council.{/size}"

red @thinking "{size=25}Nah, not at all! Actually, I think I made some good progress on that yesterday.{/size}"

calem @happy "{size=25}Splendid! What manner of progress?{/size}"

pause 1.0

red @talkingmouth "{size=25}...Uh, not sure. But progressive progress.{/size}"

calem @sad "{size=25}...I see. Well, do keep in mind there's only twelve days left.{/size}"

red @happy "{size=25}I'll mention it to everyone I talk to for the next two weeks.{/size}"

calem @thinking "{size=25}That would certainly help. But this is a school of several hundred. You'll need something with a bit more widespread impact.{/size}"

red @thinking "{size=25}Hm. I'll think on that, then. And if something comes up, I'll make sure to grab the bull in the china shop by the horns!{/size}"

calem @thinking "{size=25}I'm pretty sure that's not how the phrase goes.{/size}"

red @talkingmouth "{size=25}Well, I'll figure that out later! Right now, I'm on a mission from Janine herself. And I've got to train up [pika_name].{/size}"

calem surprised @happy "Godspeed."

hilbert angry "{size=40}That does it! Calem, I'm {i}sick{/i} and {i}tired{/i} of your--!"

scene hall_A with slideleft

play sound "audio/door_slam.mp3"

red @thinking "Sorry, Calem. Not going to stand there and feel the early-morning Hilbert fury."
red @sad "At least Flannery just yells at you. Hilbert breaks your soul..."

$ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry", loop=None)
pikachu sad "Pikachu..."

call freeroam from _call_freeroam_5

scene dorm_B norm with Dissolve(2.0)
    
stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

redmind "Hm. I don't have a whole lot of numbers in my phone, do I? I should probably see if I can get more numbers next week."
redmind @thinking "Man. So much to do. Studying, training, making friends, running for Student Council, trying to get on the Battle Team..."
redmind @thinking "Not to mention figuring out how to pay for school, reporting to Old Man Oak about Frienergy, and figuring out what the heck is up with Tia."

pause 1.0

redmind @happy "Well, I knew Kobukan was going to shove me through at light speed. I signed up for this."

pause 1.0

redmind @thinking "Kind of."

call afterroomsetuptexting from _call_afterroomsetuptexting_1

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_58

show blank2 with dis
    
$ renpy.pause(2.5, hard=True)

jump day010419