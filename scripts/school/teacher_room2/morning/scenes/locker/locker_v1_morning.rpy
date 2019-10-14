default lockerv1_open_morning_screen_notclickable = False
default C_locker_put_item = False

label locker_v1_morning_label:
    show screen map_button
    hide screen displayTextScreen
    scene locker_b1v1_p1
    if C_locker_put_item == True:
        MC "Okay. I should go far away from here. She can’t even suspect me on this."
        $ day_time = 3
        $ C_locker_put_item = False
        jump map_label
    call screen locker_b1v1_morning_screen

label lockerv1_open_morning_label:
    $ lockerv1_open_morning_screen_notclickable = False
    scene locker_b1v1_p2
    call screen lockerv1_open_morning_screen

label money_from_lockerv1_morning_label:
    $ inventory.earn(20)
    $ money_from_lockerv1 = False
    scene locker_b1v1_p2
    call screen lockerv1_open_morning_screen

label celianote_from_lockerv1_morning_label:
    $ inventory.add(celia_note)
    $ can_take_celianote = False
    scene locker_b1v1_p2
    call screen lockerv1_open_morning_screen

label put_envelopev1_morning_label:
    scene locker_b1v1_p2
    show screen lockerv1_open_morning_screen
    $ inventory.drop(envelope)
    $ celia_invitation_webcam = 1
    hide screen lockerv1_open_morning_screen
    scene locker_b1v1_p1
    MC "Okay. I should go far away from here. She can’t even suspect me on this."
    hide screen lockerv1_open_morning_screen
    $ day_time += 2
    $ envolpe_event = False
    jump map_label

label empty_envelopev1_morning_label:
    $ lockerv1_open_morning_screen_notclickable = True
    show screen lockerv1_open_morning_screen
    MC "Why should I put an empty envelope inside?"
    MC "I need a pen. I have probably a few in my locker in the school corridor."
    jump lockerv1_open_morning_label

label put_dildov1_morning_label:
    scene locker_b1v1_p1
    $ inventory.drop(dildo)
    $ store.active_item = None
    $ webcam_dildo_scenes_unloacked_V1 = 1
    $ C_locker_put_item = True
    call screen C_locker_item_menu_scr

label put_sexy_cloth_morning_label:
    scene locker_b1v1_p1
    $ inventory.drop(sexy_cloth)
    $ store.active_item = None
    $ webcam_sexy_cloth_scenes_unloacked_V1 = 1
    $ C_locker_put_item = True
    call screen C_locker_item_menu_scr

label put_vibrator_morning_label:
    scene locker_b1v1_p1
    $ inventory.drop(vibrator)
    $ store.active_item = None
    $ webcam_vibrator_scenes_unloacked_V1 = 1
    $ C_locker_put_item = True
    call screen C_locker_item_menu_scr

screen locker_b1v1_morning_screen:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 987
        ypos 164
        focus_mask True
        idle "images/school/teacher_room2/day/locker/locker_door.png"
        hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
        action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Jump("lockerv1_open_morning_label")]
        hovered Show("displayTextScreen", displayText = __("Open"))
        unhovered Hide("displayTextScreen")
    if celia_webcam_menuv1 == True:
        imagebutton:
            xpos 987
            ypos 164
            focus_mask True
            idle "images/school/teacher_room2/day/locker/locker_door.png"
            hover "images/school/teacher_room2/day/locker/locker_door_hover.png"
            action [Hide("displayTextScreen"),Hide("locker_b1v1_morning_screen"),Show("C_locker_menu_scr")]
            hovered Show("displayTextScreen", displayText = __("Open"))
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("teacher_room2_morning1")]

