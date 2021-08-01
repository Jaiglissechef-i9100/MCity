label entrace1_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump entrace1_morning2
    if day_time == 2:
        jump entrace1_day1
    if day_time == 3:
        jump entrace1_evening1
    if day_time == 4:
        jump entrace_night1

label entrace1_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen corridor_morning
    hide screen map
    scene entrace1_morning
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen entrace1_morning

