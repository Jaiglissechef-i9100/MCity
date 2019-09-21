default LiR1_climbing = False
screen a_home_outside_N_scr:
    key "hide_windows" action NullAction()

    if not "img35_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 835
            ypos 258
            focus_mask True
            idle "images/secret_gallery/Bonus/B35b.png"
            hover "images/secret_gallery/Bonus/B35b_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img35_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 452
        ypos 193
        focus_mask True
        idle "/images/a_home/outside/Entrance/N/B1.png"
        hover "/images/a_home/outside/Entrance/N/B1_hover.png"

        if clickable == True:
            if Li_key1 in inventory.items:
                action [Hide("displayTextScreen"),Jump("a_living_M1_locked")]
            else:
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("a_living_M1_locked")]
            hovered Show("displayTextScreen", displayText = __("Enter House"))
        unhovered Hide("displayTextScreen")
    if LiR1_NS5 == True:
        imagebutton:
            xpos 452
            ypos 193
            focus_mask True
            idle "/images/a_home/outside/Entrance/N/B1.png"
            hover "/images/a_home/outside/Entrance/N/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("LiR1_NS5_label")]
            hovered Show("displayTextScreen", displayText = __("Enter House"))
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1077
        ypos 451
        focus_mask True
        if a_pool_empty == True:
            idle "/images/a_home/outside/Entrance/N/B2.png"
            hover "/images/a_home/outside/Entrance/N/B2_hover.png"
        if a_pool_empty == False:
            idle "/images/a_home/outside/Entrance/N/B2a.png"
            hover "/images/a_home/outside/Entrance/N/B2a_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Pool"))
            action [Hide("displayTextScreen"),Jump("a_pool_M1")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1423
        ypos 353
        focus_mask True
        idle "/images/a_home/outside/Entrance/N/B3.png"
        hover "/images/a_home/outside/Entrance/N/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Garage")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("a_garage_M1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1577
        ypos 352
        focus_mask True
        idle "/images/a_home/outside/Entrance/N/B4.png"
        hover "/images/a_home/outside/Entrance/N/B4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Garage")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("a_garage_M1")]
            unhovered Hide("displayTextScreen")

    if LiR1_climbing == True and LiR1_NS5 == False:
        imagebutton:
            xpos 888
            ypos 292
            focus_mask True
            idle "/images/a_home/outside/Entrance/N/Climb_Icon.png"
            hover "/images/a_home/outside/Entrance/N/Climb_Icon_hover.png"
            if clickable == True:

                action [Hide("displayTextScreen"),Jump("Climbing_start0")]
            hovered Show("displayTextScreen", displayText = __("Climb"))
            unhovered Hide("displayTextScreen")
