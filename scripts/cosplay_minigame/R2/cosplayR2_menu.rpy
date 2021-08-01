default CR2_outfits_counter = 0
default CR2_outfit4_locked = True

default outfit1_R2_1stTime = True
default outfit2_R2_1stTime = True
default outfit3_R2_1stTime = True
default outfit4_R2_1stTime = True

screen cosplayR2_menu_screen:
    modal True
    add "images/cosplay_minigame/R2/CosplaySelect/Outfits.png"
    imagebutton:
        xpos 790
        ypos 324
        focus_mask True
        idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay1Normal.png"
        hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay1Hover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_R2_label"),]

    imagebutton:
        xpos 982
        ypos 324
        focus_mask True
        idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay2Normal.png"
        hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay2Hover.png"
        action [Hide("displayTextScreen"), Jump("outfit2_R2_label"),]

    imagebutton:
        xpos 790
        ypos 510
        focus_mask True
        if CR2_outfits_counter < 2:
            idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay3Locked.png"
            hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay3Locked.png"
        if CR2_outfits_counter >= 2:
            idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay3Normal.png"
            hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay3Hover.png"
            action [Hide("displayTextScreen"), Jump("outfit3_R2_label"),]

    imagebutton:
        xpos 982
        ypos 510
        focus_mask True
        if CR2_outfit4_locked == True:
            idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay4Locked.png"
            hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay4Locked.png"
        else:
            idle "images/cosplay_minigame/R2/CosplaySelect/Cosplay4Normal.png"
            hover "images/cosplay_minigame/R2/CosplaySelect/Cosplay4Hover.png"
            action [Hide("displayTextScreen"), Jump("outfit4_R2_label"),]

    imagebutton:
        xpos 1104
        ypos 209
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [Hide ("cosplayR2_menu_screen"),Jump("cosplay_CR3_close")]

