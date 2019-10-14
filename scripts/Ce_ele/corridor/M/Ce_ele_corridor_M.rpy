image Ce_ele_corridor_bg_M = "/images/Ce_ele/Corridor/M/1.jpg"


label Ce_ele_corridor_M1:
    $ in_map = False
    $ can_map = True
    if CeR2_NS1 == 1 and Celia_points == 2 and day_time == 4:
        jump CeR2_NS1_lab
    if CeR2_NS2 == 1 and Celia_points == 2 and day_time == 4:
        jump CeR2_NS2_lab
    else:

        if day_time == 1:
            jump Ce_ele_corridor_M2

        if day_time == 2:
            jump Ce_ele_corridor_D1

        if day_time == 3:
            jump Ce_ele_corridor_E1

        if day_time == 4:
            jump Ce_ele_corridor_N1

label Ce_ele_corridor_M2:
    hide screen displayTextScreen
    hide screen map

    scene Ce_ele_corridor_bg_M



    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_ele_corridor_M_scr