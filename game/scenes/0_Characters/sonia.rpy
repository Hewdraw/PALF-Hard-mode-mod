init python:
    def SoniaHasUnseenScene():
        if (GetCharValue("Sonia") >= 10 and GetRelationship("Nessa") == "Friend" and GetRelationship("Sonia") != "Friend"):
            return "Sonia1"
        return False

label Sonia1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Sonia"]["Events"].append("Level2SceneVer2")

scene research
show sonia at rightside
show nessa at leftside:
    xzoom -1
with Dissolve(2.0)
show screen songsplash("Sonia's Theme", "Syntthetix")
stop music fadeout 1.5
queue music "audio/music/sonia.mp3" fadein 1.5

narrator "You aimlessly walk into the Research Center, possibly to talk with Professor Oak, when you see Sonia and Nessa talking."

sonia @happy "And the best part, Ness, is I feel like I'm {i}really{/i} succeeding this time!"

if (IsBefore(4, 10, 2004)):
    nessa @talkingmouth "Don't get too far ahead of yourself. We're not even halfway through the year yet."

else:
    nessa @talking2mouth "Yeah. I think you are. You made it more than halfway, which was always a sticking point for you, right? Good job."

pause 0.5

nessa @surprised "Oh. [first_name]?"

red @happy "Hey-o. Hope I'm not interrupting anything."

nessa @talking2mouth "Nah. Sunny, remember that guy I told you about? The one who took me on a date to a pit in the middle of the fields?"

sonia @surprised "No, really?"

nessa @happy "Yeah, it was this guy."

if (not IsBefore(1, 5, 2004)):
    sonia @surprisedbrow happymouth "...You might've mentioned that your date was my teammate--the one that Cheren said had mind control, to boot."

    nessa @closedbrow talkingmouth "...Yeah, well, I didn't."

sonia @happy "Well, I'm very happy to see you've found someone, Ness."

nessa @closedbrow talking2mouth "Slow down there. It's just a casual thing."

sonia @sadbrow happymouth "Oh. There I go, rushing into assumptions again."

red @happy "We pretty much just talked about you, actually, Sonia."

nessa @surprised "You didn't need to say that."

sonia @surprisedbrow happymouth "Only good things, I hope?"

show nessa surprisedbrow frownmouth with dis

red @talkingmouth "Yeah. Nessa cares a lot about you."

nessa -surprisedbrow @closedbrow talkingmouth "Okay, [first_name], that's enough."

red @happy "Oops!"

nessa @closedbrow "I need to go prep some stuff for Science club. See you lat--"

sonia @surprisedbrow happymouth "Wait, {i}science{/i} club?"

nessa @talkingmouth "Yeah. It's a blow-off club. We mostly just sit around and study rocks. But it's a good place to hang out and kill time."

sonia @sadbrow talkingmouth "Ness, you know how I feel about geologists..."

red @confused "Um, sorry, what? Is there some sort of geologist-based tragic backstory I'm not privy to, here?"

nessa closedbrow happymouth "It's a fun story. Tell him, Sunny. Give him a test run for me."

$ ValueChange("Nessa", 3, 0.25)

nessa @talkingmouth "Good seeing you, [first_name]."

hide nessa with dis

pause 1.0

redmind @confusedeyebrows frownmouth "Test run?"

show sonia:
    ease 0.5 xpos 0.5

pause 0.5

sonia @talking2mouth "Don't mind Sunny. It's just a running joke we used to have."

red @closedbrow talking2mouth "A joke... between the Galarian Stars, right?"

sonia @surprised "Oh, she told you about us?"
sonia @talking2mouth "Yes, that's right. She, um, she had a lot of suitors back in Galar."

pause 0.5

sonia @closedbrow talking2mouth "Well, to call them suitors might be too polite a term, given their intentions."
sonia @sadbrow happymouth "They knew she would turn them down... so then they'd, erm, make their intentions clear. {w=0.5}To me."
sonia @sad "Given my lower standards, I'd usually accept, we'd date for a few months, and then... well, usually the relationship would end when they realized that dating me didn't get them any closer to Ness."

red @confused "Geez.{w=0.5} That's awful. I'm sorry, Sonia."

sonia @talking2mouth "Well, it happened so often, that Raihan started making jokes about how I was, like, Nessa's 'boyfriend secretary.' That I was giving them 'test runs' for her."

red @surprised "Eesh. That seems a bit... hurtful, I guess?"

