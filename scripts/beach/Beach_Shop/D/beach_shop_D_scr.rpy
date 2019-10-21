screen beach_shop_D_scr:
    add "images/Beach/Beach_Shop/M/map.jpg"

    imagebutton:
        xpos 635
        ypos 0
        focus_mask True
        idle "images/Beach/Beach_Shop/M/B1.png"
        hover "images/Beach/Beach_Shop/M/B1_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("b_shop_inside")]
            hovered Show("displayTextScreen", displayText = __("Beach Shop"))
            unhovered Hide("displayTextScreen")

    if not "img38_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1337
                ypos 561
                focus_mask True
                idle "images/secret_gallery/Bonus/B38a.png"
                hover "images/secret_gallery/Bonus/B38a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img38_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1337
                ypos 561
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img38_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    imagebutton:
        at map_arrow_anim
        xpos 1710
        ypos 880
        focus_mask True
        idle Transform("images/game_gui/map_arrow.png", rotate = 215)
        hover Transform("images/game_gui/map_arrow_hover.png", rotate = 215)
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("beach3_M1")]
            unhovered Hide("displayTextScreen")
