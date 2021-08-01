label caroline_room_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump caroline_room_morning2
    if day_time == 2:
        jump caroline_room_day1
    if day_time == 3:
        jump caroline_room_evening1
    if day_time == 4:
        jump caroline_room_night1

label caroline_room_morning2:

    hide screen displayTextScreen
    hide screen corridor_morning
    scene caroline_room_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen caroline_room_morning_not_clickable
    call screen caroline_room_morning

