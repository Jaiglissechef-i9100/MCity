image a_home_outside_bg_E = "/images/a_home/outside/Entrance/E/1.jpg"
image a_home_outside_bg2_E = "/images/a_home/outside/Entrance/E/2.jpg"

label a_home_outside_E1:
    hide screen displayTextScreen
    hide screen map
    if a_pool_empty == True:
        scene a_home_outside_bg_E
    else:
        scene a_home_outside_bg2_E

    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_home_outside_E_scr

