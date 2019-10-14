image bob_safe_p1 = "/images/Bob_work/office/M/safe/Safe.jpg"
image bob_safe_p2 = "/images/Bob_work/office/M/safe/Safe2.jpg"

default bob_safe_money_take = False

default bob_safe_firsttime_open = False
label bob_safe_label:
    scene bob_safe_p1
    call screen bob_safe_scr


screen bob_safe_scr:
    key "hide_windows" action NullAction()


    imagebutton:
        xpos 671
        ypos 141
        focus_mask True
        idle "images/Bob_work/office/M/safe/B1.png"
        hover "images/Bob_work/office/M/safe/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Safe")
            action [Hide("displayTextScreen"),Jump("bob_safeopen_label")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_desk_label")]


label bob_safeopen_label:
    if bob_safenote not in inventory.items:
        show screen bob_safe_scr
        $ clickable = False
        MC "The safe is locked. I need a code."
        $ clickable = True
        jump bob_safe_label
    if bob_safenote  in inventory.items:
        scene bob_safe_p2
        if bob_safe_firsttime_open == False:
            show screen bob_safeopen_scr
            $ clickable = False
            MC "Ah! Good! The code works. It’s now open."
            $ clickable = True
            $ bob_safe_firsttime_open = True

        call screen bob_safeopen_scr
screen bob_safeopen_scr:
    key "hide_windows" action NullAction()

    if bob_safe_money_take == False:
        imagebutton:
            xpos 1002
            ypos 344
            focus_mask True
            idle "images/Bob_work/office/M/safe/B2.png"
            hover "images/Bob_work/office/M/safe/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Money")
                action [Hide("displayTextScreen"),Jump("bob_safeopenmoney_label")]
                unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 850
        ypos 358
        focus_mask True
        idle "images/Bob_work/office/M/safe/B3.png"
        hover "images/Bob_work/office/M/safe/B3_hover.png"
        if clickable == True and Zv2_MS2_companyname_found == 1:
            hovered Show("displayTextScreen", displayText = "Note")
            action [Hide("displayTextScreen"),Jump("bob_safeopennote_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_desk_label")]


label bob_safeopenmoney_label:
    show screen bob_safeopen_scr
    $ clickable = False
    $ money = renpy.random.choice( [10, 11, 12, 13, 14, 15, 16, 17, 19, 18, 20])
    $ bob_safe_money_take = True
    $ inventory.earn(money)
    MC "Nice! +[money]$"
    $ clickable = True
    jump bob_safeopen_label



label bob_safeopennote_label:
    show screen bob_safeopen_scr
    $ clickable = False
    $ Zv2_MS2_companyname_found = 2
    MC "Hmm.. .Some notes.. There’s is also a second company name! Nice."
    $ clickable = True
    jump bob_safeopen_label