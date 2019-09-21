label classroom2_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump classroom2_morning2
    if day_time == 2:
        jump classroom2_day1

label classroom2_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene classroom2_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen classroom2_morning_notclickable
    call screen classroom2_morning
