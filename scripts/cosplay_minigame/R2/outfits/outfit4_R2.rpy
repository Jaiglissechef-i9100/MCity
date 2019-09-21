image outfit4_R2_p1 = "images/cosplay_minigame/R2/4/1.jpg"
image outfit4_R2_p2a = "images/cosplay_minigame/R2/4/2a.jpg"
image outfit4_R2_p2b = "images/cosplay_minigame/R2/4/2b.jpg"
image outfit4_R2_p2c = "images/cosplay_minigame/R2/4/2c.jpg"
image outfit4_R2_p3 = "images/cosplay_minigame/R2/4/3.jpg"
image outfit4_R2_p3a = "images/cosplay_minigame/R2/4/3a.jpg"
image outfit4_R2_p3b = "images/cosplay_minigame/R2/4/3b.jpg"
image outfit4_R2_p3c = "images/cosplay_minigame/R2/4/3c.jpg"

label outfit4_R2_label:

    if outfit4_R2_1stTime == True:

        scene black
        Caroline "Hmm… Feel free to put away the camera."
        MC "Why?"
        Caroline "This one… um… doesn’t fit properly."
        MC "I’m sure it’ll be fine!"
        Caroline "I… It’s really not."
        MC "Oh, come on! How bad can it be?"

        scene outfit4_R2_p1 with dissolve

        MC "Holy shit!"
        Caroline "(Gulp)"
        MC "That is… Wow!"
        MC "I mean… holy fucking shit!"
        Caroline "God... this is so embarrassing."
        MC "No! It’s awesome! You’ll sell shit-loads of these when people see you online, modelling it!"
        Caroline "Y-You really think so?"
        MC "Absolutely! Now act confident, lean in, and smile for the camera!"

        window hide
        $ outfit4_R2_1stTime = False
        call screen outfit4R2_scr1

    scene outfit4_R2_p1 with dissolve

    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ CR2_outfits_counter += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        $ CR2_outfit4_locked = False
        if can_CR2_AS2 == True:
            $ can_CR2_AS2 = False
            $ CR2_AS2 = True
        call screen cosplay_menu_score_screen
    call screen outfit4R2_scr1

screen outfit4R2_scr1:
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
        action [Hide("displayTextScreen"), Jump("outfit4_R2_down1"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_middle1"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_up1"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_rotate1"),]

label outfit4_R2_down1:
    scene outfit4_R2_p2a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p2a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label

label outfit4_R2_middle1:
    scene outfit4_R2_p2b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p2b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label

label outfit4_R2_up1:
    scene outfit4_R2_p2c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p2c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label

label outfit4_R2_rotate1:
    MC "Can you turn around?"
    Caroline "Sure."
    jump outfit4_R2_label2

label outfit4_R2_label2:
    scene outfit4_R2_p3 with dissolve
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ CR2_outfits_counter += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        $ CR2_outfit4_locked = False
        if can_CR2_AS2 == True:
            $ can_CR2_AS2 = False
            $ CR2_AS2 = True
        call screen cosplay_menu_score_screen
    call screen outfit4_scr2

screen outfit4_scr2:
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
        action [Hide("displayTextScreen"), Jump("outfit4_R2_down2"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_middle2"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_up2"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_R2_rotate2"),]

label outfit4_R2_down2:
    scene outfit4_R2_p3a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p3a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label2

label outfit4_R2_middle2:
    scene outfit4_R2_p3b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p3b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label2

label outfit4_R2_up2:
    scene outfit4_R2_p3c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene outfit4_R2_p3c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump outfit4_R2_label2

label outfit4_R2_rotate2:
    MC "Can you turn around?"
    Caroline "Sure."
    jump outfit4_R2_label
