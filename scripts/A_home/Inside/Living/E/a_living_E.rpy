image a_living_bg_E = "/images/a_home/Inside/Living/E/1.jpg"

label a_living_E1:
    hide screen displayTextScreen
    if not Li_key1 in inventory.items:
        hide screen map_button
        $ clickable = False
        show screen a_home_outside_E_scr
        MC "It's locked."
        $ clickable = True
        jump a_home_outside_M1
    scene a_living_bg_E
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_living_E_scr

