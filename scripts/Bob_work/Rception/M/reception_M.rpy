image bob_reception_morning = "/images/Bob_work/reception/M/reception_M.jpg"

label bob_reception_morning1:
    if day_time == 1:
        jump bob_reception_morning2
    if day_time == 2:
        jump bob_reception_day1

label bob_reception_morning2:
    hide screen displayTextScreen

    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen bob_reception_M_scr

