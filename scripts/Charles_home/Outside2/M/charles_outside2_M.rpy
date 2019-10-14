image charles_outside2_bg_M = "/images/charles_home/Outside2/M/1.jpg"



label Charles_outside2_M1:
    $ in_map = False
    $ can_map = True
    if day_time == 1:
        jump charles_outside2_M2

    if day_time == 2:
        jump charles_outside2_D1

    if day_time == 3:
        jump charles_outside2_E1

    if day_time == 4:
        jump charles_outside2_N1

label charles_outside2_M2:
    hide screen displayTextScreen
    hide screen map
    scene charles_outside2_bg_M
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Charles_outside2_M_scr