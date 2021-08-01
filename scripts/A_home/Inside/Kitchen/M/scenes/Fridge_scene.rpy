image li_fridge_p1 = "/images/a_home//Inside/Kitchen/M/scenes/Fridge/1.jpg"
image li_fridge_p2 = "/images/a_home//Inside/Kitchen/M/scenes/Fridge/2.jpg"
image li_fridge_p3 = "/images/a_home//Inside/Kitchen/M/scenes/Fridge/3.jpg"

label fridge_scene_label:
    hide screen map_button
    scene li_fridge_p1
    call screen fridge_scene_scr
label fridge_scene_label2:
    scene black

    $ renpy.pause(2,hard=True)
    MC "Nice! The beer is cold. It will be relief in that hot weather."
    scene li_fridge_p3
    MC "Okay... Done! Let's go back to them."
    $ MAS7_fridge = 3
    jump a_kitchen_M1

screen fridge_scene_scr:
    if MAS7_fridge == True:
        imagebutton:
            xpos 602
            ypos 89
            focus_mask True
            idle "/images/a_home//Inside/Kitchen/M/scenes/Fridge/Frigde2.png"
            hover "/images/a_home//Inside/Kitchen/M/scenes/Fridge/Frigde2_hover.png"
            hovered Show("displayTextScreen", displayText = __("Open"))
            if clickable == True:
                action [Hide("displayTextScreen"),Hide("fridge_scene_scr"),Show("fridge_scene_scr2")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("fridge_scene_scr"),Jump("a_kitchen_M1")]

screen fridge_scene_scr2:
    add "/images/a_home//Inside/Kitchen/M/scenes/Fridge/2.jpg"
    imagebutton:
        xpos 1027
        ypos 507
        focus_mask True
        idle "/images/a_home//Inside/Kitchen/M/scenes/Fridge/Frigde3.png"
        hover "/images/a_home//Inside/Kitchen/M/scenes/Fridge/Frigde3_hover.png"
        hovered Show("displayTextScreen", displayText = __("Beer"))
        if clickable == True:
            action [Hide("displayTextScreen"),Hide("fridge_scene_scr2"),Jump("fridge_scene_label2")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("fridge_scene_scr2"),Jump("a_kitchen_M1")]

