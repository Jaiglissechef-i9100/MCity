screen school_corridor3_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 472
        ypos 124
        focus_mask True
        idle "images/school/school_corridor3/morning/door1_morning_idle.png"
        hover "images/school/school_corridor3/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Therapist's Room"))
            action [Play ("sound", "sfx/door_open.mp3"),Jump("therapist_room_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 672
        ypos 0
        focus_mask True
        idle "images/school/school_corridor3/morning/door2_morning_idle.png"
        hover "images/school/school_corridor3/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("School Corridor"))
            clicked Jump("school_corridor1_morning1")
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1322
        ypos 122
        focus_mask True
        idle "images/school/school_corridor3/morning/door3_morning_idle.png"
        hover "images/school/school_corridor3/morning/door3_morning_hover.png"
        if clickable == True and headmaster_door_locked == True:
            action [Play ("sound", "sfx/door_locked.mp3")]

        if clickable == True and headmaster_door_locked == False:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("headmaster_room_morning1")]
        if clickable == True and headmaster_S2 == True and ml_points == 3:
            action [Hide("displayTextScreen"),Jump ("headmaster_S2")]
        if clickable == True and headmaster_S1 == True and headmaster_door_locked == False:
            action [Hide("displayTextScreen"),Jump ("headmaster_S1")]

        hovered Show("displayTextScreen", displayText = __("Headmaster's Room"))
        unhovered Hide("displayTextScreen")
