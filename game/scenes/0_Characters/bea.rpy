init python:
    def BeaHasUnseenScene():
        if (GetCharValue("Bea") >= 10 and GetRelationship("Bea") != "Planner"):
            return "Bea1"
        return False

label Bea1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Bea"]["Events"].append("Level2SceneVer2")

scene gym 
with Dissolve(2.0)
queue music "Audio/Music/StowOnSide.mp3"

pause 1.0

show balloonbot at rightside:
    yalign 0.5
    block:
        ease 1.0 yalign 0.4
        ease 1.0 yalign 0.5
        ease 1.0 yalign 0.6
        ease 1.0 yalign 0.5
        repeat

show bea at leftside
with dis

narrator "Walking into the gym, you see that, unusually for this time of day, there seems to be only one other person here."

pause 1.0

bea @closedbrow talkingmouth "Hah..."

show bea:
    easein 0.2 xpos 0.75

show balloonbot:
    pause 0.15
    ease 0.2 xpos 1.5

bea @angry "Hah!"

pause 1.0

show bea:
    ease 0.5 xpos 0.5

bea "{w=0.5}.{w=0.5}.{w=0.5}."
bea @talkingmouth "'Lo."

red @happy "Hey, Bea. Doing some training?"

bea @talkingmouth "Yes. Living in Kobukan has weakened me."
bea @closedbrow talkingmouth "At my home in Stow-On-Side, I used to wake up every morning and climb the mountains north of us."

red @talkingmouth "Cool. Cool. So, hey, you told me to find you so we could work on your, uh, face training?"

if (IsBefore(1, 5, 2004)):
    bea @talkingmouth "Yes. Are you ready?"

else:
    bea sad "{w=0.5}.{w=0.5}.{w=0.5}."

    red @sad "...It's... it's fine if you don't want to, anymore. I know things have changed, since you made that offer."

    pause 1.0

    bea -sad @closedbrow talkingmouth "...Yes, things have changed. The reveal of your power was... unexpected. For both of us."

    red @sadbrow talkingmouth "If it helps, I didn't know about it until about two weeks into the school year."

    bea @closedbrow talkingmouth "That is of no consequence. I was moved by the speech you gave."

    redmind @thinking "Moved? You could've fooled me."

    pause 1.0

    bea @talkingmouth "I understand the pain that those with power can inflict. I think it shows strength of character and will to restrain yourself--as I believe you have."

    red @sadbrow talkingmouth "Thanks."
    red @closedbrow talking2mouth "Although, the way this power works, I don't think I could have used it in a negative way."

    bea @sad "There are... those who are 'creative' in their application of their natural talents. I trust that you are not that sort."
    bea @talkingmouth "In any case, I am friends with Sabrina, and if I do not fear her, there is less than nothing to fear from you."

    redmind @confused "...I mean, that's great, but I feel a tiny bit offended."

    pause 1.0

    bea @talkingmouth "Therefore, I would ask you to join me in my training, as originally requested."

red @happy "Absolutely! So, how does this work, exactly?"

bea @talkingmouth "It's quite simple. Attack me, and I will attempt to block or dodge. If I express any fear, uncertainty, or panic, then I fail."
bea @closedbrow talkingmouth "Of course, I also fail if I cannot fend off your attack."

red @confused "Uh... attack you? I don't know any martial arts."

bea surprised "Oh."

pause 1.0

bea -surprised @talkingmouth "I assumed from your muscle definition that you knew a bit of Muay Thai."

red @thinking "I think I had that at a bar once..."

bea @talkingmouth "Well, in that case, just try to grab me."

redmind @thinking "Man, this is a {i}weird{/i} conversation to have."

red @talkingmouth "Just, like... 'grab?' Uh, where?"

bea @closedbrow talkingmouth "The extremities of the limbs are the hardest to find purchase on. However, they're the easiest to {i}keep{/i} in your possession."
bea @talkingmouth "If you were to grab onto my wrist, I would understandably jerk my arm inwards to try and slip out of your grasp." 
bea @closedbrow talkingmouth "You should counter that, not by resisting, but by following my arm's movement." 
bea @talkingmouth "After I am incapable of pulling my arm back any further, you can similarly jerk your arm backward at the same time, throwing me off balance, if my footing is not secure."
bea @closedbrow talkingmouth "However, my footing {i}will{/i} be secure. You'll want to unsteady me with a firm kick to my inner right ankle. However, I'll be expecting that, so aim higher, as I'll--"


red @surprised "Uh, Bea? I'm pretty sure none of this is relevant."
if (IsBefore(23, 4, 2004)):
    red @surprised "I mean, just looking at you, I can tell you're tough, and trained."
else:
    red @surprised "You did, like, two hundred push-ups during the Battle Team meeting. With a Clobbopus on your back."

red @happy "There's no way I'm laying a hand on you."

