label day010406:
call calendar(1) from _call_calendar_1

$ timeOfDay = "Morning"

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

redmind "Hm... looks like everyone is still asleep. Well, I wanted to get to class so I could talk to Old Man Oak before class started, so this is fine by me!"

pause 2.0

red uniform happy "I'm off, [pika_name]!"

pikachu happy_2 "Pi-ka Pika!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_15

show blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

show morning at vspaz

pause 3.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg at dissolvein behind blank2
show homeroom behind oakbg

hide blank2 with splitfade
hide dorm_A

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide morning

narrator "Unfortunately, despite your efforts to engage Professor Oak in conversation, he adamantly refuses to answer any questions, saying that he'll answer them later."
narrator "Having failed in your quest, you hope Ethan has more success, and settle in for your lesson."

oak "How's everyone doing this morning? I hope you all had a good night's sleep because we'll be covering a lot of material today.{w=0.5} This will be on the tests, so pay close attention!"

show leaf uniform:
    xpos 250 ypos 175 + 1080 alpha 0.0 zoom 1.35
    ease 0.5 alpha 1.0

leaf @talkingmouth "Professor, you haven't explained to us how testing works in this class yet."

show leaf:
    xpos 250 ypos 175 + 1080 alpha 1.0 zoom 1.35 alpha 1.0

oak "Oh, is that right?{w=0.5} Well, now's as good a time as any."

show leaf:
    xpos 250 ypos 175 + 1080 alpha 1.0 zoom 1.35
    ease 0.5 alpha 0.0

oak "As you all know, aside from raising Pokémon, you are responsible for {color=#0048ff}passing both the midterms and finals for your homeroom classes.{/color}"

hide leaf

oak "On top of those, here at homeroom you will also be given quizzes {color=#0048ff}every Monday and Thursday before the end of the day.{/color}"
oak "Not only will {color=#0048ff}some of the questions be present on future exams, but getting them right can help you outside of school.{/color}"
oak "Take my word for it. I would pay attention to these lectures if I were you.{w=0.5} You'll thank me sooner than you'd think."

redmind "When Old Man Oak says stuff like that, you know he's being serious about it."
redmind "I should probably follow his advice.{w=0.5} It hasn't let me down before."

oak "Right then, how about we take a practice quiz now? You'll be given a hypothetical battle scenario, and your goal is simply to win."

stop music

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Rattata", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Tail Whip")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Cherubi", DexMacros.Id), level=2, moves=[GetMove("Absorb")])])

call Battle([trainer1, trainer2], gainexp=False, uniforms=[True, False]) from _call_Battle
$ wonbattle = _return

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

oak "...Right, I think that's about enough time. Why don't you all pass your papers up?"

if (wonbattle):
    red uniform @happy "Hey, that was pretty easy. It was only a practice test, but I like succeeding at it, anyway."
else:
    red uniform @sad "...I don't think I'm going to do very well on that test. At least it was only a practice test, but... this doesn't bode well."

oak ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak "At a glance..."

pause 0.5


if (wonbattle):
    oak "It looks like everyone did quite well. I don't anticipate this class should have much trouble passing, if you keep that up! Though I do ask that you work on your handwriting."
else:
    oak "I recommend everyone try not to overcomplicate simple battles. Stat changes don't matter if you're already hitting for over half an opponent's health."
    oak "I want to be clear, that although this was a practice test, continued performance like this is not going to cut it. {w=0.5}Ahem! So let this be a wake-up call."

oak "You can expect harder questions than that last one starting from now on.{w=0.5} {color=#0048ff}Also, you'll have quizzes for each of your elective classes, though it's up to the individual instructors when they'll give you quizzes.{/color}"
oak "Now then, let's move on to archeology."
oak "The first Poké Balls didn't appear until the discovery of Apricorns in the Johto region over 500 years ago.{nw}"

show blank2 with dis:
    alpha 1.0

extend " In 1925 Professor Westwood V developed the modern mechanical Poké Ball..."

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_16

show blank2:
    alpha 1.0

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.pause(2.5, hard=True)

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Unfortunately, class finishes before you can talk to Professor Oak privately, and you need to leave for your elective class..."

stop music fadeout 1.5

hide oakbg
hide homeroom

jump PickElective