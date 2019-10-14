image b_house_living_N_map = "images/Beach/Beach_House/Bedroom/N/map.jpg"

label b_house_living_N1:
    scene b_house_living_N_map
    if MLR3_b_house_bag == 2:
        jump MLR3_b_house_bag2
    hide screen displayTextScreen
    hide screen map

    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen b_house_living_N_scr