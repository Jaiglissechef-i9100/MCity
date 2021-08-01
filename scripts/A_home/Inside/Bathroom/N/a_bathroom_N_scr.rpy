screen a_bathroom_N_scr:
    key "hide_windows" action NullAction()
    if not "img26_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1888
            ypos 930
            focus_mask True
            idle "images/secret_gallery/Bonus/B26b.png"
            hover "images/secret_gallery/Bonus/B26b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img26_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img27_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 441
            ypos 206
            focus_mask True
            idle "images/secret_gallery/Bonus/B27c.png"
            hover "images/secret_gallery/Bonus/B27c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img27_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("a_living_M1")]