sonia @closedbrow talkingmouth "Right, it wasn't fantastic."
sonia @sadbrow happymouth "But I'm over that now."
sonia @sad "I've got... {i}so much{/i} else to worry about... it barely even registers, honest."

red @confused "{w=0.5}.{w=0.5}.{w=0.5}."

sonia @happy "Ah, sorry. You probably don't want to hear my dull complaints."

red @talkingmouth "Hey, it's fine. I'm actually really interested in hearing what your vendetta against geologists is."
red @confused "Seems kinda weird, so there must be a good reason, right?"

sonia @talking2mouth "Well, I can't quite say if it's a good one, but, yes, I've got a bit of a history with geologists."

red @thinking "...Lay it on me."

sonia @talking2mouth "Have you ever heard of 'Wishing Stars'?"

red @talkingmouth "Yeah. They're, um, rocks that fall semi-frequently in Galar, right? And they're part of what powers the Dynamax phenomenon there."

sonia @closedbrow talkingmouth "Mostly right. What you just described was pretty much everything everyone in Galar knew about the Wishing Stars for... hundreds of years. And they'd been falling for {i}thousands{/i} before."

sonia @talkingmouth "Well, my Gran made it her life's work to investigate them properly. I helped. And we actually figured out something incredible, something that hundreds of years of past research hadn't shown up."

pause 1.0

sonia @sad "They're... not actually rocks."

pause 0.5

red @closedbrow talking2mouth "Ah. I think I can see where this is going."

sonia @happy "It does rather lay itself out, doesn't it? Yes, they're not rocks at all. Instead, they're parts of a super-ancient Pokémon, or otherwise definitively 'organic' entity."
sonia @surprised "Now, in total fairness, this entity's body is composed of a calcite-like mineralistic keratin which can be very easily mistaken for a rock, and definitely had, for hundreds of years."

redmind "Hm. She's cute when she's talking about something she's passionate about."

sonia @talkingmouth "But by analyzing the fragments of biological material still attached to the core of the Wishing Star, those trace fragments that survived the exosphere and impact with Earth--"
sonia @talking2mouth "I was able to determine that the Wishing Stars were, without a shadow of a doubt, organic."

pause 1.0

red @talking2mouth "Which made all the geologists in Galar hate you."

sonia @sad "Astrogeologists mainly, but... yes."

red @happy "What about the biologists, though?"

sonia @talkingmouth "Well, Gran and I did get a few letters from them thanking us for it. But the hatemail we got from those bloody rock nerds quite outstripped the former."

red @surprised "Jeez! I guess they were passionate about their field."

sonia @talkingmouth "If I had a pound for every letter I got threatening to 'stone' me... the pun aside, it was quite barbaric."

red @surprised "Did people lose their jobs over this? Why so much passion?"

sonia @talkingmouth "The chairman of the Galarian league had invested a {i}lot{/i} of money into gathering up Wishing Stars. There were huge payouts for anyone who could donate them to the league, or who could give him more information about them."
sonia @talkingmouth closedbrow "But as soon as Gran and I published our paper on the true nature of the Wishing Stars, those bounties dried up." 
sonia @sadmouth "The Chairman didn't explain his reasoning, just that his understanding of Galar's energy situation, and its solutions, had dramatically shifted."

red @confused "How so?"

sonia @talkingmouth "Not certain. There were rumors that he was going to try and build a rocket that could travel into space and mine the source of the Wishing Stars for the energy within."
sonia @closedbrow "I reckon that, if that {i}was{/i} his plan, us proving that these meteoroids were coming from a Pokémon would make it pretty hard to mine."

red @closedbrow talking2mouth "I get it."

sonia @sadbrow happymouth "So it's less that people 'lost their jobs' and more that... well, a lot of people were getting pretty wealthy before Gran and I published our paper."

pause 1.0

sonia @angry "Bloody cheapskate never {i}did{/i} pay us. Gran and... well, mostly just me. I could {i}really{/i} use that money right now..."

pause 1.0

red @talkingmouth "You know, we're kinda in the same boat."

sonia @surprised "Beg pardon?"
sonia @happy "I'm a Kobukan dropout, and you're the favorite of the Battle Team Captain."
sonia @surprisedbrow happymouth "I'm not sure I see the similarities there."

red @happy "Yeah, they're more than skin deep."

pause 1.0

red @talkingmouth "I say 'same boat' and I mean, well... I can't really pay for Kobukan, either."

