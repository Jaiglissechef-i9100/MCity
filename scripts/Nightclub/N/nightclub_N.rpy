
label nightclub_menu:
    if warehouse_unlocked == False:
        $ in_map = False
        if day_time == 4:
            $ clickable = True
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)
            jump nightclub_N1
        else:
            show screen map
            $ clickable = False
            MC "It's open in the night."
            jump map_label
    else:

        jump nightclub_menu2
label nightclub_menu2:
    $ in_map = False
    $ clickable = False
    show screen map
    menu:
        "Nightclub":
            if day_time == 4:
                $ clickable = True
                $ renpy.music.stop(channel="music2", fadeout=1)
                $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)
                hide screen map
                jump nightclub_N1
            else:
                show screen map

                $ clickable = True
                MC "It's open in the night."
                jump map_label
        "Warehouse":

            if day_time == 1:

                $ clickable = True
                jump CR4_warehouse
            else:
                show screen map

                $ clickable = True
                MC "I should go there at the morning."
                jump map_label
        "Back":
            $ clickable = True
            jump map_label

label nightclub_N1:
    $ music_continue = True
    $ in_map = False
    scene nc_we_map1a
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1


    call screen nightclub_scr

