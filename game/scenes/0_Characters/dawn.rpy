init python:
    def DawnHasUnseenScene():
        if (GetCharValue("Dawn") >= 10 and GetRelationship("Dawn") != "Muse"):
            return "Dawn1"
        return False

label Dawn1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Dawn"]["Events"].append("Level2SceneVer2")

scene lobby 
show dawn thinking
with Dissolve(2.0)
$ renpy.music.queue("Audio/Music/snowpoint.mp3", channel='music')

if (IsBefore(1, 5, 2004)):
    redmind @thinking "Okay, there's Dawn. From what I know of her, she handles pressure about as well as a frozen-over pond, so I should do my best to not startle her."
else:
    redmind @thinking "Okay, there's Dawn. Despite how crazy strong she is, she handles pressure about as well as a frozen-over pond, so I should do my best to not startle her."

red @happy "{size=30}Hi.{/size}"

show lobby at vpunch

dawn frownmouth @surprised "A-ah! [first_name]! I didn't see you there."

redmind @thinking "Well, I tried."

red @talkingmouth "You looked like you were pretty deep in your thoughts. Penny for one of them?"

dawn @sadbrow happymouth "Oh. Just, um... thinking about Pokémon. Y'know, same as always."

red @happy "Really? That's so cool! So was I!"

dawn @angrybrow sadmouth "Wait, you couldn't tell I was lying there?"

red @surprised "Why would you lie? You're my friend."

show lobby at vpunch

dawn surprised "We're f-friends?! I'm sorry, this is all moving way too fast! I- I- I-"

show lobby with vpunch

dawn closedbrow angrymouth "{size=40}I need to go!{/size}"

show dawn:
    ease 0.5 xpos 1.5

redmind "...Hm."

$ rantolounge = False

menu:
    ">Run after her.":
        $ rantolounge = True
        scene lounge with splitfadefaster

        show dawn surprised with dis

        dawn "Ah-ah...!"

        red @talking2mouth "Why are you running?"

        dawn "Ahhhh!"

        red @angrybrow talking2mouth "{i}Why{/i} are you running?"

        dawn sad "I...{w=0.5} I...{w=0.5} I don't knoooow!"

    ">Wait for her to come back.":

        redmind ".{w=0.5}.{w=0.5}.{w=0.5}"

        pause 2.0

        show dawn frownmouth:
            ease 1.5 xpos 0.75

    ">Call out to her.":
        red "Wait, Dawn. Please. I'm just trying to talk with you. I can slow things down."

        pause 2.0

        show dawn frownmouth:
            ease 1.5 xpos 0.75

red @sadeyes sadeyebrows happymouth "C'mon. Let's talk, Dawn. Just talk. It doesn't have to be about Pokémon."

if (not IsBefore(1, 5, 2004)):
    red @happy "I mean, I'm {i}dying{/i} to find out what's the whole deal with your Mega Altaria--and the fact you {i}fought Cynthia?!{/i}"

    pause 1.0

    red @sweat sadbrow talkingmouth "But... I mean, from our battle in the Quarter Qlash's third round, it's pretty clear that that might not be an easy topic."

red @happy "Though I'm pretty bad at talking about anything that {i}isn't{/i} about Pokémon, fair warning."

dawn -sad frownmouth @closedbrow "{size=30}You and {i}everyone{/i} else.{/size}"

red @talking2mouth "...Mind if I ask the obvious question?"

dawn @closedbrow "No..."

red @thinking "How come you don't like Pokémon?"

dawn @sadbrow happymouth "I don't know. I don't {i}dislike{/i} them. And the ones I have, I love. They're my best friends."

red @talking2mouth "I sense a large 'but' approaching."

dawn @sad "Yeah. But everything that makes other people excited about them, I just don't get. Contests are fine. Battles are fine."

if (not IsBefore(23, 4, 2004) and IsBefore(1, 5, 2004)):
    dawn @sad "I mean, even though Janine's forced me into the Battle Team... I don't really hate that, even."

dawn @sadbrow happymouth "But none of that feels... like 'it,' for me. None of that's what I want to do with my life."

