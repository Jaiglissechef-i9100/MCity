label parents_bedroom_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump parents_bedroom_morning2
    if day_time == 2:
        jump parents_bedroom_day1
    if day_time == 3:
        jump parents_bedroom_evening1
    if day_time == 4:
        jump parents_bedroom_night1

label parents_bedroom_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen salon_morning
    scene parents_bedroom_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen parents_bedroom_morning_notclickable
    call screen parents_bedroom_morning