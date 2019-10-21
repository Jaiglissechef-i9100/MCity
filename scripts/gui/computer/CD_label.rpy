image installing_software:
    "images/game_gui/pc/cd/Installing1.png"
    0.15
    "images/game_gui/pc/cd/Installing2.png"
    0.15
    "images/game_gui/pc/cd/Installing3.png"
    0.15
    "images/game_gui/pc/cd/Installing4.png"
    0.15
    "images/game_gui/pc/cd/Installing5.png"

image CD_deskop = "images/game_gui/pc/cd/CD_deskop.png"

label CD_label:
    scene main_deskop
    show screen main_deskop_pcv1
    show CD_deskop
    call screen CD_screen

label WebCam_Software_install_label:
    show screen WebCam_Software_install_screen
    scene main_deskop
    show CD_deskop
    show installing_software
    $ renpy.pause (1.57, hard=True)
    $ inventory.drop(web_cam_cd)
    $ live_camera_instaled = True
    jump CD_label

screen WebCam_Software_install_screen:
    key "hide_windows" action NullAction()
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
    timer 1.57 action Hide ("WebCam_Software_install_screen")

screen CD_screen:
    key "hide_windows" action NullAction()
    modal True
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/pc/cd/Close.png"
        hover "images/game_gui/pc/cd/Close_Hover.png"
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Hide("CD_screen"),Jump("pc_icon_label")]


    if web_cam_cd in inventory.items:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/pc/cd/WebCam_Software.png"
            hover "images/game_gui/pc/cd/WebCam_Software_Hover.png"
            hovered Show("displayTextScreen", displayText = __("WebCam Software"))
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("WebCam_Software_install_label")]
            unhovered Hide("displayTextScreen")
