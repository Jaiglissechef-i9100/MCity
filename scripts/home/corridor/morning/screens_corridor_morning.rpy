screen corridor_morning:
    key "hide_windows" action NullAction()
    add "/images/home/corridor/morning/Coridor_Morning.jpg"
    imagebutton:
        xpos 937
        ypos 195
        focus_mask True
        idle "images/home/corridor/morning/painting_B1.png"
        hover "images/home/corridor/morning/painting_B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Painting"))
            action [Hide("displayTextScreen"),Jump("painting_corridor_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 178
        ypos 167
        focus_mask True
        idle "images/home/corridor/morning/door1_morning_idle.png"
        hover "images/home/corridor/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Caroline's Bedroom"))
        if clickable == True:
            if SR3_we_bath == True:
                action Jump("SR3_bath_time_corr")
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("caroline_room_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 640
        ypos 224
        focus_mask True
        idle "images/home/corridor/morning/door2_morning_idle.png"
        hover "images/home/corridor/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("My Bedroom"))
            action [Play ("sound", "sfx/door_open.mp3"),Jump("mc_room_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1279
        ypos 200
        focus_mask True
        idle "images/home/corridor/morning/door3_morning_idle.png"
        hover "images/home/corridor/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
        if clickable == True:
            if SR3_we_bath == True:
                action Jump("SR3_bath_time_corr")
            if SR3_we_bath == False:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("sister_nerdy_morning1")]
            if SR3_MS1 == True:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("SR3_MS1")]
            unhovered Hide("displayTextScreen")

    if SR2_grounded == True:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/morning/door3_morning_idle.png"
            hover "images/home/corridor/morning/door3_morning_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
                action [Hide("displayTextScreen"),Jump("SR2_grounded_label")]
                unhovered Hide("displayTextScreen")

    if SR3_grounded == True and Sara_points == 3:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/morning/door3_morning_idle.png"
            hover "images/home/corridor/morning/door3_morning_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Sara's Bedroom"))
                action [Hide("displayTextScreen"),Jump("SR2_grounded_label")]
                unhovered Hide("displayTextScreen")

    if salon_ml_first_visit == True:
        imagebutton:
            xpos 1660
            ypos 0
            focus_mask True
            idle "images/home/corridor/morning/door4_morning_idle.png"
            hover "images/home/corridor/morning/door4_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Living Room"))
            if clickable == True:
                action [Jump("salon_morning1")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            if SR3_we_bath == True:
                action Jump("SR3_bath_time_corr")
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("entrace1_morning1")]

    if salon_ml_first_visit == False:
        imagebutton:
            xpos 1660
            ypos 0
            focus_mask True
            idle "images/home/corridor/morning/door4_morning_idle.png"
            hover "images/home/corridor/morning/door4_morning_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Living Room"))
                action [Hide("displayTextScreen"), Jump("ML_morning_scene0_v1_label")]
                unhovered Hide("displayTextScreen")

