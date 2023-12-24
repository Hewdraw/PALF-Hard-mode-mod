label gym010407:

$ timeOfDay = "Noon"

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

show alder norm2:
    xpos 0.66 alpha 0.0
    ease 0.75 alpha 1.0

show bruno think:
    xpos 450 alpha 0.0
    pause 0.25
    ease 0.75 alpha 1.0

alder "...And that, I think, should conclude the lecture! I expect to see you use what you learned in class today."
alder -norm2 @happy2 "Now, let's get right into the battles. Bruno, if you'd go to each student and tell them who their assigned partner is?"

bruno "Yes."

hide bruno
hide alder
with dis

show ethan uniform with dis

ethan @thinking "So... that's how it works, huh? I hope I get someone I can beat."

hide bruno
hide alder

if (WonBattle("Blue1")):
    ethan @happy "Think you can keep your winning streak going?"
else:
    ethan @happy "Now's your chance to redeem yourself after yesterday!"

red uniform @talkingmouth "I'm definitely going to try."

ethan "Well, good luck!"

hide ethan with dis
show bruno at leftside with dis
show cheren uniform at rightside with dis

bruno "This'll be your partner. Each of you are to use one Pokémon. The match will end when one of you no longer has a Pokémon that can battle."

hide bruno at leftside with dis

cheren @happy "It's a pleasure to battle you."

cheren @angrybrow happymouth "Let's add a little wager to this battle, to make it more interesting."

if (council_campaigning):
    cheren @happy "Whoever wins has to spend an hour campaigning for the other in the Student Council elections. How does that sound?"

    red @happy "Sounds good. I could do with another vote."

else:
    cheren @happy "If I win, you'll spend an hour campaigning for me in the Student Council elections. Does that sound fine?"

    red @angrybrow frownmouth "Sure. But if {i}I{/i} win, I get to be the headmaster of the shadow government that secretly controls you."
    
    cheren @surprised "Er...?"

    red @happy "Just kidding. Good luck, future SC Prez. But I'm going to win."

cheren @angrybrow happymouth "Let's not be so cocky, [first_name]. Back home in Aspertia, many people thought I'd take the position of Gym Leader when the old one retired."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("cheren", TrainerType.Enemy, [Pokemon(509, gender=Genders.Female, ivs=[24, 24, 24, 24, 24, 0], nature=Natures.Brave, moves=[GetMove("Fake Out"), GetMove("Scratch"), GetMove("Sand Attack"), GetMove("Growl")], ability="Prankster")])#Purrloin

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_4
$ gymbattles["Cheren1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm3 at centerside with dis
show bruno think at leftside with dis
show cheren uniform at rightside with dis

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Cheren1")):
    cheren @sad "Ah, it seems I made a few tactical errors..."

    red uniform @happy "Ah, don't worry about it. At this level, battles are basically a coin flip!"

else:
    cheren @happy "Well done, Purrloin. Your victory was well-deserved."

    red uniform @happy "Hey, don't forget to give yourself some credit!"

cheren @smilemouth "Thank you. This was a very satisfying battle. I look forward to our rematch, soon."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show bruno think with dis
alder happy2 "That'll be all for today.{w=0.5} Enjoy the rest of your day!"
show alder norm with dis

show blank2 with dis:
    alpha 1.0

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_25

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

jump lunch010407