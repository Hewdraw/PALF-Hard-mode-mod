label gym010429:

############################################################################################################################################################################################################################
#### 3. GYM: BATTLE DEMO ###################################################################################################################################################################################################
############################################################################################################################################################################################################################    

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 450

alder @norm2 "The way you use items in battles matters a lot!"
alder @happy2 "However, the most valuable items, the kinds of items that are used in the highest tiers of competitive battling, can't typically be found in common Pokémarts."
alder @norm2 "Since TMs are expensive and rare, [bluecolor]as you advance in your type elective classes, your instructors will expand the list of moves they can teach you.{/color}"
alder @norm4 "Some are original techniques, and some are well-known moves that Champions have used."
alder @spunky2 "As for other items... Life Orbs, Choice Items, Eviolites... well, some of them can be earned as rewards for performing well in various school events. You might just have to borrow or get the rest from your classmates, though."
alder @norm2 "That's what you youngsters call 'friends with benefits,' right?"

pause 2.0

alder -spunky2 @angry2 "...I sense I've misused a slang term."

bruno @norm2 "Let's move onto the battles."

pause 0.5

bruno @happy2 "[first_name], try to only battle one trainer today." 

red uniform @sweat happy "Heh heh. Oops."

bruno @norm2 "Your assigned partner is Silver."

hide bruno
hide alder
with dis

if (GetRelationship("Silver") == "Friend"):
    show silver uniform smilemouth with dis 

    red @talkingmouth "Hey, friend."

    silver @talkingmouth "Hey, [first_name]."

else:
    show silver uniform with dis
    
    silver @closedbrow talkingmouth "Hey, red."

    red @talkingmouth "Hey, red."

red @talkingmouth "How's being on the Battle Team?"

silver @talkingmouth "Been alright so far. Didn't think I'd get in."

silver @closedbrow talkingmouth "Probably wouldn't have if Janine wasn't so desperate to get {i}you{/i} in."

red @confused "Lance isn't harrassing you too much, is he?"

silver @sad "He's barely talked to me since I got in."

red @surprised "Really? But, during the battle exhibition, you were the one who yelled at him in front of the whole school."

silver @happymouth "Yeah."

pause 1.0

silver @happymouth "Honestly, I think he respected that. You can hate a guy while still respecting them."

red @closedbrow talking2mouth "Boy, can you ever."

silver @sad "He said I {i}also{/i} wouldn't get on the Battle Team... but I guess he forgot about me after you told him we were getting in anyway."
silver @closedbrow talkingmouth "It's fine. Flying under the radar is safe."

red @talkingmouth "This coming from the guy who yelled at a two-time national champ on his fourth day of school."

silver @talkingmouth "Flying low is safer. I never said I was a good pilot."

red @talkingmouth "You might want to talk to Skyla about that."

pause 1.0

silver @angry "Do {i}not{/i} get me started on her."

if (GetRelationship("Skyla") == "Wingman"):
    red @happy sweat "Ah. Right. I forgot about your... contentious relationship."
else:
    red @surprised "Oh. Okay. There's clearly a story there."

pause 1.0

silver @talkingmouth "You remember what I asked you to do when you got elected?"

red @talkingmouth "Yeah. Stop Cheren from repealing curfew."

pause 0.5

silver @talkingmouth "I'm still going to help you get elected. So say whatever you want. But are you going to do that?"

menu:
    "The curfew needs to go.":
        $ AddEvent("Silver", "RejectedCurfewRequest")
        $ ValueChange("Silver", -1, 0.5)

        silver @closedbrow talkingmouth "Ugh... that'll make my job much harder. But I get it. It's not your problem."

    "Yes.":
        $ AddEvent("Silver", "AcceptedCurfewRequest")
        $ ValueChange("Silver", 3, 0.5)

        silver @talkingmouth "Thanks. I know this isn't your problem, so I appreciate you, uh, sticking your neck out for me like this."

red @talkingmouth "About that thing you're going to do to help me get elected, though... could I have any hints as to what it is?"

