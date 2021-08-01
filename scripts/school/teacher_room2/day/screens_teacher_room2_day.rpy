screen teacher_room2_day:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 604
        focus_mask True
        idle "images/school/teacher_room2/day/locker/locker_b1v1.png"
        hover "images/school/teacher_room2/day/locker/locker_b1v1_hover.png"
        if clickable == True:
            action [Jump("locker_v1_morning_label")]
            hovered Show("displayTextScreen", displayText = __("Locker"))
            unhovered Hide("displayTextScreen")

