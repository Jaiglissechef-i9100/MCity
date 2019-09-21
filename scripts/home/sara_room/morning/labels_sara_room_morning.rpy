label sister_nerdy_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump sister_nerdy_morning2
    if day_time == 2:
        jump sister_nerdy_day1
    if day_time == 3:
        jump sister_nerdy_evening1
    if day_time == 4:
        jump sister_nerdy_night1

label sister_nerdy_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen corridor_morning
    scene SisterNerdy_morning
    if drawer_sis_nerdy == 1 and can_sara_scene3_v1 == True:
        jump scene3_v1drawer
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen sister_nerdy_morning_notclickable
    hide screen sister_nerdy_day_notclickable
    hide screen sister_nerdy_night_notclikcable
    call screen sister_nerdy_morning
