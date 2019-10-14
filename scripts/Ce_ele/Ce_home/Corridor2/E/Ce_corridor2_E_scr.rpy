screen Ce_corridor2_E_scr:

    imagebutton:
        xpos 256
        ypos 80
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/E/B1.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/E/B1_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_gym_M1")]

        hovered Show("displayTextScreen", displayText = "Gym")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 875
        ypos 104
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/E/B2.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/E/B2_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_living_M1")]

        hovered Show("displayTextScreen", displayText = "Living Room")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1386
        ypos 65
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Corridor2/E/B3.png"
        hover "/images/Ce_ele/Ce_home/Corridor2/E/B3_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_bedroom_M1")]

        hovered Show("displayTextScreen", displayText = "Bedroom")
        unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Jump("Ce_corridor_M1")]