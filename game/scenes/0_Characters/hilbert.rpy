init python:
    def HilbertHasUnseenScene():
        if (GetCharValue("Hilbert") >= 10 and personalstats["Knowledge"] >= 4 and GetRelationship("Hilbert") != "Light"):
            return "Hilbert1"
        return False

label Hilbert1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Hilbert"]["Events"].append("Level2SceneVer2")

scene city_B
show hilbert:
    xpos 0.5 ypos 0.9 zoom 0.8
with Dissolve(2.0)
stop music fadeout 1.5
show screen songsplash("Victory Road", "Zame")
queue music "audio/music/victory.mp3" fadein 1.5

narrator "You're in Inspira when you come across Hilbert, standing, frozen, staring at a statue."
narrator "His unmoving body cuts through the waves of people splitting around him like the hull of an icebreaker, uncaring of the flow of humanity all around."

pause 0.5

red @talkingmouth "Hey, Hilbert."

hilbert @surprised "Hm? Oh."

pause 0.5

hilbert @talkingmouth "It's you."

red @thinking "Warm as ever."

show hilbert:
    ease 0.5 ypos 1.0 zoom 1.0

pause 0.5

red @talkingmouth "Checking out the modern art?"

hilbert @talkingmouth "No. This is {i}classical{/i} art. Pre-renaissance. Medieval."

red @confused "Wait, isn't Kobukan a really new region? Just a couple hundred years?"

narrator "Hilbert rolls his eyes and wordlessly points at the plaque on the bottom of the statue."

narrator "You take a better look at the statue. It is composed of iron, and appears to be of a knight, sword upraised and mouth frozen in an eternal rallying cry."
narrator "At the dark knight's feet is a child, swaddled up in the knight's discarded cape."

"Plaque" "IN MEMORIAM OF\n{w=0.5}THE SACRIFICES REQUIRED TO\n{w=0.5}FREE UNOVA OF KINGS." 
"Plaque" "LET KOBUKAN BENEFIT.{w=0.5}\n{size=15}(Paid for by the Unovan Heritage Association.){/size}"

hilbert @talkingmouth "Hmph."
hilbert @closedbrow "A 'gift' from Unova. More like a reminder of what Kobukan owes them."

red @talkingmouth "You think they gifted Inspira the statue just to remind people that Unova is nearby, and very powerful?"
red @happy "I think anyone with a map would remember that one."

hilbert @closedbrow talkingmouth "People don't remember anything that isn't in their face."

narrator "Hilbert's voice is thick with bitterness."

red @talking2mouth "...Do you want to talk?"

if (IsBefore(1, 5, 2004)):
    hilbert @sadmouth "How long have we been roommates? You know this. Obviously, I don't want to talk."

else:
    hilbert @talkingmouth "How long were we roommates? You know this. Obviously, I don't want to talk."

red @confused "...Right."

pause 1.0

red @thinking "What if I wanted to talk?"

hilbert @thinking "I would not be surprised. Has anyone ever told you you're a chatty gossip, [first_name]?"

red @talking2mouth "Yeah. [blue_name]."

red @confused "Has anyone ever told you that you need to work a bit harder at getting along with people?"

pause 0.5

hilbert @smilemouth "Yes. Hilda."

red @closedbrow talkingmouth "That checks out."

pause 1.0

red @talkingmouth "So, what's your story with her?"

hilbert @sad "...It really is impossible to turn you off, isn't it?"

red @talkingmouth "Kinda, yeah."

hilbert @talkingmouth "Fine. Let's go find somewhere to sit down, though. I can't stand up any longer."

narrator "Peering closer at Hilbert, you do notice that he's starting to sweat quite a bit in the cool air, as though he was physically over-exerted."

red @talkingmouth "Uh, sure. A friend of mine has a house here. Want to go there? It's a bit more shaded."

hilbert @closedbrow talkingmouth "How far?"

red @confused "Uh, about two miles."

hilbert @talkingmouth "That's a long walk."

red @confused "It's like, fifteen minutes, tops. You can do it."

hilbert @talkingmouth "It's two miles. In order to get there in fifteen minutes, we'd need to walk at eight miles an hour. The average walking speed is three miles per hour. If you--"

show hilbert surprised with dis

narrator "You begin walking away."

hilbert "Wait. Wait, no, come back! I wasn't--"

scene black with splitfade

narrator "You make your way to Silver's house, Hilbert in hot pursuit. Every time he gets within ten feet of you, he attempts, indignantly, to explain through his labored breathing why this walk {i}is{/i}, in fact, too long."
narrator "Of course, he never gets the chance." 
narrator "By the time he's regained his breath enough to speak, you've already moved thirty feet away from him, using your long legs and not-utterly-ignored musculature to your advantage."

pause 0.5

