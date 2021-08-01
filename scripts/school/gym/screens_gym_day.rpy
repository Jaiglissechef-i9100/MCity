screen gym_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/gym/morning/door1_morning_idle.png"
        hover "images/school/gym/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Changing Room")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("changing_room_day1")]
            unhovered Hide("displayTextScreen")

    if not "img18_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1586
            ypos 198
            focus_mask True
            idle "images/secret_gallery/Bonus/B18.png"
            hover "images/secret_gallery/Bonus/B18_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img18_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_outside_day1")]