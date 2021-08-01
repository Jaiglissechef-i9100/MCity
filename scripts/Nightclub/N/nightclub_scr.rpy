
screen nightclub_scr:
    if clickable == True:
        imagebutton:
            at map_arrow_anim
            xpos 70
            ypos 270
            focus_mask True
            idle Transform("images/game_gui/map_arrow.png", zoom = 0.75)
            hover Transform("images/game_gui/map_arrow_hover.png", zoom = 0.75)

            action Jump("nc_corridor_N")
            unhovered Hide("displayTextScreen")
    if CR4_Cindy_S1 == 3:
        imagebutton:
            xpos 1070
            ypos 413
            focus_mask True
            idle "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/B1.png"
            hover "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Cindy")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR4_Cindy_S2_lab")]
                unhovered Hide("displayTextScreen")

