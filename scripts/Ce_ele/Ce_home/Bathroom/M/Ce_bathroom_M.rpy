image Ce_bathroom_bg_M = "/images/Ce_ele/Ce_home/Bathroom/M/1.jpg"


label Ce_bathroom_M1:
    $ in_map = False

    if day_time == 1:
        jump Ce_bathroom_M2

    if day_time == 2:
        jump Ce_bathroom_D1

    if day_time == 3:
        jump Ce_bathroom_E1

    if day_time == 4:
        jump Ce_bathroom_N1

label Ce_bathroom_M2:
    hide screen displayTextScreen
    hide screen map

    scene Ce_bathroom_bg_M
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_bathroom_M_scr