image Stats_mouth = Transform("images/NS_B/Mouth.png", zoom=.40)
image Stats_footjob = Transform("images/NS_B/Footjob.png", zoom=.40)
image Stats_Tits = Transform("images/NS_B/Tits.png", zoom=.40)
default g_stats_page_char = 1
default c_stats_page = 1
default ml_stats_page = 1
default s_stats_page = 1
default li_stats_page = 1
default yaz_stats_page = 1
default Caroline_stats_visited = 0
default Ml_stats_visited = 0
default Ml_stats_in_your_room = 0
default Sara_stats_visited = 0
default li_stats_visited = 0
default yaz_stats_visited = 0

label G_Stats_label:
    scene main_deskop
    show screen main_deskop_pcv1
    show screen G_Stats_scr
    hide screen ml_G_Stats_scr
    hide screen Caroline_G_Stats_scr
    hide screen screenSara_G_Stats_scr
    hide screen li_G_Stats_scr
    hide screen yaz_G_Stats_scr
    if g_stats_page_char == 1:
        show screen ml_G_Stats_scr
        show screen Caroline_G_Stats_scr
        call screen Sara_G_Stats_scr

    if g_stats_page_char == 2:
        show screen li_G_Stats_scr
        call screen yaz_G_Stats_scr

label hide_stats:
    hide screen ml_G_Stats_scr
    hide screen Caroline_G_Stats_scr
    hide screen screenSara_G_Stats_scr
    hide screen li_G_Stats_scr
    hide screen yaz_G_Stats_scr
    jump pc_icon_label

init -1 python:
    c_inv_page = 0
    ml_inv_page = 0
    s_inv_page = 0
    li_inv_page = 0
    yaz_inv_page = 0

screen G_Stats_scr:

    add "images/game_gui/pc/Stats/Stats_window.png"
    modal True
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/pc/cd/Close.png"
        hover "images/game_gui/pc/cd/Close_Hover.png"
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Hide("G_Stats_scr"),Jump("hide_stats")]
    if g_stats_page_char > 1:
        textbutton "Previous":
            action [SetVariable("g_stats_page_char", g_stats_page_char - 1),Jump ("G_Stats_label")]
            xalign 0.25
            yalign 0.8
    if g_stats_page_char < 2:
        textbutton "Next":
            action [SetVariable("g_stats_page_char", g_stats_page_char + 1),Jump ("G_Stats_label")]
            xalign 0.7
            yalign 0.8

screen ml_G_Stats_scr:
    frame:
        xpos 372
        ypos 242
        background "images/game_gui/pc/Stats/ML_Stats.png"

        has side "c":
            area (0, 100, 295, 346)

        vbox:
            spacing 15
            xsize 295
            text "Relation points: {size=-3}[ml_points]/[ml_max]{/size}" xalign 0.5
            bar range ml_max value ml_points xmaximum 160 ysize 20 xalign 0.5
            text "{b}{color=#ffff66}Night Scenes{/color}{/b}:" xalign 0.5
            if ml_stats_page == 1:
                text "Visited you: [Ml_stats_in_your_room]" xalign 0.5
            if ml_stats_page == 2:
                text "Visited: [Ml_stats_visited]" xalign 0.5
            text "{k=-.5}Option chosen:{/k}" xalign 0.5
            if ml_stats_page == 1:
                text "{color=#66ff66}Visited you{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.ml_nsb_s, key=attrgetter('number'))
            if ml_stats_page == 2:
                text "{color=#66ff66}Wake up{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.ml_nsb_wake, key=attrgetter('number'))


    $ x = 765
    $ y = 550
    $ i = 0
    $ next_ml_inv_page = ml_inv_page + 1
    $ prev_ml_inv_page = ml_inv_page - 1
    if next_ml_inv_page > int(len(nsb_box.ml_nsb_s)/9):
        $ next_ml_inv_page = 0
    if prev_ml_inv_page < int(len(nsb_box.ml_nsb_s)/9):
        $ prev_ml_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (ml_inv_page+1)*9 and i+1>ml_inv_page*9:
            $ x += 60
            if i%3==0:
                $ y += 60
                $ x = 448
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B_stats",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),] at G_Stats_scr_transform
                unhovered Hide("displayTextNS_B_stats")

            if nsb.locked == False:
                text "{size=-5}[nsb.t_played]{/size}" xpos x ypos y + 33

            if nsb.locked == True:
                add Transform("images/NS_B/Locked_slot.png", zoom=.4) xpos x ypos y

        $ i += 1
    imagebutton:
        xpos 358
        ypos 552

        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4)
        if ml_stats_page > 1:
            action [SetVariable("ml_stats_page", ml_stats_page -1),SetVariable('ml_inv_page',0)]
        else:
            action [SetVariable("ml_stats_page", ml_stats_page + 1),SetVariable('ml_inv_page',0)]
    imagebutton:
        xpos 582
        ypos 552
        focus_mask True
        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4)
        if ml_stats_page < 2:
            action [SetVariable("ml_stats_page", ml_stats_page + 1),SetVariable('ml_inv_page',0)]
        else:
            action [SetVariable("ml_stats_page", ml_stats_page -1),SetVariable('ml_inv_page',0)]
    if len(nsb_box.ml_nsb_s)>9 and ml_stats_page == 1:


        imagebutton xpos 443 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('ml_inv_page', prev_ml_inv_page),]
        imagebutton xpos 493 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('ml_inv_page', next_ml_inv_page), ]
    if len(nsb_box.ml_nsb_s)>9 and ml_stats_page == 2:

        imagebutton xpos 443 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('ml_inv_page', prev_ml_inv_page),]
        imagebutton xpos 493 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('ml_inv_page', next_ml_inv_page), ]




