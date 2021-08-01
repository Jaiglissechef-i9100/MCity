image a_pool_bg_M = "/images/a_home/outside/Pool/M/1.jpg"
image a_pool_bg2_M = "/images/a_home/outside/Pool/M/2.jpg"

label a_pool_M1:
    $ in_map = False
    $ from_a_pool = True

    if LiR1_MAS1 == True and day_time <=2:
        jump LiR1_MAS1_label

    if day_time == 1:
        jump a_pool_M2

    if day_time == 2:
        jump a_pool_D1

    if day_time == 3:
        jump a_pool_E1

    if day_time == 4:
        jump a_pool_N1

label a_pool_M2:
    hide screen displayTextScreen
    if a_pool_empty == True:
        scene a_pool_bg_M
    else:
        scene a_pool_bg2_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_pool_M_scr

