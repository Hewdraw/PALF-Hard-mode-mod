label secondhomeroom010416:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak "...needless to say, laws regarding the necessity of possessing Pokémon in the wild were quickly passed."
oak "After going outside without Pokémon became illegal, the mostly-rural population of the Kanto-Johto area quickly became a nation of Pokémon trainers. The culture then spread to essentially every major region."
oak "Some say the emperor's response to what was an isolated, if heartbreaking, tragedy was heavy-handed, but at the same time, our Pokémon-focused world nowadays is a direct result of his decisiveness."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak "Let us hope that we can all make the right decision when our moment to alter the future comes. For now, though, go home and enjoy the weekend!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

hide oakbg with dis

show may uniform with dis

may @talkingmouth "Hey! Brendan told me you're going to be battling Hilbert?"

red uniform @happy "Yep. Want to come watch?"

may @happy "Totally! I think the guys are already heading to the Battle Hall."

show leaf uniform at rightside with dis

leaf @happy "Room for one more?"

red @happy "Ooh, sorry. {i}Just{/i} sold out of tickets."

leaf @surprised "What?! But I'm a VIP! I get the corner box! The penthouse suite! The... The mint on the pillow!"

red @talking2mouth "Sorry, Ma'am. I'm not seeing your name on this list."

leaf @happy "Hah. You better look a bit harder. It might be under 'Queen Leaf III, Long May She Reign'?"
leaf @flirt "I'm actually Galarian. On the royal side."

red @thinking "Oh, my mistake. Yup, there you are."

leaf @talkingmouth "There we go." 

show may surprisedbrow with dis

leaf @flirt "I'll give you a big tip."

show may -surprisedbrow with dis

may @talkingmouth "Are... are you two dating?"

leaf @surprised "Uh... no."

$ relationship = GetRelationship("Leaf").lower()
red @talkingmouth "Yeah, no. Just [relationship]s."

may @talkingmouth "Oh. Okay."
may @happy "Sorry, guess that was a weird question, right? I'm going to go meet up with Brendan."

hide may with dis

show leaf:
    ease 0.5 xpos 0.5

pause 2.0

red @happy "Soooo..."

menu:
    "Want to go on a date?":
        show leaf fullblush angry with dis

        $ ValueChange("Leaf", -1, 0.5)

        leaf frownmouth @angry "H-hey! Cool it, mister! I've known you for, like, two weeks!"

        leaf @angrybrow talkingmouth "That's moving way, {i}way{/i} too fast. I don't think you're a jerk or a creep or anything, but I need to..."

        leaf @thinking "You know. Figure some stuff out. I'll let you know when {i}I'm{/i} ready."

        red @sadeyes sadeyebrows talking2mouth "My bad."

        pause 1.0

        leaf -frownmouth -fullblush @talking2mouth "It's alright. I can tell you meant it. I just... that earnestness is cute, but freaks me out."

        red @talking2mouth "Still. Sorry about that."

    "I'm out.":
        leaf @thinking "...{i}Are{/i} we dating?"

        red @talkingmouth "I think I'd know if we were."

        leaf @happy "Yeah, you're right."

pause 1.0

red @thinking "Looks like Hilbert's already left for the Battle Hall, then. Meet up with you there?"

leaf @talkingmouth "Sure. See you there."

call clearscreens from _call_clearscreens_54
show blank2 with splitfade
$ AddPikachu()
$ HealParty()

show stadium_empty behind blank2
show janine at rightside behind blank2
show lance at leftside behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg" 

pause 2.0

show screen currentdate
hide blank2 
with splitfade

redmind -uniform @happy "Hey, there's Janine!{w=0.5}{nw}"
extend @sad " ...And Lance."

lance @angry "{i}You.{/i}"

red @sadeyes sadeyebrows "Uh... hi, Si-"

show lance:
    ease 0.4 xpos 0.5 zoom 1.5 alpha 0.0 ypos 1.4

pause 0.2

red @surprised "Huh?"

play sound "Audio/Body Roll.ogg"

blue @surprised "Gah! What's the big idea?"

show lance:
    ease 1.0 xpos 0.25 zoom 1.0 alpha 1.0 ypos 1.0

show blue sad:
    alpha 0.0 zoom 1.5 ypos 1.4
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1.0

lance sadbrow @talkingmouth "I genuinely cannot tell whether I am angrier at you for trying to get into the Battle Hall by hiding behind another student, or for doing so poorly at it."

janine @talkingmouth "Yeah, you've got two feet of hair on this guy. You kinda stick out."

blue -sad frownmouth @talkingmouth "Look, I'm not here to cause any trouble. I just heard this guy was battling, and wanted to check it out."

janine @angry "What part of {i}banned{/i} do you not get? You are banned until the tryouts! That's three days from now. B{w=0.25}A{w=0.25}N{w=0.25}N{w=0.25}E{w=0.25}D."

