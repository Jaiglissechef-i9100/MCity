screen teacher_room1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/teacher_room1/morning/door1_morning_idle.png"
        hover "images/school/teacher_room1/morning/door1_morning_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor2_day1")]
            hovered Show("displayTextScreen", displayText = "Corridor")
            unhovered Hide("displayTextScreen")

    if can_celia_laptopv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room1/morning/celia_laptopv1/celia_laptopb1_v1.png"
            hover "images/school/teacher_room1/morning/celia_laptopv1/celia_laptopb1_v1_hover.png"
            if clickable == True:
                action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("celia_day_laptopv1_label")]
                hovered Show("displayTextScreen", displayText = "Celia's Laptop")
                unhovered Hide("displayTextScreen")