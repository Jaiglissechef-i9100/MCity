image nc_corridor_bg = "images/Nightclub/Corridor/1.jpg"
image nc_corridor_bg = "images/Nightclub/Corridor/2.jpg"

label nc_corridor_N:
    scene nc_corridor_bg

    $ in_map = False
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1

    call screen nightclub_corridor_scr

