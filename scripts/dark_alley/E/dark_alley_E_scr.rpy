screen dark_alley_E_scr:
    key "hide_windows" action NullAction()

    if not "img16_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1031
            ypos 216
            focus_mask True
            idle "images/secret_gallery/Bonus/B16a.png"
            hover "images/secret_gallery/Bonus/B16_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img16_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img17_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 733
            ypos 269
            focus_mask True
            idle "images/secret_gallery/Bonus/B17a.png"
            hover "images/secret_gallery/Bonus/B17_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img17_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Jump("map_label")]
