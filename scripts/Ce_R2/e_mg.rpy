default e_mg_button = True
default e_mg_arr_ypos = 0
default e_mg_bar = 0
default e_mg_timer = 0
default e_mg_bar_max = 0
default e_mg_bar_reset = 0
default e_mg = 1
label e_mg_start:
    $ renpy.block_rollback()
    $ e_mg_button = True
    if e_mg == 1:
        menu:
            "Play":
                $ e_mg_bar = 673
                $ e_mg_arr_ypos = 480
                $ e_mg_timer = 1.7
                $ e_mg_bar_max = 493
                $ e_mg_bar_reset = 673
            "{image=cheat_code}":
                $ e_mg_bar == e_mg_bar_max
                if e_mg_bar == e_mg_bar_max:
                    jump e_mg_scr_fuckminigame

    if e_mg == 2:
        menu:
            "Play":
                $ e_mg_bar = 493
                $ e_mg_arr_ypos = 330
                $ e_mg_timer = 1.3
                $ e_mg_bar_max = 349
                $ e_mg_bar_reset = 493
            "{image=cheat_code}":
                $ e_mg_bar == e_mg_bar_max
                if e_mg_bar == e_mg_bar_max:
                    jump e_mg_scr_fuckminigame

    if e_mg == 3:
        menu:
            "Play":
                $ e_mg_bar = 349
                $ e_mg_arr_ypos = 250
                $ e_mg_timer = 1
                $ e_mg_bar_max = 259
                $ e_mg_bar_reset = 349
            "{image=cheat_code}":
                $ e_mg_bar == e_mg_bar_max
                if e_mg_bar == e_mg_bar_max:
                    jump e_mg_scr_fuckminigame

    call screen e_mg_scr

label e_mg_scr_fuckminigame:
screen e_mg_scr:
    if e_mg == 1:
        add "images/CeR2/LS/68.jpg"
    if e_mg == 2:
        add "images/CeR2/LS/70.jpg"
    if e_mg == 3:
        add "images/CeR2/LS/70.jpg"
    add "images/e_mg/bar.png" xpos 1808 ypos 154
    add "images/e_mg/pointer.png" xpos 1815 ypos e_mg_bar
    add "images/e_mg/arrow.png" xpos 1708 ypos e_mg_arr_ypos

    if e_mg_button == True:
        add "images/e_mg/green.png" xpos 1808 ypos 154
        timer e_mg_timer action SetVariable("e_mg_button", False)

    if e_mg_button == False:
        add "images/e_mg/red.png" xpos 1808 ypos 154
        timer 1.2 action SetVariable("e_mg_button", True)
    if e_mg_bar > e_mg_bar_max:
        imagebutton:
            xpos 1720
            ypos 731
            focus_mask True
            idle "images/e_mg/B1aaa.png"
            hover "images/e_mg/B1bb.png"

            if e_mg_button == True:
                action [SetVariable("e_mg_bar", e_mg_bar - 18),]
            else:
                action [SetVariable("e_mg_bar", e_mg_bar_reset),]

    if e_mg_bar == e_mg_bar_max:
        imagebutton:
            xpos 566
            ypos 418
            focus_mask True
            idle "images/e_mg/B2.png"
            hover "images/e_mg/B2a.png"
            action Jump("e_mg_end")

label e_mg_end:
    $ renpy.block_rollback()
    if e_mg == 1:
        $ e_mg = 2
        jump after_e_mg1

    if e_mg == 2:
        $ e_mg = 3
        jump after_e_mg2

    if e_mg == 3:
        $ e_mg = 4
        jump after_e_mg3