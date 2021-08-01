screen pool_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/pool/morning/door1_morning_idle.png"
        hover "images/school/pool/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("School Corridor"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
        unhovered Hide("displayTextScreen")

