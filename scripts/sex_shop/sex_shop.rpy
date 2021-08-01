image sex_shop_map = "images/sex_shop/SexShopMap.jpg"
image sex_shop_table = "images/sex_shop/SexShopTable.jpg"
image sex_shop_1 = "images/sex_shop/1.jpg"

label sex_shop_label:
    if day_time == 3:
        hide screen map
        jump sex_shop_evening_label
    else:
        if day_time == 4:
            show screen map
            show screen sex_shop_closed_screen
            MC "Closed. It's open only in the evening."
            jump map_label
        else:
            show screen map
            show screen sex_shop_closed_screen
            MC "Closed. It's open only in the evening."
            jump map_label

screen sex_shop_closed_screen:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("sex_shop_closed_screen"),Jump("map_label")]

label sex_shop_evening_label:
    scene sex_shop_map
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen sex_shop_evening_screen

screen sex_shop_evening_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1289
        ypos 250
        focus_mask True
        idle "images/sex_shop/sex_shop_lady.png"
        hover "images/sex_shop/sex_shop_lady_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("sex_shop_table_label")]
            hovered Show("displayTextScreen", displayText = __("Saleswoman"))
            unhovered Hide("displayTextScreen")

    if not "img5_sex_shop_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1674
                ypos 285
                focus_mask True
                idle "images/secret_gallery/Bonus/SexShop Card.png"
                hover "images/secret_gallery/Bonus/SexShop Card_hover.png"
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"), addgimage("img5_sex_shop_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1674
                ypos 285
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"), addgimage("img5_sex_shop_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"), Hide("sex_shop_evening_screen"), Hide("map_button"), Jump("map_label")]
            unhovered Hide("displayTextScreen")

    if SR2_AS3 == True and not SR2_vibrator in inventory.items:
        imagebutton:
            xpos 1289
            ypos 250
            focus_mask True
            idle "images/sex_shop/sex_shop_lady.png"
            hover "images/sex_shop/sex_shop_lady_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("SR2_AS3_vibrator_label")]
                hovered Show("displayTextScreen", displayText = __("Saleswoman"))
                unhovered Hide("displayTextScreen")

    if CeR2_dildo_buy >= 1:
        imagebutton:
            xpos 1289
            ypos 250
            focus_mask True
            idle "images/sex_shop/sex_shop_lady.png"
            hover "images/sex_shop/sex_shop_lady_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("CeR2_sex_shop")]
                hovered Show("displayTextScreen", displayText = __("Saleswoman"))
                unhovered Hide("displayTextScreen")

label sex_shop_table_label:
    if sex_shop_visit == 1:
        scene sex_shop_1
        S "Oh! New customer! Nice. Just look what I have for sale."
        $ sex_shop_visit = 2
        scene sex_shop_table
        call screen sex_shop_table_screen
    if sex_shop_visit == 2:
        scene sex_shop_1
        S "Welcome."
        scene sex_shop_table
        call screen sex_shop_table_screen

label sex_shop_table_label1:
    scene sex_shop_table
    call screen sex_shop_table_screen

screen sex_shop_table_screen:
    key "hide_windows" action NullAction()
    if dildo_buy == False:
        imagebutton:
            xpos 1514
            ypos 247
            focus_mask True
            idle "images/sex_shop/DildoB1.png"
            hover "images/sex_shop/DildoB1Hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("dildo_buy_label")]
                hovered Show("displayTextScreen", displayText = __("Dildo"))
                unhovered Hide("displayTextScreen")

    if sexy_cloth_buy == False:
        imagebutton:
            xpos 584
            ypos 708
            idle "images/sex_shop/SexyClothB2.png"
            hover "images/sex_shop/SexyClothB2_Hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("sexy_cloth_buy_label")]
                hovered Show("displayTextScreen", displayText = __("Sexy Cloth"))
                unhovered Hide("displayTextScreen")

    if vibrator_buy == False:
        imagebutton:
            xpos 1420
            ypos 405
            focus_mask True
            idle "images/sex_shop/VibratorB3.png"
            hover "images/sex_shop/VibratorB3_Hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("vibrator_buy_label")]
                hovered Show("displayTextScreen", displayText = __("Vibrator"))
                unhovered Hide("displayTextScreen")

    if lube_buy == False:
        imagebutton:
            xpos 200
            ypos 131
            focus_mask True
            idle "images/sex_shop/B4.png"
            hover "images/sex_shop/B4_Hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("lube_buy_label")]
                hovered Show("displayTextScreen", displayText = __("Lube"))
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 600
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Jump("sex_shop_evening_label")]

screen sex_shop_buy_screen:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("sex_shop_buy_screen"),Jump("sex_shop_table_label1")]

label dildo_buy_label:
    show screen sex_shop_table_screen
    $ clickable = False
    if inventory.money >= 25:
        $ inventory.buy(dildo)
        $ dildo_buy = True
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1
    else:
        MC "I don't have enough money."
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1

label sexy_cloth_buy_label:
    show screen sex_shop_table_screen
    $ clickable = False
    if inventory.money >= 70:
        $ inventory.buy(sexy_cloth)
        $ sexy_cloth_buy = True
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1
    else:
        MC "I don't have enough money."
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1

label vibrator_buy_label:
    show screen sex_shop_table_screen
    $ clickable = False
    if inventory.money >= 40:
        $ inventory.buy(vibrator)
        $ vibrator_buy = True
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1
    else:
        MC "I don't have enough money."
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1

label lube_buy_label:
    show screen sex_shop_table_screen
    $ clickable = False
    if inventory.money >= 50:
        $ inventory.buy(lube)
        $ lube_buy = True
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1
    else:
        MC "I don't have enough money."
        hide screen sex_shop_table_screen
        $ clickable = True
        jump sex_shop_table_label1

