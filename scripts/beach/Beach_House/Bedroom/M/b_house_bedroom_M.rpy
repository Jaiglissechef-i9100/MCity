

label b_house_bedroom_M1:

    $ in_map = False

    if day_time == 1:
        jump b_house_bedroom_M2

    if day_time == 4:
        jump b_house_bedroom_N1

label b_house_bedroom_M2:
    hide screen displayTextScreen
    hide screen map

    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen b_house_bedroom_M_scr