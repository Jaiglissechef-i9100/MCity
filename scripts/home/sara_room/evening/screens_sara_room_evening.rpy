screen sister_nerdy_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]

    if sis_nerdy_evening_scene1_v1 == 1 and Sara_points == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 940
            ypos 404
            focus_mask True
            idle "images/home/sara_room/evening/scene1_v1/Sara.png"
            hover "images/home/sara_room/evening/scene1_v1/Sara_hover.png"
            clicked [Hide("displayTextScreen"),Jump("sis_nerdy_evening_scene1_v1_l")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if sis_nerdy_evening_scene2a_v1 == 1 and Sara_points == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 940
            ypos 404
            focus_mask True
            idle "images/home/sara_room/evening/scene1_v1/Sara.png"
            hover "images/home/sara_room/evening/scene1_v1/Sara_hover.png"
            clicked [Hide("displayTextScreen"),Jump("sis_nerdy_evening_scene2a_v1_label")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/evening/scene3_v1/sara_gamepad.png"
            hover "images/home/sara_room/evening/scene3_v1/sara_gamepad_hover.png"
            action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_gamepad_change_scene3_v1_label")]
            hovered Show("displayTextScreen", displayText = __("Sara's Gamepad"))
            unhovered Hide("displayTextScreen")
