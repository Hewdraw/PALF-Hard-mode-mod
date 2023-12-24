label PickTable():

hide blank2
show blank2 with dis:
    alpha 0.8

call screen tables(_with_none=False) with dissolve
with dissolve
hide blank2 with dissolve
narrator "You chose the [_return]?"

$ tablecalled = _return

menu:
    ">Go to the [_return].":
        if (_return == "Angry Table"):
            call angrytable from _call_angrytable
        elif (_return == "Cheerful Table"):
            call cheerfultable from _call_cheerfultable
        elif (_return == "Busy Table"):
            call busytable from _call_busytable
        elif (_return == "Romantic Table"):
            call romantictable from _call_romantictable
        elif (_return == "Calm Table"):
            call calmtable from _call_calmtable
        elif (_return == "Quiet Table"):
            call quiettable from _call_quiettable
        elif (_return == "Sleeping Table"):
            call sleepingtable from _call_sleepingtable

        if (IsDate(14, 4, 2004) and tablecalled != "Cheerful Table"):
            scene cafe with Dissolve(2.0)

            show whitney uniform angry:
                xpos 0.66
            show tia uniform angry:
                xpos 0.33
            with dis

            narrator "You sense Tia and Whitney's glares boring into the back of your head as you prepare to leave the lunchroom."

            $ ValueChange("Tia", -3, 0.33, False)
            $ ValueChange("Whitney", -3, 0.66)

            redmind uniform @thinking "Sorry, ladies. Just don't have the spoons for this right now."

        jump PickElective

    ">Rethink your choice.":
        jump PickTable