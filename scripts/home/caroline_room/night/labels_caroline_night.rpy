label caroline_room_night1:

    hide screen displayTextScreen
    hide screen corridor_night
    scene caroline_room_night
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen caroline_room_night_notclickable
    if caroline_spare_key in inventory.items:
        $ selected = False
        $ inventory.drop(caroline_spare_key)
        $ active_item = None
    $ can_hide_windows = False
    call screen caroline_room_night

