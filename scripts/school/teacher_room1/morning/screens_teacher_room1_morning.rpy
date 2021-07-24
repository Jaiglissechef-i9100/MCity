screen teacher_room1_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/teacher_room1/morning/door1_morning_idle.png"
        hover "images/school/teacher_room1/morning/door1_morning_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor2_morning1")]
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Corridor"))
            unhovered Hide("displayTextScreen")

    if can_celia_school_morning_scene1bv1 == 0 and celia_school_morning_scene1bv1 == 1 and can_celia_morning_school_work_in_pr == True:
        imagebutton:
            xpos 1276
            ypos 205
            focus_mask True
            idle "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b.png"
            hover "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("celia_school_morning_scene1bv1_label")]
                hovered Show("displayTextScreen", displayText = "Celia")
                unhovered Hide("displayTextScreen")

    if celia_work_in_progress_v1 == 1 and can_celia_morning_school_work_in_pr == True and Celia_points == 1:
        imagebutton:
            xpos 1276
            ypos 205
            focus_mask True
            idle "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b.png"
            hover "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("celia_work_in_progress_v1_label")]
                hovered Show("displayTextScreen", displayText = "Celia")
                unhovered Hide("displayTextScreen")

    if Celia_points == 2 and CeR2_MS3 >= 1:
        imagebutton:
            xpos 1250
            ypos 215
            focus_mask True
            idle "images/CeR2/MS3/Celia.png"
            hover "images/CeR2/MS3/Celia_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CeR2_MS3_lab")]
                hovered Show("displayTextScreen", displayText = "Celia")
                unhovered Hide("displayTextScreen")
    if can_celia_laptopv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room1/morning/celia_laptopv1/celia_laptopb1_v1.png"
            hover "images/school/teacher_room1/morning/celia_laptopv1/celia_laptopb1_v1_hover.png"
            if clickable == True:
                action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("celia_morning_laptopv1_label")]
                hovered Show("displayTextScreen", displayText = __("Celia's Laptop"))
                unhovered Hide("displayTextScreen")

screen teacher_room1_morning_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/teacher_room1/morning/door1_morning_idle.png"

    if can_celia_school_morning_scene1bv1 == 0 and celia_school_morning_scene1bv1 == 1 and can_celia_morning_school_work_in_pr == True:
        imagebutton:
            xpos 1276
            ypos 205
            focus_mask True
            idle "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b.png"

    if celia_work_in_progress_v1 == 1 and can_celia_morning_school_work_in_pr == True and Celia_points == 2:
        imagebutton:
            xpos 1276
            ypos 205
            focus_mask True
            idle "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/celia1b.png"


    if can_celia_laptopv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room1/morning/celia_laptopv1/celia_laptopb1_v1.png"
