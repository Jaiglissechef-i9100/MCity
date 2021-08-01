screen sister_nerdy_evening:
    key "hide_windows" action NullAction()



    if sis_nerdy_evening_scene1_v1 == 1 and Sara_points == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 940
            ypos 404
            focus_mask True
            idle "images/home/sara_room/evening/scene1_v1/Sara.png"
            hover "images/home/sara_room/evening/scene1_v1/Sara_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_scene1_v1_l")]
                hovered Show("displayTextScreen", displayText = "Sara")
                unhovered Hide("displayTextScreen")

    if sis_nerdy_evening_scene2a_v1 == 1 and Sara_points == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 940
            ypos 404
            focus_mask True
            idle "images/home/sara_room/evening/scene1_v1/Sara.png"
            hover "images/home/sara_room/evening/scene1_v1/Sara_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_scene2a_v1_label")]
                hovered Show("displayTextScreen", displayText = "Sara")
                unhovered Hide("displayTextScreen")
    if Sara_points == 3 and SR3_ES1 == True and SR3_home_end == False:
        imagebutton:
            xpos 123
            ypos 527
            focus_mask True
            idle "images/v71/1_ES1/B1.png"
            hover "images/v71/1_ES1/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR3_ES1_label")]
                unhovered Hide("displayTextScreen")

    if SR3_home_end == True and SR3_home_end_both == False:
        imagebutton:
            xpos 700
            ypos 346
            focus_mask True
            idle "images/v71/2_WE/6_Home_End/B1.png"
            hover "images/v71/2_WE/6_Home_End/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sara")
                action [Hide("displayTextScreen"),Jump("SR3_we_home_end_label")]
                unhovered Hide("displayTextScreen")
    if SR3_home_end_both == True:
        add "images/v71/2_WE/6_Home_End/B2.png" xpos 855 ypos 325
    if SR3_home_end_bed == True:
        imagebutton:
            xpos 536
            ypos 425
            focus_mask True
            idle "images/v71/2_WE/6_Home_End/B3.png"
            hover "images/v71/2_WE/6_Home_End/B3_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Bed"))
                action [Hide("displayTextScreen"),Jump("SR3_we_home_end_bed")]
                unhovered Hide("displayTextScreen")
    if SR3_home_end_couch == True:
        imagebutton:
            xpos 18
            ypos 513
            focus_mask True
            idle "images/v71/2_WE/6_Home_End/B4.png"
            hover "images/v71/2_WE/6_Home_End/B4_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Couch"))
                action [Hide("displayTextScreen"),Jump("SR3_we_home_end_couch")]
                unhovered Hide("displayTextScreen")
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0 and Sara_points == 1 and can_gamepad_sara == True and  can_sis_nerdy_gamepad_change == 1 and MLR3_ES1 == False:
        imagebutton:
            xpos 1414
            ypos 651
            focus_mask True
            idle "images/home/sara_room/evening/scene3_v1/sara_gamepad.png"
            hover "images/home/sara_room/evening/scene3_v1/sara_gamepad_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("sis_nerdy_evening_gamepad_change_scene3_v1_label")]
                hovered Show("displayTextScreen", displayText = __("Sara's Gamepad"))
                unhovered Hide("displayTextScreen")

    if clickable == True and SR3_home_end_both == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]

