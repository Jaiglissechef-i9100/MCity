screen b_house_living_N_scr:

    add "images/Beach/Beach_House/Living/N/map.jpg"

    imagebutton:
        xpos 422
        ypos 171
        focus_mask True
        idle "images/Beach/Beach_House/Living/N/B1.png"
        hover "images/Beach/Beach_House/Living/N/B1_hover.png"
        if clickable == True:
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_bedroom_M1")]
        hovered Show("displayTextScreen", displayText = __("Bedroom"))
        unhovered Hide("displayTextScreen")

    if clickable == True and MLR3_beach_event == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play("sound", "sfx/door_open.mp3"),Jump("beach3_M1")]

    if not "img36_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 913
                ypos 424
                focus_mask True
                idle "images/secret_gallery/Bonus/B36b.png"
                hover "images/secret_gallery/Bonus/B36b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img36_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 913
                ypos 424
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img36_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
