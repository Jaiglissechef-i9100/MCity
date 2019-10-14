

label bob_work_outside_night1:
    hide screen displayTextScreen
    hide screen map
    scene bob_work_outside_night
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen bob_work_outside_N_scr