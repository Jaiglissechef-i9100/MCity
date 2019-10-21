screen a_pool_E_scr:
    key "hide_windows" action NullAction()
    if not "img33_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 0
                ypos 918
                focus_mask True
                idle "images/secret_gallery/Bonus/B33b.png"
                hover "images/secret_gallery/Bonus/B33b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img33_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 0
                ypos 918
                focus_mask True
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img33_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1632
        ypos 240
        focus_mask True
        idle "/images/a_home/outside/Pool/E/B1.png"
        hover "/images/a_home/outside/Pool/E/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Garage")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("a_garage_M1")]
            unhovered Hide("displayTextScreen")

    if Li_clean_stuff in inventory.items and LiR1_poll_minigame == True:
        imagebutton:
            xpos 700
            ypos 467
            focus_mask True
            idle Transform("/images/a_home/outside/Garage/M/Li_cs_B1_hover.png",zoom = 0.5)
            hover Transform("/images/a_home/outside/Garage/M/Li_cs_B1.png",zoom = 0.5)
            if clickable == True and Li_clean_stuff.selected:
                action [Hide("displayTextScreen"),Jump("pool_minigame_start0")]

            if clickable == True and Li_clean_stuff.selected == False:
                action [Hide("displayTextScreen"),Jump("pool_minigame_not_selected")]

                hovered Show("displayTextScreen", displayText = __("Start Pool Cleaning"))
                unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("a_home_outside_M1")]
