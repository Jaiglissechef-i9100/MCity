image bob_entrance_bg = "/images/Bob_work/entrance/M/entrance.jpg"



label bob_entrance_M1:
    if day_time == 1:
        jump bob_entrance_M2
    if day_time == 2:
        jump bob_entrance_D1
    if day_time > 2:
        if day_time == 3:
            show screen bob_work_outside_E_scr

        if day_time == 4:
            show screen bob_work_outside_N_scr
        hide screen map_button
        $ can_map = False
        $ clickable = False
        MC "It's too late to enter here."
        $ clickable = True
        $ can_map = True
        jump bob_work_outside_morning1



label bob_entrance_M2:
    hide screen displayTextScreen
    scene bob_entrance_bg
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen bob_entrance_M_scr