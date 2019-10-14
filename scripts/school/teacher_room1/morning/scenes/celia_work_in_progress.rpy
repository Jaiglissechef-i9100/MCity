image lily_work_in_progress_v1_p1 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/RenPy.png"

label celia_work_in_progress_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen teacher_room1_morning_notclickable
    $ can_hide_windows = False
    $ renpy.show("workinprogress2", layer="screens",)
    "Not available now."
    $ renpy.hide("workinprogress2", layer="screens",)
    jump teacher_room1_morning2