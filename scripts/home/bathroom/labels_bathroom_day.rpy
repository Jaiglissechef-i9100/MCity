label bathroom_day1:
    hide screen displayTextScreen
    hide screen kitchen_day
    scene bathroom_day
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    hide screen bathroom_morning_notclickable
    hide screen bathroom_day_notclickable
    hide screen bathroom_evening_notclickable
    hide screen bathroom_night_notclickable
    show screen new_message_incoming1
    $ can_hide_windows = False
    call screen bathroom_day