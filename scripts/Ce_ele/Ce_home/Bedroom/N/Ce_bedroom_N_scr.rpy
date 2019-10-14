screen Ce_bedroom_N_scr:

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
            idle "images/secret_gallery/Bonus/B53c.png"
            hover "images/secret_gallery/Bonus/B53c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img53_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img54_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1354
            ypos 566
            focus_mask True
            idle "images/secret_gallery/Bonus/B54c.png"
            hover "images/secret_gallery/Bonus/B54c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img54_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img55_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1885
            ypos 723
            focus_mask True
            idle "images/secret_gallery/Bonus/B55c.png"
            hover "images/secret_gallery/Bonus/B55c_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img55_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 825
        ypos 167
        focus_mask True
        idle "/images/Ce_ele/Ce_home/Bedroom/N/B1.png"
        hover "/images/Ce_ele/Ce_home/Bedroom/N/B1_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"),Jump("Ce_corridor2_M1")]

        hovered Show("displayTextScreen", displayText = "Corridor")
        unhovered Hide("displayTextScreen")

    if CeR2_NS2 == False:
        imagebutton:
            xpos 869
            ypos 379
            focus_mask True
            idle "images/CeR2/NV/Celia.png"
            hover "images/CeR2/NV/Celia_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("Ce_NV_lab")]

            hovered Show("displayTextScreen", displayText = "Celia")
            unhovered Hide("displayTextScreen")