screen therapist_room_morning:
    key "hide_windows" action NullAction()

    if not "img41_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 211
                ypos 271
                focus_mask True
                idle "images/secret_gallery/Bonus/B41a.png"
                hover "images/secret_gallery/Bonus/B41a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img41_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 211
                ypos 271
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img41_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img42_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1677
                ypos 632
                focus_mask True
                idle "images/secret_gallery/Bonus/B42a.png"
                hover "images/secret_gallery/Bonus/B42a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img42_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1677
                ypos 632
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img42_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/therapist_room/morning/door1_morning_idle.png"
        hover "images/school/therapist_room/morning/door1_morning_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor3_morning1")]
            hovered Show("displayTextScreen", displayText = __("Corridor Floor 1"))
            unhovered Hide("displayTextScreen")

    if Judy_in_her_Office == True:
        imagebutton:
            xpos 919
            ypos 245
            focus_mask True
            idle "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_scene1_v1_b1.png"
            hover "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_scene1_v1_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("judy_menu_v1_label")]
                hovered Show("displayTextScreen", displayText = "Judy")
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1293
        ypos 300
        focus_mask True
        idle "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_cupboardv1.png"
        hover "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_cupboardv1_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("judy_morning_cupboardv1_label")]
            hovered Show("displayTextScreen", displayText = __("Cupboard"))
            unhovered Hide("displayTextScreen")
