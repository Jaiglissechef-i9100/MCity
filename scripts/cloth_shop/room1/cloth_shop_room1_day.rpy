image cloth_shop_room1 = "images/cloth_shop/room1/day/1.jpg"
image cloth_shop_empty = "images/cloth_shop/room1/day/scenes/CR2_AS3/Cleaning1/Map1.jpg"

label cloth_shop_label:
    if day_time == 2:
        jump cloth_shop_open_label
    if day_time == 4 and cloth_shop_window_unlock == True:
        jump cloth_shop_stealing_key_label
    else:

        show screen map
        show screen sex_shop_closed_screen
        MC "Closed. It's open only in the afternoon."
        jump map_label

label cloth_shop_open_label:
    if CR2_before_robber == False:
        scene cloth_shop_empty
        $ can_map = False
        if CR2_AS3 == True and CR2_AS3_firsttime == True:
            show screen cloth_shop_robber_screen
            $ clickable = False
            $ in_map = False
            $ CR2_AS3_firsttime = False
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music1", loop=True, fadein = 2)
            $ music_continue = True
            MC "Eh!? What the fuck happened in here!? "
            MC "Where’s Caroline!?"
            hide screen cloth_shop_robber_screen
            $ clickable = True
        if CR2_AS3_clean == True and CR2_AS3_clean_after == False:
            $ can_map = False
        if CR2_AS3_clean_after == True:
            $ can_map = True
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        hide screen cloth_shop_open_screen_notclickable
        call screen cloth_shop_robber_screen
    else:
        scene cloth_shop_room1
        $ can_map = True
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        hide screen cloth_shop_open_screen_notclickable
        call screen cloth_shop_open_screen
