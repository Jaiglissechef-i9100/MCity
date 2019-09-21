screen classroom2_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/classroom2/morning/door1_morning_idle.png"
        hover "images/school/classroom2/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("School Corridor"))
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
            unhovered Hide("displayTextScreen")

    if lily_school_day_scene1_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"
            hover "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Lily")
                clicked [Hide("displayTextScreen"), Jump("lily_school_day_scene1_v1_label")]
                unhovered Hide("displayTextScreen")

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
                hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Desk"))
                    action [Hide("displayTextScreen"),Jump("Table_day_Classroom_v1_label")]
                    unhovered Hide("displayTextScreen")

    if lily_school_day_scene2_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"
            hover "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Lily")
                clicked [Hide("displayTextScreen"), Jump("lily_school_day_scene2_v1_label")]
                unhovered Hide("displayTextScreen")

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
                hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = "Desk")
                    action [Hide("displayTextScreen"), Jump("Table_day_Classroom_v1_label")]
                    unhovered Hide("displayTextScreen")

    if lily_school_day_scene1_v1 == 3 and lily_school_day_scene2_v1 == 0 and can_lily_scene == True:

        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"
            hover "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Lily")
                clicked [Hide("displayTextScreen"), Jump("lily_school_scene_nothing_label")]
                unhovered Hide("displayTextScreen")

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
                hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Desk"))
                    action [Hide("displayTextScreen"),Jump("Table_day_Classroom_v1_label")]
                    unhovered Hide("displayTextScreen")

    if lily_work_in_progress_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"
            hover "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Lily")
                clicked [Hide("displayTextScreen"), Jump("lily_work_in_progress_v1_label")]
                unhovered Hide("displayTextScreen")

    if celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 977
            ypos 423
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"
            hover "images/school/classroom2/day/scenes/Table_Classroom_v1/desk_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Desk"))
                action [Hide("displayTextScreen"),Jump("Table_day_Classroom_v1_label")]
                unhovered Hide("displayTextScreen")

    if SR2_AS2 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"
            hover "images/school/classroom2/day/scenes/SR2_AS2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS2_label")]
                unhovered Hide("displayTextScreen")

    if SR2_AS3 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"
            hover "images/school/classroom2/day/scenes/SR2_AS2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS3_label")]
                unhovered Hide("displayTextScreen")

    if SR2_AS4 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"
            hover "images/school/classroom2/day/scenes/SR2_AS2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS4_label")]
                unhovered Hide("displayTextScreen")

    if SR2_AS5 == True and Sara_points == 2:
        imagebutton:
            xpos 1464
            ypos 449
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS5/B1.png"
            hover "images/school/classroom2/day/scenes/SR2_AS5/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS5_label")]
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

    if SR2_AS6 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"
            hover "images/school/classroom2/day/scenes/SR2_AS2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS6_label")]
                unhovered Hide("displayTextScreen")

screen classroom2_day_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/classroom2/morning/door1_morning_idle.png"

    if lily_school_day_scene1_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"

    if lily_school_day_scene2_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"

    if lily_school_day_scene1_v1 == 3 and lily_school_day_scene2_v1 == 0 and can_lily_scene == True:

        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"

        if celia_school_morning_scene1bv1 == 0:
            imagebutton:
                xpos 977
                ypos 423
                focus_mask True
                idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"

    if lily_work_in_progress_v1 == 1 and can_lily_scene == True:
        imagebutton:
            xpos 436
            ypos 320
            focus_mask True
            idle "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/Lily.png"

    if celia_school_morning_scene1bv1 == 0:
        imagebutton:
            xpos 977
            ypos 423
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/desk.png"

    if SR2_AS2 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"
    if SR2_AS3 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"

    if SR2_AS4 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"

    if SR2_AS5 == True and Sara_points == 2:
        imagebutton:
            xpos 1464
            ypos 449
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS5/B1.png"

    if SR2_AS6 == True and Sara_points == 2:
        imagebutton:
            xpos 1356
            ypos 444
            focus_mask True
            idle "images/school/classroom2/day/scenes/SR2_AS2/B1.png"

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
