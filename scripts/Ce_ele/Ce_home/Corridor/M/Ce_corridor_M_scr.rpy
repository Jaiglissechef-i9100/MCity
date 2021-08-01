screen Ce_corridor_M_scr:

    imagebutton:
        xpos 214
        ypos 0
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/M/B1.png"
        hover "/images/Ce_ele/Ce_home/corridor/M/B1_hover.png"

        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_bathroom_M1")]

        hovered Show("displayTextScreen", displayText = __("Bathroom"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1179
        ypos 34
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/M/B2.png"
        hover "/images/Ce_ele/Ce_home/corridor/M/B2_hover.png"
        if clickable == True:
            action Show("Ce_corridor_M_painting")

        hovered Show("displayTextScreen", displayText = __("Painting"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1641
        ypos 0
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/M/B3.png"
        hover "/images/Ce_ele/Ce_home/corridor/M/B3_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Jump("Ce_corridor2_M1")]

        hovered Show("displayTextScreen", displayText = __("Corridor"))
        unhovered Hide("displayTextScreen")

    if not "img56_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1358
                ypos 1046
                focus_mask True
                idle "images/secret_gallery/Bonus/B56a.png"
                hover "images/secret_gallery/Bonus/B56a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img56_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1358
                ypos 1046
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img56_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img57_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1429
                ypos 1057
                focus_mask True
                idle "images/secret_gallery/Bonus/B57a.png"
                hover "images/secret_gallery/Bonus/B57a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img57_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1429
                ypos 1057
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img57_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Hide("displayTextScreen"),Jump("Ce_entrance_M1")]

screen Ce_corridor_M_painting:
    zorder 102
    modal True
    add "/images/Ce_ele/Ce_home/corridor/M/2.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action Hide("Ce_corridor_M_painting")

