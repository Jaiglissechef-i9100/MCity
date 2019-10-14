screen b_house_bath_N_scr:

    add "images/Beach/Beach_House/Bathroom/N/map.jpg"


    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_bedroom_M1")]
            unhovered Hide("displayTextScreen")