blue @talkingmouth "You were willing to make an exception last week!"

janine @sad "Yeah, and see if you ever catch me doing that again."

lance @talkingmouth "I will say this simply. Begone from this place. You have stacked the deck so far against yourself that your entrance into the Battle Team now would be an absolute miracle. Remove yourself from the hole you're digging, and be gone."

janine @talkingmouth "I'll say it simpler:{w=0.5}{nw}"
extend @angry " Get lost."

pause 1.0

blue angry "Watch your back, [first_name]."

hide blue with dis

pause 1.0

lance @sad "If you continue to bring drama into this Battle Hall every time you wish to battle, [first_name], then I will ban {i}you{/i} from this location, as well."
lance @talkingmouth "Begin your battle and get out. You've tarried enough."

hide lance with dis

pause 2.0

show hilbert at leftside with dis

hilbert "Are you ready?"

red "Yep."

hilbert "Good. Let's begin."

redmind "Oh, look. There's Ethan, Brendan, Calem, and May, up in the bleachers!"

brendan "{size=50}Wooooo! You got this, bro!{/size}"
calem "{size=25}Wait, which one are you cheering for?{/size}"
ethan "{size=40}Dorm 151, rep-re-SENT!{/size}"
may "{size=40}Do your best, you two!{/size}"

$ HealParty()

