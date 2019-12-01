screen parents_bedroom_day:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_day1")]

    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/money_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/money_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_money_label")]
            hovered Show("displayTextScreen", displayText = __("Money"))
            unhovered Hide("displayTextScreen")

    if d_ml_and_f_bedroom_mornig_scene == True and Bob_workplace_unlocked == False:
        imagebutton:
            xpos 420
            ypos 248
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/d_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/d_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("d_ml_and_f_bedroom_mornig_scene_v1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Dad"))
            else:
                hovered Show("displayTextScreen", displayText = "Bob")
            unhovered Hide("displayTextScreen")

    if Bob_v2_scenes == True and ml_points == 2:
        imagebutton:
            xpos 624
            ypos 429
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/Bob_V2_B1.png"
            hover "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/Bob_V2_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("B2_AS1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Dad"))
            else:
                hovered Show("displayTextScreen", displayText = "Bob")
            unhovered Hide("displayTextScreen")

    if MLR3_Bob_AS1 != 2 and MLR3_Bob_AS1 != 4 and MLR3_Bob_AS1 < 5 and ml_points == 3:
        imagebutton:
            xpos 194
            ypos 266
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B1.png"
            hover "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_Bob_AS1")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Dad"))
            else:
                hovered Show("displayTextScreen", displayText = "Bob")
            unhovered Hide("displayTextScreen")


    if MLR3_Bob_AS1 != 1 and MLR3_Bob_AS1 != 3 and ml_points == 3:
        imagebutton:
            xpos 285
            ypos 240
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B2.png"
            hover "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_Bob_AS1")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Dad"))
            else:
                hovered Show("displayTextScreen", displayText = "Bob")
            unhovered Hide("displayTextScreen")

screen parents_bedroom_day_notclickable:
    key "hide_windows" action NullAction()
    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/money_b1.png"

    if d_ml_and_f_bedroom_mornig_scene == True and Bob_workplace_unlocked == False:
        imagebutton:
            xpos 420
            ypos 248
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/d_b1.png"

    if Bob_v2_scenes == True:
        imagebutton:
            xpos 624
            ypos 429
            idle "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/Bob_V2_B1.png"

    if MLR3_Bob_AS1 != 2 and MLR3_Bob_AS1 != 4 and MLR3_Bob_AS1 < 5 and ml_points == 3:
        imagebutton:
            xpos 194
            ypos 266
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B1.png"

    if MLR3_Bob_AS1 != 1 and MLR3_Bob_AS1 != 3 and ml_points == 3:
        imagebutton:
            xpos 285
            ypos 240
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/B2.png"
