default doc_counter = 0
default wrong_doc_counter = 0
default bob_work_loop = 0
default money_from_bob = 0

default bobwork_w = 0
default bobwork_l = 0

transform tekst_rotate:
    rotate 3
transform timer_anim2:
    rotate 3.4
    zoom 1.15
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    zoom 1.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    repeat
transform timer_anim3:
    rotate 3.0

screen bob_work_scr:

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    add "work2minigame/1.jpg"
    vbox xalign 0.01 yalign 0.99:
        text "W:{color=#00ff00}[bobwork_w]{/color} L:{color=#f00}[bobwork_l]{/color}"

    if memo_timer >0.1:
        timer 0.1 action If (memo_timer > 0.1, SetVariable("memo_timer", memo_timer - 0.1), Jump("bob_game_lose") ) repeat True
    if memo_timer >10:
        text str("{size=+20}{color=#00ff00}[memo_timer]{/color}{/size}") xalign 0.03 yalign 0.5 at timer_anim3
    if memo_timer <10 and memo_timer > 6:
        timer 1.9 action [Play ("memoriax_m", "sfx/lose1.wav")]
        text str("{size=+20}{color=#00ff00}[memo_timer]{/color}{/size}") xalign 0.03 yalign 0.5 at timer_anim3
    if memo_timer <6 and memo_timer > 0.1:
        text str("{size=+20}{color=#f00}[memo_timer]{/color}{/size}") xalign 0.03 yalign 0.5 at timer_anim2
    if memo_timer <0.1:
        timer 0.1 action Jump("bob_game_lose")
        text str("{size=+20}{color=#f00}0{/color}{/size}") xalign 0.03 yalign 0.5 at timer_anim3

    text str("{size=+25}{color=#00ff00}[doc_counter]{/color}/4{color=#00ff00}{/size}") xalign 0.04 yalign 0.25
    text str("{size=+25}{color=#f00}[wrong_doc_counter]{/color}/3{/size}") xalign 0.04 yalign 0.34
    text str("{size=+25}[bob_work_loop]/3{/size}") xalign 0.034 yalign 0.428 at tekst_rotate

    $ x = 300
    $ y = -190
    $ i = 0

    for doc in bob_doc_list:
        if i+1 <= (bob_r+1)*28 and i+1>bob_r*28:
            $ x += 210
            if i%7==0:
                $ y += 240
                $ x = 300



        imagebutton:
            idle Transform((doc["c_value"]), zoom=0.9)
            hover Transform((doc["c_value"]), zoom=1.0)
            xpos x
            ypos y

            action If ( (doc["c_chosen"] or not can_click), None, [SetDict(bob_doc_list[doc["c_number"]], "c_chosen", True), Return(doc["c_number"]) ] )
        $ i += 1
    for doc in boob_roll:
        imagebutton:
            idle Transform(doc, zoom=0.7)
            xpos 30
            ypos 80

init:
    python:
        bob_r = 0
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    image D2 = "work2minigame/D2.png"
    image D3 = "work2minigame/D3.png"
    image D4 = "work2minigame/D4.png"
    image D5 = "work2minigame/D5.png"
    image D6 = "work2minigame/D6.png"
    image D7 = "work2minigame/D7.png"
    image D8 = "work2minigame/D8.png"

label bob_deskwork_label:
    $ can_hide_windows = False
    $ renpy.block_rollback()
    $ renpy.music.stop(channel="memoriax_m", fadeout=1)
    $ A = "work2minigame/D1.png"

    menu:
        "Play":

            $ bob_doc = ["D2","D2","D2","D2","D3","D3","D3","D3","D4","D4","D4","D4","D5","D5","D5","D5","D6","D6","D6","D6","D7","D7","D7","D7","D8","D8","D8","D8"]
            $ boob_roll1 = renpy.random.choice(["D2","D3","D4","D5","D6","D7","D8"])
            $ boob_roll = [boob_roll1]

            $ bob_doc = cards_shuffle(bob_doc)

            $ bob_doc_list = []

            python:
                for i in range (0, len(bob_doc) ):
                    bob_doc_list.append ( {"c_number":i, "c_value": bob_doc[i], "c_chosen":False} )

            $ memo_timer = 20.0
            $ doc_counter = 0
            $ wrong_doc_counter = 0

            show screen bob_work_scr

            label bob_game_loop:
                $ can_click = True
                $ turned_doc_numbers = []
                $ turned_doc_values = []
                if memo_timer <0.1:
                    jump bob_game_lose

                $ turns_left = 1

                label bob_turns_loop:
                    if turns_left > 0:
                        $ result = ui.interact()
                        $ memo_timer = memo_timer
                        $ turned_doc_numbers.append (bob_doc_list[result]["c_number"])
                        $ turned_doc_values.append (bob_doc_list[result]["c_value"])
                        $ turns_left -= 1
                        jump bob_turns_loop

                if turned_doc_values != boob_roll:
                    $ wrong_doc_counter += 1

                    $ renpy.sound.play("sfx/card_flip.wav")
                    python:
                        for i in range (0, len(turned_doc_numbers) ):
                            bob_doc_list[turned_doc_numbers[i]]["c_value"] = Null()

                if turned_doc_values == boob_roll:
                    $ doc_counter += 1
                    $ renpy.sound.play("sfx/card_flip.wav")
                    python:
                        for i in range (0, len(turned_doc_numbers) ):
                            bob_doc_list[turned_doc_numbers[i]]["c_value"] = Null()

                if wrong_doc_counter > 2:
                    jump bob_game_lose
                if doc_counter == 4:
                    jump bob_game_win

                jump bob_game_loop
        "{image=cheat_code}":
            jump bob_deskwork_label_fuckminigames

label bob_game_lose:
    if memo_timer > 0.1:
        $ renpy.sound.play("sfx/failure01.wav")
    $ can_Bob_work_minigame = False
    $ bobwork_l += 1
    jump bob_game_lose1

label bob_game_lose1:
    $ renpy.music.stop(channel="sound")
    call screen bob_work_fail_scr

label bob_game_win:
    $ renpy.block_rollback()
    if bob_work_loop == 3:
        $ bobwork_w += 1
        $ renpy.music.stop(channel="memoriax_m", fadeout=1)
        $ renpy.sound.play("sfx/win_sound.wav")
        $ can_Bob_work_minigame = False
        $ money_from_bob += 1

        call screen bob_work_done_scr
    else:
        $ renpy.music.stop(channel="memoriax_m", fadeout=1)
        $ bob_work_loop += 1
        jump bob_deskwork_label

label bob_deskwork_label_fuckminigames:
    $ renpy.block_rollback()
    $ bobwork_w += 1
    $ renpy.music.stop(channel="memoriax_m", fadeout=1)
    $ renpy.sound.play("sfx/win_sound.wav")
    $ can_Bob_work_minigame = False
    $ money_from_bob += 1
    call screen bob_work_done_scr

screen bob_work_done_scr:

    modal True
    key "hide_windows" action NullAction()
    add "work2minigame/bob_done.png"
    timer 5.0 action [Hide("bob_work_scr"),Hide("bob_work_done_scr"),SetVariable("bob_work_loop", 0),Jump("bob_office_M1")]

screen bob_work_fail_scr:

    modal True
    key "hide_windows" action NullAction()
    add "work2minigame/bob_fail.png"
    timer 5.0 action [Hide("bob_work_scr"),Hide("bob_work_fail_scr"),SetVariable("bob_work_loop", 0),Jump("bob_office_M1")]
