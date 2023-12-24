label day010415:

$ playerparty.remove(pikachuobj)
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_10

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak "And that concludes the lecture! Don't forget about the quiz coming up later today!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

oak "Unless I'm very much mistaken, you'll want to research the properties of defensive moves."

hide oakbg
show flannery uniform tired at farleftside
show whitney uniform sadbrow frownmouth at leftside
with dis

pause 1.0

redmind uniform @surprised "Woah. What's up with those two? They aren't looking so well."

red @happy "Hey, guys! Rough morning?"

show flannery surprised
show whitney surprised
with dis

pause 1.0

show flannery furious with dis:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

flannery "You asshole! You did this to us!"

red @surprised "Wh-what?! What are you talking about?!"

whitney -surprised frownmouth @talkingmouth "Flan, chill. I agreed to this."

flannery "Only 'cause he pressured you into it!"

whitney @closedbrow "He really didn't. And even if he tried, I handle pressure way better than, like... you."

show flannery surprised with dis:
    ease 0.3 ypos 1.0 zoom 1.0

flannery "What?! What're you saying?"

whitney @happy "I'm saying that a landmine handles pressure as well as you, girl. And would kill fewer people."

show flannery furious with vpunch:
    xpos 0.5

flannery "I AM THE PICTURE OF GRACE UNDER PRESSURE!"

whitney @thinking "Sorry, [first_name]. Bianca kept us up all night last night. She just got a laptop, and..."

flannery tired @tiredbrow talkingmouth "She thinks everything she sees on the internet is real. She keeps asking us how to... like, find the damn search engine she's already on."

whitney @closedbrow talkingmouth "I've seen eighty-year-olds who understand technology more than her."

flannery @tiredbrow talkingmouth "And she wants {i}everyone's{/i} opinion on everything she asks, so instead of just waking Whitney up every five minutes, she wakes all of us up."

red @sad "Geez. That sounds pretty rough. Can't you just tell her to stop?"

pause 2.0

whitney -frownmouth @happy "Well, we would, except it's really, really cute. I feel like Dorm 721 has just adopted a little sister."

flannery @thinking "Girl's just trying to learn. I can't get too mad at her for that. Not to her face, anyway."

menu:
    "{color=#b7669e}[[Charm] Thank you so much for your patience.":
        $ TraitChange("Charm")

        whitney @happy "Aw, it's no problem."

        flannery @angry "No, it {i}is{/i} a goddamn problem, and if you're going to drop this mystery girl on us and ask us not to ask any questions, you're going to make damn sure we get a good night's sleep in exchange."    

    "{color=#60c2f8}[[Wit] I'll see if I can get her to stop.":

        $ TraitChange("Wit")

        flannery @angry "Yeah, you'd better do a lot more than 'see if.' If you're going to drop this mystery girl on us and ask us not to ask any questions, you're going to make damn sure we get a good night's sleep in exchange."    

red @surprised "Uh... yes, Ma'am."

whitney @surprised "Uh... yeah, what Flan said. {size=25}Thanks, girl.{/size}"

flannery tired "Mmmph."

hide flannery with dis

show whitney with dis:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

whitney @happy "For real, though, anything you can do to make her act more like a person would be {i}really{/i} appreciated."

show whitney with dis:
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

red @talking2mouth "Hey. She {i}is{/i} a person. Maybe just a different kind of person." 
red @talkingmouth "All I can promise is I'm going to try and get her to wake you up less in the middle of the night."

whitney closedbrow frownmouth "Guess that'll have to do, then... I gotta go look after Bianca."

show whitney at dissolveaway:
    xpos 0.5

red @surprised "Oh, wait, hold up!"

show whitney at dissolvein

whitney -closedbrow "Mmyup?"

red @thinking "You know everyone, right? Do you know a girl named 'Gardenia?'"

if (persondex["Gardenia"]["Value"] <= 3):
    red @talkingmouth "I met her once or twice, but don't know a whole lot about her."
elif (classstats["Ghost"] > 6.5 and classstats["Grass"] > 6.5):
    red @talkingmouth "She's in my ghost and grass classes, but I've only seen her a couple times outside of class."
elif (classstats["Ghost"] > 6.5):
    red @talkingmouth "She's in my ghost class, but I've only seen her a couple times outside of class."
elif (classstats["Grass"] > 6.5):
    red @talkingmouth "She's in my grass class, but I've only seen her a couple times outside of class."
elif (persondex["Gardenia"]["Value"] > 3):
    red "I've actually met up with her quite a few times, but I'm just not sure where she spends her free time."

whitney -frownmouth @happy "Oh, you're totally in luck."
whitney @talkingmouth "She sits with me at lunch every day, obvi, but if you wanted to try and get her alone, she's usually at the baseball fields after school."
whitney @thinking "Flan and I are usually there as well, but... we can just, like, wander around in the outfield while you chat."

red @happy "Thanks a bunch. I'll do that."
red @confusedeyebrows talking2mouth "Also, you're, like, crazy good at taking this weird social stuff in stride."

whitney @happy "Shut up, dude, I know it."

jump homeroom1transition