silver @talkingmouth "No. You can't be expecting it, or it won't work."

red @closedbrow sweat happymouth "Alright. If you say so."

pause 1.0

red @talkingmouth "So. Battle time?"

silver angrybrow happymouth "Get dunked on, nerd."

python:
    trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)

    silverskorupiobj.UpdateLevel(14, updateMoves=False)
    silverstunkyobj.UpdateLevel(14)
    silverstunkyobj.UpdateMoves(["Bad Breath", "Acid Spray", "Bite", "Fury Swipes"])
    silvergrimerobj = Pokemon(88.1, level=14, moves=[GetMove("Bad Breath"), GetMove("Bite"), GetMove("Acid Spray"), GetMove("Pound")], ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Adamant, gender=Genders.Female, ability="Power of Alchemy")
    silverscraggyobj = Pokemon("Scraggy", level=14, moves=[GetMove("Headbutt"),GetMove("Rock Smash"),GetMove("Feint Attack"),GetMove("Payback")], ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Jolly, gender=Genders.Male, ability="Intimidate")
    silvercroagunkobj = Pokemon("Croagunk", level=14, moves=[GetMove("Rock Smash"), GetMove("Poison Sting"), GetMove("Mud-Slap"), GetMove("Astonish")], ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Jolly, gender=Genders.Male, ability="Poison Touch")
    silversneaselobj = Pokemon("Sneasel", level=14, moves=[GetMove("Feint Attack"),GetMove("Icy Wind"),GetMove("Quick Attack")], ivs=[24, 24, 24, 24, 24, 24], nature=Natures.Jolly, gender=Genders.Male, ability="Pickpocket")

    silverparty = [silverskorupiobj, silverstunkyobj, silverscraggyobj, silversneaselobj, silvergrimerobj, silvercroagunkobj]

    trainer2 = Trainer("silver", TrainerType.Enemy, silverparty, number=2)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_67
$ gymbattles["Silver3"]  = _return

show alder norm at leftside with dis
show bruno think at centerside with dis
show silver uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

red @surprised "Woah!"

silver @surprisedbrow "What?"

red @happy "Silver, you've got six Pokémon! That's kinda a lot, isn't it?"

silver @thinking "Oh. Yeah... These, are, uh, they're not all mine."

pause 1.0

silver @angry "I didn't steal them!"

pause 0.5

silver @closedbrow talkingmouth "Some of my Dad's employees aren't... aren't great trainers. So I train their Pokémon up for them. Actually, I'm training these guys up for something later this week."

red @talkingmouth "Oh, seriously? So, which of these are actually {i}your{/i} Pokémon?"

pause 0.5

silver @closedbrow happymouth "Heh. None of them."

if (GetRelationship("Silver") == "Friend"):

    show silver:
        xpos 0.75
        ease 0.5 ypos 1.2 zoom 1.3

    silver @happymouth "[first_name], I have a {i}Crobat.{/i}"

    red @surprised "Woah."

    silver @talkingmouth "Yeah. People say Zubat are trash, but with the right attention, any Zubat can become a super-fast hard-hitting infiltrator."

    silver @angrybrow happymouth "It's amazing what trash can do when given the chance."

    silver @happy "Just blink. That's all he needs to take you out. One single blink and my boy can..."

    pause 0.5

    show silver:
        xpos 0.75
        ease 0.5 ypos 1.0 zoom 1.0

    silver @closedbrow "Anyway. I'm pretty strong."

else:
    silver @happymouth "You can't handle {i}my{/i} team yet, believe me. I'm pretty strong."

if (WonBattle("Silver3")):
    silver @talkingmouth "You're pretty strong, too, though. I mean, you {i}did{/i} just beat me."

    $ ValueChange("Silver", 3, 0.75)

    silver @talkingmouth "Keep it up. I want to show you my real team some day."

else:
    silver @talkingmouth "If you want me to bring out my real team, I'm going to need you to be tougher, though."

    red @confused "I'm working on it!"

    silver @smilemouth "Good."

jump lunchtransition