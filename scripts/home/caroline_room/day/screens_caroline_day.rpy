screen caroline_room_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_day1")]

    if Caroline_points == 3 and CR3_AS7a_can1 == True:
        imagebutton:
            xpos 946
            ypos 379
            focus_mask True
            idle "/images/home/caroline_room/day/CR3_AS7a_B1.png"
            hover "/images/home/caroline_room/day/CR3_AS7a_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS7a_label")]
                hovered Show("displayTextScreen", displayText = __("Caroline's Bed"))
                unhovered Hide("displayTextScreen")

