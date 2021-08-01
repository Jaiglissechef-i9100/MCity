screen Ce_living_N_scr:
    if CeR2_NS2 >= 1:

        imagebutton:
            xpos 847
            ypos 73
            focus_mask True
            idle "/images/Ce_ele/Ce_home/Living/E/B1.png"
            hover "/images/Ce_ele/Ce_home/Living/E/B1_hover.png"
            if clickable == True:
                action [Show("Ce_living_E_painting")]

            hovered Show("displayTextScreen", displayText = "Painting")
            unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            xpos 847
            ypos 73
            focus_mask True
            idle "/images/Ce_ele/Ce_home/Living/N/B1.png"
            hover "/images/Ce_ele/Ce_home/Living/N/B1_hover.png"
            if clickable == True:
                action [Show("Ce_living_N_painting")]

            hovered Show("displayTextScreen", displayText = "Painting")
            unhovered Hide("displayTextScreen")


    if CeR2_NS2 == 5:
        imagebutton:
            xpos 653
            ypos 293
            focus_mask True
            idle "images/CeR2/NS2/Waiting/Sofa.png"
            hover "images/CeR2/NS2/Waiting/Sofa_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CeR2_NS2_talking_lab")]

            hovered Show("displayTextScreen", displayText = "Sofa")
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_corridor2_M1")]

screen Ce_living_N_painting:
    zorder 102
    modal True
    add "/images/Ce_ele/Ce_home/Living/N/2.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Hide("Ce_living_N_painting")]