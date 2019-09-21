screen beach2_E_scr:

    add "images/Beach/Beach2/E/map.jpg"

    imagebutton:
        at map_arrow_anim
        xpos 1720
        ypos 620
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 150)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 150)
        if clickable == True:
            action Jump("beach_M1")
            unhovered Hide("displayTextScreen")
    if not "img39_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 498
            ypos 408
            focus_mask True
            idle "images/secret_gallery/Bonus/B39a.png"
            hover "images/secret_gallery/Bonus/B39a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img39_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        at map_arrow_anim
        xpos 10
        ypos 820
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 10)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 10)
        if clickable == True:
            action Jump("beach3_M1")
            unhovered Hide("displayTextScreen")
