screen a_bedroom_N_scr:
    key "hide_windows" action NullAction()

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("a_living_M1")]
    if LiR1_NS3 == True:
        imagebutton:
            xpos 722
            ypos 412
            focus_mask True
            idle "/images/a_home/Inside/Bedroom/N/scenes/LiR1_NS3/B1.png"
            hover "/images/a_home/Inside/Bedroom/N/scenes/LiR1_NS3/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("LiR1_NS3_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Auntie and Yazmin"))
            else:
                hovered Show("displayTextScreen", displayText = __("Liza and Yazmin"))
            unhovered Hide("displayTextScreen")
