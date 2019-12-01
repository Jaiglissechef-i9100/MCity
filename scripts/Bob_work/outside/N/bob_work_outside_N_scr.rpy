screen bob_work_outside_N_scr:

    key "hide_windows" action NullAction()
    imagebutton:
        xpos 966
        ypos 223
        focus_mask True
        idle "images/Bob_work/outside/N/B1.png"
        hover "images/Bob_work/outside/N/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("[Dad_name]'s Workplace"))
            action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("bob_work_locked_label")]
            unhovered Hide("displayTextScreen")
