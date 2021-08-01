
default intercom_after_vibrator = False
label school_entrance_morning1:


    if day_time == 1:
        if celia_school_morning_scene1bv1 == 1 and can_school_intercom == True and Celia_points ==1 and intercom_after_vibrator == True:
            jump school_entrance_intercom_label
        else:
            jump school_entrance_morning2
    if day_time == 2:
        jump school_entrance_day1

label school_entrance_morning2:
    hide screen displayTextScreen
    hide screen school_outside_morning
    scene school_entrance_morning
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen school_entrance_day_notclickable
    call screen school_entrance_morning

