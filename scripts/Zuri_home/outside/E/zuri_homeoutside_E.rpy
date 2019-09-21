image zuri_home_Ebg1 = "/images/zuri_home/outside/E/1.jpg"
image zuri_home_Ebg2 = "/images/zuri_home/outside/E/2.jpg"
image zuri_home_Ebg3 = "/images/zuri_home/outside/E/3.jpg"

label zuri_homeoutside_E1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen map
    scene zuri_home_Ebg1
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen zuri_homeoutside_E_scr

label Z_home_door_E_label:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen map
    scene zuri_home_Ebg2
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen Z_home_door_E_scr

label Z_home_doorknock_E_label:
    $ can_hide_windows = False
    scene zuri_home_Ebg3
    show screen Z_home_door_E_scr
    if zuri_inhome == True and Z_points == 1:
        $ clickable = False
        $ renpy.sound.play("sfx/knock_knock.wav")
        Zuri "Doors are open! Come inside!"
        $ renpy.music.stop(channel="sound")
        $ clickable = True
        hide screen Z_home_door_E_scr
        jump zuri_home_E_label
    else:
        $ clickable = False
        $ renpy.sound.play("sfx/knock_knock.wav")
        MC "Hmm.. I guess there’s no one inside."
        $ renpy.music.stop(channel="sound", fadeout=1)
        $ clickable = True
        hide screen Z_home_door_E_scr
        jump Z_home_door_E_label
