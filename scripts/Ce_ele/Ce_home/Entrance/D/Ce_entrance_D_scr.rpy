screen Ce_entrance_D_scr:

    imagebutton:
        xpos 1397
        ypos 208
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Entrance/M/B1.png"
        hover "/images/Ce_ele/Ce_home/Entrance/M/B1_hover.png"

        if clickable == True:
            action Show("Ce_entrance_M_painting")

        hovered Show("displayTextScreen", displayText = __("Painting"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1097
        ypos 121
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Entrance/M/B2.png"
        hover "/images/Ce_ele/Ce_home/Entrance/M/B2_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"),Jump("Ce_corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Corridor"))
        unhovered Hide("displayTextScreen")

    if not "img58_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 682
                ypos 910
                focus_mask True
                idle "images/secret_gallery/Bonus/B58a.png"
                hover "images/secret_gallery/Bonus/B58a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img58_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 682
                ypos 910
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img58_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img59_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 136
                ypos 206
                focus_mask True
                idle "images/secret_gallery/Bonus/B59a.png"
                hover "images/secret_gallery/Bonus/B59a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img59_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 136
                ypos 206
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img59_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img60_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 780
                ypos 565
                focus_mask True
                idle "images/secret_gallery/Bonus/B60a.png"
                hover "images/secret_gallery/Bonus/B60a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img60_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 780
                ypos 565
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img60_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img61_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1890
                ypos 618
                focus_mask True
                idle "images/secret_gallery/Bonus/B61a.png"
                hover "images/secret_gallery/Bonus/B61a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img61_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1890
                ypos 618
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img61_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img62_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 618
                ypos 401
                focus_mask True
                idle "images/secret_gallery/Bonus/B62a.png"
                hover "images/secret_gallery/Bonus/B62a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img62_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 618
                ypos 401
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img62_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_ele_corridor_M1")]


screen Ce_entrance_M_painting:
    zorder 102
    modal True
    add "/images/Ce_ele/Ce_home/Entrance/M/2.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action Hide("Ce_entrance_M_painting")

