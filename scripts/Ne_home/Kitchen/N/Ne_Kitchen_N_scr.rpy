screen Ne_Kitchen_N_scr:
    add "images/Ne_1/Map/Kitchen/N.jpg"

    imagebutton:
        xpos 1133
        ypos 92
        focus_mask True
        idle "images/Ne_1/Map/Kitchen/B1_N.png"
        hover "images/Ne_1/Map/Kitchen/B1_N_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Corridor"))
        unhovered Hide("displayTextScreen")