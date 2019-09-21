image a_living_bg_N = "/images/a_home/Inside/Living/N/1.jpg"

label a_living_N1:
    hide screen displayTextScreen
    scene a_living_bg_N
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_living_N_scr
