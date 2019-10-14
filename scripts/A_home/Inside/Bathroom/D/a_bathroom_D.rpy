label a_bathroom_D1:
    hide screen displayTextScreen
    scene a_bathroom_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_bathroom_D_scr
