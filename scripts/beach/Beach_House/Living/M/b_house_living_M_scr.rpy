screen b_house_living_M_scr:
    key "hide_windows" action NullAction()
    add "images/Beach/Beach_House/Living/M/map.jpg"

    imagebutton:
        xpos 422
        ypos 171
        focus_mask True
        idle "images/Beach/Beach_House/Living/M/B1.png"
        hover "images/Beach/Beach_House/Living/M/B1_hover.png"
        if clickable == True:
            action [Play("sound", "sfx/door_open.mp3"),Jump("b_house_bedroom_M1")]
        hovered Show("displayTextScreen", displayText = __("Bedroom"))
        unhovered Hide("displayTextScreen")

    if clickable == True and MLR3_beach_event == False:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play("sound", "sfx/door_open.mp3"),Jump("beach3_M1")]


    if not "img36_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 913
            ypos 424
            focus_mask True
            idle "images/secret_gallery/Bonus/B36a.png"
            hover "images/secret_gallery/Bonus/B36a_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img36_sec_card"),SetVariable("clickable", False), Show("card_found_alert")]
            unhovered Hide("displayTextScreen")

    if MLR3_b_house_wait == 4 and MLR3_beach_event == True:
        imagebutton:
            xpos 2
            ypos 395
            focus_mask True
            idle "images/Beach/MLR3_beach_event/House/MorningCoffie/B1.png"
            hover "images/Beach/MLR3_beach_event/House/MorningCoffie/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_b_house_coffe"),]
                if renpy.loadable("patch.rpy"):
                    hovered Show("displayTextScreen", displayText = __("Mom"))
                if not renpy.loadable("patch.rpy"):
                    hovered Show("displayTextScreen", displayText = "Linda")
                unhovered Hide("displayTextScreen")

    if MLR3_b_house_wait == 6 and MLR3_beach_event == True:
        imagebutton:
            xpos 805
            ypos 84
            focus_mask True
            idle "images/Beach/MLR3_beach_event/House/Leaving/B1.png"
            hover "images/Beach/MLR3_beach_event/House/Leaving/B1_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("MLR3_b_house_leaving"),]
                if renpy.loadable("patch.rpy"):
                    hovered Show("displayTextScreen", displayText = __("Mom"))
                if not renpy.loadable("patch.rpy"):
                    hovered Show("displayTextScreen", displayText = "Linda")
                unhovered Hide("displayTextScreen")
