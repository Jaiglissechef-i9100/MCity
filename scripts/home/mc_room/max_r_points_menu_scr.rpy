
default C_R_max_page = 1
default C_harem = False
default C_pregnant = False
screen max_r_points_menu_scr:
    zorder 108
    modal True
    add "images/game_gui/Max_R_Points/6.png"
    imagebutton:
        xpos 440
        ypos 380
        focus_mask True
        idle "images/game_gui/Phone/relations/Caroline.png"
        hover "images/game_gui/Phone/relations/CarolineHover.png"
        action [Hide("max_r_points_menu_scr"), Show("max_r_points_C_scr"),SetVariable("C_R_max_page",1)]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1620
        ypos 129
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [Hide("max_r_points_menu_scr"),]

screen max_r_points_C_scr:
    zorder 108
    modal True
    add "images/game_gui/Max_R_Points/1.png"

    imagebutton:
        xpos 1620
        ypos 129
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [Hide("max_r_points_C_scr"),]

    if C_R_max_page == 1 and C_harem == False:
        imagebutton:
            xpos 584
            ypos 328
            idle "images/game_gui/Max_R_Points/4.png"
            hover "images/game_gui/Max_R_Points/4a.png"
            action NullAction()
            hovered Show("C_harem_info")
            unhovered Hide("C_harem_info")

    if C_R_max_page == 1 and C_harem == True:
        add "images/game_gui/Max_R_Points/4b.png" xpos 584 ypos 328

    if C_pregnant == False and C_R_max_page == 2:
        imagebutton:
            xpos 584
            ypos 328
            idle "images/game_gui/Max_R_Points/5.png"
            hover "images/game_gui/Max_R_Points/5a.png"
            action [Hide("C_pregnant_info"),SetVariable("C_pregnant", True)]
            hovered Show("C_pregnant_info")
            unhovered Hide("C_pregnant_info")

    if C_pregnant == True and C_R_max_page == 2:

        add "images/game_gui/Max_R_Points/5.png" xpos 584 ypos 328
        add "images/game_gui/Max_R_Points/9.png" xpos 584 ypos 328

    if C_R_max_page < 2:
        imagebutton:
            xpos 1511
            ypos 500
            idle "images/game_gui/Max_R_Points/3.png"
            hover "images/game_gui/Max_R_Points/3a.png"
            action SetVariable("C_R_max_page", C_R_max_page+1)
    if C_R_max_page >1:
        imagebutton:
            xpos 295
            ypos 500
            idle "images/game_gui/Max_R_Points/2.png"
            hover "images/game_gui/Max_R_Points/2a.png"
            action SetVariable("C_R_max_page", C_R_max_page-1)

screen C_pregnant_info:
    zorder 109
    add "images/game_gui/Max_R_Points/8.png" xpos 1255 ypos 624

    vbox xpos 1360 ypos 704 spacing 20:
        text "{color=#000000}Requirements:{/color}" size 33
        if Caroline_points == 5:
            text "{color=#49F212}{b}Caroline [Caroline_points]/5{/b}{/color}" size 33
        if Caroline_points < 5:
            text "{color=#F00B0B}{b}Caroline [Caroline_points]/5{/b}{/color}" size 33

screen C_harem_info:
    zorder 109
    add "images/game_gui/Max_R_Points/8.png" xpos 1255 ypos 624

    vbox xpos 1360 ypos 704 spacing 20:
        text "{color=#000000}Requirements:{/color}" size 33
        if Caroline_points == 5:
            text "{color=#49F212}{b}Caroline [Caroline_points]/5{/b}{/color}" size 33
        if Caroline_points < 5:
            text "{color=#F00B0B}{b}Caroline [Caroline_points]/5{/b}{/color}" size 33

        if Sara_points < 5:
            text "{color=#F00B0B}{b}Sara [Sara_points]/5{/b}{/color}" size 33
        if Sara_points == 5:
            text "{color=#49F212}{b}Sara [Sara_points]/5{/b}{/color}" size 33

        if ml_points == 5:
            text "{color=#49F212}{b}[Mom_name] [ml_points]/5{/b}{/color}" size 33
        if Sara_points < 5:
            text "{color=#F00B0B}{b}[Mom_name] [ml_points]/5{/b}{/color}" size 33