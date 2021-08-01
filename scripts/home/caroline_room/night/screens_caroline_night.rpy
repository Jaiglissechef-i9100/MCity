screen caroline_room_night:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_night1")]

    if caroline_room_night_scene1 == True and CR2_NS3 == False and CR2_NS2 == False and CR3_deal_aff == False and C_NS_locked == False:
        imagebutton:
            xpos 1089
            ypos 474
            focus_mask True
            idle "images/home/caroline_room/night/scenes/caroline_room_night_scene1/caroline_b1.png"
            hover "images/home/caroline_room/night/scenes/caroline_room_night_scene1/caroline_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("caroline_room_night_scene1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if CR2_NS3 ==  True and CR3_deal_aff == False:
        imagebutton:
            xpos 1154
            ypos 514
            focus_mask True
            idle "images/home/caroline_room/night/scenes/CR2_NS3/B1.png"
            hover "images/home/caroline_room/night/scenes/CR2_NS3/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("CR2_NS3_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if CR3_NS1 == True and CR3_deal_aff == True and Caroline_points == 3:
        imagebutton:
            xpos 981
            ypos 485
            focus_mask True
            idle "images/home/caroline_room/night/CR3_NS1_B1.png"
            hover "images/home/caroline_room/night/CR3_NS1_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("CR3_NS1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

