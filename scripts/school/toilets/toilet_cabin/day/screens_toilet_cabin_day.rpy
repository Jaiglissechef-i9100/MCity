screen toilet_cabin_day:
    key "hide_windows" action NullAction()
    if Celia_points == 2:
        imagebutton:
            xpos 507
            ypos 515
            focus_mask True
            idle "images/CeR2/AS1/B1.png"
            hover "images/CeR2/AS1/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Gloryhole")
            if clickable == True:
                if CeR2_AS1 == 2:
                    action [Hide("displayTextScreen"),Jump("CeR2_AS1_lab")]
                if CeR2_AS2 == 2:
                    action [Hide("displayTextScreen"),Jump("CeR2_AS2_lab")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/toilet cabin.mp3"),Jump("toilets_day1")]
