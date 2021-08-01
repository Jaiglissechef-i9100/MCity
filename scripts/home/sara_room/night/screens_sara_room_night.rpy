screen sister_nerdy_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_night1")]


    if sis_nerdy_night_sleeping1_v1 == 1 and can_sis_nerdy_night_sleeping1_v1 == True and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
            hover "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1_hover.png"
            clicked [Hide("displayTextScreen"),Jump("sis_nerdy_night_sleeping1_v1_label")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")
    if sis_nerdy_night_sleeping1_v1 == 1 and can_sis_nerdy_night_sleeping1_v1 == False and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
            hover "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
            clicked [Hide("displayTextScreen"),Jump("sis_nerdy_night_sleeping1_v1_label")]

    if sara_room_night_sleeping2 == True and Sara_points == 1 and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
            hover "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1_hover.png"
            clicked [Hide("displayTextScreen"),Jump("sara_room_night_sleeping2_label")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")
    if sara_room_night_sleeping2 == True and Sara_points >= 2 and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
            hover "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1_hover.png"
            clicked [Hide("displayTextScreen"),Jump("sara_room_night_sleeping2_label")]
            hovered Show("displayTextScreen", displayText = "Sara")
            unhovered Hide("displayTextScreen")

    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/night/game_pad_b1.png"
            hover "images/home/sara_room/night/game_pad_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_gamepad_change_scene3_v1_label_can")]
            hovered Show("displayTextScreen", displayText = "Sara's Gamepad")
            unhovered Hide("displayTextScreen")

screen sister_nerdy_night_notclikcable:

    key "hide_windows" action NullAction()
    if sis_nerdy_night_sleeping1_v1 == 1 and can_sis_nerdy_night_sleeping1_v1 == True and Sara_points == 1 and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"


    if sis_nerdy_night_sleeping1_v1 == 1 and can_sis_nerdy_night_sleeping1_v1 == False and Sara_points == 1 and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"

    if sara_room_night_sleeping2 == True and Sara_points == 1 and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"
    if sara_room_night_sleeping2 == True and Sara_points >= 2 and S_N_inbed == True and S_N_inbed == True:
        imagebutton:
            xpos 536
            ypos 426
            focus_mask True
            idle "images/home/sara_room/night/scenes/sleeping1/Sara_sleeping1.png"


    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/night/game_pad_b1.png"