image room2_R2_scene = "images/Work_Minigame/Room2R2/Room.jpg"

label work_minigame_R2room2_label:
    menu:
        "Play":
            scene room2_R2_scene
            hide screen map_button
            call screen work_minigame_R2room2_items1
        "{image=cheat_code}":
            jump after_ml_workR2_AS2_label

screen work_minigame_R2room2_items1:
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
            xpos 1720
            ypos 363
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item1.png"
            hover "images/Work_Minigame/room2R2/Items1/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colletedR2_items1_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 46
            ypos 720
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item2.png"
            hover "images/Work_Minigame/room2R2/Items1/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colletedR2_items1_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 824
            ypos 256
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item3.png"
            hover "images/Work_Minigame/room2R2/Items1/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colletedR2_items1_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 1475
            ypos 10
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item4.png"
            hover "images/Work_Minigame/room2R2/Items1/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colletedR2_items1_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 188
            ypos 243
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item5.png"
            hover "images/Work_Minigame/room2R2/Items1/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colletedR2_items1_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 935
            ypos 432
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items1/Item6.png"
            hover "images/Work_Minigame/room2R2/Items1/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colletedR2_items1_room2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2R2_items2_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colletedR2_items1_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label rubbish2_colletedR2_items1_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label rubbish3_colletedR2_items1_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label rubbish4_colletedR2_items1_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label rubbish5_colletedR2_items1_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label rubbish6_colletedR2_items1_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2room2_label

label work_minigame_room2R2_items2_label:
    scene black
    $ renpy.pause(3, hard = True)
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump work_minigame_room2R2_items2_label1

label work_minigame_room2R2_items2_label1:
    scene room2_R2_scene
    call screen work_minigame_room2R2_items2

screen work_minigame_room2R2_items2:
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
            xpos 1261
            ypos 244
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item1.png"
            hover "images/Work_Minigame/room2R2/Items2/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colletedR2_items2_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 10
            ypos 508
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item2.png"
            hover "images/Work_Minigame/room2R2/Items2/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colletedR2_items2_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1870
            ypos 535
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item3.png"
            hover "images/Work_Minigame/room2R2/Items2/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colletedR2_items2_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 139
            ypos 959
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item4.png"
            hover "images/Work_Minigame/room2R2/Items2/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colletedR2_items2_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 1223
            ypos 503
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item5.png"
            hover "images/Work_Minigame/room2R2/Items2/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colletedR2_items2_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 663
            ypos 506
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items2/Item6.png"
            hover "images/Work_Minigame/room2R2/Items2/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colletedR2_items2_room2_label"),]

    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2R2_items3_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colletedR2_items2_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label rubbish2_colletedR2_items2_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label rubbish3_colletedR2_items2_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label rubbish4_colletedR2_items2_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label rubbish5_colletedR2_items2_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label rubbish6_colletedR2_items2_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items2_label1

label work_minigame_room2R2_items3_label:
    scene black
    $ renpy.pause(3, hard = True)
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump work_minigame_room2R2_items3_label1

label work_minigame_room2R2_items3_label1:
    scene room2_R2_scene
    call screen work_minigame_room2R2_items3

screen work_minigame_room2R2_items3:
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
            xpos 525
            ypos 39
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item1.png"
            hover "images/Work_Minigame/room2R2/Items3/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colletedR2_items3_room2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 1198
            ypos 229
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item2.png"
            hover "images/Work_Minigame/room2R2/Items3/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colletedR2_items3_room2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 259
            ypos 753
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item3.png"
            hover "images/Work_Minigame/room2R2/Items3/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colletedR2_items3_room2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 1776
            ypos 249
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item4.png"
            hover "images/Work_Minigame/room2R2/Items3/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colletedR2_items3_room2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 803
            ypos 996
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item5.png"
            hover "images/Work_Minigame/room2R2/Items3/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colletedR2_items3_room2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 808
            ypos 497
            focus_mask True
            idle "images/Work_Minigame/room2R2/Items3/Item6.png"
            hover "images/Work_Minigame/room2R2/Items3/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colletedR2_items3_room2_label"),]

    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/DoneNormal.png"
            hover "images/Work_Minigame/DoneHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room2R2_done_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_colletedR2_items3_room2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label rubbish2_colletedR2_items3_room2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label rubbish3_colletedR2_items3_room2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label rubbish4_colletedR2_items3_room2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label rubbish5_colletedR2_items3_room2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label rubbish6_colletedR2_items3_room2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room2R2_items3_label1

label work_minigame_room2R2_done_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump after_ml_workR2_AS2_label

