screen b_house_bedroom_N_scr:

    add "images/Beach/Beach_House/Bedroom/N/map.jpg"

    imagebutton:
        xpos 279
        ypos 155
        focus_mask True
        idle "images/Beach/Beach_House/Bedroom/N/B1.png"
        hover "images/Beach/Beach_House/Bedroom/N/B1_hover.png"
        if clickable == True and  can_b_living_room == True:
            action [Hide("displayTextScreen"),Play("sound", "sfx/door_open.mp3"),Jump("b_house_living_M1")]
        hovered Show("displayTextScreen", displayText = "Living Room")
        unhovered Hide("displayTextScreen")
    if not "img37_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1299
            ypos 85
            focus_mask True
            idle "images/secret_gallery/Bonus/B37b.png"
            hover "images/secret_gallery/Bonus/B37b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img37_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if MLR3_b_house_wait > 1:
        imagebutton:
            xpos 1240
            ypos 191
            focus_mask True
            idle "images/Beach/Beach_House/Bedroom/N/B2.png"
            hover "images/Beach/Beach_House/Bedroom/N/B2_hover.png"
            if clickable == True and MLR3_b_house_wait == 2:
                action [Hide("displayTextScreen"),Play("sound", "sfx/door_open.mp3"),Jump("MLR3_b_house_wait")]
            if clickable == True and MLR3_b_house_wait > 2:
                action [Hide("displayTextScreen"),Play("sound", "sfx/door_open.mp3"),Jump("b_house_bath_M1")]
            hovered Show("displayTextScreen", displayText = "Bathroom")
            unhovered Hide("displayTextScreen")

    if MLR3_b_house_bag == 1:
        imagebutton:
            xpos 947
            ypos 501
            focus_mask True
            idle "images/Beach/Beach_House/Bedroom/N/B3.png"
            hover "images/Beach/Beach_House/Bedroom/N/B3_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),SetVariable("MLR3_b_house_bag", MLR3_b_house_bag +1), Jump("MLR3_b_house_bag")]
            hovered Show("displayTextScreen", displayText = "Put the Bag")
            unhovered Hide("displayTextScreen")

    if MLR3_b_house_bag > 1:
        imagebutton:
            xpos 947
            ypos 501
            focus_mask True
            idle "images/Beach/Beach_House/Bedroom/N/B4.png"
    if MLR3_b_house_bag == 3 and MLR3_b_house_wait == 1:
        imagebutton:
            xpos 601
            ypos 670
            focus_mask True
            idle "images/Beach/Beach_House/Bedroom/N/B5.png"
            hover "images/Beach/Beach_House/Bedroom/N/B5_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_b_house_wait")]
            hovered Show("displayTextScreen", displayText = "Bed")
            unhovered Hide("displayTextScreen")