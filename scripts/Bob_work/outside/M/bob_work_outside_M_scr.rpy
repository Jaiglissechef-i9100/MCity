screen bob_work_outside_M_scr:

    key "hide_windows" action NullAction()
    if persistent.incest_patch == True:
        imagebutton:
            xpos 966
            ypos 223
            focus_mask True
            idle "images/Bob_work/outside/D/B1_D.png"
            hover "images/Bob_work/outside/D/B1_D_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Dad's Workplace"))
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_entrance_M1")]
                unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            xpos 966
            ypos 223
            focus_mask True
            idle "images/Bob_work/outside/D/B1_D.png"
            hover "images/Bob_work/outside/D/B1_D_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Bob's Workplace"))
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_entrance_M1")]
                unhovered Hide("displayTextScreen")

    if Bob_in_work == True:
        imagebutton:
            xpos 137
            ypos 296
            focus_mask True
            idle "images/Bob_work/outside/M/B2_M.png"
            hover "images/Bob_work/outside/M/B2_M_hover.png"
            hovered Show("displayTextScreen", displayText = __("Car"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("bob_car_label")]
                unhovered Hide("displayTextScreen")
