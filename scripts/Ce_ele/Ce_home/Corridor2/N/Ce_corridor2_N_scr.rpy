screen Ce_corridor2_N_scr:

    imagebutton:
        xpos 256
        ypos 80
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/N/B1.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/N/B1_hover.png"

        if clickable == True:
            if CeR2_NS2 == 2:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"), Jump("CeR2_NS2_boxing_lab")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_gym_M1")]

        hovered Show("displayTextScreen", displayText = __("Gym"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 875
        ypos 104
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/N/B2.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/N/B2_hover.png"
        if clickable == True:
            if CeR2_NS2 == 3:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"), Jump("CeR2_NS2_wait_lab")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_living_M1")]

        hovered Show("displayTextScreen", displayText = __("Living Room"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1386
        ypos 65
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/N/B3.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/N/B3_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_bedroom_M1")]

        hovered Show("displayTextScreen", displayText = __("Bedroom"))
        unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Jump("Ce_corridor_M1")]