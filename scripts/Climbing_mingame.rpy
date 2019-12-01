
image Climbing1 = "images/ClimbingMinigame/1.jpg"
image Climbing2 = "images/ClimbingMinigame/2.jpg"
image Climbing3 = "images/ClimbingMinigame/3.jpg"
image Climbing4 = "images/ClimbingMinigame/4.jpg"
image Climbing5 = "images/ClimbingMinigame/5.jpg"
image Climbing6 = "images/ClimbingMinigame/6.jpg"
image Climbing7 = "images/ClimbingMinigame/7.jpg"

image ClimbingSuccess_p1 = "images/ClimbingMinigame/Success/1.jpg"
image ClimbingSuccess_p2 = "images/ClimbingMinigame/Success/2.jpg"
image ClimbingSuccess_p3 = "images/ClimbingMinigame/Success/3.jpg"
image ClimbingSuccess_p4 = "images/ClimbingMinigame/Success/4.jpg"
image ClimbingSuccess_p5 = "images/ClimbingMinigame/Success/5.jpg"
image ClimbingSuccess_p6 = "images/ClimbingMinigame/Success/6.jpg"
image ClimbingSuccess_p5:
    "images/ClimbingMinigame/Success/5.jpg"
    0.5
    "images/ClimbingMinigame/Success/6.jpg"

image ClimbingFall1 = "images/ClimbingMinigame/Fall1.jpg"
image ClimbingFall2 = "images/ClimbingMinigame/Fall2.jpg"
image ClimbingFall3 = "images/ClimbingMinigame/Fall3.jpg"

default last_hand = 0
default climb_lvl = 0
default climb_bar_max = 1
default climb_bar_value = 0
default climb_bar_minus = False
default climb_spot_yNormal = 0
default climb_spot_value = 0
default climb_spot_value2 = 0
default can_climb_bar_loop = True
default LastClimbHand = "N"
default can2_LiR1_NS = True
default climb_w = 0
default climb_l = 0
label Climbing_start0:
    if can2_LiR1_NS == False:

        $ clickable = False
        hide screen map_button
        show screen a_home_outside_N_scr
        MC "I've been in their bedroom today."
        $ clickable = True
        hide screen a_home_outside_N_scr
        jump a_home_outside_M1

    if can_LiR1_NS == False:
        $ clickable = False
        hide screen map_button
        show screen a_home_outside_N_scr
        MC "I've already been there today."
        $ clickable = True
        hide screen a_home_outside_N_scr
        jump a_home_outside_M1
    else:
        hide screen map_button
        $ can_map = False
        $ climb_lvl = 0
        $ LastClimbHand = "N"
        scene Climbing1 with dissolve

        call screen ClimbingMenu_scr



label Climbing_start:

    $ climb_lvl = 0
    $ LastClimbHand = "N"
    scene Climbing1
    call screen ClimbingStart_scr

label Climbing_loop:
    $ renpy.block_rollback()
    $ climb_spot_value = renpy.random.choice([0,0.1,0.2,0.3,0.4,0.5,0.6,])
    $ can_climb_bar_loop = True
    if climb_spot_value == 0:
        $ climb_spot_value2 = 0.4
        $ climb_spot_yNormal = 516

    if climb_spot_value == 0.1:
        $ climb_spot_value2 = 0.5
        $ climb_spot_yNormal = 493

    if climb_spot_value == 0.2:
        $ climb_spot_value2 = 0.6
        $ climb_spot_yNormal = 470

    if climb_spot_value == 0.3:
        $ climb_spot_value2 = 0.7
        $ climb_spot_yNormal = 447

    if climb_spot_value == 0.4:
        $ climb_spot_value2 = 0.8
        $ climb_spot_yNormal = 424

    if climb_spot_value == 0.5:
        $ climb_spot_value2 = 0.9
        $ climb_spot_yNormal = 401

    if climb_spot_value == 0.6:
        $ climb_spot_value2 = 1.0
        $ climb_spot_yNormal = 378


    if climb_lvl == 0:
        scene Climbing2
    if climb_lvl == 1:
        scene Climbing3
    if climb_lvl == 2:
        scene Climbing4
    if climb_lvl == 3:
        scene Climbing5
    if climb_lvl == 4:
        scene Climbing6
    if climb_lvl == 5:
        scene Climbing7
    if climb_lvl == 6:
        scene Climbing7
        call screen ClimbingSuccess_scr
    if climb_lvl == 7:
        scene ClimbingSuccess_p1
        $ renpy.pause()
        scene ClimbingSuccess_p2
        call screen ClimbingSuccess_scr
    if climb_lvl == 8:
        scene ClimbingSuccess_p3
        call screen ClimbingSuccess_scr
    if climb_lvl == 9:
        scene ClimbingSuccess_p4
        call screen ClimbingSuccess_scr
    if climb_lvl == 10:
        $ climb_w +=1

        $ renpy.pause(0.30, hard = True)
        scene black
        jump LiR1_NS1_label
    call screen ClimbingStart_scr

