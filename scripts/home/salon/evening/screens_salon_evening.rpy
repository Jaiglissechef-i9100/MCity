screen salon_evening:
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door1_evening_idle.png"
        hover "images/home/salon/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Corridor")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door2_evening_idle.png"
        hover "images/home/salon/evening/door2_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Kitchen")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door3_evening_idle.png"
        hover "images/home/salon/evening/door3_evening_hover.png"
        if renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Parent's Bedroom")
        if not renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Main Bedroom")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("parents_bedroom_evening1")]
        unhovered Hide("displayTextScreen")

    if caroline_salon_evening_scene1 == True and Caroline_points == 1:
        imagebutton:
            xpos 1487
            ypos 704
            focus_mask True
            idle "images/home/salon/evening/scenes/caroline_salon_evening_scene1/caroline_b1.png"
            hover "images/home/salon/evening/scenes/caroline_salon_evening_scene1/caroline_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"),Jump("caroline_salon_evening_scene1_label")]
            unhovered Hide("displayTextScreen")
    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/evening/Money Salon Evening.png"
            hover "images/home/salon/evening/Money Salon Evening_hover.png"
            hovered Show("displayTextScreen", displayText = "Money")
            action [Hide("displayTextScreen"),Jump("salon_money_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"
        hover "images/home/salon/morning/paint_b1_hover.png"
        hovered Show("displayTextScreen", displayText = "Painting")
        action [Hide("displayTextScreen"),Jump("salon_paint_label")]
        unhovered Hide("displayTextScreen")
    if CR2_ES1 == True and Caroline_points == 2:
        imagebutton:
            xpos 325
            ypos 499
            focus_mask True
            idle "images/home/salon/evening/scenes/CR2_ES1/B1.png"
            hover "images/home/salon/evening/scenes/CR2_ES1/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"),Jump("CR2_ES1_label")]
            unhovered Hide("displayTextScreen")

    if CR2_ES2 == True and Caroline_points == 2:
        imagebutton:
            xpos 214
            ypos 396
            focus_mask True
            idle "images/home/salon/evening/scenes/CR2_ES2/B1.png"
            hover "images/home/salon/evening/scenes/CR2_ES2/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"),Jump("CR2_ES2_label")]
            unhovered Hide("displayTextScreen")

    if MLR2_ES2 == True and can_MLR2_ES2 == True and ml_points == 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/evening/door3_evening_idle.png"
            hover "images/home/salon/evening/door3_evening_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Parent's Bedroom")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Main Bedroom")
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("MLR2_ES2_label")]
            unhovered Hide("displayTextScreen")
screen salon_evening_notclickable:
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/morning/paint_b1.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door1_evening_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door2_evening_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/evening/door3_evening_idle.png"

    if caroline_salon_evening_scene1 == True and Caroline_points == 1:
        imagebutton:
            xpos 1487
            ypos 704
            focus_mask True
            idle "images/home/salon/evening/scenes/caroline_salon_evening_scene1/caroline_b1.png"
    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/evening/Money Salon Evening.png"
            hover "images/home/salon/evening/Money Salon Evening_hover.png"

    if CR2_ES1 == True and Caroline_points == 2:
        imagebutton:
            xpos 325
            ypos 499
            focus_mask True
            idle "images/home/salon/evening/scenes/CR2_ES1/B1.png"
            hover "images/home/salon/evening/scenes/CR2_ES1/B1_hover.png"

    if CR2_ES2 == True and Caroline_points == 2:
        imagebutton:
            xpos 214
            ypos 396
            focus_mask True
            idle "images/home/salon/evening/scenes/CR2_ES2/B1.png"

    if MLR2_ES2 == True and can_MLR2_ES2 == True and ml_points == 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/evening/door3_evening_idle.png"