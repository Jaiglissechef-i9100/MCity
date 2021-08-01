image lily_work_in_progress_v1_p1 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/RenPy.png"

label celia_work_in_progress_v1_label:

    $ clickable = False
    hide screen map_button
    show screen teacher_room1_morning
    $ can_hide_windows = False
    Celia "Meet me at my home at night."
    hide screen teacher_room1_morning
    $ renpy.hide("workinprogress2", layer="screens",)
    $ clickable = True
    jump teacher_room1_morning2