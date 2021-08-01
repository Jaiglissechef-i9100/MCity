image bob_car_bg1 = "/images/Bob_work/outside/M/CarInside/Car1.jpg"
image bob_car_bg2 = "/images/Bob_work/outside/M/CarInside/Car2.jpg"

default bob_carbook_s = 1
default bob_carmoney = True
label bob_car_label:
    scene bob_car_bg1
    $ can_map = False
    call screen bob_car_scr

label bob_car_locked_label:
    $ clickable = False
    MC "It's locked."
    $ clickable = True
    jump bob_car_label


screen bob_car_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 525
        ypos 73
        focus_mask True
        idle "images/Bob_work/outside/M/CarInside/B1.png"
        hover "images/Bob_work/outside/M/CarInside/B1_hover.png"
        if bob_carkeys.selected:
            hovered Show("displayTextScreen", displayText = "Open Car")
            if clickable == True:
                activate_sound "sfx/car_open.wav"
                action [Hide("displayTextScreen"),Jump("bob_car_label2")]
                unhovered Hide("displayTextScreen")
        else:
            hovered Show("displayTextScreen", displayText = "Car Door")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("bob_car_locked_label")]
                unhovered Hide("displayTextScreen")


    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_work_outside_morning1")]

label bob_car_label2:
    $ renpy.pause(1, hard = True)
    scene bob_car_bg2
    call screen bob_car_scr2


screen bob_car_scr2:
    key "hide_windows" action NullAction()
    if bob_carbook_s == 1:
        imagebutton:
            xpos 1150
            ypos 378
            focus_mask True
            idle "images/Bob_work/outside/M/CarInside/B2.png"
            hover "images/Bob_work/outside/M/CarInside/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Book")
                action [Hide("displayTextScreen"),Jump("bob_carbook")]
                unhovered Hide("displayTextScreen")
    if bob_carmoney == True:
        imagebutton:
            xpos 630
            ypos 95
            focus_mask True
            idle "images/Bob_work/outside/M/CarInside/B3.png"
            hover "images/Bob_work/outside/M/CarInside/B3_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Money")
                action [Hide("displayTextScreen"),Jump("bob_carmoney")]
                unhovered Hide("displayTextScreen")

    if not "img12_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1891
            ypos 478
            focus_mask True
            idle "images/secret_gallery/Bonus/B12.png"
            hover "images/secret_gallery/Bonus/B12_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img12_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            activate_sound "sfx/car_close.wav"
            action [Hide("bob_car_scr2"), Jump("bob_work_outside_morning1")]


label bob_carbook:
    show screen bob_car_scr2
    $ clickable = False
    if renpy.loadable("patch.rpy"):
        MC "What’s that book doing in here? It looks like it’s from Dad’s office. Maybe Dad might need it. I should return it to his office."
    else:
        MC "What’s that book doing in here? It looks like it’s from Bob’s office. Maybe Bob might need it. I should return it to his office."
    $ bob_carbook_s = 2
    $ inventory.add(bob_carbook)
    $ clickable = True
    jump bob_car_label2

label bob_carmoney:
    show screen bob_car_scr2
    $ clickable = False
    $ money = renpy.random.choice( [10, 11, 12, 13, 14, 15, 16, 17, 19, 18, 20])
    $ inventory.earn(money)
    MC "Nice! +[money]$"
    $ clickable = True
    $ bob_carmoney = False
    jump bob_car_label2