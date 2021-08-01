image a_kitchen_bg_M = "/images/a_home/Inside/Kitchen/M/1.jpg"

label a_kitchen_M1:
    if LiR1_MAS5 == True and day_time <3:
        jump LiR1_MAS5_label
    if day_time == 1:
        jump a_kitchen_M2

    if day_time == 2:
        jump a_kitchen_D1

    if day_time == 3:
        jump a_kitchen_E1

    if day_time == 4:
        jump a_kitchen_N1

label a_kitchen_M2:
    hide screen displayTextScreen
    scene a_kitchen_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_kitchen_M_scr

