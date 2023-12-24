define dip_white = Fade(1.0, 1.0, 0.5, color="#ffffff")

transform farleftside:
    xcenter 0.12

transform leftside:
    xcenter 0.25

transform midleftside:
    xcenter 0.37

transform centerside:
    xcenter 0.5

transform midrightside:
    xcenter 0.63

transform rightside:
    xcenter 0.75

transform farrightside:
    xcenter 0.88

transform dissolvein:
    alpha 0.0
    ease 1.0 alpha 1.0

transform dissolveaway:
    alpha 1.0
    ease 1.0 alpha 0.0

transform moveinleft:
    xcenter 1.5
    ease 1.0 xcenter 0.5

transform hovering:
    animation
    0.2
    yoffset 10
    0.2
    yoffset -10
    repeat

transform itemhover:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 0.5 zoom 0.0 rotate 10
    block:
        parallel:
            ease 0.25 alpha 1.0 zoom 1.0 yalign 0.3
        parallel:
            ease 0.25 rotate -10
            ease 0.25 rotate 10
            repeat 4
    ease 0.25 rotate 0 zoom 0.75

transform itemhide:
    subpixel True
    rotate 0 zoom 0.75 yalign 0.3
    ease 0.25 zoom 0.4 xalign 0.98 yalign 0.97
    pause 0.75
    ease 0.25 zoom 0.0

transform itemgive:
    alpha 1.0 yalign 0.97 xalign 0.98 zoom 0.0
    pause 0.25
    ease 0.5 zoom 0.5 xalign 0.5 yalign 0.5

transform getcloser:
    ypos 1.0 zoom 1.0
    ease 0.9 zoom 1.2 ypos 1.1

transform getfurther:
    ypos 1.1 zoom 1.2
    ease 0.9 zoom 1.0 ypos 1.0

transform sepia:
    matrixcolor SepiaMatrix()

transform monochrome:
    matrixcolor SaturationMatrix(0.0) * ContrastMatrix(2.0)

transform night:
    matrixcolor BrightnessMatrix(-0.2) * ContrastMatrix(1.3)

transform morning:
    matrixcolor TintMatrix(Color(rgb=(.95,.80,.75))) * BrightnessMatrix(-0.10) * ContrastMatrix(1.2)

transform pointsup(oldpos):
    subpixel True
    xpos oldpos ypos 0.33 zoom 0.0
    parallel:
        ease 0.25 zoom 1.0
        pause 0.25
        ease 1.0 alpha 0.0
    parallel:
        ease 1.0 xpos (oldpos + 0.04) ypos 0.22

transform hall_move1:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 960 yalign 1.0 rotate 0
    linear 0.1 xpos 1160 yalign 0.85 zoom 1.1 rotate -3

transform hall_move2:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    linear 0.1 xpos 960 yalign 1.0 zoom 1.0 rotate 0

transform vspaz:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 0.0
    ease 0.1 alpha 1.0 yalign 0.65
    ease 0.02 yalign 0.35
    ease 0.01 yalign 0.6
    ease 0.01 yalign 0.4
    ease 0.02 yalign 0.55
    ease 0.01 yalign 0.45
    ease 0.01 yalign 0.53
    ease 0.01 yalign 0.48
    ease 0.02 yalign 0.5
    pause 2.0
    ease 0.5 alpha 0.0

transform dormdesk:
    xpos 0.5 ypos 0.78

transform pokeball:
    animation
    matrixcolor BrightnessMatrix(1.0) * ContrastMatrix(0.0) zoom 0.0 xanchor 0.5 yanchor 0.95
    parallel:
        ease 0.2 zoom 1.0
    parallel:
        ease 2.0 matrixcolor BrightnessMatrix(0.0) * ContrastMatrix(1.0)

transform backinpokeball:
    matrixcolor BrightnessMatrix(0.0) * ContrastMatrix(1.0) zoom 1.0 xanchor 0.5 yanchor 0.95
    parallel:
        pause 1.8
        ease 0.2 zoom 0.0 
    parallel:
        ease 2.0 matrixcolor BrightnessMatrix(1.0) * ContrastMatrix(0.0)

transform choicefade:
    subpixel True
    alpha 0.0
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform fadeinleft(finalpos):
    alpha 0.0 xpos 0.0
    ease 0.7 xpos finalpos alpha 1.0

transform fadeinright(finalpos):
    alpha 0.0 xpos 1.0
    ease 0.7 xpos finalpos alpha 1.0

