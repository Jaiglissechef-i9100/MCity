image alcohol_shelf_bg = "images/shop/AlcoholShelf.jpg"

default red_wine_buy = False
default white_wine_buy = False

label alcohol_shelf_label:
    scene alcohol_shelf_bg
    $ can_map = False
    call screen alcohol_shelf_scr

screen alcohol_shelf_scr:
    key "hide_windows" action NullAction()
    if red_wine_buy == False:
        imagebutton:
            xpos 806
            ypos 423
            focus_mask True
            idle "images/shop/WineRedNormal.png"
            if clickable == True:
                hover "images/shop/WineRedHover.png"
                action [Hide("displayTextScreen"),Jump("red_wine_buy_label")]

    if white_wine_buy == False:
        imagebutton:
            xpos 537
            ypos 422
            focus_mask True
            idle "images/shop/WineWhiteNormal.png"
            if clickable == True:
                hover "images/shop/WineWhiteHover.png"
                action [Hide("displayTextScreen"),Jump("white_wine_buy_label")]

    if clickable == True:
        imagebutton:
            xpos 600
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Hide("screen alcohol_shelf_scr"),Jump("shop_open_label")]

label red_wine_buy_label:
    $ clickable = False
    show screen alcohol_shelf_scr
    if inventory.money >= 95:
        $ inventory.buy(red_wine)
        $ red_wine_buy = True
        $ clickable = True
        jump alcohol_shelf_label
    else:

        MC "I don't have enough money."
        $ clickable = True
        jump alcohol_shelf_label

label white_wine_buy_label:
    $ clickable = False
    show screen alcohol_shelf_scr
    if inventory.money >= 80:
        $ inventory.buy(white_wine)
        $ white_wine_buy = True
        $ clickable = True
        jump alcohol_shelf_label
    else:

        MC "I don't have enough money."
        $ clickable = True
        jump alcohol_shelf_label

