screen Ce_bedroom_M_scr:

    if not "img52_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 118
            ypos 704
            focus_mask True
            idle "images/secret_gallery/Bonus/B52a.png"
            hover "images/secret_gallery/Bonus/B52a_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img52_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img53_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1030
            ypos 407
            focus_mask True
            idle "images/secret_gallery/Bonus/B53a.png"
            hover "images/secret_gallery/Bonus/B53a_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img53_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img54_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1354
            ypos 566
            focus_mask True
            idle "images/secret_gallery/Bonus/B54a.png"
            hover "images/secret_gallery/Bonus/B54a_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img54_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img55_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1885
            ypos 723
            focus_mask True
            idle "images/secret_gallery/Bonus/B55a.png"
            hover "images/secret_gallery/Bonus/B55a_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img55_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 825
        ypos 167
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Bedroom/M/B1.png"
        hover "/images/Ce_ele/Ce_home/Bedroom/M/B1_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_corridor2_M1")]

        hovered Show("displayTextScreen", displayText = "Corridor")
        unhovered Hide("displayTextScreen")