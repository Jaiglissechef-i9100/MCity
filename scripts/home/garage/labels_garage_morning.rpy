label garage_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump garage_morning2
    if day_time == 2:
        jump garage_day1
    if day_time == 3:
        jump garage_evening1
    if day_time == 4:
        jump garage_night1

label garage_morning2:
    $ can_hide_windows = False
    $ can_map = False
    hide screen displayTextScreen
    hide screen entrance2_morning
    scene garage_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen garage_morning
