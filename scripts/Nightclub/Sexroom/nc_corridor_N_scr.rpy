screen nc_sexroom_N_scr:
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("nc_corridor_N")]

    if CR4_Cindy_S1 == 5:
        imagebutton:
            xpos 922
            ypos 214
            focus_mask True
            idle "images/Nightclub/S_room/Scenes/Cindy_S5/B1.png"
            hover "images/Nightclub/S_room/Scenes/Cindy_S5/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Cindy")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ci_S5_lab")]
                unhovered Hide("displayTextScreen")