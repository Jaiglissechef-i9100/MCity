screen zuri_homeoutside_M_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 870
        ypos 391
        focus_mask True
        idle "images/Zuri_home/outside/M/B1.png"
        hover "images/Zuri_home/outside/M/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Doors"))
            action [Hide("displayTextScreen"),Jump("Z_home_door_M_label")]
            unhovered Hide("displayTextScreen")

    if not "img19_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1657
                ypos 779
                focus_mask True
                idle "images/secret_gallery/Bonus/B19.png"
                hover "images/secret_gallery/Bonus/B19_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img19_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1657
                ypos 779
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img19_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

screen Z_home_door_M_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 550
            ypos 132
            focus_mask True
            idle "images/Zuri_home/outside/M/B2.png"
            hover "images/Zuri_home/outside/M/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Enter Zuri's Home"))
                action [Hide("displayTextScreen"),Jump("Z_home_doorlocked_M_label")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("zuri_homeoutside_M1")]

