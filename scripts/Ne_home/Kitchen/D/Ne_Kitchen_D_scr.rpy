screen Ne_Kitchen_D_scr:
    add "images/Ne_1/Map/Kitchen/M.jpg"

    imagebutton:
        xpos 1133
        ypos 92
        focus_mask True
        idle "images/Ne_1/Map/Kitchen/B1_M.png"
        hover "images/Ne_1/Map/Kitchen/B1_M_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Corridor"))
        unhovered Hide("displayTextScreen")