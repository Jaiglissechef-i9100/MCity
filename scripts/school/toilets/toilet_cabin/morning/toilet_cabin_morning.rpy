label toilet_cabin_morning1:

    if day_time == 1:
        jump toilet_cabin_morning2
    if day_time == 2:
        jump toilets_day1

label toilet_cabin_morning2:
    hide screen displayTextScreen
    scene toilet_cabin_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen toilet_cabin_morning
