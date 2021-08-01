screen salon_morning:
    key "hide_windows" action NullAction()
    add "/images/home/salon/morning/Salon_morning.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door1_morning_idle.png"
        hover "images/home/salon/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Corridor")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door2_morning_idle.png"
        hover "images/home/salon/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Kitchen")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door3_morning_idle.png"
        hover "images/home/salon/morning/door3_morning_hover.png"
        if renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Parent's Bedroom")
        if not renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Main Bedroom")
        if clickable == True:
            if SR3_we_bath == True:
                action Jump("SR3_bath_time_living")
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("parents_bedroom_morning1")]
            unhovered Hide("displayTextScreen")
    if MLR3_MS1 == True and ml_points == 3 and SR3_we_bath == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/morning/door3_morning_idle.png"
            hover "images/home/salon/morning/door3_morning_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Parent's Bedroom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Main Bedroom")
            if clickable == True:
                action [Jump("MLR3_MS1")]
                unhovered Hide("displayTextScreen")

    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit == 1 and ml_can_salon_morning_scene2 == True and SR3_we_bath == False:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"
            hover "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("ml_morning_salon_scenes1to3_v1_label")]
                unhovered Hide("displayTextScreen")
    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit > 1 and ml_can_salon_morning_scene2 == True  and SR3_we_bath == False:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"
            hover "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("ml_morning_salon_scenes1to3_v1_label")]
                unhovered Hide("displayTextScreen")
    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit > 3 and ml_can_salon_morning_scene2 == True  and SR3_we_bath == False:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"
            hover "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("ml_morning_salon_scenes1to3_v1_label")]
                unhovered Hide("displayTextScreen")
    if ml_salon_morning_visit == 4 and ml_can_salon_morning_scene == False and SR3_we_bath == False:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"
            hover "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Mom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("ml_morning_salon_scenes1to3_v1_label")]
                unhovered Hide("displayTextScreen")
    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/morning/Money Salon Morning.png"
            hover "images/home/salon/morning/Money Salon Morning_hover.png"
            hovered Show("displayTextScreen", displayText = "Money")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("salon_money_label")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"
        hover "images/home/salon/morning/paint_b1_hover.png"
        hovered Show("displayTextScreen", displayText = "Painting")
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("salon_paint_label")]
            unhovered Hide("displayTextScreen")
screen salon_morning_notclickable:
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door1_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door2_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door3_morning_idle.png"


    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit == 1 and ml_can_salon_morning_scene2 == True:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"

    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit > 1 and ml_can_salon_morning_scene2 == True:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"

    if ml_morning_salon_scene_active == True and  ml_salon_morning_visit > 3 and ml_can_salon_morning_scene2 == True:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"

    if ml_salon_morning_visit == 4 and ml_can_salon_morning_scene == False:
        imagebutton:
            xpos 270
            ypos 454
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/ML_b1.png"

    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/morning/Money Salon Morning.png"

    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"