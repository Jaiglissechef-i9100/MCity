screen Ce_living_D_scr:
    imagebutton:
        xpos 847
        ypos 73
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Living/M/B1.png"
        hover "/images/Ce_ele/Ce_home/Living/M/B1_hover.png"
        if clickable == True:
            action Show("Ce_living_M_painting")

        hovered Show("displayTextScreen", displayText = __("Painting"))
        unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_corridor2_M1")]

screen Ce_living_M_painting:
    zorder 102
    modal True
    add "/images/Ce_ele/Ce_home/Living/M/2.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action Hide("Ce_living_M_painting")

