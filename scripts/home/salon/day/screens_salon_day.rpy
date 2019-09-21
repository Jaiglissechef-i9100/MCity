screen salon_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door1_morning_idle.png"
        hover "images/home/salon/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Corridor"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door2_morning_idle.png"
        hover "images/home/salon/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Kitchen"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door3_morning_idle.png"
        hover "images/home/salon/morning/door3_morning_hover.png"
        if renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = __("Parent's Bedroom"))
        if not renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = __("Main Bedroom"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("parents_bedroom_day1")]
        unhovered Hide("displayTextScreen")

    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/morning/Money Salon Morning.png"
            hover "images/home/salon/morning/Money Salon Morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Money"))
            action [Hide("displayTextScreen"),Jump("salon_money_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"
        hover "images/home/salon/morning/paint_b1_hover.png"
        hovered Show("displayTextScreen", displayText = __("Painting"))
        action [Hide("displayTextScreen"),Jump("salon_paint_label")]
        unhovered Hide("displayTextScreen")

screen salon_day_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door1_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door2_morning_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/morning/door3_morning_idle.png"

    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/morning/Money Salon Morning.png"
