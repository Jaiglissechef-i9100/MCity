image cloth_shop_room3 = "images/cloth_shop/room3/day/3.jpg"

label cloth_shop_room3_label:
    scene cloth_shop_room3
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    $ can_hide_windows = False
    call screen cloth_shop_room3_screen
