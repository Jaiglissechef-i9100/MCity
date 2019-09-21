image cosplay_outfit1_p1 = "images/cosplay_minigame/1/1.jpg"
image cosplay_outfit1_p2a = "images/cosplay_minigame/1/2a.jpg"
image cosplay_outfit1_p2b = "images/cosplay_minigame/1/2b.jpg"
image cosplay_outfit1_p2c = "images/cosplay_minigame/1/2c.jpg"
image cosplay_outfit1_p3 = "images/cosplay_minigame/1/3.jpg"
image cosplay_outfit1_p3a = "images/cosplay_minigame/1/3a.jpg"
image cosplay_outfit1_p3b = "images/cosplay_minigame/1/3b.jpg"
image cosplay_outfit1_p3c = "images/cosplay_minigame/1/3c.jpg"

label cosplay_outfit1_label:
    hide screen cloth_shop_open_screen_notclickable
    scene cosplay_outfit1_p1 with dissolve
    if cosplay_outfit1_first_time == True:
        Caroline "Well? What do you think?"
        MC "Wow!"
        MC "(I’m not even sure what she’s cosplaying as - but she looks amazing!)"
        Caroline "Do you think it’ll sell well? Any ideas for how to market it?"
        MC "Yeah, it will! Umm... you could maybe try selling a bunch, around Valentine’s Day."
        Caroline "Perfect! I’ll make sure to order extra stock for February then."
        window hide
        $ cosplay_outfit1_first_time = False
        call screen outfit1_screen1
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit1_screen1

screen outfit1_screen1:
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
        action [Hide("displayTextScreen"), Jump("outfit1_down1"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_middle1"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_up1"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_rotate1"),]

label outfit1_down1:
    scene cosplay_outfit1_p2a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p2a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label

label outfit1_middle1:
    scene cosplay_outfit1_p2b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p2b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label

label outfit1_up1:
    scene cosplay_outfit1_p2c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p2c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label

label outfit1_rotate1:
    MC "Can you turn around?"
    Caroline "Sure."
    jump cosplay_outfit1_label2

label cosplay_outfit1_label2:
    scene cosplay_outfit1_p3 with dissolve
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit1_screen2

screen outfit1_screen2:
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
        action [Hide("displayTextScreen"), Jump("outfit1_down2"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_middle2"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_up2"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit1_rotate2"),]

label outfit1_down2:
    scene cosplay_outfit1_p3a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p3a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label2

label outfit1_middle2:
    scene cosplay_outfit1_p3b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p3b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label2

label outfit1_up2:
    scene cosplay_outfit1_p3c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit1_p3c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit1_label2

label outfit1_rotate2:
    MC "Can you turn around?"
    Caroline "Sure."
    jump cosplay_outfit1_label
