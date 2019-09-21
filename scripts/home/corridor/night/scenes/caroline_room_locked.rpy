label caroline_room_locked_label:
    show screen corridor_night_notclickable
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_door_locked_visit == 1:
        MC "It’s locked… I think she has a spare key somewhere!"
        $ caroline_door_locked_visit = 2
        $ caroline_can_door_locked = False
        jump corridor_night1
    if caroline_can_door_locked == False and caroline_door_locked_visit == 2:
        MC "It’s locked… I think she has a spare key somewhere!"
        jump corridor_night1
    if caroline_can_door_locked == True and caroline_door_locked_visit == 2:
        MC "It’s locked just as before! As far as I remember, she should have her spare key in the shop!"
        jump corridor_night1
