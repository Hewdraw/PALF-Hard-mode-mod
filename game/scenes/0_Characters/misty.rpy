init python:
    def MistyHasUnseenScene():
        if (GetCharValue("Misty") >= 10 and personalstats["Courage"] >= 7 and GetRelationship("Misty") != "Jerk"):
            return "Misty1"
        return False

label Misty1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Misty"]["Events"].append("Level2SceneVer2")

scene pool 
show misty
with Dissolve(2.0)
queue music "Audio/Music/CeruleanCity.mp3"

red @happy "Hi."

show misty surprised with dis

pause 1.0

misty -surprised @sadmouth "What do you want?"

red @thinking "Hmm... to become a Pokémon Champion, mostly."

misty @angry "Yeah, good luck with that. You can do that somewhere else, can't you?"

red @happy "Probably, but I thought it might be more fun to do it in your company."

misty sweat @surprised "Huh? Something wrong with you? I'm not exactly pleasant company."

red @closedbrow talking2mouth "{size=25}Well, I can't deny that...{/size}"
red @thinking "But I thought maybe I could do something to help you out. And then you might be... uh..."

pause 1.0

misty -sweat @sad "Less of a bitch?"

red @closedbrow talking2mouth "I was going to say 'more comfortable around me.'"

if (not IsBefore(1, 5, 2004)):
    misty @surprised "What, you're still on about the whole mind control thing?"

    misty @closedbrow talkingmouth "Give it a rest. I already know you don't have that thing. You told the entire school, remember?"

    red @talkingmouth "Do I ever. But I didn't mean that kind of 'more comfortable.' I just meant, like, generally."

misty closedbrow @talking2mouth "Whatever. I don't even know what you could do for me, anyway."

red @happy "Then you're in luck, because I totally do!"

misty -closedbrow @surprised "Oh, this'll be good. What is it?"

red @thinking "Well, I've been thinking about your Psyduck, ever since we battled in Gym Class."

misty @sad "...Yeah? What about him?"

red @talkingmouth "I was thinking I might be able to help you make him listen to you."

if (IsBefore(1, 5, 2004)):
    misty @talkingmouth "Oh, what, like you're some kinda Pokémon whisperer?"
else:
    misty @closedbrow "Oh, yeah, that was one of your powers or whatever, wasn't it? You're a Pokémon whisperer."

red @closedbrow talking2mouth "Well... I don't talk to them, but I am pretty good with them, yeah."

if (IsBefore(1, 5, 2004)):
    $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
    pikachu happy_2 "Pika!"
else:
    $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
    libpikachu happy "Pika!"

red @happy "Thanks for the support, bud."

misty @closedbrow talkingmouth "Well, fine. What are you going to do?"

red @talkingmouth "Would you mind sending out your Psyduck?"

play sound "audio/Pokemon/Ball sound.ogg"
queue sound "audio/Pokemon/Cries/54.wav"

$ sidemonnum = pokedexlookupname("Psyduck", DexMacros.Id)

show sideportraitfull at dormdesk, pokeball
show misty:
    easein 0.5 xpos 0.75

"{color=#c4a300}Psyduck{/color}" "Psy?"

red @thinking "Hey, little man! How're you doing?"

queue sound "audio/Pokemon/Cries/54.wav"

"{color=#c4a300}Psyduck{/color}" "Psy-ai-ai!"

red @happy "Really? Wow. To shreds, you say?"

red @thinking "And how's her bike holding up?"

"{color=#c4a300}Psyduck{/color}" "Psy."

red @thinking "Really? Wow. To shreds, you say?"

show sideportraitfull:
    ease 0.5 xpos 0.75 ypos 1.1 zoom 0.8 xzoom 1
    pause 0.5
    parallel:
        ease 1.0 xpos .65
        ease 1.0 xpos .75
        ease 1.0 xpos 0.85
        ease 1.0 xpos 0.75
        repeat
    parallel:
        pause 0.8
        ease 0.2 xzoom -1
        pause 1.0
        pause 0.8
        ease 0.2 xzoom 1
        pause 1.0
        repeat
    parallel:
        pause 1.2
        ease 0.2 ypos 1.07
        ease 0.2 ypos 1.1
        repeat

misty @surprised "Uh... are you {i}actually{/i} talking to my Psyduck?"

red @happy "Nah, just messing with you."

misty @angry "Ugh! Get serious, you jerk!"

