label a_pool_D1:
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
    call screen a_pool_D_scr
