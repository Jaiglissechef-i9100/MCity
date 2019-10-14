image shop_map = "images/shop/ShopMap.jpg"
image shop_shelf = "images/shop/ShopShelf.jpg"

label shop_label:
    if day_time == 1:
        hide screen map
        jump shop_open_label
    if day_time == 2:
        hide screen map
        jump shop_open_label
    else:

        show screen map
        show screen shop_closed_screen
        MC "Closed. It's open only at the morning and in the afternoon."
        jump map_label

screen shop_closed_screen():
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("shop_closed_screen"),Jump("map_label")]

label shop_open_label:
    scene shop_map
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen shop_open_screen

screen shop_open_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 534
        ypos 289
        focus_mask True
        idle "images/shop/shelf.png"
        hover "images/shop/shelf_hover.png"
        action [Hide("displayTextScreen"),Jump("shop_shelf_label")]
        hovered Show("displayTextScreen", displayText = __("Shelf"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 792
        ypos 309
        focus_mask True
        idle "images/shop/b6.png"
        hover "images/shop/b6_hover.png"
        action [Hide("displayTextScreen"),Jump("alcohol_shelf_label")]
        hovered Show("displayTextScreen", displayText = __("Alcohol Shelf"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1304
        ypos 279
        focus_mask True
        idle "images/shop/shop_door_exit.png"
        hover "images/shop/shop_door_exit_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"), Hide("shop_open_screen"), Hide("map_button"), Jump("map_label")]
        hovered Show("displayTextScreen", displayText = __("Exit"))
        unhovered Hide("displayTextScreen")

label shop_shelf_label:
    scene shop_shelf
    $ can_map = False
    hide screen shop_open_screen
    hide screen shop_shelf_screen_notclickable
    call screen shop_shelf_screen

screen shop_shelf_screen:
    key "hide_windows" action NullAction()
    if b5_web_cam_software_buy == False:
        imagebutton:
            xpos 1204
            ypos 371
            focus_mask True
            idle "images/shop/b5_web_cam_software.png"
            hover "images/shop/b5_web_cam_software_hover.png"
            action [Hide("displayTextScreen"),Jump("b5_web_cam_software_buy_label")]
    if b1_binoculars_buy == False:
        imagebutton:
            xpos 956
            ypos 347
            focus_mask True
            idle "images/shop/b1_binoculars.png"
            hover "images/shop/b1_binoculars_hover.png"
            action [Hide("displayTextScreen"),Jump("b1_binoculars_buy_label")]

    if b2_camera1_buy == False:
        imagebutton:
            xpos 372
            ypos 376
            focus_mask True
            idle "images/shop/b2_camera.png"
            hover "images/shop/b2_camera_hover.png"
            action [Hide("displayTextScreen"),Jump("b2_camera_buy_label")]

    if b3_controller_buy == False:
        imagebutton:
            xpos 628
            ypos 146
            focus_mask True
            idle "images/shop/b3_controller.png"
            hover "images/shop/b3_controller_hover.png"
            action [Hide("displayTextScreen"),Jump("b3_controller_buy_label")]

    if b4_spy_camera_buy == False:
        imagebutton:
            xpos 1228
            ypos 198
            focus_mask True
            idle "images/shop/b4_spy_camera.png"
            hover "images/shop/b4_spy_camera_hover.png"
            action [Hide("displayTextScreen"),Jump("b4_spy_camera_buy_label")]

    imagebutton:
        xpos 600
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Hide("displayTextScreen"),Hide("shop_shelf_screen"),Jump("shop_open_label")]

screen shop_shelf_screen_notclickable:
    key "hide_windows" action NullAction()
    if b5_web_cam_software_buy == False:
        imagebutton:
            xpos 1204
            ypos 371
            focus_mask True
            idle "images/shop/b5_web_cam_software.png"

    if b1_binoculars_buy == False:
        imagebutton:
            xpos 956
            ypos 347
            focus_mask True
            idle "images/shop/b1_binoculars.png"

    if b2_camera1_buy == False:
        imagebutton:
            xpos 372
            ypos 376
            focus_mask True
            idle "images/shop/b2_camera.png"

    if b3_controller_buy == False:
        imagebutton:
            xpos 628
            ypos 146
            focus_mask True
            idle "images/shop/b3_controller.png"

    if b4_spy_camera_buy == False:
        imagebutton:
            xpos 1228
            ypos 198
            focus_mask True
            idle "images/shop/b4_spy_camera.png"

label b5_web_cam_software_buy_label:
    show screen shop_shelf_screen_notclickable
    if inventory.money >= 20:
        $ inventory.buy(web_cam_cd)
        $ b5_web_cam_software_buy = True
        jump shop_shelf_label
    else:
        MC "I don't have enough money."
        jump shop_shelf_label

label b1_binoculars_buy_label:
    show screen shop_shelf_screen_notclickable
    if inventory.money >= 100:
        $ inventory.buy(binoculars)
        $ b1_binoculars_buy = True
        jump shop_shelf_label
    else:
        MC "I don't have enough money."
        jump shop_shelf_label

label b2_camera_buy_label:
    show screen shop_shelf_screen_notclickable
    if inventory.money >= 80:
        $ inventory.buy(camera1)
        $ b2_camera1_buy = True
        jump shop_shelf_label
    else:
        MC "I don't have enough money."
        jump shop_shelf_label

label b3_controller_buy_label:
    show screen shop_shelf_screen_notclickable
    if inventory.money >= 5:
        $ inventory.buy(broken_gamepad)
        $ b3_controller_buy = True
        jump shop_shelf_label
    else:
        MC "I don't have enough money."
        jump shop_shelf_label

label b4_spy_camera_buy_label:
    show screen shop_shelf_screen_notclickable
    if inventory.money >= 55:
        $ inventory.buy(camera)
        $ b4_spy_camera_buy = True
        jump shop_shelf_label
    else:
        MC "I don't have enough money."
        jump shop_shelf_label