red @happy "Sorry, sorry."

pause 1.0

misty @sad "Well? What's wrong with him?"

pause 1.0

red @thinking "I mean... I'm not a doctor or a psychologist or anything. Professor Oak would actually be the perfect person to talk to about this."
red @thinking "He's a Poké-homo Psychosociologist, after all. Human-Pokémon relationships are literally his field of study."
red @talking2mouth "But, if I were to give my best guess, Psyduck feels like you don't love him."

pause 1.0

misty @angry "Dummy! That's exactly what Alder said! If you're not going to tell me anything useful or new, what are you even doing here?"

red @thinking "That's not exactly what Alder said. Alder said you don't give your Psyduck enough attention. But I've been hanging out with you for a while, and I'm not sure that's entirely correct."

misty @surprised "Huh?"

red @talking2mouth "Misty, I think you {i}do{/i} give your Pokémon attention. But I don't think it's positive attention."

misty @surprised "What?"

red @closedbrow talking2mouth "Maybe I'm making some assumptions here, but you {i}do{/i} love your Pokémon, right?"

misty @angry "Of... of course! I'm a bitch, not {i}evil{/i}."

red @thinking "I really wish you wouldn't call yourself that. But that's not the point. The point is, well..."
red @talkingmouth "Misty, do you treat your Pokémon, even a little bit, like you treat people?"

pause 1.0

show misty sadbrow with dis

misty @sadmouth "I..."

pause 1.0

red @thinking "Pokémon tend to act very still and quiet around me. They usually just sit at my feet and wait for my orders. But what's your Psyduck doing?"

misty @angry "Just... running around randomly?"

red @talkingmouth "Not exactly."

misty @closedbrow talkingmouth "Fine, what?"

red @happy "How about you walk over here?"

misty @angry "What kind of dumb game is this?"

red @sadbrow talkingmouth "Humor me?"

misty @closedbrow talkingmouth "Ugh... fine."

show misty:
    ease 1.0 xpos 0.25

pause 2.0

show sideportraitfull:
    ease 0.2 xzoom 1
    pause 1.0
    ease 0.2 ypos 1.05
    ease 0.2 ypos 1.1
    parallel:
        ease 1.0 xpos .15
        ease 1.0 xpos .25
        ease 1.0 xpos 0.35
        ease 1.0 xpos 0.25
        repeat
    parallel:
        pause 0.8
        ease 0.2 xzoom -1
        pause 1.0
        pause 0.8
        ease 0.2 xzoom 1
        pause 1.0
        repeat
    parallel:
        pause 1.2
        ease 0.2 ypos 1.07
        ease 0.2 ypos 1.1
        repeat

pause 2.0

red @happy "See?"

misty @talkingmouth "He's... following me?"

red @talkingmouth "He's showing off."

misty @surprised "Huh?"

red @happy "Your Psyduck is going through its paces. It's shadowboxing, it's working on its footing."

red @talking2mouth "It's trying to show you that it'll fight for you. I mean, it lets itself out of its own Poké Ball--so it can {i}literally{/i} fight for you."

red @talking2mouth "Yeah, it might look a bit silly, like it's bouncing around aimlessly, but there's a thinking brain, and a feeling heart, in that duck."

pause 1.0

play sound "audio/Pokemon/Cries/54.wav"
queue sound "audio/Pokemon/Ball sound.ogg"

show sideportraitfull at backinpokeball:
    zoom 0.8

pause 2.5

show misty:
    ease 0.5 xpos 0.5

misty @talking2mouth "Oh."

red @thinking "Misty, you know that your attitude drives people away. And that's fine, I'm sure you've got a reason for not wanting anyone to get close to you. But you can't do that to your Pokémon. They're innocent."

misty @sad "{size=30}I mean, so are you...{/size}"

pause 1.0

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @closedbrow talking2mouth "That's another thing. {w=0.5}{nw}"

show misty surprised with dis

extend "People can hear you when you mutter under your breath."

misty "Wha-{w=0.5}wha-{w=0.5}wha-{w=0.5}"

red @confused "C'mon. You know people can. So you're, like, trying to let people know you don't {i}actually{/i} hate them. But you feel like you can't do it outright, for some reason."

misty -surprised @closedbrow "Mmmmph."

pause 1.0

misty @angry "You... jerk! Dummy! Idiot! What are you even doing here? Just walking into my life and telling me I need to change who I am?!"

