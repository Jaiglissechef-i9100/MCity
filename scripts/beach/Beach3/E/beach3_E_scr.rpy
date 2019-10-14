screen beach3_E_scr:

    add "images/Beach/Beach3/E/map.jpg"

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
        idle "images/Beach/Beach3/E/B_house.png"
        hover "images/Beach/Beach3/E/B_house_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("beach_shop_M1")]
            hovered Show("displayTextScreen", displayText = __("Beach Shop"))
            unhovered Hide("displayTextScreen")
