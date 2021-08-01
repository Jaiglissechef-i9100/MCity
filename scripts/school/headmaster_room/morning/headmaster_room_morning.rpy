label headmaster_room_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump headmaster_room_morning2
    if day_time == 2:
        jump headmaster_room_day1

label headmaster_room_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene headmaster_room_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen headmaster_room_morning

