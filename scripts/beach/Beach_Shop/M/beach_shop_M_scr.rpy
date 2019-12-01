image shop_M_map = "images/Beach/Beach_Shop/M/map.jpg"

screen beach_shop_M_scr:
    add "images/Beach/Beach_Shop/M/map.jpg"

    imagebutton:
        xpos 636
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

    if clickable == True:
        imagebutton:
            at map_arrow_anim
            xpos 1710
            ypos 880
            focus_mask True
            idle Transform("images/game_gui/map_arrow.png", rotate = 215)
            hover Transform("images/game_gui/map_arrow_hover.png", rotate = 215)
            action [Hide("displayTextScreen"),Jump("beach3_M1")]
            unhovered Hide("displayTextScreen")

    if MLR3_beach_drink == True and not drink in inventory.items and beach_buy_B2_talk == False:
        imagebutton:
            xpos 0
            ypos 234
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B5.png"
            hover "images/Beach/Beach_Shop/M/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_drink")]
            hovered Show("displayTextScreen", displayText = __("Propose a Drink"))
            unhovered Hide("displayTextScreen")

    if MLR3_beach_drink == True and not drink in inventory.items and beach_buy_B2_talk == True:
        imagebutton:
            xpos 0
            ypos 234
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B6.png"
            hover "images/Beach/Beach_Shop/M/B6_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_drink")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if MLR3_beach_drink == True and drink in inventory.items and beach_buy_B2_talk == True:
        imagebutton:
            xpos 0
            ypos 234
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B6.png"
            hover "images/Beach/Beach_Shop/M/B6_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_drink")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if MLR3_beach_drink == True and drink in inventory.items and beach_buy_B2_talk == False:
        imagebutton:
            xpos 0
            ypos 234
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B5.png"
            hover "images/Beach/Beach_Shop/M/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_beach_drink")]
            hovered Show("displayTextScreen", displayText = __("Propose a Drink"))
            unhovered Hide("displayTextScreen")
