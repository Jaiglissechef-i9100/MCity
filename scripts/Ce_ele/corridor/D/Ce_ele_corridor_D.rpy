
label Ce_ele_corridor_D1:
    hide screen displayTextScreen
    hide screen map

    scene Ce_ele_corridor_bg_M
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_ele_corridor_D_scr

