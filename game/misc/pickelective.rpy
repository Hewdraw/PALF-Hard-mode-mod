label PickElective():

show blank2 as blackground with dis

if (excusesecondelective):
    narrator "You take advantage of your Excused Absence to skip your elective."
    jump freeroam

show map with dis
hide blank2
show blank2 with dis:
    alpha 0.8

stop music fadeout 1.5
$ renpy.music.stop(channel="crowd", fadeout=1.5)
$ renpy.music.queue("Audio/Music/ViridianCity_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianCity_Loop.ogg", channel='music', loop=True, tight=None)

label AfterMusic:

if (timeOfDay == "Morning"):
    $ lastclass = ""

call screen electives(_with_none=False) with dissolve
with dissolve
hide blackground
hide screen classmates with dissolve
narrator "You chose [_return]?"

menu:
    ">Go to [_return] class.":
        python:
            classtype = _return
            jumpname = classtype.lower() + "elective"
            lastclass = classtype
            renpy.call(jumpname)

        $ renpy.music.set_volume(0.1, delay=1.0, channel="music")
        play sound "Audio/BellChime.ogg"

        $ renpy.pause(1.0, hard=True)
        $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

        narrator "Before you know it, class is over."
        python:
            numstudents = len(GetStudents(classtype)) + 1
            for i, student in enumerate(GetStudents(classtype) | {"Ethan"}):
                renpy.hide(student.lower())
                xbuffer = (i + 1) / (numstudents + 1)
                GetSmilePortrait(student.lower() + " uniform", [Transform(xpos=xbuffer), dissolvein])

            renpy.pause(1.0)

            for i, student in enumerate(GetStudents(classtype) | {"Ethan"}):
                xbuffer = (i + 1) / (numstudents + 1)
                valueamount = 1
                if (student in ["Jasmine", "Grusha"]):
                    valueamount = 2
                ValueChange(student, valueamount, xbuffer, False)
                if (classtype not in persondex[student]["ClassesKnown"]):
                    persondex[student]["ClassesKnown"].append(classtype)
            
            PlaySound("PointsUp.ogg")

        hide blank2

        narrator "Classmates' bonds increased!"
        $ IncreaseProficiency(classtype, 1)

        label aftertutoring:

        if (passedclass):
            $ ClearTest(classtype)

        $ taughtmove = None

        if (timeOfDay == "Morning"):
            $ timeOfDay = "Noon"
        elif (timeOfDay == "Afternoon"):
            $ timeOfDay = "Evening"

        hide blank2
        show blank2 with dis

        $ renpy.transition(dissolve)
        call clearscreens from _call_clearscreens_1

        window hide
        stop music fadeout 1.0
        $ renpy.pause(1.0, hard=True)

        if (timeOfDay == "Noon"):
            show noon at vspaz
        elif (timeOfDay == "Evening"):
            show evening at vspaz
            
        pause 3.5

        $ jumpto = "gym" if timeOfDay == "Noon" else "secondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)

    ">Rethink your choice.":
        jump AfterMusic

label endclass:#for skipping class if you elect for move tutoring instead
narrator "The class passes swiftly as you are tutored in a new move."

$ taughtmove = None

jump aftertutoring

label endclasscraft:# for skipping class if you elect for crafting instead
narrator "The class passes swiftly as you craft the item."

jump aftertutoring
