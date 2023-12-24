label ethanevent:
    show ethan uniform at centerside with dis

    if (getTotalElectives() == 0):
        show ethan uniform at centerside with dis
        red surprised uniform "Huh?! Ethan!"
        ethan "Huh. Hey, [first_name]."
        red happy "Good to see you! Crazy we both chose the same first elective, huh?"
        ethan @happy "Yeah, kinda wild."
        red -happy "This seat taken?"
        ethan @talkingmouth "Go ahead."
        hide ethan with dis

    elif (getTotalElectives() == 1):
        show ethan uniform at centerside with dis
        red surprised uniform "Huh. We're in the same class?"
        ethan @sadbrow "Looks like it. Small world?"
        red happy "Smaller than I thought!"
        ethan @happy "Well, I'll never turn down more you. Wanna sit here?"
        red -happy "Don't mind if I do."
        hide ethan with dis

    elif (getTotalElectives() == 2):
        show ethan uniform at centerside with dis
        red surprised uniform "We're... in the same class again."
        ethan @thinking "Yeah... well, come on and sit here, I guess."
        red -surprised "Sure."
        hide ethan with dis

    elif (getTotalElectives() == 3):
        show ethan uniform at centerside with dis
        red uniform "Hey, Ethan. Again."
        ethan @thinking "The odds of this are... so incredibly small, it's hard to describe."
        red "Yeah. But there's something going on here that beats the odds, obviously."
        hide ethan with dis

    elif (getTotalElectives() == 4):
        show ethan uniform at centerside with dis
        red uniform "Hey, Ethan."
        ethan "Let's, uh, let's just pretend there's nothing weird about this from now on."
        red @thinking "Yeah, I don't want to go through this every day for the rest of the year."
        hide ethan with dis

    else:
        show ethan uniform at centerside with dis
        red happy uniform "Hey, Ethan!"
        ethan happy "[first_name]! Good to see ya. Let's get this done!"
        hide ethan with dis

    pause 1.0

    hide ethan
    
    return