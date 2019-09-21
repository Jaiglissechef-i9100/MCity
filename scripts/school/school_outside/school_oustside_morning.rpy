label school_outside_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump school_outside_morning2
    if day_time == 2:
        jump school_outside_day1
    if day_time == 3:
        jump school_outside_evening1
    if day_time == 4:
        jump school_outside_night1

label school_outside_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entracne_morning
    hide screen gym_morning
    hide screen map
    scene school_outside_morning
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen school_outside_morning
