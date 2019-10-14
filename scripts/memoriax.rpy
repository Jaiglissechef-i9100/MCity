transform timer_anim:
    zoom 1.15
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    zoom 1.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    repeat
transform cards_anim:
    xalign 5.0
    linear 0.4 xalign 0.0
    linear 0.2 xalign 0.5
default memoriax_bet10 = False
default memoriax_bet25 = False
default memoriax_bet50 = False
default memo_w = 0
default memo_l = 0
init python:
    renpy.music.register_channel("memoriax_m", mixer="sfx", loop=False)
init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    image C1 = "memoriax/card1.png"
    image C2 = "memoriax/card2.png"
    image C3 = "memoriax/card3.png"
    image C4 = "memoriax/card4.png"
    image C5 = "memoriax/card5.png"
    image C6 = "memoriax/card6.png"
    image C7 = "memoriax/card7.png"
    image C8 = "memoriax/card8.png"
    image C9 = "memoriax/card9.png"
    image C10 = "memoriax/card10.png"
    image C11 = "memoriax/card11.png"
    image C12 = "memoriax/card12.png"
    image C13 = "memoriax/card13.png"
    image C14 = "memoriax/card14.png"
    image C15 = "memoriax/card15.png"
    image C16 = "memoriax/card16.png"
    image C17 = "memoriax/card17.png"
    image C18 = "memoriax/card18.png"
    image C19 = "memoriax/card19.png"
    image C20 = "memoriax/card20.png"
    image C_Idle = "memoriax/CardNormal.png"
    image C_Hover = "memoriax/CardHover.png"
    image memoriax_bg1 = "images/memoriax/background.jpg"