bea @talking2mouth "...Training may not be enough to overcome the additional ninety pounds of muscle you're bringing to our bout."

red @happy "Fair enough."

show gym:
    xalign 0.5 yalign 0.5
    ease 2.0 zoom 1.2

show bea:
    ease 2.0 ypos 1.2 zoom 1.3

bea @closedbrow "Now..."

bea angry "Begin!"

show bea:
    ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

pause 0.35

play sound "audio/body roll.ogg"
queue sound "audio/body crash.ogg"

show blank2 with vpunch
hide bea

red @surprised "OOF!"
red @talkingmouth "Woah--I thought I was going to attack you, and you were going to defend?"

bea @talkingmouth "Yes." 
bea @angry "And the best defense is an unweatherable offense!"

red @happy "Well, I can't argue with that. Gimme a second to--"

show blank2 with vpunch

red @surprised "Oh, shit! We're still going?"

bea @angry "Attack me!"

narrator "You end up wrestling with Bea for more than ten minutes. Though she is clearly more skilled than you, you notice her stamina is starting to flag, and you suspect that you might be able to successfully grab her wrist."
narrator "You push through your tiredness, and--"

show bea surprisedbrow angrymouth behind blank2:
    ypos 1.2 zoom 1.3
hide blank2

red @happy "Gotcha!"

bea "Ah!"

pause 1.0

red "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

red @confused "Uh... aren't you going to, like, pull your arm back? What happened to that big plan?"

bea -angrymouth sadbrow @sadmouth "...Please let go."

show bea:
    ease 0.5 ypos 1.0 zoom 1.0

red @surprised "Huh? Oh, yeah, of course!"

pause 1.0

red @sad "I'm sorry. Did I... did I hurt you?"

bea @sadmouth "No."

pause 1.0

red @talkingmouth "Um... you kinda froze, there. Is that something you'd like to tell me about?"

bea @closedbrow sadmouth "With... the understanding that you tell no-one else?"

red @talking2mouth "I promise."

pause 1.0

bea @talkingmouth "I was a trainer once before. In Galar, trainer schools aren't typically a thing. Most people just start their journey after getting an endorsement."

if (GetRelationshipRank("Nessa") > 0):
    red @thinking "Yeah, Nessa explained that to me."

bea @thinking "I wasn't alone on that journey. With me, there was... another."

pause 1.0

bea @talkingmouth "A boy I loved like a brother. He didn't actually want to go on an adventure. And he was too young, too. But I dragged him along, and..." 
bea @thinking "We had just started our journey when we were attacked."

pause 1.0

bea @sadmouth "My brother was timid and shy. I promised to protect him. It was the only way I could have gotten him to leave his library. I {i}promised.{/i}"
bea @angry "But... I froze. I panicked. I {i}failed.{/i}"

if (not IsBefore(1, 5, 2004)):
    bea @sad "When Cheren was saying those awful things to you, up on that stage..."
    bea @talkingmouth "I saw a fear in your eyes that I recognized. Blind panic. Betrayal. Hurt and noncomprehension the world could be so cruel."
    bea @thinking "I felt the same from Sabrina. Of course, using her powers, she {i}could{/i} have defended herself. But she, like others, cannot comprehend of the {i}need{/i} to defend oneself."
    bea @sad "I can. I should have done so. But, once again... I froze, and panicked, and failed."
    
    pause 1.0

    bea @sad "I thought... after years had passed... that my strength would be enough. That I could save another from the fate that befell my brother. But absolutely nothing has changed."

pause 1.0

bea @sad "And now my brother barely leaves his room, and can't bear to show his face to anyone. He lives with a poisonous, caustic, shame."
bea @closedbrow "A shame that should be mine."

red @angrybrow talking2mouth "Hey. {i}No.{/i} You have nothing to be ashamed of. Neither does your brother. You were {i}kids{/i}."
red @thinking "And even if you were fully grown, you still have nothing to be ashamed of."

pause 1.0

red @sad "What happened next?"

bea @talkingmouth "We went back home. My brother retreated into his library, hiding himself ever deeper in the shadows."
bea @sadmouth "Then, after returning home from school one day, he brought home a papier-mâché mask he made in art class... and I've never seen his face since."

red @sad "Is that why you wear a mask, too, then?"

bea -sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
bea @talkingmouth "Yes. I must train myself so my weakness does not cause more tragedies like this to happen again. For that, eliminating uncontrolled movement in my body is practical."
bea @talkingmouth "But removing all traces of emotion from my face is not strictly necessary for that. {i}That{/i} is... my penance."

pause 1.0

red @talking2mouth "Okay."

bea @surprised "Oh?"

red @talkingmouth "Okay. I understand."

bea @talkingmouth "I'm happy, but surprised. {i}Why{/i} do you understand? No-one but my brother ever has. Ever {i}could.{/i}"

