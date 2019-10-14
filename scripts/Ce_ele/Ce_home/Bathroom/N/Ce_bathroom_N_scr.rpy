screen Ce_bathroom_N_scr:

    if not "img49_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1507
            ypos 694
            focus_mask True
            idle "images/secret_gallery/Bonus/B49c.png"
            hover "images/secret_gallery/Bonus/B49c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img49_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img50_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1298
            ypos 92
            focus_mask True
            idle "images/secret_gallery/Bonus/B50c.png"
            hover "images/secret_gallery/Bonus/B50c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img50_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img51_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 28
            ypos 919
            focus_mask True
            idle "images/secret_gallery/Bonus/B51c.png"
            hover "images/secret_gallery/Bonus/B51c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img51_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_corridor_M1")]