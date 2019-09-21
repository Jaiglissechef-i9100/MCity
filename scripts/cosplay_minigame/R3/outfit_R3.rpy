image O1_R3_p1 = "images/cosplay_minigame/R3/1/1.jpg"
image O1_R3_p2a = "images/cosplay_minigame/R3/1/2a.jpg"
image O1_R3_p2b = "images/cosplay_minigame/R3/1/2b.jpg"
image O1_R3_p2c = "images/cosplay_minigame/R3/1/2c.jpg"
image O1_R3_p3 = "images/cosplay_minigame/R3/1/3.jpg"
image O1_R3_p3a = "images/cosplay_minigame/R3/1/3a.jpg"
image O1_R3_p3b = "images/cosplay_minigame/R3/1/3b.jpg"
image O1_R3_p3c = "images/cosplay_minigame/R3/1/3c.jpg"

image O2_R3_p1 = "images/cosplay_minigame/R3/2/1.jpg"
image O2_R3_p2a = "images/cosplay_minigame/R3/2/2a.jpg"
image O2_R3_p2b = "images/cosplay_minigame/R3/2/2b.jpg"
image O2_R3_p2c = "images/cosplay_minigame/R3/2/2c.jpg"
image O2_R3_p3 = "images/cosplay_minigame/R3/2/3.jpg"
image O2_R3_p3a = "images/cosplay_minigame/R3/2/3a.jpg"
image O2_R3_p3b = "images/cosplay_minigame/R3/2/3b.jpg"
image O2_R3_p3c = "images/cosplay_minigame/R3/2/3c.jpg"

image O3_R3_p1 = "images/cosplay_minigame/R3/3/1.jpg"
image O3_R3_p2a = "images/cosplay_minigame/R3/3/2a.jpg"
image O3_R3_p2b = "images/cosplay_minigame/R3/3/2b.jpg"
image O3_R3_p2c = "images/cosplay_minigame/R3/3/2c.jpg"
image O3_R3_p3 = "images/cosplay_minigame/R3/3/3.jpg"
image O3_R3_p3a = "images/cosplay_minigame/R3/3/3a.jpg"
image O3_R3_p3b = "images/cosplay_minigame/R3/3/3b.jpg"
image O3_R3_p3c = "images/cosplay_minigame/R3/3/3c.jpg"

image O4_R3_p1 = "images/cosplay_minigame/R3/4/1.jpg"
image O4_R3_p2a = "images/cosplay_minigame/R3/4/2a.jpg"
image O4_R3_p2b = "images/cosplay_minigame/R3/4/2b.jpg"
image O4_R3_p2c = "images/cosplay_minigame/R3/4/2c.jpg"
image O4_R3_p3 = "images/cosplay_minigame/R3/4/3.jpg"
image O4_R3_p3a = "images/cosplay_minigame/R3/4/3a.jpg"
image O4_R3_p3b = "images/cosplay_minigame/R3/4/3b.jpg"
image O4_R3_p3c = "images/cosplay_minigame/R3/4/3c.jpg"

default outfit_start = 1
label outfit_R3_start:

    $ cosplay_score1 = cosplay_score
    $ cosplay_score = 0
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if outfit_start == 1:
        $ outfit_list = ["O1_R3_p2a","O1_R3_p2b","O1_R3_p2c","O1_R3_p3a","O1_R3_p3b","O1_R3_p3c"]
        $ outfit_pos_normal = "O1_R3_p1"
    if outfit_start == 2:
        $ outfit_list = ["O2_R3_p2a","O2_R3_p2b","O2_R3_p2c","O2_R3_p3a","O2_R3_p3b","O2_R3_p3c"]
        $ outfit_pos_normal = "O2_R3_p1"
    if outfit_start == 3:
        $ outfit_list = ["O3_R3_p2a","O3_R3_p2b","O3_R3_p2c","O3_R3_p3a","O3_R3_p3b","O3_R3_p3c"]
        $ outfit_pos_normal = "O3_R3_p1"
    if outfit_start == 4:
        $ outfit_list = ["O4_R3_p2a","O4_R3_p2b","O4_R3_p2c","O4_R3_p3a","O4_R3_p3b","O4_R3_p3c"]
        $ outfit_pos_normal = "O4_R3_p1"
    $ outfit_list_roll = []
    $ outfit_chosen = []
    jump outfit_R3_loop

