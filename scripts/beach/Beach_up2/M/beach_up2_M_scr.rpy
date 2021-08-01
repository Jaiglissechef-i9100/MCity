screen beach_up2_M_scr:

    add "images/Beach/Beach_Up2/M/map.jpg"

    imagebutton:
        at map_arrow_anim
        xpos 980
        ypos 900
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = -90)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = -90)
        if clickable == True:
            action Jump("beach_up_M1")
            unhovered Hide("displayTextScreen")

    if MLR3_beach_cliff == True and beach_buy_B2_talk == False:
        imagebutton:
            xpos 780
            ypos 600
            focus_mask True
            idle "images/game_gui/C_jump.png"
            hover "images/game_gui/C_jump_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_cliff")]
                hovered Show("displayTextScreen", displayText = __("Jump From The Cliff"))
                unhovered Hide("displayTextScreen")

