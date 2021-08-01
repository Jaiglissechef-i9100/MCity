screen classroom1_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 485
        ypos 162
        focus_mask True
        idle "images/school/classroom1/morning/door1_morning_idle.png"
        hover "images/school/classroom1/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "School Corridor")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_morning1")]
            unhovered Hide("displayTextScreen")

    if not "img8_mc_classroom_card" in gallery_photos.storage:
        imagebutton:
            xpos 1893
            ypos 1039
            focus_mask True
            idle "images/secret_gallery/Bonus/MCClassroom Card.png"
            hover "images/secret_gallery/Bonus/MCClassroom Card_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), addgimage("img8_mc_classroom_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if celia_school_morning_scene2v1 == 1:
        imagebutton:
            xpos 1322
            ypos 224
            focus_mask True
            idle "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/Celia_b2.png"
            hover "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/Celia_b2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Celia")
                action [Hide("displayTextScreen"),Jump("celia_school_morning_scene2v1_label")]
                unhovered Hide("displayTextScreen")
    if macy_classroom1_morning_scene1 == True:
        imagebutton:
            xpos 333
            ypos 412
            focus_mask True
            idle "images/school/classroom1/morning/scenes/macy_scene1/macy_b1.png"
            hover "images/school/classroom1/morning/scenes/macy_scene1/macy_b1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Macy")
                action [Hide("displayTextScreen"),Jump("macy_scene1_label")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 788
        ypos 689
        focus_mask True
        idle "images/school/classroom1/morning/deskb1.png"
        hover "images/school/classroom1/morning/deskb1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Desk")
            action [Hide("displayTextScreen"),Jump("Deskb1_label")]
            unhovered Hide("displayTextScreen")


screen classroom1_morning_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 485
        ypos 162
        focus_mask True
        idle "images/school/classroom1/morning/door1_morning_idle.png"


    if not "img8_mc_classroom_card" in gallery_photos.storage:
        imagebutton:
            xpos 1893
            ypos 1039
            focus_mask True
            idle "images/secret_gallery/Bonus/MCClassroom Card.png"

    if celia_school_morning_scene2v1 == 1:
        imagebutton:
            xpos 1322
            ypos 224
            focus_mask True
            idle "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/Celia_b2.png"

    if macy_classroom1_morning_scene1 == True:
        imagebutton:
            xpos 333
            ypos 412
            focus_mask True
            idle "images/school/classroom1/morning/scenes/macy_scene1/macy_b1.png"
    imagebutton:
        xpos 788
        ypos 689
        focus_mask True
        idle "images/school/classroom1/morning/deskb1.png"