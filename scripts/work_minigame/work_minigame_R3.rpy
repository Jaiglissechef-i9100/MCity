init python:
    class Rubbish(store.object):
        
        def __init__(self, image="", hover_i="", r_xpos = 0, r_ypos = 0 ):
            self.image = image
            self.hover_i=hover_i
            self.r_xpos = r_xpos
            self.r_ypos = r_ypos
    class droprubb(Action):
        
        def __init__(self, rubbish):
            self.rubbish = rubbish
        
        def __call__(self):
            rubbish_box.box.remove(self.rubbish)
            renpy.restart_interaction()

    class Rubbish_box(store.object):
        def __init__(self):
            
            self.box = []
        
        def add(self, rubbish):
            self.box.append(rubbish)

default rubbish_box = Rubbish_box()

default Rubb_r1_1 = Rubbish(image="images/Work_Minigame/room1/Items1/Item1.png", hover_i="images/Work_Minigame/room1/Items1/Item1_hover.png", r_xpos = 706, r_ypos = 554)
default Rubb_r1_2 = Rubbish(image="images/Work_Minigame/room1/Items1/Item2.png", hover_i="images/Work_Minigame/room1/Items1/Item2_hover.png", r_xpos = 1036, r_ypos = 343)
default Rubb_r1_3 = Rubbish(image="images/Work_Minigame/room1/Items1/Item3.png", hover_i="images/Work_Minigame/room1/Items1/Item3_hover.png", r_xpos = 304, r_ypos = 420)
default Rubb_r1_4 = Rubbish(image="images/Work_Minigame/room1/Items1/Item4.png", hover_i="images/Work_Minigame/room1/Items1/Item4_hover.png", r_xpos = 1131, r_ypos = 385)
default Rubb_r1_5 = Rubbish(image="images/Work_Minigame/room1/Items1/Item5.png", hover_i="images/Work_Minigame/room1/Items1/Item5_hover.png", r_xpos = 1570, r_ypos = 432)
default Rubb_r1_6 = Rubbish(image="images/Work_Minigame/room1/Items1/Item6.png", hover_i="images/Work_Minigame/room1/Items1/Item6_hover.png", r_xpos = 656, r_ypos = 322)

default Rubb_r1_7 = Rubbish(image="images/Work_Minigame/room1/Items2/Item1.png", hover_i="images/Work_Minigame/room1/Items2/Item1_hover.png", r_xpos = 1165, r_ypos = 349)
default Rubb_r1_8 = Rubbish(image="images/Work_Minigame/room1/Items2/Item2.png", hover_i="images/Work_Minigame/room1/Items2/Item2_hover.png", r_xpos = 160, r_ypos = 421)
default Rubb_r1_9 = Rubbish(image="images/Work_Minigame/room1/Items2/Item3.png", hover_i="images/Work_Minigame/room1/Items2/Item3_hover.png", r_xpos = 1143, r_ypos = 583)
default Rubb_r1_10 = Rubbish(image="images/Work_Minigame/room1/Items2/Item4.png", hover_i="images/Work_Minigame/room1/Items2/Item4_hover.png", r_xpos = 119, r_ypos = 618)
default Rubb_r1_11 = Rubbish(image="images/Work_Minigame/room1/Items2/Item5.png", hover_i="images/Work_Minigame/room1/Items2/Item5_hover.png", r_xpos = 931, r_ypos = 353)
default Rubb_r1_12 = Rubbish(image="images/Work_Minigame/room1/Items2/Item6.png", hover_i="images/Work_Minigame/room1/Items2/Item6_hover.png", r_xpos = 1514, r_ypos = 596)

