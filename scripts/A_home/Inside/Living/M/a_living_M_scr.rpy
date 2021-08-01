screen a_living_M_scr:
    key "hide_windows" action NullAction()

    imagebutton:
        xpos 0
        ypos 157
        focus_mask True
        idle "/images/a_home/Inside/Living/M/B1.png"
        hover "/images/a_home/Inside/Living/M/B1_hover.png"
        if clickable == True:

            action [Hide("displayTextScreen"),Jump("a_kitchen_M1")]
        hovered Show("displayTextScreen", displayText = __("Kitchen"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 570
        ypos 143
        focus_mask True
        idle "/images/a_home/Inside/Living/M/B2.png"
        hover "/images/a_home/Inside/Living/M/B2_hover.png"
        if clickable == True:

            action [Hide("displayTextScreen"),Jump("a_bathroom_M1")]
        hovered Show("displayTextScreen", displayText = __("Bathroom"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 823
        ypos 31
        focus_mask True
        idle "/images/a_home/Inside/Living/M/B3.png"
        hover "/images/a_home/Inside/Living/M/B3_hover.png"
        if clickable == True:

            action [Hide("displayTextScreen"),Jump("a_bedroom_M1")]
        hovered Show("displayTextScreen", displayText = __("Stairs"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1184
        ypos 65
        focus_mask True
        idle "/images/a_home/Inside/Living/M/B4.png"
        hover "/images/a_home/Inside/Living/M/B4_hover.png"
        if clickable == True:

            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("a_office_M1")]
        hovered Show("displayTextScreen", displayText = __("Office"))
        unhovered Hide("displayTextScreen")

    if LiR1_MAS2 == True and Li_points == 1 and Y_points == 1:
        imagebutton:
            xpos 932
            ypos 278
            focus_mask True
            idle "/images/a_home/Inside/Living/M/scenes/LiR1_MAS2/Li_B1.png"
            hover "/images/a_home/Inside/Living/M/scenes/LiR1_MAS2/Li_B1_hover.png"
            if clickable == True:

                action [Hide("displayTextScreen"),Jump("Li_MAS2_label")]
            hovered Show("displayTextScreen", displayText = "Liza")
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("a_home_outside_M1")]

