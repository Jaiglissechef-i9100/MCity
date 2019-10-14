screen cloth_shop_open_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 768
        ypos 207
        focus_mask True
        idle "images/cloth_shop/room1/day/door_b1.png"
        hover "images/cloth_shop/room1/day/door_b1_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("cloth_shop_room2_label")]
            hovered Show("displayTextScreen", displayText = "Door")
            unhovered Hide("displayTextScreen")
    if cloth_shop_minigame_unlocked == True and Caroline_points == 1:
        imagebutton:
            xpos 1061
            ypos 254
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1.png"
            hover "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("caroline_cloth_shop_afternoon_scene1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")
    if Caroline_points == 2 and CR2_before_robber == True and cloth_shop_minigame_unlocked == True:
        imagebutton:
            xpos 1061
            ypos 254
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1.png"
            hover "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR2_minigame_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"), Hide("cloth_shop_open_screen"), Hide("map_button"), Jump("map_label")]
            unhovered Hide("displayTextScreen")



screen cloth_shop_open_screen_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 768
        ypos 207
        focus_mask True
        idle "images/cloth_shop/room1/day/door_b1.png"
        hover "images/cloth_shop/room1/day/door_b1_hover.png"

    if cloth_shop_minigame_unlocked == True and Caroline_points <= 2:
        imagebutton:
            xpos 1061
            ypos 254
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1.png"
            hover "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/caroline_b1_hover.png"










screen cloth_shop_robber_screen:
    key "hide_windows" action NullAction()

    imagebutton:
        xpos 459
        ypos 194
        focus_mask True
        idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B4.png"
        hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B4_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("cloth_shop_room2_label")]
            hovered Show("displayTextScreen", displayText = "Door")
            unhovered Hide("displayTextScreen")
    if CR2_AS3 == True:
        imagebutton:
            xpos 707
            ypos 460
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR2_AS3_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")
    if CR2_AS3a == True:
        imagebutton:
            xpos 782
            ypos 256
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/B1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR2_AS3a_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")
    if CR2_AS3_clean1 == False:
        imagebutton:
            xpos 1171
            ypos 490
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/A1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/A1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/metalic.wav"),SetVariable("CR2_AS3_clean1", True),Jump("CR2_AS3_clean_counter_label")]
    if CR2_AS3_clean1 == True:
        imagebutton:
            xpos 1172
            ypos 419
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/A2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/A2.png"


    if CR2_AS3_clean2 == False:
        imagebutton:
            xpos 937
            ypos 382
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B2_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/paper3.wav"),SetVariable("CR2_AS3_clean2", True),Jump("CR2_AS3_clean_counter_label")]
    if CR2_AS3_clean2 == True:
        imagebutton:
            xpos 1235
            ypos 109
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B3.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/B3.png"

    if CR2_AS3_clean3 == False:
        imagebutton:
            xpos 1584
            ypos 352
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/C1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/C1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/clothes.mp3"),SetVariable("CR2_AS3_clean3", True),Jump("CR2_AS3_clean_counter_label")]
    if CR2_AS3_clean3 == True:
        imagebutton:
            xpos 1581
            ypos 114
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/C2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/C2.png"

    if CR2_AS3_clean4 == False:
        imagebutton:
            xpos 0
            ypos 599
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/D1.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/D1_hover.png"
            if clickable == True and CR2_AS3_clean == True:
                action [Play ("sound", "sfx/wood1.wav"),SetVariable("CR2_AS3_clean4", True),Jump("CR2_AS3_clean_counter_label")]
    if CR2_AS3_clean4 == True:
        imagebutton:
            xpos 0
            ypos 195
            focus_mask True
            idle "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/D2.png"
            hover "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/D2.png"
    if CR2_AS3_clean_after == True and clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"), Hide("cloth_shop_open_screen"), Hide("map_button"), Jump("map_label")]
            unhovered Hide("displayTextScreen")

    if CR2_AS4 == True:
        imagebutton:
            xpos 292
            ypos 742
            focus_mask True
            idle Transform("images/cloth_shop/room1/day/scenes/CR2_AS4/B1.png", zoom=1.5)
            hover Transform("images/cloth_shop/room1/day/scenes/CR2_AS4/B1_hover.png", zoom=1.5)
            action [Hide("displayTextScreen"),Jump("CR2_AS4_label")]
            hovered Show("displayTextScreen", displayText = "Glass Bottle")
            unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_AS1 == True:
        imagebutton:
            xpos 818
            ypos 256
            focus_mask True
            idle "images/cloth_shop/room1/day/CR3_AS1_B2.png"
            hover "images/cloth_shop/room1/day/CR3_AS1_B2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS1_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_AS2 == True and CR3_AS5 == False and CR3_AS10 == False and CR3_outfit4_can == True:
        imagebutton:
            xpos 366
            ypos 253
            focus_mask True
            idle "images/cloth_shop/room1/day/CR3_AS2_B3.png"
            hover "images/cloth_shop/room1/day/CR3_AS2_B3_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS2_label")]
                hovered Show("displayTextScreen", displayText = "Caroline and Violet")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_AS5 == True:
        imagebutton:
            xpos 736
            ypos 255
            focus_mask True
            idle "images/cloth_shop/room1/day/B4.png"
            hover "images/cloth_shop/room1/day/B4_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS5_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")


    if Caroline_points == 3 and CR3_AS7 == True:
        imagebutton:
            xpos 851
            ypos 310
            focus_mask True
            idle "images/cloth_shop/room1/day/B5.png"
            hover "images/cloth_shop/room1/day/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS7_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")
    if Caroline_points == 3 and CR3_outfit4_can == False:
        imagebutton:
            xpos 851
            ypos 310
            focus_mask True
            idle "images/cloth_shop/room1/day/B5.png"
            hover "images/cloth_shop/room1/day/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS7_outfit4_lock")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")

    if Caroline_points == 3 and CR3_AS10 == True:
        imagebutton:
            xpos 851
            ypos 310
            focus_mask True
            idle "images/cloth_shop/room1/day/B5.png"
            hover "images/cloth_shop/room1/day/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CR3_AS10_label")]
                hovered Show("displayTextScreen", displayText = "Caroline")
                unhovered Hide("displayTextScreen")