red @closedbrow talking2mouth "When bad stuff happens to us, we all have different coping methods. It's not my place to judge yours. If it makes you feel like you're 'paying off' some sort of debt, then carry on. Forever, if you need to."

bea @surprised "That's the exact opposite of what my therapist said."

red @happy "Well, I don't have a degree."
red @talkingmouth "The way I see it, as long as you're not hurting anyone, you can do whatever you want."
red @happy "If you want to keep your emotions hidden, go ahead."

bea @happymouth "Hm. No-one has ever said that's fine before... I'm interested, now."
bea @talkingmouth "Who {i}are{/i} you, [first_name] [last_name]?"

red @happy "Just a guy who's going to be a Pokémon Champion."

bea @talking2mouth "Hm."

red @talkingmouth "What about you, Bea?"

if (IsBefore(23, 4, 2004)):
    bea @talkingmouth "I intend to join the Battle Team. I'll leverage my position as a member of the Battle Team to return to Galar and get a second endorsement, beginning my journey again."

else:
    bea @talkingmouth "I intend to leverage my position as a member of the Battle Team to return to Galar and get a second endorsement, beginning my journey again."

red @surprised "Oh! You're going to try the Galarian league again?"

bea @closedbrow talkingmouth "Yes. The first part of my penance is to wear my brother's mask. The second part is to finish my journey alone."

red @thinking "And after that, you'll... be satisfied?"

bea @talkingmouth "After that, I'll feel I have done enough to deserve the chance to beg for my brother's forgiveness."

red @confusedeyebrows talking2mouth "Aren't you being a bit hard on yourself?"

pause 1.0

bea @talkingmouth "There's an old Galarian story my brother told me about a Rolycoly. This Rolycoly was very small, and weak, and all the other Rolycoly used to mock and shun her."
bea @closedbrow talkingmouth "...Actually, in the original story, the Rolycoly was male, but I like to imagine it was female."
bea @talkingmouth "Anyway. Because this Rolycoly was never able to participate in the coal-running along with the others, it was left behind when they evolved into Carkol."
bea @talkingmouth "So it started training itself. It would ram itself into walls, over and over, to toughen its shell."
bea @closedbrow talkingmouth "It did this for ages. Until, one day, it rammed itself into the wall of the abandoned mine so hard that it caused a cave-in."
bea @surprisedbrow talkingmouth "The other Carkol and Coalossal were wracked with grief as they saw what their bullying and shunning had done."
bea @talkingmouth "As they wept above the pile of rubble that was their home, and now marked their sister's grave, one of them noticed a shining light coming from the debris."
bea @talkingmouth "The Coal Pokémon quickly began excavating the rubble, and beneath, they saw something remarkable--the lone Rolycoly's body, through its intense training, and the pressure of the collapsed mine, had become shining diamond."

pause 1.0

red @confused "So... the Rolycoly survived, right?"

bea @surprised "Hm?"
bea @talkingmouth "Oh, no, she was quite dead."

pause 1.0

red @confused "I guess I don't get the moral of the story."

bea @closedbrow talking2mouth "I think the moral is that Galar is a dim, rainy, place where everybody has very grim outlooks on life."

pause 1.0

red @confused "Why did you tell me this story? I asked you if you were being a bit hard on yourself."

bea @surprised "Oh."
bea @closedbrow talkingmouth "Right. I'd forgotten the point I was trying to make."
bea @talkingmouth "The point is, it's always easiest to see one's best qualities after they've been broken."
bea @talking2mouth "So that's my goal. I will become an unbreakable, unflinching fist, then shatter myself against the stones."
bea @talkingmouth "I will eliminate my weakness, and temper my strength."

red @confused "So you'll make yourself strong... and then weak?"

bea @closedbrow talkingmouth "I will show my brother that even the strong can be broken. His shame comes because he believes that his weakness caused the attack. But I will teach him that even the strong can be weakened." 
bea @sadbrow talkingmouth "And then, perhaps, after my penance has been paid, and he sees that his misfortunes are not his fault, things can go back... back to how they were before."

red @confused "See, I was with you for the 'wearing a metaphorical mask' part of your plan, but I think I'm a bit lost on some of the details now."

bea @talkingmouth "Elaborate?"

red @closedbrow talking2mouth "Like, when you say you're going to make yourself stronger, you mean, you will become {i}physically{/i} stronger, right? As in, put on more muscle, learn new martial arts?"

bea @talkingmouth "Yes."

red @confused "Okay, so I get how you'll do that. Exercise and training. Simple enough. But what about the 'breaking?' How are you going to do that--to prove to your brother that even the strong can be broken?"

bea "By begging for forgiveness."

red @closedbrow "Right. This is... this is kinda a complicated plan."

bea @surprised "What?"

bea @talkingmouth "No, it has two steps. Get strong, then ask for forgiveness. It's very simple."