$ hilbertcubchooobj = Pokemon(pokedexlookupname("Cubchoo", DexMacros.Id), level=11, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Icy Wind")], nature=Natures.Adamant, ability="Slush Rush")
$ hilberthonedgeobj = Pokemon(pokedexlookupname("Honedge", DexMacros.Id), level=11, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Shadow Sneak")], nature=Natures.Brave, ability="No Guard")
$ hilbertsnoruntobj = Pokemon(pokedexlookupname("Snorunt", DexMacros.Id), level=11, ivs=[24, 24, 24, 24, 24, 24], moves=[GetMove("Powder Snow")], gender=Genders.Female, nature=Natures.Modest, ability="Moody")

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("hilbert", TrainerType.Enemy, [hilbertcubchooobj, hilberthonedgeobj, hilbertsnoruntobj])

call Battle([trainer1, trainer2]) from _call_Battle_21
$ gymbattles["Hilbert1"]  = _return

show hilbert at centerside with dis

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=1.5)

pause 1.0

red @surprised "Hey, each of your Pokémon only used one move over and over! Do they actually listen to you?"

hilbert @talkingmouth "Not as such. Rather, I've made them forget all their moves except their most powerful."

red @happy "Hey, that's pretty clever! How did you do that?"

hilbert @smilemouth "I cannot explain it.{w=0.5} ...Forgetting has always come easily to me."

red @talkingmouth "Well, clearly, it worked. Good job."

if (WonBattle("Hilbert1")):
    hilbert @talkingmouth "Thank you. You've shown yourself to be a competent trainer, even without the obedience edge."
    hilbert @closedbrow talkingmouth "I'll lend you my Pokémon."
else:
    hilbert @sad "Your praises mean nothing, as the defeated. I will not be lending you my Pokémon."

show lance at leftside 
show janine surprised
with dis

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

lance @talkingmouth "What's this about lending Pokémon?"

hilbert @talkingmouth "We were battling to see if [first_name] could borrow my Pokémon for the upcoming Battle Team tryouts."

lance angry "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @sadeyes sadeyebrows frownmouth "Oh, man, he's pissed."

hide hilbert with dis

lance -angry @talkingmouth "Janine, did you recommend this young man borrow Pokémon to use for his application to the Battle Team?"

janine -surprised @talkingmouth "Yes, I did."

lance @angry "Despite the fact I had explicitly declared he will {i}not{/i} get onto the Battle Team?"

janine @talkingmouth "Technically, Sir, I wasn't there when you said that, so I couldn't be blamed for not knowing."

lance @sadbrow "One of the Team has told you by now, though. So, I repeat."

janine @talkingmouth "Yes, Sir. I think he could be an amazing asset in battle. We'd be able to sweep the Quarter Qlashes this year with him."

pause 1.0

lance @talkingmouth "Carry on."

janine @thinking "He doesn't need to have even used a Pokémon before in order to be in perfect sync with them." 
janine @happymouth "As long as he knows how to battle, and his Pokémon {i}are{/i} stronger, there's no fight he can't win."
janine @talkingmouth "We can't just leave him on the table, Sir."

pause 1.0

lance @talkingmouth "However. I declared that he {i}would not{/i} make it into the Battle Team."

janine @sad "Sir... you know I really respect you, but... at the end of the day..."

lance @closedbrow "It is the Captain's decision."

pause 2.0

lance @talkingmouth "It {i}is{/i} the Captain's decision. However. The terms of the battle tryouts are set by the faculty. And 'borrowed' Pokémon will not be permitted."

janine @surprised "Sir?!"

lance @closedbrow talkingmouth "I have said it; it is so."

pause 1.0

janine @talkingmouth "Will you permit the usage of a strength equalizer then, Sir?"

show lance sadbrow with dis

pause 2.0

lance @sadbrow talkingmouth "Fine. But sticking your neck out for this child will only serve to hurt you."

hide lance with dis

pause 2.0

brendan @happy "{size=50}Wooooo! Great battle, guys! {/size}Wait, where'd Hilbert go?"

janine @thinking "Hm... thinking, thinking, thinking... okay."

stop music channel "crowd" fadeout 0.5

janine @angry "Everyone out. Now."

pause 2.0

redmind @surprised "Woah. I've never seen a room empty so fast. She didn't even yell."

show janine:
    ease 0.5 xpos 0.5

janine @talkingmouth "Look at me."

red "Yes, Ma'am."

janine @thinking "And cut that out, I'm only twenty-one."

redmind "It's definitely more about how you present yourself than it is about your actual age."

janine @thinking "So, borrowing Pokémon is a bust, thanks to your dormmate."
janine @talkingmouth "But I got us a strength equalizer. That means, even if your opponents have much higher-level Pokémon, you'll all be fighting at the same level."

red @talking2mouth "But that doesn't cover movepools... or base stats, or items..."

janine thinking @talkingmouth "No. And you'll definitely be facing opponents who've been training a lot longer." 

pause 2.0

janine -thinking @talkingmouth "Alright, got it. You're going to go to Inspira tomorrow."

red @talkingmouth "Oh. Yes, I am! I was actually going to go there tomorrow with some friends."

janine @happy "Good. Go to the Pokémon Center, and use the PC there. As a registered trainer, I have access to the Pokémon Center's Pokémon storage database." 
janine @talkingmouth "Log in under the username xToxikxShadowx. Password is I<3Venonat. You--"

janine @angry "Write those down."

red @talkingmouth "Oh, okay!"

janine @talkingmouth "After you log in, create a new set of boxes for yourself. Then, go to the Pokémart in the same building, and buy as many Poké Balls as you can carry."

red @thinking "With you so far..."

janine @talkingmouth "Use those Poké Balls to catch a full team of six Pokémon. Your advantage is your ability to command multiple Pokémon at once." 
janine @talkingmouth "Your opponents might be stronger, but your best bet is to overwhelm them with sheer numbers."

red "Like when I battled [blue_name]... or that Absol."

janine @surprised "You fought an Absol? Huh. Anyway, yeah, exactly."

janine @sad "Most of your opponents will be using Pokémon around level 20 or so, before the strength equalizer. Expect to see a few evolved Pokémon. And, uh..."
janine @talkingmouth "Your biggest advantage? That your Pokémon listen to you right away? Expect that to go away. Around level 20 is when trainers can start commanding their Pokémon properly."

red @thinking "Geez. Guess the grace period is over, huh?"

janine @talkingmouth "Yeah."

red @happy "Thanks for doing all this for me, though. I really appreciate it."

janine @talkingmouth "You're worth it. If this Battle Team gets you... well, there's nothing stopping us from finally sweeping the National Tournament." 
janine @happy "And then I'll finally be free to try for Champion."

menu:
    "{color=#60c2f8}[[Wit] You want a dominating victory before you leave?":
        show janine surprised with dis

        $ TraitChange("Wit")

        janine -surprised @talkingmouth "Figured it out? Yeah. We've done well the last few years, but Kobukan deserves more than 'well.'"
        janine @happy "I really love this school. And nothing would make me happier than if it got what it deserved--a brutal crushing of our opponents, and a straight shot to the Kobukan Championship."
    
    "{color=#ff8412}[[Courage] I'm going to beat you there.":
        show janine surprised with dis

        $ TraitChange("Courage")

        janine -surprised @talkingmouth "Woah. Cocky, aren't you?"

        red @happy "Confident. I've heard that Kobukan doesn't even have a Champion right now. Seems like a good spot for me to fill."

        janine @happy "Well, I like your ambition. Keep that end-goal in mind."

        janine @smirkmouth "And don't be so disappointed when I hand you a crushingly brutal defeat."

red @happy "Is the brutality necessary?"

janine @smirkmouth "If we're going to spend some time together, there's something you're going to need to learn."

pause 1.0

show janine:
    ease 2.5 xpos 0.5 ypos 1.2 zoom 1.3

pause 1.0

janine @smirkmouth blush "I don't like only having a piece of something. I want it {i}all.{/i}" 

red @surprisedeyes surprisedeyebrows frownmouth "Un-- understood. Janine."

show janine:
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

janine @happy "Good."

janine @talkingmouth "Now get out of here. I've got some logistics to handle for the tryouts."

red @talkingmouth "See you Monday."

janine @sad "Mm."

call freeroam from _call_freeroam_4

call texting from _call_texting_5

jump day010417