sonia @surprised "{w=0.5}.{w=0.5}.{w=0.5}.Wot?"

red @sadbrow sweat happymouth "Yeah. I'm from a small town in the Southeast of Kanto. Pallet Town. Most people haven't heard of it. Have you?"

sonia @sad "'Fraid not. Sorry."

red @talkingmouth "No biggie. Anyway, yeah, I'm from a tiny town, and I lived in a tiny house, and it was just me and my Mom. I got into this school, but I can't afford it."

if (not IsBefore(4, 10, 2004)):#FIX THIS: Address if you pay your first semester
    red @closedbrow talking2mouth "I mean, we both obviously managed to pay for our first semesters, but I, at least, have no idea how I'm going to do my second."

sonia @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
sonia @talking2mouth "Something will come up."

red @confusedeyebrows talkingmouth "Really? Where's this coming from?"

sonia @talkingmouth "...I can't rightly say. But I have a feeling. I know when bad things are about to happen, but I also know when good things are about to happen. It's... well, I suppose you'd call it an ability."

if (not IsBefore(1, 5, 2004)):
    sonia @sadbrow happymouth "Though nothing of the sort resembling yours, of course."

sonia @talking2mouth "There's a group in Galar that believes in a concept called 'Karma.' Good things happen to those who've had bad happen to them, and vice versa."
sonia @happy "It's a comforting thought. That everything will balance out in the end."
sonia @talking2mouth "A lot of awful stuff has happened to me, but I'm certain that the good is just around the corner. And the longer I wait, the better it'll be."

pause 1.0

redmind @thinking "That's either some impressive optimism...{w=0.5} or {i}damaging{/i} delusion."

sonia @talkingmouth "I just need to get through the 'now', and tomorrow will be better."

pause 1.0

red @talking2mouth "...Hey. Would you be willing to tell me {i}why{/i} you left Kobukan last year?"
red @thinking "Was it {i}really{/i} because you discovered the Battle Team was hideously corrupt and evil, and you had to leave to train for a year until you were strong enough to come back and defeat them?"

pause 1.0

sonia @surprised "That sounds like something Leaf would say."

red @talkingmouth "Yeah, she did."

sonia @sad "So, people are talking about why I left... well, I suppose that's no surprise."
sonia @talkingmouth "No, I'm afraid it wasn't anything so stylish. I'm not some sort of secret agent, I don't have an exploding pen, I like my Martinis stirred, and I don't have any insidious dirt on the Battle Team."

pause 1.0

sonia @sad "That'd be a more fun story, honest."

pause 0.5

sonia @closedbrow "I'm willing to tell you, [first_name], but you'll probably just think less of me."

red @talkingmouth "Everyone slips and falls occasionally. I'm sure it's not that bad."

if (not IsBefore(1, 5, 2004)):
    red @talkingmouth "Besides, if you can overlook the whole 'Frienergy' thing..."

sonia @talkingmouth "...Right. Well, the story began in February."

red @thinking "Last year?"

sonia @talkingmouth "No, this year. Last {i}school{/i} year, but Kobukan runs a year-long program. So... just a couple months before you enrolled, I imagine."

red @talkingmouth "Ah, gotcha."

sonia @talkingmouth "I was part of the Battle Team. A decent battler, I think. I'd gotten through the first Quarter Qlash easily enough. Quarter Qlash two was quite a bit harder. Quarter Qlash three was... almost impossible."

red @confused "But you {i}did{/i} make it through."

sonia @talkingmouth "Yes. Not easily, but I managed it."

red @thinking "{w=0.5}.{w=0.5}.{w=0.5}."

sonia frownmouth @closedbrow talkingmouth "But that's when I... well, that's when... I'd only {i}barely{/i} gotten through QQ three. I needed to train harder. I started staying up at nights to train."

sonia @sadbrow talkingmouth "But then I ended up losing sleep, so I did poorer on my academics. I needed to focus more on that, so I started skipping lunches to study. The hunger made me even more tired, and I started falling asleep in classes."

pause 1.0

sonia @talkingmouth "I collapsed in Gym Class. Went {i}right{/i} out."
sonia @talkingmouth "Spent three days in the infirmary with pneumonia from my weakened immune system, due to lack of sleep or nutrition."
sonia @sad "Then they... had to send me to the {i}actual{/i} hospital to pump my lungs, and... the bill for that was enormous... and I was terrified of sending it to Gran, so..."

