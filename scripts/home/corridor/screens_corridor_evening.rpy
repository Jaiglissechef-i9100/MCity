screen corridor_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 937
        ypos 195
        focus_mask True
        idle "images/home/corridor/evening/painting_B1.png"
        hover "images/home/corridor/evening/painting_B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Painting"))
            action [Hide("displayTextScreen"),Jump("painting_corridor_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 178
        ypos 167
        focus_mask True
        idle "images/home/corridor/evening/door1_evening_idle.png"
        hover "images/home/corridor/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Caroline's Bedroom"))
        if clickable == True:
            if SR3_home_end == True:
                action [Jump("SR3_home_end_corridor_dialogue")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("caroline_room_evening1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 640
        ypos 224
        focus_mask True
        idle "images/home/corridor/evening/door2_evening_idle.png"
        hover "images/home/corridor/evening/door2_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("My Bedroom"))
        if clickable == True:
            if SR3_home_end == True:
                action [Jump("SR3_home_end_corridor_dialogue")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("mc_room_evening1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1279
        ypos 200
        focus_mask True
        idle "images/home/corridor/evening/door3_evening_idle.png"
        hover "images/home/corridor/evening/door3_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
        if clickable == True:
            if SR3_home_end == True:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("sister_nerdy_evening1")]
            if SR3_home_end_bath == 1 and SR3_home_end == True:
                action [Jump("SR3_home_end_corridor_dialogue")]
            if SR3_home_end_bath == 2:
                action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("SR3_we_home_end_penetrate_con1")]
            if SR3_home_end == False:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("sister_nerdy_evening1")]
            if SR3_ES1_talked == False and Sara_points == 3:
                action [Hide("displayTextScreen"),Jump("SR3_ES1_label")]
            unhovered Hide("displayTextScreen")

    if SR2_grounded == True:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/evening/door3_evening_idle.png"
            hover "images/home/corridor/evening/door3_evening_hover.png"
            hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
            if clickable == True:

                action [Hide("displayTextScreen") ,Jump("SR2_grounded_label")]
                unhovered Hide("displayTextScreen")
    if SR3_grounded == True and Sara_points == 3:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/evening/door3_evening_idle.png"
            hover "images/home/corridor/evening/door3_evening_hover.png"
            hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
            if clickable == True:
                action [Hide("displayTextScreen") ,Jump("SR2_grounded_label")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1660
        ypos 0
        focus_mask True
        idle "images/home/corridor/evening/door4_evening_idle.png"
        hover "images/home/corridor/evening/door4_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Living Room"))
        if clickable == True:
            if SR3_home_end == True:
                action [Jump("SR3_home_end_corridor_dialogue")]
            if SR3_home_end_bath > 0 and SR3_home_end == True:
                action [Jump("salon_evening1")]
            if SR3_home_end == False:
                action [Jump("salon_evening1")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            if SR3_home_end_bath > 0 and SR3_home_end == True:
                action [Jump("SR3_home_end_corridor_dialogue")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("entrace1_evening1")]

