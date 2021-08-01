screen a_garage_D_scr:
    key "hide_windows" action NullAction()

    imagebutton:
        xpos 994
        ypos 329
        focus_mask True
        idle "/images/a_home/outside/Garage/M/B1.png"
        hover "/images/a_home/outside/Garage/M/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Car"))
            action [Hide("displayTextScreen"),Jump("Li_car_label")]
            unhovered Hide("displayTextScreen")

    if not Li_clean_stuff in inventory.items:
        imagebutton:
            xpos 0
            ypos 327
            focus_mask True
            idle "/images/a_home/outside/Garage/M/Li_cs_B1.png"
            hover "/images/a_home/outside/Garage/M/Li_cs_B1_hover.png"
            if clickable == True and LiR1_poll_minigame == True:
                hovered Show("displayTextScreen", displayText = __("Cleaning Stuff"))
                action [Hide("displayTextScreen"),addItem(Li_clean_stuff)]
                unhovered Hide("displayTextScreen")

    if not "img28_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 414
            ypos 346
            focus_mask True
            idle "images/secret_gallery/Bonus/B28a.png"
            hover "images/secret_gallery/Bonus/B28a_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                action [Hide("displayTextScreen"),addgimage("img28_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if not "img29_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1900
                ypos 390
                focus_mask True
                idle "images/secret_gallery/Bonus/B29a.png"
                hover "images/secret_gallery/Bonus/B29a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img29_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1900
                ypos 390
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img29_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            if from_a_pool == False:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/garage door.mp3"),Jump("a_home_outside_M1")]
            else:
                action [Hide("displayTextScreen"),Play ("sound", "sfx/garage door.mp3"),Jump("a_pool_M1")]

