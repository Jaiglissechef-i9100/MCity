screen entrance2_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrance2/night/garage_door_night_idle.png"
        hover "images/home/entrance2/night/garage_door_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Garage")
        action [Play ("sound", "sfx/garage door.mp3"),Jump("garage_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrance2/night/door1_night_idle.png"
        hover "images/home/entrance2/night/door1_night_hover.png"
        hovered Show("displayTextScreen", displayText = __("Kitchen"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("entrace_night1")]

    if SR2_NS3 == True and Sara_points == 2:
        imagebutton:
            xpos 362
            ypos 430
            focus_mask True
            idle "images/home/entrance2/night/scenes/SR2_NS3/B1.png"
            hover "images/home/entrance2/night/scenes/SR2_NS3/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Sara")
            action [Hide("displayTextScreen"),Jump("SR2_NS3_label")]
            unhovered Hide("displayTextScreen")

    if not "img2_garage_entrance_card" in gallery_photos.storage:
        imagebutton:
            xpos 53
            ypos 543
            focus_mask True
            idle "images/secret_gallery/Bonus/GarageEntranceOutsideSecretCard.png"
            hover "images/secret_gallery/Bonus/GarageEntranceOutsideSecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img2_garage_entrance_card") ,Jump("garage_entrance_card")]
            hovered Show("displayTextScreen", displayText = __("Secret Card"))
            unhovered Hide("displayTextScreen")
