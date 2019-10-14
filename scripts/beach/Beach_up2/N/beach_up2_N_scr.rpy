screen beach_up2_N_scr:

    add "images/Beach/Beach_Up2/N/map.jpg"

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
