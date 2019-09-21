image a_kitchen_bg_E = "/images/a_home/Inside/kitchen/E/1.jpg"

label a_kitchen_E1:
    hide screen displayTextScreen
    scene a_kitchen_bg_E
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_kitchen_E_scr
