screen entrace1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/Entrance_door_morning_idle.png"
        hover "images/home/entrace1/morning/Entrance_door_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Enter House"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/entrance_path_morning_idle.png"
        hover "images/home/entrace1/morning/entrance_path_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Entrance"))
        if clickable == True:
            action [Jump("entrance2_day1")]
        unhovered Hide("displayTextScreen")

    if not "img3_home_entrance_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1843
                ypos 607
                focus_mask True
                idle "images/secret_gallery/Bonus/EntranceHouse SecretCard.png"
                hover "images/secret_gallery/Bonus/EntranceHouse SecretCard_hover.png"
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
                action [Hide("displayTextScreen"), addgimage("img3_home_entrance_card") ,Jump("home_entrance_card")]
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                unhovered Hide("displayTextScreen")

