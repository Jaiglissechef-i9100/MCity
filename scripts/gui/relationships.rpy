

screen relations:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"), Hide("displayTextScreen"),Hide("relations")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/Relations/PhoneRelations.png", zoom=.7) hover Transform("images/game_gui/phone/Relations/PhoneRelations.png", zoom=.7) action NullAction()

    imagebutton xalign 0.503 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("relations")]
    frame:
        background Transform("images/game_gui/phone/Relations/PhoneRelationsBackground.png" , zoom=.68)
        align (0.501, 0.558)

        has side "c":
            area (0, 0, 249, 346)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                spacing 0.1
            imagebutton xpos 0 ypos 0 focus_mask True idle Transform("images/game_gui/Phone/Relations/ML.png", zoom=0.58)
            text "{size=-3}[ml_points]/[ml_max]{/size}" xpos 155 ypos -80
            bar range ml_max value ml_points xmaximum 160 ysize 20 ypos -78 xpos 100

            imagebutton xpos 0 ypos -20 focus_mask True idle Transform("images/game_gui/Phone/Relations/Caroline.png", zoom=0.58)
            text "{size=-3}[Caroline_points]/[Caroline_max]{/size}" xpos 155 ypos -100
            bar range Caroline_max value Caroline_points xmaximum 160 ysize 20 ypos -98 xpos 100

            imagebutton xpos 0 ypos -40 focus_mask True idle Transform("images/game_gui/Phone/Relations/Sara.png", zoom=0.58)
            text "{size=-3}[Sara_points]/[Sara_max]{/size}" xpos 155 ypos -120
            bar range Sara_max value Sara_points xmaximum 160 ysize 20 ypos -118 xpos 100

            imagebutton xpos 0 ypos -60 focus_mask True idle Transform("images/game_gui/Phone/Relations/Celia.png", zoom=0.58)
            text "{size=-3}[Celia_points]/[Celia_max]{/size} " xpos 155 ypos -140
            bar range Celia_max value Celia_points xmaximum 160 ysize 20 ypos -138 xpos 100

            imagebutton xpos 0 ypos -80 focus_mask True idle Transform("images/game_gui/Phone/Relations/Liza.png", zoom=0.58)
            text "{size=-3}[Li_points]/[Li_max]{/size} " xpos 155 ypos -160
            bar range Li_max value Li_points xmaximum 160 ysize 20 ypos -158 xpos 100