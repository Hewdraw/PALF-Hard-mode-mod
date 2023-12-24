init python:
    def LeafHasUnseenScene():
        if (GetCharValue("Leaf") >= 10 and GetRelationshipRank("Leaf") == 0):
            return "Leaf1"
        return False

label Leaf1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Leaf"]["Events"].append("Level2SceneVer2")

scene hall_B 
show leaf
with Dissolve(2.0)

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)
    
red @talkingmouth "Hey, Leaf."

if (IsBefore(1, 5, 2004)):
    leaf @happy "[first_name]! There you are. I see you're using your free time to track me down. To hang out? Perchance to dream?"

else:
    leaf @flirt "[first_name]! There you are. Didn't get enough of me in the dorm, hm? Well, what do you want to do? Want to hang out? Perchance to dream?"

red @happy "Yeah, actually.{nw}"

show leaf surprisedbrow with dis

extend " {w=0.5}You're always bringing me to places, and making plans. Figured I'd return the favor."

leaf happy "Hah! I appreciate it. But it's probably for the best that I'm the one making the plans here." 

red @surprised "Hey! What do you mean by that?"

leaf -happy @flirt "Be honest with me, [first_name]. Where would you take me?"

red @thinking ".{w=0.25}.{w=0.25}.{w=0.25}"
extend @sadbrow happymouth "The fields? For a run?"

leaf @sarcastic "And that's why you leave the planning to me, sweet cheeks."

red @angrybrow frownmouth "I'm feeling very offended right now."

leaf @flirt "Hey, chill. I'll buy you something nice to make up for it."

pause 2.0

leaf @sad "Ah... sorry. I forgot, that's a sore point with you."

red @thinking "It's alright. I mean, it's not really a sore point, it's just a fact. I'm poor."

leaf frownmouth @thinking ".{w=0.5}.{w=0.5}.{w=0.5}"

if (IsBefore(1, 5, 2004)):
    red @happy "You want to ask, huh?"

    leaf @embarrassed "{i}So{/i} badly. But I won't, if, uh..."

    red @talkingmouth "We're friends. Go ahead."

    leaf @surprised "Oh, thank god. Yeah, so, what's up with that? Kobukan is pricey as hell. My parents are pretty wealthy, and even they were like 'but honey, the cost...' when I told them I wanted to go here."

    redmind @thinking "...{i}Sigh.{/i} I shouldn't have told her she could ask. Because now I'll have to lie, and I can't do that."

    red @sadeyes sadeyebrows happymouth "I... uh... had very good recommendations?"

    leaf @surprisedbrow frownmouth "...What? Really, [first_name]? You're lying to me?"

    red @sadbrow talking2mouth "I'm sorry..."

    leaf -frownmouth @angrybrow angrysmilemouth "Well, fine! I'm not going to tell you my super-secret ultra-tragic plot-twisty backstory, then."

else:
    leaf @talkingmouth "Your house was nice."

    red @happy "Eh, tiny! Tiny. But nice, yeah."
    red @thinking "Still... I have no idea how I'm going to pay for it. Kobukan, I mean, not my house." 
    red @talking2mouth "You've probably figured out how I got in, right?"

    leaf @closedbrow talkingmouth "Not entirely, but I get the feeling that Ol' Samuel Oak was pretty involved."

    red @sadbrow sweat talkingmouth "That's the ballpark."

    pause 1.0

    red @confused "What about you? Not how you got into Kobukan, but, I mean... your thing about water?"
    red @thinking "It's pretty obvious at this point you're kinda... seriously hydrophobic."

    leaf @sarcastic "Aquaphobic."

    red @surprisedbrow frownmouth "Hm?"

    leaf @talkingmouth "The condition's called 'Aquaphobia'. Hydrophobia is caused by rabies."

    red @confused "...Oh."

    pause 1.0

    red @confused "Well?"

    leaf @talking2mouth "Well, a girl has to keep her secrets."

red @thinking "Hm... would you be down to play twenty questions for your backstory, then?"

leaf @thinking "Sure. But what do I get if I win?"

red @surprised "Huh? If I'm playing for your backstory, then aren't I the one that can win?"

leaf @sarcastic "Yeah, but if you can't figure it out, then that means I win."

red @talkingmouth "Oh, yeah, okay, that makes sense."

red @happy "Alright, first question. Where are you from?"

pause 2.0

leaf frownmouth @surprised "...Aw, man."

red @surprised "What?"

leaf @angrybrow angrysmilemouth "You got it in one question!"

red @thinking "Huh? Your tragic backstory is just where you came from?"

leaf -frownmouth @talking2mouth "Yep."

red @thinking "I'm not sure how that's possible...?"

leaf @surprised "Seriously? You're a Kantonian from Pallet Town, right?"

red @talking2mouth "Yeah."

leaf @sarcastic "And you can't think of a {i}single{/i} location that is inexorably interwoven with catastrophically tragic eventualities?"

red @angrybrow talking2mouth "Stop using five-syllable words. I got a C+ in my Japanese class in Pallet High, that's not fair."

