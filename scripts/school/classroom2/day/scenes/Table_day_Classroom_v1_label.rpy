image Table_day_Classroom_v1_p1 = "images/school/classroom2/day/scenes/Table_Classroom_v1/RenPy2.jpg"

label Table_day_Classroom_v1_label:

    hide screen map_button
    scene Table_day_Classroom_v1_p1
    call screen Table_day_Classroom_v1

label Table_day_Classroom_exams_v1_label:

    hide screen map_button
    $ clickable = False
    show screen Table_day_Classroom_v1
    scene Table_day_Classroom_v1_p1
    MC "Our exams… I better leave it alone."
    $ clickable = True
    jump Table_day_Classroom_v1_label

label Table_day_Classroom_books_v1_label:

    hide screen map_button
    $ clickable = False
    show screen Table_day_Classroom_v1
    scene Table_day_Classroom_v1_p1
    MC "Just some random books."
    $ clickable = True
    jump Table_day_Classroom_v1_label

screen Table_day_Classroom_v1:
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("Table_day_Classroom_v1"),Jump("classroom2_morning1")]

    imagebutton:
        xpos 1423
        ypos 141
        focus_mask True
        idle "images/school/classroom2/day/scenes/Table_Classroom_v1/exams_b1.png"
        hover "images/school/classroom2/day/scenes/Table_Classroom_v1/exams_b1_hover.png"
        hovered Show("displayTextScreen", displayText = __("Exams"))
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("Table_day_Classroom_exams_v1_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1087
        ypos 215
        focus_mask True
        idle "images/school/classroom2/day/scenes/Table_Classroom_v1/books_b2.png"
        hover "images/school/classroom2/day/scenes/Table_Classroom_v1/books_b2_hover.png"
        hovered Show("displayTextScreen", displayText = __("Books"))
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("Table_day_Classroom_books_v1_label")]
            unhovered Hide("displayTextScreen")

    if celia_key not in inventory.items and celia_key_take == True:
        imagebutton:
            xpos 515
            ypos 370
            focus_mask True
            idle "images/school/classroom2/day/scenes/Table_Classroom_v1/Celia_key_b3.png"
            hover "images/school/classroom2/day/scenes/Table_Classroom_v1/Celia_key_b3_hover.png"
            hovered Show("displayTextScreen", displayText = __("Teacher’s Break Room Key"))
            if clickable == True:
                action [Hide("displayTextScreen"),addItem(celia_key),Jump("Table_day_Classroom_v1_label")]
                unhovered Hide("displayTextScreen")
