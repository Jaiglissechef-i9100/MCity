screen Charles_outside_E_scr:
    if Charles_end == False:
        imagebutton:
            xpos 720
            ypos 58
            focus_mask True
            idle "/images/charles_home/outside/E/B1.png"
            hover "/images/charles_home/outside/E/B1_hover.png"
            if clickable == True:
                action Jump("Charles_outside2_M1")
                unhovered Hide("displayTextScreen")
    if Charles_end == True:
        imagebutton:
            xpos 720
            ypos 58
            focus_mask True
            idle "/images/charles_home/outside/E/B1a.png"
            hover "/images/charles_home/outside/E/B1a_hover.png"
            if clickable == True:
                action Jump("Charles_outside2_M1")
                unhovered Hide("displayTextScreen")
    if Ch_S_door == True:
        imagebutton:
            xpos 1275
            ypos 185
            focus_mask True
            idle "/images/charles_home/outside/E/B2.png"
            hover "/images/charles_home/outside/E/B2_hover.png"
            hovered Show("displayTextScreen", displayText = __("Doors"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ch_doors_lab")]
                unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 1436
            ypos 241
            focus_mask True
            idle "/images/charles_home/outside/E/B3.png"
            hover "/images/charles_home/outside/E/B3_hover.png"
            hovered Show("displayTextScreen", displayText = __("Window"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ch_window_lab")]
                unhovered Hide("displayTextScreen")

