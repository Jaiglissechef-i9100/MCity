
image w_guard_p1a1 = "images/Nightclub/Warehouse/Minigame/1a1.jpg"
image w_guard_p1d = "images/Nightclub/Warehouse/Minigame/1d.jpg"
image w_guard_p1f = "images/Nightclub/Warehouse/Minigame/1f.jpg"
image w_guard_pfail = "images/Nightclub/Warehouse/Minigame/fail.jpg"
image w_guard_p2 = "images/Nightclub/Warehouse/Minigame/2.jpg"
image w_guard_p3 = "images/Nightclub/Warehouse/Minigame/3.jpg"
image w_guard_p4c = "images/Nightclub/Warehouse/Minigame/4c.jpg"
image w_guard_p4d = "images/Nightclub/Warehouse/Minigame/4d.jpg"
image w_guard_p4e = "images/Nightclub/Warehouse/Minigame/4e.jpg"
image w_guard_p4f = "images/Nightclub/Warehouse/Minigame/4f.jpg"
image w_guard_p5d = "images/Nightclub/Warehouse/Minigame/5d.jpg"
image w_guard_p6 = "images/Nightclub/Warehouse/Minigame/6.jpg"
image w_guard_p7 = "images/Nightclub/Warehouse/Minigame/7.jpg"
image w_guard_p9f = "images/Nightclub/Warehouse/Minigame/9f.jpg"
image w_guard_p9g = "images/Nightclub/Warehouse/Minigame/9g.jpg"
image w_guard_p9h = "images/Nightclub/Warehouse/Minigame/9h.jpg"
image w_guard_p10 = "images/Nightclub/Warehouse/Minigame/10.jpg"
image w_guard_p11 = "images/Nightclub/Warehouse/Minigame/11.jpg"
image w_guard_p12 = "images/Nightclub/Warehouse/Minigame/12.jpg"
define e = Character("Eileen")
init 15 python:
    w_bar = 527
    guard_pos = 1
    w_minigame_r = 1
init:
    transform w_bar_move(w_bar):

        xpos w_bar
        ypos 966


label start_w_minigame:
    $ guard_pos = 1
    $ renpy.block_rollback()
    scene black
    show screen w_timer_right
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    if w_minigame_r == 1:
        call screen w_minigame_scr1
    if w_minigame_r == 2:
        call screen w_minigame_scr2
    if w_minigame_r == 3:
        call screen w_minigame_scr3
    if w_minigame_r == 4:
        hide screen w_timer_right
        hide screen w_timer_left
        call screen w_minigame_scr4

label w_minigame_fail:
    $ renpy.block_rollback()
    hide screen w_timer_right
    hide screen w_timer_left
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    if w_minigame_r == 1:
        if guard_pos == 1:
            scene w_guard_p1d
            $ renpy.pause(2,hard = True)
            scene w_guard_p1f
            $ renpy.pause(2,hard = True)
        if guard_pos == 2:
            scene w_guard_p1a1
            $ renpy.pause(2,hard = True)
            scene w_guard_p1f
            $ renpy.pause(2,hard = True)
        if guard_pos == 3:
            scene w_guard_p1f
            $ renpy.pause(2,hard = True)
    if w_minigame_r == 2:
        scene w_guard_p5d
        $ renpy.pause(2,hard = True)
    scene black
    $ renpy.pause(2,hard = True)
    scene w_guard_pfail
    $ renpy.pause(2,hard = True)

    $ w_minigame_r = 1
    jump start_w_minigame

label w_minigame_r_next:
    $ renpy.block_rollback()
    hide screen w_timer_right
    hide screen w_timer_left
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    if w_minigame_r == 2:
        scene w_guard_p2
        $ renpy.pause(2,hard = True)
        scene w_guard_p3
        $ renpy.pause(2,hard = True)
        scene black
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        call screen CR4_warehouse_scr3

    if w_minigame_r == 3:
        scene w_guard_p6
        $ renpy.pause(2,hard = True)
        scene w_guard_p7
        $ renpy.pause(2,hard = True)
        scene black
        jump start_w_minigame
    if w_minigame_r == 4:
        scene w_guard_p10
        $ renpy.pause(2,hard = True)
        scene w_guard_p11
        $ renpy.pause(2,hard = True)
        scene w_guard_p12
        $ renpy.pause(2,hard = True)
        scene black
        jump start_w_minigame

