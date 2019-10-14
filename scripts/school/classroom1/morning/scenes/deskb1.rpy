label Deskb1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen classroom1_morning_notclickable
    $ can_hide_windows = False
    if day_time == 1:
        menu:
            "Do you want to start the lesson?":
                hide screen classroom1_morning_notclickable
                scene macy_scene1_p5
                $ renpy.pause(3,)
                scene black
                $ renpy.pause(2,hard = True)
                $ day_time += 1
                jump classroom1_morning1
            "Cancel":
                jump classroom1_morning1
