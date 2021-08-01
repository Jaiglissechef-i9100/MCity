screen beach3_D_scr:

    add "images/Beach/Beach3/M/map.jpg"

    imagebutton:
        at map_arrow_anim
        xpos 1720
        ypos 830
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 195)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 195)
        if clickable == True:
            action Jump("beach2_M1")
            unhovered Hide("displayTextScreen")

    imagebutton:

        xpos 0
        ypos 332
        focus_mask True
        idle "images/Beach/Beach3/M/B_house.png"
        hover "images/Beach/Beach3/M/B_house_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("beach_shop_M1")]
            hovered Show("displayTextScreen", displayText = __("Beach Shop"))
            unhovered Hide("displayTextScreen")

    imagebutton:
        at map_arrow_anim
        xpos 20
        ypos 830
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 20)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 20)
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("b_house_living_M1")]
            hovered Show("displayTextScreen", displayText = __("Beach House"))
            unhovered Hide("displayTextScreen")

