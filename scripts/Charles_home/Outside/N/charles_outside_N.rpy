image charles_outside_bg_N = "/images/charles_home/outside/N/1.jpg"
image charles_outside_bg2_N = "/images/charles_home/outside/N/2.jpg"

label charles_outside_N1:
    hide screen displayTextScreen
    hide screen map
    if Charles_end == False:
        scene charles_outside_bg_N
    else:
        scene charles_outside_bg2_N
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Charles_outside_N_scr