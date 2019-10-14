image Li_car_p1 = "/images/a_home/outside/Garage/M/scenes/Li_Car/1.jpg"
image Li_car_p1b = "/images/a_home/outside/Garage/M/scenes/Li_Car/1b.jpg"
image Li_car_p2 = "/images/a_home/outside/Garage/M/scenes/Li_Car/2.jpg"
image Li_car_p2a = "/images/a_home/outside/Garage/M/scenes/Li_Car/2b.jpg"
default Li_car_money = True
label Li_car_label:
    hide screen map_button
    $ can_hide_windows = False
    if day_time == 4:
        scene Li_car_p2
    else:
        scene Li_car_p1
    call screen Li_car_scr

label Li_car_label_money:
    show screen Li_car_scr2
    $ clickable = False
    $ money = renpy.random.choice( [10, 11, 12, 13, 14, 15, 16, 17, 19, 18, 20])
    $ inventory.earn(money)
    MC "Nice! +[money]$"
    $ clickable = True
    $ Li_car_money = False
    hide screen Li_car_scr2
    call screen Li_car_scr2

label Li_car_label2:
    if day_time == 4:
        scene Li_car_p2
    else:
        scene Li_car_p1
    $ renpy.pause(0.4,hard = True)
    if day_time == 4:
        scene Li_car_p2a
    else:
        scene Li_car_p1b
    call screen Li_car_scr2
screen Li_car_scr:

    if day_time == 4:

        imagebutton:
            xpos 725
            ypos 182
            focus_mask True
            idle "/images/a_home/outside/Garage/M/scenes/Li_Car/B1b.png"
            hover "/images/a_home/outside/Garage/M/scenes/Li_Car/B1b_hover.png"
            if clickable == True:
                activate_sound "sfx/car_door.wav"
                hovered Show("displayTextScreen", displayText = __("Open"))
                action [Hide("Li_car_scr"),Hide("displayTextScreen"),Jump("Li_car_label2")]
                unhovered Hide("displayTextScreen")

    if day_time != 4:
        imagebutton:
            xpos 725
            ypos 182
            focus_mask True
            idle "/images/a_home/outside/Garage/M/scenes/Li_Car/B1a.png"
            hover "/images/a_home/outside/Garage/M/scenes/Li_Car/B1a_hover.png"
            if clickable == True:
                activate_sound "sfx/car_door.wav"
                hovered Show("displayTextScreen", displayText = __("Open"))
                action [Hide("Li_car_scr"),Hide("displayTextScreen"),Jump("Li_car_label2")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("Li_car_scr"), Jump("a_garage_M1")]

screen Li_car_scr2:

    if Li_car_money == True:
        if day_time == 4:
            add "/images/a_home/outside/Garage/M/scenes/Li_Car/2b.jpg"
            imagebutton:
                xpos 850
                ypos 399
                focus_mask True
                idle "/images/a_home/outside/Garage/M/scenes/Li_Car/B2b.png"
                hover "/images/a_home/outside/Garage/M/scenes/Li_Car/B2b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Money"))
                    action [Hide("displayTextScreen"),Jump("Li_car_label_money")]
                    unhovered Hide("displayTextScreen")
        else:
            add "/images/a_home/outside/Garage/M/scenes/Li_Car/1b.jpg"
            imagebutton:
                xpos 850
                ypos 399
                focus_mask True
                idle "/images/a_home/outside/Garage/M/scenes/Li_Car/B2a.png"
                hover "/images/a_home/outside/Garage/M/scenes/Li_Car/B2a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Money"))
                    action [Hide("displayTextScreen"),Jump("Li_car_label_money")]
                    unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            activate_sound "sfx/car_close.wav"
            action [Hide("Li_car_scr2"), Jump("a_garage_M1")]
