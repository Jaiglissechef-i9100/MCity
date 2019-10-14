image charles_outside_bg_M = "/images/charles_home/outside/M/1.jpg"
image charles_outside_bg2_M = "/images/charles_home/outside/M/2.jpg"

default Charles_end = False
label charles_outside_M1:
    $ in_map = False

    if day_time == 1:
        jump charles_outside_M2

    if day_time == 2:
        jump charles_outside_D1

    if day_time == 3:
        jump charles_outside_E1

    if day_time == 4:
        jump charles_outside_N1

label charles_outside_M2:
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
    call screen Charles_outside_M_scr