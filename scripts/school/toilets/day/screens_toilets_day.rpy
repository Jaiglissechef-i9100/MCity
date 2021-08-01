screen toilets_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/toilets/morning/door1_morning_idle.png"
        hover "images/school/toilets/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Toilet's Cabin"))
        action [Play ("sound", "sfx/toilet cabin.mp3"),Jump("toilet_cabin_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]

    if unlock_celia_toilet_cabin_day_scene3_v1 == 1 and can_unlock_celia_toilet_cabin_day_scene3_v1 == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/toilets/morning/door1_morning_idle.png"
            hover "images/school/toilets/morning/door1_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Toilet's Cabin"))
            action [Hide("displayTextScreen"),Play ("sound", "sfx/toilet cabin.mp3"),Jump("celia_toilet_cabin_day_scene3_v1_label")]
            unhovered Hide("displayTextScreen")

    if can2_unlock_celia_toilet_cabin_day_scene4_v1 == 1 and unlock_celia_toilet_cabin_day_scene4_v1 == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/toilets/morning/door1_morning_idle.png"
            hover "images/school/toilets/morning/door1_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Toilet's Cabin"))
            action [Hide("displayTextScreen"),Play ("sound", "sfx/toilet cabin.mp3"),Jump("celia_toilet_cabin_day_scene4_v1_label")]
            unhovered Hide("displayTextScreen")

    if CeR2_AS3 == True and Celia_points == 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/toilets/morning/door1_morning_idle.png"
            hover "images/school/toilets/morning/door1_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Toilet's Cabin"))
            action [Hide("displayTextScreen"),Play ("sound", "sfx/toilet cabin.mp3"),Jump("CeR2_AS3_lab")]
            unhovered Hide("displayTextScreen")

