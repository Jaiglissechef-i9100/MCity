label beach_up_M1:

    $ in_map = False

    if day_time == 1:
        jump beach_up_M2

    if day_time == 2:
        jump beach_up_D1

    if day_time == 3:
        jump beach_up_E1

    if day_time == 4:
        jump beach_up_N1

label beach_up_M2:
    hide screen displayTextScreen
    hide screen map

    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen beach_up_M_scr