pause 1.0

sonia @closedbrow sadmouth "I'm sorry, I... I can't..."

red @sadbrow talking2mouth "Hey, it's alright. I understand. You don't need to explain anything. You can stop now."

pause 0.5

sonia @sadbrow happymouth "...No. No, I started this. So I should see it through to the end, shouldn't I?"

pause 0.5

sonia @talkingmouth "Well. After all that, I was a nervous wreck when it was time to actually show up for the fourth Quarter Qlash. All I could think about was my gym challenge in Galar, and how I'd failed that." 
sonia @sad "I had every advantage, but Opal still beat me handily."

pause 0.5

sonia @closedbrow talkingmouth "I couldn't bear to go through that embarrassment again. I couldn't... let everyone down again, like that."
sonia @sad "So I did exactly what I was most afraid of, and let everyone down anyway. I just ran away. I hid in Kobukan, renting out a small apartment with my pocket change, and taking on odd jobs at anywhere that would hire me."

red @talking2mouth "I'm sorry."

sonia @closedbrow sadmouth "I never intended to come back. But when I heard the music from the Stadium... a years' worth of memories rushed back into me, and I... I couldn't help but think that maybe I had another chance."

pause 1.0

sonia @angry "Of course, I may have slightly overlooked the fact that I couldn't possibly {i}afford{/i} a second chance."
sonia @sad "Dean Drayden was exceedingly generous for letting me re-enroll, even after the deadline. He often makes exceptions like that. But he can't just waive my entire tuitition fee."

pause 1.0

red @talkingmouth "Well, like you said. Something will come up."

sonia -frownmouth @happybrow sadmouth "I suppose that's all we can do for now. Keep the faith, right?"

red @happy "We'll make it through, Sonia. I believe it. We'll make it through together."

pause 1.0

sonia @surprisedbrow talking2mouth "Hm. Ness is pretty lucky, finding a guy like you."

red @surprised "Huh?"

sonia @sadbrow talking2mouth "Well, most of the guys she attracts are shallow idiots who just want her fame, or money, or nice arse. You seem {i}real.{/i}"

red @happy "Hey, that's a serious compliment. I'll put that on my review page."

pause 1.0

red @closedbrow talking2mouth "But, to be honest, I'm not really sure she attracted me. She was pretty forward when it came to, uh, setting up our date."

sonia @talking2mouth "Hm. That sounds like Ness, alright."

sonia @sadbrow happymouth "I almost wish that I {i}could have{/i} given you a test run for her."

red @confused "Um?"

sonia @happymouth "Hah! That's a joke. Sorry, in rather poor taste, wasn't it? Just a joke."
sonia @sadbrow talkingmouth "I haven't... really had anyone to talk to like this... or at all... for a couple months, since I was 'in hiding.'"

pause 0.5

red @talking2mouth "All your friends from last year are gone, then?"

sonia @talkingmouth "Yes. I'm... endlessly glad that Nessa's here with me, now, but... well, the only two people I know in this year, Janine and Nessa, are both a bit mad at me."
sonia @closedbrow talkingmouth "For good, reason, of course. But, since I arrived late, after most people were introduced to each other, I..."
sonia @sadbrow happymouth "It'd be nice if I had a [bluecolor]friend{/color} that wasn't angry at me."

pause 1.0

red @happy "You called?"

sonia @surprised "Hm?"

red @talkingmouth "A friend that's not mad at you. He's standing right here, he's got two thumbs, and his name is [first_name] [last_name]."

sonia @surprised "Oh! Um. Well... I mean, if you're not... against it... I could certainly help you out, I think I know quite a bit from my previous year, and--"

red @happy "Sonia, chill. You don't need to sell yourself to me. I like you. I want to be friends because of {i}you,{/i} not because of what you can do."
red @talkingmouth "You're passionate about your work, knowledgeable about research and Pokémon, and you're incredibly determined. When bad stuff happens to you, you just keep going, even if you have to do it alone."
red @sadbrow happymouth "I admire that about you. Seriously. So, yeah, I want to be friends."

pause 1.0

sonia @happymouth "I... um, I'd like that. If you wouldn't mind."

$ persondex["Sonia"]["Relationship"] = "Friend"
$ persondex["Sonia"]["RelationshipRank"] = 1

$ PlaySound("sav.wav")

narrator "Your heart shifts as you feel your relationship with Sonia evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

return