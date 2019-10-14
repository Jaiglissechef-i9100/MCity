screen caroline_room_morning:
    key "hide_windows" action NullAction()

    if caroline_morning_scenes_visit == 1 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 406
            ypos 374
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene1_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 2 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 406
            ypos 374
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene1_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 2 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene2_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 3 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene2_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 3 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 1005
            ypos 288
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene3_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 4 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 1005
            ypos 288
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene3_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 5 and caroline_can_room_morning_scenes == True and Caroline_points == 1:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene4_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if caroline_morning_scenes_visit == 6 and caroline_can_room_morning_scenes == False and Caroline_points == 1 and can_caroline_morning_scene4_after == True:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_morning_scene4_label")]
            hovered Show("displayTextScreen", displayText = "Caroline")
            unhovered Hide("displayTextScreen")

    if Caroline_points == 2 and CR2_MS1 == True:
        imagebutton:
            xpos 1192
            ypos 477
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/CR2_MS1/B1_R2.png"
            hover "/images/home/caroline_room/morning/scenes/CR2_MS1/B1_R2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR2_MS1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 2 and CR2_MS2 == True:
        imagebutton:
            xpos 1309
            ypos 504
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/CR2_MS2/B1.png"
            hover "/images/home/caroline_room/morning/scenes/CR2_MS2/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR2_MS2_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_morning1")]

    if Caroline_points == 3 and CR3_MS1 == True and CR3_deal_aff == True:
        imagebutton:
            xpos 1155
            ypos 369
            focus_mask True
            idle "/images/home/caroline_room/morning/CR3_B1.png"
            hover "/images/home/caroline_room/morning/CR3_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_MS1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_MS3 == True and CR3_deal_aff == False:
        imagebutton:
            xpos 1330
            ypos 547
            focus_mask True
            idle "/images/home/caroline_room/morning/CR3_B2.png"
            hover "/images/home/caroline_room/morning/CR3_B2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_MS3_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_MS3 == False  and CR3_AS7a_can1 == True:
        imagebutton:
            xpos 946
            ypos 379
            focus_mask True
            idle "/images/home/caroline_room/day/CR3_AS7a_B1.png"
            hover "/images/home/caroline_room/day/CR3_AS7a_B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS7a_label")]
                hovered Show("displayTextScreen", displayText = __("Caroline's Bed"))
                unhovered Hide("displayTextScreen")

    if Caroline_points == 4 and CR4_MS1 == True:
        imagebutton:
            xpos 411
            ypos 412
            focus_mask True
            idle "/images/home/caroline_room/morning/CR4_B3.png"
            hover "/images/home/caroline_room/morning/CR4_B3_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR4_MS1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

screen caroline_room_morning_not_clickable:
    key "hide_windows" action NullAction()

    if caroline_morning_scenes_visit == 1 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 406
            ypos 374
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 2 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 406
            ypos 374
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 2 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 3 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 3 and caroline_can_room_morning_scenes == True:
        imagebutton:
            xpos 1005
            ypos 288
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 4 and caroline_can_room_morning_scenes == False:
        imagebutton:
            xpos 1005
            ypos 288
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1.png"
            hover "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/caroline_b1_hover.png"

    if caroline_morning_scenes_visit == 5 and caroline_can_room_morning_scenes == True and Caroline_points == 1:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1.png"

    if caroline_morning_scenes_visit == 6 and caroline_can_room_morning_scenes == False and Caroline_points == 1 and can_caroline_morning_scene4_after == True:
        imagebutton:
            xpos 1148
            ypos 442
            focus_mask True
            idle "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/caroline_b1.png"

    if Caroline_points == 3 and CR3_MS1 == True and CR3_deal_aff == True:
        imagebutton:
            xpos 1155
            ypos 369
            focus_mask True
            idle "/images/home/caroline_room/morning/CR3_B1.png"

    if Caroline_points == 3 and CR3_MS3 == True and CR3_deal_aff == False:
        imagebutton:
            xpos 1330
            ypos 547
            focus_mask True
            idle "/images/home/caroline_room/morning/CR3_B2.png"

    if Caroline_points == 4 and CR4_MS1 == True:
        imagebutton:
            xpos 411
            ypos 412
            idle "/images/home/caroline_room/morning/CR4_B3.png"