transform swipeinleft:
    alpha 0.0 ypos 0.2 xpos -500
    ease 0.4 ypos 0.35 alpha 1.0 xpos 50
    linear 1.2 ypos 0.45 xpos 100
    ease 0.6 ypos 1.0 xpos -2000

transform swipeinleftslow:
    alpha 0.0 ypos 0.1 xpos -500
    ease 1.0 ypos 0.17 alpha 1.0 xpos 50
    linear 3.0 ypos 0.23 xpos 100
    ease 1.5 ypos 1.0 xpos -2000

transform swipeinright:
    alpha 0.0 ypos 0.2 xpos 1920 + 500
    ease 0.4 ypos 0.35 alpha 1.0 xpos 1920 - 50
    linear 1.2 ypos 0.45 xpos 1920 - 100
    ease 0.6 ypos 1.0 xpos 1920 + 2000

transform garden_move1:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 960 rotate 0
    linear 0.1 xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    
transform garden_move2:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    linear 0.1 xpos 960 zoom 0.84781 rotate 0

transform evolveaway:
    align (0.5, 0.5) alpha 0.0 zoom 0.0 matrixcolor BrightnessMatrix(0)
    ease 1.0 zoom 1.0 alpha 1.0 
    pause 2.0
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.1)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(0.2)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.3)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(0.4)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.5)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(0.6)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.7)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(0.8)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.9)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)

transform evolvein:
    align (0.5, 0.5) zoom 0.0 matrixcolor BrightnessMatrix(0)
    pause 2.4
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.4 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 1.0 matrixcolor BrightnessMatrix(1.0)
    ease 5.0 zoom 1.2 matrixcolor BrightnessMatrix(0)

transform speedlines:
    yalign 0.5 xalign 0.5 alpha 0.0 zoom 3.25 rotate 0
    parallel:
        pause 1.0
        ease 3.0 alpha 1.0
        pause 17.5
        easeout_circ 0.5 alpha 0.0
    parallel:
        ease 5.5 zoom 1.5
        pause 15
        easeout_circ 0.5 zoom 5.0
    parallel:
        easeout_circ 22 rotate 3600

transform liberizemovein: 
    xpos 2.0 ypos 2.0
    ease 0.5 xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0

transform liberizefadein:
    xpos 2.0 ypos 2.0 alpha 0.0
    ease 0.5 xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0 alpha 1.0

transform liberizeactivefadein:
    alpha 0.0
    ease 0.5 alpha 1.0

transform tintstrobe:
    animation
    block:
        ease 2.0 matrixcolor TintMatrix("#fc8c8c")
        ease 2.0 matrixcolor TintMatrix("#8cfc8c")
        ease 2.0 matrixcolor TintMatrix("#8c8cfc")
        repeat

transform hoverfloat:
    yanchor 1.0 xanchor 0.0 blur 3.0
    parallel:
            ease 2.0 yanchor 0.98
            ease 2.0 yanchor 1.0
            repeat
    parallel:
        ease 2.0 xanchor 0.02
        ease 2.0 xanchor 0.0
        ease 2.0 xanchor -0.02
        ease 2.0 xanchor 0.0
        repeat

define fadeinbottom = ComposeTransition(Dissolve(0.5), after=easeinbottom)
define fadeoutbottom = ComposeTransition(Dissolve(0.5), after=easeoutbottom)

define dis = { "master" : Dissolve(0.25) }

init python:
    splitfadeslow = ImageDissolve(im.Tile("GFX/TransMask.jpg"), 2.5, 64)
    splitfade = ImageDissolve(im.Tile("GFX/TransMask.jpg"), 1.5, 64)
    splitfadefast = ImageDissolve(im.Tile("GFX/TransMask.jpg"), 0.8, 64)
    splitfadefaster = ImageDissolve(im.Tile("GFX/TransMask.jpg"), 0.4, 64)
    spinfade = ImageDissolve(im.Tile("GFX/TransTwirl.jpg"), 1.5, 64)
    spinfaderapid = ImageDissolve(im.Tile("GFX/TransTwirl.jpg"), 0.3, 64)
    transball = ImageDissolve(im.Tile("GFX/TransBall.jpg"), 2.0, 90)
    transeye = ImageDissolve(im.Tile("GFX/TransEye.jpg"), 1.0, 90)
    transeye2 = ImageDissolve(im.Tile("GFX/TransEye2.jpg"), 1.0, 90)
    gaussdissolve = ImageDissolve(im.Tile("GFX/gauss.webp"), 3.0, 90)

    transeye2nopause = { "master" : ImageDissolve(im.Tile("GFX/TransEye2.jpg"), 1.0, 90) }