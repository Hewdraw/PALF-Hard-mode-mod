init python:
    def WhitneyHasUnseenScene():
        if (GetCharValue("Whitney") >= 10 and personalstats["Charm"] >= 7 and GetRelationship("Whitney") != "Project"):
            return "Whitney1"
        return False

label Whitney1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Whitney"]["Events"].append("Level2SceneVer2")

scene baseball
with Dissolve(2.0)
queue music "audio/music/goldenrod.mp3"

narrator "You're walking past the baseball field to get to Inspira city when you suddenly hear a shouting voice from far away."

whitney @surprised "{size=15}W{/size}{size=18}a{/size}{size=21}t{/size}{size=24}c{/size}{size=27}h{/size} {size=30}o{/size}{size=33}u{/size}{size=36}t{/size}{size=39}!{/size}"

show baseballitem:
    xanchor 0.5 yanchor 0.5 xpos 1.1 ypos -0.1 zoom 0.2 alpha 1.0
    easeout 0.5 xpos 0.3 ypos 1.6 zoom 1.0 alpha 0.3

if (IsBefore(1, 5, 2004)):
    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    pikachu angry_4 "Pika!"

else:
    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    libpikachu glowing angry sparks "Pika!"

narrator "Moments before the ball would hit you, [pika_name] jumps off your shoulder and deflects the ball with his tail, slamming it into the dirt."

red @surprised "Woah. [pika_name]?"

if (IsBefore(1, 5, 2004)):
    $ PlaySound("Pokemon/pikachu_norm2.ogg")
    pikachu neutral_2 "Pi... ka."

else:
    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    libpikachu angrybrow happymouth -sparks "Pi... ka."

red @happy "That was actually--"

show whitney:
    xpos 1.1
    ease 0.3 xpos 0.5

whitney @surprisedbrow happymouth "That was {i}so{/i} cool!"

red @happy "Yeah, what she said."

whitney @talkingmouth "Your Pikachu totally just deflected that ball! Like he'd trained, even! Has your Pikachu ever been in a Pokéathlon, or something?"

red @talkingmouth "Nah. He's just very motivated by not taking a baseball to the face."

whitney @smilemouth "Yeah, I get that! It's not as bad after the first couple times, though!"
whitney @surprised "Try taking a {i}bat{/i} to the face! Now, {i}that's{/i} pain."

red @happy "Has that happened to you?"

whitney @happy "It happens to everyone if you play this game long enough! But, I..."

pause 0.5

whitney @surprised "Oh, I need to get back to the game! Want to watch?"

red @thinking "I was planning on heading into Inspira, actually."

whitney @thinking "Hm."
whitney @talkingmouth "Tell ya what. You stay here for half an hour and watch me clean up this game, then we can go into Inspira together."
whitney @smilemouth "Sounds good?"

red @talkingmouth "Sure."

whitney happy "Cool! See ya in a bit."

hide whitney with dis

pause 1.0

narrator "You take a seat in the outfield, with [pika_name] nestled snugly in your lap."
narrator "You watch the game unfold as you pat [pika_name], keeping a careful eye on Whitney."
narrator "You're not too familiar with the rules of baseball, but it's impossible to ignore that Whitney is doing {i}very{/i} well."
narrator "Every time she hits the ball, a resounding {i}crack{/i} echoes across the Kobukan campus, hinting at the strength hidden with Whitney's self-proclaimed 'tiny, but dense' frame."

pause 1.0

narrator "Eventually, the game wraps up with a dominating victory for Whitney's team, and Whitney trudges over, sweaty but beaming."

pause 0.5

show whitney with dis

whitney @happy "Did you {i}see{/i} me out there? Woo! I hit {i}three{/i} home runs!"

red @talkingmouth "Very impressive."
red @confused "Are you still good to go to Inspira, though? I imagine you're pretty tired."

whitney @talkingmouth "Nah, I've got tons of energy! I just don't get tired anymore, now that I'm on Tia duty pretty much 24/7."

red @happymouth confusedeyebrows "Tia duty?"

whitney @thinking "Yeah, you know. Reminding her to wake up in the mornings, making sure she eats more than just fish, reminding her to take showers."
whitney @surprised "Like, she is 100%% okay with just jumping in public fountains, or diving into the seaport in Inspira, but showers just always slip her mind."

red @thinking "Huh."

whitney @sad "Man, where did you even {i}find{/i} that girl?"

red @sadbrow happymouth "Um... she sorta just fell out of the sky."

whitney @smilemouth "Alright, keep your secrets. Just means I get to ask you for more when it comes time to repay me."

red @confusedeyebrows talkingmouth "I trust you won't abuse that privilege?"

whitney @surprised "Ooh! Bad move. You definitely shouldn't trust me. I'm going to abuse the {i}hell{/i} out of it, actually."

