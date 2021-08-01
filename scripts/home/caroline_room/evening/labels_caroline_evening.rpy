label caroline_room_evening1:

    hide screen displayTextScreen
    hide screen corridor_evening
    scene caroline_room_evening
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen caroline_room_evening_not_clickable
    $ can_hide_windows = False
    call screen caroline_room_evening

