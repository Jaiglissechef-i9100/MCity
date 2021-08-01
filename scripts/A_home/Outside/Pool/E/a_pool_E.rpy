image a_pool_bg_E = "/images/a_home/outside/Pool/E/1.jpg"
image a_pool_bg2_E = "/images/a_home/outside/Pool/E/2.jpg"

label a_pool_E1:
    hide screen displayTextScreen
    if a_pool_empty == True:
        scene a_pool_bg_E
    else:
        scene a_pool_bg2_E
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_pool_E_scr