narrator "You sneak a peek over your shoulder at his small form hurrying after you, and you can't help but smirk. He's actually kinda cute... {w=0.5}when he isn't talking, anyway."

scene abandonedhouse 
show hilbert angry at night
with splitfade

hilbert "{w=0.5}Hah... {w=0.5}Hah... {w=0.5}...Hah. D-don't... {w=0.5}Hah..."

red night @happy "See? Told you you could make it."

hilbert @closedbrow angrymouth "And I... told {i}you...{/i} that it was too long a walk."

pause 2.0

hilbert -angry @talkingmouth "...Where are we?"

red @talkingmouth "A friend's house."

hilbert @angrybrow talkingmouth "Your friend lives in a shack in the middle of the city?"

if (IsBefore(26, 4, 2004)):
    red @talkingmouth "We can't {i}all{/i} live in palaces, Prince Hilbert."
else:
    red @talkingmouth "We can't {i}all{/i} live in palaces, Prince von Schwarzdrachen."

hilbert @surprised "What?"

red @talkingmouth "Oh, I just called you--"

hilbert @talkingmouth "No, I know {i}what{/i} you said. {i}Why{/i} did you say that name?"

red @talking2mouth "...I dunno, man. Sorry if I crossed a line. I was just poking fun at you, since you were acting kinda... princely."

hilbert @sad "...Tch. That's what my mother used to call me."

red @closedbrow "Aurea?"

hilbert @closedbrow "No, Professor Juniper is my guardian. My {i}mother.{/i}"

red @thinking "Um... Hilda?"

pause 1.0

hilbert @closedbrow talkingmouth "{size=30}God.{/size}"

red @happy "Sorry, Hilbert! I don't think you've mentioned your mother before."

hilbert @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.I thought I had.{w=0.5} I suppose I forgot."

red @talkingmouth "Well, now's as good a time as any, right?"

hilbert @talkingmouth "She's dead."

red @surprised "Oh."

hilbert @talkingmouth "Father's dead, too."

red @sad "Oh."

hilbert @talkingmouth "They were murdered. Right in front of me."

red @sad "Oh..."

hilbert @talkingmouth "And I swore, on that day, that I would kill the one responsible."

red @surprised "Oh!"

pause 1.0

red @talking2mouth "Wait, {i}kill{/i}?"

hilbert @talkingmouth "Yes."

red @talkingmouth "Not... 'find'? Or 'bring to justice'? Or even 'punish'?"

hilbert @talkingmouth "No. Kill. Revenge is my ideal. I've no interest in the truth."

pause 1.0

red @closedbrow talking2mouth "That's... pretty heavy, man."

hilbert @talkingmouth "It's the only thought that's occupied my mind for many, many years. I've been plotting. Hating. Dreaming of when I could get my revenge."
hilbert @angry "I have been wallowing in darkness. To the point the dark, and the cold, has become my own bitter blade."

red @talkingmouth "Uh..."

hilbert @angry "The dragon of the meteor will die at my hand. And then, if there's a life left for me..."

pause 0.5

hilbert @talkingmouth "...I guess I'll go to prison."

red @surprised "What?"

if (not IsBefore(1, 5, 2004)):
    redmind @frownmouth "The dragon of the meteor? He can't be... he {i}can't{/i} be talking about Tia, can he?"
else:
    redmind @frownmouth "The dragon of the meteor? He can't be... he {i}can't{/i} be talking about Rayquaza, can he?"

hilbert "{w=0.5}.{w=0.5}.{w=0.5}."

hilbert @talkingmouth "You don't seem phased."

red @talking2mouth "Honestly, I'm just not sure how to react. This is a lot you're dropping on me."

hilbert @sad "Do you see why I don't talk, now? Can you imagine what it's like trying to have friends, have a normal conversation, when you've been planning a death ever since you were twelve?"

if (not IsBefore(1, 5, 2004)):
    hilbert @talkingmouth "I despise how easily it comes to you. I loathe that you made me trust you, when you knew full well what power you had."

    red @sadbrow "Hilbert, I didn't know about Frienergy until a couple weeks into the year..."

    hilbert @angry "And when you found out, did you tell me about it? Did you tell anyone?"

pause 1.0

red @talking2mouth "No."

if (not IsBefore(1, 5, 2004)):
    hilbert @talkingmouth "Of course you can't."

else:
    hilbert @talkingmouth "Of course you didn't."

pause 1.0

hilbert @talkingmouth "You can go."

red @confusedeyebrows frownmouth "Hm?"

if (IsBefore(1, 5, 2004)):
    hilbert @talkingmouth "I haven't shared my dream with anyone. Ever. Because I knew the instant I did, there would be someone out there trying to stop me. So, that's you, now."
