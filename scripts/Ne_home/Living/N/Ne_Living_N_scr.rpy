screen Ne_Living_N_scr:
    add "images/Ne_1/Map/Living/N.jpg"

    imagebutton:
        xpos 514
        ypos 138
        focus_mask True
        idle "images/Ne_1/Map/Living/B1_N.png"
        hover "images/Ne_1/Map/Living/B1_N_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = "Corridor")
        unhovered Hide("displayTextScreen")