default Ne_fence = False

label Ne_fence_lab:

    if Ne_fence == False:
        hide screen map_button
        if day_time == 1:
            show screen Ne_entrance_M_scr

        if day_time == 2:
            show screen Ne_entrance_D_scr

        if day_time == 3:
            show screen Ne_entrance_E_scr

        if day_time == 4:
            show screen Ne_entrance_N_scr
        $ clickable = False
        MC "It's just a fence."
        $ clickable = True
        hide screen Ne_entrance_M_scr
        hide screen Ne_entrance_D_scr
        hide screen Ne_entrance_E_scr
        hide screen Ne_entrance_N_scr
        jump Ne_entrance_M1

    if Ne_fence == True:
        hide screen map_button
        if day_time == 3:
            if Ne_ES1 == True:

                hide screen week_day_viewer
                hide screen time_skip_button
                hide screen day_time_viewer
                $ renpy.music.stop(channel="music2", fadeout=1)
                $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
                scene Ne_ES1_p1 with dissolve
                MC "(If I want to find out what these two women are really up to, I’m going to need to raise my game when it comes to investigating them!)"
                MC "(I’ll hop over the back fence, if I’m lucky they’ll be at it when I reach the house!)"
                scene Ne_ES1_p2
                MC "Ugh… Arggh…"
                MC "C’mon… uh! Just a bit more…"
            else:
                scene Ne_ES1_p1 with dissolve
                MC "Ugh… Arggh…"
                scene Ne_ES1_p2
                MC "C’mon… uh! Just a bit more…"
            menu:
                "Play":
                    call screen Ne_fence_climb
                "{image=cheat_code}":
                    jump Ne_fence_lab2
        if day_time == 4:
            scene Ne_ES1_p1a with dissolve
            MC "Ugh… Arggh…"
            scene Ne_ES1_p2a
            MC "C’mon… uh! Just a bit more…"
            menu:
                "Play":
                    call screen Ne_fence_climb
                "{image=cheat_code}":
                    jump Ne_fence_lab2
        else:

            hide screen map_button
            if day_time == 1:
                show screen Ne_entrance_M_scr
            if day_time == 2:
                show screen Ne_entrance_D_scr
            if day_time == 3:
                show screen Ne_entrance_E_scr
            if day_time == 4:
                show screen Ne_entrance_N_scr
            $ clickable = False
            MC "Somebody can see me at this time. I should try in the evening or at night."
            $ clickable = True
            hide screen Ne_entrance_M_scr
            hide screen Ne_entrance_D_scr
            hide screen Ne_entrance_E_scr
            hide screen Ne_entrance_N_scr
            jump Ne_entrance_M1


screen Ne_fence_climb:
    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1320 ypos 180
    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True
    imagebutton:

        xpos 1344
        ypos 51
        focus_mask True
        idle "images/Ne_1/ES1/C_mg/climb.png"
        hover "images/Ne_1/ES1/C_mg/climb_hover.png"

        action [SetVariable("clean_bar_value", clean_bar_value + 0.30)]
        unhovered Hide("displayTextScreen")

    if clean_bar_value >= 1.5:
        timer 1.3 action [Hide("Ne_fence_climb"),SetVariable("clean_bar_value", 0),Jump("Ne_fence_lab2")]

label Ne_fence_lab2:

    if day_time ==3 and Ne_ES1 == False:
        scene Ne_ES1_p3
        $ renpy.pause(2,hard = True)
        MC "*Pant* Got it!"

        scene Ne_ES1_p5
        MC "(That wasn’t too hard! I was afraid I was going to get hurt climbing that!)"
        jump Ne_outside_M1


    if day_time ==4:
        scene Ne_ES1_p3a
        $ renpy.pause(2,hard = True)
        MC "*Pant* Got it!"
        scene Ne_ES1_p5a
        MC "(That wasn’t too hard! I was afraid I was going to get hurt climbing that!)"
        $ renpy.block_rollback()
        jump Ne_outside_M1

    if Ne_ES1 == True:

        scene Ne_ES1_p3
        $ renpy.pause(2,hard = True)
        MC "*Pant* Got it!"

        MC "(That wasn’t too hard! I was afraid I was going to get hurt climbing that!)"

        scene Ne_ES1_p4
        "*THUD*"
        MC "Ouch…"
        MC "(Yeah, I spoke too soon on that one.)"

        scene Ne_ES1_p5
        MC "(Alright, let’s see what I can find back here.)"
        MC "(Remember, keep your eyes on the prize, [player_name]. You’re here to see some hot lesbian action!)"
        $ renpy.block_rollback()
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump Ne_outside_M1