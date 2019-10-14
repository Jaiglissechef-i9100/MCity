image lily_work_in_progress_v1_p1 = "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/renpy.png"
label lily_work_in_progress_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen classroom2_day_notclickable
    $ can_hide_windows = False
    $ renpy.show("workinprogress2", layer="screens",)
    "Not available now."
    $ renpy.hide("workinprogress2", layer="screens",)
    jump classroom2_day1