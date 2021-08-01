label salon_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump salon_morning2
    if day_time == 2:
        jump salon_day1
    if day_time == 3:
        jump salon_evening1
    if day_time == 4:
        jump salon_night1

label salon_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen corridor_morning
    scene salon_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen salon_morning_notclickable
    call screen salon_morning