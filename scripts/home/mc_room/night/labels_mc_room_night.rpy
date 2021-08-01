image ml_take_nap = "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_take_nap.png"
image window_take_nap = "images/home/mc_room/night/window_wake_up_night.png"

label mc_room_night1:
    $ can_hide_windows = False
    if take_nap == True:
        scene mc_room_night
        hide screen mc_room_evening_notclickable
        if Neighboor_spy_mc_room == True:
            $ renpy.show("window_take_nap", layer="screens")
        $ renpy.show("mc_sleep_night", layer="screens")
        if ml_mc_room_night_scene3 == True and ml_points == 1 and SR2_ML == True:
            $ renpy.show("ml_take_nap", layer="screens")
        if ml_mc_room_night_scene3 == True and ml_points == 2 and MLR2_Sleep == False:
            $ renpy.show("ml_take_nap", layer="screens")

        show screen mc_room_night_notclickable
        hide screen new_message_incoming1
        MC "Time to get up!"
        $ renpy.hide("ml_take_nap", layer="screens")
        $ renpy.hide("mc_sleep_morning", layer="screens")
        $ renpy.hide("mc_sleep_day", layer="screens")
        $ renpy.hide("mc_sleep_evening", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("window_take_nap", layer="screens")
        $ take_nap = False


        jump mc_room_night1


    hide screen displayTextScreen
    hide screen corridor_night
    scene mc_room_night
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen mc_room_night_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_day_notclickable
    hide screen mc_room_morning_notclickable
    call screen mc_room_night