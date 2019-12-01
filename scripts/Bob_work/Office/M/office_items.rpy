image bob_statue_p1 = "/images/Bob_work/office/M/Statue.jpg"
image bob_fireplace_p1 = "/images/Bob_work/office/M/Fireplace.jpg"
image bob_tableR_p1 = "/images/Bob_work/office/M/tableR/tableR.jpg"
image bob_tableR_p2 = "/images/Bob_work/office/M/tableR/tableR2.jpg"
image bob_tableL_p1 = "/images/Bob_work/office/M/tableL/tableL.jpg"
image bob_tableL_p2 = "/images/Bob_work/office/M/tableL/tableL2.jpg"
image bob_redstatue_p1 = "/images/Bob_work/office/M/table.jpg"
default bob_carkeys_take = False
default bob_carkeys_put = True

default can_safe_note = False

label bob_statue_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene bob_statue_p1 with dissolve
    $ can_hide_windows = True
    MC "(I never understood why classical artists chose not to sculpt heads or hands.)"
    MC "(I mean, the face is one of the most interesting parts of any statue.)"
    $ can_hide_windows = False
    jump bob_office_M1

label bob_fireplace_label:
    scene bob_fireplace_p1
    call screen bob_fireplace_scr

screen bob_fireplace_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 327
        ypos 433
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B1.png"
        hover "images/Bob_work/office/M/Fireplace/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Head Statue"))
            action [Hide("displayTextScreen"),Jump("bob_headstatue_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 698
        ypos 25
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B2.png"
        hover "images/Bob_work/office/M/Fireplace/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Painting"))
            action [Hide("displayTextScreen"),Jump("bob_painting_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1537
        ypos 547
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B3.png"
        hover "images/Bob_work/office/M/Fireplace/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Statue")
            action [Hide("displayTextScreen"),Jump("bob_statue1_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_headstatue_label:
    show screen bob_fireplace_scr
    $ clickable = False
    MC "(It’s a deep blue marble bust. There is a bright shine off it - someone has polished this thing to perfection!)"
    MC "(I can almost see my reflection in it!)"
    $ clickable = True
    jump bob_fireplace_label

label bob_painting_label:
    show screen bob_fireplace_scr
    $ clickable = False

    MC "(There’s something deeply unsettling about this painting.)"
    MC "(It’s kinda like a dirty sidewalk. Who the hell would want THIS, hanging up in their office?)"

    $ clickable = True
    jump bob_fireplace_label

label bob_statue1_label:
    show screen bob_fireplace_scr
    $ clickable = False
    MC "(Is this supposed to be a lightswitch?)"
    MC "(Or maybe it’s a person’s nose?)"
    MC "(God! I hate abstract art.)"
    $ clickable = True
    jump bob_fireplace_label

label bob_tableR_label:
    scene bob_tableR_p1
    call screen bob_tableR_scr

screen bob_tableR_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 640
        ypos 458
        focus_mask True
        idle "images/Bob_work/office/M/tableR/B1.png"
        hover "images/Bob_work/office/M/tableR/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Open"))
            action [Play ("sound", "sfx/drawer_op.wav"),Hide("displayTextScreen"),Jump("bob_tableRopen_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_tableRopen_label:
    $ renpy.pause(0.2,hard= True)
    scene bob_tableR_p2
    call screen bob_tableRopen_scr

screen bob_tableRopen_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_tableL_label:
    scene bob_tableL_p1
    call screen bob_tableL_scr

screen bob_tableL_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 705
        ypos 425
        focus_mask True
        idle "images/Bob_work/office/M/tableL/B1.png"
        hover "images/Bob_work/office/M/tableL/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Open"))
            action [Play ("sound", "sfx/drawer_op.wav"),Hide("displayTextScreen"),Jump("bob_tableLopen_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_tableLopen_label:
    $ renpy.pause(0.2,hard = True)
    scene bob_tableL_p2
    call screen bob_tableLopen_scr

screen bob_tableLopen_scr:
    key "hide_windows" action NullAction()
    if bob_safenote not in inventory.items and day_time == 2 and Zv2_MS2_companyname == 2 and can_safe_note == True:
        imagebutton:
            xpos 850
            ypos 561
            focus_mask True
            idle "images/Bob_work/office/M/tableL/B2.png"
            hover "images/Bob_work/office/M/tableL/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Safe Note"))
                action [Hide("displayTextScreen"),Jump("bob_safenote_label")]
                unhovered Hide("displayTextScreen")

    if bob_safenote in inventory.items and bob_safenote.selected and day_time == 2 and Zv2_MS2_companyname == 2 and can_safe_note == True:
        imagebutton:
            xpos 850
            ypos 561
            focus_mask True
            idle "images/Bob_work/office/M/tableL/B3.png"
            hover "images/Bob_work/office/M/tableL/B3_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Put Safe Note"))
                action [Hide("displayTextScreen"),Jump("bob_safenoteput_label")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_safenote_label:
    $ clickable = False
    show screen bob_tableLopen_scr
    MC "Hmm... safe code be useful. Not very wise to leave it lying around like that. Anyone could find it."
    $ inventory.add(bob_safenote)
    $ clickable = True
    jump bob_tableLopen_label

label bob_safenoteput_label:
    $ clickable = False
    show screen bob_tableLopen_scr
    $ inventory.drop(bob_safenote)
    MC "Let’s leave it in here."

    $ bob_safenote.selected = False
    $ clickable = True
    jump bob_tableLopen_label

label bob_redstatue_label:
    scene bob_redstatue_p1
    call screen bob_redstatue_scr

screen bob_redstatue_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 466
        ypos 62
        focus_mask True
        idle "images/Bob_work/office/M/B10.png"
        hover "images/Bob_work/office/M/B10_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Red Statue"))
            action [Hide("displayTextScreen"),Jump("bob_redstatue2_label")]
            unhovered Hide("displayTextScreen")

    if bob_carkeys_take == False and day_time == 1 and Bob_in_work == True:
        imagebutton:
            xpos 1024
            ypos 512
            focus_mask True
            idle "images/Bob_work/office/M/B1.png"
            hover "images/Bob_work/office/M/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Car Keys"))
                action [Hide("displayTextScreen"),Jump("bob_carkeys_label")]
                unhovered Hide("displayTextScreen")

    if bob_carkeys_put == False and bob_carkeys.selected:
        imagebutton:
            xpos 1024
            ypos 512
            focus_mask True
            idle "images/Bob_work/office/M/B2.png"
            hover "images/Bob_work/office/M/B1.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Put Car Keys"))
                action [Hide("displayTextScreen"),Jump("bob_carkeys_put_label")]
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_redstatue2_label:
    $ clickable = False
    show screen bob_redstatue_scr
    MC "(This is pretty cool! It looks like it’s made out of red glass, or maybe even a tinted jade!)"
    MC "(Is it supposed to be a cat? Or maybe a panther?)"
    $ clickable = True
    jump bob_redstatue_label

label bob_carkeys_label:
    show screen bob_redstatue_scr
    $ clickable = False
    if persistent.incest_patch == True:
        MC "Oh! It’s Dad’s car keys. But why are there two? The other one must be a spare?"
    else:
        MC "Oh! It’s Bob’s car keys. But why are there two? The other one must be a spare?"
    $ inventory.add(bob_carkeys)
    $ bob_carkeys_take = True
    $ clickable = True
    $ bob_carkeys_put = False
    $ bob_carkeys.selected = False
    jump bob_redstatue_label

label bob_carkeys_put_label:
    show screen bob_redstatue_scr
    $ clickable = False
    $ inventory.drop(bob_carkeys)
    $ bob_carkeys_take = False
    $ bob_carkeys_put = True
    $ active_item = None
    $ bob_carkeys.selected = False
    if persistent.incest_patch == True:
        MC "Let’s return Dad’s keys."
    else:
        MC "Let’s return Bob’s keys."
    $ clickable = True
    jump bob_redstatue_label
