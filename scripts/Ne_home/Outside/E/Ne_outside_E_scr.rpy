default Ne_ladder = 1

screen Ne_outside_E_scr:

    if Ne_ladder == 1:
        add "images/Ne_1/Map/Outside/E.jpg"
        imagebutton:
            xpos 200
            ypos 389
            focus_mask True
            idle "images/Ne_1/Map/Outside/B1_E.png"
            hover "images/Ne_1/Map/Outside/B1_E_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), SetVariable("Ne_ladder", 2)]

            hovered Show("displayTextScreen", displayText = "Ladder")
            unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 722
            ypos 103
            focus_mask True
            idle "images/Ne_1/Map/Outside/B2_E.png"
            hover "images/Ne_1/Map/Outside/B2_E_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_ES1_door")]

            hovered Show("displayTextScreen", displayText = "Doors")
            unhovered Hide("displayTextScreen")

    if Ne_ladder == 2:
        add "images/Ne_1/Map/Outside/E2.jpg"


        imagebutton:
            xpos 722
            ypos 103
            focus_mask True
            idle "images/Ne_1/Map/Outside/B2_E.png"
            hover "images/Ne_1/Map/Outside/B2_E_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_ES1_door2")]

            hovered Show("displayTextScreen", displayText = "Doors")
            unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 1042
            ypos 0
            focus_mask True
            idle "images/Ne_1/Map/Outside/B3_E.png"
            hover "images/Ne_1/Map/Outside/B3_E_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_c_mg")]

            hovered Show("displayTextScreen", displayText = "Ladder")
            unhovered Hide("displayTextScreen")
    if not "img75_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 36
            ypos 355
            focus_mask True
            idle "images/secret_gallery/Bonus/B75b.png"
            hover "images/secret_gallery/Bonus/B75b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img75_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img76_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 708
            ypos 0
            focus_mask True
            idle "images/secret_gallery/Bonus/B76b.png"
            hover "images/secret_gallery/Bonus/B76b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img76_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img77_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1830
            ypos 151
            focus_mask True
            idle "images/secret_gallery/Bonus/B77b.png"
            hover "images/secret_gallery/Bonus/B77b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img77_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img78_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1859
            ypos 644
            focus_mask True
            idle "images/secret_gallery/Bonus/B78b.png"
            hover "images/secret_gallery/Bonus/B78b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img78_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img79_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1415
            ypos 1042
            focus_mask True
            idle "images/secret_gallery/Bonus/B79b.png"
            hover "images/secret_gallery/Bonus/B79b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img79_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")