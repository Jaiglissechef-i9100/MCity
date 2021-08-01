screen bob_office_D_scr:

    imagebutton:
        xpos 935
        ypos 219
        focus_mask True
        idle "images/Bob_work/office/M/B3.png"
        hover "images/Bob_work/office/M/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Statue"))
            action [Hide("displayTextScreen"),Jump("bob_statue_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 176
        ypos 45
        focus_mask True
        idle "images/Bob_work/office/M/B4.png"
        hover "images/Bob_work/office/M/B4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Fire Place"))
            action [Hide("displayTextScreen"),Jump("bob_fireplace_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1583
        ypos 402
        focus_mask True
        idle "images/Bob_work/office/M/B5.png"
        hover "images/Bob_work/office/M/B5_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Table"))
            action [Hide("displayTextScreen"),Jump("bob_tableR_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1146
        ypos 375
        focus_mask True
        idle "images/Bob_work/office/M/B6.png"
        hover "images/Bob_work/office/M/B6_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Table"))
            action [Hide("displayTextScreen"),Jump("bob_tableL_label")]
            unhovered Hide("displayTextScreen")

    if zuri_magentcard in inventory.items and Bob_work_minigame == True:
        imagebutton:
            xpos 27
            ypos 346
            focus_mask True
            idle "images/Bob_work/office/M/B7.png"
            hover "images/Bob_work/office/M/B7_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Sit on Chair"))
                action [Hide("displayTextScreen"),Jump("bob_desk_label")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 722
        ypos 127
        focus_mask True
        idle "images/Bob_work/office/M/B8.png"
        hover "images/Bob_work/office/M/B8_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Bookcase"))
            action [Hide("displayTextScreen"),Jump("bob_shelf_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 413
        ypos 414
        focus_mask True
        idle "images/Bob_work/office/M/B9.png"
        hover "images/Bob_work/office/M/B9_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Red Statue"))
            action [Hide("displayTextScreen"),Jump("bob_redstatue_label")]
            unhovered Hide("displayTextScreen")

    if not "img14_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 85
                ypos 152
                focus_mask True
                idle "images/secret_gallery/Bonus/B14.png"
                hover "images/secret_gallery/Bonus/B14_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img14_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 85
                ypos 152
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img14_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img15_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 9
                ypos 781
                focus_mask True
                idle "images/secret_gallery/Bonus/B15.png"
                hover "images/secret_gallery/Bonus/B15_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img15_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 9
                ypos 781
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img15_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("office_leave")]

