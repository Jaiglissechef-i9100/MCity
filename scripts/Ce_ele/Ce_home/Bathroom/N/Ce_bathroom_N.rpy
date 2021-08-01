image Ce_bathroom_bg_N = "/images/Ce_ele/Ce_home/Bathroom/N/1.jpg"

label Ce_bathroom_N1:
    hide screen displayTextScreen
    hide screen map

    scene Ce_bathroom_bg_N
    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_bathroom_N_scr

