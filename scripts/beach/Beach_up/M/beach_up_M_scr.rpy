screen beach_up_M_scr:

    add "images/Beach/Beach_Up/M/map.jpg"

    imagebutton:
        at map_arrow_anim
        xpos 960
        ypos 280
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 90, zoom = 0.7)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 90, zoom = 0.7)
        if clickable == True:
            action Jump("beach_up2_M1")
            unhovered Hide("displayTextScreen")

    imagebutton:
        at map_arrow_anim
        xpos 10
        ypos 700
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 40)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 40)
        if clickable == True:
            action Jump("beach_M1")
            unhovered Hide("displayTextScreen")
