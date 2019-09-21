screen a_bedroom_D_scr:
    key "hide_windows" action NullAction()

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("a_living_M1")]
