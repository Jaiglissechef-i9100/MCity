screen parents_bedroom_morning:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_morning1")]

    if ml_bedroom_morning_scene5 == True and ml_can_bedroom_morning_scene5 == True:
        imagebutton:
            xpos 30
            ypos 223
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_scene5_v1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if ml_bedroom_morning_scene6 == True:
        imagebutton:
            xpos 394
            ypos 222
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_scene6_v1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

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


    if ml_points >=2 and MLR2_MS1_active == True:
        imagebutton:
            xpos 1087
            ypos 295
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR2_MS1_label")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if ml_points == 3 and MLR3_Bob_MS1 == True:
        imagebutton:
            xpos 354
            ypos 286
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_Bob_MS1")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Dad"))
            else:
                hovered Show("displayTextScreen", displayText = "Bob")
            unhovered Hide("displayTextScreen")

    if ml_points == 3 and MLR3_Linda_MS1 == True:
        imagebutton:
            xpos 867
            ypos 398
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b2.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_Linda_MS1")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if ml_points == 3 and MLR3_MS2 == True:
        imagebutton:
            xpos 427
            ypos 206
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_MS2")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")


    if ml_points == 3 and MLR3_MS3 == True:
        imagebutton:
            xpos 1128
            ypos 549
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_MS3")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

screen parents_bedroom_morning_notclickable:

    key "hide_windows" action NullAction()
    if ml_bedroom_morning_scene5 == True and ml_can_bedroom_morning_scene5 == True and ml_bedroom_book_scene == False:
        imagebutton:
            xpos 30
            ypos 223
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1.png"

    if ml_bedroom_morning_scene6 == True:
        imagebutton:
            xpos 394
            ypos 222
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1.png"

    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/money_b1.png"
    if ml_points >=2 and MLR2_MS1_active == True:
        imagebutton:
            xpos 1087
            ypos 295
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1.png"

    if ml_points == 3 and MLR3_Bob_MS1 == True:
        imagebutton:
            xpos 354
            ypos 286
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b1.png"

    if ml_points == 3 and MLR3_Linda_MS1 == True:
        imagebutton:
            xpos 867
            ypos 398
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/b2.png"

    if ml_points == 3 and MLR3_MS2 == True:
        imagebutton:
            xpos 427
            ypos 206
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/b1.png"

    if ml_points == 3 and MLR3_MS3 == True:
        imagebutton:
            xpos 1128
            ypos 549
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/b1.png"

