screen Ne_entrance_E_scr:
    add "images/Ne_1/Map/Entrance/E.jpg"

    imagebutton:
        xpos 753
        ypos 336
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B1_E.png"
        hover "images/Ne_1/Map/Entrance/B1_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"), Jump("Ne_Corridor_M1")]

        hovered Show("displayTextScreen", displayText = "Doors")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1301
        ypos 270
        focus_mask True
        idle "images/Ne_1/Map/Entrance/B2_E.png"
        hover "images/Ne_1/Map/Entrance/B2_E_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Jump("Ne_fence_lab")]

        hovered Show("displayTextScreen", displayText = "Fence")
        unhovered Hide("displayTextScreen")
    if not "img63_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 140
            ypos 905
            focus_mask True
            idle "images/secret_gallery/Bonus/B63b.png"
            hover "images/secret_gallery/Bonus/B63b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img63_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img64_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1129
            ypos 355
            focus_mask True
            idle "images/secret_gallery/Bonus/B64b.png"
            hover "images/secret_gallery/Bonus/B64b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img64_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img65_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1365
            ypos 247
            focus_mask True
            idle "images/secret_gallery/Bonus/B65b.png"
            hover "images/secret_gallery/Bonus/B65b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img65_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")