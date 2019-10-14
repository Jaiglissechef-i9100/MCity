image b_house_living_M_map = "images/Beach/Beach_House/Living/M/map.jpg"

label b_house_living_M1:
    if MLR3_b_house_wait == 3:
        jump MLR3_b_house_Bed
    $ in_map = False

    if day_time == 1:
        jump b_house_living_M2

    if day_time == 4:
        jump b_house_living_N1

label b_house_living_M2:
    hide screen displayTextScreen
    hide screen map
    scene b_house_living_M_map
    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen b_house_living_M_scr
