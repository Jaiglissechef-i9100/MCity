screen sister_nerdy_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_day1")]

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

screen sister_nerdy_day_notclickable:
    key "hide_windows" action NullAction()
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/evening/scene3_v1/sara_gamepad.png"
            hover "images/home/sara_room/evening/scene3_v1/sara_gamepad_hover.png"

