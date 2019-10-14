transform map_arrow_anim:
    subpixel True
    on idle:
        block:
            linear 0.1 rotate 0
    on hover:

        block:
            linear 0.1 rotate 20
            linear 0.1 rotate 0
            linear 0.1 rotate -20
            linear 0.1 rotate 0
image beach1_map = "images/Beach/Beach1/M/map.jpg"
label beach_M1:
    $ can_map = True
    if MLR3_beach_event == True:
        $ can_map = False
    $ in_map = False

    if day_time == 1:
        jump beach_M2

    if day_time == 2:
        jump beach_D1

    if day_time == 3:
        jump beach_E1

    if day_time == 4:
        jump beach_N1

label beach_M2:
    hide screen displayTextScreen
    hide screen map

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen beach_M_scr
