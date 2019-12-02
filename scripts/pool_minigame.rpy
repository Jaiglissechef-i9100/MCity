







transform rotation1:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 12



image pool_minigame_bg = "images/pool_minigame/clean1/bg.jpg"
image pool_minigame_bg2 = "images/pool_minigame/clean2/bg.jpg"
image pool_minigame_bg3 = "images/pool_minigame/clean3/bg.jpg"

image player1 = "images/pool_minigame/player/B1.png"
default clean_bar_max = 1.5
default clean_bar_value = 0
default clean_count = 0
default pool_B1 = True
default pool_B2 = True
default pool_B3 = True
default pool_B4 = True
default pool_B5 = True

default pool_B1_chosen = False
default pool_B2_chosen = False
default pool_B3_chosen = False
default pool_B4_chosen = False
default pool_B5_chosen = False
default clean_loop = 0
define barxsize = 200
define barysize = 30

label pool_minigame_not_selected:
    $ clickable = False
    if day_time == 1:
        show screen a_pool_M_scr
    if day_time == 2:
        show screen a_pool_D_scr
    if day_time == 3:
        show screen a_pool_E_scr
    if day_time == 4:
        show screen a_pool_N_scr
    if day_time <3:
        MC "Cleaning stuff has to be selected."
    else:
        MC "It's too late for cleaning the pool."
    $ clickable = True
    jump a_pool_M1

label pool_minigame_start0:
    hide screen map_button
    if LiR1_poll_minigame_can == 0:
        $ clickable = False
        if day_time == 1:
            show screen a_pool_M_scr
        if day_time == 2:
            show screen a_pool_D_scr
        if day_time == 3:
            show screen a_pool_E_scr
        if day_time == 4:
            show screen a_pool_N_scr
        MC "I should start cleaning the pool tomorrow."
        $ clickable = True
        jump a_pool_M1
    if day_time > 2:
        $ clickable = False
        if day_time == 3:
            show screen a_pool_E_scr
        if day_time == 4:
            show screen a_pool_N_scr
        MC "It's too late for cleaning the pool."
        $ clickable = True
        jump a_pool_M1

    if LiR1_poll_minigame_can == False:
        $ clickable = False
        if day_time == 1:
            show screen a_pool_M_scr
        if day_time == 2:
            show screen a_pool_D_scr
        if day_time == 3:
            show screen a_pool_E_scr
        if day_time == 4:
            show screen a_pool_N_scr

        MC "That's enough for today. I'm exhausted."
        $ clickable = True
        jump a_pool_M1
    else:
        jump pool_minigame_start

label pool_minigame_start:
    $ renpy.block_rollback()
    $ last_pressed = "a"
    $ clean_loop += 1
    $ clean_count = 0
    $ pool_B1 = True
    $ pool_B2 = True
    $ pool_B3 = True
    $ pool_B4 = True
    $ pool_B5 = True
    if persistent.skip_mg == True:
        scene black

        jump pool_minigame_end
    else:
        if clean_loop == 1:
            scene pool_minigame_bg
            call screen pool_minigame_scr
        if clean_loop == 2:
            scene pool_minigame_bg2
            call screen pool_minigame_scr2
        if clean_loop == 3:
            scene pool_minigame_bg3
            call screen pool_minigame_scr3


label pool_minigame_loop:
    $ clickable = True
    $ clean_count += 1
    $ renpy.block_rollback()
    $ clean_bar_value = 0
    $ pool_B1_chosen = False
    $ pool_B2_chosen = False
    $ pool_B3_chosen = False
    $ pool_B4_chosen = False
    $ pool_B5_chosen = False
    if clean_loop == 1:
        scene pool_minigame_bg
        call screen pool_minigame_scr
    if clean_loop == 2:
        scene pool_minigame_bg2
        call screen pool_minigame_scr2
    if clean_loop == 3:
        scene pool_minigame_bg3
        call screen pool_minigame_scr3

label pool_minigame_end:
    $ LiR1_poll_minigame_can = False
    $ Li_clean_stuff.selected = False
    $ inventory.earn(15)
    $ day_time += 1
    if clean_loop < 3:
        MC "Okay, that's enough for today. I'm exhausted. {color=#00ff00}(+15$){/color}"
        jump a_pool_M1
    else:

        $ LiR1_poll_minigame = False
        $ LiR1_poll_event_end = True
        MC "I've finally finished cleaning it. I should go and tell them. {color=#00ff00}(+15$){/color}"
        jump a_pool_M1

