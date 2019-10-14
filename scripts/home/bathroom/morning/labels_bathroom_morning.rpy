label bathroom_morning1:

    hide screen bathroom_morning_notclickable
    hide screen bathroom_day_notclickable
    hide screen bathroom_evening_notclickable
    hide screen bathroom_night_notclickable
    $ can_hide_windows = False
    if day_time == 1:
        jump bathroom_morning2
    if day_time == 2:
        jump bathroom_day1
    if day_time == 3:
        jump bathroom_evening1
    if day_time == 4:
        jump bathroom_night1

label bathroom_morning2:
    hide screen displayTextScreen
    hide screen kitchen_morning
    scene bathroom_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen bathroom_morning_notclickable
    hide screen bathroom_day_notclickable
    hide screen bathroom_evening_notclickable
    hide screen bathroom_night_notclickable
    $ can_hide_windows = False
    call screen bathroom_morning