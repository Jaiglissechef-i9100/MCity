image map_day1 = "images/game_gui/map/Map_Day.jpg"
image map_night1 = "images/game_gui/map/Map_Night.jpg"
#-------------------------------------------------------------------------------
default Ce_unread_alert = True

screen map_button:

    key "focus_left" action NullAction()
    key "focus_right" action NullAction()
    key "focus_up" action NullAction()
    key "focus_down" action NullAction()
    zorder 101

    if ML_end_content == True and ml_points == 4:
        on "show" action Show("ML_end_content_scr")
    if Li_end_content == True:
        on "show" action Show("Li_end_content_scr")
    if C_end_content == True and Caroline_points == 5:
        on "show" action Show("C_end_content_scr")


    if can_map==True:
        if clickable == True:
            imagebutton:
                xpos 1800
                ypos 0
                focus_mask True
                idle Transform("images/game_gui/icons/Map_Icon_Idle.png", zoom=.8)
                hover Transform("images/game_gui/icons/Map_Icon_Hover.png", zoom=.8)
                if bob_carkeys in inventory.items:
                    action Jump("leave_cant")
                else:
                    action [Hide("map_button"),Hide("displayTextScreen"),SetVariable("in_map", True),Play ("sound", "sfx/map_open.mp3"), Jump("map_label"),]
                hovered Show("displayTextScreen", displayText = "Map", size=9)
                unhovered Hide("displayTextScreen")
        if clickable == False:
            imagebutton:
                xpos 1800
                ypos 0
                focus_mask True
                idle Transform("images/game_gui/icons/No_Map_Hover.png", zoom=.8)
                hover Transform("images/game_gui/icons/Map Icon Hover Cant.png", zoom=.8)
                action [Show("map_button"),Show("displayTextScreen", displayText = "Map")]
                hovered Show("displayTextScreen", displayText = "Map")
                unhovered Hide("displayTextScreen")
    if can_map==False:
        imagebutton:
            xpos 1800
            ypos 0
            focus_mask True
            idle Transform("images/game_gui/icons/No_Map_Hover.png", zoom=.8)
            hover Transform("images/game_gui/icons/Map Icon Hover Cant.png", zoom=.8)
            action [Show("map_button"),Show("displayTextScreen", displayText = "Map")]
            hovered Show("displayTextScreen", displayText = "Map")
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1675
        ypos 0
        focus_mask True
        idle Transform("images/game_gui/icons/BackPack_Icon_Idle.png", zoom=.8)
        hover Transform("images/game_gui/icons/BackPack_Icon_Hover.png", zoom=.8)
        action [SetVariable("inv_page", 0),Show("inventory_screen"), Play ("sound", "sfx/zipper.mp3") ]
        hovered Show("displayTextScreen", displayText = __("Inventory"))
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1550
        ypos 0
        focus_mask True
        idle Transform("images/game_gui/icons/Phone_Icon_Idle.png", zoom=.8)
        hover Transform("images/game_gui/icons/Phone_Icon_Hover.png", zoom=.8)
        action [Show("phone_main_screen"), Play ("sound", "sfx/phone_unlock.mp3") ]
        hovered Show("displayTextScreen", displayText = "Phone")
        unhovered Hide("displayTextScreen")

    if Linda_unread_alert == False:
        add "images/game_gui/phone/sms/Alert1.png" xpos 1550 ypos 5
    elif Sara_unread_alert == False:
        add "images/game_gui/phone/sms/Alert1.png" xpos 1550 ypos 5
    elif Caroline_unread_alert == False:
        add "images/game_gui/phone/sms/Alert1.png" xpos 1550 ypos 5
    elif Zuri_unread_alert == False:
        add "images/game_gui/phone/sms/Alert1.png" xpos 1550 ypos 5
    elif Ce_unread_alert == False:
        add "images/game_gui/phone/sms/Alert1.png" xpos 1550 ypos 5

#---------------------------------------------------------------------------------------------------------

