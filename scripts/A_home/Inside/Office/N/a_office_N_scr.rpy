screen a_office_N_scr:
    key "hide_windows" action NullAction()
    if not "img32_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1185
                ypos 416
                focus_mask True
                idle "images/secret_gallery/Bonus/B32c.png"
                hover "images/secret_gallery/Bonus/B32c_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img32_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1185
                ypos 416
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img32_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("a_living_M1")]
