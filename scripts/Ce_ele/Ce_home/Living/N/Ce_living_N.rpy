image Ce_living_bg_N = "/images/Ce_ele/Ce_home/Living/N/1.jpg"
image Ce_living_bg2_N = "images/CeR2/NS2/Waiting/Map.jpg"
label Ce_living_N1:
    hide screen displayTextScreen
    hide screen map
    if CeR2_NS2 >= 1:
        scene Ce_living_bg2_N
    else:
        scene Ce_living_bg_N
    $ can_map = False


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ce_living_N_scr