label map_label:
    $ can_hide_windows = False
    $ clickable = True
    if music_continue == True:
        $ music_continue = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    if day_time == 4:
        $ in_map=True
        scene map_night1
        hide screen map_button
        show screen week_day_viewer
        show screen day_time_viewer
        show screen time_skip_button
        call screen map
    if day_time == 3:
        $ in_map=True
        $ unlock_celia_toilet_cabin_day_scene3_v1 = 3
        $ can2_unlock_celia_toilet_cabin_day_scene4_v1 = 3
        hide screen map_button
        show screen week_day_viewer
        show screen day_time_viewer
        show screen time_skip_button
        scene map_day1
        if New_NSB_U1_can == True:
            show screen map
            call screen New_NSB_U1_scr
        call screen map
    else:
        $ in_map=True
        hide screen map_button
        show screen week_day_viewer
        show screen day_time_viewer
        show screen time_skip_button
        scene map_day1
        call screen map

screen map:

    zorder 102
    if Li_end_content == True:
        on "show" action Show("Li_end_content_scr")

    imagebutton:
        xpos 482
        ypos 443
        focus_mask True
        idle "images/game_gui/map/Home_Idle.png"
        hover "images/game_gui/map/Home_Hover.png"
        if clickable == True:
            action [SetVariable("in_map", False), Jump("entrace1_morning1"), Hide("map_button"), ]
    imagebutton:
        xpos 1403
        ypos 268
        focus_mask True
        idle "images/game_gui/map/School Normal.png"
        hover "images/game_gui/map/School Hover.png"
        if clickable == True:
            action [SetVariable("in_map", False), Jump("school_outside_morning1"), Hide("map_button"),]
    if beach_unlocked == True:
        imagebutton:
            xpos 1716
            ypos 186
            focus_mask True
            idle "images/game_gui/map/Beach Normal.png"
            hover "images/game_gui/map/Beach Hover.png"
            if clickable == True:
                action [Jump("beach_M1"), Hide("displayTextScreen")]
    if celia_house_unlocked == True:
        imagebutton:
            xpos 1230
            ypos 518
            focus_mask True
            idle "images/game_gui/map/CeliaHouse Normal.png"
            hover "images/game_gui/map/CeliaHouse Hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), Jump("Ce_ele_corridor_M1")]
    if church_unlocked == True:
        imagebutton:
            xpos 228
            ypos 315
            focus_mask True
            idle "images/game_gui/map/Church Normal.png"
            hover "images/game_gui/map/Church Hover.png"
            if clickable == True:
                action [Show("screen_work_in_progress"), Hide("displayTextScreen")]
    if cinema_unlocked == True:
        imagebutton:
            xpos 1114
            ypos 142
            focus_mask True
            idle "images/game_gui/map/Cinema Normal.png"
            hover "images/game_gui/map/Cinema Hover.png"
            if clickable == True:
                action [Show("screen_work_in_progress"), Hide("displayTextScreen")]
    if dark_alley_unlocked == True:
        imagebutton:
            xpos 1363
            ypos 906
            focus_mask True
            idle "images/game_gui/map/DarkAlley Normal.png"
            hover "images/game_gui/map/DarkAlley Hover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Jump("dark_alley_label"), Hide("displayTextScreen")]
    if gym_unlocked == True:
        imagebutton:
            xpos 991
            ypos 549
            focus_mask True
            idle "images/game_gui/map/Gym Normal.png"
            hover "images/game_gui/map/Gym Hover.png"
            if clickable == True:
                action [Show("screen_work_in_progress"), Hide("displayTextScreen")]
    if hospital_unlocked == True:
        imagebutton:
            xpos 1170
            ypos 293
            focus_mask True
            idle "images/game_gui/map/Hospital Normal.png"
            hover "images/game_gui/map/Hospital Hover.png"
            if clickable == True:
                action [Show("screen_work_in_progress"), Hide("displayTextScreen")]
    if ml_work_unloacked == True:
        imagebutton:
            xpos 411
            ypos 774
            focus_mask True
            idle "images/game_gui/map/ml_work.png"
            hover "images/game_gui/map/ml_work_hover.png"
            if clickable == True:
                action [SetVariable("in_map", False),Hide("displayTextScreen"),Jump("ml_work_day1")]
    if neighboor_unlocked == True:
        imagebutton:
            xpos 510
            ypos 415
            focus_mask True
            idle "images/game_gui/map/Neighbor1 Normal.png"
            hover "images/game_gui/map/Neighbor1 Hover.png"
            if clickable == True:
                action [Jump("Ne_entrance_M1")]
    if night_club_unlocked == True:
        imagebutton:
            xpos 377
            ypos 174
            focus_mask True
            idle "images/game_gui/map/Nightclub Normal.png"
            hover "images/game_gui/map/Nightclub Hover.png"
            if clickable == True:
                action Jump("nightclub_menu")
    imagebutton:
        xpos 362
        ypos 446
        focus_mask True
        idle "images/game_gui/map/Shop Normal.png"
        hover "images/game_gui/map/Shop Hover.png"
        if clickable == True:
            action [SetVariable("in_map", False),Hide("displayTextScreen"),Jump("shop_label")]

    imagebutton:
        xpos 395
        ypos 259
        focus_mask True
        idle "images/game_gui/map/SexShop Normal.png"
        hover "images/game_gui/map/SexShop Hover.png"
        if clickable == True:
            action [SetVariable("in_map", False),Hide("displayTextScreen"),Jump("sex_shop_label")]


    if cosplay_shop_unlocked == True:
        imagebutton:
            xpos 1165
            ypos 109
            focus_mask True
            idle "images/game_gui/map/ClothesShop.png"
            hover "images/game_gui/map/ClothesShop_hover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Hide("displayTextScreen"), Jump("cloth_shop_label")]


    if Bob_workplace_unlocked == True:
        imagebutton:
            xpos 1618
            ypos 699
            focus_mask True
            idle "images/game_gui/map/BobWorkplaceNormal.png"
            hover "images/game_gui/map/BobWorkplaceHover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Hide("displayTextScreen"), Jump("bob_work_outside_morning1")]

    if Z_home_unlocked == True:
        imagebutton:
            xpos 1023
            ypos 549
            focus_mask True
            idle "images/game_gui/map/ZuriNormal.png"
            hover "images/game_gui/map/ZuriHover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Hide("displayTextScreen"), Jump("zuri_homeoutside_M1")]

    if aunt_house_unlocked == True:
        imagebutton:
            xpos 1160
            ypos 616
            focus_mask True
            idle "images/game_gui/map/au.png"
            hover "images/game_gui/map/au_hover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Hide("displayTextScreen"), Jump("a_home_outside_M1")]

    if J_home_unlocked == True:
        imagebutton:
            xpos 15
            ypos 290
            focus_mask True
            idle "images/game_gui/map/Judy.png"
            hover "images/game_gui/map/Judy_hover.png"
            if clickable == True:
                action [Show("screen_work_in_progress"), Hide("displayTextScreen")]


    if Charles_home == True:
        imagebutton:
            xpos 100
            ypos 616
            focus_mask True
            idle "images/game_gui/map/charles_idle.png"
            hover "images/game_gui/map/charles_hover.png"
            if clickable == True:
                action [SetVariable("in_map", False), Hide("displayTextScreen"), Jump("Charles_outside2_M1")]

