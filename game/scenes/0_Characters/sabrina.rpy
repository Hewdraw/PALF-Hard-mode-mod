init python:
    def SabrinaHasUnseenScene():
        if (GetCharValue("Sabrina") >= 10 and GetRelationship("Sabrina") != "Friend"):
            return "Sabrina1"
        return False

label Sabrina1:#FIX THIS: DO MASSIVE REWRITE OF THIS SCENE FOR WEEK 5

if (not IsBefore(1, 5, 2004)):
    $ persondex["Sabrina"]["Events"].append("Level2SceneVer2")

scene library
show sabrina
with Dissolve(2.0)

$ renpy.music.queue("Audio/Music/lavender.mp3", channel='music', loop=True, fadein=0.0, tight=None)
    
red @talking2mouth "Sabrina. We need to talk."

pause 2.0

redmind @thinking "...Did she hear me?"

sabrina @talkingmouth "Yes. I am waiting for you to tell me what you want to talk about."

red @confusedeyebrows talking2mouth "Wait, don't you know?"

sabrina @sad "Yes. But I am trying to pretend to be {w=0.5}ignorant."

sabrina @talkingmouth "It comforts most people."

redmind @thinking "Geez."

sabrina "{w=0.25}.{w=0.25}.{w=0.25}."

red @thinking "Look. You said you didn't want me trying to help you. And you also said that I didn't need to worry about you telling people about Frienergy."

sabrina @talkingmouth "That is correct, yes."

red @talkingmouth "Well, why?"

sabrina @talkingmouth "To which part?"

red @talkingmouth "Both. But I figure the first one is a more sensitive topic, so I guess you can answer the second one first."

sabrina @closedbrow talkingmouth "You presume to have access to my time."

red @confusedeyebrows talkingmouth "Are you busy?"

sabrina @sad "...No."

red @happy "Then, yeah, I presume the hell out of my access to your time. Or whatever you said."

sabrina @happymouth "...Hm. Amusing."

sabrina @closedbrow "My lack of desire to expose your secret is very simple."
sabrina @talkingmouth "I do not have any reason to."

sabrina @sad "Doing so would be a malicious act, and you have done nothing wrong to me."

red @sad "Er... even that thought I had when we first met? The, uh, 'inappropriate' one?"

sabrina @talkingmouth "I have been hearing thoughts far worse than that since I was far too young to handle them."
sabrina @sad "It is a reprieve, in some ways, to hear that sort of thought from someone who is not utterly detestable to the eye."

red @confusedeyebrows talkingmouth "'Not utterly detestable to the eye?' Gotta put that one in my book of compliments."

sabrina @sad "Besides, even if I did intend to act with malice towards you... I believe exposing your power is a bridge too far."

red @confusedeyebrows talking2mouth "What do you mean?"

sabrina @talkingmouth "I am aware of the effect I have on people."

pause 2.0

sabrina @neutralpowered poweredbrow "...No, {i}not{/i} that effect. The effect of fear."
sabrina @closedbrow talkingmouth "They feel discomfort around me. And I cannot blame them. Secrets, fantasies, shadows... the very core of people's identities... are laid bare to me the moment they become aware of my power."

red @thinking "Yeah, I guess most people can't help thinking of something the moment they realize they shouldn't think of it."

sabrina @sad "I have resigned myself to this fate of isolation. To the point I now volunteer the truth of my power."
sabrina @talkingmouth "I used to attempt to hide it. In vain."
sabrina "{w=0.25}.{w=0.25}.{w=0.25}."
sabrina @closedbrow talkingmouth "No more. I will live as myself amongst others, or live as myself, by myself. I will discard my cares of another's thoughts."
sabrina @sad "Destiny burdens me too much to ask me to wear a mask, too."

red @thinking "So... you really have given up."

sabrina @talkingmouth "Entirely."

pause 2.0

red @happy "Man, that's a load of shit!"

sabrina neutralpowered poweredbrow "...I beg your pardon?"

red @talkingmouth "You haven't given up. Not yet. And there are three ways I can tell, even without reading your mind."

sabrina "Do share your theory with me. But speak carefully. Telepathy is only one of my many psychic skills, and amongst my least invasive."

red @talking2mouth "The first is that you're telling me all this. When you told me about your powers, and now, you've been apologetic. You know what an apology is, right?"
red @happy "It's asking someone to overlook something you've done wrong. Now, you haven't done anything wrong, but the fact you want me to overlook something means you care about what I think. Literally."

pause 2.0

red @talking2mouth "The second thing is that you're here in Kobukan. It's not easy to get in. And--correct me if I'm wrong--I don't think anyone forced you to come here."

if (GetRelationship("Dawn") != "Classmate"):
    red @thinking "I know one girl was forced to come here, but you're basically as different from her as I could imagine."

red @thinking "Am I right?"

sabrina -neutralpowered -poweredbrow @talkingmouth "You are correct. I was not forced to come here."

