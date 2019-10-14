image cloth_shop_room2 = "images/cloth_shop/room2/day/2.jpg"
image cloth_shop_empty2 = "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning2/Map2.jpg"

label cloth_shop_room2_label:
    if CR2_before_robber == False:
        scene cloth_shop_empty2
        if CR2_AS3_clean_after == True:
            scene cloth_shop_room2
        $ can_map = False
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        hide screen cloth_shop_room2_screen_notclickable
        $ can_hide_windows = False
        call screen cloth_shop_room2_robbery_screen
    else:

        scene cloth_shop_room2
        $ can_map = False
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        hide screen cloth_shop_room2_screen_notclickable
        $ can_hide_windows = False
        call screen cloth_shop_room2_screen