label changing_room_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump changing_room_morning2
    if day_time == 2:
        jump changing_room_day1

label changing_room_morning2:
    hide screen displayTextScreen
    hide screen changing_room_morning
    scene changing_room_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen changing_room_morning

