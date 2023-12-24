label gardeniaevent:

if (not persondex["Gardenia"]["Named"]):
    narrator "You take this time to stretch your arms. In doing so, you inadvertently knock over a pencil."

    play sound "Audio/Body Roll.ogg"

    show gardeniaintro with vpunch

    red uniform surprised "Holy-! What a dive!"

    ethan uniform surprised "Woah, that girl was sitting two rows behind us!{w=0.5} How did she react that fast?"

    red "That was a nice catch!"

    hide gardeniaintro 
    show gardenia uniform
    with dis

    gardenia angrybrow "Thanks! But it was nothing."
    red happy "No, I'm serious! Your reaction time is insane.{w=0.5} I barely reacted myself."
    gardenia sadbrow frownmouth "Really?{w=0.5} You're training for the Pokémon League, aren't you?"
    gardenia @talkingmouth "This really isn't all that impressive."
    red -happy @closedeyes sadeyebrows "Oh. Uh..."
    gardenia happy "Nah, I'm just messing with you!{w=0.5} It's okay if your reflexes are a bit slow. There are plenty of other things to worry about in the big leagues anyway."
    show gardenia angrybrow -happymouth with dis

    red @thinking "You didn't have to go and say--"
    $ BecomeNamed("Gardenia")
    gardenia @surprisedbrow talkingmouth "Oh, my name's Gardenia! What's yours?"

    red "I'm [first_name]."

    gardenia @talking2mouth "Nice meeting you, [first_name]."
    gardenia @happybrow "Hey, if you ever want to buff up your skills, find me outside of class! I used to teach at a gym back in Eterna City."
    red @surprised "A Pokémon gym?"
    gardenia @surprised "Eh?"
    gardenia @happy "Oh, nah, sorry! Just a regular gym. I mean, I'm only eighteen. How'd I get a job at a gym, y'know?"
    red "Yeah, I guess that makes sense."

    pause 0.5

    gardenia surprised "Oh, looks like Teach is here! Catch ya later!"
    $ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")

    show gardenia:
        xpos 0.5 ypos 1.1 zoom 1.0 alpha 1.0
        ease 0.4 xpos -0.5 ypos 1.3 zoom 1.5 alpha 0.0

    narrator "Gardenia nimbly goes back{w=0.3}--or more like {i}jumps{/i} back--into her seat."

    pause 1.0

    hide gardenia

    ethan uniform @surprised "Hey... dude. Gardenia actually asked you to find her outside of class!"
    red @surprised "Yeah? What about it?"
    ethan @happy "That's an 'in', dude! Not only is it an 'in', she's practically lighting up the path!"
    ethan @angrybrow happymouth "She's waving those light-up things that they use at airports, dude! This is it!"
    red "Uh-huh. Well, I'll let you know how things go."

    pause 2.0

return