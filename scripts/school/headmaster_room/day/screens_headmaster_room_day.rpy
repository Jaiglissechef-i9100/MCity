screen headmaster_room_day:
    key "hide_windows" action NullAction()

    if not "img20_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1905
            ypos 510
            focus_mask True
            idle "images/secret_gallery/Bonus/B20.png"
            hover "images/secret_gallery/Bonus/B20_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img20_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img40_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 860
            ypos 462
            focus_mask True
            idle "images/secret_gallery/Bonus/B40a.png"
            hover "images/secret_gallery/Bonus/B40a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img40_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
            unhovered Hide("displayTextScreen")

    if headmaster_door_locked == False:
        imagebutton:
            xpos 860
            ypos 377
            focus_mask True
            idle "images/school/headmaster_room/morning/headmaster_S1/B1.png"
            hover "images/school/headmaster_room/morning/headmaster_S1/B1_hover.png"
            if clickable == True:
                action Hide("displayTextScreen")
            hovered Show("displayTextScreen", displayText = __("Headmaster"))
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor3_morning1")]
