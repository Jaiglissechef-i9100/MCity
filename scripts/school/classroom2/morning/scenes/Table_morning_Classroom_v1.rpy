image Table_morning_Classroom_v1_desk_p1 = "images/school/classroom2/day/scenes/Table_Classroom_v1/RenPy1.png"

label Table_morning_Classroom_v1_label:

    hide screen map_button
    show screen classroom2_morning
    $ clickable = False
    if celia_school_morning_scene1bv1 == 0:
        MC "I can’t just search her desk while she’s around."
        hide screen classroom2_morning
        $ clickable = True
        jump classroom2_morning2
    else:
        MC "I can’t just search her desk while she’s around."
        hide screen classroom2_morning
        $ clickable = True
        jump classroom2_morning2