



screen dark_alley_D_scr:
    key "hide_windows" action NullAction()
    if violetV2_scene == True:
        imagebutton:
            xpos 409
            ypos 419
            focus_mask True
            idle "/images/dark_alley/D/scenes/Vv2_AS1/B1.png"
            hover "/images/dark_alley/D/scenes/Vv2_AS1/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Violet")
                action [Hide("displayTextScreen"),Jump("Vv2_AS1_label")]
                unhovered Hide("displayTextScreen")
    if not "img16_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1031
            ypos 216
            focus_mask True
            idle "images/secret_gallery/Bonus/B16.png"
            hover "images/secret_gallery/Bonus/B16_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img16_sec_card"),SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img17_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 733
            ypos 269
            focus_mask True
            idle "images/secret_gallery/Bonus/B17.png"
            hover "images/secret_gallery/Bonus/B17_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img17_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if V_points == 2 and CR2_VS == True and Caroline_points <4 and can_violet_CR3 == True:
        imagebutton:
            xpos 1219
            ypos 416
            focus_mask True
            idle "/images/dark_alley/D/CR3_VS.png"
            hover "/images/dark_alley/D/CR3_VS_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Violet")
                action [Hide("displayTextScreen"),Jump("CR3_VS_label")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Jump("map_label")]