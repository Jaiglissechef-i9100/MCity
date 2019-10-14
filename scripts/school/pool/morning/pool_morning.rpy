label pool_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump pool_morning2
    if day_time == 2:
        jump pool_day1

label pool_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene pool_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen pool_morning_notclickable
    call screen pool_morning