label corridor_night1:
    $ clickable = True
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen entrace1_night
    scene corridor_night
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen corridor_night_notclickable
    call screen corridor_night