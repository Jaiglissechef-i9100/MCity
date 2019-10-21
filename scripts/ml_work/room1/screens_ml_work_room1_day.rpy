screen ml_work_room1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 836
        ypos 234
        focus_mask True
        idle "/images/ml_work/room1/Room1_door1.png"
        hover "/images/ml_work/room1/Room1_door1_hover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Jump("ml_work_day1")]
            hovered Show("displayTextScreen", displayText = __("Doors"))
            unhovered Hide("displayTextScreen")

    if ml_work_day_scene1 == True and ml_points == 1 and can_ml_work_day_scene1 == True:
        imagebutton:
            xpos 1227
            ypos 290
            focus_mask True
            idle "/images/ml_work/room1/scenes/ml_b1.png"
            hover "/images/ml_work/room1/scenes/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_work_day_scene1_v1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Mom"))
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if ml_work_day_scene2 == True and can_ml_work_day_scene2 == True and ml_points == 1:
        imagebutton:
            xpos 1227
            ypos 290
            focus_mask True
            idle "/images/ml_work/room1/scenes/ml_b1.png"
            hover "/images/ml_work/room1/scenes/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_work_day_scene2_v1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Mom"))
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if not "img10_mom_office_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1733
                ypos 536
                focus_mask True
                idle "images/secret_gallery/Bonus/MLOffice SecretCard1.png"
                hover "images/secret_gallery/Bonus/MLOffice SecretCard1_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img10_mom_office_card"), Jump("mom_office_card")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1733
                ypos 536
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img10_mom_office_card"), Jump("mom_office_card")]
                    unhovered Hide("displayTextScreen")
    if not "img11_mom_office_card2" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 370
                ypos 436
                focus_mask True
                idle "images/secret_gallery/Bonus/MLOffice SecretCard1.png"
                hover "images/secret_gallery/Bonus/MLOffice SecretCard1_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img11_mom_office_card2"), Jump("mom_office_card2")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 370
                ypos 436
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    hovered Show("displayTextScreen", displayText = __("Secret Photo"))
                    action [Hide("displayTextScreen"),addgimage("img11_mom_office_card2"), Jump("mom_office_card2")]
                    unhovered Hide("displayTextScreen")
    if ml_workR2_AS1 == True and can_ml_workR2 == True and ml_points == 2:
        imagebutton:
            xpos 1227
            ypos 290
            focus_mask True
            idle "/images/ml_work/room1/scenes/ml_b1.png"
            hover "/images/ml_work/room1/scenes/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_workR2_AS1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Mom"))
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if ml_workR2_AS2 == True and can_ml_workR2 == True and ml_points == 2:
        imagebutton:
            xpos 1227
            ypos 290
            focus_mask True
            idle "/images/ml_work/room1/scenes/ml_b1.png"
            hover "/images/ml_work/room1/scenes/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("ml_workR2_AS2_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Mom"))
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")

    if MLR3_AS2 == True and ml_points == 3 and MLR3_AS3 != 3:
        imagebutton:
            xpos 1227
            ypos 290
            focus_mask True
            idle "/images/ml_work/room1/scenes/ml_b1.png"
            hover "/images/ml_work/room1/scenes/ml_b1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_AS2")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = __("Mom"))
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Linda")
            unhovered Hide("displayTextScreen")