red @surprised "You're here in Kobukan, though?"

dawn @sad "Yeah, my mother, Johanna, is a pretty famous contest star in Sinnoh. She... doesn't like what I spend my free time doing. She was hoping that Kobukan might change my mind about Pokémon."

red @thinking "Hm. What do you spend your free time doing?"

show dawn sad with dis

pause 1.0

red @surprised "Woah, hey, you don't have to tell me! I mean, if it's embarrassing or something."

dawn -sad frownmouth @sadbrow happymouth "I... I don't know. I kinda want to tell {i}someone,{/i} but right now, nobody at Kobukan knows except Instructor Melony."

red @happy "Well, I'll be here if you decide you want to tell me later."

dawn @talkingmouth "Al... alright." 

dawn @happy "Thank you."

dawn @happy "It's um, alright, I guess, if you want to call yourself my friend. I mean, I wouldn't.{nw}" 
extend @surprised " Because I can't. I mean, you can't be your own friend. Well maybe you can, but I can't. Oh god, I'm rambling."

dawn @angry "The point is we're friends now! For real! Two-way street!"

red @surprised "Really?"

if (IsBefore(1, 5, 2004)):
    dawn @thinking "Yeah. For some reason, I... I trust you. So you're my {color=#0048ff}trusted friend{/color}."

else:
    dawn @thinking "Yeah. It's probably just because of your power, but... I... I trust you." 
    dawn @sadbrow happymouth "Well, maybe not entirely because of your power. I really appreciate what you did for me in the Quarter Qlashes. I can't stop thinking about that battle..."
    dawn @thinking "So you're my {color=#0048ff}trusted friend{/color}."

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Dawn evolve from '{color=#0048ff}Friend{/color}' to {w=0.5}{nw}"

if (rantolounge):
    show lounge with vpunch

else:
    show lobby with vpunch

dawn surprised "W-wait!"

dawn @closedbrow sadmouth "I- I- I- I want to show you! What I do in my free time! I changed my mind. Which is why I want to show you now."
dawn -surprised @sad "P-please...?"

red @happy "Hey, you can show me anything."

dawn @thinking "Okay. Now, how do I take you there without you knowing how to get back there? Do I have blindfold or anything?"

red @happymouth shadow noeyes noshine "Hm... I could just wear my cap really low, so it covers my eyes."

dawn @angry "Stop making fun of me!"

red @happy "Sorry. But you already said Instructor Melony knows about this. So I figure that it's her classroom, right?"

if (classstats["Ice"] == 5):
    red @surprised "I mean, I've never been to her class, but I'm pretty sure I can just look it up on the school website."

dawn @thinking "Oh. Um... yes. {size=30}Good going, Dawn.{/size}"

red @happy "Alright, let's go."

if (rantolounge):
    scene lounge
    show blank2 
    with splitfade

else:
    scene lobby
    show blank2 
    with splitfade

show classroom behind blank2
show icetype behind blank2
show iceglow behind blank2:
    alpha 0.5 xalign 0.5 yalign 1.0
    block:
        ease 2.0 alpha 0.25
        ease 1.8 alpha 0.7
        repeat

hide blank2 with splitfade

if (classstats["Ice"] > 5):
    red @surprised "Brr. I'll never get used to how cold Instructor Melony keeps her classroom. It's like the top of a mountain!"
else:
    red @surprised "Brr. It's really chilly in here. It's like the top of a mountain!"

red @confusedeyebrows talking2mouth "Hey, how come you're not cold?"

dawn @talkingmouth "Well, I grew up in Snowpoint City, in Sinnoh."

red @thinking "Hm. I'm not familiar, but I think the name tells me everything I need to know."

redmind @thinking "Still, you're showing quite a bit of leg for someone stepping into a freezer."

narrator "Dawn goes to the back of the classroom and unlocks a door. A moment later, she begins wheeling something out on a cart, with visible effort."

show dawn:
    xpos -0.2
    ease 7.0 xpos 0.45

