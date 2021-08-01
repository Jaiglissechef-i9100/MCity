label toilets_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump toilets_morning2
    if day_time == 2:
        jump toilets_day1

label toilets_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene toilets_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen toilets_morning