screen pool_minigame_scr:
    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()



    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True

    if clean_count == 0:
        add "images/pool_minigame/HUD/0.png" ypos 810 xpos 10
    if clean_count == 1:
        add "images/pool_minigame/HUD/1.png" ypos 810 xpos 10
    if clean_count == 2:
        add "images/pool_minigame/HUD/2.png" ypos 810 xpos 10
    if clean_count == 3:
        add "images/pool_minigame/HUD/3.png" ypos 810 xpos 10
    if clean_count == 4:
        add "images/pool_minigame/HUD/4.png" ypos 810 xpos 10
    if clean_count == 5:
        add "images/pool_minigame/HUD/5.png" ypos 810 xpos 10
        imagebutton:
            xpos 311
            ypos 973
            focus_mask True
            idle "images/pool_minigame/HUD/completed.png"
            hover "images/pool_minigame/HUD/completed_hover.png"
            if clickable == True:
                action [Jump("pool_minigame_end")]
                unhovered Hide("displayTextScreen")

    if pool_B1 == True:
        imagebutton:
            xpos 1333
            ypos 224
            focus_mask True
            idle "images/pool_minigame/clean1/B1.png"
            hover "images/pool_minigame/clean1/B1_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B1"), SetVariable("clickable", False), SetVariable("pool_B1_chosen", True)]
                unhovered Hide("displayTextScreen")

    if pool_B2 == True:
        imagebutton:
            xpos 1442
            ypos 775
            focus_mask True
            idle "images/pool_minigame/clean1/B2.png"
            hover "images/pool_minigame/clean1/B2_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B1"),SetVariable("clickable", False), SetVariable("pool_B2_chosen", True)]
                unhovered Hide("displayTextScreen")

    if pool_B3 == True:
        imagebutton:
            xpos 977
            ypos 786
            focus_mask True
            idle "images/pool_minigame/clean1/B3.png"
            hover "images/pool_minigame/clean1/B3_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B1"),SetVariable("clickable", False), SetVariable("pool_B3_chosen", True)]
                unhovered Hide("displayTextScreen")

    if pool_B4 == True:
        imagebutton:
            xpos 376
            ypos 678
            focus_mask True
            idle "images/pool_minigame/clean1/B4.png"
            hover "images/pool_minigame/clean1/B4_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B1"),SetVariable("clickable", False) , SetVariable("pool_B4_chosen", True)]
                unhovered Hide("displayTextScreen")

    if pool_B5 == True:
        imagebutton:
            xpos 622
            ypos 234
            focus_mask True
            idle "images/pool_minigame/clean1/B5.png"
            hover "images/pool_minigame/clean1/B5_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B1"),SetVariable("clickable", False), SetVariable("pool_B5_chosen", True)]
                unhovered Hide("displayTextScreen")

screen pool_minigame_B1:
    key "game_menu" action NullAction()
    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1880 ypos 864

    if clean_bar_value < 1.6 and last_pressed == "d":

        key "mouseup_1" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "a" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "mouseup_3" action NullAction()
    if clean_bar_value < 1.6 and last_pressed == "a":
        key "mouseup_3" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
        key "d" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
    if last_pressed == "d":
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954
    if last_pressed == "a":
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954



    if clean_bar_value > 1.5 and pool_B1_chosen == True:
        timer 0.15 action [SetVariable("pool_B1", False),Hide("pool_minigame_B1"),Jump("pool_minigame_loop")]

    if pool_B1_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/B1.png" xpos 1095 ypos 240
    if pool_B1_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/B2.png" xpos 1095 ypos 240




    if clean_bar_value > 1.5 and pool_B2_chosen == True:
        timer 0.15 action [SetVariable("pool_B2", False),Hide("pool_minigame_B1"),Jump("pool_minigame_loop")]

    if pool_B2_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 1395 ypos 540
    if pool_B2_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 1395 ypos 540




    if clean_bar_value > 1.5 and pool_B3_chosen == True:
        timer 0.15 action [SetVariable("pool_B3", False),Hide("pool_minigame_B1"),Jump("pool_minigame_loop")]

    if pool_B3_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/A1.png" xpos 785 ypos 600
    if pool_B3_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/A2.png" xpos 785 ypos 600




    if clean_bar_value > 1.5 and pool_B4_chosen == True:
        timer 0.15 action [SetVariable("pool_B4", False),Hide("pool_minigame_B1"),Jump("pool_minigame_loop")]

    if pool_B4_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 350 ypos 500
    if pool_B4_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 350 ypos 500




    if clean_bar_value > 1.5 and pool_B5_chosen == True:
        timer 0.15 action [SetVariable("pool_B5", False),Hide("pool_minigame_B1"),Jump("pool_minigame_loop")]

    if pool_B5_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/D1.png" xpos 550 ypos 200
    if pool_B5_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/D2.png" xpos 550 ypos 200



