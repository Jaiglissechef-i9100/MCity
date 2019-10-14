image nc_sexroom_bg = "images/Nightclub/S_room/1.jpg"


label nc_sexroom_N:
    scene nc_sexroom_bg


    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1

    call screen nc_sexroom_N_scr

label sexroom_locked:

    hide screen map_button
    show screen nightclub_corridor_scr
    $ clickable = False
    MC "I need a key."
    $ clickable = True
    hide screen nightclub_corridor_scr
    jump nc_corridor_N