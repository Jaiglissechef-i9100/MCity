image live_camera_deskop = "images/game_gui/pc/LiveCamera/LiveCameraDeskop.png"
image Celia_Invitation_v1_p1 = "images/game_gui/pc/LiveCamera/Celia_Invitation.png"
image Sara_Invitation_v1_p1 = "images/game_gui/pc/LiveCamera/Sara_Invitation.png"

default Ce_web_cam_locked = False
label live_camera_label:
    scene main_deskop
    show live_camera_deskop
    show screen main_deskop_pcv1
    if celia_invitation_webcam == 1 and day_time == 3 and S_inv_webcam == False:
        show screen live_camera_screen
        call screen celia_invitation_screen
    elif S_inv_webcam == True and day_time == 3:
        show screen live_camera_screen
        call screen sara_invitation_screen
    call screen live_camera_screen



screen live_camera_screen:
    key "hide_windows" action NullAction()
    modal True
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/pc/cd/Close.png"
        hover "images/game_gui/pc/cd/Close_Hover.png"
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Hide("live_camera_screen"),Jump("pc_icon_label")]

    if celia_in_camweb_contacts == True and day_time != 3:
        imagebutton:
            xpos 324
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"
            hover "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"

    if celia_in_camweb_contacts == False:
        imagebutton:
            xpos 324
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/NoName.png"
            hover "images/game_gui/pc/LiveCamera/NoName.png"

    if celia_in_camweb_contacts == True and day_time == 3 and Celia_points <3 and Ce_web_cam_locked == False:
        imagebutton:
            xpos 324
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/CeliaLive.png"
            hover "images/game_gui/pc/LiveCamera/CeliaLiveHover.png"
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("celia_webcam_scenes")]
            unhovered Hide("displayTextScreen")
    if Ce_web_cam_locked == True and celia_in_camweb_contacts == True:
        imagebutton:
            xpos 324
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"
            hover "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"
    if Celia_points >=3:
        imagebutton:
            xpos 324
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"
            hover "images/game_gui/pc/LiveCamera/Celia_webcam_contact.png"
    if sara_in_camweb_contacts == True and day_time != 3:
        imagebutton:
            xpos 516
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/Sara_B1.png"
            hover "images/game_gui/pc/LiveCamera/Sara_B1.png"

    if sara_in_camweb_contacts == False:
        imagebutton:
            xpos 516
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/NoName.png"
            hover "images/game_gui/pc/LiveCamera/NoName.png"

    if sara_in_camweb_contacts == True and day_time == 3 and sara_webcam_online == True:
        imagebutton:
            xpos 516
            ypos 247
            focus_mask True
            idle "images/game_gui/pc/LiveCamera/Sara_B2.png"
            hover "images/game_gui/pc/LiveCamera/Sara_B2_hover.png"
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("SR2_ES1_label")]
            unhovered Hide("displayTextScreen")











screen celia_invitation_screen:
    key "hide_windows" action NullAction()
    zorder 102
    modal True
    add "images/game_gui/pc/LiveCamera/Celia_Invitation.png"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/pc/LiveCamera/accept_button.png"
        hover "images/game_gui/pc/LiveCamera/accept_button_hover.png"
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Hide("celia_invitation_screen"),SetVariable("celia_invitation_webcam", 3),SetVariable("celia_in_camweb_contacts", True),Jump("live_camera_label")]


screen sara_invitation_screen:
    key "hide_windows" action NullAction()
    zorder 102
    modal True
    add "images/game_gui/pc/LiveCamera/Sara_Invitation.png"
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/pc/LiveCamera/accept_button.png"
        hover "images/game_gui/pc/LiveCamera/accept_button_hover.png"
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Hide("sara_invitation_screen"),SetVariable("S_inv_webcam", False),SetVariable("sara_in_camweb_contacts", True),Jump("live_camera_label")]