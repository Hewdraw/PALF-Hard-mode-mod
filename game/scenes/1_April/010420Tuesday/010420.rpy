label day010420:

$ excusesecondelective = False
$ excusesecondhomeroom = False

python:
    for mon in playerparty:
        if (mon.GetId() == 25):
            pikachuobj = mon
    playerparty.remove(pikachuobj)
    timeOfDay = "Morning"
call calendar(1) from _call_calendar_15

show morning at vspaz

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

redmind uniform @thinking "...Why are so many people missing from class today? It looks like one-fifth of the class is gone.{w=0.5} And what's that weird smell?"

oak "Hm! Lots of absences today. Perhaps there's something going around? Well, let's open a door, vent out the place."
oak "Nothing cures a bout of the 'downies' like fresh air!"

show leaf uniform with dis

leaf @talkingmouth "Open that door, and the stank'll get way worse, trust me. Old people, am I right?"

red @talkingmouth "He's not that old. Just... sixties, maybe?"

leaf @talking2mouth "You never asked?"

red @talking2mouth "I mean, I'm not sure it was ever relevant."

leaf @sarcastic "Uh-huh. But you asked the girl you met {size=25}crawling out of a meteor crater{/size} her age immediately."

red @closedbrow angrymouth "Oh my {i}god{/i}, give it a rest."

leaf @flirt "Sorry, sorry."

pause 1.0

leaf @talking2mouth "I actually just came over to tell you good job at the tryouts yesterday."
leaf @embarrassed "I would've texted you, but I was so tired Hilda pretty much had to carry me into bed."

if (WonBattle("Leaf1")):
    red @happy "Thanks. You put up a serious fight."
    leaf @happy "Ah, you're just saying that. You crushed me!"

else:
    red @happy "Ah, you're just saying that. You crushed me!"

leaf @surprised "Oh, speaking of crushing, what's up with that Sonia chick? She's scary strong."

if (GetRelationship("Nessa") == "Friend"):
    red @thinking "Nessa told me about her. She's apparently a Kobukan dropout from last year. Nessa said she ghosted everyone she knew and disappeared."

else:
    red @thinking "I have no idea. From what Janine said, I think she's a dropout from last year? Janine mentioned she ghosted the team."

leaf @thinking "Geez. Wonder why?"

red @talkingmouth "Maybe the pressure just got too much for her?"

leaf @sarcastic "Maybe, but that's boring."
leaf @talkingmouth "Until I hear otherwise, I'm going to put my money on her discovering the Battle Team is actually, like, hugely corrupt and evil, and she ditched it until she was strong enough to take it down from the inside."

red @happy "I guess that'd be a more interesting story."

leaf @talking2mouth "Yeah. Well, even if it {i}is{/i} evil, I hope I get in."
leaf @thinking "The support and resources of the Battle Team would really help when it comes to the Quarter Qlashes."

red @thinking "Right. When are those, again?"

leaf @talkingmouth "The first one starts May 5th."

red @surprised "Seriously? That's pretty soon."

leaf @talkingmouth "Yeah. And you might just get matched up against someone you totally can't beat, like Janine."

red @thinking "Is Lance participating in the QQs?"

leaf @talking2mouth "Hm... I don't know. He's already a Champion of two regions. After winning Kanto and Johto, Kobukan kinda feels like small potatoes. Might be beneath his notice."

red @closedbrow talking2mouth "Man, I hope so."

oak "Ahem! Anything you two would care to share with the class?"

leaf surprised "Oops! Gotta go!"

hide leaf with dis

jump homeroom1transition