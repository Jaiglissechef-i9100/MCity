label gym_day1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entrace_day
    hide screen changing_room_day
    scene gym_day
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen gym_day
