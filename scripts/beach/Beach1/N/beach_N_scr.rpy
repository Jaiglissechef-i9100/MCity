screen beach_N_scr:
    add "images/Beach/Beach1/N/map.jpg"

    imagebutton:
        at map_arrow_anim
        xpos 10
        ypos 700
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 40)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 40)
        if clickable == True:
            action Jump("beach2_M1")
            unhovered Hide("displayTextScreen")

    imagebutton:
        at map_arrow_anim
        xpos 800
        ypos 150
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 90, zoom = 0.7)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 90, zoom = 0.7)
        if clickable == True:
            action Jump("beach_up_M1")
            unhovered Hide("displayTextScreen")
