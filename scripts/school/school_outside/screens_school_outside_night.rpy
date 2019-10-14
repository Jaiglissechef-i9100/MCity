screen school_outside_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 561
        ypos 437
        focus_mask True
        idle "images/school/school_outside/night/door1_night_idle.png"
        hover "images/school/school_outside/night/door1_night_hover.png"
        hovered Show("displayTextScreen", displayText = "School(Closed)")
        action [Play ("sound", "sfx/door_locked.mp3"),Jump("school_outside_morning1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_outside/night/door2_night_idle.png"
        hover "images/school/school_outside/night/door2_night_hover.png"
        hovered Show("displayTextScreen", displayText = "To GYM(Closed)")
        action [Jump("school_outside_morning1")]
        unhovered Hide("displayTextScreen")