label Boxes_w_minigame:
    $ renpy.block_rollback()
    hide screen w_timer_right
    hide screen w_timer_left
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    if w_minigame_r == 2:
        scene w_guard_p4c
        $ renpy.pause(2,hard = True)
        scene w_guard_p4d
        $ renpy.pause(2,hard = True)
        scene w_guard_p4e
        $ renpy.pause(2,hard = True)
        scene w_guard_p4f
        $ renpy.pause(2,hard = True)
        scene black

    if w_minigame_r == 3:
        scene w_guard_p9f
        $ renpy.pause(2,hard = True)
        scene w_guard_p9g
        $ renpy.pause(2,hard = True)
        scene w_guard_p9h
        $ renpy.pause(2,hard = True)

    $ renpy.pause(2,hard = True)
    scene w_guard_pfail
    $ renpy.pause(2,hard = True)
    $ w_minigame_r = 1
    jump start_w_minigame

screen w_minigame_scr1:
    if guard_pos == 1:
        add "images/Nightclub/Warehouse/Minigame/1.jpg"
    if guard_pos == 2:
        add "images/Nightclub/Warehouse/Minigame/1a.jpg"
    if guard_pos == 3:
        add "images/Nightclub/Warehouse/Minigame/1b.jpg"
    if guard_pos == 4:
        add "images/Nightclub/Warehouse/Minigame/1c.jpg"

    add "images/Nightclub/Warehouse/Minigame/Bar.png" xpos 524 ypos 965
    add "images/Nightclub/Warehouse/Minigame/Bar_p.png" at w_bar_move(w_bar)

    timer 3.0 action [If(guard_pos == 4,SetVariable("guard_pos", 1),SetVariable("guard_pos", guard_pos +1)) ] repeat True

    imagebutton:

        xpos 20
        ypos 550
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 40)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 40)
        if w_bar >= 802 and w_bar <=1089 and guard_pos == 2:
            action [SetVariable("w_minigame_r", w_minigame_r +1),Jump("w_minigame_r_next")]
        else:
            action [SetVariable("guard_pos", 5),Hide("w_minigame_scr1"),Jump("w_minigame_fail")]

    imagebutton:

        xpos 1720
        ypos 600
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 220)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 220)
        action [Hide("w_minigame_scr1"),Jump("w_minigame_fail"),]



screen w_timer_right:
    timer 0.025 repeat True action [If(w_bar >= 520, SetVariable("w_bar", w_bar +5)), If(w_bar >= 1363, Hide("w_timer_right")), If(w_bar >= 1363, Show("w_timer_left"),SetVariable("w_bar_rl", "l"))]
screen w_timer_left:

    timer 0.025 repeat True action [If(w_bar >= 527, SetVariable("w_bar", w_bar -5)), If(w_bar <= 527, Hide("w_timer_left")), If(w_bar <= 527, Show("w_timer_right")), SetVariable("w_bar_rl", "r"),]

