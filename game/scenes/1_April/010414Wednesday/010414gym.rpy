label gym010414:

############################################################################################################################################################################################################################
#### 3. GYM: BATTLE DEMO ###################################################################################################################################################################################################
############################################################################################################################################################################################################################    

$ HealParty()

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

alder "...And that, I believe, is the end of the lecture!"

pause 1.0

alder norm @norm2 "Bruno, do you have a partner for [first_name]?"

bruno happy @happy2 "Yes. Miss, please come here."

red uniform "Huh? Bruno looks... uncharacteristically happy. Wait, is he {i}blushing?{/i}"

hide alder
hide bruno 
with dis

show nessa uniform with dis

pause 1.0

if (not persondex["Nessa"]["Named"]):
    red uniform happy "Hi there! Don't think we've met. Nessa, right?"

    nessa @talkingmouth "Yeah. What's up?"

    red "I was thinking you looked kinda familiar. Have I seen you somewhere?"

    nessa @closedbrow "Maybe. I've been a model for a few magazines."

    red "Oh, is that right? I'm [first_name]."

    $ BecomeNamed("Nessa")
    nessa @talkingmouth "Nessa, but I often went under other names. I was a minor until recently, so, you know. Privacy concerns."

    red "Sure, sure. So how come a model like you is here at Kobukan?"
    red surprised "Ah, shit, that wasn't rude, was it?" 
    red -surprised "I just meant that you've already got a career path, and at such a young age, you know?"

    nessa happy "It's cool."
    nessa -happy "..."
    nessa thinking "I think... I'm here because I'm afraid it won't last."

    red "..."

    nessa "You know how water erodes rocks over millions of years? Time does the same thing to beauty. Which I guess doesn't sound very modest."
    nessa happy "Sorry, not sorry. I know I'm hot."
    nessa sad "But, you know, I'm not going to have what I have now forever. So I need a backup plan."

    red "Makes a lot of sense."

    nessa happy "Besides, I always had an interest in Pokémon. I was actually on my way to get my first Pokémon when a recruiter saw me in the street."
    nessa -happy "After the guy talked to my parents, we went back down to the beach and I caught my Drednaw. Back then, I figured that modeling would be something I'd do to fund my Pokémon career..."
    nessa "And now it's the opposite."
    nessa happy "Heh."
    nessa -happy "You're a good listener. You're probably only tolerating me 'cause I'm gorgeous, but, hey, thanks anyway."

    red happy "Hey, if I'm going to beat you in battle, I want to know who I'm beating."

    nessa @talkingmouth "Confident, aren't you? That's good."

    nessa @closedbrow "..."
    nessa "Look, I'm going to be really busy this year, so I don't have time for anything serious, but if you ask me on a date, I'll say yes."

    red "Cool. I'm not going to ask you in the classroom, though."

    nessa @talking2mouth "Thank god. Do {i}not{/i} want to associate this place with dates."

    $ BecomeContacted("Nessa")

    nessa @talkingmouth "When you have some free time, just call me. I'm free whenever."

else:
    red @happy "Hey, Nessa!"

    nessa @talkingmouth "Hey. Good to see you. Noticed you haven't invited me out on that date yet."

    red @sadeyes sadeyebrows happymouth "Uh... would you be offended if I said I've been really busy?"

    nessa @talkingmouth "Nah, I get it. Just keep it in mind."

red @thinking "Of course. But battles now, dates later, right?" 

nessa @happy "Got a good set of priorities there. I appreciate it."

red @happy "I gotta admit, I'm a bit scared of facing you. Not looking forward to fighting that Drednaw of yours."

nessa @talkingmouth "I'm not going to be using her in this battle."

red @surprised "Really? Isn't Drednaw a really powerful Pokémon, though?"

nessa @talkingmouth "Yeah. So I need to get the rest of my team to her level."

red @thinking "Don't you want to have the best chance of winning, though?"

nessa frownmouth @sad "...What would winning get me? We learn more from losing."

red @talkingmouth "Well, uh... in my personal experience, people like you more if you're a tough opponent who gives them a good battle."

nessa @thinking "Yeah, I guess so. Well, I'm not going to tryhard this."

redmind @thinking "What's up with her...? It feels like she doesn't even care if she wins or loses." 
redmind @thinking "If she doesn't care about people liking her more... but she basically asked me out on a date..."
redmind @thinking "What does this all mean?"

nessa @talkingmouth "Hey. You still with us?"

red @thinking "Yeah, I guess. Alright. Let's, uh, battle..."
redmind @thinking "Somehow, she's sucked all the fun out of this..."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("nessa", TrainerType.Enemy,
    [Pokemon(222, level=10, nature=Natures.Bold, gender=Genders.Female, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Healing Spring"), GetMove("Ancient Power"), GetMove("Bubble Beam"), GetMove("Recover")], ability="Regenerator")])#corsola

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_16
$ gymbattles["Nessa1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside 
show bruno think at leftside
show nessa uniform at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Nessa1")):
    nessa @talkingmouth "Mm. Good job. You're pretty tough."

    $ ValueChange("Nessa", 1, 0.75)

else:
    nessa @sad "Huh. Thought you'd win that one."

red uniform @confusedeyebrows talking2mouth "...That's it?"

nessa @talkingmouth "What do you mean?"

red @thinking "I mean... a battle's a back-and-forth. It's all about passion, and fire, and emotions!"
red @sadeyebrows sadeyes talkingmouth "But, uh... you don't seem to care. Before, or after."

red @surprised "Wait, do you not like Pokémon, or battles?" 

if (persondex["Dawn"]["Named"]):
    red @surprised "Are there {i}two{/i} people like that in this school?"

nessa @talkingmouth "No, battles are fun. I like Pokémon, too. I wanted to be a trainer before I wanted to be a model, remember."
nessa @thinking "Hm... how to explain this..."
nessa @happy "Oh, I know. So, you know how I mentioned how water erodes rock over millions of years?"

red @thinking "Yeah?"

nessa @sad "Well, that's how I see... everything?"

red @surprised "Huh?"

nessa @talkingmouth "Yeah. Everything. The only run that matters is the long-run. So what if I win or lose this battle? It's not even graded."

red @confusedeyebrows talkingmouth "I think... I'm confused."

nessa @talkingmouth "That's fine. It doesn't matter." 
nessa @happy "Try not to take everything so seriously. You'll give yourself wrinkles."
nessa @happy "We can talk more during our date, I guess."

jump lunchtransition