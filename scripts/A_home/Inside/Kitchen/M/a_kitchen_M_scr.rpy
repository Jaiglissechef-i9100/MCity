
screen a_kitchen_M_scr:
    key "hide_windows" action NullAction()
    if not "img30_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 561
            ypos 884
            focus_mask True
            idle "images/secret_gallery/Bonus/B30a.png"
            hover "images/secret_gallery/Bonus/B30a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img30_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img31_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 807
            ypos 212
            focus_mask True
            idle "images/secret_gallery/Bonus/B31a.png"
            hover "images/secret_gallery/Bonus/B31a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img31_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if MAS7_fridge == True:
        imagebutton:
            xpos 402
            ypos 186
            focus_mask True
            idle "/images/a_home//Inside/Kitchen/M/B1.png"
            hover "/images/a_home//Inside/Kitchen/M/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Fridge")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("fridge_scene_label")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("a_living_M1")]