screen memoraix_bet:
    key "hide_windows" action NullAction()
    add "images/memoriax/background.jpg"

    modal True
    vbox xalign 0.01 yalign 0.99:
        frame:
            xmaximum 200
            style "frame_gui1"
            text __("W:{color=#00ff00}[memo_w]{/color} L:{color=#f00}[memo_l]{/color}")
    vbox xalign 0.95 yalign 0.01 spacing 20:
        frame:
            style "frame_gui1"
            text "$"+str(inventory.money) size 50

    imagebutton:
        xpos 1414
        ypos 5
        focus_mask True
        idle Transform("images/memoriax/HelpNormal.png")
        hover Transform("images/memoriax/HelpHover.png")
        action NullAction()
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 374
        ypos 332
        focus_mask True
        idle Transform("images/memoriax/Bet10Normal.png")
        hover Transform("images/memoriax/Bet10Hover.png")
        clicked [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"), Jump("memoraix_bet10_label"),]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 806
        ypos 332
        focus_mask True
        idle Transform("images/memoriax/Bet25Normal.png")
        hover Transform("images/memoriax/Bet25Hover.png")
        clicked [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"), Jump("memoraix_bet25_label"),]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1237
        ypos 332
        focus_mask True
        idle Transform("images/memoriax/Bet50Normal.png")
        hover Transform("images/memoriax/Bet50Hover.png")
        clicked [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"), Jump("memoraix_bet50_label"),]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 850
        ypos 792
        focus_mask True
        idle Transform("images/memoriax/ExitNormal.png")
        hover Transform("images/memoriax/ExitHover.png")
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"), Hide("memoriax_again_screen"),Hide("memoraix_bet"), Jump("pc_icon_label"),]
        unhovered Hide("displayTextScreen")

screen memoriax_scr:
    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    add "images/memoriax/BackGround2.jpg"

    if memo_timer >0.1:
        timer 0.1 action If (memo_timer > 0.1, SetVariable("memo_timer", memo_timer - 0.1), Jump("memoriax_game_lose") ) repeat True

    if memo_timer >10:
        text str("{size=+20}{color=#00ff00}[memo_timer]{/color}{/size}") xalign 0.54 yalign 0.014
    if memo_timer <10 and memo_timer > 0.1:
        timer 1.9 action [Play ("memoriax_m", "sfx/lose1.wav")]
        text str("{size=+20}{color=#f00}[memo_timer]{/color}{/size}") xalign 0.54 yalign 0.014 at timer_anim

    elif memo_timer <0.1:
        timer 0.1 action Jump("memoriax_game_lose")
        text str("{size=+20}{color=#f00}0{/color}{/size}") xalign 0.54 yalign 0.014

    vbox xalign 0.95 yalign 0.01 spacing 20:
        frame:
            style "frame_gui1"
            text str(__("{size=+18} Turns Left:{color=#00ff00}[turns_left] {/color}{/size}"))

    $ a = cards_gird
    $ b = cards_gird2
    grid a b:

        xalign 0.5
        yalign 0.5
        spacing 50
        at cards_anim
        for card in cards_list:
            imagebutton:

                if card["c_chosen"]:

                    idle (card["c_value"])
                    hover (card["c_value"])
                else:
                    idle ("C_Idle")
                    hover Transform("C_Hover",zoom=0.98)

                if memo_timer >0.1:
                    action If ( (card["c_chosen"] or not can_click), None, [Play ("sound", "sfx/card_flip.wav"),SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )

screen memoriax_wonmoney_fuckminigames:
    modal True
    key "hide_windows" action NullAction()
    add "images/RPS_minigame/E-Won.png"
    if memoriax_bet10 == True:
        text "{size=+25}{color=#00ff00}+20{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet25 == True:
        text "{size=+25}{color=#00ff00}+50{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet50 == True:
        text "{size=+25}{color=#00ff00}+100{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    timer 0.5 action [Hide("displayTextScreen"), Hide("screen_memoriax_wonmoney_fuckminigames"), Jump("memoriax_label")]

label memoriax_label:
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    scene memoriax_bg1
    call screen memoraix_bet

label memoraix_bet10_label:
    $ renpy.block_rollback()
    if inventory.money >= 10:
        $ inventory.drop_money(10)
        $ memoriax_bet10 = True
        hide screen memoraix_bet
        jump memoriax_game_roll
    else:
        hide screen memoraix_bet
        jump memoriax_label
label memoraix_bet25_label:
    $ renpy.block_rollback()
    if inventory.money >= 25:
        $ inventory.drop_money(25)
        $ memoriax_bet25 = True
        hide screen memoraix_bet
        jump memoriax_game_roll
    else:
        hide screen memoraix_bet
        jump memoriax_label
label memoraix_bet50_label:
    $ renpy.block_rollback()
    if inventory.money >= 50:
        $ inventory.drop_money(50)
        $ memoriax_bet50 = True
        hide screen memoraix_bet
        jump memoriax_game_roll
    else:
        hide screen memoraix_bet
        jump memoriax_label

label memoriax_game_roll:
    $ values_list_roll = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19"]
    $ values_list_rolled = []
    if memoriax_bet10 == True:
        $ turns_left_roll = 2
        $ memo_timer = 38
        $ cards_number = 6
        $ cards_gird = 4
        $ cards_gird2 = 3
        jump memoriax_cards_roll
    if memoriax_bet25 == True:
        $ turns_left_roll = renpy.random.choice([2,3,])
        if turns_left_roll == 2:
            $ cards_number = 8
            $ memo_timer = 75
            $ cards_gird = 8
            $ cards_gird2 = 2
        if turns_left_roll == 3:
            $ memo_timer = 66
            $ cards_gird = 6
            $ cards_gird2 = 3
            $ cards_number = 6
        jump memoriax_cards_roll
    if memoriax_bet50 == True:
        $ turns_left_roll = renpy.random.choice([3,4])
        $ cards_gird = 8
        $ cards_gird2 = 3

        if turns_left_roll == 4:
            $ memo_timer = 80
            $ cards_number = 6
        if turns_left_roll == 3:
            $ memo_timer = 88
            $ cards_number = 8
        jump memoriax_cards_roll

        label memoriax_cards_roll:
            if cards_number > 0:
                $ card_roll = renpy.random.choice(values_list_roll)
                if turns_left_roll == 4:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)

                if turns_left_roll == 3:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)

                if turns_left_roll == 2:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                $ values_list_roll.remove(card_roll)
                $ cards_number -= 1
                jump memoriax_cards_roll
            else:
                jump memoriax_game

label memoriax_game:
    menu:
        "Play":
            $ renpy.block_rollback()
            window hide

            $ values_list = values_list_rolled

            $ values_list = cards_shuffle(values_list)
            $ cards_list = []

            python:
                for i in range (0, len(values_list) ):
                    cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )

            $ renpy.sound.play("sfx/card_slide.wav")
            show screen memoriax_scr

            label memoriax_game_loop:
                $ can_click = True
                $ turned_cards_numbers = []
                $ turned_cards_values = []

                if turns_left_roll == 2:
                    $ turns_left = 2
                if turns_left_roll == 3:
                    $ turns_left = 3
                if turns_left_roll == 4:
                    $ turns_left = 4

                label turns_loop:
                    if turns_left > 0:
                        $ result = ui.interact()
                        $ memo_timer = memo_timer
                        $ turned_cards_numbers.append (cards_list[result]["c_number"])
                        $ turned_cards_values.append (cards_list[result]["c_value"])
                        $ turns_left -= 1
                        jump turns_loop

                $ can_click = False

                if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
                    $ renpy.sound.play("sfx/failure01.wav")
                    $ renpy.pause (1.0, hard = True)
                    $ renpy.sound.play("sfx/card_flip.wav")
                    python:
                        for i in range (0, len(turned_cards_numbers) ):
                            cards_list[turned_cards_numbers[i]]["c_chosen"] = False
                else:

                    $ renpy.sound.play("sfx/correct2.wav")
                    $ renpy.pause (1.0, hard = True)
                    $ renpy.sound.play("sfx/card_flip.wav")
                    python:

                        for i in range (0, len(turned_cards_numbers) ):
                            cards_list[turned_cards_numbers[i]]["c_value"] = Null()

                        for j in cards_list:
                            if j["c_chosen"] == False:
                                renpy.jump ("memoriax_game_loop")
                        renpy.jump ("memoriax_game_win")

                jump memoriax_game_loop
        "Fuck minigame":
            $ memo_w += 1
            $ renpy.music.stop(channel='memoriax_m', fadeout=None)
            $ renpy.sound.play("sfx/win_sound.wav")
            $ renpy.block_rollback()
            if memoriax_bet10 == True:
                $ inventory.earn(20)
            if memoriax_bet25 == True:
                $ inventory.earn(50)
            if memoriax_bet50 == True:
                $ inventory.earn(100)
            call screen memoriax_wonmoney_fuckminigames

screen screen_memoriax_losemoney:
    modal True
    key "hide_windows" action NullAction()
    add "images/RPS_minigame/E-lose.png"
    $ renpy.block_rollback()
    if memoriax_bet10 == True:
        text "{size=+25}{color=#00ff00}-10{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet25 == True:
        text "{size=+25}{color=#00ff00}-25{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet50 == True:
        text "{size=+25}{color=#00ff00}-50{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    timer 3.0 action [Jump("memoriax_again_label")]

screen screen_memoriax_wonmoney:
    modal True
    key "hide_windows" action NullAction()
    add "images/RPS_minigame/E-Won.png"
    if memoriax_bet10 == True:
        text "{size=+25}{color=#00ff00}+20{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet25 == True:
        text "{size=+25}{color=#00ff00}+50{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memoriax_bet50 == True:
        text "{size=+25}{color=#00ff00}+100{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    timer 3.0 action [Jump("memoriax_again_label")]

label memoriax_game_lose:

    $ renpy.block_rollback()
    $ memo_l += 1
    call screen screen_memoriax_losemoney

label memoriax_game_win:
    $ renpy.music.stop(channel='memoriax_m', fadeout=None)
    $ renpy.sound.play("sfx/win_sound.wav")
    $ renpy.block_rollback()
    $ memo_w += 1
    if memoriax_bet10 == True:
        $ inventory.earn(20)

    if memoriax_bet25 == True:
        $ inventory.earn(50)

    if memoriax_bet50 == True:
        $ inventory.earn(100)
    call screen screen_memoriax_wonmoney

label memoriax_again_label:
    $ renpy.block_rollback()
    $ memoriax_bet10 = False
    $ memoriax_bet25 = False
    $ memoriax_bet50 = False
    call screen memoriax_again_screen
screen memoriax_again_screen:
    modal True
    key "hide_windows" action NullAction()
    $ renpy.block_rollback()

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle Transform("images/RPS_minigame/PlayAgainNormal.png")
        hover Transform("images/RPS_minigame/PlayAgainHover.png")
        action [Hide("displayTextScreen"), Hide("memoriax_again_screen"),Hide("memoriax_scr"),Hide("screen_memoriax_losemoney"),Hide("screen_memoriax_wonmoney"), Jump("memoriax_label"),]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle Transform("images/RPS_minigame/PlayExitNormal.png")
        hover Transform("images/RPS_minigame/PlayExitHover.png")
        action [Hide("displayTextScreen"), Hide("memoriax_again_screen"),Hide("memoriax_scr"),Hide("screen_memoriax_losemoney"),Hide("screen_memoriax_wonmoney"), Jump("pc_icon_label"),]
        unhovered Hide("displayTextScreen")
