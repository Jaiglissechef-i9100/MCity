label kitchen_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump kitchen_morning2
    if day_time == 2:
        jump kitchen_day1
    if day_time == 3:
        jump kitchen_evening1
    if day_time == 4:
        jump kitchen_night1

label kitchen_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen salon_morning
    hide screen entrance2_morning
    scene kitchen_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen kitchen_morning_notclickable
    call screen kitchen_morning
