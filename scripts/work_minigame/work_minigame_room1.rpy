image room1_scene = "images/Work_Minigame/room1/Room1.jpg"

default rubbish_colleted_counter = 0
default rubbish1_colleted = False
default rubbish2_colleted = False
default rubbish3_colleted = False
default rubbish4_colleted = False
default rubbish5_colleted = False
default rubbish6_colleted = False

label work_minigame_room1_label:
    menu:
        "Play":
            scene room1_scene
            call screen work_minigame_room1_items1
        "{image=cheat_code}":
            jump ml_work_day_scene1_v1_label_after_minigame

screen work_minigame_room1_items1:
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
            xpos 706
            ypos 554
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item1.png"
            hover "images/Work_Minigame/room1/Items1/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 986
            ypos 343
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item2.png"
            hover "images/Work_Minigame/room1/Items1/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 304
            ypos 420
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item3.png"
            hover "images/Work_Minigame/room1/Items1/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 1131
            ypos 385
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item4.png"
            hover "images/Work_Minigame/room1/Items1/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 1570
            ypos 432
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item5.png"
            hover "images/Work_Minigame/room1/Items1/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 826
            ypos 322
            focus_mask True
            idle "images/Work_Minigame/room1/Items1/Item6.png"
            hover "images/Work_Minigame/room1/Items1/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1_items2_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colleted_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label rubbish2_colleted_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label rubbish3_colleted_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label rubbish4_colleted_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label rubbish5_colleted_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label rubbish6_colleted_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_label

label work_minigame_room1_items2_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    scene black
    $ renpy.pause(3, hard = True)
    jump work_minigame_room1_items2_label1

label work_minigame_room1_items2_label1:
    scene room1_scene
    call screen work_minigame_room1_items2

screen work_minigame_room1_items2:
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
            xpos 1190
            ypos 349
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item1.png"
            hover "images/Work_Minigame/room1/Items2/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_items2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 160
            ypos 421
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item2.png"
            hover "images/Work_Minigame/room1/Items2/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_items2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1143
            ypos 583
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item3.png"
            hover "images/Work_Minigame/room1/Items2/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_items2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 119
            ypos 618
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item4.png"
            hover "images/Work_Minigame/room1/Items2/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_items2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 931
            ypos 353
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item5.png"
            hover "images/Work_Minigame/room1/Items2/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_items2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 1514
            ypos 596
            focus_mask True
            idle "images/Work_Minigame/room1/Items2/Item6.png"
            hover "images/Work_Minigame/room1/Items2/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_items2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1_items3_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colleted_items2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label rubbish2_colleted_items2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label rubbish3_colleted_items2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label rubbish4_colleted_items2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label rubbish5_colleted_items2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label rubbish6_colleted_items2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items2_label1

label work_minigame_room1_items3_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    scene black
    $ renpy.pause(3, hard = True)
    jump work_minigame_room1_items3_label1

label work_minigame_room1_items3_label1:
    scene room1_scene
    call screen work_minigame_room1_items3

screen work_minigame_room1_items3:
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
            xpos 801
            ypos 389
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item1.png"
            hover "images/Work_Minigame/room1/Items3/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colleted_items3_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 459
            ypos 334
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item2.png"
            hover "images/Work_Minigame/room1/Items3/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colleted_items3_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1187
            ypos 395
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item3.png"
            hover "images/Work_Minigame/room1/Items3/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colleted_items3_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 228
            ypos 719
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item4.png"
            hover "images/Work_Minigame/room1/Items3/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colleted_items3_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 1759
            ypos 465
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item5.png"
            hover "images/Work_Minigame/room1/Items3/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colleted_items3_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 1573
            ypos 155
            focus_mask True
            idle "images/Work_Minigame/room1/Items3/Item6.png"
            hover "images/Work_Minigame/room1/Items3/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colleted_items3_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/DoneNormal.png"
            hover "images/Work_Minigame/DoneHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1_done_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"
label rubbish1_colleted_items3_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label rubbish2_colleted_items3_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label rubbish3_colleted_items3_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label rubbish4_colleted_items3_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label rubbish5_colleted_items3_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label rubbish6_colleted_items3_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1_items3_label1

label work_minigame_room1_done_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump ml_work_day_scene1_v1_label_after_minigame

