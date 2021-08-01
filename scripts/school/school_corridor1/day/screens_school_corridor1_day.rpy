screen school_corridor1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_corridor1/morning/door1_morning_idle.png"
        hover "images/school/school_corridor1/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("My Classroom"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("classroom1_day1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 645
        ypos 274
        focus_mask True
        idle "images/school/school_corridor1/morning/door2_morning_idle.png"
        hover "images/school/school_corridor1/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Toilets"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("toilets_day1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 772
        ypos 203
        focus_mask True
        idle "images/school/school_corridor1/morning/door3_morning_idle.png"
        hover "images/school/school_corridor1/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Floor 1"))
        if clickable == True:
            action [Jump("school_corridor3_day1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 881
        ypos 371
        focus_mask True
        idle "images/school/school_corridor1/morning/door4_morning_idle.png"
        hover "images/school/school_corridor1/morning/door4_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Pool"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("pool_day1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1130
        ypos 205
        focus_mask True
        idle "images/school/school_corridor1/morning/door5_morning_idle.png"
        hover "images/school/school_corridor1/morning/door5_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Corridor"))
        if clickable == True:
            action [Jump("school_corridor2_day1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1464
        ypos 89
        focus_mask True
        idle "images/school/school_corridor1/morning/door7_morning_idle.png"
        hover "images/school/school_corridor1/morning/door7_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Sara's Classroom"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("classroom2_day1")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_entrance_day1")]

    if corridor1_door_to_teacher_room2_open == False and celia_key_take==True:
        if celia_key.selected:
            imagebutton:
                xpos 1251
                ypos 273
                focus_mask True
                idle "images/school/school_corridor1/morning/door6_morning_idle.png"
                hover "images/school/school_corridor1/morning/door6_morning_hover.png"
                hovered Show("displayTextScreen", displayText = __("Teacher’s Break Room(Closed)"))
                if clickable == True:
                    action [Play ("sound", "sfx/door_open.mp3"),dropItem(celia_key),SetVariable("corridor1_door_to_teacher_room2_open", True),SetVariable("celia_key_take", False), Jump("teacher_room2_day1")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1251
                ypos 273
                focus_mask True
                idle "images/school/school_corridor1/morning/door6_morning_idle.png"
                hover "images/school/school_corridor1/morning/door6_morning_hover.png"
                hovered Show("displayTextScreen", displayText = __("Teacher’s Break Room(Closed)"))
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
            hovered Show("displayTextScreen", displayText = __("Teacher’s Break Room"))
            if clickable == True:
                action [Play ("sound", "sfx/door_open.mp3"),SetVariable("celia_key_take", False),Jump("teacher_room2_day1")]
                unhovered Hide("displayTextScreen")

    if not "img7_school_corridor1_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1075
                ypos 576
                focus_mask True
                idle "images/secret_gallery/Bonus/SchoolCorridor1 Card.png"
                hover "images/secret_gallery/Bonus/SchoolCorridor1 Card_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"), addgimage("img7_school_corridor1_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1075
                ypos 576
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"), addgimage("img7_school_corridor1_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

