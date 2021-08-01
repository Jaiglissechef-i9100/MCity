screen classroom1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 485
        ypos 162
        focus_mask True
        idle "images/school/classroom1/morning/door1_morning_idle.png"
        hover "images/school/classroom1/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("School Corridor"))
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
            unhovered Hide("displayTextScreen")

    if not "img8_mc_classroom_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1893
                ypos 1039
                focus_mask True
                idle "images/secret_gallery/Bonus/MCClassroom Card.png"
                hover "images/secret_gallery/Bonus/MCClassroom Card_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"), addgimage("img8_mc_classroom_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1893
                ypos 1039
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"), addgimage("img8_mc_classroom_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

