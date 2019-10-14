image room1_R2_scene = "images/Work_Minigame/room1R2/Room.jpg"




label work_minigame_R2_room1_label:
    scene room1_R2_scene
    hide screen map_button
    call screen work_minigame_R2_room1_items1


screen work_minigame_R2_room1_items1:
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
            xpos 808
            ypos 301
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item1.png"
            hover "images/Work_Minigame/room1R2/Items1/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_R2colleted_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 1203
            ypos 101
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item2.png"
            hover "images/Work_Minigame/room1R2/Items1/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_R2colleted_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 221
            ypos 283
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item3.png"
            hover "images/Work_Minigame/room1R2/Items1/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_R2colleted_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 766
            ypos 597
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item4.png"
            hover "images/Work_Minigame/room1R2/Items1/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_R2colleted_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 1736
            ypos 763
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item5.png"
            hover "images/Work_Minigame/room1R2/Items1/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_R2colleted_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 877
            ypos 20
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items1/Item6.png"
            hover "images/Work_Minigame/room1R2/Items1/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_R2colleted_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1R2_items2_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_R2colleted_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label

label rubbish2_R2colleted_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label

label rubbish3_R2colleted_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label

label rubbish4_R2colleted_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label

label rubbish5_R2colleted_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label

label rubbish6_R2colleted_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_R2_room1_label


label work_minigame_room1R2_items2_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    scene black
    $ renpy.pause(3, hard = True)
    jump work_minigame_room1R2_items2_label1

label work_minigame_room1R2_items2_label1:
    scene room1_R2_scene
    call screen work_minigame_room1R2_items2

screen work_minigame_room1R2_items2:
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
            xpos 1143
            ypos 669
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item1.png"
            hover "images/Work_Minigame/room1R2/Items2/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_R2colleted_items2_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 90
            ypos 157
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item2.png"
            hover "images/Work_Minigame/room1R2/Items2/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_R2colleted_items2_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 1225
            ypos 225
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item3.png"
            hover "images/Work_Minigame/room1R2/Items2/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_R2colleted_items2_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 40
            ypos 868
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item4.png"
            hover "images/Work_Minigame/room1R2/Items2/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_R2colleted_items2_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 970
            ypos 336
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item5.png"
            hover "images/Work_Minigame/room1R2/Items2/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_R2colleted_items2_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 409
            ypos 175
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items2/Item6.png"
            hover "images/Work_Minigame/room1R2/Items2/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_R2colleted_items2_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1R2_items3_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

label rubbish1_R2colleted_items2_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1

label rubbish2_R2colleted_items2_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1

label rubbish3_R2colleted_items2_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1

label rubbish4_R2colleted_items2_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1

label rubbish5_R2colleted_items2_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1

label rubbish6_R2colleted_items2_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items2_label1


label work_minigame_room1R2_items3_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    scene black
    $ renpy.pause(3, hard = True)
    jump work_minigame_room1R2_items3_label1

label work_minigame_room1R2_items3_label1:
    scene room1_R2_scene
    call screen work_minigame_room1R2_items3

screen work_minigame_room1R2_items3:
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
            xpos 1673
            ypos 380
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item1.png"
            hover "images/Work_Minigame/room1R2/Items3/Item1_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish1_colletedR2_items3_label"),]
    if rubbish2_colleted == False:
        imagebutton:
            xpos 324
            ypos 55
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item2.png"
            hover "images/Work_Minigame/room1R2/Items3/Item2_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish2_colletedR2_items3_label"),]
    if rubbish3_colleted == False:
        imagebutton:
            xpos 854
            ypos 337
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item3.png"
            hover "images/Work_Minigame/room1R2/Items3/Item3_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish3_colletedR2_items3_label"),]
    if rubbish4_colleted == False:
        imagebutton:
            xpos 737
            ypos 696
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item4.png"
            hover "images/Work_Minigame/room1R2/Items3/Item4_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish4_colletedR2_items3_label"),]
    if rubbish5_colleted == False:
        imagebutton:
            xpos 0
            ypos 720
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item5.png"
            hover "images/Work_Minigame/room1R2/Items3/Item5_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish5_colletedR2_items3_label"),]
    if rubbish6_colleted == False:
        imagebutton:
            xpos 1180
            ypos 704
            focus_mask True
            idle "images/Work_Minigame/room1R2/Items3/Item6.png"
            hover "images/Work_Minigame/room1R2/Items3/Item6_hover.png"
            action [Hide("displayTextScreen"), Jump("rubbish6_colletedR2_items3_label"),]
    if rubbish_colleted_counter == 6:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/DoneNormal.png"
            hover "images/Work_Minigame/DoneHover.png"
            action [Hide("displayTextScreen"), Jump("work_minigame_room1R2_done_label"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"
label rubbish1_colletedR2_items3_label:
    $ rubbish1_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1

label rubbish2_colletedR2_items3_label:
    $ rubbish2_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1

label rubbish3_colletedR2_items3_label:
    $ rubbish3_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1

label rubbish4_colletedR2_items3_label:
    $ rubbish4_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1

label rubbish5_colletedR2_items3_label:
    $ rubbish5_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1

label rubbish6_colletedR2_items3_label:
    $ rubbish6_colleted = True
    $ rubbish_colleted_counter += 1
    jump work_minigame_room1R2_items3_label1


label work_minigame_room1R2_done_label:
    $ rubbish_colleted_counter = 0
    $ rubbish1_colleted = False
    $ rubbish2_colleted = False
    $ rubbish3_colleted = False
    $ rubbish4_colleted = False
    $ rubbish5_colleted = False
    $ rubbish6_colleted = False
    jump after_ml_workR2_AS1_label