style f_outline is frame:
    align (0.5, 0.55)
    padding (2, 2)
    background "#000"
style f_main is frame:
    align (0.5, 0.5)
    padding (50, 50)
    background "#0E0E0E"

style guide_title is text:
    font "fonts/Proxima Nova Semibold.otf"
    xalign 0.5 yalign 0.18
    size 96
style header is text:
    font "fonts/Proxima Nova Bold.otf"
    size 32
style green_check is text:
    font "fonts/SourceSansPro-Regular.otf"
    color "#00ff00"
    align (0.5, 0.5)
    size 30
style too_low is text:
    font "Fonts/Lato-Regular.ttf"
    color "#f00"
    align (0.5, 0.5)
    size 32
style z is text:
    font "Fonts/Lato-Regular.ttf"
    size 32
    color "#fff"

screen Walk_Throught:
    imagebutton:
        xpos 0
        ypos 0
        idle "/images/game_gui/icons/WalkShow.png"
        hover "/images/game_gui/icons/WalkShow.png"
        action Hide("Walk_Throught")

    if Sara_points >= 3:
        text "You've completed Sara's content!" style "guide_title"

    elif SR2_AS5 or SR2_AS6 or SR2_NS4:
        text "Sara - Part 9" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if SR2_NS3 or SR2_AS6:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if SR2_AS6:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if lube_buy:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if SR2_NS4:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                        text "5" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                        text "Evening" style "z"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Go to Sara's classroom at the school and talk to her" style "z"
                        text "Talk to Sara near your garage" style "z"
                        text "Buy lube from the sex shop ($50)" style "z"
                        text "Go to Sara's classroom at the school and talk to her" style "z"
                        text "Go to your room and talk to Sara" style "z"


    elif SR2_AS4:
        text "Sara - Part 8" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if b5_web_cam_software_buy:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if S_inv_webcam and SR2_ES1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Afternoon" style "z"
                        text "Afternoon" style "z"
                        text "Evening" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Buy the webcam software from the store" style "z"
                        text "Go to Sara's classroom at the school and talk to her" style "z"
                        text "Use the webcam on the computer in your room" style "z"



    elif SR2_AS3:
        text "Sara - Part 7" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if SR2_vibrator in inventory.items or SR2_NS2:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if SR2_NS2:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Evening" style "z"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "When you have $80 talk to the saleswoman at the sex shop" style "z"
                        text "Go to Sara's classroom at the school and talk to her" style "z"
                        text "Go to your room and talk to Sara" style "z"


    elif SR2_MS2 or SR2_grounded or SR2_NS1:
        text "Sara - Part 6" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        text "-" style "z" xalign 0.5
                        if SR2_grounded:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if SR2_NS1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Morning" style "z"
                        text "Morning" style "z"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Optional: Use the spy cam on the bathroom door" style "z"
                        text "Talk to Sara in her room" style "z"
                        text "Go to Sara's classroom at the school and talk to her" style "z"
                        text "Go to your room and talk to Sara" style "z"


    elif mc_sara_night_scene1_v1 >= 3 and sis_nerdy_school_scene3_v1 >= 1:
        text "Sara - Part 5" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if Sara_points >= 2 and sis_nerdy_school_scene1_v1_talk >= 5 and sis_nerdy_school_scene3_v1 >= 3:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if SR2_weekend_swimming_pool:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        text "-" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                        text "Friday" style "z"
                        text "Morning" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Enter the school and talk to Sara and Lily near the lockers" style "z"
                        text "Go to sleep" style "z"
                        if SR2_grounded == False:
                            text __("Optional: Click your bed and do Sara's weekend event") style "z"
                        else:
                            text __("Optional: Sara is grounded not Sara's weekend event") style "z"
                        text "Talk to Sara in her room" style "z"


    elif sis_nerdy_evening_scene2a_v1 >= 3 and sis_nerdy_evening_scene1_v1 >= 3:
        text "Sara - Part 4" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if b4_spy_camera_buy:
                            text "✓" style "green_check"
                        else:
                            text "-" style "z" xalign 0.5
                        text "-" style "z" xalign 0.5
                        if sis_nerdy_school_scene2_v1 >= 3 and mc_sara_night_scene1_v1 >= 1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Morning" style "z"
                        text "Morning" style "z"
                        text "Afternoon" style "z"
                        text "Night" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Optional: Buy the spy cam from the store" style "z"
                        text "Optional: Use the spy cam on the bathroom door" style "z"
                        text "Enter the school and talk to Sara and Lily near the lockers" style "z"
                        text "Go to sleep" style "z"


    elif can_sis_nerdy_gamepad_change >= 1:
        text "Sara - Part 3" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if b3_controller_buy:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if can_sis_nerdy_gamepad_change >= 3:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Morning" style "z"
                        text "Morning" style "z"
                        text "Evening" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Buy the cheap controller from the store" style "z"
                        text "Click the controller in your inventory, then click her controller under her tv" style "z"
                        text "Talk to Sara in her room -> \"Sneak a peek\"" style "z"


    elif sis_nerdy_night_sleeping1_v1 >= 3:
        text "Sara - Part 2" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if sis_nerdy_scene1_v1 >= 3 and after_sis_nerdy_scene1_v1 >= 3:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if drawer_sis_nerdy >= 3 and sis_nerdy_evening_scene2_v1 >= 1 and sis_nerdy_scene4_v1 >= 1 and first_sis_nerdy_scene4_v1 >= 1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if first_sis_nerdy_scene4_v1 >= 3 and sis_nerdy_school_scene2_v1 >= 1 and fourth_visit_sister_nerdy_scene4_v1 >= 1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if can_sis_nerdy_gamepad_change >= 1:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Morning" style "z"
                        text "Morning" style "z"
                        text "Evening" style "z"
                        text "Evening" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Talk to Sara in her room" style "z"
                        text "Go to Sara's room the next day and search the drawer under the tv" style "z"
                        text "Talk to Sara in her room" style "z"
                        text "The next day talk to Sara in her room" style "z"


    elif sis_nerdy_night_sleeping1_v1 < 3:
        text "Sara - Part 1" style "guide_title"
        frame:
            style "f_outline"
            has frame:
                style "f_main"
            vbox at truecenter:
                hbox:
                    align (0.5, 0.5)
                    spacing 50
                    vbox:
                        spacing 3
                        text "Done" style "header"
                        if sis_nerdy_scene1_v1 >= 2 and after_sis_nerdy_scene1_v1 >= 2:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if sis_nerdy_school_scene1_v1_talk >= 2:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                        if can_sis_nerdy_evening_scene1_v1 == False:
                            text "✓" style "green_check"
                        else:
                            text "" style "green_check"
                    vbox:
                        spacing 3
                        text "Step" style "header"
                        text "1" style "z" xalign 0.5
                        text "2" style "z" xalign 0.5
                        text "3" style "z" xalign 0.5
                        text "4" style "z" xalign 0.5
                    vbox:
                        spacing 3
                        text "Time" style "header"
                        text "Morning" style "z"
                        text "Afternoon" style "z"
                        text "Evening" style "z"
                        text "Night" style "z"
                    vbox:
                        spacing 3
                        text " " style "header"
                        text "Talk to Sara in her room" style "z"
                        text "Enter the school and talk to Sara near the lockers" style "z"
                        text "Talk to Sara in her room" style "z"
                        text "Click on Sara in her bed" style "z"