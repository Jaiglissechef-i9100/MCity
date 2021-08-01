image locker_b1v1_p1 = "images/school/teacher_room2/day/locker/RenPy2.jpg"
image locker_b1v1_p2 = "images/school/teacher_room2/day/locker/RenPy3.jpg"

default money_from_lockerv1 = True
default put_envelopev1 = False

label locker_v1_label:
    scene locker_b1v1_p1
    call screen locker_b1v1_screen

label lockerv1_open_label:
    scene locker_b1v1_p2
    call screen lockerv1_open_screen

label money_from_lockerv1_label:
    $ inventory.earn(20)
    $ money_from_lockerv1 = False
    scene locker_b1v1_p2
    call screen lockerv1_open_screen

label celianote_from_lockerv1_label:
    $ inventory.add(celia_note)
    $ can_take_celianote = False
    scene locker_b1v1_p2
    call screen lockerv1_open_screen

label put_envelopev1_label:
    scene locker_b1v1_p2
    show screen lockerv1_open_screen
    $ inventory.drop(envelope)
    $ store.active_item = None
    $ celia_invitation_webcam = 1
    hide screen lockerv1_open_screen
    scene locker_b1v1_p1
    MC "Okay. I should go far away from here. She can’t even suspect me on this."
    $ envolpe_event = False
    $ day_time += 1
    jump map_label

label empty_envelopev1_label:
    $ lockerv1_open_morning_screen_notclickable = True
    show screen lockerv1_open_morning_screen
    MC "Why should I put an empty envelope inside?"
    MC "I need a pen. I have probably a few in my locker in the school corridor."
    jump lockerv1_open_morning_label

label put_dildov1_label:
    scene locker_b1v1_p1
    $ inventory.drop(dildo)
    $ store.active_item = None
    $ webcam_dildo_scenes_unloacked_V1 = 1
    MC "Okay. I should go far away from here. She can’t even suspect me on this."
    $ day_time += 1
    jump map_label

label put_sexy_cloth_label:
    scene locker_b1v1_p1
    $ inventory.drop(sexy_cloth)
    $ store.active_item = None
    $ webcam_sexy_cloth_scenes_unloacked_V1 = 1
    MC "Okay. I should go far away from here. She can’t even suspect me on this."
    $ day_time += 1
    jump map_label

label put_vibrator_label:
    scene locker_b1v1_p1
    $ inventory.drop(vibrator)
    $ store.active_item = None
    $ webcam_vibrator_scenes_unloacked_V1 = 1
    MC "Okay. I should go far away from here. She can’t even suspect me on this."
    $ day_time += 1
    jump map_label

screen locker_b1v1_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/teacher_room2/day/locker/locker_door.png"
        hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
        action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Jump("lockerv1_open_label")]
        hovered Show("displayTextScreen", displayText = __("Open"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("teacher_room2_day1")]

    if dildo.selected and dildo in inventory.items and celia_webcam_menuv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/locker_door.png"
            hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
            action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Jump("put_dildov1_label")]
            hovered Show("displayTextScreen", displayText = __("Put Dildo"))
            unhovered Hide("displayTextScreen")

    if sexy_cloth.selected and sexy_cloth in inventory.items and celia_webcam_menuv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/locker_door.png"
            hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
            action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Jump("put_sexy_cloth_label")]
            hovered Show("displayTextScreen", displayText = __("Put Sexy Cloth"))
            unhovered Hide("displayTextScreen")

    if vibrator.selected and vibrator in inventory.items and celia_webcam_menuv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/locker_door.png"
            hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
            action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Jump("put_vibrator_label")]
            hovered Show("displayTextScreen", displayText = __("Put Vibrator"))
            unhovered Hide("displayTextScreen")

screen lockerv1_open_screen:
    key "hide_windows" action NullAction()
    if money_from_lockerv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/Money20$.png"
            if lockerv1_open_morning_screen_notclickable == False:
                hover "images/school/teacher_room2/day/locker/Money20$_hover.png"
                action [Hide("displayTextScreen"),Jump("money_from_lockerv1_label")]
                hovered Show("displayTextScreen", displayText = __("Money(20$)"))
                unhovered Hide("displayTextScreen")

    if celia_note not in inventory.items and can_take_celianote == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/celia_note_b1.png"
            hover "images/school/teacher_room2/day/locker/celia_note_b1_hover.png"
            if lockerv1_open_morning_screen_notclickable == False:
                action [Hide("displayTextScreen"),Jump("celianote_from_lockerv1_label")]
                hovered Show("displayTextScreen", displayText = __("Celia’s Note"))
                unhovered Hide("displayTextScreen")

    if envelope in inventory.items and envelope.selected and put_envelopev1 == False and lockerv1_open_morning_screen_notclickable == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/envelope_b3.png"
            hover "images/school/teacher_room2/day/locker/envelope_b3.png"
            action [Hide("displayTextScreen"),SetVariable("put_envelopev1", True),Jump("put_envelopev1_label")]
            hovered Show("displayTextScreen", displayText = __("Put Envelope"))
            unhovered Hide("displayTextScreen")

    if empty_envelope in inventory.items and empty_envelope.selected and put_envelopev1 == False and lockerv1_open_morning_screen_notclickable == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/envelope_b3.png"
            hover "images/school/teacher_room2/day/locker/envelope_b3.png"
            action [Hide("displayTextScreen"),Jump("empty_envelopev1_morning_label")]
            hovered Show("displayTextScreen", displayText = __("Put Envelope"))
            unhovered Hide("displayTextScreen")

    if put_envelopev1 == True and  envolpe_event == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/envelope_b2.png"
            hover "images/school/teacher_room2/day/locker/envelope_b2.png"

    if lockerv1_open_morning_screen_notclickable == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/metal_drawer_close.mp3"),Jump("locker_v1_label")]