screen Caroline_G_Stats_scr:
    frame:
        xpos 750
        ypos 242
        background "images/game_gui/pc/Stats/C_Stats.png"

        has side "c":
            area (0, 100, 295, 346)

        vbox:
            spacing 15
            xsize 295
            text "Relation points: {size=-3}[Caroline_points]/[Caroline_max]{/size}" xalign 0.5
            bar range Caroline_max value Caroline_points xmaximum 160 ysize 20 xalign 0.5
            text "{b}{color=#ffff66}Night Scenes{/color}{/b}:" xalign 0.5
            text "Visited: [Caroline_stats_visited]" xalign 0.5
            text "{k=-.5}Option chosen:{/k}" xalign 0.5
            if c_stats_page == 1:
                text "{color=#66ff66}While Sleeping{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.c_nsb_s, key=attrgetter('number'))
            if c_stats_page == 2:
                text "{color=#66ff66}Wake up{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.c_nsb_wake, key=attrgetter('number'))


    $ x = 765
    $ y = 550
    $ i = 0
    $ next_c_inv_page = c_inv_page + 1
    $ prev_c_inv_page = c_inv_page - 1
    if next_c_inv_page > int(len(nsb_box.c_nsb_s)/9):
        $ next_c_inv_page = 0
    if prev_c_inv_page < int(len(nsb_box.c_nsb_s)/9):
        $ prev_c_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (c_inv_page+1)*9 and i+1>c_inv_page*9:
            $ x += 60
            if i%3==0:
                $ y += 60
                $ x = 820
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B_stats",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),] at G_Stats_scr_transform
                unhovered Hide("displayTextNS_B_stats")

            if nsb.locked == False:
                text "{size=-5}[nsb.t_played]{/size}" xpos x ypos y + 33
            if nsb.locked == True:
                add Transform("images/NS_B/Locked_slot.png", zoom=.4) xpos x ypos y
        $ i += 1
    imagebutton:
        xpos 735
        ypos 552

        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4)
        if c_stats_page > 1:
            action [SetVariable("c_stats_page", c_stats_page -1),SetVariable('c_inv_page',0)]
        else:
            action [SetVariable("c_stats_page", c_stats_page + 1),SetVariable('c_inv_page',0)]
    imagebutton:
        xpos 960
        ypos 552
        focus_mask True
        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4)
        if c_stats_page < 2:
            action [SetVariable("c_stats_page", c_stats_page + 1),SetVariable('c_inv_page',0)]
        else:
            action [SetVariable("c_stats_page", c_stats_page -1),SetVariable('c_inv_page',0)]
    if len(nsb_box.c_nsb_s)>9 and c_stats_page == 1:


        imagebutton xpos 820 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('c_inv_page', prev_c_inv_page),]
        imagebutton xpos 870 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('c_inv_page', next_c_inv_page), ]
    if len(nsb_box.c_nsb_wake)>9 and c_stats_page == 2:

        imagebutton xpos 820 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('c_inv_page', prev_c_inv_page),]
        imagebutton xpos 870 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('c_inv_page', next_c_inv_page), ]

