

screen nightclub_corridor_scr:
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            if CR4_Cindy_S1 == 1:
                action Jump("CR4_Cindy_S1_lab")
            else:
                action Jump("nightclub_N1")
    if CR4_guard < 4:
        imagebutton:
            xpos 1073
            ypos 197
            focus_mask True
            idle "images/Nightclub/Corridor/B1.png"
            hover "images/Nightclub/Corridor/B1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Security"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR4_sceurity_lab")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1176
        ypos 169
        focus_mask True
        idle "images/Nightclub/Corridor/B2.png"
        hover "images/Nightclub/Corridor/B2_hover.png"
        hovered Show("displayTextScreen", displayText = __("Boss Office"))
        if clickable == True and CR4_guard < 4:
            action [Hide("displayTextScreen"),Jump("CR4_sceurity_lab")]
        if NC_Boss > 0:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("CR4_Boss_necklace")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 382
        ypos 79
        focus_mask True
        idle "images/Nightclub/Corridor/B3.png"
        hover "images/Nightclub/Corridor/B3_hover.png"
        hovered Show("displayTextScreen", displayText = __("Sex Room"))
        if clickable == True and sexroom_key in inventory.items:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("nc_sexroom_N")]

        if clickable == True and sexroom_key not in inventory.items:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_locked.mp3"),Jump("sexroom_locked")]
        unhovered Hide("displayTextScreen")