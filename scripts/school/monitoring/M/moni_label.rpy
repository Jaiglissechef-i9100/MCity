image moni_bg = "/images/CeR2/monitoring/Map.jpg"
label moni_M1:
    $ can_hide_windows = False
    if day_time == 1:
        jump moni_M2
    if day_time == 2:
        jump moni_D1

label moni_M2:

    hide screen displayTextScreen
    scene moni_bg
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen moni_M_scr

