image a_bedroom_bg_M = "/images/a_home/Inside/Bedroom/M/1.jpg"



label a_bedroom_M1:

    if day_time == 1:
        jump a_bedroom_M2

    if day_time == 2:
        jump a_bedroom_D1

    if day_time == 3:
        jump a_bedroom_E1

    if day_time == 4:
        jump a_bedroom_N1

label a_bedroom_M2:
    hide screen displayTextScreen
    scene a_bedroom_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_bedroom_M_scr