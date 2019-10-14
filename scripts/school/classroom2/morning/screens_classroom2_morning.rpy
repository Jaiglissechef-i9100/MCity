screen classroom2_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/classroom2/morning/door1_morning_idle.png"
        hover "images/school/classroom2/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("School Corridor"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_morning1")]
            unhovered Hide("displayTextScreen")

    if celia_school_morning_scene1v1 == 1 and celia_school_morning_scene2v1 == 0 and celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 1531
            ypos 159
            focus_mask True
            idle "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/celia_school_scene1.png"
            hover "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/celia_school_scene1_hover.png"
            hovered Show("displayTextScreen", displayText = "Celia")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("celia_school_morning_scene1v1_label")]
                unhovered Hide("displayTextScreen")

    if celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 977
            ypos 423
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
            hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
            hovered Show("displayTextScreen", displayText = __("Desk"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Table_morning_Classroom_v1_label")]
                unhovered Hide("displayTextScreen")
    if celia_school_morning_scene2v1 == 1:
        imagebutton:
            xpos 977
            ypos 423
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
            hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Desk")
                action [Hide("displayTextScreen"),Jump("Table_day_Classroom_v1_label")]
                unhovered Hide("displayTextScreen")
    if not "img24_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 406
            ypos 686
            focus_mask True
            idle "images/secret_gallery/Bonus/B24.png"
            hover "images/secret_gallery/Bonus/B24_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img24_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img25_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1150
            ypos 110
            focus_mask True
            idle "images/secret_gallery/Bonus/B25.png"
            hover "images/secret_gallery/Bonus/B25_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img25_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

screen classroom2_morning_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/classroom2/morning/door1_morning_idle.png"

    if celia_school_morning_scene1v1 == 1 and celia_school_morning_scene2v1 == 0 and celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 1531
            ypos 159
            focus_mask True
            idle "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/celia_school_scene1.png"

    if celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 977
            ypos 423
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"

    if not "img24_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 406
            ypos 686
            focus_mask True
            idle "images/secret_gallery/Bonus/B24.png"

    if not "img25_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1150
            ypos 110
            focus_mask True
            idle "images/secret_gallery/Bonus/B25.png"
