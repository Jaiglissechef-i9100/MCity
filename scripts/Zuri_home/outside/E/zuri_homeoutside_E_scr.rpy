screen zuri_homeoutside_E_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 871
        ypos 392
        focus_mask True
        idle "images/Zuri_home/outside/E/B1.png"
        hover "images/Zuri_home/outside/E/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Doors"))
            action [Hide("displayTextScreen"),Jump("Z_home_door_E_label")]
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

screen Z_home_door_E_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 550
            ypos 132
            focus_mask True
            idle "images/Zuri_home/outside/E/B2.png"
            hover "images/Zuri_home/outside/E/B2_hover.png"
            hovered Show("displayTextScreen", displayText = __("Enter Zuri's Home"))
            action [Hide("displayTextScreen"),Jump("Z_home_doorknock_E_label")]
            unhovered Hide("displayTextScreen")

    if can_Zv2_ES1 == True and Zv2_ES1 == True:
        imagebutton:
            xpos 550
            ypos 132
            focus_mask True
            idle "images/Zuri_home/outside/E/B2.png"
            hover "images/Zuri_home/outside/E/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Enter Zuri's Home"))
                action [Hide("displayTextScreen"),Jump("Z_ES1_label")]
                unhovered Hide("displayTextScreen")

    if Zv2_ES4 == True and Zv2_lie_counter > 1:
        imagebutton:
            xpos 550
            ypos 132
            focus_mask True
            idle "images/Zuri_home/outside/E/B2.png"
            hover "images/Zuri_home/outside/E/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Enter Zuri's Home"))
                action [Hide("displayTextScreen"),Jump("Zv2_ES4_lie_label")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("zuri_homeoutside_M1")]