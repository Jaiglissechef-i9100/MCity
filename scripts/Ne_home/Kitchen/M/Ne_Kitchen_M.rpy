label Ne_Kitchen_M1:
    $ in_map = False
    $ can_map = False



    if day_time == 1:
        jump Ne_Kitchen_M2

    if day_time == 2:
        jump Ne_Kitchen_D1

    if day_time == 3:
        jump Ne_Kitchen_E1

    if day_time == 4:
        jump Ne_Kitchen_N1

label Ne_Kitchen_M2:
    hide screen displayTextScreen
    hide screen map

    scene black



    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ne_Kitchen_M_scr