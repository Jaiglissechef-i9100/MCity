screen Ne_entrance_N_scr:
    add "images/Ne_1/Map/Entrance/N.jpg"

    imagebutton:
        xpos 753
        ypos 336
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B1_N.png"
        hover "images/Ne_1/Map/Entrance/B1_N_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Doors"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1301
        ypos 270
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B2_N.png"
        hover "images/Ne_1/Map/Entrance/B2_N_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Jump("Ne_fence_lab")]

        hovered Show("displayTextScreen", displayText = __("Fence"))
        unhovered Hide("displayTextScreen")

    if not "img63_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 140
                ypos 905
                focus_mask True
                idle "images/secret_gallery/Bonus/B63c.png"
                hover "images/secret_gallery/Bonus/B63c_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img63_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 140
                ypos 905
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img63_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img64_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1129
                ypos 355
                focus_mask True
                idle "images/secret_gallery/Bonus/B64c.png"
                hover "images/secret_gallery/Bonus/B64c_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img64_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1129
                ypos 355
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img64_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img65_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1365
                ypos 247
                focus_mask True
                idle "images/secret_gallery/Bonus/B65c.png"
                hover "images/secret_gallery/Bonus/B65c_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img65_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1365
                ypos 247
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img65_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")