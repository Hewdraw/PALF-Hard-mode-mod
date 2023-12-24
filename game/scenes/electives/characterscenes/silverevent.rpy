label silverevent:

if (persondex["Silver"]["ClassesKnown"] == [] and calDate.day <= 7 and calDate.month == 4):
    narrator "You spot a familiar student and go to greet him."
    
    show silver uniform with dis

    pause 0.5

    red uniform happy "Hi ho, Silver!"

    silver angry "Piss off."
    silver surprised "Wait, it's you!"
    silver thinking "Wait, that shouldn't matter."
    silver sad "...Hi."

    red confusedeyebrows "That was... a rollercoaster."

    silver closedbrow @talkingmouth "Yeah, I'm still working on... everything."

    red "I didn't know you were a student here."

    silver "Yeah, well, I am."

    red "Right. Well, see you around."

    silver sad "Yeah."
    silver surprised "Uh... thanks."
    silver -surprised "For talking to me."
    silver sad "..."
    silver "I know it's, uh, it's difficult to get through the first five seconds of a conversation with me. But I appreciate that you've, uh, done it. A few times."

    red "Hey, anytime."

    silver "Uh... yeah. That's all. Bye."

    hide silver with dis

    pause 2.0

    hide silver

return