#-------------------------------------------------------------------------------

screen day_time_viewer:

    zorder 103
    if day_time==1:
        add Transform("images/game_gui/icons/Hud1-Morning.png", zoom=.8)

    if day_time==2:
        add Transform("images/game_gui/icons/Hud2-Afternoon.png", zoom=.8)

    if day_time==3:
        add Transform("images/game_gui/icons/Hud3-Evening.png", zoom=.8)

    if day_time==4:
        add Transform("images/game_gui/icons/Hud4-Night.png", zoom=.8)

#-------------------------------------------------------------------------------

screen week_day_viewer:

    zorder 103
    if week_day==1:

        add Transform("images/game_gui/icons/1Monday.png", zoom=.8)

    if week_day==2:

        add Transform("images/game_gui/icons/2Tuesday.png", zoom=.8)

    if week_day==3:

        add Transform("images/game_gui/icons/3Wednesday.png", zoom=.8)

    if week_day==4:
        add Transform("images/game_gui/icons/4Thursday.png", zoom=.8)

    if week_day==5:

        add Transform("images/game_gui/icons/5Friday.png", zoom=.8)

    if week_day==6:

        add Transform("images/game_gui/icons/6Saturday.png", zoom=.8)

    if week_day==7:

        add Transform("images/game_gui/icons/7Sunday.png", zoom=.8)

