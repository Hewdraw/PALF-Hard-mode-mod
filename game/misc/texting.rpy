init python:
    def GetDialog(speaker):
        if (speaker == "Leaf"):
            if (IsBefore(5, 5, 2004)):
                if ("RejectedConfession" in persondex["Leaf"]["Events"]):
                    return "hey, [first_name]. still hitting me up late at night? knew you couldnt leave me"
                elif ("AcceptedConfession" in persondex["Leaf"]["Events"]):
                    return "looking forward to our date! i hope youre ready for my date outfit. might be a bit too scandalous, but idc. ;3"
                else:
                    return "hitting me up late at night? ;3 im onto you."
            else:
                if (GetMood("Leaf") < 0):
                    return "you could just yell, you know. im right here."
                else:
                    if ("RejectedConfession" in persondex["Leaf"]["Events"]):
                        return "dude, what? im literally outside your room. i think u might be a tiny bit obsessive, ngl.\njk"
                    elif ("AcceptedConfession" in persondex["Leaf"]["Events"]):
                        return "dude, what? im literally outside your room. i think u might be a tiny bit obsessive, ngl.\n(xox)"
        elif (speaker == "Serena"):
            if (IsBefore(5, 5, 2004)):
                if (GetRelationship("Serena") == "Conspirator"):
                    return "Oh, delightful. You've come to update me on your mission regarding Calem, yes? Please, do tell."
                else:
                    return "What a splendid surprise. To what do I owe this pleasure?"
            else:
                if (GetMood("Serena") < 0):
                    return "Apologies, I don't think I can be very entertaining right now."
                else:
                    return "What a splendid surprise. To what do I owe this pleasure?"
        elif (speaker == "Calem"):
            if (IsBefore(5, 5, 2004)):
                return "Why are you texting me, [first_name]?\nI'm literally right here."
            else:
                if (GetMood("Calem") < 0):
                    return "[first_name]. I'm very sorry to say this, but I can't spend too much time talking. Serena is trying to discuss something."
                else:
                    return "[first_name]. Good to hear from you. This reminds me of when we were roommates."
        elif (speaker == "Brendan"):
            if (IsBefore(5, 5, 2004)):
                return "BRO, YOUR TEXTNG ME WHILE WERE IN THE SAME ROOM??? WACK"
            else:
                if (GetMood("Brendan") < 0):
                    return "NGL DUDE BAD TIME. TALK LATER???"
                else:
                    return "HEY BRO LONG TIME NO TALK MAYBE. I DONT REMEMBER"
        elif (speaker == "May"):
            lowername = first_name.lower()
            if (IsBefore(5, 5, 2004)):
                return "{}? its pretty late. whats up???".format(lowername)
            else:
                if (GetMood("May") < 0):
                    return "sorry, im kinda talking with Brendan right now... mind waiting a bit???"
                else:
                    return "{}? its pretty late. whats up???".format(lowername)
        elif (speaker == "Nate"):
            firstinitial = first_name[0]
            if (IsBefore(5, 5, 2004)):
                return "Heya, {}! It's past 2200! L8 to bed 2nite? Just touching base?".format(firstinitial)
            else:
                if (GetMood("Nate") < 0):
                    return "{}, sorry, don't really have time 2 talk rn. Got some stuff 2do. Catch u l8r?".format(firstinitial)
                else:
                    return "Heya, {}! It's past 2200! L8 to bed 2nite? Just touching base?".format(firstinitial)    
        elif (speaker == "Nessa"):#Nessa is not affected by mood at night
            if (GetRelationship("Nessa") == "Friend"):
                return "hi, [first_name]. pretty late. should let you know i dont give out 'spicy' texts before the second date, but if you just wanna chat, im down."
            else:
                return "sorry, i dont text before the first date. hurry up and take me out, k?"
        elif (speaker == "Sabrina"):
            if (IsBefore(5, 5, 2004)):
                return "It's nice to hear from you again. How was your day?"
            else:
                return "YOU SHOULD NOT BE HERE"
        elif (speaker == "Blue"):
            if (IsBefore(5, 5, 2004)):
                return "wat the hel's your PROLBEM? I was IN THE MIDLDE of trainin! you were probly gonna BEG me for tips, huh? tough! ill BLOKC this number!\n*PROBLEM"
            else:
                return "I'm in the other goddamn room, you idiot! Just {i}yell!{/i}"
        elif (speaker == "Hilda"):
            if (IsBefore(5, 5, 2004)):
                if (GetRelationship("Hilda") == "Friend"): 
                    return "orz, bz. ttyl, k?"
                else:
                    return "So, got some free time. Thanks to you. But you better quit that spit! I can handle myself!\n*shit!"
            else:
                if (GetMood("Hilda") < 0 or GetRelationshipRank("Hilda") < 1):
                    return "orz, bz. ttyl, k?"
                else:
                    return "So, got some free time. Thanks to you. But you better quit that spit! I can handle myself!\n*shit!"
        elif (speaker == "Misty"):#always moody
            return "yeah so i kinda just want to be left alone rn.\ni guess we can text, but don't send/ask for any pics, perv."
        elif (speaker == "Bea"):#always stoic
            return "{cps=15}Hi.{w=1.0} How are you?{w=1.0} What do you mean, {w=1.0}I text slowly?{/cps}"
        elif (speaker == "Bianca"):#always cheerful
            return "hiiii!!!~ how was your day??? today was so fun for me!!! I got up and then went to class---oh but i had breakfast first, and then i went to class,,, and---"
        elif (speaker == "Gardenia"):#always business
            return "What're you looking for? Big deal$? Ma$$ive $aving$? Hot $ingle$ in your area? I got it all!"

