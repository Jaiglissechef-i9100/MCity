label mc_room_morning1:
    $ can_hide_windows = False
    $ music_continue = True
    if day_time == 1:
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        jump mc_room_morning2
    if day_time == 2:
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        jump mc_room_day1
    if day_time == 3:
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        jump mc_room_evening1
    if day_time == 4:
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        if CR3_NS5 == True and Caroline_points == 3:
            $ day_time = 4
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            hide screen mc_room_night_notclickable
            hide screen mc_room_day_notclickable
            hide screen mc_room_morning_notclickable
            hide screen mc_room_evening_notclickable
            jump CR3_NS5_label
        jump mc_room_night1

label mc_room_morning2:
    $ can_hide_windows = False
    $ renpy.hide("mc_sleep_night_bed", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    $ can_map = False
    hide screen displayTextScreen
    hide screen corridor_morning
    scene mc_room_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen mc_room_night_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_day_notclickable
    hide screen mc_room_morning_notclickable
    call screen mc_room_morning