label climbing_fall:
    scene ClimbingFall1
    if climb_lvl == 0:
        $ renpy.pause (0.5, hard = True)
    $ renpy.pause (climb_lvl/2, hard = True)
    $ renpy.sound.play("sfx/body_fall.mp3")
    $ renpy.pause (0.2, hard = True)
    scene ClimbingFall1 with vpunch
    scene ClimbingFall2 with dissolve
    $ renpy.pause (2, hard = True)
    scene ClimbingFall3 with dissolve
    $ renpy.pause (2, hard = True)
    $ climb_l +=1
    jump Climbing_start0
screen ClimbingMenu_scr:
    vbox xalign 0.01 yalign 0.99:
        frame:
            style "frame_gui1"
            text "W:{color=#00ff00}[climb_w]{/color} L:{color=#f00}[climb_l]{/color}"
    add "images/ClimbingMinigame/Hands0.png" xpos 322 ypos 733

    imagebutton:
        xpos 785
        ypos 333
        focus_mask True
        idle "images/ClimbingMinigame/B_Start.png"
        hover "images/ClimbingMinigame/B_Start_H.png"
        action [Jump("Climbing_loop") ]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 785
        ypos 500
        focus_mask True
        idle "images/ClimbingMinigame/PlayExitNormal1.png"
        hover "images/ClimbingMinigame/PlayExitHover1.png"
        action [Hide("ClimbingMenu_scr"), Jump("a_home_outside_M1") ]
        unhovered Hide("displayTextScreen")


