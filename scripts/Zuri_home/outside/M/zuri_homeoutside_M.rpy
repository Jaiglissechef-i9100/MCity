

image zuri_home_Mbg1 = "/images/zuri_home/outside/M/1.jpg"
image zuri_home_Mbg2 = "/images/zuri_home/outside/M/2.jpg"
image zuri_home_Mbg3 = "/images/zuri_home/outside/M/3.jpg"



label zuri_homeoutside_M1:
    $ can_hide_windows = False
    if day_time == 4:
        show screen map
        show screen sex_shop_closed_screen
        MC "It’s too late."
        jump map_label
    $ in_map = False
    if day_time == 1:
        jump zuri_homeoutside_M2
    if day_time == 2:
        jump zuri_homeoutside_D1
    if day_time == 3:
        jump zuri_homeoutside_E1



label zuri_homeoutside_M2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen map
    scene zuri_home_Mbg1
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen zuri_homeoutside_M_scr



label Z_home_door_M_label:
    hide screen displayTextScreen
    hide screen map
    scene zuri_home_Mbg2
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    if day_time == 2:
        call screen Z_home_door_D_scr
    else:
        call screen Z_home_door_M_scr


label Z_home_doorlocked_M_label:
    scene zuri_home_Mbg3
    hide screen map_button
    if day_time == 2:
        show screen Z_home_door_D_scr
    else:
        show screen Z_home_door_M_scr
    scene zuri_home_Mbg3
    $ clickable = False
    $ renpy.sound.play("sfx/knock_knock.wav")
    MC "Hmm.. I guess there’s no one inside."
    $ renpy.music.stop(channel="sound", fadeout=1)
    $ clickable = True
    jump Z_home_door_M_label