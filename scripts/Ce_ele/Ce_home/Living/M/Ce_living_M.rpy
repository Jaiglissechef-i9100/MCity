image Ce_living_bg_M = "/images/Ce_ele/Ce_home/Living/M/1.jpg"


label Ce_living_M1:
    $ in_map = False

    if day_time == 1:
        jump Ce_living_M2

    if day_time == 2:
        jump Ce_living_D1

    if day_time == 3:
        jump Ce_living_E1

    if day_time == 4:
        jump Ce_living_N1

label Ce_living_M2:
    hide screen displayTextScreen
    hide screen map

    scene Ce_living_bg_M
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_living_M_scr

