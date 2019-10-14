label entrance2_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump entrance2_morning2
    if day_time == 2:
        jump entrance2_day1
    if day_time == 3:
        jump entrance2_evening1
    if day_time == 4:
        jump entrance2_night1
label entrance2_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen entrace1_morning
    hide screen garage_morning
    $ can_map = False
    scene entrance2_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen entrance2_morning