red @closedbrow talking2mouth "Sure, but what about hiding your emotions? How long will that last? And how strong is strong enough? I mean, you're already pretty strong." 

show bea surprised with dis

red @confused "And what's the point of finishing your Pokémon journey in Galar if you're focused on becoming {i}physically{/i} stronger?"
red @thinking "What happens if you actually do, like, {i}really{/i} well in Kobukan? Are you just going to quit wherever you ended up and become a beginner trainer again in Galar?"
red @talkingmouth "And if you {i}were{/i} going to do that, then what about the Pokémon you trained in Kobukan? Are you just going to leave them in a PC and pick up a Farfetch'd somewhere in the wilds?"

pause 1.0

bea sad "Um."

red @sadbrow talking2mouth "You've been thinking about this plan for a long time, haven't you?"

bea "Yes..."

red @sadbrow talking2mouth "I can tell. You've added so much to this plan, you lost your original goal."

pause 1.0

red @thinking "The number one thing you want is to get your brother to open up again?"

bea -sad @talkingmouth "I want him to feel safe again."

red @talkingmouth "Okay. Let's focus on that. And let's come up with a plan for how we're going to do that."

bea @talking2mouth "We?"

red @talkingmouth "Sure! I want to help you. And even though you tossed me around this gym for ten minutes, it seems like you could do with a little help on the planning front."

bea "{w=0.5}.{w=0.5}.{w=0.5}."
bea @closedbrow talkingmouth "That's fair. What do you have in mind?"

red @talking2mouth "I don't know yet. But I'll seek you out when I can, alright?"

bea @happymouth "...Yes."

$ BecomeContacted("Bea")

bea @talkingmouth "Please contact me as soon as you feel we could begin our discussion of this plan."

red @happy "Sure thing. Oh, by the way, Bea?"

bea @surprised "Hm?"

red @confused "You've been kinda... 'loose' with your face for this entire conversation."

bea "{w=0.5}.{w=0.5}.{w=0.5}."

if (IsBefore(1, 5, 2004)):
    bea @closedbrow talkingmouth "I find it difficult to hide my feelings around you, for some reason. I just need more practice."
else:
    bea @closedbrow talkingmouth "I find it difficult to hide my feelings around you, for some reason. I imagine this is a side-effect of your power."

    pause 1.0

    redmind @thinking "Yeah, maybe."

red @happy "Yeah, alright. Seeya, Bea."

hide bea with dis

pause 2.0

redmind @thinking "Eeesh. That was {i}intense.{/i}"

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 3.0

show blank
show janine behind blank

pause 0.1

$ renpy.transition(None)
hide smoke
hide blank

if (GetRelationship("Janine") == "Good Boy"):
    red @surprised "Woah! Miss Janine!"
else:
    red @surprised "Woah! Janine!"

janine @talkingmouth "Yeah, hi. What were you talking about?"

red @confused "Um... she was just telling me about her past, and her home in Galar, really..."

pause 1.0

red @confused "Why?"

if (IsBefore(23, 4, 2004)):
    janine @talkingmouth "I want that girl in the Battle Team."

    red @happy "Oh, you're in luck, then! She said she wants to join."

    janine @thinking "Hm. Good."

    janine @happy "If you have any influence over her... keep her that way. She'll be useful. Almost as useful as you, I bet."

    $ ValueChange("Janine", 3, 0.5)

    red @confused "Uh... thanks?"

    janine closedbrow talkingmouth "The girl's strong, but doesn't think long-term. And when she does, she just confuses herself. She needs, like... a notebook, or a {color=#0048ff}planner{/color} or something..."
else:
    janine @talkingmouth "She's part of my Battle Team. I just want to know how my battlers are doing."
    janine @happy "And keep an eye out for possible mutiny, of course."

    red @talkingmouth "Well, she's doing fine. She's a bit confused, but... she's alright. Figuring it out."

    janine @sad "Right... from what she told me, she..."

    pause 1.0

    janine @talkingmouth "Nevermind. If she wants to tell you, she will. Not everyone's as much of an open book as I am."
    janine @happy "Hey. She's your teammate, she's been through a lot, and I care about her."
    janine @angrybrow talkingmouth "Be nice to her. Or else. And not in the fun way."

    red @talking2mouth "Of course. I wouldn't dream of anything else."

    $ ValueChange("Janine", 3, 0.5)

    janine @happy "Good!"

    janine closedbrow talkingmouth "The girl's strong, but doesn't think long-term. And when she does, she just confuses herself. She needs, like... a notebook, or a {color=#0048ff}planner{/color} or something..."

$ persondex["Bea"]["Relationship"] = "Planner"
$ persondex["Bea"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Bea evolve from '{color=#0048ff}Training Partner{/color}' to '{color=#0048ff}Planner{/color}'!"

return