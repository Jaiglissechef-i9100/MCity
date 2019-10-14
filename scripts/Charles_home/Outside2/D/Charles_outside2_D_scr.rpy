screen Charles_outside2_D_scr:
    if not "img80_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 125
            ypos 420
            focus_mask True
            idle "images/secret_gallery/Bonus/B80a.png"
            hover "images/secret_gallery/Bonus/B80a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img80_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img81_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1771
            ypos 349
            focus_mask True
            idle "images/secret_gallery/Bonus/B81a.png"
            hover "images/secret_gallery/Bonus/B81a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img81_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            at map_arrow_anim
            xpos 1160
            ypos 350
            focus_mask True
            idle Transform("images/game_gui/map_arrow.png", rotate = 60)
            hover Transform("images/game_gui/map_arrow_hover.png", rotate = 60)
            if Ch_last_scene == True:
                action Jump("Ch_last_scene")
            else:
                action Jump("charles_outside_M1")

            unhovered Hide("displayTextScreen")