screen school_entrance_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 215
        ypos 254
        focus_mask True
        idle "images/school/school_entrance/morning/door1_morning_idle.png"
        hover "images/school/school_entrance/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Exit School")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_outside_day1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1651
        ypos 152
        focus_mask True
        idle "images/school/school_entrance/morning/door2_morning_idle.png"
        hover "images/school/school_entrance/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "School Corridor")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
            unhovered Hide("displayTextScreen")

    if sis_nerdy_school_scene2_v1 == 0 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene1_v1/sara_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("sis_nerdy_school_scene1_v1_label")]
                unhovered Hide("displayTextScreen")

    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 0 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene1_v1/sara_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("sis_nerdy_school_scene1_v1_label")]
                unhovered Hide("displayTextScreen")

    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 3 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene1_v1/sara_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("sis_nerdy_school_scene1_v1_label")]
                unhovered Hide("displayTextScreen")

    if sis_nerdy_school_scene2_v1 == 1 and Sara_points == 1:
        imagebutton:
            xpos 868
            ypos 290
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene2_v1/Lily_Sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene2_v1/Lily_Sara_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara and Lily")
                action [Hide("displayTextScreen"),Jump("sis_nerdy_school_scene2_v1_label")]
                unhovered Hide("displayTextScreen")

    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 1 and can1_sis_nerdy_school_scene3_v1 == True and can2_sis_nerdy_school_scene3_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 864
            ypos 285
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene3_v1/Lily_Sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene3_v1/Lily_Sara_Hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara and Lily")
                action [Hide("displayTextScreen"),Jump("sis_nerdy_school_scene3_v1_label")]
                unhovered Hide("displayTextScreen")
    if SR2_AS1 == True and Sara_points == 2:
        imagebutton:
            xpos 809
            ypos 484
            focus_mask True
            idle "images/school/school_entrance/day/scenes/SR2_AS1/B1.png"
            hover "images/school/school_entrance/day/scenes/SR2_AS1/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR2_AS1_label")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1259
        ypos 232
        focus_mask True
        idle "images/school/school_entrance/morning/school_entrance_locker_morning.png"
        hover "images/school/school_entrance/morning/school_entrance_locker_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Locker")
            action [Hide("displayTextScreen"),Jump("school_lockerv1_day_label")]
            unhovered Hide("displayTextScreen")

    if not "img6_exit_school_corridor_card" in gallery_photos.storage:
        imagebutton:
            xpos 944
            ypos 259
            focus_mask True
            idle "images/secret_gallery/Bonus/ExitSchoolCorridor Card.png"
            if clickable == True:
                hover "images/secret_gallery/Bonus/ExitSchoolCorridor Card_hover.png"
                action [Hide("displayTextScreen"), addgimage("img6_exit_school_corridor_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img23_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 738
            ypos 522
            focus_mask True
            idle "images/secret_gallery/Bonus/B23.png"
            hover "images/secret_gallery/Bonus/B23_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img23_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

screen school_entrance_day_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 215
        ypos 254
        focus_mask True
        idle "images/school/school_entrance/morning/door1_morning_idle.png"
        hover "images/school/school_entrance/morning/door1_morning_hover.png"

    imagebutton:
        xpos 1651
        ypos 152
        focus_mask True
        idle "images/school/school_entrance/morning/door2_morning_idle.png"
        hover "images/school/school_entrance/morning/door2_morning_hover.png"


    if sis_nerdy_school_scene2_v1 == 0 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"
            hover "images/school/school_entrance/day/scenes/sara_scene1_v1/sara_hover.png"


    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 0 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"


    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 3 and sis_nerdy_school_scene1_v1 == 1 and can2_sis_nerdy_school_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 872
            ypos 453
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene1_v1/sara.png"


    if sis_nerdy_school_scene2_v1 == 1 and Sara_points == 1:
        imagebutton:
            xpos 868
            ypos 290
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene2_v1/Lily_Sara.png"


    if sis_nerdy_school_scene2_v1 == 3 and sis_nerdy_school_scene3_v1 == 1 and can1_sis_nerdy_school_scene3_v1 == True and can2_sis_nerdy_school_scene3_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 864
            ypos 285
            focus_mask True
            idle "images/school/school_entrance/day/scenes/sara_scene3_v1/Lily_Sara.png"
    if SR2_AS1 == True and Sara_points == 2:
        imagebutton:
            xpos 809
            ypos 484
            focus_mask True
            idle "images/school/school_entrance/day/scenes/SR2_AS1/B1.png"
    imagebutton:
        xpos 1259
        ypos 232
        focus_mask True
        idle "images/school/school_entrance/morning/school_entrance_locker_morning.png"


    if not "img6_exit_school_corridor_card" in gallery_photos.storage:
        imagebutton:
            xpos 944
            ypos 259
            focus_mask True
            idle "images/secret_gallery/Bonus/ExitSchoolCorridor Card.png"

    if not "img23_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 738
            ypos 522
            focus_mask True
            idle "images/secret_gallery/Bonus/B23.png"