red @closedbrow talking2mouth "Great."

pause 0.5

red @confused "Well, what can I do for you?"

whitney @thinking "Hmmm... figuring that out sounds like a lot of work."
whitney @angrybrow happymouth "How about I delegate that to a real expert in the field?"

red @confused "Are you talking about--"

whitney @closedbrow talkingmouth "Yes, I'm {i}obviously{/i} talking about you."

pause 0.5

red @thinking "Well, I, uh, I gotta be honest, I'm not sure what I can do to pay you back for your Tia-wrangling. Maybe if I knew you a bit better, I'd be able to figure out something you need help with?"

whitney @talkingmouth "Mmm... alright. Let's walk to Inspira, and I'll give you an unabridged history of Whitney."

red @talkingmouth "I'll grab the popcorn."

if (IsBefore(1, 5, 2004)):
    $ PlaySound("Pokemon/pikachu_sad.ogg")
    pikachu sad_2 "Piiiika."

else:
    $ PlaySound("Pokemon/pikachu_sad.ogg")
    libpikachu sad "Piiiika."

scene city_A with splitfade

pause 0.5

show whitney with dis 

pause 0.5

whitney @happy "Anyway, that brings us to {i}Cathy{/i}, and you've already heard about Cathy from when I told you about when I was dating Samantha--"

red @surprised "Oh my god, you dated Cathy? {i}Right{/i} after Carrie?"

whitney @angry "Hey! It was a revenge date! She cheated on me with a {i}boy{/i}, so the sis code does {i}not{/i} apply there."

red @sadbrow "That's more than a violation of the sis code, Whitney. You dated Carrie's literal sister."

whitney @closedbrow talkingmouth "{i}For revenge,{/i} though."

red @angrybrow talking2mouth "That does {i}not{/i} make it better."

whitney @closedbrow "Come to think of it, I think there might have been a couple weeks where I was dating both of them..."

red @surprised "Oh my god."

whitney @happy "Did I mention they were twins?"

red @closedbrow talking2mouth "Oh my {i}god.{/i}"

narrator "While walking to Inspira, Whitney has, true to her promise, been giving you a {i}very{/i} unabridged history of Whitney."

red @talkingmouth "What's your secret?"

whitney @thinking "Hm?"

red @talkingmouth "How have you had {i}so many{/i} exes? It sounds like you've dated more people than were in my entire hometown."

whitney @talkingmouth "Well, I did live in Goldenrod. It's a really big city, with a very young population, so there's all sorts of stuff to go to for high schoolers."
whitney @talkingmouth "Besides, when you're the most popular girl in high school, you don't really need to try very hard to find people who want to date you."

red @confused "...You, uh, you aren't humble about that, are you?"

whitney @smilemouth "Nope. False modesty is gross."
whitney @sadbrow talkingmouth "...I wasn't the best person in high school, though. If I was, I might not have so many exes."

pause 1.0

whitney @talkingmouth "Actually, this probably comes as a surprise to you, given how awesome I am, and how everyone loves me, but--"

redmind @surprisedbrow frownmouth "Really?"

whitney @closedbrow talkingmouth "When I got to Kobukan, I'd... kinda..."

pause 1.0

whitney @sadbrow talkingmouth "Burned all my bridges back home."

pause 0.5

red @talking2mouth "That {i}does{/i} surprise me."

whitney @talkingmouth "Surprised me, too. One day, people loved that I was loud, popular, did my own thing, and was awesome at everything I did. All that mattered was that I was Prom Queen, and I was in charge of Goldenrod High's gossip engine."
whitney frownmouth @closedbrow talkingmouth "...And the next day, everyone was talking about going to University, and 'being an adult', and boring stuff like that, and I wasn't cute anymore."

pause 0.5

whitney @smilemouth "I didn't really notice the change until people got tired of me."

pause 0.5

whitney @talkingmouth "Or maybe I {i}did{/i} notice the change, but was hoping that I could ignore it. More this one, I guess."

red @talkingmouth "Well, regardless of what mistakes you made in the past, you've clearly cemented yourself into Kobukan's social fabric."

whitney "{size=30}Cemented into fabric?{/size}"

red @happy "Everyone knows Whitney. And you know everyone. You're the one people go to when they need to find someone, or get a favor done."
red @talkingmouth "You're like the Godfather of Kobukan."

whitney -frownmouth @smilemouth "You really like your old movies, don't you?"

red @happy "What can I say? I've an appreciation for the classics."

whitney @smilemouth "Anyway... thanks. I mean, I'm over all that stuff in the past. No use moping over it. There's tons more bridges in front of me. Can't worry about the ones burning behind me, right?"

red @talkingmouth "Sure."

whitney @happy "Anyway, I've found that I really like helping people with their problems."

