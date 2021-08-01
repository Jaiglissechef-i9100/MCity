screen toilets_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/toilets/morning/door1_morning_idle.png"
        hover "images/school/toilets/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Toilet's Cabin")
        action [Play ("sound", "sfx/toilet cabin.mp3"),Jump("toilet_cabin_morning1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_morning1")]