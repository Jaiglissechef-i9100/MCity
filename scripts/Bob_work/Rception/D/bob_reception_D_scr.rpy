screen bob_reception_D_scr:

    key "hide_windows" action NullAction()
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1444
        ypos 107
        focus_mask True
        idle "images/Bob_work/reception/M/B1.png"
        hover "images/Bob_work/reception/M/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Office"))
            if zuri_magentcard in inventory.items:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_office_M1")]
            else:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_locked.mp3"),Jump("bob_officelocked")]
            unhovered Hide("displayTextScreen")

    if Zv2_first_meet == True:
        imagebutton:
            xpos 169
            ypos 235
            focus_mask True
            idle "images/Bob_work/reception/M/scenes/Zv2_MS1/B1.png"
            hover "images/Bob_work/reception/M/scenes/Zv2_MS1/B1_hover.png"
            if clickable == True and Zv2_MS1_ask_boob_office == True:
                hovered Show("displayTextScreen", displayText = "???")
                action [Hide("displayTextScreen"),Jump("Zv2_MS1_daymeet_label")]
            if clickable == True and Zv2_MS1_ask_boob_office == False:
                hovered Show("displayTextScreen", displayText = "Zuri")
                action [Hide("displayTextScreen"),Jump("Zv2_MS1_daymeet_label")]
            unhovered Hide("displayTextScreen")

    if Zv2_MS2 == True:
        imagebutton:
            xpos 169
            ypos 235
            focus_mask True
            idle "images/Bob_work/reception/M/scenes/Zv2_MS1/B1.png"
            hover "images/Bob_work/reception/M/scenes/Zv2_MS1/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Zuri")
                action [Hide("displayTextScreen"),Jump("Zv2_MS2_label")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1075
        ypos 28
        focus_mask True
        idle "images/Bob_work/reception/M/B2.png"
        hover "images/Bob_work/reception/M/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Painting"))
            action [Hide("displayTextScreen"),Jump("bob_paintingreception_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("bob_entrance_M1")]
