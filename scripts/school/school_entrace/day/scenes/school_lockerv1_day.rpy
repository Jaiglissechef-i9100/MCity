label school_lockerv1_day_label:
    scene school_lockerv1_p1
    call screen school_lockerv1_day_screen1

label school_open_lockerv1_day_label:
    $ b_clickable = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    scene school_lockerv1_p2
    call screen school_open_lockerv1_day_screen

label empty_envelope_pen_day_usev1_label:
    $ b_clickable = False
    hide screen map_button
    show screen school_open_lockerv1_day_screen
    $ can_hide_windows = False
    if empty_envelope in inventory.items and not empty_envelope.selected:
        MC "I could use those pens to write that empty envelope."
        hide screen school_open_lockerv1_day_screen
        jump school_open_lockerv1_day_label
    if empty_envelope in inventory.items and empty_envelope.selected:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        scene school_lockerv1_p3
        hide screen school_open_lockerv1_day_screen
        MC "(Okay.. Let’s write it, just as we planned, Judy.)"
        scene black
        $ renpy.sound.play("sfx/writing.mp3")
        $ renpy.pause(3, hard=True)
        $ can_empty_envelope_school_lockerv1 = 3
        $ inventory.drop(empty_envelope)
        $ inventory.add(envelope)
        $ b_clickable = True
        jump school_entrance_day1
    else:
        MC "That's my pens."
        hide screen school_open_lockerv1_day_screen
        jump school_open_lockerv1_day_label

screen school_lockerv1_day_screen1:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_entrance/morning/locker/door_lockerv1.png"
        if b_clickable == True:
            hover "images/school/school_entrance/morning/locker/door_lockerv1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Open"))
            action [Hide("displayTextScreen"),Jump("school_open_lockerv1_day_label")]
            unhovered Hide("displayTextScreen")
    if b_clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("school_entrance_day1")]

screen school_open_lockerv1_day_screen:
    key "hide_windows" action NullAction()
    if can_empty_envelope_school_lockerv1 == 1 and empty_envelope.selected and empty_envelope in inventory.items:
        imagebutton:
            xpos 0
            ypos -1
            focus_mask True
            idle "images/school/school_entrance/morning/locker/penv1.png"
            if b_clickable == True:
                hover "images/school/school_entrance/morning/locker/penv1_hover.png"
                hovered Show("displayTextScreen", displayText = __("Pens"))
                action [Hide("displayTextScreen"),Jump("empty_envelope_pen_day_usev1_label")]
                unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            xpos 0
            ypos -1
            focus_mask True
            idle "images/school/school_entrance/morning/locker/penv1.png"
            if b_clickable == True:
                hover "images/school/school_entrance/morning/locker/penv1_hover.png"
                hovered Show("displayTextScreen", displayText = __("Pens"))
                action [Hide("displayTextScreen"),Jump("empty_envelope_pen_day_usev1_label")]
                unhovered Hide("displayTextScreen")
    if b_clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("school_entrance_day1")]

