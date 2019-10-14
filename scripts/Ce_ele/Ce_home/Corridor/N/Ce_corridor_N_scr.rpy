screen Ce_corridor_N_scr:

    imagebutton:
        xpos 214
        ypos 0
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/N/B1.png"
        hover "/images/Ce_ele/Ce_home/corridor/N/B1_hover.png"

        if clickable == True:
            if CeR2_NS2 >= 3 and CeR2_NS2 < 6:
                action [Hide("displayTextScreen"),Jump("CeR2_NS2_bath_lab")]
            else:
                action [Play ("sound", "sfx/door_open.mp3"), Jump("Ce_bathroom_M1")]

        hovered Show("displayTextScreen", displayText = "Bathroom")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1179
        ypos 34
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/N/B2.png"
        hover "/images/Ce_ele/Ce_home/corridor/N/B2_hover.png"
        if clickable == True:
            action Show("Ce_corridor_N_painting")

        hovered Show("displayTextScreen", displayText = "Painting")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1641
        ypos 0
        focus_mask True
        idle "/images/Ce_ele/Ce_home/corridor/N/B3.png"
        hover "/images/Ce_ele/Ce_home/corridor/N/B3_hover.png"

        if clickable == True:
            action [Hide("displayTextScreen"), Jump("Ce_corridor2_M1")]

        hovered Show("displayTextScreen", displayText = "Corridor")
        unhovered Hide("displayTextScreen")

    if not "img56_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1358
            ypos 1046
            focus_mask True
            idle "images/secret_gallery/Bonus/B56c.png"
            hover "images/secret_gallery/Bonus/B56c_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img56_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img57_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1429
            ypos 1057
            focus_mask True
            idle "images/secret_gallery/Bonus/B57c.png"
            hover "images/secret_gallery/Bonus/B57c_hover.png"
            if clickable == True:
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

screen Ce_corridor_N_painting:
    zorder 102
    add "/images/Ce_ele/Ce_home/corridor/N/2.jpg"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action Hide("Ce_corridor_N_painting")