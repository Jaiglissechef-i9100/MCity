screen a_home_outside_D_scr:
    key "hide_windows" action NullAction()

    if not "img35_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 835
                ypos 258
                focus_mask True
                idle "images/secret_gallery/Bonus/B35a.png"
                hover "images/secret_gallery/Bonus/B35a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img35_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 835
                ypos 258
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img35_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 452
        ypos 193
        focus_mask True
        idle "/images/a_home/outside/Entrance/M/B1.png"
        hover "/images/a_home/outside/Entrance/M/B1_hover.png"
        if clickable == True:
            if Li_door_locked == False:
                action [Play ("sound", "sfx/door_open.mp3"),Jump("a_living_M1")]
            else:
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("a_living_M1")]
            hovered Show("displayTextScreen", displayText = __("Enter House"))
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1077
        ypos 451
        focus_mask True
        if a_pool_empty == True:
            idle "/images/a_home/outside/Entrance/M/B2.png"
            hover "/images/a_home/outside/Entrance/M/B2_hover.png"
        if a_pool_empty == False:
            idle "/images/a_home/outside/Entrance/M/B2a.png"
            hover "/images/a_home/outside/Entrance/M/B2a_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Pool"))
            action [Hide("displayTextScreen"),Jump("a_pool_M1")]
            unhovered Hide("displayTextScreen")
    if LiR1_MAS6 == True:
        add "/images/a_home/outside/Pool/M/B2a.png" xpos 1076 ypos 441
    if LiR1_MAS7 == True:
        add "/images/a_home/outside/Pool/M/B3a.png" xpos 1127 ypos 430
    if LiR1_MAS8 == True:
        add "/images/a_home/outside/Pool/M/B4a.png" xpos 1075 ypos 461
    imagebutton:
        xpos 1423
        ypos 353
        focus_mask True
        idle "/images/a_home/outside/Entrance/M/B3.png"
        hover "/images/a_home/outside/Entrance/M/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Garage")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("a_garage_M1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1577
        ypos 352
        focus_mask True
        idle "/images/a_home/outside/Entrance/M/B4.png"
        hover "/images/a_home/outside/Entrance/M/B4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Garage")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("a_garage_M1")]
            unhovered Hide("displayTextScreen")