label texting():

if (IsBefore(5, 5, 2004)):
    scene dorm_B norm with Dissolve(2.0)
else:
    scene bedroommidnight with Dissolve(2.0)
    
stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

if (IsBefore(5, 5, 2004)):
    redmind "...I should text someone before I head to bed."
else:
    redmind night "...I should text someone before I head to bed."

label afterroomsetuptexting():

show phone_B behind blank2
show phone_A behind blank2
with fadeinbottom

python:
    triggergardenia = False
    if (not persondex["Gardenia"]["Contact"] and not IsBefore(25, 4, 2004)):
        for item in elementitems.keys():
            if (GetNumItems(item) > 0):
                triggergardenia = True
            for mon in playerparty + box:
                if (mon.Item == item):
                    triggergardenia = True

if (triggergardenia):
    show phone_B
    show phone_A
    show gardenia behind phone_A:
        zoom 0.95
    with fadeinbottom

    gardenia @happy "Hey, partner!"

    red @confused "Huh? Gardenia? How'd you get this number?"

    gardenia @talking2mouth "Oh, I paid Nate to tell me!"

    red @closedbrow talking2mouth "I really need to have a talk with Nate about how callous he is about other people's personal information."

    gardenia @talkingmouth "Yeah, it's pretty awful of him. {w=0.5}{nw}"
    extend @happy "Anyway! A little birdie told me that you recently acquired a certain item in one of your elective classes!"
    gardenia @angrybrow happymouth "And that set off my 'ooh, business opportunity' sense."
    
    red @confused "Is this about investing in the city stores?"

    if (investment == 0):
        gardenia @talkingmouth "No, but you {i}should{/i} do that."
    else:
        gardenia @happy "No, but I appreciate your support in that regard!"

    gardenia @talking2mouth "I've got some 'independent merchants' in the city who sell official Pokémon League items under the table."
    gardenia @talkingmouth "Nothing wrong with them--they just don't pass inspection, or fall off trucks, or are surplus goods, or whatever."
    gardenia @happy "Anyway, those guys have been looking to expand their product lines to some less mass-produced items, the kind we can get in our elective classes pretty easily."

    red @talkingmouth "[bluecolor]So you want me to make these items in my elective classes and sell them to you,{/color} so you can re-sell them to some shady black market people?"

    gardenia @talking2mouth "Pretty much, yup!"

    red @confused "Do you have... {i}any{/i} money-making plans that aren't some flavor of illegal?"

    gardenia @angrybrow happymouth "Uh, yeah. My gym classes. But you aren't signing up for them!"

    red @sweat closedbrow happymouth "Fair enough."

    gardenia @talkingmouth "So, I obviously {i}want{/i} you to sell this stuff to me, but, in the interest of fair play, I should probably tell you what else you can do with 'em."

    red @confused "Just... like, give them to my Pokémon in battle, right?"

    gardenia @talking2mouth "That's one thing. [bluecolor]But don't forget you can gift them to people, as well.{/color}"

    red @thinking "Huh."

    gardenia @happy "Giving people gifts to make them like you! Classic. Never fails."
    gardenia @talkingmouth "[bluecolor]Oh, but don't give anyone more than one gift a week.{/color} That'll just seem desperate, and people can smell desperation."

    red @confused "Noted."
    red @thinking "[bluecolor]So, if I wanted to sell items, I should meet up with you in the Baseball field, right?{/color}"

    gardenia @talking2mouth "That's right. Same place you'd go to make investments."

    red @talkingmouth "And what about if I wanted to give these items as gifts?"

    gardenia @happy "Just find whoever you're trying to give the gift to during your free time and hand it off. Quick and easy. Doesn't even take any time."

    red @talkingmouth "Cool. Thanks for the, uh, business advice."

    $ ValueChange("Gardenia", 3, 0.5)

    gardenia @happy "Yeah, I'll be sending you my consultant's fee in the morning. Ta-ta!"

    hide phone_B
    hide phone_A
    hide gardenia
    with fadeoutbottom

    pause 1.0

    red @thinking "I really hope she's joking."

    $ BecomeContacted("Gardenia")

    show blank2 with Dissolve(2.0)