label outfit_R3_loop:

    $ outfit_list_rolled = renpy.random.choice(outfit_list)
    $ outfit_list_roll.append(outfit_list_rolled)
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_R3_score_screen
    call screen outfit1_R3_scr1

label outfit_R3_loop1:

    $ outfit_list_roll.remove(outfit_list_rolled)
    $ outfit_chosen.remove(outfit_chosen1)
    $ outfit_list_rolled = renpy.random.choice(outfit_list)
    $ outfit_list_roll.append(outfit_list_rolled)
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_R3_score_screen
    call screen outfit1_R3_scr1

screen outfit1_R3_scr1:

    add outfit_pos_normal
    add "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/P_Frame.png" xpos 89 ypos 72
    add outfit_list_rolled xpos 100 ypos 84 at outfit_R3_transform

    imagebutton:
        xpos 1679
        ypos 0
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ScoreCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_score]{/color}{/size}" xpos 1832 ypos 8
    imagebutton:
        xpos 1679
        ypos 73
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/PicCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_pic_count]/4{/color}{/size}" xpos 1800 ypos 78
    imagebutton:
        xpos 1680
        ypos 623
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDown.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDownHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_R3_down"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_R3_middle"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_R3_up"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Jump("outfit_R3_rotate"),]

label outfit1_R3_down:

    if outfit_start == 1:
        if outfit_pos_normal == "O1_R3_p1":
            $ outfit_chosen1 = "O1_R3_p2a"
        else:
            $ outfit_chosen1 = "O1_R3_p3a"

    if outfit_start == 2:
        if outfit_pos_normal == "O2_R3_p1":
            $ outfit_chosen1 = "O2_R3_p2a"
        else:
            $ outfit_chosen1 = "O2_R3_p3a"

    if outfit_start == 3:
        if outfit_pos_normal == "O3_R3_p1":
            $ outfit_chosen1 = "O3_R3_p2a"
        else:
            $ outfit_chosen1 = "O3_R3_p3a"

    if outfit_start == 4:
        if outfit_pos_normal == "O4_R3_p1":
            $ outfit_chosen1 = "O4_R3_p2a"
        else:
            $ outfit_chosen1 = "O4_R3_p3a"

    $ outfit_chosen.append(outfit_chosen1)
    call screen outfit1_R3_confirm_scr

label outfit1_R3_middle:

    if outfit_start == 1:
        if outfit_pos_normal == "O1_R3_p1":
            $ outfit_chosen1 = "O1_R3_p2b"
        else:
            $ outfit_chosen1 = "O1_R3_p3b"

    if outfit_start == 2:
        if outfit_pos_normal == "O2_R3_p1":
            $ outfit_chosen1 = "O2_R3_p2b"
        else:
            $ outfit_chosen1 = "O2_R3_p3b"

    if outfit_start == 3:
        if outfit_pos_normal == "O3_R3_p1":
            $ outfit_chosen1 = "O3_R3_p2b"
        else:
            $ outfit_chosen1 = "O3_R3_p3b"

    if outfit_start == 4:
        if outfit_pos_normal == "O4_R3_p1":
            $ outfit_chosen1 = "O4_R3_p2b"
        else:
            $ outfit_chosen1 = "O4_R3_p3b"
    $ outfit_chosen.append(outfit_chosen1)
    call screen outfit1_R3_confirm_scr

label outfit1_R3_up:

    if outfit_start == 1:
        if outfit_pos_normal == "O1_R3_p1":
            $ outfit_chosen1 = "O1_R3_p2c"
        else:
            $ outfit_chosen1 = "O1_R3_p3c"

    if outfit_start == 2:
        if outfit_pos_normal == "O2_R3_p1":
            $ outfit_chosen1 = "O2_R3_p2c"
        else:
            $ outfit_chosen1 = "O2_R3_p3c"

    if outfit_start == 3:
        if outfit_pos_normal == "O3_R3_p1":
            $ outfit_chosen1 = "O3_R3_p2c"
        else:
            $ outfit_chosen1 = "O3_R3_p3c"

    if outfit_start == 4:
        if outfit_pos_normal == "O4_R3_p1":
            $ outfit_chosen1 = "O4_R3_p2c"
        else:
            $ outfit_chosen1 = "O4_R3_p3c"
    $ outfit_chosen.append(outfit_chosen1)
    call screen outfit1_R3_confirm_scr

