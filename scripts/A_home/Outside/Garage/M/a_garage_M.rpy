image a_garage_bg_M = "/images/a_home/outside/Garage/M/1.jpg"



label a_garage_M1:
    $ in_map = False

    if day_time == 1:
        jump a_garage_M2

    if day_time == 2:
        jump a_garage_D1

    if day_time == 3:
        jump a_garage_E1

    if day_time == 4:
        jump a_garage_N1

label a_garage_M2:
    hide screen displayTextScreen
    scene a_garage_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_garage_M_scr