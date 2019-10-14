

screen Ne_outside_N_scr:

    if Ne_ladder == 1:
        add "images/Ne_1/Map/Outside/N.jpg"
        imagebutton:
            xpos 230
            ypos 409
            focus_mask True
            idle "images/Ne_1/Map/Outside/B1_N.png"
            hover "images/Ne_1/Map/Outside/B1_N_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), SetVariable("Ne_ladder", 2)]

            hovered Show("displayTextScreen", displayText = "Ladder")
            unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 722
            ypos 103
            focus_mask True
            idle "images/Ne_1/Map/Outside/B2_N.png"
            hover "images/Ne_1/Map/Outside/B2_N_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_ES1_door")]

            hovered Show("displayTextScreen", displayText = "Doors")
            unhovered Hide("displayTextScreen")

    if Ne_ladder == 2:
        add "images/Ne_1/Map/Outside/N2.jpg"


        imagebutton:
            xpos 722
            ypos 103
            focus_mask True
            idle "images/Ne_1/Map/Outside/B2_N.png"
            hover "images/Ne_1/Map/Outside/B2_N_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_ES1_door2")]

            hovered Show("displayTextScreen", displayText = "Doors")
            unhovered Hide("displayTextScreen")

        imagebutton:
            xpos 1042
            ypos 0
            focus_mask True
            idle "images/Ne_1/Map/Outside/B3_N.png"
            hover "images/Ne_1/Map/Outside/B3_N_hover.png"

            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ne_c_mg")]

            hovered Show("displayTextScreen", displayText = "Ladder")
            unhovered Hide("displayTextScreen")
    if not "img75_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 36
            ypos 355
            focus_mask True
            idle "images/secret_gallery/Bonus/B75c.png"
            hover "images/secret_gallery/Bonus/B75c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img75_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img76_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 708
            ypos 0
            focus_mask True
            idle "images/secret_gallery/Bonus/B76c.png"
            hover "images/secret_gallery/Bonus/B76c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img76_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img77_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1830
            ypos 151
            focus_mask True
            idle "images/secret_gallery/Bonus/B77c.png"
            hover "images/secret_gallery/Bonus/B77c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img77_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img78_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1859
            ypos 644
            focus_mask True
            idle "images/secret_gallery/Bonus/B78c.png"
            hover "images/secret_gallery/Bonus/B78c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img78_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img79_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1415
            ypos 1042
            focus_mask True
            idle "images/secret_gallery/Bonus/B79c.png"
            hover "images/secret_gallery/Bonus/B79c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img79_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")