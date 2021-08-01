screen Ne_Living_E_scr:
    add "images/Ne_1/Map/Living/E.jpg"

    imagebutton:
        xpos 514
        ypos 138
        focus_mask True
        idle "images/Ne_1/Map/Living/B1_E.png"
        hover "images/Ne_1/Map/Living/B1_E_hover.png"

        if clickable == True and Ne_ES2 < 3:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]
        if clickable == True and Ne_ES2 == 3:
            action [Hide("displayTextScreen"),Jump("NE_ES2_lab4")]
        hovered Show("displayTextScreen", displayText = "Corridor")
        unhovered Hide("displayTextScreen")

    if Ne_ES2 == 2:
        imagebutton:
            xpos 964
            ypos 326
            focus_mask True
            idle "images/Ne_1/ES2/Isla.png"
            hover "images/Ne_1/ES2/Isla_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"),Jump("NE_ES2_lab2")]

            hovered Show("displayTextScreen", displayText = "Isla")
            unhovered Hide("displayTextScreen")

    if Ne_ES2 == 3:
        imagebutton:
            xpos 17
            ypos 141
            focus_mask True
            idle "images/Ne_1/ES2/Closet.png"
            hover "images/Ne_1/ES2/Closet_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"),Jump("NE_ES2_lab3")]

            hovered Show("displayTextScreen", displayText = "Closet")
            unhovered Hide("displayTextScreen")