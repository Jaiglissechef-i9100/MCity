image charles_outside_bg_E = "/images/charles_home/outside/E/1.jpg"
image charles_outside_bg2_E = "/images/charles_home/outside/E/2.jpg"

label charles_outside_E1:
    hide screen displayTextScreen
    hide screen map
    if Charles_end == False:
        scene charles_outside_bg_E
    else:
        scene charles_outside_bg2_E
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Charles_outside_E_scr