screen pool_minigame_scr2:
    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()



    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True

    if clean_count == 0:
        add "images/pool_minigame/HUD/0.png" ypos 810 xpos 10
    if clean_count == 1:
        add "images/pool_minigame/HUD/1.png" ypos 810 xpos 10
    if clean_count == 2:
        add "images/pool_minigame/HUD/2.png" ypos 810 xpos 10
    if clean_count == 3:
        add "images/pool_minigame/HUD/3.png" ypos 810 xpos 10
    if clean_count == 4:
        add "images/pool_minigame/HUD/4.png" ypos 810 xpos 10
    if clean_count == 5:
        add "images/pool_minigame/HUD/5.png" ypos 810 xpos 10
        imagebutton:
            xpos 311
            ypos 973
            focus_mask True
            idle "images/pool_minigame/HUD/completed.png"
            hover "images/pool_minigame/HUD/completed_hover.png"
            if clickable == True:
                action [Jump("pool_minigame_end")]


    if pool_B1 == True:
        imagebutton:
            xpos 1310
            ypos 261
            focus_mask True
            idle "images/pool_minigame/clean2/B1.png"
            hover "images/pool_minigame/clean2/B1_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B2"), SetVariable("clickable", False), SetVariable("pool_B1_chosen", True)]

    if pool_B2 == True:
        imagebutton:
            xpos 1565
            ypos 346
            focus_mask True
            idle "images/pool_minigame/clean2/B2.png"
            hover "images/pool_minigame/clean2/B2_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B2"), SetVariable("clickable", False), SetVariable("pool_B2_chosen", True)]

    if pool_B3 == True:
        imagebutton:
            xpos 1000
            ypos 700
            focus_mask True
            idle "images/pool_minigame/clean2/B3.png"
            hover "images/pool_minigame/clean2/B3_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B2"), SetVariable("clickable", False), SetVariable("pool_B3_chosen", True)]

    if pool_B4 == True:
        imagebutton:
            xpos 728
            ypos 538
            focus_mask True
            idle "images/pool_minigame/clean2/B4.png"
            hover "images/pool_minigame/clean2/B4_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B2"), SetVariable("clickable", False), SetVariable("pool_B4_chosen", True)]

    if pool_B5 == True:
        imagebutton:
            xpos 435
            ypos 752
            focus_mask True
            idle "images/pool_minigame/clean2/B5.png"
            hover "images/pool_minigame/clean2/B5_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B2"), SetVariable("clickable", False), SetVariable("pool_B5_chosen", True)]

screen pool_minigame_B2:
    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()
    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1880 ypos 864

    if clean_bar_value < 1.6 and last_pressed == "d":
        key "mouseup_1" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "a" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "mouseup_3" action NullAction()
    if clean_bar_value < 1.6 and last_pressed == "a":
        key "mouseup_3" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
        key "d" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
    if last_pressed == "d":
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954
    if last_pressed == "a":
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954



    if clean_bar_value > 1.5 and pool_B1_chosen == True:
        timer 0.15 action [SetVariable("pool_B1", False),Hide("pool_minigame_B2"),Jump("pool_minigame_loop")]

    if pool_B1_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/B1.png" xpos 1095 ypos 260
    if pool_B1_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/B2.png" xpos 1095 ypos 260



    if clean_bar_value > 1.5 and pool_B2_chosen == True:
        timer 0.15 action [SetVariable("pool_B2", False),Hide("pool_minigame_B2"),Jump("pool_minigame_loop")]

    if pool_B2_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/B1.png" xpos 1395 ypos 390
    if pool_B2_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/B2.png" xpos 1395 ypos 390



    if clean_bar_value > 1.5 and pool_B3_chosen == True:
        timer 0.15 action [SetVariable("pool_B3", False),Hide("pool_minigame_B2"),Jump("pool_minigame_loop")]

    if pool_B3_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 955 ypos 510
    if pool_B3_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 955 ypos 510



    if clean_bar_value > 1.5 and pool_B4_chosen == True:
        timer 0.15 action [SetVariable("pool_B4", False),Hide("pool_minigame_B2"),Jump("pool_minigame_loop")]

    if pool_B4_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 755 ypos 350
    if pool_B4_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 755 ypos 350



    if clean_bar_value > 1.5 and pool_B5_chosen == True:
        timer 0.15 action [SetVariable("pool_B5", False),Hide("pool_minigame_B2"),Jump("pool_minigame_loop")]

    if pool_B5_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 395 ypos 600
    if pool_B5_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 395 ypos 600



