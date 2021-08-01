screen Ne_corridor_E_scr:
    add "images/Ne_1/Map/Corridor/E.jpg"

    imagebutton:
        xpos 0
        ypos 14
        focus_mask True
        idle "images/Ne_1/Map/Corridor/B1_E.png"
        hover "images/Ne_1/Map/Corridor/B1_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Bath_M1")]

        hovered Show("displayTextScreen", displayText = __("Bath Room"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 572
        ypos 101
        focus_mask True
        idle "images/Ne_1/Map/Corridor/B2_E.png"
        hover "images/Ne_1/Map/Corridor/B2_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Kitchen_M1")]

        hovered Show("displayTextScreen", displayText = __("Kitchen"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1091
        ypos 161
        focus_mask True
        idle "images/Ne_1/Map/Corridor/B3_E.png"
        hover "images/Ne_1/Map/Corridor/B3_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Living_M1")]

        hovered Show("displayTextScreen", displayText = __("Living Room"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1729
        ypos 66
        focus_mask True
        idle "images/Ne_1/Map/Corridor/B4_E.png"
        hover "images/Ne_1/Map/Corridor/B4_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Bedroom_M1")]

        hovered Show("displayTextScreen", displayText = __("Bed Room"))
        unhovered Hide("displayTextScreen")
    if not "img66_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 484
                ypos 176
                focus_mask True
                idle "images/secret_gallery/Bonus/B66b.png"
                hover "images/secret_gallery/Bonus/B66b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img66_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 484
                ypos 176
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img66_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img67_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1766
                ypos 280
                focus_mask True
                idle "images/secret_gallery/Bonus/B67b.png"
                hover "images/secret_gallery/Bonus/B67b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img67_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1766
                ypos 280
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img67_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img68_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1867
                ypos 708
                focus_mask True
                idle "images/secret_gallery/Bonus/B68b.png"
                hover "images/secret_gallery/Bonus/B68b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img68_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1867
                ypos 708
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img68_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if clickable == True and Ne_ES2 < 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("Ne_entrance_M1")]

