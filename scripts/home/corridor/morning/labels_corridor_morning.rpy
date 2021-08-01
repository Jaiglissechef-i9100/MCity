label corridor_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump corridor_morning2
    if day_time == 2:
        jump corridor_day1
    if day_time == 3:
        jump corridor_evening1
    if day_time == 4:
        jump corridor_night1

label corridor_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen entrace1_morning
    scene corridor_morning
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen corridor_morning

