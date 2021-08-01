screen mc_room_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/night/pc_idle.png"
        hover "images/home/mc_room/night/pc_hover.png"
        hovered Show("displayTextScreen", displayText = __("Computer"))
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("computer_menu")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1158
        ypos 84
        focus_mask True
        idle "images/home/mc_room/night/door1_night_idle1.png"
        hover "images/home/mc_room/night/door1_night_hover1.png"
        hovered Show("displayTextScreen", displayText = __("Corridor"))
        clicked [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 26
        ypos 529
        focus_mask True
        idle "images/home/mc_room/night/bed_night_idle1.png"
        hover "images/home/mc_room/night/bed_night_hover1.png"
        hovered Show("displayTextScreen", displayText = __("Bed"))
        clicked Jump("day_time_changer")
        unhovered Hide("displayTextScreen")

    if mc_sara_night_scene1_v1 == 1 and can1_mc_sara_night_scene1_v1 == True and can2_mc_sara_night_scene1_v1 == True and Sara_points == 1:
        imagebutton:
            xpos 26
            ypos 529
            focus_mask True
            idle "images/home/mc_room/night/bed_night_idle1.png"
            hover "images/home/mc_room/night/bed_night_hover1.png"
            hovered Show("displayTextScreen", displayText = __("Bed"))
            clicked [Hide("displayTextScreen"), Jump("mc_sara_night_scene1_v1_label")]
            unhovered Hide("displayTextScreen")

    if can_sms3_from_sara == 1:
        imagebutton:
            xpos 26
            ypos 529
            focus_mask True
            idle "images/home/mc_room/night/bed_night_idle1.png"
            hover "images/home/mc_room/night/bed_night_hover1.png"
            hovered Show("displayTextScreen", displayText = __("Bed"))
            clicked [Hide("displayTextScreen"), Show("sms3_from_sara")]
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
                idle "images/secret_gallery/Bonus/B28b.png"
                hover "images/secret_gallery/Bonus/B28b_hover.png"
                action [Hide("displayTextScreen"), addgimage("img4_mc_room_card") ,Jump("mc_room_card")]
                hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/night/s_gallery.png"
        hover "images/home/mc_room/night/s_gallery_hover.png"
        hovered Show("displayTextScreen", displayText = __("Secret Gallery"))
        action [Hide("displayTextScreen"), Show("secret_gallery"),]
        unhovered Hide("displayTextScreen")

    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/night/window_night.png"
            hover "images/home/mc_room/night/window_night_hover.png"
            hovered Show("displayTextScreen", displayText = __("Window"))
            action [Hide("displayTextScreen"), Jump("neighboor_spy_v1_label"),]
            unhovered Hide("displayTextScreen")

    if ml_mc_room_night_scene3 == True and ml_points == 1 and SR2_ML == True:
        imagebutton:
            xpos 349
            ypos 328
            focus_mask True
            idle "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1.png"
            hover "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1_hover.png"
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            clicked [Hide("displayTextScreen"),Jump("ml_mc_room_night_scene3_v1_label")]
            unhovered Hide("displayTextScreen")

    if ml_mc_room_night_scene3 == True and ml_points >= 2 and MLR2_Sleep == False:
        imagebutton:
            xpos 349
            ypos 328
            focus_mask True
            idle "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1.png"
            hover "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1_hover.png"
            if persistent.incest_patch == True:
                hovered Show("displayTextScreen", displayText = __("Mom"))
            else:
                hovered Show("displayTextScreen", displayText = "Linda")
            clicked [Hide("displayTextScreen"),Jump("ml_mc_room_night_scene3_v1_label")]
            unhovered Hide("displayTextScreen")

    if SR2_NS1 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 227
            ypos 355
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS1/B1.png"
            hover "images/home/mc_room/night/scenes/SR2_NS1/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Sara")
            action [Hide("displayTextScreen"),Jump("SR2_NS1_label")]
            unhovered Hide("displayTextScreen")

    if SR2_NS2 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 347
            ypos 338
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS2/B1.png"
            hover "images/home/mc_room/night/scenes/SR2_NS2/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Sara")
            action [Hide("displayTextScreen"),Jump("SR2_NS2_label")]
            unhovered Hide("displayTextScreen")

    if SR2_NS4 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 232
            ypos 251
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS4/B1.png"
            hover "images/home/mc_room/night/scenes/SR2_NS4/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Sara")
            action [Hide("displayTextScreen"),Jump("SR2_NS4_label")]
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

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/night/b1.png"
            hover "images/home/mc_room/night/b1_hover.png"
            hovered Show("displayTextScreen", displayText = __("Money"))
            action [Hide("displayTextScreen"), Jump("money_less10"),]
            unhovered Hide("displayTextScreen")

screen mc_room_night_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/night/pc_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/night/door1_night_idle.png"

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
        idle "images/home/mc_room/night/s_gallery.png"

    if Neighboor_spy_mc_room == True and take_nap == False:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/night/window_night.png"
    if in_bed_menu  == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/mc_room/morning/sleeping/SleepNight.png"

    if ml_mc_room_night_scene3 == True and ml_points == 1 and SR2_ML == True:
        imagebutton:
            xpos 349
            ypos 328
            focus_mask True
            idle "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1.png"

    if ml_mc_room_night_scene3 == True and ml_points >= 2 and MLR2_Sleep == False:
        imagebutton:
            xpos 349
            ypos 328
            focus_mask True
            idle "images/home/mc_room/night/scenes/ml_mc_room_night_scene3_v1/ml_b1.png"

    if SR2_NS1 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 227
            ypos 355
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS1/B2.png"

    if SR2_NS2 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 347
            ypos 338
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS2/B1.png"

    if SR2_NS4 == True and Sara_points == 2 and MLR2_Sleep == True and SR2_ML == False:
        imagebutton:
            xpos 232
            ypos 251
            focus_mask True
            idle "images/home/mc_room/night/scenes/SR2_NS4/B1.png"

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/night/b1.png"

    if max_r_points == True:
        imagebutton:
            xpos 1860
            ypos 120
            focus_mask True
            idle Transform("images/game_gui/Max_R_Points/7.png", zoom=.4)

