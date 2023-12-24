label sabrinaevent:

if (not persondex["Sabrina"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show sabrina uniform with dis

    pause 0.5

    red uniform happy "Hi there!"

    pause 1.0

    sabrina ".{w=0.25}.{w=0.25}.{w=0.25}"

    red -happy "Um... hello?"

    sabrina @talkingmouth "You want to know who I am."
    
    red "Uh, yeah."

    $ BecomeNamed("Sabrina")
    sabrina "Sabrina."

    red happy "Nice to meet you, Sabrina."

    sabrina ".{w=0.25}.{w=0.25}.{w=0.25}"
    sabrina @talkingmouth "You have what you want. You may go now."

    red -happy "Uh... alright. See ya!"

    play sound "Audio/Wood Fall Small.ogg"
    pause 1.0

    red "Oh, whoops. Dropped my... pencil...?"

    window hide

    pause 1.0

    show pencil2:
        alpha 0.0 xpos 200 ypos 800 zoom 0.75 rotate 20
        parallel:
            ease 0.25 rotate -20 ypos 650
            pause 0.25
            ease 0.25 rotate 20 ypos 550
            pause 0.25
            repeat
        parallel:
            ease 0.75 xpos 600 zoom 1.0
            pause 0.5
            ease 0.75 xpos 900 zoom 1.2
        parallel:
            ease 0.5 alpha 1.0

    $ renpy.pause(2.0, hard=True)

    show pencil2:
        ease 0.5 alpha 1.0 xpos 900 ypos 550 rotate 20 zoom 1.2
        parallel:
            ease 0.25 rotate -20
            pause 0.25
            ease 0.25 rotate 20
            pause 0.25
            repeat
        parallel:
            ease 0.66 xpos 870 ypos 620
            ease 0.66 xpos 930 ypos 500
            repeat
        parallel:
            ease 0.5 zoom 1.4

    red "Wha--"

    red "Uh... do you have an Abra or something? Wait, {i}you're{/i} not doing this, are you?"

    window hide
    pause 1.0

    red surprised "Oh my god, you totally are."

    show pencil2:
        zoom 1.4
        parallel:
            ease 0.25 rotate -20
            pause 0.25
            ease 0.25 rotate 20
            pause 0.25
            repeat
        parallel:
            ease 0.66 xpos 870 ypos 620
            ease 0.66 xpos 930 ypos 500
            repeat
        parallel:
            ease 1.0 zoom 2.0

    pause 1.5

    sabrina @talkingmouth "...You dropped this."

    red "Oh-oh.{w=0.5} That's my.{w=0.25}.{w=0.25}.{w=0.25} my pencil."

    pause 1.5

    sabrina @talkingmouth ".{w=0.25}.{w=0.25}.Yes. We've established that."

    pause 1.5
    show sabrina closedbrow
    pause 2.0

    sabrina @talkingmouth "...Well?{w=0.5} You want it back. Take it."

    red "Yes!{w=0.3} Sorry!{w=0.3} Thank you... um... Sabrina."

    show pencil2:
        alpha 1.0 zoom 2.0
        parallel:
            ease 0.25 rotate -20
            pause 0.25
            ease 0.25 rotate 20
            pause 0.25
            repeat
        parallel:
            ease 0.66 xpos 870 ypos 620
            ease 0.66 xpos 930 ypos 500
            repeat
        parallel:
            ease 0.7 alpha 0.0

    sabrina -closedbrow "...What?"

    hide pencil2

    red "How are you... able to do that?"
    
    sabrina "...You don't want to know."

    red "I really do."

    sabrina closedbrow "No, you don't. You're trying to figure out how to shift the conversation to you telling me your name."
    sabrina -closedbrow "Unnecessary. It's [first_name] [last_name]."

    red "Uh... yeah. Hey, have you been reading my mind?"

    sabrina "Obviously."

    red thinking "Hm. Kinda feel like that's a violation of my privacy?"

    sabrina @talkingmouth "You figure out a way to make me stop, and I will."

    red surprised "Wait, so it's not up to you? You can't stop reading minds?"

    sabrina @talkingmouth "Yes."

    redmind "Crap, so I really need to be careful what I think around her..."

    sabrina @talkingmouth "Yes."

    red "Oh, shit. Uh, forgive me for this!"

    pause 2.0

    sabrina @closedbrow "...What, are you expecting me to call you a pervert?"

    red thinking "I mean, it'd be fair..."

    sabrina @talkingmouth "Hmph. It's not your fault. It's natural."

    red surprised "Really? That's... uh, that's really understanding of you."

    sabrina closedbrow "I understand people more than anyone else. I wish I could stop."

    pause 2.0

    sabrina -closedbrow "Don't you dare think that."

    red surprised "What?"

    sabrina uniformpowered poweredbrow "You can't help me. No-one can."

    red sad "You're... just giving up?"

    sabrina @talkingmouth "...Allow me to make a correction. Stay away from me. {i}That's{/i} how you can help."

    hide sabrina with dis

    pause 1.0

    redmind @angrybrow happymouth "...Of course, a future Champion isn't giving up that easily."

return