default Rubb_r1_13 = Rubbish(image="images/Work_Minigame/room1/Items3/Item1.png", hover_i="images/Work_Minigame/room1/Items3/Item1_hover.png", r_xpos = 801, r_ypos = 389)
default Rubb_r1_14 = Rubbish(image="images/Work_Minigame/room1/Items3/Item2.png", hover_i="images/Work_Minigame/room1/Items3/Item2_hover.png", r_xpos = 459, r_ypos = 334)
default Rubb_r1_15 = Rubbish(image="images/Work_Minigame/room1/Items3/Item3.png", hover_i="images/Work_Minigame/room1/Items3/Item3_hover.png", r_xpos = 1187, r_ypos = 395)
default Rubb_r1_16 = Rubbish(image="images/Work_Minigame/room1/Items3/Item4.png", hover_i="images/Work_Minigame/room1/Items3/Item4_hover.png", r_xpos = 228, r_ypos = 719)
default Rubb_r1_17 = Rubbish(image="images/Work_Minigame/room1/Items3/Item5.png", hover_i="images/Work_Minigame/room1/Items3/Item5_hover.png", r_xpos = 1759, r_ypos = 465)
default Rubb_r1_18 = Rubbish(image="images/Work_Minigame/room1/Items3/Item6.png", hover_i="images/Work_Minigame/room1/Items3/Item6_hover.png", r_xpos = 1573, r_ypos = 155)


default Rubb_r2_1 = Rubbish(image="images/Work_Minigame/room2/Items1/Item1.png", hover_i="images/Work_Minigame/room2/Items1/Item1_hover.png", r_xpos = 1214, r_ypos = 211)
default Rubb_r2_2 = Rubbish(image="images/Work_Minigame/room2/Items1/Item2.png", hover_i="images/Work_Minigame/room2/Items1/Item2_hover.png", r_xpos = 1467, r_ypos = 255)
default Rubb_r2_3 = Rubbish(image="images/Work_Minigame/room2/Items1/Item3.png", hover_i="images/Work_Minigame/room2/Items1/Item3_hover.png", r_xpos = 99, r_ypos = 568)
default Rubb_r2_4 = Rubbish(image="images/Work_Minigame/room2/Items1/Item4.png", hover_i="images/Work_Minigame/room2/Items1/Item4_hover.png", r_xpos = 423, r_ypos = 316)
default Rubb_r2_5 = Rubbish(image="images/Work_Minigame/room2/Items1/Item5.png", hover_i="images/Work_Minigame/room2/Items1/Item5_hover.png", r_xpos = 1406, r_ypos = 684)
default Rubb_r2_6 = Rubbish(image="images/Work_Minigame/room2/Items1/Item6.png", hover_i="images/Work_Minigame/room2/Items1/Item6_hover.png", r_xpos = 764, r_ypos = 239)

default Rubb_r2_7 = Rubbish(image="images/Work_Minigame/room2/Items2/Item1.png", hover_i="images/Work_Minigame/room2/Items2/Item1_hover.png", r_xpos = 494, r_ypos = 515)
default Rubb_r2_8 = Rubbish(image="images/Work_Minigame/room2/Items2/Item2.png", hover_i="images/Work_Minigame/room2/Items2/Item2_hover.png", r_xpos = 1592, r_ypos = 301)
default Rubb_r2_9 = Rubbish(image="images/Work_Minigame/room2/Items2/Item3.png", hover_i="images/Work_Minigame/room2/Items2/Item3_hover.png", r_xpos = 1030, r_ypos = 239)
default Rubb_r2_10 = Rubbish(image="images/Work_Minigame/room2/Items2/Item4.png", hover_i="images/Work_Minigame/room2/Items2/Item4_hover.png", r_xpos = 1327, r_ypos = 801)
default Rubb_r2_11 = Rubbish(image="images/Work_Minigame/room2/Items2/Item5.png", hover_i="images/Work_Minigame/room2/Items2/Item5_hover.png", r_xpos = 628, r_ypos = 388)
default Rubb_r2_12 = Rubbish(image="images/Work_Minigame/room2/Items2/Item6.png", hover_i="images/Work_Minigame/room2/Items2/Item6_hover.png", r_xpos = 1671, r_ypos = 408)

