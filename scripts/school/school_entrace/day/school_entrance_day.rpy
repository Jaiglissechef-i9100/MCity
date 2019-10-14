label school_entrance_day1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_outside_day
    scene school_entrance_day
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen school_entrance_day_notclickable
    call screen school_entrance_day