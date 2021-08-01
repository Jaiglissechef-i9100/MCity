screen beach_M_scr:

    add "images/Beach/Beach1/M/map.jpg"

    if clickable == True:
        imagebutton:
            at map_arrow_anim
            xpos 10
            ypos 700
            focus_mask True
            idle Transform("images/game_gui/map_arrow.png", rotate = 40)
            hover Transform("images/game_gui/map_arrow_hover.png", rotate = 40)

            action Jump("beach2_M1")
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            at map_arrow_anim
            xpos 800
            ypos 150
            focus_mask True
            idle Transform("images/game_gui/map_arrow.png", rotate = 90, zoom = 0.7)
            hover Transform("images/game_gui/map_arrow_hover.png", rotate = 90, zoom = 0.7)

            action Jump("beach_up_M1")
            unhovered Hide("displayTextScreen")

    if MLR3_beach_done > 1 and MLR3_beach_event == True:
        add "images/Beach/MLR3_beach_event/B3.png" xpos 1409 ypos 770
        imagebutton:
            xpos 744
            ypos 705
            focus_mask True
            idle "images/Beach/MLR3_beach_event/B1.png"
            hover "images/Beach/MLR3_beach_event/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_event3")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")
    if MLR3_beach_done < 2 and MLR3_beach_event == True:

        add "images/Beach/MLR3_beach_event/B2.png" xpos 745 ypos 769

    if beach_money == True and MLR3_beach_event == True:
        imagebutton:
            xpos 1409
            ypos 770
            focus_mask True
            idle "images/Beach/MLR3_beach_event/B3.png"
            hover "images/Beach/MLR3_beach_event/B3_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_money")]
                hovered Show("displayTextScreen", displayText = __("Bag"))
            unhovered Hide("displayTextScreen")