default Rubb_r2_13 = Rubbish(image="images/Work_Minigame/room2/Items3/Item1.png", hover_i="images/Work_Minigame/room2/Items3/Item1_hover.png", r_xpos = 795, r_ypos = 249)
default Rubb_r2_14 = Rubbish(image="images/Work_Minigame/room2/Items3/Item2.png", hover_i="images/Work_Minigame/room2/Items3/Item2_hover.png", r_xpos = 397, r_ypos = 393)
default Rubb_r2_15 = Rubbish(image="images/Work_Minigame/room2/Items3/Item3.png", hover_i="images/Work_Minigame/room2/Items3/Item3_hover.png", r_xpos = 1287, r_ypos = 272)
default Rubb_r2_16 = Rubbish(image="images/Work_Minigame/room2/Items3/Item4.png", hover_i="images/Work_Minigame/room2/Items3/Item4_hover.png", r_xpos = 542, r_ypos = 802)
default Rubb_r2_17 = Rubbish(image="images/Work_Minigame/room2/Items3/Item5.png", hover_i="images/Work_Minigame/room2/Items3/Item5_hover.png", r_xpos = 90, r_ypos = 495)
default Rubb_r2_18 = Rubbish(image="images/Work_Minigame/room2/Items3/Item6.png", hover_i="images/Work_Minigame/room2/Items3/Item6_hover.png", r_xpos = 579, r_ypos = 403)

default Rubb_r3_1 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item1.png", hover_i="images/Work_Minigame/room1R2/Items1/Item1_hover.png", r_xpos = 808, r_ypos = 301)
default Rubb_r3_2 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item2.png", hover_i="images/Work_Minigame/room1R2/Items1/Item2_hover.png", r_xpos = 1203, r_ypos = 101)
default Rubb_r3_3 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item3.png", hover_i="images/Work_Minigame/room1R2/Items1/Item3_hover.png", r_xpos = 221, r_ypos = 283)
default Rubb_r3_4 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item4.png", hover_i="images/Work_Minigame/room1R2/Items1/Item4_hover.png", r_xpos = 766, r_ypos = 597)
default Rubb_r3_5 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item5.png", hover_i="images/Work_Minigame/room1R2/Items1/Item5_hover.png", r_xpos = 1736, r_ypos = 763)
default Rubb_r3_6 = Rubbish(image="images/Work_Minigame/room1R2/Items1/Item6.png", hover_i="images/Work_Minigame/room1R2/Items1/Item6_hover.png", r_xpos = 877, r_ypos = 20)

default Rubb_r3_7 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item1.png", hover_i="images/Work_Minigame/room1R2/Items2/Item1_hover.png", r_xpos = 1143, r_ypos = 669)
default Rubb_r3_8 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item2.png", hover_i="images/Work_Minigame/room1R2/Items2/Item2_hover.png", r_xpos = 90, r_ypos = 157)
default Rubb_r3_9 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item3.png", hover_i="images/Work_Minigame/room1R2/Items2/Item3_hover.png", r_xpos = 1225, r_ypos = 225)
default Rubb_r3_10 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item4.png", hover_i="images/Work_Minigame/room1R2/Items2/Item4_hover.png", r_xpos = 120, r_ypos = 868)
default Rubb_r3_11 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item5.png", hover_i="images/Work_Minigame/room1R2/Items2/Item5_hover.png", r_xpos = 970, r_ypos = 336)
default Rubb_r3_12 = Rubbish(image="images/Work_Minigame/room1R2/Items2/Item6.png", hover_i="images/Work_Minigame/room1R2/Items2/Item6_hover.png", r_xpos = 409, r_ypos = 175)

default Rubb_r3_13 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item1.png", hover_i="images/Work_Minigame/room1R2/Items3/Item1_hover.png", r_xpos = 1673, r_ypos = 380)
default Rubb_r3_14 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item2.png", hover_i="images/Work_Minigame/room1R2/Items3/Item2_hover.png", r_xpos = 324, r_ypos = 55)
default Rubb_r3_15 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item3.png", hover_i="images/Work_Minigame/room1R2/Items3/Item3_hover.png", r_xpos = 854, r_ypos = 337)
default Rubb_r3_16 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item4.png", hover_i="images/Work_Minigame/room1R2/Items3/Item4_hover.png", r_xpos = 737, r_ypos = 696)
default Rubb_r3_17 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item5.png", hover_i="images/Work_Minigame/room1R2/Items3/Item5_hover.png", r_xpos = 0, r_ypos = 720)
default Rubb_r3_18 = Rubbish(image="images/Work_Minigame/room1R2/Items3/Item6.png", hover_i="images/Work_Minigame/room1R2/Items3/Item6_hover.png", r_xpos = 1180, r_ypos = 704)
default roll_count = 6

init -1 python:

    rubbish = None

