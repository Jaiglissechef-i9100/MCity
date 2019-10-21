screen Ne_Bath_D_scr:
    add "images/Ne_1/Map/Bath/M.jpg"
    if not "img72_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 452
                ypos 177
                focus_mask True
                idle "images/secret_gallery/Bonus/B72a.png"
                hover "images/secret_gallery/Bonus/B72a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img72_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 452
                ypos 177
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img72_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img73_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 801
                ypos 254
                focus_mask True
                idle "images/secret_gallery/Bonus/B73a.png"
                hover "images/secret_gallery/Bonus/B73a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img73_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 801
                ypos 254
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img73_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img74_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 641
                ypos 455
                focus_mask True
                idle "images/secret_gallery/Bonus/B74a.png"
                hover "images/secret_gallery/Bonus/B74a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img74_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 641
                ypos 455
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img74_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img75_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 580
                ypos 850
                focus_mask True
                idle "images/secret_gallery/Bonus/B75a.png"
                hover "images/secret_gallery/Bonus/B75a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img75_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 580
                ypos 850
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img75_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1527
        ypos 0
        focus_mask True
        idle "images/Ne_1/Map/Bath/B1_M.png"
        hover "images/Ne_1/Map/Bath/B1_M_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Corridor"))
        unhovered Hide("displayTextScreen")