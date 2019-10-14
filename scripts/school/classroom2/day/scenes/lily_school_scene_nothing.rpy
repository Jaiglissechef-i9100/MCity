label lily_school_scene_nothing_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    hide screen classroom2_day
    show screen classroom2_day_notclickable
    $ can_hide_windows = False
    Lily "Not now, [player_name]."
    jump classroom2_morning1
