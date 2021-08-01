image bob_work_outside_morning = "/images/Bob_work/outside/D/outside_day.jpg"
image bob_work_outside_day = "/images/Bob_work/outside/D/outside_day.jpg"
image bob_work_outside_evening = "/images/Bob_work/outside/E/outside_evening.jpg"
image bob_work_outside_night = "/images/Bob_work/outside/N/outside_night.jpg"


label bob_work_outside_morning1:
    $ in_map = False
    if day_time == 1:
        jump bob_work_outside_morning2
    if day_time == 2:
        jump bob_work_outside_day1
    if day_time == 3:
        jump bob_work_outside_evening1
    if day_time == 4:
        jump bob_work_outside_night1

label bob_work_outside_morning2:
    hide screen displayTextScreen
    hide screen map
    scene bob_work_outside_morning
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen bob_work_outside_M_scr



label leave_cant:

    $ clickable = False
    if day_time == 1:
        show  screen bob_work_outside_M_scr
    if day_time == 2:
        show  screen bob_work_outside_D_scr
    MC "Before I leave, I should put the car keys back."
    $ clickable = True
    jump bob_work_outside_morning1