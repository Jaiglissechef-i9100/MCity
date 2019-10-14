image a_home_outside_bg_D = "/images/a_home/outside/Entrance/M/1.jpg"
image a_home_outside_bg2_D = "/images/a_home/outside/Entrance/M/2.jpg"

label a_home_outside_D1:
    hide screen displayTextScreen
    hide screen map
    if a_pool_empty == True:
        scene a_home_outside_bg_D
    else:
        scene a_home_outside_bg2_D

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
    call screen a_home_outside_D_scr
