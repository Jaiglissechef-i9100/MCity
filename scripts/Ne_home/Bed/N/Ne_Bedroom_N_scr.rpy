
screen Ne_Bedroom_N_scr:
    add "images/Ne_1/Map/Bed/N.jpg"
    imagebutton:
        xpos 486
        ypos 182
        focus_mask True
        idle "images/Ne_1/NV/NV.png"
        hover "images/Ne_1/NV/NV_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("Ne_NV_lab")]

        hovered Show("displayTextScreen", displayText = "Sidra and Isla")
        unhovered Hide("displayTextScreen")
    if not "img69_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 424
            ypos 444
            focus_mask True
            idle "images/secret_gallery/Bonus/B69c.png"
            hover "images/secret_gallery/Bonus/B69c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img69_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img70_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1766
            ypos 383
            focus_mask True
            idle "images/secret_gallery/Bonus/B70c.png"
            hover "images/secret_gallery/Bonus/B70c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img70_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img71_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1889
            ypos 728
            focus_mask True
            idle "images/secret_gallery/Bonus/B71c.png"
            hover "images/secret_gallery/Bonus/B71c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img71_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("Ne_Corridor_N1")]