label ML_workR3:
    $ roll_count = 6
    $ rubb_room_finished = 1
    $ rubbish_box_r1 = [Rubb_r1_1,Rubb_r1_2,Rubb_r1_3,Rubb_r1_4,Rubb_r1_5,Rubb_r1_6,Rubb_r1_7,Rubb_r1_8,Rubb_r1_9,Rubb_r1_10,Rubb_r1_11,Rubb_r1_12,Rubb_r1_13,Rubb_r1_14,Rubb_r1_15,Rubb_r1_16,Rubb_r1_17,Rubb_r1_18]

    $ rubbish_box_r2 = [Rubb_r2_1,Rubb_r2_2,Rubb_r2_3,Rubb_r2_4,Rubb_r2_5,Rubb_r2_6,Rubb_r2_7,Rubb_r2_8,Rubb_r2_9,Rubb_r2_10,Rubb_r2_11,Rubb_r2_12,Rubb_r2_13,Rubb_r2_14,Rubb_r2_15,Rubb_r2_16,Rubb_r2_17,Rubb_r2_18]

    $ rubbish_box_r3 = [Rubb_r3_1,Rubb_r3_2,Rubb_r3_3,Rubb_r3_4,Rubb_r3_5,Rubb_r3_6,Rubb_r3_7,Rubb_r3_8,Rubb_r3_9,Rubb_r3_10,Rubb_r3_11,Rubb_r3_12,Rubb_r3_13,Rubb_r3_14,Rubb_r3_15,Rubb_r3_16,Rubb_r3_17,Rubb_r3_18]

    $ rubb_room = [1,2,3]
    $ rubb_room_roll = renpy.random.choice(rubb_room)
    show screen ML_workR3_scr
    jump ML_workR3_roll



label ML_workR3_roll:
    $ rubbish_colleted_counter = 0
    if roll_count > 0:
        if rubb_room_roll == 1:
            scene room1_scene
            $ rubb_roll1 = renpy.random.choice(rubbish_box_r1)
            $ rubbish_box.box.append(rubb_roll1)
            $ rubbish_box_r1.remove(rubb_roll1)

        if rubb_room_roll == 2:
            scene room2_scene
            $ rubb_roll1 = renpy.random.choice(rubbish_box_r2)
            $ rubbish_box.box.append(rubb_roll1)
            $ rubbish_box_r2.remove(rubb_roll1)

        if rubb_room_roll == 3:
            scene room1_R2_scene
            $ rubb_roll1 = renpy.random.choice(rubbish_box_r3)
            $ rubbish_box.box.append(rubb_roll1)
            $ rubbish_box_r3.remove(rubb_roll1)

        $ roll_count -= 1
        jump ML_workR3_roll
    if roll_count == 0:
        $ rubb_room = [1,2,3]
        $ rubb_room_roll = renpy.random.choice(rubb_room)
        $ roll_count = 6
        call screen ML_workR3_scr




screen ML_workR3_scr:
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

    if rubbish_colleted_counter == 6 and rubb_room_finished <3:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/NextNormal.png"
            hover "images/Work_Minigame/NextHover.png"
            action [Hide("displayTextScreen"),SetVariable("rubb_room_finished",rubb_room_finished +1),Jump("ML_workR3_roll"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"
    if rubbish_colleted_counter == 6 and rubb_room_finished == 3:
        imagebutton:
            xpos 1687
            ypos 833
            focus_mask True
            idle "images/Work_Minigame/DoneNormal.png"
            hover "images/Work_Minigame/DoneHover.png"
            action [Hide("displayTextScreen"),SetVariable("rubb_room_finished",rubb_room_finished +1),Jump("ML_workR3_finished"),]
        imagebutton:
            xpos 1690
            ypos 915
            focus_mask True
            idle "images/Work_Minigame/R6.png"

    for rubbish in rubbish_box.box:

        $ r_pic = rubbish.image

        $ r_pic_h = rubbish.hover_i
        $ rubb_x = rubbish.r_xpos
        $ rubb_y = rubbish.r_ypos
        imagebutton focus_mask True idle r_pic hover r_pic_h xpos rubb_x ypos rubb_y action [SetVariable("rubbish_colleted_counter",rubbish_colleted_counter +1), droprubb(rubbish)]


label ML_workR3_finished:
    if ml_points == 3:
        $ MLR3_AS2_event = 2
        jump MLR3_AS2