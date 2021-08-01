screen b_house_bath_M_scr:

    add "images/Beach/Beach_House/Bathroom/M/map.jpg"


    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_bedroom_M1")]
            unhovered Hide("displayTextScreen")
    if MLR3_b_house_wait == 5:
        imagebutton:
            xpos 1668
            ypos 143
            focus_mask True
            idle "images/Beach/MLR3_beach_event/House/Shower/B1.png"
            hover "images/Beach/MLR3_beach_event/House/Shower/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_b_house_shower_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")