red @happy "Cool. Kobukan's a school with tons of busy people with strong ambitions and goals, and very active minds, all crammed into a single campus. You probably dorm with four other girls, right?"
red @sad "...I don't know how your power works, exactly, but I have to imagine being around a lot of people doesn't make things any quieter."

sabrina @talkingmouth "And why do you think that?"

red @talkingmouth "You're here, in the back corner of the library, alone."

sabrina "{w=0.25}.{w=0.25}.{w=0.25}."

redmind @thinking "Am I right?"

redmind @happy "{color=#600080}Yes.{/color}"

red @happy "Nice."

sabrina @talkingmouth "What's the third thing, then?"

red @talkingmouth "Well, it's, uh...{w=0.5}{nw}" 
extend @happy "You're beautiful."

show sabrina blush with Dissolve(2.0)

sabrina @talkingmouth "I don't see how that's relevant to anything."

red @happy "Well, I might be totally off-base, here, but... your hair is really shiny and straight, so you gotta be using some kind of special shampoo. And you comb it every day, too, right? Hair that long, probably multiple times a day."
red @talkingmouth "Your posture is, like, incredible. I've never seen someone with a straighter back."
red @happy "And, well, your outfit is... very flattering. And you know it. You know what people think when they see you."

sabrina @closedbrow talkingmouth "It is typical of a man to believe I adorn myself for his pleasure."

red @talking2mouth "I don't think it's for me. I think you heard people mentally needle and point out tiny flaws in your appearance over and over, until you eliminated them."

sabrina "{w=0.25}.{w=0.25}.{w=0.25}."

sabrina @talkingmouth "Even if that's true, how would that indicate that I haven't fully discarded the thoughts and opinions of others?"

red @happy "Well, you heard people's thoughts, and changed yourself. Unless I'm meant to believe that you were born this way."

sabrina -blush @talkingmouth "...You are...{w=0.5}{nw}"
extend @sad " Not entirely incorrect."

pause 2.0

redmind @thinking "Well? Tell me more."

pause 2.0

sabrina @talkingmouth "Espers are not uncommon. Not as uncommon as many would think, in any case."
sabrina @closedbrow "There are communities of Espers that live together in every region. Sometimes, they even manage to develop a culture and society that can exist alongside Euthymics'."
sabrina @talkingmouth "A 'Euthymic' is what Espers call non-Espers."
sabrina @sad "But... I could not live in one of those communities."

red @confusedeyebrows "...?"

sabrina @talkingmouth "Espers live together in peace, taking advantage of their abilities without suffering the downsides as I do."
sabrina @closedbrow talkingmouth "For the vast majority of Espers, their powers are voluntary. Mine are not. I do not believe they ever will be."
sabrina @closedbrow "When I am forced to read the mind of an Esper, reading the mind of another, who was possibly reading another... it was an excrutiating feedback loop. Debilitating headaches followed. I cannot be around them."

red @surprised "Oh, wow. Like when Roxanne blasted out our ears during orientation?"

sabrina @closedbrow "Yes. Constantly."
sabrina @talkingmouth "...So I sought a place in the Euthymic world. And still seek it now, as you have proven. As much as I may try to deny it, or tell myself that I've given up caring."

red @talking2mouth "...Maybe you should try {i}not{/i} immediately telling people that you read minds? It might be easier to fit in."

sabrina @sad "I have tried that. My precious friend felt betrayed. She hated me, then. And I could feel her thoughts turn from love to poison."
sabrina @talkingmouth "No. If I am to imbibe poison, then I will prepare the chalice for myself, at a time of my choosing."

red @sad "Oh... I'm really sorry to hear about your friend..."
red @thinking "But you can't give up just because one person reacted negatively!"

sabrina "{w=0.25}.{w=0.25}.{w=0.25}."
sabrina @talkingmouth "Would you risk letting a single one of your friends know of your... 'Frienergy?'"
sabrina @sad "I know it is not mind control. It's a conduit for empathy, at its strongest."
sabrina @talkingmouth "But my power is also not mind control. Nor is it 'soul-stealing,' 'witchcraft,' or 'evil.'"
sabrina @sad "And yet... it has been described as such by many."

red @thinking "...Hm. Was it described as that aloud? Or did you get that from peoples' minds?"

sabrina @closedbrow "None have ever chosen to state those sorts of true feelings to my face. I don't see what difference it makes, though."

red @happy "I think it makes a huge difference, actually."

sabrina ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talkingmouth "Oh?"

red @thinking "Yeah. I mean, people have all kinds of intrusive thoughts, you know?" 
red @talkingmouth "You know, more than anyone, that people can't help but think of the worst things at the worst possible times when they're around you."
red @happy "But if they choose not to say it, then they're making a choice to be better than their instincts. Sure, maybe they're just trying not to make you angry or whatever..."
red @talkingmouth "But I bet if that was the case, you would know what their intentions were, too, right?"

