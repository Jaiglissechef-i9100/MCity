screen kitchen_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door1_morning_idle.png"
        hover "images/home/kitchen/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Living Room"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_morning1")]
        unhovered Hide("displayTextScreen")
    if salon_ml_first_visit == False and SR3_we_bath == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door1_morning_idle.png"
            hover "images/home/kitchen/morning/door1_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Living Room"))
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ML_morning_scene0_v1_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door2_morning_idle.png"
        hover "images/home/kitchen/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Entrance"))
        if clickable == True:
            if SR3_we_bath == True:
                action [Hide("displayTextScreen"),Jump("SR3_bath_time_kitchen")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_morning1")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door3_morning_idle.png"
        hover "images/home/kitchen/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Bathroom"))
        if clickable == True:
            if SR3_we_bath == True:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("SR3_we_bath")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_morning1")]
        unhovered Hide("displayTextScreen")

    if sis_nerdy_scene4_v1 == 1 and Sara_points == 1:

        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"
            hover "images/home/kitchen/morning/door3_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Bathroom"))
            action [Hide("displayTextScreen"),Jump("sister_nerdy_scene4_v11")]
            unhovered Hide("displayTextScreen")

        if not camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"
                hover "images/home/kitchen/morning/door3_morning_hover.png"
                hovered Show("displayTextScreen", displayText = __("Bathroom"))
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("sister_nerdy_scene4_v1_l_door_locked")]
                unhovered Hide("displayTextScreen")

    if can_toilet_after_sara_scene4_1 == False and Sara_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"
            hover "images/home/kitchen/morning/door3_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Bathroom"))
            action [Hide("displayTextScreen"),Jump("sister_nerdy_scene4_v1_l_door_locked")]
            unhovered Hide("displayTextScreen")

    if SR2_bath == True and Sara_points == 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"
            hover "images/home/kitchen/morning/door3_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Bathroom"))
            action [Hide("displayTextScreen"),Jump("SR2_bath_label")]
            unhovered Hide("displayTextScreen")

    if ml_can_salon_morning_scene_dish_wash == True and ml_points == 1 and SR3_we_bath == False:
        imagebutton:
            xpos 1437
            ypos 528
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/Dishes_b1.png"
            hover "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/Dishes_b1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Wash The Dishes"))
            action [Hide("displayTextScreen"),Jump("ml_salon_morning_scene_dish_wash_label")]
            unhovered Hide("displayTextScreen")

    if ml_kitchen_morning_scene == True and  ml_can_kitchen_morning_scene4 == True and ml_points == 1 and SR3_we_bath == False:
        imagebutton:
            xpos 369
            ypos 388
            focus_mask True
            idle "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie.png"
            hover "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie_hover.png"
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom and Auntie"))
            else:
                hovered Show("displayTextScreen", displayText = __("Linda and her Friend"))
            action [Hide("displayTextScreen"),Jump("ml_kitchen_morning_scene4_V1_label")]
            unhovered Hide("displayTextScreen")

    if ml_salon_morning_visit == 5 and ml_can_bedroom_morning_scene5 == False and ml_points == 1 and SR3_we_bath == False:
        imagebutton:
            xpos 369
            ypos 388
            focus_mask True
            idle "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie.png"
            hover "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie_hover.png"
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom and Auntie"))
            else:
                hovered Show("displayTextScreen", displayText = __("Linda and her Friend"))
            action [Hide("displayTextScreen"),Jump("ml_kitchen_morning_scene4_V1_label")]
            unhovered Hide("displayTextScreen")

screen kitchen_morning_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door1_morning_idle.png"

    if salon_ml_first_visit == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door1_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door2_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door3_morning_idle.png"

    if sis_nerdy_scene4_v1 == 1 and Sara_points == 1:

        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"
            hover "images/home/kitchen/morning/door3_morning_hover.png"

        if not camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"

    if can_toilet_after_sara_scene4_1 == False and Sara_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"

    if SR2_bath == True and Sara_points == 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/morning/door3_morning_idle.png"

    if ml_can_salon_morning_scene_dish_wash == True and ml_points == 1:
        imagebutton:
            xpos 1437
            ypos 528
            focus_mask True
            idle "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/Dishes_b1.png"

    if ml_kitchen_morning_scene == True and  ml_can_kitchen_morning_scene4 == True and ml_points == 1:
        imagebutton:
            xpos 369
            ypos 388
            focus_mask True
            idle "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie.png"

    if ml_salon_morning_visit == 5 and ml_can_bedroom_morning_scene5 == False and ml_points == 1:
        imagebutton:
            xpos 369
            ypos 388
            focus_mask True
            idle "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/Mom_Auntie.png"

