default in_Ne_home = False
label Ne_Corridor_M1:



    $ in_map = False
    $ can_map = False
    if in_Ne_home == True:
        if day_time == 1:
            jump Ne_Corridor_M2

        if day_time == 2:
            jump Ne_Corridor_D1

        if day_time == 3:
            jump Ne_Corridor_E1

        if day_time == 4:
            jump Ne_Corridor_N1
    if Ne_locked == True:
        if Ne_MS1 >= 1 and day_time == 1:
            jump Ne_MS1_lab
        if Ne_ES2 == True and day_time == 3:
            jump NE_ES2_lab
        else:

            if day_time == 1:
                show screen Ne_entrance_M_scr
            if day_time == 2:
                show screen Ne_entrance_D_scr
            if day_time == 3:
                show screen Ne_entrance_E_scr
            if day_time == 4:
                show screen Ne_entrance_N_scr
            $ clickable = False
            MC "It's locked."
            $ clickable = True
            hide screen Ne_entrance_M_scr
            hide screen Ne_entrance_D_scr
            hide screen Ne_entrance_E_scr
            hide screen Ne_entrance_N_scr
            $ clickable = True
            jump Ne_entrance_M1
    else:

        if day_time == 1:
            jump Ne_Corridor_M2

        if day_time == 2:
            jump Ne_Corridor_D1

        if day_time == 3:
            jump Ne_Corridor_E1

        if day_time == 4:
            jump Ne_Corridor_N1

label Ne_Corridor_M2:
    hide screen displayTextScreen
    hide screen map

    scene black



    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Ne_corridor_M_scr