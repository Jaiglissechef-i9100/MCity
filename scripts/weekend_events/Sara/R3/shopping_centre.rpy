
label SC_label_M1:
    if day_time > 2:
        show screen map
        show screen sex_shop_closed_screen
        MC "Closed. It's open only at the morning and in the afternoon."
        jump map_label
    else:
        jump SC_label

label SC_label:

    hide screen displayTextScreen
    hide screen map
    $ can_map = True
    if SR3_weekend_event == True:
        $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen SC_scr

label SC_floor2_label:
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen SC_floor2_scr

screen SC_scr:
    if SC_closed == True:
        add "images/v71/Maps/Closed.jpg"
    else:
        add "images/v71/Maps/SC.jpg"


    imagebutton:
        xpos 170
        ypos 0
        focus_mask True
        idle "images/v71/Maps/Stairs.png"
        hover "images/v71/Maps/Stairs_hover.png"
        hovered Show("displayTextScreen", displayText = __("Stairs"))
        if clickable == True:
            if SR3_we_SC_wait == True:
                action [Hide("displayTextScreen"),Jump("SR3_SC_floor2_wait_locked")]
            else:
                action [Hide("displayTextScreen"),Jump("SC_floor2_label")]
            unhovered Hide("displayTextScreen")

    if SR3_we_SC_wait == True:
        imagebutton:
            xpos 922
            ypos 659
            focus_mask True
            idle "images/v71/2_WE/3_Shopping Centre/B1.png"
            hover "images/v71/2_WE/3_Shopping Centre/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Sara")
            if clickable == True:
                action [Hide("displayTextScreen"),Jump("SR3_we_SC_wait_label")]
                unhovered Hide("displayTextScreen")

    if not "img82_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1060
                ypos 504
                focus_mask True
                idle "images/v71/gui/B82a.png"
                hover "images/v71/gui/B82a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img82_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1060
                ypos 504
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img82_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
    if not "img83_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1586
                ypos 445
                focus_mask True
                idle "images/v71/gui/B83a.png"
                hover "images/v71/gui/B83a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img83_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1586
                ypos 445
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img83_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img84_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 51
                ypos 700
                focus_mask True
                idle "images/v71/gui/B84a.png"
                hover "images/v71/gui/B84a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img84_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 51
                ypos 700
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img84_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")


screen SC_floor2_scr:

    if SC_closed == True:
        add "images/v71/Maps/Closed_floor2.jpg"
    else:
        add "images/v71/Maps/floor2.jpg"

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("SC_label")]

    if SR3_we_SC_bus == True:
        imagebutton:
            xpos 1111
            ypos 325
            focus_mask True
            idle "images/v71/2_WE/3_Shopping Centre/B2.png"
            hover "images/v71/2_WE/3_Shopping Centre/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Ice Cream Van")
                action [Hide("displayTextScreen"),Jump("SR3_we_SC_bus_label")]
                unhovered Hide("displayTextScreen")


    if not "img85_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 1774
                ypos 984
                focus_mask True
                idle "images/v71/gui/B85a.png"
                hover "images/v71/gui/B85a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img85_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 1774
                ypos 984
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img85_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

    if not "img86_sec_card" in gallery_photos.storage:
        if jack_frost == False:
            imagebutton:
                xpos 995
                ypos 262
                focus_mask True
                idle "images/v71/gui/B86a.png"
                hover "images/v71/gui/B86a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img86_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 995
                ypos 262
                focus_mask True
                idle "images/secret_gallery/Bonus/B28a.png"
                hover "images/secret_gallery/Bonus/B28a_hover.png"
                if clickable == True:
                    action [Hide("displayTextScreen"),addgimage("img86_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                    unhovered Hide("displayTextScreen")

