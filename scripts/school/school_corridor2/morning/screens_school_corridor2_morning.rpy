screen school_corridor2_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 850
        ypos 230
        focus_mask True
        idle "images/school/school_corridor2/morning/door1_morning_idle.png"
        hover "images/school/school_corridor2/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Security Room")
        if clickable == True:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("moni_M1")]
        if CeR2_moni == 5:
            action [Hide("displayTextScreen"),Jump("CeR2_del_data")]

        unhovered Hide("displayTextScreen")

    if CeR2_moni == 5:
        imagebutton:
            xpos 1168
            ypos 270
            focus_mask True
            idle "/images/CeR2/monitoring/Deleting Data/B1.png"
            hover "/images/CeR2/monitoring/Deleting Data/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Celia and Big Jake")
                action [Hide("displayTextScreen"),Jump("CeR2_del_data")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1372
        ypos 226
        focus_mask True
        idle "images/school/school_corridor2/morning/door2_morning_idle.png"
        hover "images/school/school_corridor2/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Teacher’s Office")

        if clickable == True:
            if Celia_points == 2 and CeR2_MS2 == 2:
                action [Hide("displayTextScreen"), Play ("sound", "sfx/door_open.mp3"),Jump("CeR2_MS2_lab")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("teacher_room1_morning1")]

            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            clicked Jump("school_corridor1_morning1")


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