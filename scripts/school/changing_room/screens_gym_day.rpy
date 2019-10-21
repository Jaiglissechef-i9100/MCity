screen changing_room_day:
    key "hide_windows" action NullAction()

    if not "img34_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1911
                ypos 481
                focus_mask True
                idle "images/secret_gallery/Bonus/B34a.png"
                hover "images/secret_gallery/Bonus/B34a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img34_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1911
                ypos 481
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img34_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/changing_room/morning/door1_morning_idle.png"
        hover "images/school/changing_room/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("GYM"))
        clicked Jump("gym_day1")
        unhovered Hide("displayTextScreen")
