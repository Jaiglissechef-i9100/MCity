screen Ce_ele_corridor_N_scr:


    imagebutton:
        xpos 250
        ypos 192
        focus_mask True
        idle "/images/Ce_ele/Corridor/N/B1.png"
        hover "/images/Ce_ele/Corridor/N/B1_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_locked.mp3"), Jump("Ce_ele_corridor_M1")]

        hovered Show("displayTextScreen", displayText = "Apartment 51")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 999
        ypos 281
        focus_mask True
        idle "/images/Ce_ele/Corridor/N/B2.png"
        hover "/images/Ce_ele/Corridor/N/B2_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_locked.mp3"), Jump("Ce_ele_corridor_M1")]

        hovered Show("displayTextScreen", displayText = "Apartment 52")
        unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 1299
        ypos 293
        focus_mask True
        idle "/images/Ce_ele/Corridor/N/B3.png"
        hover "/images/Ce_ele/Corridor/N/B3_hover.png"

        if clickable == True:

            if Ce_home_key in inventory.items:
                action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_entrance_M1")]
            if not Ce_home_key in inventory.items:
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("Ce_closed")]
            if CeR2_NS1 == 3 and Celia_points == 2:
                action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("CeR2_NS1_lab")]
            if CeR2_NS3 == True  and Celia_points == 2:
                action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("CeR2_NS3_lab")]

        hovered Show("displayTextScreen", displayText = "Apartment 53")
        unhovered Hide("displayTextScreen")

    if not "img46_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1197
            ypos 37
            focus_mask True
            idle "images/secret_gallery/Bonus/B46c.png"
            hover "images/secret_gallery/Bonus/B46c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img46_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img47_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1701
            ypos 325
            focus_mask True
            idle "images/secret_gallery/Bonus/B47c.png"
            hover "images/secret_gallery/Bonus/B47c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img47_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img48_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 942
            ypos 259
            focus_mask True
            idle "images/secret_gallery/Bonus/B48c.png"
            hover "images/secret_gallery/Bonus/B48c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img48_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("map_label")]