label bathroom_night1:
    hide screen displayTextScreen
    hide screen kitchen_night
    scene bathroom_night
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    hide screen bathroom_morning_notclickable
    hide screen bathroom_day_notclickable
    hide screen bathroom_evening_notclickable
    hide screen bathroom_night_notclickable
    $ can_hide_windows = False
    call screen bathroom_night