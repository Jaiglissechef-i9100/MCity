screen entrace1_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/night/Entrance_door_night_idle.png"
        hover "images/home/entrace1/night/Entrance_door_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Enter House")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/night/entrance_path_night_idle.png"
        hover "images/home/entrace1/night/entrance_path_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Entrance")
        action [Jump("entrance2_night1")]
        unhovered Hide("displayTextScreen")

    if not "img3_home_entrance_card" in gallery_photos.storage:
        imagebutton:
            xpos 1843
            ypos 607
            focus_mask True
            idle "images/secret_gallery/Bonus/EntranceHouse SecretCard.png"
            hover "images/secret_gallery/Bonus/EntranceHouse SecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img3_home_entrance_card") ,Jump("home_entrance_card")]
            hovered Show("displayTextScreen", displayText = "Secret Card")
            unhovered Hide("displayTextScreen")

    if CR2_NS2 == True and Caroline_points == 2:
        imagebutton:
            xpos 844
            ypos 336
            focus_mask True
            idle "images/home/entrace1/night/scenes/CR2_NS2/B1.png"
            hover "images/home/entrace1/night/scenes/CR2_NS2/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"),Jump("CR2_NS2_label")]
            unhovered Hide("displayTextScreen")