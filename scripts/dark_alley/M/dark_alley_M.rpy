image dark_alley_Mbg = "/images/dark_alley/M/1.jpg"
image dark_alley_Ebg = "/images/dark_alley/E/1.jpg"
image dark_alley_Nbg = "/images/dark_alley/N/1.jpg"
label dark_alley_label:

    if day_time == 1:
        jump dark_alley_M2
    if day_time == 2:
        jump dark_alley_D1
    if day_time == 3:
        jump dark_alley_E1
    if day_time == 4:
        jump dark_alley_N1

label dark_alley_M2:
    hide screen displayTextScreen
    scene dark_alley_Mbg
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    $ can_hide_windows = False
    call screen dark_alley_M_scr
