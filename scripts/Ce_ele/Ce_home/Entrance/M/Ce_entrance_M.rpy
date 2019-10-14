image Ce_entrance_bg_M = "/images/Ce_ele/Ce_home/Entrance/M/1.jpg"


label Ce_entrance_M1:
    $ in_map = False



    if day_time == 1:
        jump Ce_entrance_M2

    if day_time == 2:
        jump Ce_entrance_D1

    if day_time == 3:
        jump Ce_entrance_E1

    if day_time == 4:
        jump Ce_entrance_N1

label Ce_entrance_M2:
    hide screen displayTextScreen
    hide screen map

    scene Ce_entrance_bg_M
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_entrance_M_scr

label Ce_closed:
    if day_time == 1:
        show screen Ce_ele_corridor_M_scr
    if day_time == 2:
        show screen Ce_ele_corridor_D_scr
    if day_time == 3:
        show screen Ce_ele_corridor_E_scr
    if day_time == 4:
        show screen Ce_ele_corridor_N_scr
    hide screen map
    hide screen Ce_ele_corridor_M_scr
    hide screen Ce_ele_corridor_D_scr
    hide screen Ce_ele_corridor_E_scr
    hide screen Ce_ele_corridor_N_scr
    $ clickable = False
    MC "It's locked. I need a key."
    $ clickable = True
    jump Ce_ele_corridor_M1