screen CR4_warehouse_scr3:
    add "images/Nightclub/Warehouse/Minigame/4.jpg"
    imagebutton:
        xpos 255
        ypos 95
        focus_mask True
        idle "images/Nightclub/Warehouse/Minigame/4a.png"
        hover "images/Nightclub/Warehouse/Minigame/4a_hover.png"
        hovered Show("displayTextScreen", displayText = __("Boxes"))

        action [Hide("displayTextScreen"),Hide("CR4_warehouse_scr"),Jump("Boxes_w_minigame")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1344
        ypos 575
        focus_mask True
        idle "images/Nightclub/Warehouse/Minigame/4b.png"
        hover "images/Nightclub/Warehouse/Minigame/4b_hover.png"
        hovered Show("displayTextScreen", displayText = __("Barrels"))
        action [Hide("displayTextScreen"),Hide("CR4_warehouse_scr"),Jump("start_w_minigame")]
        unhovered Hide("displayTextScreen")

screen w_minigame_scr2:
    if guard_pos == 1:
        add "images/Nightclub/Warehouse/Minigame/5.jpg"
    if guard_pos == 2:
        add "images/Nightclub/Warehouse/Minigame/5a.jpg"
    if guard_pos == 3:
        add "images/Nightclub/Warehouse/Minigame/5b.jpg"
    if guard_pos == 4:
        add "images/Nightclub/Warehouse/Minigame/5c.jpg"

    add "images/Nightclub/Warehouse/Minigame/Bar.png" xpos 524 ypos 965
    add "images/Nightclub/Warehouse/Minigame/Bar_p.png" at w_bar_move(w_bar)

    timer 3.0 action [If(guard_pos == 4,SetVariable("guard_pos", 1),SetVariable("guard_pos", guard_pos +1)) ] repeat True

    imagebutton:

        xpos 20
        ypos 550
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 40)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 40)
        if w_bar >= 802 and w_bar <=1089 and guard_pos == 4:
            action [SetVariable("w_minigame_r", w_minigame_r +1),Jump("w_minigame_r_next")]
        else:
            action [SetVariable("guard_pos", 5),Hide("w_minigame_scr1"),Jump("w_minigame_fail")]

screen w_minigame_scr3:
    if guard_pos == 1:
        add "images/Nightclub/Warehouse/Minigame/9.jpg"
    if guard_pos == 2:
        add "images/Nightclub/Warehouse/Minigame/9b.jpg"
    if guard_pos == 3:
        add "images/Nightclub/Warehouse/Minigame/9c.jpg"
    if guard_pos == 4:
        add "images/Nightclub/Warehouse/Minigame/9d.jpg"
    if guard_pos == 5:
        add "images/Nightclub/Warehouse/Minigame/9e.jpg"

    add "images/Nightclub/Warehouse/Minigame/Bar.png" xpos 524 ypos 965
    add "images/Nightclub/Warehouse/Minigame/Bar_p.png" at w_bar_move(w_bar)

    timer 3.0 action [If(guard_pos == 5,SetVariable("guard_pos", 1),SetVariable("guard_pos", guard_pos +1)) ] repeat True

    imagebutton:
        xpos 710
        ypos 300
        focus_mask True
        idle "images/Nightclub/Warehouse/Minigame/9a.png"
        hover "images/Nightclub/Warehouse/Minigame/9a_hover.png"
        hovered Show("displayTextScreen", displayText = __("Barrels"))
        action [Hide("displayTextScreen"),Hide("CR4_warehouse_scr"),Jump("Boxes_w_minigame")]
        unhovered Hide("displayTextScreen")


    imagebutton:

        xpos 1037
        ypos 313
        focus_mask True
        idle "images/Nightclub/Warehouse/Minigame/9j.png"
        hover "images/Nightclub/Warehouse/Minigame/9j_hover.png"
        hovered Show("displayTextScreen", displayText = __("Boxes"))
        if w_bar >= 802 and w_bar <=1089 and guard_pos != 1,4,5:
            action [Hide("displayTextScreen"),SetVariable("w_minigame_r", w_minigame_r +1),Jump("w_minigame_r_next")]
        else:
            action [Hide("displayTextScreen"), SetVariable("guard_pos", 5), Hide("w_minigame_scr1"),Jump("w_minigame_fail")]
        unhovered Hide("displayTextScreen")

screen w_minigame_scr4:
    add "images/Nightclub/Warehouse/Minigame/13.jpg"
    imagebutton:
        xpos 869
        ypos 144
        focus_mask True
        idle "images/Nightclub/Warehouse/Minigame/13a.png"
        hover "images/Nightclub/Warehouse/Minigame/13a_hover.png"
        hovered Show("displayTextScreen", displayText = __("Doors"))

        action [Hide("displayTextScreen"),Hide("w_minigame_scr4"),Jump("CR4_warehouse_con")]
        unhovered Hide("displayTextScreen")