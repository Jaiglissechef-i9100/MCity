screen kitchen_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door1_evening_idle.png"
        hover "images/home/kitchen/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Living Room"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door2_evening_idle.png"
        hover "images/home/kitchen/evening/door2_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Entrance"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_evening1")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door3_evening_idle.png"
        hover "images/home/kitchen/evening/door3_evening_hover.png"
        hovered Show("displayTextScreen", displayText = __("Bathroom"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_evening1")]
        unhovered Hide("displayTextScreen")

    if ml_evening_bathroom_scene_v1 == True and ml_points == 1 and CR3_ES1 == False:
        if camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/evening/door3_evening_idle.png"
                hover "images/home/kitchen/evening/door3_evening_hover.png"
                hovered Show("displayTextScreen", displayText = __("Bathroom"))
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"
                hover "images/home/kitchen/morning/door3_morning_hover.png"
                hovered Show("displayTextScreen", displayText = __("Bathroom"))
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_locked_scene_v1_label")]
                unhovered Hide("displayTextScreen")

    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1 and CR3_ES1 == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"
            hover "images/home/kitchen/evening/door3_evening_hover.png"
            hovered Show("displayTextScreen", displayText = __("Bathroom"))
            action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
            unhovered Hide("displayTextScreen")

    if MLR2_ES1 == True and ml_points == 2 and CR3_ES1 == False:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR2_ES1/b1.png"
            hover "images/home/kitchen/evening/scenes/MLR2_ES1/b1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR2_ES1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if CR3_ES1 == True and Caroline_points == 3 and MLR3_ES1 == False:
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

    if MLR3_ES1 == True and ml_points == 3:
        imagebutton:
            xpos 1024
            ypos 141
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR3_ES1/B1.png"
            hover "images/home/kitchen/evening/scenes/MLR3_ES1/B1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR3_ES1")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom and Sara"))
            else:
                hovered Show("displayTextScreen", displayText = __("Linda and Sara"))
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

    if ml_evening_bathroom_scene_v1 == True and ml_points == 1 and CR3_ES1 == False:
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

    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1 and CR3_ES1 == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"

    if MLR2_ES1 == True and ml_points == 2 and CR3_ES1 == False:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/morning/scenes/MLR2_ES1/b1.png"

    if CR3_ES1 == True and Caroline_points == 3 and MLR3_ES1 == False:
        imagebutton:
            xpos 637
            ypos 372
            focus_mask True
            idle "images/home/kitchen/evening/CR3_ES1_B1.png"

    if MLR3_ES1 == True and ml_points == 3:
        imagebutton:
            xpos 1024
            ypos 141
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR3_ES1/B1.png"
