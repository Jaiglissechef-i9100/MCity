image salon_paint_p1 = "images/home/salon/morning/scenes/salon_paint/Painting Evening.jpg"
image salon_paint_p2 = "images/home/salon/morning/scenes/salon_paint/Painting Morning.jpg"
image salon_paint_p3 = "images/home/salon/morning/scenes/salon_paint/Painting Night.jpg"

label salon_paint_label:
    if day_time == 1:
        scene salon_paint_p2
        $ renpy.pause()
        jump salon_morning1
    if day_time == 2:
        scene salon_paint_p2
        $ renpy.pause()
        jump salon_morning1
    if day_time == 3:
        scene salon_paint_p1
        $ renpy.pause()
        jump salon_morning1
    if day_time == 4:
        scene salon_paint_p3
        $ renpy.pause()
        jump salon_morning1

