image nc_we_map = "images/Weekend_Events/Caroline/R3/NC/1.jpg"
image nc_we_map1a = "images/Weekend_Events/Caroline/R3/NC/1a.jpg"
screen WE_map:
    add "images/game_gui/map/Map_Night.jpg"
    zorder 102

    imagebutton:
        xpos 377
        ypos 174
        focus_mask True
        idle "images/game_gui/map/Nightclub Normal.png"
        hover "images/game_gui/map/Nightclub Hover.png"
        if clickable == True:
            action Jump("night_club_we_label")

label night_club_we_label:
    if CR3_WE ==5:
        jump CR3_WE_label_con4
    hide screen displayTextScreen
    if CR3_WE <2:
        scene nc_we_map
    else:
        scene nc_we_map1a
    $ can_map = False
    $ can_hide_windows = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen nc_we_scr

screen nc_we_scr:
    if CR3_WE == 1:
        imagebutton:
            xpos 1548
            ypos 352
            focus_mask True
            idle "images/Weekend_Events/Caroline/R3/NC/C_WE_B1.png"
            hover "images/Weekend_Events/Caroline/R3/NC/C_WE_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_WE_label_con1")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if CR3_G1 !=3:
        imagebutton:
            xpos 426
            ypos 227
            focus_mask True
            idle "images/Weekend_Events/Caroline/R3/NC/G1_B2.png"
            hover "images/Weekend_Events/Caroline/R3/NC/G1_B2_hover.png"
            if clickable == True and CR3_G1 == True:
                action [Hide("displayTextScreen"),Jump("CR3_WE_G1_label")]
                hovered Show("displayTextScreen", displayText = "???")
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1515
        ypos 238
        focus_mask True
        idle "images/Weekend_Events/Caroline/R3/NC/G2_B3.png"
        hover "images/Weekend_Events/Caroline/R3/NC/G2_B3_hover.png"
        if clickable == True and CR3_G2 == True:
            action [Hide("displayTextScreen"),Jump("CR3_WE_G2_label")]
            hovered Show("displayTextScreen", displayText = "???")
            unhovered Hide("displayTextScreen")

    if CR3_Ex !=3:
        imagebutton:
            xpos 766
            ypos 280
            focus_mask True
            idle "images/Weekend_Events/Caroline/R3/NC/Ex_B4.png"
            hover "images/Weekend_Events/Caroline/R3/NC/Ex_B4_hover.png"
            if clickable == True and CR3_Ex == True:
                action [Hide("displayTextScreen"),Jump("CR3_WE_Ex_label")]
                hovered Show("displayTextScreen", displayText = "Charles")
                unhovered Hide("displayTextScreen")
