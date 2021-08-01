screen pool_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/pool/morning/door1_morning_idle.png"
        hover "images/school/pool/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "School Corridor")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_morning1")]
        unhovered Hide("displayTextScreen")
    if delilah_scene1 == True:
        imagebutton:
            xpos 597
            ypos 454
            focus_mask True
            idle "images/school/pool/morning/scenes/delilah_scene1/delilah_b1.png"
            hover "images/school/pool/morning/scenes/delilah_scene1/delilah_b1_hover.png"
            if delilah_work_inprogress == True:
                hovered Show("displayTextScreen", displayText = "Delilah")
            if delilah_work_inprogress == False:
                hovered Show("displayTextScreen", displayText = "???")
            action [Hide("displayTextScreen"),Jump("delilah_scene1_label")]
            unhovered Hide("displayTextScreen")

screen pool_morning_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/pool/morning/door1_morning_idle.png"

    if delilah_scene1 == True:
        imagebutton:
            xpos 597
            ypos 454
            focus_mask True
            idle "images/school/pool/morning/scenes/delilah_scene1/delilah_b1.png"
            hover "images/school/pool/morning/scenes/delilah_scene1/delilah_b1_hover.png"