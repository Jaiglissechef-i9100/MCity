image cosplay_menu_p1 = "images/cosplay_minigame/1/1.jpg"
default cosplay_unlock_switch = 0
default cosplay_score = 0
default cosplay_pic_count = 0
default cosplay_score_add = 0
default cosplay_score1 = 0
define flash3 = Fade(0.3, 0.2, 1, color="#fff")

default cosplay_outfit1_first_time = True
default cosplay_outfit2_first_time = True
default cosplay_outfit3_first_time = True
default cosplay_outfit4_first_time = True
default cosplay_outfit5_first_time = True
label cosplay_menu_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    $ cosplay_score1 = cosplay_score
    $ cosplay_score = 0
    if Caroline_points == 1:
        call screen cosplay_menu_screen
    if Caroline_points == 2:
        call screen cosplayR2_menu_screen

screen cosplay_menu_screen:
    modal True
    add "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Outfits.png"
    imagebutton:
        xpos 720
        ypos 330
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay1Normal.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay1Hover.png"
        action [Hide("displayTextScreen"), Jump("cosplay_outfit1_label"),]
    imagebutton:
        xpos 894
        ypos 330
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay2Normal.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay2Hover.png"
        action [Hide("displayTextScreen"), Jump("cosplay_outfit2_label"),]
    imagebutton:
        xpos 1067
        ypos 330
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay3Normal.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay3Hover.png"
        action [Hide("displayTextScreen"), Jump("cosplay_outfit3_label"),]
    imagebutton:
        xpos 720
        ypos 524
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay4Normal.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay4Hover.png"
        action [Hide("displayTextScreen"), Jump("cosplay_outfit4_label"),]
    if cosplay_unlock_switch >= 2:
        imagebutton:
            xpos 894
            ypos 524
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay5Normal.png"
            hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay5Hover.png"
            action [Hide("displayTextScreen"), Jump("cosplay_outfit5_label"),]
    if cosplay_unlock_switch <= 1:
        imagebutton:
            xpos 894
            ypos 524
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay5Locked.png"
    if cosplay_unlock_switch >= 4:
        imagebutton:
            xpos 1067
            ypos 524
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay6Normal.png"
            hover "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay6Hover.png"
            action [Hide("displayTextScreen"), Jump("cosplay_outfit6_label1"),]
    if cosplay_unlock_switch <= 3:
        imagebutton:
            xpos 1067
            ypos 524
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplaySelection/Cosplay6Locked.png"

    imagebutton:
        xpos 1104
        ypos 209
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [Hide ("cosplay_menu_screen"),Jump("cosplay_CR3_close")]




screen cosplay_menu_score_screen:
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/CompleteReward.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/CompleteReward.png"
        action [Hide("displayTextScreen"), Jump("cosplay_end_label"),]
    if Caroline_points != 2:
        text "{size=+25}{color=#00ff00}[cosplay_score]${/size}" xpos 1000 ypos 510
    if Caroline_points == 2:
        text "{size=+25}{color=#00ff00}0${/size}" xpos 1000 ypos 510
        text "{color=#00ff00}(Deal with Caroline is active.)" xpos 780 ypos 600
    imagebutton:
        xpos 1679
        ypos 0
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ScoreCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_score1]{/color}{/size}" xpos 1832 ypos 8

label cosplay_end_label:

    if Caroline_points == 1:
        $ inventory.earn(cosplay_score)
        $ day_time +=1
        if caroline_after_cosplay_outfit5 == True:
            jump caroline_cloth_shop_afternoon_scene2_label
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump map_label
    if Caroline_points == 2:
        $ day_time +=1
        if CR2_AS1 == True:
            jump CR2_AS1_label
        if CR2_AS2 == True:
            jump CR2_AS2_label
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump map_label

    if Caroline_points == 3:
        if CR3_deal_aff == True:
            $ inventory.earn(cosplay_score)
        $ day_time +=1
        if CR3_AS5_can == 2:
            $ CR3_AS5 = True
        if outfit_start == 3 and C_R3_outfit3.t_played == 1:
            jump CR3_AS8_O3_con2
        if outfit_start == 4 and C_R3_outfit4.t_played == 1:
            jump CR3_AS9_O4_con2
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump map_label