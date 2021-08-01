image Ne_cmg_p1 = "images/Ne_1/ES1/C_mg/1.jpg"
image Ne_cmg_p2 = "images/Ne_1/ES1/C_mg/2.jpg"
image Ne_cmg_p3 = "images/Ne_1/ES1/C_mg/3.jpg"
image Ne_cmg_p4 = "images/Ne_1/ES1/C_mg/4.jpg"
image Ne_cmg_p5 = "images/Ne_1/ES1/C_mg/5.jpg"
image Ne_cmg_p6 = "images/Ne_1/ES1/C_mg/6.jpg"
image Ne_cmg_p7 = "images/Ne_1/ES1/C_mg/7.jpg"
image Ne_cmg_p8 = "images/Ne_1/ES1/C_mg/8.jpg"
image Ne_cmg_p9 = "images/Ne_1/ES1/C_mg/9.jpg"
image Ne_cmg_p10 = "images/Ne_1/ES1/C_mg/10.jpg"
image Ne_cmg_p11 = "images/Ne_1/ES1/C_mg/11.jpg"
image Ne_cmg_p12 = "images/Ne_1/ES1/C_mg/12.jpg"
image Ne_cmg_p13 = "images/Ne_1/ES1/C_mg/13.jpg"
image Ne_cmg_p14 = "images/Ne_1/ES1/C_mg/14.jpg"
image Ne_cmg_p15 = "images/Ne_1/ES1/C_mg/15.jpg"
image Ne_cmg_p16 = "images/Ne_1/ES1/C_mg/16.jpg"

image Ne_cmg_p1a = "images/Ne_1/ES1/C_mg/1a.jpg"
image Ne_cmg_p2a = "images/Ne_1/ES1/C_mg/2a.jpg"
image Ne_cmg_p3a = "images/Ne_1/ES1/C_mg/3a.jpg"
image Ne_cmg_p4a = "images/Ne_1/ES1/C_mg/4a.jpg"
image Ne_cmg_p5a = "images/Ne_1/ES1/C_mg/5a.jpg"
image Ne_cmg_p6a = "images/Ne_1/ES1/C_mg/6a.jpg"
image Ne_cmg_p7a = "images/Ne_1/ES1/C_mg/7a.jpg"
image Ne_cmg_p8a = "images/Ne_1/ES1/C_mg/8a.jpg"
image Ne_cmg_p9a = "images/Ne_1/ES1/C_mg/9a.jpg"
image Ne_cmg_p10a = "images/Ne_1/ES1/C_mg/10a.jpg"
image Ne_cmg_p11a = "images/Ne_1/ES1/C_mg/11a.jpg"
image Ne_cmg_p12a = "images/Ne_1/ES1/C_mg/12a.jpg"
image Ne_cmg_p13a = "images/Ne_1/ES1/C_mg/13a.jpg"
image Ne_cmg_p14a = "images/Ne_1/ES1/C_mg/14a.jpg"
image Ne_cmg_p15a = "images/Ne_1/ES1/C_mg/15a.jpg"
image Ne_cmg_p16a = "images/Ne_1/ES1/C_mg/16a.jpg"

default Ne_cmg = 1
label Ne_c_mg:
    if persistent.skip_mg == True:
        $ Ne_cmg = 5
    hide screen map_button
    $ renpy.block_rollback()
    $ w_bar = 527
    if Ne_cmg == 1:
        if day_time == 3:
            scene Ne_cmg_p1
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p2
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p3
            $ renpy.pause (1.5, hard = True)
        if day_time == 4:
            scene Ne_cmg_p1a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p2a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p3a
            $ renpy.pause (1.5, hard = True)
        call screen Ne_c_mg_scr

    if Ne_cmg == 2:
        if day_time == 3:
            scene Ne_cmg_p4
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p5
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p6
            $ renpy.pause (1.5, hard = True)
        if day_time == 4:
            scene Ne_cmg_p4a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p5a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p6a
            $ renpy.pause (1.5, hard = True)
        call screen Ne_c_mg_scr

    if Ne_cmg == 3:
        if day_time == 3:
            scene Ne_cmg_p7
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p8
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p9
            $ renpy.pause (1.5, hard = True)
        if day_time == 4:
            scene Ne_cmg_p7a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p8a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p9a
            $ renpy.pause (1.5, hard = True)
        call screen Ne_c_mg_scr

    if Ne_cmg == 4:
        if day_time == 3:
            scene Ne_cmg_p10
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p11
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p12
            $ renpy.pause (1.5, hard = True)
        if day_time == 4:
            scene Ne_cmg_p10a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p11a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p12a
            $ renpy.pause (1.5, hard = True)
        call screen Ne_c_mg_scr

    if Ne_cmg == 5:
        $ Ne_cmg = 1
        if day_time == 3:
            scene Ne_cmg_p13
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p14
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p15
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p16
            $ renpy.pause (1.5, hard = True)

            jump Ne_ES1_lab

        if day_time == 4:
            scene Ne_cmg_p13a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p14a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p15a
            $ renpy.pause (1.5, hard = True)
            scene Ne_cmg_p16a
            $ renpy.pause (1.5, hard = True)

            jump Ne_Bedroom_M1

screen Ne_c_mg_scr:
    add "images/Nightclub/Warehouse/Minigame/Bar.png" xpos 524 ypos 965
    add "images/Nightclub/Warehouse/Minigame/Bar_p.png" at w_bar_move(w_bar)
    if w_bar >= 802 and w_bar <=1089:
        timer 3 action [SetVariable("Ne_cmg", Ne_cmg +1),Jump("Ne_c_mg")]

    if w_bar >= 537:
        timer 0.15 action SetVariable("w_bar", w_bar - 10) repeat True
    imagebutton:

        xpos 904
        ypos 431
        focus_mask True
        idle "images/Ne_1/ES1/C_mg/climb.png"
        hover "images/Ne_1/ES1/C_mg/climb_hover.png"

        action [SetVariable("w_bar", w_bar + 30)]