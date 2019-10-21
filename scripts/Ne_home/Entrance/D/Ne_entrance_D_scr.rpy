screen Ne_entrance_D_scr:
    add "images/Ne_1/Map/Entrance/M.jpg"

    imagebutton:
        xpos 753
        ypos 336
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B1_M.png"
        hover "images/Ne_1/Map/Entrance/B1_M_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Doors"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1301
        ypos 270
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B2_M.png"
        hover "images/Ne_1/Map/Entrance/B2_M_hover.png"

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
                idle "images/secret_gallery/Bonus/B63a.png"
                hover "images/secret_gallery/Bonus/B63a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img63_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 140
                ypos 905
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
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
                idle "images/secret_gallery/Bonus/B64a.png"
                hover "images/secret_gallery/Bonus/B64a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img64_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1129
                ypos 355
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
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
                idle "images/secret_gallery/Bonus/B65a.png"
                hover "images/secret_gallery/Bonus/B65a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img65_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1365
                ypos 247
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img65_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")