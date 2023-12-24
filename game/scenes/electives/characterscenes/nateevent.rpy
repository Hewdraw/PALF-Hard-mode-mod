label nateevent:

if (not persondex["Nate"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet him."
    
    show nate uniform with dis

    pause 0.5

    red uniform happy "Hi there!"

    nate happy "Oh, hey! Nice hat."

    red -happy "Thanks! I got it from--"

    nate surprised "Hold it!"

    pause 1.5

    red surprised "Um... okay? For how long?"

    nate thinking "About... seven more words, I'd say?"

    red @angrybrow "Seven more words? What does that mean?"

    nate happy "{size=30}Locked on.{/size} Southwest Kanto!"

    red -surprised @surprised "Huh?!"

    nate "I'm right, right?"

    red "I mean... yeah. I lived in Pallet Town my whole life. And I got the hat from there. Well, I mean, I actually got it from Old Man Oak, but he lives there too, so..."
    red @surprised "Wait, that doesn't matter. How'd you know?"

    nate -happy "I'm pretty good at reading accents! As soon as you said 'hi there,' I knew you had to be from Kanto, but I couldn't tell where until I had a bit more to go off of."

    red "Cool. Is that useful?"

    nate happy sweat "Not at all! It's a neat party trick, though."

    red "Well, it {i}is{/i} pretty neat. What's your name? I'm [first_name]."

    $ BecomeNamed("Nate")
    nate -sweat "Nate!"

    red "So how'd you end up with that ability?"

    nate -happy "Oh, I've lived all over. Military mom, you know. Guess you could call me inter-Nate-ional!"

    pause 1.0

    red @sad "No pun intended?"

    nate angry "What? Hell no! I intend every one of my puns."
    nate "Puns are the most valid form of humor out there! Only cowards don't intend their puns!"

    red happymouth "Interesting perspective. Not sure I agree, but, hey, whatever floats your boat."

    nate happy "Water, mostly!"

    play sound "Audio/vibrate.ogg"
    pause 1.5

    nate surprised "Oop, gotta go handle something. Seeya, [first_name]!"
    show nate happy with dis

    red "See you around."

    hide nate with dis

    pause 2.0

    hide nate

return