screen Sara_G_Stats_scr:
    frame:
        xpos 1122
        ypos 242
        background "images/game_gui/pc/Stats/S_Stats.png"

        has side "c":
            area (0, 100, 295, 346)

        vbox:
            spacing 15
            xsize 295
            text "Relation points: {size=-3}[Sara_points]/[Sara_max]{/size}" xalign 0.5
            bar range Sara_max value Sara_points xmaximum 160 ysize 20 xalign 0.5
            text "{b}{color=#ffff66}Night Scenes{/color}{/b}:" xalign 0.5
            text "Visited: [Sara_stats_visited]" xalign 0.5
            text "Option chosen:" xalign 0.5
            if s_stats_page == 1:
                text "{color=#66ff66}While Sleeping{/color}" xalign 0.5
                $ s_sorted_nsb = sorted(nsb_box.s_nsb_s, key=attrgetter('number'))
            if s_stats_page == 2:
                text "{color=#66ff66}Wake up{/color}" xalign 0.5
                $ s_sorted_nsb = sorted(nsb_box.s_nsb_wake, key=attrgetter('number'))


    $ x = 765
    $ y = 550
    $ i = 0
    $ next_s_inv_page = s_inv_page + 1
    $ prev_s_inv_page = s_inv_page - 1
    if next_s_inv_page > int(len(nsb_box.s_nsb_s)/9):
        $ next_s_inv_page = 0
    if prev_s_inv_page < int(len(nsb_box.s_nsb_s)/9):
        $ prev_s_inv_page = 0

    for nsb in s_sorted_nsb:
        if i+1 <= (s_inv_page+1)*9 and i+1>s_inv_page*9:
            $ x += 60
            if i%3==0:
                $ y += 60
                $ x = 1192
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B_stats",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),] at G_Stats_scr_transform
                unhovered Hide("displayTextNS_B_stats")

            if nsb.locked == False:
                text "{size=-5}[nsb.t_played]{/size}" xpos x ypos y + 33

            if nsb.locked == True:
                add Transform("images/NS_B/Locked_slot.png", zoom=.4) xpos x ypos y
        $ i += 1
    imagebutton:
        xpos 1107
        ypos 552
        focus_mask True
        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4)
        if s_stats_page > 1:
            action [SetVariable("s_stats_page", s_stats_page -1),SetVariable('s_inv_page',0)]
        else:
            action [SetVariable("s_stats_page", s_stats_page + 1),SetVariable('s_inv_page',0)]
    imagebutton:
        xpos 1332
        ypos 552
        focus_mask True
        idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4)
        hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4)
        if s_stats_page < 2:
            action [SetVariable("s_stats_page", s_stats_page + 1),SetVariable('s_inv_page',0)]
        else:
            action [SetVariable("s_stats_page", s_stats_page -1),SetVariable('s_inv_page',0)]

    if len(nsb_box.s_nsb_s)>9 and s_stats_page == 1:


        imagebutton xpos 1192 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('s_inv_page', prev_s_inv_page),]
        imagebutton xpos 1242 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('s_inv_page', next_s_inv_page), ]
    if len(nsb_box.s_nsb_wake)>9 and s_stats_page == 2:

        imagebutton xpos 1192 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('s_inv_page', prev_s_inv_page),]
        imagebutton xpos 1242 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('s_inv_page', next_s_inv_page), ]