else:
    call screen phoneinterface(_with_none=False)
    with dissolve

    $ interaction = _return
    if (interaction == "Back"):
        narrator "You don't want to text anyone? Going to sleep early will confer no benefit right now."

        menu:
            "Yes, just go to sleep.":
                pass

            "No, I do.":
                jump texting
        
    else:
        if (interaction != "Sabrina"):
            $ interactionsprite = interaction.lower()
            if (interaction == "Professor Cherry"):
                $ interactionsprite = "kris"
            
            $ renpy.show(interactionsprite, at_list=[dissolvein, Transform(zoom=0.8, ypos=0.95)], behind=["phone_A"])

            narrator "You want to text [interaction]?"

            menu:
                "Yes, text [interaction].":
                    if (interaction == "Blue" and not IsBefore(1, 5, 2004)):
                        pause 1.0

                        narrator "Silence, at first, and then..."

                        show bedroommidnight with vpunch

                        blue night @angry "I'm in the other goddamn room, you idiot! Just yell!"

                        $ ValueChange(interaction, 1, 0.5)

                        if (IsDate(6, 5, 2004)):
                            narrator "You spent some time yelling at Blue, but then..."

                            hide phone_A
                            hide phone_B
                            hide phone_C
                            $ renpy.hide(interactionsprite)
                            with dis

                        else:
                            narrator "You spent some time yelling at [interaction] before drifting off to sleep."

                        call clearscreens from _call_clearscreens_84

                    else:
                        $ GetSmilePortrait(interactionsprite)

                        red @happy "Just thought I'd text. How're you doing?"

                        $ renpy.say("{color=" + getCharColor(interaction) + "}" + interaction, GetDialog(interaction))
                        
                        $ ValueChange(interaction, 1, 0.5)

                        if (IsDate(6, 5, 2004)):
                            narrator "You spent some time texting [interaction], but then..."

                            hide phone_A
                            hide phone_B
                            hide phone_C
                            $ renpy.hide(interactionsprite)
                            with dis

                        else:
                            narrator "You spent some time texting [interaction] before drifting off to sleep."

                        call clearscreens from _call_clearscreens_52

                "Nevermind.":
                    python:
                        renpy.hide(interactionsprite)
                        renpy.jump("texting")

        else:
            narrator "You want to think about Sabrina?"

            menu:
                "Yes, open your mind to her.":
                    if (not IsBefore(5, 5, 2004) and IsBefore(16, 5, 2004)):
                        narrator "The comforting whisper of Sabrina's telepathy, which you've gotten so used to..."

                        pause 1.0

                        narrator "Is completely absent."

                        jump texting

                    hide phone_B
                    hide phone_A
                    with fadeoutbottom

                    $ dialog = GetDialog("Sabrina")
                    redmind @happy "Just thought I'd check in. How're you doing?"
                    redmind "{color=#600080}[dialog]{/color}"

                    $ ValueChange("Sabrina", 1, 0.5)

                    narrator "You spent some time thinking back and forth with Sabrina before drifting off to sleep."
                    
                "Nevermind.":
                    python:
                        renpy.hide(interactionsprite)
                        renpy.jump("texting")

return