sabrina @talkingmouth "Are you trying to convince me that there is something governing peoples' actions other than their thoughts?"
sabrina @sad "Pity. I thought this conversation was going somewhere."

red @talking2mouth "...People aren't machines, Sabrina. You can't just read the code from their heads and know exactly what they're going to do."
red @happy "Sometimes, even if they're thinking one thing, they're going to do the exact opposite."

sabrina @talkingmouth "I challenge you to name one situation in which that's the case."

red @happy "Well, you're pretty difficult to talk to, right?"

sabrina @sad "As you have constantly been thinking, yes."

pause 2.0

red @talkingmouth "I'm still here, aren't I?"

sabrina @closedbrow "...Now, that {i}is{/i} strange. Why?"

red @talkingmouth "Because I want to help you. And I have no idea how, and I don't even know where to begin, and I might not ever be able to help you with your powers."
red @happy "But I can at least be your friend. We can be weird power buddies!"

sabrina @sad "Our powers are in no way comparable."

red @talkingmouth "Uh-huh."

sabrina "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talkingmouth "Fine."

red @happy "Sweet! So--"

sabrina @closedbrow "No, I will not help you cheat on tests. No, I will not help you win at cards. No, I will not..."
sabrina "..."
sabrina @talkingmouth "You want me to send you the lyrics to songs while you're doing karaoke, so you can pretend to have memorized them?"

red @happy "Yeah!"

sabrina @sad "A person with my powers could be ruling nations, or upending dynasties. And you want me to use my powers to make you seem better at karaoke."

red @confusedeyebrows talking2mouth "Be honest with me--what have you actually used your powers for? On purpose? Because it sounds to me like you've mostly been trying to avoid them."

pause 2.0

sabrina @closedbrow "...I used them to win at blackjack once. I needed some money, shortly after I moved to Inspira."
sabrina @sad "I wasn't allowed to keep my winnings, though. Not because I read the dealer's mind, but because I was under twenty-one, and shouldn't have been in the casino in the first place."

red @surprised "Geez. Did you get arrested?"

sabrina @closedbrow "...No. The dealer was also an Esper, actually. He said he wouldn't turn me in as long as I became his protégé."
sabrina @talkingmouth "Eventually, he got me a job at the same casino. Which is where this particular outfit comes from."
sabrina @happymouth "He is bombastic, and showy, and ridiculous... not to mention a weak Esper... but he does give me hope that life amongst the Euthymics is possible."

red @happy "Well, see? The one time you used your powers, instead of trying to hide from their effects, everything turned out fine."

sabrina @talkingmouth "We'll see. The future has yet to arrive."
sabrina "{w=0.5}.{w=0.5}.{w=0.5}."
sabrina @talkingmouth "I would ask two questions, which I have not been able to figure out, even as I search your mind."

red @talkingmouth "Oh, sure. What is it?"

sabrina @closedbrow "When you were stating those three facts, which proved to you that I still hold onto some vain hope of 'normalcy...' I could never see what your next argument would be until you were already saying it. How?"

red @happy "Oh, that? Yeah, I was just improvising like crazy there. I pretty much only came up with each argument after I'd already started saying it."

sabrina @sad "So when you said you had three things...?"

red @thinking "It might've been more accurate to say that I was {i}going to figure out{/i} three things."

sabrina @happymouth "{w=0.5}.{w=0.5}.{w=0.5}."
extend @closedbrow happymouth "Remarkable. Your mind works fast, considering how empty it is."

red @angrybrow frown2mouth "Hey. It might be mostly empty, but I've got enough wrinkles in the ol' thinkmeat to get offended."
red @happy "...But not for long. So what was your second question?"

sabrina @sad "Why is that song about the baby Sharpedo playing in your head? Just... over and over...?"

red @thinking "Oh, yeah, I, uh... I heard it, like, a week or two ago."

sabrina "..."

red @talking2mouth "So it'll probably be another month or so before it leaves."

sabrina @sad "If we are to spend more time together, could you not... perhaps... get some classical piano stuck in your head? Something that fades into the background?"

red @happy "I mean, I could try."
redmind @surprised "Wait! We're going to be spending more time together?"

show sabrina blush with dis

redmind "{color=#600080}You said that you would be my friend. I am given to understand friends... 'hang out.'{/color}"
redmind @happy "We sure do. Give me some time to figure out where we should go, alright?"

sabrina @happymouth "...Very well. Is it alright, then, if I contact you in the future? Through your mind? If you think of me, I will know."

redmind @happy "Kinda scary to hear that, but sure!"

$ BecomeContacted("Sabrina")

sabrina happy "Thank you. My {color=#0048ff}friend{/color}."

$ persondex["Sabrina"]["Relationship"] = "Friend"
$ persondex["Sabrina"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Sabrina evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

return