else:
    hilbert @talkingmouth "The only person I've shared my dream with is Nate. And he's got enough problems that {i}my{/i} dream didn't even phase him."
    hilbert @closedbrow talkingmouth "But you're different. You're kind. You can't just shrug this off, like he can."

hilbert @talkingmouth "I shouldn't have told you."
hilbert @sad "You made me trust you. And I resent you for that. Someone with my dream can't afford to trust."

pause 1.0

red @sad "...Hilbert."

hilbert @talkingmouth "Yes."

red @closedbrow frownmouth "I... can't begin to understand the pain you're going through, but killing isn't the answer."

hilbert @talkingmouth "Then what is? 'Forgiveness'? 'Living well'?"

red @thinking "Um... I'd try just talking it out with the person you've got a vendetta against."

hilbert @closedbrow talkingmouth "...Whatever. When you see everything with blackened eyes, the world looks dark. 'Living well' is impossible."

pause 1.0

red @talkingmouth "Look, Hilbert, I--"

hilbert @closedbrow "I'm bored of this conversation. Where did you get that hat?"

red @confused "Huh?"

hilbert @talkingmouth "Your hat."

hilbert @sad "It looks like a first edition Pokémon League Expo hat. It's probably a counterfeit, though, since they were only on for a limited run."
    
red @happy "Oh, uh... Old Man Oak gave it to me. Er, Professor Oak, I mean."

hilbert @talkingmouth "Can I see it?"

red @thinking "Sure?"

narrator "You hand over your hat."

hilbert @talkingmouth "Hm. This is the official seal of the Kantonian Pokémon League."

"{color=#cf0000}[first_name]{/color}" "\"Huh. Is that valuable?\""

pause 1.0

hilbert @talkingmouth "{i}Why{/i} are you hiding underneath the table?"

"{color=#cf0000}[first_name]{/color}" "\"Oh, just tying my laces.\""

hilbert @angrybrow talkingmouth "Really? Because it looks to me like you're trying to hide your head."

"{color=#cf0000}[first_name]{/color}" "Nope! I'm not."

pause 1.0

hilbert @talkingmouth "Whatever. Take the hat back."

pause 1.0

red @talkingmouth "Thanks."
red @thinking "...But, really, what was that about?"

hilbert @talkingmouth "There are exactly seven hundred and forty-eight of those hats in existence. They were manufactured in 1989." 
hilbert @talkingmouth "They were the last Kantonian League Expo hats ever made." 
hilbert @talkingmouth "This is because, mid-manufacturing, Lance won his thirty-fourth attempt at beating the Kanto league, and the Kanto League Expo was merged with the Johto League Expo into the Indigo League Expo."

hilbert @talkingmouth "These hats were given away as novelties at the expo, along with their Johto counterparts, which had finished their production run, and numbered in the thousands."

pause 1.0

hilbert @talkingmouth "These hats, mementos of a single, significant moment, that could never be replicated, were just {i}given{/i} away. Alongside the new first edition Indigo League Expo hats, which are now a dime a dozen."

hilbert @talkingmouth "Of that cancelled run of Kantonian League Expo hats, five hundred and sixteen are in the hands of private collectors. One hundred and two are in museums. Lance owns three, and gave one to Janine." 
hilbert @closedbrow talkingmouth "And the rest are unaccounted for."

pause 1.0

$ PlaySound("idea.mp3")

red @surprised "Wait. So, what you're telling me is... this hat is {i}really{/i} valuable?"

hilbert @talkingmouth "It could be."

show hilbert:
    ease 0.5 ypos 1.2 zoom 1.3

narrator "Hilbert snatches the hat off your head and gestures at its insides angrily."

hilbert @angrybrow talkingmouth "If you hadn't {i}soiled{/i} it with your greasy hair, and... and your... dandruff!"

narrator "Hilbert tosses the hat back to you."

red @surprised "No, this really matters. Like, how valuable was it, before I used it for ten years?"

hilbert @closedbrow "Easily $1,500,000."

red @sad "Oh, no... and how much is it worth now?"

hilbert @angry "After ten years of use? $70,000 maximum."

pause 1.0

red @closedbrow sadmouth tears "Oh... I could have been rich..."

if (IsBefore(1, 5, 2004)):
    hilbert @talkingmouth "Ugh. I'm actually glad we had this talk. At least now you appreciate your damn hat more. It physically pained me seeing you going to bed every night with it on. You don't even put it on the nightstand or anything."

else:
    hilbert @talkingmouth "Ugh. I'm actually glad we had this talk. At least now you appreciate your damn hat more. It physically pained me seeing you going to bed every night with it on. You didn't even put it on the nightstand or anything."

pause 0.5

