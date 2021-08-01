screen mc_room_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1158
        ypos 84
        focus_mask True
        idle "images/home/mc_room/evening/door1_evening_idle1.png"
        hover "images/home/mc_room/evening/door1_evening_hover1.png"
        hovered Show("displayTextScreen", displayText = "Corridor")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 26
        ypos 529
        focus_mask True
        idle "images/home/mc_room/evening/bed_evening_idle1.png"
        hover "images/home/mc_room/evening/bed_evening_hover1.png"
        hovered Show("displayTextScreen", displayText = "Bed")
        clicked Jump("day_time_changer")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/evening/pc_idle.png"
        hover "images/home/mc_room/evening/pc_hover.png"
        hovered Show("displayTextScreen", displayText = "Computer")
        if MC_computer == False:
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("MC_computer_lab")]
        else:
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("computer_menu")]
        unhovered Hide("displayTextScreen")

    if not "img4_mc_room_card" in gallery_photos.storage:
        imagebutton:
            xpos 23
            ypos 906
            focus_mask True
            idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
            hover "images/secret_gallery/Bonus/MCBedroom SecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img4_mc_room_card") ,Jump("mc_room_card")]
            hovered Show("displayTextScreen", displayText = "Secret Card")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/evening/s_gallery.png"
        hover "images/home/mc_room/evening/s_gallery_hover.png"
        hovered Show("displayTextScreen", displayText = "Secret Gallery")
        action [Hide("displayTextScreen"), Show("secret_gallery"),]
        unhovered Hide("displayTextScreen")

    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/window_evening.png"
            hover "images/home/mc_room/evening/window_evening_hover.png"
            hovered Show("displayTextScreen", displayText = "Window")
            action [Hide("displayTextScreen"), Jump("neighboor_spy_v1_label"),]
            unhovered Hide("displayTextScreen")
    if caroline_mc_room_evening_scene2 == True and CeR2_ES2 == False:
        imagebutton:
            xpos 735
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1.png"
            hover "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"), Jump("caroline_mc_room_evening_scene2_label"),]
            unhovered Hide("displayTextScreen")
    if caroline_mc_room_evening_scene3 == True and caroline_mc_room_can_evening_scene3 == True and CeR2_ES2 == False:
        imagebutton:
            xpos 717
            ypos 217
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1.png"
            hover "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Caroline")
            action [Hide("displayTextScreen"), Jump("caroline_mc_room_evening_scene3_label"),]
            unhovered Hide("displayTextScreen")

    if CeR2_ES2 == True:
        imagebutton:
            xpos 1412
            ypos 243
            focus_mask True
            idle "images/CeR2/ES2/Celia.png"
            hover "images/CeR2/ES2/Celia_hover.png"
            hovered Show("displayTextScreen", displayText = "Celia")

            action [Hide("displayTextScreen"), Jump("CeR2_ES2_lab"),]
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
            idle "images/home/mc_room/evening/b1.png"
            hover "images/home/mc_room/evening/b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Money")
            action [Hide("displayTextScreen"), Jump("money_less10"),]
            unhovered Hide("displayTextScreen")
screen mc_room_evening_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/door1_evening_idle.png"
        hover "images/home/mc_room/evening/door1_evening_hover.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/bed_evening_idle.png"
        hover "images/home/mc_room/evening/bed_evening_hover.png"


    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/evening/pc_idle.png"
        hover "images/home/mc_room/evening/pc_hover.png"

    if not "img4_mc_room_card" in gallery_photos.storage:
        imagebutton:
            xpos 23
            ypos 906
            focus_mask True
            idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
            hover "images/secret_gallery/Bonus/MCBedroom SecretCard_hover.png"


    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/evening/s_gallery.png"
        hover "images/home/mc_room/evening/s_gallery_hover.png"


    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/window_evening.png"
            hover "images/home/mc_room/evening/window_evening_hover.png"
    if caroline_mc_room_evening_scene2 == True and CeR2_ES2 == False:
        imagebutton:
            xpos 735
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1.png"
    if caroline_mc_room_evening_scene3 == True and caroline_mc_room_can_evening_scene3 == True and CeR2_ES2 == False:
        imagebutton:
            xpos 717
            ypos 217
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1.png"

    if CeR2_ES2 == True:
        imagebutton:
            xpos 1412
            ypos 243
            focus_mask True
            idle "images/CeR2/ES2/Celia.png"

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/evening/b1.png"
    if max_r_points == True:
        imagebutton:
            xpos 1860
            ypos 120
            focus_mask True
            idle Transform("images/game_gui/Max_R_Points/7.png", zoom=.4)