leaf @flirtbrow angrysmilemouth "...Dude, it's like fifty miles directly south of Pallet."

red @sadbrow happymouth "I got a C+ in my geography class, too."

leaf @surprised "Holy shit, you are literally not a functional human being."

red @confusedeyebrows "Uh... bit hurtful."

leaf @embarrassed blush "Sorry."

red @happy "All good. Now, tragic backstory?"

leaf @surprised "Oh! Right."

leaf @talkingmouth "Uh, it's Cinnabar Island."

red @surprised "Wait! Holy shit, I actually {i}do{/i} know that one. The volcano erupted, right? And the island was... obliterated."

leaf @thinking "Yeah, it wasn't pretty. But my family lived right on the shore, in a laboratory. We gathered up our Pokémon, helped our neighbors evacuate, and were miles away by the time the lava started flowing."

red @thinking "Oh. So it didn't actually, like... hurt you, or anyone you knew?"

leaf @angry "Hey! My childhood home went up in flames! That's plenty of trauma, I'll have you know!"

red @happy "Sorry. I was just expecting... I dunno. More death."

leaf @angrybrow angrysmilemouth "Well, sorry to disappoint. Dickhead."

red @talking2mouth "On a serious note, though, you said you lived in a laboratory?"

leaf @talking2mouth "Oh, yeah, a fossil restoration laboratory. Kinda my parents' specialty."

red @thinking "Scientists?"

leaf @happy "The best. They actually worked with Dr. Blaine. Who, I think, is a teacher at this school."

if (classstats["Fire"] > 5):
    red @talkingmouth "Yeah, I've taken my Fire-type elective with him."

    leaf @happy "Seriously? He used to come over to our house and give me candy. I should drop by his classroom."

    red @angrybrow talkingmouth "For more candy, right?"

    leaf @talking2mouth "You know it."

red @happy "Huh. Well, that's pretty cool."

leaf @thinking "..."

leaf @blush sadbrow talking2mouth "Hey. Thanks for being cool about the Cinnabar thing."

red @confusedeyebrows talkingmouth "What do you mean?"

leaf @sarcastic "Believe it or not, most people, when I tell them that, figure that I'm actually super-broken about it, and have secretly never recovered. It's all 'be sensitive' and junk after that."

red @talkingmouth "Nah. I can tell you're fine. You're strong."

if (not IsBefore(1, 5, 2004)):
    red @talkingmouth "Even though flying across the ocean terrified you, you still did it. For me. And that means a ton."

leaf bigblush @surprised "...H-hey, cool it, skippy."

if ("RejectedConfession" not in persondex["Leaf"]["Events"]):
    red @talkingmouth closedbrow "And miss out on that blush of yours? Fat chance."

else:
    red @talkingmouth "Nah. I think I'm just going to praise you more. After all, you do it enough, so you can't be {i}too{/i} upset when someone else does it, right?"

leaf -bigblush @sarcastic "God, you'd be so cute if you just learned to keep your mouth shut."

red @thinking "I've been told that's a flaw, yeah."

if (not IsBefore(1, 5, 2004)):
    redmind @thinking "...So, now I know what triggered her fear of water... but it sounds like the volcano was the bigger problem, there. I don't get it. Shouldn't she be afraid of fire, then?"

if ("RejectedConfession" in persondex["Leaf"]["Events"]):
    leaf @happy "Well, another obvious flaw is that you suck at figuring out where to take a girl. At this point, maybe I should be {i}thankful{/i} you turned me down. I've given you enough time to think up a place, now. What've you got?"

else:
    leaf @happy "Well, another obvious flaw is that you suck at figuring out where to take a girl. I've given you enough time to think up a place, now. What've you got?"

red @surprised "I was meant to be thinking up a place to go that whole time?"

leaf @thinking "So... you didn't."

red @thinking "If I pretend I did, would you believe me?"

leaf @thinking "Not a chance, no, but go ahead."

red @happy "The Student Center. Figured we could get a bite to eat, chat for a bit."

leaf @sarcastic "Wow, that sounds like a very real and thought-out plan that you {i}definitely{/i} didn't come up with just now."

red @thinking "You know, my mother always says sarcasm is the lowest form of wit."

leaf @sarcastic "Uh, yeah. I'm aiming low."

scene blank
with fade

pause 0.5

scene cafe with fade

show leaf with dis

leaf @talking2mouth "Man, it sure is crowded in here. Don't these guys have any studying to do? Why are they all just loitering around?"

red @talkingmouth "We're not any different."

leaf @sarcastic "Uh, yeah we are. We're {i}self-aware{/i}. That makes anything okay."

red @thinking "I learn so many new things around you."

leaf @flirt "I like to think of myself as a teacher. The world deserves to hear my experience."

leaf @happy "So, what'd you want to talk about? Nothing serious, I hope. I mean, I already told you about the destruction of my home planet, so you'd have to go pretty dark to beat that."

red @thinking "So, uh, what do you do for fun outside of school?"

leaf @talkingmouth "Well, I... uh..."
leaf @embarrassed "Will I sound like a nerd if I say 'study?'"

