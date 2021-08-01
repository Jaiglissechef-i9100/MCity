label mc_room_day1:
    $ can_hide_windows = False
    if take_nap == True:
        scene mc_room_day
        hide screen mc_room_morning_notclickable
        show screen mc_room_day_notclickable
        hide screen new_message_incoming1
        $ renpy.show("mc_sleep_morning", layer="screens")
        show screen bed_images
        MC "Time to get up!"
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ take_nap = False
        hide screen bed_images
        jump mc_room_day1
    hide screen displayTextScreen
    hide screen corridor_day
    scene mc_room_day
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen mc_room_night_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_day_notclickable
    hide screen mc_room_morning_notclickable
    call screen mc_room_day