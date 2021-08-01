style phone_frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame1.png", 25, 25)


screen phone_main_screen:
    key "hide_windows" action NullAction()
    zorder 102

    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"), Hide("displayTextScreen")]

    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/phone.png", zoom=.7) hover Transform("images/game_gui/phone/phone.png", zoom=.7) action NullAction()

    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Hide("phone_main_screen"),Play ("sound", "sfx/phone_click2.mp3"),]

    imagebutton:
        xalign 0.465
        yalign 0.325
        focus_mask True
        idle Transform("images/game_gui/phone/SMS_Icon_Idle.png", zoom=.7)
        hover Transform("images/game_gui/phone/SMS_Icon_Hover.png", zoom=.7)
        hovered [Play ("sound", "sfx/phone_click.mp3"), Show("displayTextScreen", displayText = "SMS")]
        unhovered Hide("displayTextScreen")
        action [Play ("sound", "sfx/phone_click2.mp3"), Show("contact_screen"),Hide("phone_main_screen"),Hide("displayTextScreen")]
    if Linda_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    elif Sara_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    elif Caroline_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    elif Zuri_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    elif Celia_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    elif Lily_unread_alert == False:
        add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.76) xpos 840 ypos 310
    imagebutton:
        xalign 0.535
        yalign 0.325
        focus_mask True
        idle Transform("images/game_gui/phone/Camera_Icon_Idle.png", zoom=.7)
        hover Transform("images/game_gui/phone/Camera_Icon_Hover.png", zoom=.7)
        hovered [Play ("sound", "sfx/phone_click.mp3"), Show("displayTextScreen", displayText = "Camera")]
        unhovered Hide("displayTextScreen")
        action NullAction()

    imagebutton:
        xalign 0.465
        yalign 0.450
        focus_mask True
        idle Transform("images/game_gui/phone/Stats_Icon_Idle.png", zoom=.7)
        hover Transform("images/game_gui/phone/Stats_Icon_Hover.png", zoom=.7)
        hovered [Play ("sound", "sfx/phone_click.mp3"), Show("displayTextScreen", displayText = "Stats")]
        unhovered Hide("displayTextScreen")
        action [Play ("sound", "sfx/phone_click2.mp3"), Show("relations"),Hide("phone_main_screen"),Hide("displayTextScreen")]

    imagebutton:
        xalign 0.543
        yalign 0.674
        focus_mask True
        idle Transform("images/game_gui/phone/Patreon_Icon_Idle2.png", zoom=.52)
        hover Transform("images/game_gui/phone/Patreon_Icon_Hover2.png", zoom=.52)
        hovered [Play ("sound", "sfx/phone_click.mp3"), Show("displayTextScreen", displayText = "Patreon Site")]
        unhovered Hide("displayTextScreen")
        action [Play ("sound", "sfx/phone_click2.mp3"), OpenURL("https://www.patreon.com/icstor")]




screen m_from_Celia:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Celia")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) hover Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) action NullAction()
    imagebutton xalign 0.448 yalign 0.292 focus_mask True idle Transform("images/game_gui/phone/sms/SMSCelia.png", zoom=.44) hover Transform("images/game_gui/phone/sms/SMSCelia.png", zoom=.44) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("m_from_Celia")]

    frame:
        background Transform("images/game_gui/phone/sms/SMS_Selected_Reading1.png" , zoom=.7)
        align (0.498, 0.540)

        has side "c":
            area (5, 5, 250, 368)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                xfill True
                at left
                spacing 10
            for sms in sms_box.sms_s:
                $ s_pic = sms.simage
                if sms.sname == "sCelia" and  sms.sphoto1==True:
                    frame:
                        style "frame_gui1"
                        imagebutton idle Transform(s_pic, zoom=.5) hover Transform(s_pic, zoom=.5) xpos 0 ypos 0 clicked [Play ("sound", "sfx/phone_click2.mp3"), Show("sms_photo_view",),SetVariable("sms", sms),] hovered [ Play ("sound", "sfx/phone_click.mp3"),]

                if sms.sname == "sCelia" and sms.sphoto1==False:
                    frame:
                        style "frame_gui1"
                        xfill True
                        text ("{size=-5}[sms.mtext]{/size}")