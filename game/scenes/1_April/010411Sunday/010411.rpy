############################################################################################################################################################################################################################
# APRIL 11
# FREE EXPLORATION BEGINS

############################################################################################################################################################################################################################
############################################################################################################################################################################################################################
############################################################################################################################################################################################################################

label day010411:
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_4

stop music

scene blank2
show morning at vspaz

pause 3.5

queue music "Audio/Music/Road to Viridian City.ogg"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red "Morning time, huh? I almost slept in! Alright, gotta run!"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
pikachu neutral_2 "Pikachu!"

red @talkingmouth "Good morning, buddy. Sleep well?"

show brendan at rightside
show ethan at centerside
show calem at leftside
with dis

brendan @talkingmouth "No doubt, bro. [pika_name] looked tired as hell after our all-day trip yesterday.{w=0.5}{nw}"
extend @happy " He went out like a light!"
    
red @happy "I dunno, the lazy lil' guy always sleeps like a log, even if all he's been doing is napping."
red @talkingmouth "That's why I gotta make him run, so he doesn't get too fat. Speaking of which--hop to it, [pika_name]!"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
pikachu sad "Pi-ka..."

red @happy "It's for your own good, buddy. Can't have you developing the 'beetus!"

calem @talkingmouth "Do you know where you're going?"

red @talkingmouth "Nope, but I'll find out when I get there!"

ethan @happy "Alright! Seeya, dude!"

scene relichall_A with splitfade:
    zoom 1.0 align (0.5, 0.5)

redmind "Alright, I've finally got some time to myself. I can finally go out and train my Pokémon... or maybe just hang out with some friends?"

redmind "Whatever the case, I just want to put this 'Frienergy' stuff out of my head. I can't stop thinking about it..."

show sabrina with dis

sabrina "Frienergy?"

if (classstats["Psychic"] + classstats["Ghost"] > 5):
    red @surprised "Ah, shit, no! Sabrina, stop! Don't read my mind!"

    pause 2.0

    sabrina @sad "...I can't help it. You know this."

    red @thinking "Yeah, I guess..."

else:
    red @surprised "H-huh?! What? Who are you?"

    sabrina @sad "...You don't want to know. You want to know how I know about your Frienergy power."

    red @thinking "I mean, yes, I'd like to know that, too..."

    $ BecomeNamed("Sabrina")
    sabrina @talkingmouth "I am the Esper Sabrina. I read minds."

    red @angrybrow frownmouth "Could you not read mine, then? That's a {i}massive{/i} violation of my privacy."

    sabrina @sad "...I cannot stop."

    red @surprised "Huh?"

    sabrina @neutralpowered poweredbrow talkingmouth "My telepathy is involuntary. You were thinking {i}very{/i} loudly about this... 'Frienergy.'"

    red @thinking "Wait, so... anything I think about, you know? Whether or not you want to?"

    sabrina @talkingmouth "Yes."

    red @surprised "Oh, shit. Uh, forgive me for this!"

    pause 2.0

    sabrina @closedbrow "...What, are you expecting me to call you a pervert?"

    red @thinking "I mean, it'd be fair..."

    sabrina @talkingmouth "Hmph. It's not your fault. It's natural."

    red @surprised "Really? That's... uh, that's really understanding of you."

    sabrina closedbrow "I understand people more than anyone else. I wish I could stop."

    pause 2.0

    sabrina -closedbrow "Don't you dare think that."

    red @surprised "What?"

    sabrina neutralpowered poweredbrow "You can't help me. No-one can."

    red sad "You're... just giving up?"

    sabrina @talkingmouth "...Allow me to make a correction. Stay away from me. {i}That's{/i} how you can help."

    red "I mean... I didn't even know you existed until you popped up in front of me and casually mentioned something I've been trying to keep very secret!"

sabrina -neutralpowered -poweredbrow @sad "I apologize. I should not have said anything. I simply thought for a moment that you might... no, nevermind."

red @thinking "No, I know, I just... I mean... that's {i}really{/i} personal!"

sabrina @talkingmouth "...Yes. I {cps=2}apologize.{/cps}"

red @sad "I mean, I know it's not your fault. But... crap, what do I do now? No-one else was supposed to know!"

sabrina @talkingmouth "...You want me to keep it a secret."

red @sadeyes sadeyebrows talking2mouth "Please!"

sabrina @talkingmouth "Your secret is safe with my indifference."

hide sabrina with dis

pause 2.0

redmind @thinking "In-indifference? How can she be indifferent about this? I've got a massive secret that I'm hiding from everyone!"

redmind @surprised "{color=#600080}As do all.{/color}"

redmind @surprised "Wh-what the hell? I didn't think that. Did she just speak directly into my mind?"

redmind @surprised "{color=#600080}Yes.{/color}"

redmind @angrybrow frownmouth "Hey. Could you cut that out? You're, like fifty feet away, and still walking. This isn't how you're supposed to have a conversation."

pause 2.0

redmind @thinking "...Ugh. Well, now there's three people. Old Man Oak, Sabrina, and myself."

redmind @sad "What a way to start my free day..."

call freeroam from _call_freeroam

call texting from _call_texting

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_27

show blank2 with dis
    
$ renpy.pause(2.5, hard=True)

jump day010412