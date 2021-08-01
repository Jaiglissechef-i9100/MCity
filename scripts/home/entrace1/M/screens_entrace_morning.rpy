screen entrace1_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/Entrance_door_morning_idle.png"
        hover "images/home/entrace1/morning/Entrance_door_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Enter House"))
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/entrance_path_morning_idle.png"
        hover "images/home/entrace1/morning/entrance_path_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Entrance"))
        if clickable == True:
            action [Jump("entrance2_morning1")]
            unhovered Hide("displayTextScreen")

    if not "img3_home_entrance_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1843
                ypos 607
                focus_mask True
                idle "images/secret_gallery/Bonus/EntranceHouse SecretCard.png"
                hover "images/secret_gallery/Bonus/EntranceHouse SecretCard_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"), addgimage("img3_home_entrance_card") ,Jump("home_entrance_card")]
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1843
                ypos 607
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"), addgimage("img3_home_entrance_card") ,Jump("home_entrance_card")]
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    unhovered Hide("displayTextScreen")

    if CR3_MS2 == True and Caroline_points == 3 and CR3_deal_aff == True and CR3_MS2_can3 == True:
        imagebutton:
            xpos 708
            ypos 435
            focus_mask True
            idle "images/home/entrace1/morning/CR3_MS2_b1.png"
            hover "images/home/entrace1/morning/CR3_MS2_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("CR3_MS2_label")]
                unhovered Hide("displayTextScreen")

