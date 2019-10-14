screen entrance2_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrance2/morning/garage_door_morning_idle.png"
        hover "images/home/entrance2/morning/garage_door_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Garage")
        action [Play ("sound", "sfx/garage door.mp3"),Jump("garage_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrance2/morning/door1_morning_idle.png"
        hover "images/home/entrance2/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Kitchen")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("entrace1_evening1")]


    if not "img2_garage_entrance_card" in gallery_photos.storage:
        imagebutton:
            xpos 53
            ypos 543
            focus_mask True
            idle "images/secret_gallery/Bonus/GarageEntranceOutsideSecretCard.png"
            hover "images/secret_gallery/Bonus/GarageEntranceOutsideSecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img2_garage_entrance_card") ,Jump("garage_entrance_card")]
            hovered Show("displayTextScreen", displayText = "Secret Card")
            unhovered Hide("displayTextScreen")