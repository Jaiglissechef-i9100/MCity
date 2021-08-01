label turn_off_label:

    if day_time == 1:
        jump mc_room_morning2
    if day_time == 2:
        jump mc_room_day1
    if day_time == 3:
        jump mc_room_evening1
    if day_time == 4:
        jump mc_room_night1

