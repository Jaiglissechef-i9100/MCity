screen school_corridor2_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 850
        ypos 230
        focus_mask True
        idle "images/school/school_corridor2/morning/door1_morning_idle.png"
        hover "images/school/school_corridor2/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Door(Closed)")
            action [Play ("sound", "sfx/door_locked.mp3"),Jump("school_corridor2_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1372
        ypos 226
        focus_mask True
        idle "images/school/school_corridor2/morning/door2_morning_idle.png"
        hover "images/school/school_corridor2/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Teacher’s Office")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("teacher_room1_day1")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            clicked Jump("school_corridor1_day1")


    if not "img9_school_corrior2_card" in gallery_photos.storage:
        imagebutton:
            xpos 505
            ypos 1058
            focus_mask True
            idle "images/secret_gallery/Bonus/School Corrior2 Card.png"
            hover "images/secret_gallery/Bonus/School Corrior2 Card_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), addgimage("img9_school_corrior2_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")