screen ClimbingStart_scr:
    modal True
    if LastClimbHand == "L":
        add "images/ClimbingMinigame/Hands4.png" xpos 322 ypos 733
        add "images/ClimbingMinigame/Hand_W.png" xpos 274 ypos 444
        add "images/ClimbingMinigame/Hand_G.png" xpos 1457 ypos 444
    if LastClimbHand == "R":
        add "images/ClimbingMinigame/Hands3.png" xpos 322 ypos 733
        add "images/ClimbingMinigame/Hand_G.png" xpos 274 ypos 444
        add "images/ClimbingMinigame/Hand_W.png" xpos 1457 ypos 444
    if LastClimbHand == "N":
        add "images/ClimbingMinigame/Hands2.png" xpos 322 ypos 733

    vbar top_bar Frame("images/ClimbingMinigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/ClimbingMinigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range climb_bar_max value climb_bar_value xsize 37 ysize 230 xpos 980 ypos 400
    add "images/ClimbingMinigame/Click_spot.png" xpos 922 ypos climb_spot_yNormal

    imagebutton:
        xpos 292
        ypos 463
        idle "images/ClimbingMinigame/Hand_L.png"
        hover "images/ClimbingMinigame/Hand_L_hover.png"
        if climb_bar_value > climb_spot_value and climb_bar_value <= climb_spot_value2 and LastClimbHand != "L":
            action [Play ("sound", "sfx/correct2.wav"), SetVariable("climb_lvl", climb_lvl + 1), SetVariable("LastClimbHand", "L"), SetVariable("can_climb_bar_loop", False),Jump("Climbing_loop") ]
        else:
            action [Play ("sound", "sfx/failure2.wav"), Jump("climbing_fall") ]

    imagebutton:
        xpos 1475
        ypos 463
        idle "images/ClimbingMinigame/Hand_R.png"
        hover "images/ClimbingMinigame/Hand_R_hover.png"
        if climb_bar_value > climb_spot_value and climb_bar_value <= climb_spot_value2 and LastClimbHand != "R":
            action [Play ("sound", "sfx/correct2.wav"), SetVariable("climb_lvl", climb_lvl + 1), SetVariable("LastClimbHand", "R"), SetVariable("can_climb_bar_loop", False), Jump("Climbing_loop") ]
        else:
            action [Play ("sound", "sfx/failure2.wav"), Jump("climbing_fall") ]

    if climb_bar_minus == True and can_climb_bar_loop == True:
        timer 0.03 action If (climb_bar_value > 0, SetVariable("climb_bar_value", climb_bar_value - 0.04), SetVariable("climb_bar_minus", False) ) repeat True

    if climb_bar_minus == False and can_climb_bar_loop == True:
        timer 0.03 action If (climb_bar_value < 1, SetVariable("climb_bar_value", climb_bar_value + 0.04), SetVariable("climb_bar_minus", True) ) repeat True

screen ClimbingSuccess_scr:
    modal True
    if climb_lvl == 6:
        add "images/ClimbingMinigame/Hands2.png" xpos 322 ypos 733
        imagebutton:
            xpos 920
            ypos 700
            focus_mask True
            idle "images/ClimbingMinigame/A_Up.png"
            hover "images/ClimbingMinigame/A_Up_hover.png"
            if climb_bar_value > climb_spot_value and climb_bar_value <= climb_spot_value2:
                action [Play ("sound", "sfx/correct2.wav"), SetVariable("climb_lvl", climb_lvl + 1),Jump("Climbing_loop")]
            else:
                action [Play ("sound", "sfx/failure2.wav"), Jump("climbing_fall") ]
            unhovered Hide("displayTextScreen")

    if climb_lvl == 7:

        imagebutton:
            xpos 292
            ypos 463
            focus_mask True
            idle "images/ClimbingMinigame/A_Left.png"
            hover "images/ClimbingMinigame/A_Left_hover.png"
            if climb_bar_value > climb_spot_value and climb_bar_value <= climb_spot_value2:
                action [Play ("sound", "sfx/correct2.wav"), SetVariable("climb_lvl", climb_lvl + 1),Jump("Climbing_loop")]
            else:
                action [Play ("sound", "sfx/failure2.wav"), Jump("climbing_fall") ]
            unhovered Hide("displayTextScreen")
    if climb_lvl < 8:
        vbar top_bar Frame("images/ClimbingMinigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/ClimbingMinigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range climb_bar_max value climb_bar_value xsize 37 ysize 230 xpos 980 ypos 400
        add "images/ClimbingMinigame/Click_spot.png" xpos 922 ypos climb_spot_yNormal
        if climb_bar_minus == True and can_climb_bar_loop == True:
            timer 0.03 action If (climb_bar_value > 0, SetVariable("climb_bar_value", climb_bar_value - 0.04), SetVariable("climb_bar_minus", False) ) repeat True

        if climb_bar_minus == False and can_climb_bar_loop == True:
            timer 0.03 action If (climb_bar_value < 1, SetVariable("climb_bar_value", climb_bar_value + 0.04), SetVariable("climb_bar_minus", True) ) repeat True



    if climb_lvl == 8:
        imagebutton:
            xpos 1120
            ypos 100
            focus_mask True
            idle Transform("images/ClimbingMinigame/Spy.png", zoom= 0.5)
            hover Transform("images/ClimbingMinigame/Spy_hover.png", zoom= 0.5)
            action [SetVariable("climb_lvl", 10), Jump("Climbing_loop")]

    if climb_lvl == 9:
        imagebutton:
            xpos 920
            ypos 700
            focus_mask True
            idle "images/ClimbingMinigame/A_Up.png"
            hover "images/ClimbingMinigame/A_Up_hover.png"
            action [SetVariable("climb_lvl", climb_lvl + 1), Jump("Climbing_loop")]