screen kitchen_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door1_evening_idle.png"
        hover "images/home/kitchen/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Living Room")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door2_evening_idle.png"
        hover "images/home/kitchen/evening/door2_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Entrance")
        if clickable == True:
            if SR3_home_end_bath > 0 and SR3_home_end == True:
                action [Jump("SR3_home_end_kitchen_dialogue")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_evening1")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door3_evening_idle.png"
        hover "images/home/kitchen/evening/door3_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Bathroom")
        if clickable == True:
            if SR3_home_end_bath > 0 and SR3_home_end == True:
                action [Hide("displayTextScreen"),Jump("SR3_home_end_clean")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_evening1")]
        unhovered Hide("displayTextScreen")

    if ml_evening_bathroom_scene_v1 == True and ml_points == 1 and CR3_ES1 == False and SR3_home_end == False:
        if camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/evening/door3_evening_idle.png"
                hover "images/home/kitchen/evening/door3_evening_hover.png"
                hovered Show("displayTextScreen", displayText = "Bathroom")
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"
                hover "images/home/kitchen/morning/door3_morning_hover.png"
                hovered Show("displayTextScreen", displayText = "Bathroom")
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_locked_scene_v1_label")]
                unhovered Hide("displayTextScreen")
    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1 and CR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"
            hover "images/home/kitchen/evening/door3_evening_hover.png"
            hovered Show("displayTextScreen", displayText = "Bathroom")
            action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
            unhovered Hide("displayTextScreen")
    if MLR2_ES1 == True and ml_points == 2 and CR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR2_ES1/b1.png"
            hover "images/home/kitchen/evening/scenes/MLR2_ES1/b1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR2_ES1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if CR3_ES1 == True and Caroline_points == 3 and MLR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 637
            ypos 372
            focus_mask True
            idle "images/home/kitchen/evening/CR3_ES1_B1.png"
            hover "images/home/kitchen/evening/CR3_ES1_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_ES1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")
    if MLR3_ES1 == True and ml_points == 3 and SR3_home_end == False:
        imagebutton:
            xpos 1024
            ypos 141
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR3_ES1/B1.png"
            hover "images/home/kitchen/evening/scenes/MLR3_ES1/B1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR3_ES1")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom and Sara")
            else:
                hovered Show("displayTextScreen", displayText = "Linda and Sara")
            unhovered Hide("displayTextScreen")

screen kitchen_evening_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door1_evening_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door2_evening_idle.png"


    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door3_evening_idle.png"


    if ml_evening_bathroom_scene_v1 == True and ml_points == 1 and CR3_ES1 == False and SR3_home_end == False:
        if camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/evening/door3_evening_idle.png"

        else:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"

    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1 and CR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"
    if MLR2_ES1 == True and ml_points == 2 and CR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/morning/scenes/MLR2_ES1/b1.png"

    if CR3_ES1 == True and Caroline_points == 3 and MLR3_ES1 == False and SR3_home_end == False:
        imagebutton:
            xpos 637
            ypos 372
            focus_mask True
            idle "images/home/kitchen/evening/CR3_ES1_B1.png"

    if MLR3_ES1 == True and ml_points == 3 and SR3_home_end == False:
        imagebutton:
            xpos 1024
            ypos 141
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR3_ES1/B1.png"