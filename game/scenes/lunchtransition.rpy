label lunchtransition:

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
play sound "Audio/BellChime.ogg"

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show bruno think with dis
alder happy2 "That'll be all for today.{w=0.5} Enjoy the rest of your day!"
show alder norm with dis

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_51

$ renpy.pause(2.0, hard=True)

$ HealParty()

scene blank2
    
show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

show cafe behind blank2
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

$ jumpto = "lunch"
$ jumptoyear = "01"
$ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
$ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
$ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)