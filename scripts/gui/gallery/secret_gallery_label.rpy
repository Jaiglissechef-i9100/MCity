screen card_found_alert:
    key "hide_windows" action NullAction()
    zorder 106
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/secret_gallery/Bonus/alert.png"
        hover "images/secret_gallery/Bonus/alert.png"
        action [SetVariable("clickable", True),Hide("card_found_alert")]

label garage_card:
    show screen map_button
    show screen card_found_alert with dissolve
    $ renpy.pause()
    if day_time == 1:
        hide screen card_found_alert
        jump garage_morning2
    if day_time == 2:
        hide screen card_found_alert
        jump garage_day1
    if day_time == 3:
        hide screen card_found_alert
        jump garage_evening1
    if day_time == 4:
        hide screen card_found_alert
        show screen map_button
        jump garage_night1

label garage_entrance_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen entrance2_morning
        jump entrance2_morning2
    if day_time == 2:
        show screen entrance2_day
        jump entrance2_day1
    if day_time == 3:
        show screen entrance2_evening
        jump entrance2_evening1
    if day_time == 4:
        show screen entrance2_night
        jump entrance2_night1

label home_entrance_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen entrace1_morning
        jump entrace1_morning2
    if day_time == 2:
        show screen entrace1_day
        jump entrace1_day1
    if day_time == 3:
        show screen entrace1_evening
        jump entrace1_evening1
    if day_time == 4:
        show screen entrace1_night
        jump entrace_night1

label mc_room_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen mc_room_morning
        jump mc_room_morning2
    if day_time == 2:
        show screen mc_room_day
        jump mc_room_day1
    if day_time == 3:
        show screen mc_room_evening
        jump mc_room_evening1
    if day_time == 4:
        show screen mc_room_night
        jump mc_room_night1

label sex_shop_card:
    show screen card_found_alert with dissolve
    show screen sex_shop_evening_screen
    jump sex_shop_evening_label

label exit_school_corridor_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen school_entrance_morning
        jump school_entrance_morning2
    if day_time == 2:
        show screen school_entrance_day
        jump school_entrance_day1

label school_corridor1_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen school_corridor1_morning
        jump school_corridor1_morning2
    if day_time == 2:
        show screen school_corridor1_day
        jump school_corridor1_day1

label mc_classroom_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen classroom1_morning
        jump classroom1_morning2
    if day_time == 2:
        show screen classroom1_day
        jump classroom1_day1

label school_corridor2_card:
    show screen card_found_alert with dissolve
    if day_time == 1:
        show screen school_corridor2_morning
        jump school_corridor2_morning2
    if day_time == 2:
        show screen school_corridor2_day
        jump school_corridor2_day1
label mom_office_card:
    show screen card_found_alert with dissolve
    show screen ml_work_room1_day
    jump ml_work_room1_day1

label mom_office_card2:
    show screen card_found_alert with dissolve
    show screen ml_work_room1_day
    jump ml_work_room1_day1

label img12_sec_card_label:
    show screen card_found_alert with dissolve
    show screen bob_car_scr2
    jump bob_car_label2

label img13_sec_card_label:
    if day_time == 2:
        show screen bob_entrance_D_scr
    if day_time == 1:
        show screen bob_entrance_M_scr
    show screen card_found_alert with dissolve
    jump bob_entrance_M1

label img14_sec_card_label:
    if day_time == 2:
        show screen bob_office_D_scr
    if day_time == 1:
        show screen bob_office_M_scr
    show screen card_found_alert with dissolve
    jump bob_office_M1

label img15_sec_card_label:
    if day_time == 2:
        show screen bob_office_D_scr
    if day_time == 1:
        show screen bob_office_M_scr
    show screen card_found_alert with dissolve
    jump bob_office_M1