red @talkingmouth "Right, your 'projects.' Flannery's one. Tia's another."

whitney @talkingmouth "Yup. I think I might become a Nurse when I graduate Kobukan."

red @confused "Huh? Aren't you going to be... a trainer? Or a coordinator, at least?"

whitney @talkingmouth "Nah! Nurses use Pokémon too, silly."

red @confused "They do?"

whitney @happy "Sure. Like, Ralts are really good at sensing people's emotions, right? Blissey eggs are pretty much {i}pure{/i} endorphins. Audino are great at communicating with hearing-impaired or nonverbal people." 
whitney @smilemouth "Miltank milk is hyper-nutritious, and Togekiss can literally shower people with something called 'Joy Dust,' which is a super-thin down that triggers immense dopamine rushes in people."

red @surprised "Wow. Almost all those Pokémon are Fairy or Normal-type."

whitney @angrybrow happymouth "Uh, yeah! That's why I'm in those classes, silly!"

red @happy "I just... wow, this is a whole new side of you, Whit. Is it cool if I call you Whit?"

whitney @smilemouth "It's cool."

red @thinking "After our battle in Gym Class, I kinda thought you were... I don't know. I didn't think you'd want to be a nurse. I didn't think you'd want to be so... helpful, if that makes sense."

pause 1.0

whitney frownmouth "Hm."

red @sadbrow talking2mouth "Sorry. That was rude of me."

whitney @talkingmouth "Maybe a little bit, but... well, why do you say that?"

red @thinking "Well, it's... when we battled, you kinda used your Cleffa as a sandbag to trick me into a false sense of security. And the way you refer to some people as 'projects'... I don't know. It feels a bit... utilitarian?"

whitney @talkingmouth "...Yeah. You got me."

red @surprised "Huh?"

whitney @thinking "[first_name], can you keep a secret?"

red @talkingmouth "Very, {i}very{/i} well, actually."

if (not IsBefore(1, 5, 2004)):
    red @closedbrow talking2mouth "As long as it's not about me. You know, the whole 'Frienergy' thing..."

pause 1.0

hide whitney with dis

show seaport with Dissolve(2.0)

narrator "Whitney is silent for a long while as you walk through Inspira. Her head is down, deep in thought, as she leads you through the city, seemingly on autopilot."

pause 1.0

narrator "After a while, you end up at the seaport."

if (not seaportunlocked):
    narrator "The harsh cries of some angered bird Pokémon ring in your ears, but Whitney doesn't seem to notice."

narrator "Slowly, Whitney sits down on the dock and pats the ground next to her."

show whitney frownmouth with dis:
    xpos 0.5 ypos 1.2 zoom 1.3

whitney @talkingmouth "...I don't do good things because they're the right thing to do."

red @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

whitney @closedbrow talkingmouth "I never have. And I feel bad about that."
whitney @sadbrow talkingmouth "...Do you get what I mean?"

red @sad "I'm not sure I do."
red @thinking "Do you... do good things because you think people expect them of you?"

whitney @talkingmouth "No, that's Hilda."

red @confused "Then you do them because you just don't mind doing them?"

whitney @talkingmouth "Bianca."

pause 0.5

red @talking2mouth "Please explain."

whitney @closedbrow talkingmouth "...{i}Sigh{/i}."
whitney @talkingmouth "I'm helping Flannery with her problems because she's fascinating. Her morning-evening thing is crazy. Like, it could be a whole new syndrome that she could have named after her. And that {i}really{/i} interests me."
whitney @talkingmouth "I'm helping Tia because as long as I look out for her, and don't ask questions, you kinda have to do whatever I say. And Tia's hilarious. I like being around her because she's really, really funny."

red @confused "That wasn't {i}exactly{/i} our deal."

whitney @sadbrow talkingmouth "I learned sign language just so I could flirt with a girl. And I want to be a nurse because... I like the feeling of people needing my help."

pause 1.0

whitney @talkingmouth "Yeah. That's the problem. I like when people need my help, or owe me something."
whitney @angrybrow "And I don't like that about myself."

pause 0.5

whitney -shadow @happy "Isn't that screwed up?"

red @thinking "{w=0.5}.{w=0.5}.{w=0.5}."

pause 0.5

whitney @sadbrow talkingmouth "If... you want to leave now, that's totally fair. I'd get that."

red @thinking "No, that's not it. I think I get what's happening here."

whitney @surprised "Hm?"

red @talking2mouth "You were a super-popular girl back in high school, right? But as everyone started thinking about college, they started losing interest in high school stuff, your domain, and left."

red @talking2mouth "I get that. Something similar happened to me. And... I mean, I was just a kid back then, but kids can feel, just like adults. And kids can be hurt."

pause 0.5

red @confused "That probably... hurt, right?"

