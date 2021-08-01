label beach2_M1:
    $ can_map = True
    if MLR3_beach_event == True:
        $ can_map = False

    $ in_map = False


    if day_time == 1:
        jump beach2_M2

    if day_time == 2:
        jump beach2_D1

    if day_time == 3:
        jump beach2_E1

    if day_time == 4:
        jump beach2_N1

label beach2_M2:
    hide screen displayTextScreen
    hide screen map

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen beach2_M_scr

