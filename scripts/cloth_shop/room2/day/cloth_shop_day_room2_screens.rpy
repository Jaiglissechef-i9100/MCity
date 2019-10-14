screen cloth_shop_room2_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 377
        ypos 187
        focus_mask True
        idle "images/cloth_shop/room2/day/door_b1.png"
        hover "images/cloth_shop/room2/day/door_b1_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("cloth_shop_room3_label")]
        hovered Show("displayTextScreen", displayText = "Door")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("cloth_shop_open_label")]
    if cloth_shop_window_unlock == False:
        imagebutton:
            xpos 1276
            ypos 137
            focus_mask True
            idle "images/cloth_shop/room2/day/window_b2.png"
            hover "images/cloth_shop/room2/day/window_b2_hover.png"
            action [Hide("displayTextScreen"),Jump("cloth_shop_window_unlock_label")]
            hovered Show("displayTextScreen", displayText = "Window")
            unhovered Hide("displayTextScreen")

screen cloth_shop_room2_screen_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 377
        ypos 187
        focus_mask True
        idle "images/cloth_shop/room2/day/door_b1.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"

    if cloth_shop_window_unlock == False:
        imagebutton:
            xpos 1276
            ypos 137
            focus_mask True
            idle "images/cloth_shop/room2/day/window_b2.png"





screen cloth_shop_room2_robbery_screen:
    key "hide_windows" action NullAction()
    if cloth_shop_window_unlock == False and CR2_AS3_clean_after == True:
        imagebutton:
            xpos 1276
            ypos 137
            focus_mask True
            idle "images/cloth_shop/room2/day/window_b2.png"
            hover "images/cloth_shop/room2/day/window_b2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("cloth_shop_window_unlock_label")]
                hovered Show("displayTextScreen", displayText = "Window")
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 377
        ypos 187
        focus_mask True
        idle "images/cloth_shop/room2/day/door_b1.png"
        hover "images/cloth_shop/room2/day/door_b1_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("cloth_shop_room3_label")]
            hovered Show("displayTextScreen", displayText = "Door")
            unhovered Hide("displayTextScreen")

    if CR2_AS3_clean7 == False:
        imagebutton:
            xpos 940
            ypos 441
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/C1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/C1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/wood1.wav"),SetVariable("CR2_AS3_clean7", True),Jump("CR2_AS3_clean_counter_label2")]

    if CR2_AS3_clean7 == True:
        imagebutton:
            xpos 991
            ypos 302
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/C2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/C2.png"

    if CR2_AS3_clean5 == False:
        imagebutton:
            xpos 674
            ypos 596
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/A1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/A1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/metalic.wav"),SetVariable("CR2_AS3_clean5", True),Jump("CR2_AS3_clean_counter_label2")]
    if CR2_AS3_clean5 == True:
        imagebutton:
            xpos 708
            ypos 415
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/A2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/A2.png"

    if CR2_AS3_clean6 == False:
        imagebutton:
            xpos 669
            ypos 720
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/B1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/B1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/chair2.wav"),SetVariable("CR2_AS3_clean6", True),Jump("CR2_AS3_clean_counter_label2")]
    if CR2_AS3_clean6 == True:
        imagebutton:
            xpos 1173
            ypos 463
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/B2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/B2.png"



    if CR2_AS5 == True and Caroline_points == 2:
        imagebutton:
            xpos 1249
            ypos 407
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS5/B1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS5/B1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Hide("displayTextScreen"),Jump("CR2_AS5_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("cloth_shop_open_label")]