screen changing_room_morning:
    key "hide_windows" action NullAction()
    if not "img34_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1911
            ypos 481
            focus_mask True
            idle "images/secret_gallery/Bonus/B34a.png"
            hover "images/secret_gallery/Bonus/B34a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img34_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if Ne_MS2 >=2:

        imagebutton:
            xpos 669
            ypos 401
            focus_mask True
            idle "images/Ne_1/MS2/Isla.png"
            hover "images/Ne_1/MS2/Isla_hover.png"
            if clickable == True:
                if Isla_name == "???":
                    hovered Show("displayTextScreen", displayText = "???")
                else:
                    hovered Show("displayTextScreen", displayText = "Isla")
                action [Hide("displayTextScreen"),Jump("Ne_MS2_lab")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/changing_room/morning/door1_morning_idle.png"
        hover "images/school/changing_room/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("GYM"))
        if clickable == True:
            action Jump("gym_morning1")
            unhovered Hide("displayTextScreen")