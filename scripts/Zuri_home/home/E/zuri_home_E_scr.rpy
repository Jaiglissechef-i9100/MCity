

screen zuri_home_E_scr:
    key "hide_windows" action NullAction()
    if Zv2_ES1 == True:
        imagebutton:
            xpos 35
            ypos 374
            focus_mask True
            idle "images/Zuri_home/outside/E/scenes/Z_ES1/B1.png"
            hover "images/Zuri_home/outside/E/scenes/Z_ES1/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Sit on Couch")
                action [Hide("displayTextScreen"),Jump("Z_ES1_q1_label")]
                unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 1296
            ypos 186
            focus_mask True
            idle "images/Zuri_home/outside/E/scenes/Z_ES1/B2.png"
            hover "images/Zuri_home/outside/E/scenes/Z_ES1/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri")
                action [Hide("displayTextScreen"),Jump("Z_ES1_q2_label")]
                unhovered Hide("displayTextScreen")
    if Zv2_ES2 == True:
        imagebutton:
            xpos 287
            ypos 293
            focus_mask True
            idle "images/Zuri_home/home/E/scenes/Zv2_ES2/B1.png"
            hover "images/Zuri_home/home/E/scenes/Zv2_ES2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri and Suri")
                action [Hide("displayTextScreen"),Jump("Zv2_ES2_label")]
                unhovered Hide("displayTextScreen")

    if Zv2_ES3 == True:
        imagebutton:
            xpos 287
            ypos 293
            focus_mask True
            idle "images/Zuri_home/home/E/scenes/Zv2_ES2/B1.png"
            hover "images/Zuri_home/home/E/scenes/Zv2_ES2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri and Suri")
                action [Hide("displayTextScreen"),Jump("Zv2_ES3_label")]
                unhovered Hide("displayTextScreen")
    if Zv2_ES3a == True:
        imagebutton:
            xpos 287
            ypos 293
            focus_mask True
            idle "images/Zuri_home/home/E/scenes/Zv2_ES2/B1.png"
            hover "images/Zuri_home/home/E/scenes/Zv2_ES2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri and Suri")
                action [Hide("displayTextScreen"),Jump("Zv2_ES3a_label")]
                unhovered Hide("displayTextScreen")
    if Zv2_ES4 == True:
        imagebutton:
            xpos 287
            ypos 293
            focus_mask True
            idle "images/Zuri_home/home/E/scenes/Zv2_ES2/B1.png"
            hover "images/Zuri_home/home/E/scenes/Zv2_ES2/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri and Suri")
                action [Hide("displayTextScreen"),Jump("Zv2_ES4_label")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("zuri_homeoutside_M1")]