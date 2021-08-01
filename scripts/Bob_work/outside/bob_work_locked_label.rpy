


label bob_work_locked_label:
    hide screen map_button
    $ clickable = False
    if day_time == 3:
        show screen bob_work_outside_E_scr
    if day_time == 4:
        show screen bob_work_outside_N_scr

    MC "Closed. Bob's Workplace is open only in the morning and afternoon."
    if day_time == 3:
        hide screen bob_work_outside_E_scr
    if day_time == 4:
        hide screen bob_work_outside_N_scr
    $ clickable = True
    jump bob_work_outside_morning1