red @thinking "No. I'm telling you you need to {i}show{/i} who you are."

misty @talkingmouth "Or what?"

red @confused "...Well, you'll, uh, have a pretty hard time making friends. I mean, maybe you don't care about that, but... I think you do? Correct me if I'm wrong."

misty @angry "You're wrong! Wrong, wrong, very wrong!"

red @happy "Ah, alright, then! My bad."

call clearscreens from _call_clearscreens_59

show misty surprised with dis

show blank2 with Dissolve(2.0)

hide blank2

show screen currentdate

misty sadbrow @sad "W-wait!"

red @confused "Yeah?"

pause 1.0

misty @sad "Uh... what if... Like, what if you weren't completely wrong? What do I do to fix this? {w=0.5}{size=30}To fix me?{/size}"

pause 1.0

red @happy "Oh, I have no idea."

misty @angry "Wha--well, what good are you?!"

red @talkingmouth "Look, I'm not a therapist. Whatever's made you feel like you need to be hostile and argumentative all the time isn't something I can figure out in a twenty-minute chat."

pause 1.0

red @confused "Scratch that, a thirty-minute chat. Wow, we've really been going on at it, haven't we?"

pause 1.0

misty @talkingmouth "...Why do you know all this? All this stuff about me? And about how I treat people?"
misty @sad "I've been trying to put my problem into words for... years. Ever since I was a child. But you just walked in here and told me what was wrong."

red @thinking "Well... you're kinda like your Psyduck, I think."

misty @surprised "Huh?"

red @thinking "You know. Acting out for attention."

misty @angry "Hey!"

red @talkingmouth "It reminds me of an old friend of mine. He felt like he had to do more and more outrageous things to stand out."

$ ValueChange("Blue", 3, -0.5)

red @thinking "Actually, I think I get him a bit more now... He definitely wanted his grandpa's attention."
red @thinking "So... is there anyone out there whose attention you're specifically trying to get?"

pause 1.0

misty @closedbrow talking2mouth "God, this is so stupid."
misty @talkingmouth "Look, my parents--"

red @surprised "Wait! Hold on! I have something for this."

pause 1.0

red glasses @talkingmouth "Dr. [last_name] is ready."

pause 1.0

misty @talkingmouth "Where did you get those?"

red @happy "Bianca gave them to me. She had some extras."

pause 1.0

misty angry "UGH! You {i}idiot!{/i} I thought you were going to take me seriously, but you're just making a big joke out of this, like everyone else!"

misty "You... {w=0.7}{nw}"

show blank2 behind pool

play sound "Audio/Slap.ogg"
pause 0.1

show misty:
    xpos 0.5 ypos 1.0 zoom 1.0 rotate 0
    ease 0.2 xpos 0.25 ypos 1.1 zoom 1.33 rotate -3

show pool at hall_move1

extend "jerk!{w=1.0}{nw}"

show misty:
    xpos 0.25 ypos 1.1 zoom 1.33 rotate -3
    ease 0.4 xpos -0.5 ypos 1.0 zoom 1.25 rotate 0

show pool at hall_move2

red @thinking "...Okay. Yeah, that one was a little on me. Maybe not the time for a bad joke."

show misty:
    ease 0.5 xpos 0.25

misty @angry "When you feel like taking me {i}seriously{/i}, give me a call, you {nw}"

play sound "Audio/Slap.ogg"

show misty angry:
    xpos 0.25 ypos 1.0 zoom 1.0 rotate 0
    ease 0.2 xpos 0.5 ypos 1.1 zoom 1.33 rotate -3

show pool at hall_move1

extend "{color=#0048ff}jerk{/color}!{w=1.0}{nw}"

show misty angry:
    xpos 0.5 ypos 1.1 zoom 1.33 rotate -3
    ease 0.4 xpos 1.5 ypos 1.0 zoom 1.25 rotate 0

show pool at hall_move2

red @angry "Now, see, that-- {size=40}{i}that{/i} was excessive!{/size}"

pause 1.0

redmind @confused "What did she just throw at me...?"

$ BecomeContacted("Misty")

redmind @closedbrow talking2mouth "Of course."

$ persondex["Misty"]["Relationship"] = "Jerk"
$ persondex["Misty"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Misty evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Jerk{/color}'!"

pause 2.0

red @talkingmouth "...Damn, I look good in glasses. Shame I can't see anything."

return