screen mc_room_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1158
        ypos 84
        focus_mask True
        idle "images/home/mc_room/morning/door1_morning_idle1.png"
        hover "images/home/mc_room/morning/door1_morning_hover1.png"
        hovered Show("displayTextScreen", displayText = __("Corridor"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 26
        ypos 529
        focus_mask True
        idle "images/home/mc_room/morning/bed_morning_idle1.png"
        hover "images/home/mc_room/morning/bed_morning_hover1.png"
        hovered Show("displayTextScreen", displayText = __("Bed"))
        clicked Jump("day_time_changer")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/morning/pc_idle.png"
        hover "images/home/mc_room/morning/pc_hover.png"
        hovered Show("displayTextScreen", displayText = __("Computer"))
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("computer_menu")]
        unhovered Hide("displayTextScreen")

    if not "img4_mc_room_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 23
                ypos 906
                focus_mask True
                idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
                hover "images/secret_gallery/Bonus/MCBedroom SecretCard_hover.png"
                action [Hide("displayTextScreen"), addgimage("img4_mc_room_card") ,Jump("mc_room_card")]
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 23
                ypos 906
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                action [Hide("displayTextScreen"), addgimage("img4_mc_room_card") ,Jump("mc_room_card")]
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/morning/s_gallery.png"
        hover "images/home/mc_room/morning/s_gallery_hover.png"
        hovered Show("displayTextScreen", displayText = __("Secret Gallery"))
        action [Hide("displayTextScreen"), Show("secret_gallery"),]
        unhovered Hide("displayTextScreen")

    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/morning/window_morning.png"
            hover "images/home/mc_room/morning/window_morning_hover.png"
            hovered Show("displayTextScreen", displayText = __("Window"))
            action [Hide("displayTextScreen"), Jump("neighboor_spy_v1_label"),]
            unhovered Hide("displayTextScreen")

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/morning/b1.png"
            hover "images/home/mc_room/morning/b1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Money"))
            action [Hide("displayTextScreen"), Jump("money_less10"),]
            unhovered Hide("displayTextScreen")

    if MLR3_AS3  == 3 and ml_points == 3:
        imagebutton:
            xpos 396
            ypos 299
            focus_mask True
            idle "images/home/mc_room/day/scenes/MLR3_AS3/B1.png"
            hover "images/home/mc_room/day/scenes/MLR3_AS3/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_AS3")]
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if max_r_points == True:
        imagebutton:
            xpos 1860
            ypos 120
            focus_mask True
            idle Transform("images/game_gui/Max_R_Points/7.png", zoom=.4)
            hover Transform("images/game_gui/Max_R_Points/7a.png", zoom=.4)

            action [Hide("displayTextScreen"), Show("max_r_points_menu_scr"),]
            unhovered Hide("displayTextScreen")

screen bed_images:
    if MLR3_AS3  == 3 and ml_points == 3:
        imagebutton:
            xpos 396
            ypos 299
            focus_mask True
            idle "images/home/mc_room/day/scenes/MLR3_AS3/B1.png"

screen mc_room_day_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/morning/door1_morning_idle.png"
        hover "images/home/mc_room/morning/door1_morning_hover.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/morning/bed_morning_idle.png"
        hover "images/home/mc_room/morning/bed_morning_hover.png"

    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/morning/pc_idle.png"
        hover "images/home/mc_room/morning/pc_hover.png"

    if not "img4_mc_room_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 23
                ypos 906
                focus_mask True
                idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
        else:
            imagebutton:
                xpos 23
                ypos 906
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"

    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/morning/s_gallery.png"
        hover "images/home/mc_room/morning/s_gallery_hover.png"

    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/morning/window_morning.png"
            hover "images/home/mc_room/morning/window_morning_hover.png"

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/morning/b1.png"

    if MLR3_AS3  == 3 and ml_points == 3:
        imagebutton:
            xpos 396
            ypos 299
            focus_mask True
            idle "images/home/mc_room/day/scenes/MLR3_AS3/B1.png"

    if max_r_points == True:
        imagebutton:
            xpos 1860
            ypos 120
            focus_mask True
            idle Transform("images/game_gui/Max_R_Points/7.png", zoom=.4)

