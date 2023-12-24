label homeroom1transition:

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_49

play sound "Audio/BellChime.ogg"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")
hide blank2
show blank2 with splitfade

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_50
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

jump PickElective