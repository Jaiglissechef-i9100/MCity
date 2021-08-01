screen a_living_N_scr:
    key "hide_windows" action NullAction()

    imagebutton:
        xpos 0
        ypos 157
        focus_mask True
        idle "/images/a_home/Inside/Living/N/B1.png"
        hover "/images/a_home/Inside/Living/N/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Kitchen"))
            action [Jump("a_kitchen_M1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 570
        ypos 143
        focus_mask True
        idle "/images/a_home/Inside/Living/N/B2.png"
        hover "/images/a_home/Inside/Living/N/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Bathroom"))
            action [Jump("a_bathroom_M1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 823
        ypos 31
        focus_mask True
        idle "/images/a_home/Inside/Living/N/B3.png"
        hover "/images/a_home/Inside/Living/N/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Stairs"))
            action [Jump("a_bedroom_M1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1184
        ypos 65
        focus_mask True
        idle "/images/a_home/Inside/Living/N/B4.png"
        hover "/images/a_home/Inside/Living/N/B4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Office"))
            action [Play ("sound", "sfx/door_open.mp3"),Jump("a_office_M1")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("a_home_outside_M1")]