screen li_G_Stats_scr:
    frame:
        xpos 372
        ypos 242
        background "images/game_gui/pc/Stats/Li_Stats.png"

        has side "c":
            area (0, 100, 295, 346)

        vbox:
            spacing 15
            xsize 295
            text "Relation points: {size=-3}[Li_points]/[Li_max]{/size}" xalign 0.5
            bar range Li_max value Li_points xmaximum 160 ysize 20 xalign 0.5
            text "{b}{color=#ffff66}Night Scenes{/color}{/b}:" xalign 0.5

            text "Visited: [li_stats_visited]" xalign 0.5
            text "{k=-.5}Option chosen:{/k}" xalign 0.5
            if li_stats_page == 1:
                text "{color=#66ff66}While sleeping{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.li_nsb_s, key=attrgetter('number'))





    $ x = 765
    $ y = 550
    $ i = 0
    $ next_li_inv_page = li_inv_page + 1
    $ prev_li_inv_page = li_inv_page - 1
    if next_li_inv_page > int(len(nsb_box.li_nsb_s)/9):
        $ next_li_inv_page = 0
    if prev_li_inv_page < int(len(nsb_box.li_nsb_s)/9):
        $ prev_li_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (li_inv_page+1)*9 and i+1>li_inv_page*9:
            $ x += 60
            if i%3==0:
                $ y += 60
                $ x = 448
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B_stats",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),] at G_Stats_scr_transform
                unhovered Hide("displayTextNS_B_stats")

            if nsb.locked == False:
                text "{size=-5}[nsb.t_played]{/size}" xpos x ypos y + 33

            if nsb.locked == True:
                add Transform("images/NS_B/Locked_slot.png", zoom=.4) xpos x ypos y
        $ i += 1



        if len(nsb_box.li_nsb_s)>9 and li_stats_page == 1:


            imagebutton xpos 443 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('li_inv_page', prev_li_inv_page),]
            imagebutton xpos 493 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('li_inv_page', next_li_inv_page), ]

screen yaz_G_Stats_scr:
    frame:
        xpos 750
        ypos 242
        background "images/game_gui/pc/Stats/Yaz_Stats.png"

        has side "c":
            area (0, 100, 295, 346)

        vbox:
            spacing 15
            xsize 295
            text "Relation points: {size=-3}[Y_points]/[Y_max]{/size}" xalign 0.5
            bar range Y_max value Y_points xmaximum 160 ysize 20 xalign 0.5
            text "{b}{color=#ffff66}Night Scenes{/color}{/b}:" xalign 0.5

            text "Visited: [yaz_stats_visited]" xalign 0.5
            text "{k=-.5}Option chosen:{/k}" xalign 0.5
            if yaz_stats_page == 1:
                text "{color=#66ff66}While sleeping{/color}" xalign 0.5
                $ sorted_nsb = sorted(nsb_box.yaz_nsb_s, key=attrgetter('number'))

    $ x = 765
    $ y = 550
    $ i = 0
    $ next_yaz_inv_page = yaz_inv_page + 1
    $ prev_yaz_inv_page = yaz_inv_page - 1
    if next_yaz_inv_page > int(len(nsb_box.yaz_nsb_s)/9):
        $ next_yaz_inv_page = 0
    if prev_yaz_inv_page < int(len(nsb_box.yaz_nsb_s)/9):
        $ prev_yaz_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (yaz_inv_page+1)*9 and i+1>yaz_inv_page*9:
            $ x += 60
            if i%3==0:
                $ y += 60
                $ x = 820
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B_stats",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),] at G_Stats_scr_transform
                unhovered Hide("displayTextNS_B_stats")

            if nsb.locked == False:
                text "{size=-5}[nsb.t_played]{/size}" xpos x ypos y + 33

            if nsb.locked == True:
                add Transform("images/NS_B/Locked_slot.png", zoom=.4) xpos x ypos y
        $ i += 1

        if len(nsb_box.yaz_nsb_s)>9 and yaz_stats_page == 1:

            imagebutton xpos 443 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.4) action [SetVariable('yaz_inv_page', prev_yaz_inv_page),]
            imagebutton xpos 493 ypos 780 focus_mask True idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.4) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.4) action [SetVariable('yaz_inv_page', next_yaz_inv_page), ]

transform G_Stats_scr_transform:
    zoom 0.4

screen displayTextNS_B_stats:

    default displayText2 = ""

    vbox:
        xpos tt_xpos + 50
        ypos tt_ypos

        frame:
            style "frame_gui2_stats"
            text displayText2 style "date_s_stats"

style date_s_stats is text:
    size 23
    text_align 0.5
style frame_gui2_stats:
    padding gui.frame_borders.padding
    background Frame("gui/frame2.png", 25, 25)
    xmaximum 300