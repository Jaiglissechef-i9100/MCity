label teacher_room2_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump teacher_room2_morning2
    if day_time == 2:
        jump teacher_room2_day1

label teacher_room2_morning2:
    hide screen displayTextScreen
    scene teacher_room2_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen teacher_room2_morning

