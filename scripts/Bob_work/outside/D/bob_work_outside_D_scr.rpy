


screen bob_work_outside_D_scr:

    key "hide_windows" action NullAction()
    imagebutton:
        xpos 966
        ypos 223
        focus_mask True
        idle "images/Bob_work/outside/D/B1_D.png"
        hover "images/Bob_work/outside/D/B1_D_hover.png"
        hovered Show("displayTextScreen", displayText = "Bob's Workplace")
        action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_entrance_M1")]
        unhovered Hide("displayTextScreen")