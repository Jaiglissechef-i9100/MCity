screen a_office_M_scr:
    key "hide_windows" action NullAction()

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("a_living_M1")]
    if LiR1_MAS3 == True and Li_points == 1:
        add "/images/a_home/Inside/Office/M/B3.png" xpos 1210 ypos 338
        imagebutton:
            xpos 969
            ypos 333
            focus_mask True
            idle "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/Y_B1.png"
            hover "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/Y_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Li_MAS3_label")]
            hovered Show("displayTextScreen", displayText = "Yazmin")
            unhovered Hide("displayTextScreen")
    if not "img32_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1185
            ypos 416
            focus_mask True
            idle "images/secret_gallery/Bonus/B32a.png"
            hover "images/secret_gallery/Bonus/B32a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img32_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not Li_key1 in inventory.items and LiR1_keyMAS7 == True:
        imagebutton:
            xpos 198
            ypos 711
            focus_mask True
            idle "/images/a_home/Inside/Office/M/Li_key_B2.png"
            hover "/images/a_home/Inside/Office/M/Li_key_B2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Li_key_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Auntie's Key")
            else:
                hovered Show("displayTextScreen", displayText = "Liza's Key")
            unhovered Hide("displayTextScreen")