screen lockerv1_open_morning_screen:
    key "hide_windows" action NullAction()
    if money_from_lockerv1 == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/Money20$.png"
            hover "images/school/teacher_room2/day/locker/Money20$_hover.png"
            if lockerv1_open_morning_screen_notclickable == False:
                action [Hide("displayTextScreen"),Jump("money_from_lockerv1_morning_label")]
                hovered Show("displayTextScreen", displayText = __("Money(20$)"))
                unhovered Hide("displayTextScreen")
    if celia_note not in inventory.items and can_take_celianote == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/celia_note_b1.png"
            if lockerv1_open_morning_screen_notclickable == False:
                hover "images/school/teacher_room2/day/locker/celia_note_b1_hover.png"
                action [Hide("displayTextScreen"),Jump("celianote_from_lockerv1_morning_label")]
                hovered Show("displayTextScreen", displayText = __("Celia’s Note"))
                unhovered Hide("displayTextScreen")

    if envelope in inventory.items and envelope.selected and put_envelopev1 == False and lockerv1_open_morning_screen_notclickable == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/teacher_room2/day/locker/envelope_b3.png"
            hover "images/school/teacher_room2/day/locker/envelope_b3.png"
            action [Hide("displayTextScreen"),SetVariable("put_envelopev1", True),Jump("put_envelopev1_morning_label")]
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
            action [Play ("sound", "sfx/metal_drawer_close.mp3"),Jump("locker_v1_morning_label")]

screen C_locker_menu_scr:
    modal True
    imagebutton:
        xpos 750
        ypos 300
        focus_mask True
        idle "images/school/teacher_room2/day/locker/Open_locker.png"
        hover "images/school/teacher_room2/day/locker/Open_locker_hover.png"
        action [Play ("sound", "sfx/metal_drawer_open.mp3"),Hide("displayTextScreen"),Hide("C_locker_menu_scr"),Jump("lockerv1_open_morning_label")]

    if celia_webcam_menuv1 == True:
        imagebutton:
            xpos 750
            ypos 450
            focus_mask True
            idle "images/school/teacher_room2/day/locker/Select_Item.png"
            hover "images/school/teacher_room2/day/locker/Select_Item_hover.png"
            action [Play ("sound", "sfx/zipper.mp3"),Hide("displayTextScreen"),Hide("C_locker_menu_scr"),Hide("map_button"), Show("C_locker_item_menu_scr")]

screen C_locker_item_menu_scr:
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        unhovered Hide("display_Item_Name")
        action [SetVariable("inv_page", 0),Hide("C_locker_item_menu_scr"),Hide("display_Item_Name"), Hide("displayTextScreen"), Play ("sound", "sfx/zipper.mp3"), Jump("locker_v1_morning_label")]
    add Transform("images/game_gui/icons/inventory.png", zoom=.7) xalign 0.5 yalign 0.5
    $ x = 700
    $ y = 294
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(inventory.items)/12):
        $ next_inv_page = 0
    if prev_inv_page < int(len(inventory.items)/12):
        $ prev_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*12 and i+1>inv_page*12:
            $ x += 137
            if i%4==0:
                $ y += 133
                $ x = 750
            $ pic = item.image

            $ pich = item.hover_i

            imagebutton idle pic hover pich xpos x ypos y action [Show("display_Item_Name", my_tt_ypos=y, my_tt_xpos=x, displayText1 = [item.name]),  SetVariable("item", item), selectItem(item)] hovered [ Play ("sound", "sfx/click.wav"), Show("display_Item_Name",  my_tt_ypos=y, my_tt_xpos=x, displayText1 = [item.name]),] unhovered [Hide("display_Item_Name")] at inv_eff
            if item.selected:
                add Transform("gui/selected.png", zoom=.7) xpos x ypos y anchor (.5,.4)

        $ i += 1

    if dildo.selected and dildo in inventory.items and celia_webcam_menuv1 == True:
        add "images/school/teacher_room2/day/locker/Put1.png" xpos 743 ypos 785
    elif sexy_cloth.selected and sexy_cloth in inventory.items and celia_webcam_menuv1 == True:
        add "images/school/teacher_room2/day/locker/Put1.png" xpos 743 ypos 785
    elif vibrator.selected and vibrator in inventory.items and celia_webcam_menuv1 == True:
        add "images/school/teacher_room2/day/locker/Put1.png" xpos 743 ypos 785

    imagebutton:
        xpos 750
        ypos 790
        focus_mask True
        idle "images/school/teacher_room2/day/locker/Put.png"
        hover "images/school/teacher_room2/day/locker/Put_hover.png"
        if dildo.selected and dildo in inventory.items and celia_webcam_menuv1 == True:
            action Jump("put_dildov1_morning_label")
        elif sexy_cloth.selected and sexy_cloth in inventory.items and celia_webcam_menuv1 == True:
            action Jump("put_sexy_cloth_morning_label")
        elif vibrator.selected and vibrator in inventory.items and celia_webcam_menuv1 == True:
            action Jump("put_vibrator_morning_label")
        else:
            action NullAction()
