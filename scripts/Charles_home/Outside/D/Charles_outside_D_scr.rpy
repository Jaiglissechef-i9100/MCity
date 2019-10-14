

screen Charles_outside_D_scr:
    if Charles_end == False:
        imagebutton:
            xpos 720
            ypos 58
            focus_mask True
            idle "/images/charles_home/outside/M/B1.png"
            hover "/images/charles_home/outside/M/B1_hover.png"

            if clickable == True:
                action Jump("Charles_outside2_M1")
                unhovered Hide("displayTextScreen")
    if Charles_end == True:
        imagebutton:
            xpos 720
            ypos 58
            focus_mask True
            idle "/images/charles_home/outside/M/B1a.png"
            hover "/images/charles_home/outside/M/B1a_hover.png"

            if clickable == True:
                action Jump("Charles_outside2_M1")
                unhovered Hide("displayTextScreen")
    if Ch_S_door == True:
        imagebutton:
            xpos 1275
            ypos 185
            focus_mask True
            idle "/images/charles_home/outside/M/B2.png"
            hover "/images/charles_home/outside/M/B2_hover.png"
            hovered Show("displayTextScreen", displayText = "Doors")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ch_doors_lab")]
                unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 1436
            ypos 241
            focus_mask True
            idle "/images/charles_home/outside/M/B3.png"
            hover "/images/charles_home/outside/M/B3_hover.png"
            hovered Show("displayTextScreen", displayText = "Window")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ch_window_lab")]
                unhovered Hide("displayTextScreen")