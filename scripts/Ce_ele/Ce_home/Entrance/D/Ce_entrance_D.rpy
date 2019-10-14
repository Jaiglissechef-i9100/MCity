image Ce_entrance_bg_M = "/images/Ce_ele/Ce_home/Entrance/M/1.jpg"



label Ce_entrance_D1:
    hide screen displayTextScreen
    hide screen map

    scene Ce_entrance_bg_M
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_entrance_D_scr