whitney "{w=0.5}.{w=0.5}.{w=0.5}."
whitney sadbrow @talkingmouth "I had to chase them down to sign my yearbook."

pause 0.5

red @talkingmouth "I think, Whitney, that you don't want your friends to be able to leave you."

whitney @surprised "Hm?"

red @talkingmouth "You want your friends to owe you something, or be dependent on you for something. So they can't just 'lose interest', and ghost you."
red @sad "And... based on some of the stories you've told me about your exes... it might be that you're afraid of being treated like you treated some of the women you dated."

pause 0.5

whitney @talkingmouth "I'm an awful person."

pause 0.5

red @closedbrow talking2mouth "Nah. An awful person wouldn't feel awfully about the awful things she's done."

whitney @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
whitney @talkingmouth "I don't like losing. I {i}rarely{/i} do. I'm lucky like that. But the thing I like losing least is a friend."

red @talkingmouth "Whitney, I know {i}exactly{/i} how you feel."

if (not IsBefore(1, 5, 2004)):
    red @talkingmouth "It's happened to me twice. But you can always bounce back."

whitney "{w=0.5}.{w=0.5}.{w=0.5}."
whitney -sadbrow -frownmouth @closedbrow talkingmouth "Okay. I've gotten {i}way{/I} too personal. How about we change the topic a bit?"

if (IsBefore(1, 5, 2004)):
    red @happy "Sure. Want to know my darkest secrets, too? Maybe it'd make you feel better."

else:
    red @happy "Sure. I'd offer to tell you about my darkest secrets, too, but... I think the whole school already knows that one."

whitney @happy "Nah, but thanks for the offer. Let's just talk about Pokémon."

red @talkingmouth "Alright. So, you're a big fan of the emotion and happiness Pokémon, huh? Have you ever heard of that legend from the Sinnoh region, Mesprit?"

show black with Dissolve(1.0)

narrator "Time passes as you and Whitney chat about inconsequential things, slowly bringing the mood back to room temperature."
narrator "However, the mood suddenly spikes once more, when..."

show whitney -frownmouth
hide black with dis

whitney @smilemouth "So, we've been talking for, like, two hours now, and you haven't asked me out. What's up with that?"

red @confused "I... kinda assumed you were a lesbian."

whitney @closedbrow frownmouth "Well, you shouldn't assume."

red @happy "Ah, but you thought, because I'm a guy, that I would've asked you out by now. So aren't you the assumer here, while I am the innocent assumee?"

whitney @surprised "Those... aren't words.{w=0.5} {size=30}Are those words?{/size} No, those aren't words."

red @talkingmouth "Baseball star, polyglot, owner of an ultimate weapon in the form of a cow, aspiring nurse, and now apparent linguist."
red @happy "Whitney really does have it all. I'm sure your next Ex will tell stories about you for a long time."

whitney @angrybrow happymouth "Hey! That's mean!"

red @happy "Sorry, Whitney. But, um... well, besides assuming you were a lesbian, which you haven't denied..."
red @sadbrow happymouth "I like you, but I've heard how you treated your exes, and... well, I don't really want to be a project."

if (IsBefore(1, 5, 2004)):
    whitney @closedbrow talkingmouth "Mm. I guess that makes sense. I'm not sure how I even could projectify you, anyway. You seem perfect. Popular, good at everything, attractive enough. For a guy."

    red @happy "Well, hey, so did you, before you told me all that stuff about pre-Kobukan Whitney. I'm just not dumping all {i}my{/i} dark secrets on you, so you'd have to work a little harder to make me a project."

else:
    whitney @closedbrow talkingmouth "Mm. I guess that makes sense. I'm not sure how I even could projectify you, anyway. You seem perfect. Kind, good at everything, attractive enough. For a guy."

    red @happy "Well, hey, I still sometimes just clam up in front of people. I'm sure I could pay a therapist's kids through college if they took a crack at that. Interested?"

whitney @surprised "Ugh, {i}work?{/i} Yeah, I'll pass."

red @happy "Hah. Seeya, Whit. It's been good talking with you."

whitney @smilemouth "Seeya, [first_name]."

narrator "You depart the seaport, leaving Whitney sitting on the dock, feet trailing in the high tide."

pause 2.0

whitney @angrybrow frownmouth "He can't turn down being my [bluecolor]project{/color}!"

whitney thinking "I mean, he's the most interesting person I've met since Flan, so... yeah, I'm going to make this happen."

pause 1.0

whitney thinking "But I'm still a lesbian. {w=0.5}...Pretty sure."

$ persondex["Whitney"]["Relationship"] = "Project"
$ persondex["Whitney"]["RelationshipRank"] = 1

$ PlaySound("sav.wav")

narrator "Your heart shifts as your relationship with Whitney unknowingly evolves from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Project{/color}'!"

return