red @talkingmouth "Yeah. Nerd."

leaf @angry "Hey! I don't even wear glasses!"

red @happy "No, I get it, though. Like, studying from books isn't super-fun, but if it's about Pokémon, it becomes fun, right?"

leaf @happy "Yeah, you get it! And battles are just, like... aren't battles just the best thing ever?"

red @happy "...Hm?"

stop music fadeout 3.0

leaf @closedbrow talking2mouth "Yeah. I can hear it now. The roar of the crowd. The flanks of my Pokémon shining as the light catches them."
leaf @closedbrow "The struggle, the pain, the triumph. The bond between Pokémon and trainer tested to its breaking point in the crucible of combat."
leaf @closedbrow happymouth "The fury of battle! The emotions! The expressions of the other trainer! Confidence, rage, fear. And, at the end, the feeling of hands clasped in respect, and understanding."

pause 2.0

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=2.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

leaf bigblush @embarrassedbrow happymouth "I, uh... I really like battles."

red @happy "...I could see it."

leaf @surprised "Huh?"

red @thinking "I could see it. I could see you standing on the battlefield, commanding a team of Pokémon to victory."

leaf @surprised ".{w=0.25}.{w=0.25}.{w=0.25}"
extend @happy "Heh heh. I like you."

red @happy "That's the plan."

leaf -bigblush @talking2mouth "So, my turn to ask a question. What's up with you and [blue_name]?"

if (not IsBefore(1, 5, 2004)):
    leaf @thinking "I kinda got the vibe that Blue knew about Frienergy, and... something happened with your friend group back in the day?"

red @thinking "Ah. Well, that's... that's a story."

leaf @happy "I have time."

red @talkingmouth "Clearly.{w=0.5} Well, Pallet Town wasn't very big. But I had a small group of friends, he had a small group of friends, and we were friends with each other ever since we were, like, six."

leaf @talkingmouth "Ooh, a friends-to-enemies arc?"

red @thinking "Wasn't an arc so much as an unexpected and unasked for plot twist."

red @talkingmouth "He'd been getting really moody for a few years before High School started."

leaf @sarcastic "Puberty?"

red @talkingmouth "Family problems, I think. He never told me. Anyway, on the first day of high school, he stood up in front of class and told everyone that he was going to be a Pokémon Champion."

leaf @thinking "What, like, the first day of Professor Oak's homeroom?"

red @talkingmouth "Yeah, exactly like that. Obnoxious and loud-mouthed. Anyway, I did the exact same thing."

leaf @surprised "What?"

red @closedeyes talking2mouth "Cut me some slack, I was 14. We ended up having this big argument in front of the class before the teacher even did attendance."

leaf @embarrassed "I guess I'm confused. What was there to fight about?"

red @talking2mouth "Becoming Pokémon Champion was my thing. It's the only future I've ever planned for, for as long as I can remember. All our friends knew that. He was trying to steal my gimmick."

leaf @thinking "Oh, yeah, I {i}do{/i} understand how important gimmicks are in High School. But, still..."

leaf frownmouth @embarrassed "...Well, I'm not sure you're in the right there."

red @thinking "Yeah, looking back on it, it was really a small thing. I mean, in college, who even cares about gimmicks like that?"

leaf @thinking "So how come you two haven't made up?"

red @sad "Well... I mentioned we had two groups of friends, right? By the time we had hit high school, our friend group had merged into one."

red @thinking "And when Blue left the group, well, all my friends went with him. So, uh, I guess {i}I{/i} was the one who left the group."

leaf surprised "{i}All{/i} of them?"

if (IsBefore(1, 5, 2004)):
    red @sad "Yeah. I think he told them some stories about me. I don't know. They just kinda avoided me for four years."

else:
    red @sad "Yeah. He told them about Frienergy, and... They just kinda avoided me for four years."

leaf -surprised frownmouth @sad "That's awful... I'm so sorry to hear that."

red @happy "Hey, if I didn't cry over your backstory, you can't cry over mine."

leaf @angrybrow talking2mouth "I'm not. I'm just mad at him! No wonder you set out like a friend-seeking missile as soon as you enrolled here!"

red @thinking "Yeah, being able to meet a ton of people I didn't know really helped me start over fresh."

if (IsBefore(1, 5, 2004)):
    leaf @angry "Well, next time I see that [blue_name], I'm going to give him such a talking-to!"

else:
    leaf @angry "Well, when we get back to the dorm, I'm going to give [blue_name] such a talking-to!"

red @surprised "Oh god, no, don't do that."

leaf happy "Sorry, you don't have a choice. That's just the kind of thing I do for my {color=#0048ff}besties{/color}!"

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

$ relationship = GetRelationship("Leaf")
$ newrelationship = ("Bestie" if relationship != "Date" else "Bestie & Date")

narrator "Your heart shifts as you feel your relationship with Leaf evolve from '{color=#0048ff}[relationship]{/color}' to '{color=#0048ff}[newrelationship]{/color}'!"

$ persondex["Leaf"]["Relationship"] = newrelationship
$ persondex["Leaf"]["RelationshipRank"] = 1

return