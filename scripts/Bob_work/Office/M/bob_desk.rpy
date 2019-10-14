image bob_desk_p1 = "/images/Bob_work/office/M/desk/Desk.jpg"

default car_book_put = False
label bob_desk_label:
    scene bob_desk_p1
    call screen bob_desk_scr


screen bob_desk_scr:
    key "hide_windows" action NullAction()



    imagebutton:
        xpos 0
        ypos 175
        focus_mask True
        idle "images/Bob_work/office/M/desk/B1.png"
        hover "images/Bob_work/office/M/desk/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Books")
            action [Hide("displayTextScreen"),Jump("bob_deskbooks_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 977
        ypos 205
        focus_mask True
        idle "images/Bob_work/office/M/desk/B2.png"
        hover "images/Bob_work/office/M/desk/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Laptop")
            action [Hide("displayTextScreen"),Jump("bob_desklaptop_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 558
        ypos 224
        focus_mask True
        idle "images/Bob_work/office/M/desk/B3.png"
        hover "images/Bob_work/office/M/desk/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Papers")
            action [Hide("displayTextScreen"),Jump("bob_deskpapers_label")]
            unhovered Hide("displayTextScreen")
    if day_time == 2 and Zv2_MS2_companyname == 1:
        imagebutton:
            xpos 782
            ypos 201
            focus_mask True
            idle "images/Bob_work/office/M/desk/B4.png"
            hover "images/Bob_work/office/M/desk/B4_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Reports")
                action [Hide("displayTextScreen"),Jump("bob_deskraports_label")]
                unhovered Hide("displayTextScreen")

    if car_book_put == False and bob_carbook.selected:
        imagebutton:
            xpos 283
            ypos 215
            focus_mask True
            idle "images/Bob_work/office/M/desk/B5.png"
            hover "images/Bob_work/office/M/desk/B6.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Put Book")
                action [Hide("displayTextScreen"),Jump("bob_deskcarbookput_label")]
                unhovered Hide("displayTextScreen")

    if car_book_put == True:
        imagebutton:
            xpos 283
            ypos 215
            focus_mask True
            idle "images/Bob_work/office/M/desk/B6.png"
            hover "images/Bob_work/office/M/desk/B6_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Book")
                action [Hide("displayTextScreen"),Jump("bob_deskcarbook_label")]
                unhovered Hide("displayTextScreen")
    if Bob_work_minigame == True:
        imagebutton:
            xpos 786
            ypos 316
            focus_mask True
            idle "images/Bob_work/office/M/desk/Minigame.png"
            hover "images/Bob_work/office/M/desk/Minigame_hover.png"
            if clickable == True and day_time == 2:
                hovered Show("displayTextScreen", displayText = "Documents")
                action [Hide("displayTextScreen"),Jump("bob_deskminigame_label")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 119
        ypos 998
        focus_mask True
        idle "images/Bob_work/office/M/desk/B7.png"
        hover "images/Bob_work/office/M/desk/B7_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Safe")
            action [Hide("displayTextScreen"),Jump("bob_safe_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]
label bob_deskbooks_label:
    show screen bob_desk_scr
    $ clickable = False
    if renpy.loadable("patch.rpy"):
        MC "Those are Dad’s books."
    else:
        MC "Those are Bob’s books."
    MC "I guess he has a lot of free time in here."
    $ clickable = True
    jump bob_desk_label

label bob_desklaptop_label:
    show screen bob_desk_scr
    $ clickable = False
    if renpy.loadable("patch.rpy"):
        MC "Dad’s laptop. I don't need to use it right now."
    else:
        MC "Bob’s laptop. I don't need to use it right now."
    $ clickable = True
    jump bob_desk_label

label bob_deskpapers_label:
    show screen bob_desk_scr
    $ clickable = False
    MC "Meh.. Just papers. Some boring work stuff."
    $ clickable = True
    jump bob_desk_label


label bob_deskraports_label:

    show screen bob_desk_scr
    $ clickable = False
    $ Zv2_MS2_companyname_found = 1
    MC "Hmm.. Just some reports..."
    MC "I should check a few pages, just in case."
    hide screen bob_desk_scr
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2,hard=True)
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    scene bob_desk_p1
    show screen bob_desk_scr
    $ can_hide_windows = True
    MC "There's something interesting..."
    MC "Bingo! That's the name of the company. I think this is what Zuri wants."
    $ clickable = True
    $ can_hide_windows = False
    jump bob_desk_label

label bob_deskcarbookput_label:
    show screen bob_desk_scr
    $ clickable = False
    $ car_book_put = True
    $ inventory.drop(bob_carbook)
    $ bob_carbook.selected = False
    MC "Let’s leave it in here. I don’t need it."
    $ clickable = True
    jump bob_desk_label

label bob_deskcarbook_label:
    show screen bob_desk_scr
    $ inventory.add(bob_carbook)
    $ car_book_put = False
    jump bob_desk_label

label bob_deskminigame_label:
    show screen bob_desk_scr
    $ clickable = False
    if can_Bob_work_minigame == True:
        MC "Okay. Let’s do some work! It should be easy."
        $ clickable = True
        hide screen bob_desk_scr
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        jump bob_deskwork_label
    else:
        MC "Tomorrow there will probably be more work."
        $ clickable = True
        jump bob_desk_label