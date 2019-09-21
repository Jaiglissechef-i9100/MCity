label gym_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump gym_morning2
    if day_time == 2:
        jump gym_day1

label gym_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entrace_morning
    hide screen changing_room_morning
    scene gym_morning
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen gym_morning