if (IsBefore(1, 5, 2004)):
    red @talking2mouth "Hey... do you watch me sleep?"

    hilbert @talkingmouth "I watch everyone in the room sleep. You're not special."

    red @confused "Sorry if this is a dumb question--"

    hilbert @closedbrow talkingmouth "Just don't ask it."

    red @angrybrow talking2mouth "No, I'm going to ask it. Why do you watch us sleep?"

    hilbert @talkingmouth "I'm scared of the dark. Watching you four sleep reminds me that I'm not alone."

else:
    red @talking2mouth "Hey... did you watch me sleep?"

    hilbert @talkingmouth "I watched everyone in that room sleep. You're not special."

    red @confused "Sorry if this is a dumb question--"

    hilbert @closedbrow talkingmouth "Just don't ask it."

    red @angrybrow talking2mouth "No, I'm going to ask it. Why did you watch us sleep?"

    hilbert @talkingmouth "I'm scared of the dark. Watching you four sleep reminded me that I'm not alone."
    hilbert @talkingmouth "I do the same thing in my new dorm."

pause 1.0

red @surprised "What?"

hilbert @angry "What is {i}wrong{/i} with your ears?"

red @talking2mouth "Is that, like, really dry sarcasm?"

hilbert @sad "You mean the lowest form of wit? No, it's not."

pause 1.0

hilbert @talkingmouth "Tch. This whole conversation has been a waste of time. And now I've forgotten why I even came to Inspira in the first place."

red @talkingmouth "...I think I know."

hilbert @talkingmouth "Then keep it to yourself."

pause 1.0

red @talkingmouth "You're serious about wanting to kill the one responsible for your parents' death?"

hilbert @talkingmouth "I would die for it. Attendance at Kobukan just gives me the power and resources I need to make it happen."

pause 1.0

red @closedbrow "I can't let that happen. For your safety."

hilbert "{w=0.5}.{w=0.5}.{w=0.5}."

red @talkingmouth "...But I'll help you find the one responsible, if you can tell me about them."

hilbert @talkingmouth "I accept your help."

red @surprised "Woah. That easily?"

if (IsBefore(1, 5, 2004)):
    hilbert @talkingmouth "I'm not in any position to be turning down offers of aid. Besides, you're... {w=0.5}competent. I would welcome your aid as my... compatriot."

else:
    hilbert @sad "Your power affords you... communicative ability. I'm not in any position to be turning down people who can provide that. Besides, you're... {w=0.5}competent. I would welcome your aid as my... compatriot."

red @talkingmouth "That's{w=0.5}.{w=0.5}.{w=0.5}.{nw}"

hide hilbert with dis

extend @surprised " Oh, he just walked away."

pause 0.5 

red @talkingmouth "Well, I don't much like the sound of 'compatriot.'"
red @thinking "Before I go back to campus, I should probably swing by a store. I think I can think of a little present Hilbert might appreciate."

pause 2.0

show silver surprisedbrow at night with dis

pause 2.0

silver @talkingmouth "What the fuck...?"

scene black with Dissolve(2.0)

narrator "When Hilbert returns to his room later, he finds a little box on his nightstand. Opening the box, he sees a small, Vanillite-shaped object."

if (IsBefore(1, 5, 2004)):
    narrator "Turning it over, its form and function becomes apparent. It's a nightlight. Hilbert wordlessly plugs it in, nodding his thanks at you."

    pause 0.5

    narrator "In the dim light, you think you can see traces of a smile. It seems he appreciates his {color=#0048ff}light{/color}."

    pause 0.5

    narrator "Whatever the case, Hilbert's behavior certainly becomes more tolerable, raising the morale of everyone in the room."

else:
    narrator "Turning it over, its form and function becomes apparent. It's a nightlight. Hilbert wordlessly plugs it in."

    pause 0.5

    narrator "Were you there, in the dim light, you may be able to make out traces of a smile. It seems he appreciates his {color=#0048ff}light{/color}."

    pause 0.5

    narrator "Whatever the case, Hilbert's behavior certainly becomes more tolerable, raising the morale of all his dormmates."

if (IsBefore(1, 5, 2004)):
    $ ValueChange("Calem", 1, 0.25, False)
    $ ValueChange("Ethan", 1, 0.5, False)
    $ ValueChange("Brendan", 1, 0.75)
else:
    $ ValueChange("Bea", 1, 0.2, False)
    $ ValueChange("Nate", 1, 0.4, False)
    $ ValueChange("Hilda", 1, 0.6, False)
    $ ValueChange("Bianca", 1, 0.8, False)

$ persondex["Hilbert"]["Relationship"] = "Light"
$ persondex["Hilbert"]["RelationshipRank"] = 1

$ PlaySound("sav.wav")

narrator "Your heart shifts as you feel your relationship with Hilbert evolve from '{color=#0048ff}Dormmate{/color}' to '{color=#0048ff}Light{/color}'!"

return