screen pool_minigame_scr3:
    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()



    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True

    if clean_count == 0:
        add "images/pool_minigame/HUD/0.png" ypos 810 xpos 10
    if clean_count == 1:
        add "images/pool_minigame/HUD/1.png" ypos 810 xpos 10
    if clean_count == 2:
        add "images/pool_minigame/HUD/2.png" ypos 810 xpos 10
    if clean_count == 3:
        add "images/pool_minigame/HUD/3.png" ypos 810 xpos 10
    if clean_count == 4:
        add "images/pool_minigame/HUD/4.png" ypos 810 xpos 10
    if clean_count == 5:
        add "images/pool_minigame/HUD/5.png" ypos 810 xpos 10
        imagebutton:
            xpos 311
            ypos 973
            focus_mask True
            idle "images/pool_minigame/HUD/completed.png"
            hover "images/pool_minigame/HUD/completed_hover.png"
            if clickable == True:
                action [Jump("pool_minigame_end")]


    if pool_B1 == True:
        imagebutton:
            xpos 1650
            ypos 357
            focus_mask True
            idle "images/pool_minigame/clean3/B1.png"
            hover "images/pool_minigame/clean3/B1_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B3"), SetVariable("clickable", False), SetVariable("pool_B1_chosen", True)]

    if pool_B2 == True:
        imagebutton:
            xpos 1522
            ypos 336
            focus_mask True
            idle "images/pool_minigame/clean3/B2.png"
            hover "images/pool_minigame/clean3/B2_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B3"), SetVariable("clickable", False), SetVariable("pool_B2_chosen", True)]

    if pool_B3 == True:
        imagebutton:
            xpos 1148
            ypos 718
            focus_mask True
            idle "images/pool_minigame/clean3/B3.png"
            hover "images/pool_minigame/clean3/B3_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B3"), SetVariable("clickable", False), SetVariable("pool_B3_chosen", True)]

    if pool_B4 == True:
        imagebutton:
            xpos 630
            ypos 521
            focus_mask True
            idle "images/pool_minigame/clean3/B4.png"
            hover "images/pool_minigame/clean3/B4_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B3"), SetVariable("clickable", False), SetVariable("pool_B4_chosen", True)]

    if pool_B5 == True:
        imagebutton:
            xpos 425
            ypos 721
            focus_mask True
            idle "images/pool_minigame/clean3/B5.png"
            hover "images/pool_minigame/clean3/B5_hover.png"
            if clickable == True:
                action [Show("pool_minigame_B3"), SetVariable("clickable", False), SetVariable("pool_B5_chosen", True)]

screen pool_minigame_B3:
    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()
    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1880 ypos 864

    if clean_bar_value < 1.6 and last_pressed == "d":
        key "mouseup_1" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "a" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "a")]
        key "mouseup_3" action NullAction()
    if clean_bar_value < 1.6 and last_pressed == "a":
        key "mouseup_3" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
        key "d" action [SetVariable("clean_bar_value", clean_bar_value + 0.30),SetVariable("last_pressed", "d")]
    if last_pressed == "d":
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954
    if last_pressed == "a":
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954



    if clean_bar_value > 1.5 and pool_B1_chosen == True:
        timer 0.15 action [SetVariable("pool_B1", False),Hide("pool_minigame_B3"),Jump("pool_minigame_loop")]

    if pool_B1_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/B1.png" xpos 1395 ypos 360
    if pool_B1_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/B2.png" xpos 1395 ypos 360



    if clean_bar_value > 1.5 and pool_B2_chosen == True:
        timer 0.15 action [SetVariable("pool_B2", False),Hide("pool_minigame_B3"),Jump("pool_minigame_loop")]

    if pool_B2_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/B1.png" xpos 1295 ypos 320
    if pool_B2_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/B2.png" xpos 1295 ypos 320



    if clean_bar_value > 1.5 and pool_B3_chosen == True:
        timer 0.15 action [SetVariable("pool_B3", False),Hide("pool_minigame_B3"),Jump("pool_minigame_loop")]

    if pool_B3_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 1095 ypos 520
    if pool_B3_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 1095 ypos 520



    if clean_bar_value > 1.5 and pool_B4_chosen == True:
        timer 0.15 action [SetVariable("pool_B4", False),Hide("pool_minigame_B3"),Jump("pool_minigame_loop")]

    if pool_B4_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/A1.png" xpos 495 ypos 320
    if pool_B4_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/A2.png" xpos 495 ypos 320



    if clean_bar_value > 1.5 and pool_B5_chosen == True:
        timer 0.15 action [SetVariable("pool_B5", False),Hide("pool_minigame_B3"),Jump("pool_minigame_loop")]

    if pool_B5_chosen == True and last_pressed == "d":
        add "images/pool_minigame/player/C1.png" xpos 395 ypos 520
    if pool_B5_chosen == True and last_pressed == "a":
        add "images/pool_minigame/player/C2.png" xpos 395 ypos 520