#-------------------------------------------------------------------------------

screen time_skip_button:

    zorder 103
    if in_map==True:
        imagebutton:
            xpos 400
            ypos 0
            focus_mask True
            idle Transform("images/game_gui/icons/Skip_Icon_Idle.png", zoom=.4)
            hover Transform("images/game_gui/icons/Skip_Icon_Hover.png", zoom=.4)
            action [Hide("displayTextScreen"), SetVariable("day_time", day_time + 1, ), Show("time_skip_button"), Jump("map_label")]
            hovered Show("displayTextScreen", displayText = __("Skip Time"))
            unhovered Hide("displayTextScreen")
    if day_time==4:
        imagebutton:
            xpos 400
            ypos 0
            focus_mask True
            idle Transform("images/game_gui/icons/No_Skip_Icon_Hover.png", zoom=.4)
            hover Transform("images/game_gui/icons/No_Skip_Icon_Idle.png", zoom=.4)
            action [SetVariable("day_time",  4), Show("time_skip_button"), Jump("map_label")]
            hovered Show("displayTextScreen", displayText = __("Skip Time"))
            unhovered Hide("displayTextScreen")
    if in_map==False:
        imagebutton:
            xpos 400
            ypos 0
            focus_mask True
            idle Transform("images/game_gui/icons/No_Skip_Icon_Hover.png", zoom=.4)
            hover Transform("images/game_gui/icons/No_Skip_Icon_Idle.png", zoom=.4)
            action [Show("time_skip_button"),]
            hovered Show("displayTextScreen", displayText = __("Skip Time"))
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 400
        ypos 60
        focus_mask True
        idle Transform("images/game_gui/icons/Help.png", zoom=.4)
        hover Transform("images/game_gui/icons/HelpHover.png", zoom=.4)
        action [Hide("displayTextScreen"), Show ("Info_screen") ]
        hovered Show("displayTextScreen", displayText = __("Help"))
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 460
        ypos 60
        focus_mask True
        idle Transform("images/game_gui/icons/Walk.png", zoom=.4)
        hover Transform("images/game_gui/icons/WalkHover.png", zoom=.4)
        action [Hide("displayTextScreen"), Show ("modmenu") ]
        hovered Show("displayTextScreen", displayText = __("Lain's Walkthrough Mod"))
        unhovered Hide("displayTextScreen")

    if jack_frost == False:
        imagebutton idle Transform("images/game_gui/icons/jack_frost.png", zoom=.4) xpos 460 ypos 0 focus_mask True action [Hide("displayTextScreen"), SetVariable('jack_frost', True) ] hovered ShowTransient("displayTextScreen", displayText = __("Secret Card Cheated")) unhovered Hide("displayTextScreen")
    else:
        imagebutton idle Transform("images/game_gui/icons/jack_frost_hover.png", zoom=.4) xpos 460 ypos 0 focus_mask True action [Hide("displayTextScreen"), SetVariable('jack_frost', False) ] hovered ShowTransient("displayTextScreen", displayText = __("Secret Card Not Cheated")) unhovered Hide("displayTextScreen")

#-----------------------------------------------------------------------------------------

screen screen_work_in_progress:
    zorder 104
    imagebutton:
        xpos 0
        ypos 0
        idle "/images/game_gui/icons/workinprogress.png"
        hover "/images/game_gui/icons/workinprogress.png"
        action Hide("screen_work_in_progress")

screen Info_screen:
    modal True
    zorder 105
    imagebutton:
        xpos 0
        ypos 0
        idle "/images/game_gui/icons/HelpShow.png"
        hover "/images/game_gui/icons/HelpShow.png"
        action Hide("Info_screen")
