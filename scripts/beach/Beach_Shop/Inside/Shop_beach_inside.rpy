image items_map = "images/Beach/Beach_Shop/M/1a.jpg"
default beach_buy_B2 = False
default beach_buy_B3 = False
default beach_buy_B4 = False
label b_shop_inside:

    $ in_map = False

    if day_time == 1:
        jump beach_shop_items

    if day_time == 2:
        jump beach_shop_items
    else:

        $ clickable = False
        if day_time == 3:
            show screen beach_shop_E_scr

        if day_time == 4:
            show screen beach_shop_N_scr

        MC "It's closed now."
        $ clickable = True
        hide screen beach_shop_E_scr
        hide screen beach_shop_N_scr
        jump beach_shop_M1

label beach_shop_items:
    hide screen map_button
    scene items_map
    call screen beach_shop_items_scr

screen beach_shop_items_scr:
    vbox xpos 1070 ypos 700 spacing 20:
        frame:
            style "frame_gui1"
            text "$"+str(inventory.money) size 30

    if beach_buy_B2 == False:
        imagebutton:
            xpos 686
            ypos 224
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B2.png"
            hover "images/Beach/Beach_Shop/M/B2_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("beach_buy_B2")]
            hovered Show("displayTextScreen", displayText = __("Drink"))
            unhovered Hide("displayTextScreen")

    if beach_buy_B3 == False:
        imagebutton:
            xpos 936
            ypos 443
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B3.png"
            hover "images/Beach/Beach_Shop/M/B3_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("beach_buy_B3")]
            hovered Show("displayTextScreen", displayText = __("Ice Creams"))
            unhovered Hide("displayTextScreen")

    if beach_buy_B4 == False:
        imagebutton:
            xpos 1099
            ypos 246
            focus_mask True
            idle "images/Beach/Beach_Shop/M/B4.png"
            hover "images/Beach/Beach_Shop/M/B4_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("beach_buy_B4")]
            hovered Show("displayTextScreen", displayText = __("SunScreen"))
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1220
        ypos 160
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("beach_shop_M1")]
        hovered Show("displayTextScreen", displayText = __("Close"))
        unhovered Hide("displayTextScreen")

label beach_buy_B2:
    show screen beach_shop_items_scr
    $ clickable = False

    if inventory.money >= 10:
        $ inventory.buy(drink)
        $ beach_buy_B2 = True
        $ clickable = True
        jump beach_shop_items
    else:

        MC "I don't have enough money."
        $ clickable = True
        jump beach_shop_items

label beach_buy_B3:
    show screen beach_shop_items_scr
    $ clickable = False

    if inventory.money >= 8:
        $ inventory.buy(icecream)
        $ beach_buy_B3 = True
        $ clickable = True
        jump beach_shop_items
    else:

        MC "I don't have enough money."
        $ clickable = True
        jump beach_shop_items

label beach_buy_B4:
    show screen beach_shop_items_scr
    $ clickable = False
    if inventory.money >= 20:
        $ inventory.buy(sunscreen)
        $ beach_buy_B4 = True
        $ clickable = True
        jump beach_shop_items
    else:

        MC "I don't have enough money."
        $ clickable = True
        jump beach_shop_items
