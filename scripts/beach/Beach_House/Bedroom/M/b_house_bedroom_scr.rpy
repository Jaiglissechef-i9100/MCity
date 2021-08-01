

screen b_house_bedroom_M_scr:

    add "images/Beach/Beach_House/Bedroom/M/map.jpg"

    imagebutton:
        xpos 278
        ypos 145
        focus_mask True
        idle "images/Beach/Beach_House/Bedroom/M/B1.png"
        hover "images/Beach/Beach_House/Bedroom/M/B1_hover.png"
        if clickable == True:
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_living_M1")]
            hovered Show("displayTextScreen", displayText = "Living Room")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1235
        ypos 184
        focus_mask True
        idle "images/Beach/Beach_House/Bedroom/M/B2.png"
        hover "images/Beach/Beach_House/Bedroom/M/B2_hover.png"
        if clickable == True:
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_bath_M1")]
            hovered Show("displayTextScreen", displayText = "Bathroom")
            unhovered Hide("displayTextScreen")

    if not "img37_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1299
            ypos 85
            focus_mask True
            idle "images/secret_gallery/Bonus/B37a.png"
            hover "images/secret_gallery/Bonus/B37a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img37_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                unhovered Hide("displayTextScreen")