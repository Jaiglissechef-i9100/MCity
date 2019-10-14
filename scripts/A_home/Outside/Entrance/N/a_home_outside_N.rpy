image a_home_outside_bg_N = "/images/a_home/outside/Entrance/N/1.jpg"
image a_home_outside_bg2_N = "/images/a_home/outside/Entrance/N/2.jpg"

label a_home_outside_N1:
    hide screen displayTextScreen
    hide screen map
    if LiR1_NS2_can1 == True and LiR1_NS2_can2 == True:
        $ LiR1_climbing = True
        $ LiR1_NS2 = True
    if a_pool_empty == True:
        scene a_home_outside_bg_N
    else:
        scene a_home_outside_bg2_N
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_home_outside_N_scr
