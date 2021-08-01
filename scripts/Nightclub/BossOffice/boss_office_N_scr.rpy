
screen boss_office_N_scr:
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("nc_corridor_N")]

    if NC_Boss == 1:
        imagebutton:
            xpos 927
            ypos 283
            focus_mask True
            idle "images/Nightclub/BossOffice/B1.png"
            hover "images/Nightclub/BossOffice/B1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Headmaster"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR4_Boss_next_day")]
            unhovered Hide("displayTextScreen")