label outfit1_R3_confirm:

    show screen outfit1_R3_confirm_scr
    $ clickable = False
    if outfit_chosen != outfit_list_roll:
        $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        $ cosplay_score = cosplay_score - cosplay_score_add
        if cosplay_score <0:
            $ cosplay_score =0
        $ renpy.pause(1,hard=True)
        $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
        scene white with flash3
        $ cosplay_score_add = 0
        $ cosplay_pic_count += 1
        $ renpy.pause(1, hard = True)
        $ outfit_list_roll.remove(outfit_list_rolled)
        $ outfit_chosen.remove(outfit_chosen1)
        $ outfit_list.remove(outfit_list_rolled)
        $ clickable = True
        hide screen outfit1_R3_confirm_scr
        jump outfit_R3_loop
    else:

        $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        $ cosplay_score = cosplay_score + cosplay_score_add
        $ renpy.pause(1,hard=True)
        $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
        scene white with flash3
        $ cosplay_score_add = 0
        $ cosplay_pic_count += 1
        $ outfit_list_roll.remove(outfit_list_rolled)
        $ outfit_chosen.remove(outfit_chosen1)
        $ outfit_list.remove(outfit_list_rolled)
        $ renpy.pause(1, hard = True)
        $ clickable = True
        hide screen outfit1_R3_confirm_scr
        jump outfit_R3_loop

label outfit_R3_rotate:

    if outfit_start == 1:

        if outfit_pos_normal == "O1_R3_p1":
            scene O1_R3_p1
            $ outfit_pos_normal = "O1_R3_p3"
        else:
            scene O1_R3_p3
            $ outfit_pos_normal = "O1_R3_p1"

    if outfit_start == 2:
        if outfit_pos_normal == "O2_R3_p1":
            scene O2_R3_p1
            $ outfit_pos_normal = "O2_R3_p3"
        else:
            scene O2_R3_p3
            $ outfit_pos_normal = "O2_R3_p1"
    if outfit_start == 3:
        if outfit_pos_normal == "O3_R3_p1":
            scene O3_R3_p1
            $ outfit_pos_normal = "O3_R3_p3"
        else:
            scene O3_R3_p3
            $ outfit_pos_normal = "O3_R3_p1"
    if outfit_start == 4:
        if outfit_pos_normal == "O4_R3_p1":
            scene O4_R3_p1
            $ outfit_pos_normal = "O4_R3_p3"
        else:
            scene O4_R3_p3
            $ outfit_pos_normal = "O4_R3_p1"

    MC "Can we change position, Caroline?"
    Caroline "Sure."
    call screen outfit1_R3_scr1 with dissolve

screen outfit1_R3_confirm_scr:

    add outfit_chosen1
    if clickable == True:
        imagebutton:
            xpos 1808
            ypos 488
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/accept.png"
            hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/accept_hover.png"
            action [Jump("outfit1_R3_confirm")]

        imagebutton:
            xpos 1680
            ypos 488
            focus_mask True
            idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
            hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
            action [Jump("outfit_R3_loop1")]

screen cosplay_R3_score_screen:
    add outfit_pos_normal
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/CompleteReward.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/CompleteReward.png"
        action [Hide("displayTextScreen"), Jump("cosplay_end_label"),]
    if CR3_deal_aff == True:
        text "{size=+25}{color=#00ff00}[cosplay_score]${/size}" xpos 1000 ypos 510
    else:
        text "{size=+25}{color=#00ff00}0${/size}" xpos 1000 ypos 510
        text "{color=#00ff00}(Deal with Caroline is active.)" xpos 780 ypos 600
    imagebutton:
        xpos 1679
        ypos 0
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ScoreCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_score1]{/color}{/size}" xpos 1832 ypos 8
transform outfit_R3_transform:
    zoom 0.18
