screen sister_nerdy_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_morning1")]

    if sis_nerdy_scene1_v1== 1 and after_sis_nerdy_scene1_v1 == 1 and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"
            hover "images/home/sara_room/morning/Scene1_v1/sara_hover.png"
            action [Hide("displayTextScreen"), Jump("scene1_v1")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if sis_nerdy_scene1_v1== 2 and after_sis_nerdy_scene1_v1 == 2 and next_day == False and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"
            hover "images/home/sara_room/morning/Scene1_v1/sara_hover.png"
            action [Hide("displayTextScreen"), Jump("after_sis_nerdy_scene1_v1")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if next_day == True and after_sis_nerdy_scene1_v1 == 2 and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"
            hover "images/home/sara_room/morning/Scene1_v1/sara_hover.png"
            action [Hide("displayTextScreen"), Jump("next_day_after_sis_nerdy_scene1_v1")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if drawer_sis_nerdy == 1 and Sara_points == 1 and can_sara_scene3_v1 == True:
        imagebutton:
            xpos 1387
            ypos 692
            focus_mask True
            idle "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"
            hover "images/home/sara_room/morning/Scene3_v1/drawer_sara_hover.png"
            action [Hide("displayTextScreen"), Jump("sis_nerdy_scene3_1_v1")]
            hovered Show("displayTextScreen", displayText = __("Drawer"))
            unhovered Hide("displayTextScreen")

    if drawer_sis_nerdy == 2 and Sara_points == 1 and can_sara_scene3_v1 == True:
        imagebutton:
            xpos 1387
            ypos 692
            focus_mask True
            idle "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"
            hover "images/home/sara_room/morning/Scene3_v1/drawer_sara_hover.png"
            action [Hide("displayTextScreen"), Jump("sis_nerdy_scene3_1_v1")]
            hovered Show("displayTextScreen", displayText = __("Drawer"))
            unhovered Hide("displayTextScreen")

    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/evening/scene3_v1/sara_gamepad.png"
            hover "images/home/sara_room/evening/scene3_v1/sara_gamepad_hover.png"
            action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_gamepad_change_scene3_v1_label_can")]
            hovered Show("displayTextScreen", displayText = __("Sara's Gamepad"))
            unhovered Hide("displayTextScreen")

    if SR2_MS1 == True and Sara_points == 2:
        imagebutton:
            xpos 990
            ypos 471
            focus_mask True
            idle "images/home/sara_room/morning/SR2_MS1/B1.png"
            hover "images/home/sara_room/morning/SR2_MS1/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("SR2_MS1_label")]
                hovered Show("displayTextScreen", displayText = "Sara")
                unhovered Hide("displayTextScreen")

    if SR2_MS2 == True and can_SR2_MS2 == True and Sara_points == 2:
        imagebutton:
            xpos 959
            ypos 277
            focus_mask True
            idle "images/home/sara_room/morning/SR2_MS2/B1.png"
            hover "images/home/sara_room/morning/SR2_MS2/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("SR2_MS2_label")]
                hovered Show("displayTextScreen", displayText = "Sara")
                unhovered Hide("displayTextScreen")

screen sister_nerdy_morning_notclickable:
    key "hide_windows" action NullAction()

    if sis_nerdy_scene1_v1== 1 and after_sis_nerdy_scene1_v1 == 1 and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"

    if sis_nerdy_scene1_v1== 2 and after_sis_nerdy_scene1_v1 == 2 and next_day == False and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"

    if next_day == True and after_sis_nerdy_scene1_v1 == 2 and sis_nerdy_in_room == True and Sara_points == 1:
        imagebutton:
            xpos 958
            ypos 403
            focus_mask True
            idle "images/home/sara_room/morning/Scene1_v1/sara.png"

    if drawer_sis_nerdy == 1 and Sara_points == 1 and can_sara_scene3_v1 == True:
        imagebutton:
            xpos 1387
            ypos 692
            focus_mask True
            idle "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"

    if drawer_sis_nerdy == 2 and Sara_points == 1 and can_sara_scene3_v1 == True:
        imagebutton:
            xpos 1387
            ypos 692
            focus_mask True
            idle "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"

    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/evening/scene3_v1/sara_gamepad.png"

    if SR2_MS1 == True and Sara_points == 2:
        imagebutton:
            xpos 990
            ypos 471
            focus_mask True
            idle "images/home/sara_room/morning/SR2_MS1/B1.png"

    if SR2_MS2 == True and can_SR2_MS2 == True and Sara_points == 2:
        imagebutton:
            xpos 959
            ypos 277
            focus_mask True
            idle "images/home/sara_room/morning/SR2_MS2/B1.png"

