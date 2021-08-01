image a_home_outside_bg_M = "/images/a_home/outside/Entrance/M/1.jpg"
image a_home_outside_bg2_M = "/images/a_home/outside/Entrance/M/2.jpg"

label a_home_outside_M1:
    $ Linda_name = Mom_name
    $ in_map = False
    $ from_a_pool = False

    if day_time == 1:
        jump a_home_outside_M2

    if day_time == 2:
        jump a_home_outside_D1

    if day_time == 3:
        jump a_home_outside_E1

    if day_time == 4:
        jump a_home_outside_N1

label a_home_outside_M2:
    hide screen displayTextScreen
    hide screen map
    if a_pool_empty == True:
        scene a_home_outside_bg_M
    else:
        scene a_home_outside_bg2_M

    $ can_map = True

    if LiR1_MAS1a == True:
        $ can_map = False


    if LiR1_MAS7 == True:
        $ can_map = False
    if LiR1_MAS9 == True:
        $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_home_outside_M_scr

