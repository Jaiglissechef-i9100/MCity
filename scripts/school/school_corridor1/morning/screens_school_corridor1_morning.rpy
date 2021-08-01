screen school_corridor1_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_corridor1/morning/door1_morning_idle.png"
        hover "images/school/school_corridor1/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "My Classroom")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("classroom1_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 645
        ypos 274
        focus_mask True
        idle "images/school/school_corridor1/morning/door2_morning_idle.png"
        hover "images/school/school_corridor1/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Toilets")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("toilets_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 772
        ypos 203
        focus_mask True
        idle "images/school/school_corridor1/morning/door3_morning_idle.png"
        hover "images/school/school_corridor1/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Floor 1")
        if clickable == True:
            clicked Jump("school_corridor3_morning1")
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 881
        ypos 371
        focus_mask True
        idle "images/school/school_corridor1/morning/door4_morning_idle.png"
        hover "images/school/school_corridor1/morning/door4_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Pool")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("pool_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1130
        ypos 205
        focus_mask True
        idle "images/school/school_corridor1/morning/door5_morning_idle.png"
        hover "images/school/school_corridor1/morning/door5_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Corridor")
        if clickable == True:
            clicked Jump("school_corridor2_morning1")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1464
        ypos 89
        focus_mask True
        idle "images/school/school_corridor1/morning/door7_morning_idle.png"
        hover "images/school/school_corridor1/morning/door7_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Sara's Classroom")
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("classroom2_morning1")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_entrance_morning1")]


    if corridor1_door_to_teacher_room2_open == False:
        if celia_key.selected and celia_key_take==True:
            imagebutton:
                xpos 1251
                ypos 273
                focus_mask True
                idle "images/school/school_corridor1/morning/door6_morning_idle.png"
                hover "images/school/school_corridor1/morning/door6_morning_hover.png"
                hovered Show("displayTextScreen", displayText = "Teacher’s Break Room(Closed)")
                if clickable == True:
                    action [Play ("sound", "sfx/door_open.mp3"),dropItem(celia_key),SetVariable("corridor1_door_to_teacher_room2_open", True),SetVariable("celia_key_take", False), Jump("teacher_room2_morning1")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1251
                ypos 273
                focus_mask True
                idle "images/school/school_corridor1/morning/door6_morning_idle.png"
                hover "images/school/school_corridor1/morning/door6_morning_hover.png"
                hovered Show("displayTextScreen", displayText = "Teacher’s Break Room(Closed)")
                if clickable == True:
                    action [Play ("sound", "sfx/door_locked.mp3")]
                    unhovered Hide("displayTextScreen")
    if corridor1_door_to_teacher_room2_open == True:
        imagebutton:
            xpos 1251
            ypos 273
            focus_mask True
            idle "images/school/school_corridor1/morning/door6_morning_idle.png"
            hover "images/school/school_corridor1/morning/door6_morning_hover.png"
            hovered Show("displayTextScreen", displayText = "Teacher’s Break Room")
            if clickable == True:
                action [Play ("sound", "sfx/door_open.mp3"),SetVariable("celia_key_take", False),Jump("teacher_room2_morning1")]
                unhovered Hide("displayTextScreen")

    if not "img7_school_corridor1_card" in gallery_photos.storage:
        imagebutton:
            xpos 1075
            ypos 576
            focus_mask True
            idle "images/secret_gallery/Bonus/SchoolCorridor1 Card.png"
            hover "images/secret_gallery/Bonus/SchoolCorridor1 Card_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), addgimage("img7_school_corridor1_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")