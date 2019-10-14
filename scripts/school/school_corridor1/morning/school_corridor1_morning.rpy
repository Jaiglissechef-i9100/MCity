label school_corridor1_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump school_corridor1_morning2
    if day_time == 2:
        jump school_corridor1_day1

label school_corridor1_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entrance_morning
    scene school_corridor1_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen school_corridor1_morning