show altariasculpture behind dawn:
    xpos -0.7 zoom 2.0 yanchor 1.0 ypos 1.2 alpha 0.95
    ease 7.0 xpos 0.3

pause 5.0

red @surprised "Holy shit."

narrator "You stare at a massive ice sculpture, an almost perfect replica of a Mega Altaria."

if (IsBefore(1, 5, 2004)):
    red @surprised "That's insane. How long did that take?"

else:
    red @surprised "That's insane. It looks {i}exactly{/i} like your Altaria. How long did that take?"

dawn @happy "About nine days. I'm kinda proud of it."
dawn @angry "Some of the details are a bit off, and I don't like the lack of definition between the Altaria's tail and wingfeathers."
dawn @sadbrow angrymouth "Also, her claws totally have the wrong texture. Her beak looks more like a Staraptor's."
dawn @sad "It's pretty much just a bad copy of D'Gelato's work from the 1700s. And I had to make the tail way thicker to work as a base, so--"

show dawn surprised
show classroom
show icetype
with vpunch

red @happy "It's beautiful!"

dawn "I... wha... really?"

red @happy "I don't know art, but that's it, right there. You should be very proud. And that should be very public! Like, display it in the gardens, or something!"

dawn -surprised @sad "...It'd melt."

red @thinking "Oh, yeah. Uh, what do you do with a sculpture after you finish it?"

dawn @thinking "Back home, I'd just put it outside."

dawn @sadbrow happymouth "I guess, here at Kobukan, I'll just put it in Instructor Melony's storage closet forever."

red @thinking "Hm... well, maybe we'll think of something better to do with it later."

red @happy "So, what's next?"

dawn @sadbrow "Well... I still need to study feather textures more, but, um, I was kinda thinking about doing something with food, but..."

dawn @surprised "What are you doing?"

red @shadow noeyes noshine talkingmouth "Huh? What do you mean?"

dawn "That thing with your hat. What're you doing with your hat?"

red @shadow noeyes noshine talkingmouth "Oh, just lowering it. Your statue is so bright, it's kinda glaring in my eyes. If I lower my hat, I can--"

dawn angrybrow surprisedmouth "Don't move!"

red @shadow noeyes noshine surprisedmouth "Huh?"

dawn happymouth "Yes, that's great! Now, keep your arm just like that. Twist your head a bit to the side..."

red @confusedeyebrows shadow noeyes noshine talking2mouth "Okaaaay?"

dawn @closedbrow talkingmouth "Not quite. What was it you said before? That this room was like the top of a mountain? ...No, no, you need to be higher. Um... can you get on top of that desk for me?"

red @confusedeyebrows shadow noeyes noshine talking2mouth "Just, like, climb up? Uh, sure."

dawn "Yes, almost there. The trainer standing on top of the mountain, hat lowered, unphased by the freezing winds..."

redmind @shadow noeyes noshine frownmouth "Actually, I'm very phased."

dawn "...What do you say to that?"

red @shadow noeyes noshine frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

dawn @happy "I got it! Yes, perfect! '...' is {i}perfect{/i}!"

red @shadow noeyes noshine talkingmouth "Uh... great. I feel kinda ridiculous, though. (And cold.)"

dawn happy "Don't! You look... so inspiring! Yeah, this--you'll be my next piece!"

dawn sad "...Um, with your permission?"

red @shadow noeyes noshine happymouth "Pfft. If you look at me like that, I can't say no to you. Besides, I've always wanted to be an artist's muscle."

dawn happy @surprised "Muscle?"

red "Yeah, isn't that what you call someone who inspires an artist?"

dawn @confusedeyebrows shadow noeyes noshine talking2mouth "...You're thinking of a 'muse,' [first_name]."

red @surprisedeyebrows shadow noeyes noshine surprisedmouth "Oh."

pause 2.0

red @confusedeyebrows shadow noeyes noshine talking2mouth "Can I get down, now? My arm's cramping."

dawn happy "Not yet... my {color=#0048ff}muse{/color}!"

$ persondex["Dawn"]["Relationship"] = "Muse"
$ persondex["Dawn"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Dawn evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Muse{/color}'!"

return