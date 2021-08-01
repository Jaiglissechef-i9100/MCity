label charles_outside_D1:
    hide screen displayTextScreen
    hide screen map
    if Charles_end == False:
        scene charles_outside_bg_M
    else:
        scene charles_outside_bg2_M
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Charles_outside_D_scr

