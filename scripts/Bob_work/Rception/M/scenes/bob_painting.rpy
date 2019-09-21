image bob_reception_painting = "/images/Bob_work/reception/M/1.jpg"

label bob_paintingreception_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene bob_reception_painting with dissolve
    $ renpy.pause()
    jump bob_reception_morning1
