image a_living_bg_M = "/images/a_home/Inside/Living/M/1.jpg"
default Li_key_first_time = True

label a_living_M1:

    if Li_door_locked == True:
        $ clickable = False
        hide screen map_button
        if day_time == 1:
            show screen a_home_outside_M_scr
        if day_time == 2:
            show screen a_home_outside_D_scr
        if day_time == 3:
            show screen a_home_outside_E_scr
        if day_time == 4:
            show screen a_home_outside_N_scr
        if LiR1_MAS2 == True:
            MC "It's locked."
        else:
            MC "It's locked. Maybe, I should look for someone around?"

        $ clickable = True
        hide screen a_home_outside_M_scr
        hide screen a_home_outside_D_scr
        hide screen a_home_outside_E_scr
        hide screen a_home_outside_N_scr
        jump a_home_outside_M1

    if LiR1_MAS1a == True and day_time <=2:
        jump LiR1_MAS1a_label

    if LiR1_MAS4 == True and day_time <=2:
        jump LiR1_MAS4_label

    if day_time == 1:
        jump a_living_M2

    if day_time == 2:
        jump a_living_D1

    if day_time == 3:
        jump a_living_E1

    if day_time == 4:

        jump a_living_N1

label a_living_M2:
    hide screen displayTextScreen
    scene a_living_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_living_M_scr

label a_living_M1_locked:
    hide screen map_button
    if LiR1_NS3 == True and Li_key1 in inventory.items:
        $ clickable = False
        if Li_key_first_time == True:
            show screen a_home_outside_N_scr
            MC "(Okay, here goes nothing… Let’s hope this spare key works…)"
            hide screen a_home_outside_N_scr
            $ Li_key_first_time = False
        scene black
        $ renpy.sound.play("sfx/door_squeak.mp3")
        "*Creeeaaak*"
        $ renpy.pause(0.14, hard = True)

        MC "(Perfect!)"
        MC "(The hinges are a little loud - but at least I’m in now.)"
        $ clickable = True
        jump a_living_N1
    else:

        $ clickable = False
        show screen a_home_outside_N_scr
        MC "It's locked. I need a key to go inside."
        $ clickable = True
        jump a_home_outside_M1

