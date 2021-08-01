screen Ce_ele_corridor_D_scr:

    imagebutton:
        xpos 250
        ypos 192
        focus_mask True
        idle "/images/Ce_ele/Corridor/M/B1.png"
        hover "/images/Ce_ele/Corridor/M/B1_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_locked.mp3"), Jump("Ce_ele_corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Apartment 51"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 999
        ypos 281
        focus_mask True
        idle "/images/Ce_ele/Corridor/M/B2.png"
        hover "/images/Ce_ele/Corridor/M/B2_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_locked.mp3"), Jump("Ce_ele_corridor_M1")]

        hovered Show("displayTextScreen", displayText = __("Apartment 52"))
        unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 1299
        ypos 293
        focus_mask True
        idle "/images/Ce_ele/Corridor/M/B3.png"
        hover "/images/Ce_ele/Corridor/M/B3_hover.png"

        if clickable == True:
            if Ce_home_key in inventory.items:
                action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_entrance_M1")]
            else:
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("Ce_closed")]

        hovered Show("displayTextScreen", displayText = __("Apartment 53"))
        unhovered Hide("displayTextScreen")

    if not "img46_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1197
                ypos 37
                focus_mask True
                idle "images/secret_gallery/Bonus/B46a.png"
                hover "images/secret_gallery/Bonus/B46a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img46_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1197
                ypos 37
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img46_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img47_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1701
                ypos 325
                focus_mask True
                idle "images/secret_gallery/Bonus/B47a.png"
                hover "images/secret_gallery/Bonus/B47a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img47_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1701
                ypos 325
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img47_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img48_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 942
                ypos 259
                focus_mask True
                idle "images/secret_gallery/Bonus/B48a.png"
                hover "images/secret_gallery/Bonus/B48a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img48_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 942
                ypos 259
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
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

