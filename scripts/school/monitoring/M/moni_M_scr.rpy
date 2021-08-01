screen moni_M_scr:
    imagebutton:
        xpos 1039
        ypos 425
        focus_mask True
        idle "/images/CeR2/monitoring/B1.png"
        hover "/images/CeR2/monitoring/B1_hover.png"
        hovered Show("displayTextScreen", displayText = __("Security"))
        if clickable == True and CeR2_moni < 4:
            action [Hide("displayTextScreen"), Jump("CeR2_moni_lab")]
            unhovered Hide("displayTextScreen")
    if not "img43_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1072
                ypos 235
                focus_mask True
                idle "images/secret_gallery/Bonus/B43a.png"
                hover "images/secret_gallery/Bonus/B43a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img43_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1072
                ypos 235
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img43_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img44_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1717
                ypos 797
                focus_mask True
                idle "images/secret_gallery/Bonus/B44a.png"
                hover "images/secret_gallery/Bonus/B44a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img44_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1717
                ypos 797
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img44_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img45_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 767
                ypos 681
                focus_mask True
                idle "images/secret_gallery/Bonus/B45a.png"
                hover "images/secret_gallery/Bonus/B45a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img45_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 767
                ypos 681
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img45_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor2_morning1")]

