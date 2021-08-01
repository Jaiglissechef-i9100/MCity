image corridor_painting_p1 = "/images/home/corridor/morning/scenes/corridor_painting/b1_day.jpg"
image corridor_painting_p2 = "/images/home/corridor/morning/scenes/corridor_painting/b1_evening.jpg"
image corridor_painting_p3 = "/images/home/corridor/morning/scenes/corridor_painting/b1_night.jpg"

label painting_corridor_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if day_time == 1:
        scene corridor_painting_p1 with dissolve
        $ renpy.pause()
        jump corridor_morning1

    if day_time == 2:
        scene corridor_painting_p1 with dissolve
        $ renpy.pause()
        jump corridor_morning1

    if day_time == 3:
        scene corridor_painting_p2 with dissolve
        $ renpy.pause()
        jump corridor_morning1

    if day_time == 4:
        scene corridor_painting_p3 with dissolve
        $ renpy.pause()
        jump corridor_morning1

