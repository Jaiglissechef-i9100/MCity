image room2_scene = "images/Work_Minigame/Room2/Room2.jpg"

label work_minigame_room2_label:
    menu:
        "Play":
            scene room2_scene
            call screen work_minigame_room2_items1
        "{image=cheat_code}":
            jump ml_work_day_scene2_v1_label_after_work

screen work_minigame_room2_items1:
    key "hide_windows" action NullAction()
    if rubbish_colleted_counter == 0:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R0.png"
    if rubbish_colleted_counter == 1:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R1.png"
    if rubbish_colleted_counter == 2:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R2.png"
    if rubbish_colleted_counter == 3:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R3.png"
    if rubbish_colleted_counter == 4:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R4.png"
    if rubbish_colleted_counter == 5:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R5.png"

    if rubbish1_colleted == False:
        imagebutton:
            xpos 1214
            ypos 211
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item1.png"
            hover "images/Work_Minigame/room2/Items1/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_items1_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 1467
            ypos 255
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item2.png"
            hover "images/Work_Minigame/room2/Items1/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_items1_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 99
            ypos 568
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item3.png"
            hover "images/Work_Minigame/room2/Items1/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_items1_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 423
            ypos 316
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item4.png"
            hover "images/Work_Minigame/room2/Items1/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_items1_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 1406
            ypos 684
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item5.png"
            hover "images/Work_Minigame/room2/Items1/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_items1_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 764
            ypos 239
            focus_mask True
            idle "images/Work_Minigame/room2/Items1/Item6.png"
            hover "images/Work_Minigame/room2/Items1/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_items1_room2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2_items2_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colleted_items1_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label rubbish2_colleted_items1_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label rubbish3_colleted_items1_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label rubbish4_colleted_items1_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label rubbish5_colleted_items1_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label rubbish6_colleted_items1_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_label

label work_minigame_room2_items2_label:
    scene black
    $ renpy.pause(3, hard = True)
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump work_minigame_room2_items2_label1

label work_minigame_room2_items2_label1:
    scene room2_scene
    call screen work_minigame_room2_items2

screen work_minigame_room2_items2:
    key "hide_windows" action NullAction()
    if rubbish_colleted_counter == 0:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R0.png"
    if rubbish_colleted_counter == 1:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R1.png"
    if rubbish_colleted_counter == 2:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R2.png"
    if rubbish_colleted_counter == 3:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R3.png"
    if rubbish_colleted_counter == 4:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R4.png"
    if rubbish_colleted_counter == 5:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R5.png"

    if rubbish1_colleted == False:
        imagebutton:
            xpos 434
            ypos 515
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item1.png"
            hover "images/Work_Minigame/room2/Items2/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_items2_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 1592
            ypos 301
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item2.png"
            hover "images/Work_Minigame/room2/Items2/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_items2_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1030
            ypos 239
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item3.png"
            hover "images/Work_Minigame/room2/Items2/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_items2_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 1427
            ypos 721
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item4.png"
            hover "images/Work_Minigame/room2/Items2/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_items2_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 628
            ypos 388
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item5.png"
            hover "images/Work_Minigame/room2/Items2/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_items2_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 1671
            ypos 408
            focus_mask True
            idle "images/Work_Minigame/room2/Items2/Item6.png"
            hover "images/Work_Minigame/room2/Items2/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_items2_room2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2_items3_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colleted_items2_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label rubbish2_colleted_items2_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label rubbish3_colleted_items2_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label rubbish4_colleted_items2_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label rubbish5_colleted_items2_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label rubbish6_colleted_items2_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items2_label1

label work_minigame_room2_items3_label:
    scene black
    $ renpy.pause(3, hard = True)
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump work_minigame_room2_items3_label1

label work_minigame_room2_items3_label1:
    scene room2_scene
    call screen work_minigame_room2_items3

screen work_minigame_room2_items3:
    key "hide_windows" action NullAction()
    if rubbish_colleted_counter == 0:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R0.png"
    if rubbish_colleted_counter == 1:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R1.png"
    if rubbish_colleted_counter == 2:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R2.png"
    if rubbish_colleted_counter == 3:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R3.png"
    if rubbish_colleted_counter == 4:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R4.png"
    if rubbish_colleted_counter == 5:
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R5.png"

    if rubbish1_colleted == False:
        imagebutton:
            xpos 775
            ypos 252
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item1.png"
            hover "images/Work_Minigame/room2/Items3/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_items3_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 397
            ypos 393
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item2.png"
            hover "images/Work_Minigame/room2/Items3/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_items3_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1287
            ypos 272
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item3.png"
            hover "images/Work_Minigame/room2/Items3/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_items3_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 542
            ypos 802
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item4.png"
            hover "images/Work_Minigame/room2/Items3/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_items3_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 92
            ypos 536
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item5.png"
            hover "images/Work_Minigame/room2/Items3/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_items3_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 579
            ypos 403
            focus_mask True
            idle "images/Work_Minigame/room2/Items3/Item6.png"
            hover "images/Work_Minigame/room2/Items3/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_items3_room2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/DoneNormal.png"
            hover "images/Work_Minigame/DoneHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2_done_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"
label rubbish1_colleted_items3_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label rubbish2_colleted_items3_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label rubbish3_colleted_items3_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label rubbish4_colleted_items3_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label rubbish5_colleted_items3_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label rubbish6_colleted_items3_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2_items3_label1

label work_minigame_room2_done_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump ml_work_day_scene2_v1_label_after_work

