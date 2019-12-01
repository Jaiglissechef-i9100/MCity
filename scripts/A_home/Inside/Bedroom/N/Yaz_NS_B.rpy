default Yaz_NS_feet = nsb(__("Play with her feet."),image_idle = "images/NS_B/Feet2.png", image_hover = "images/NS_B/Feet2_hover.png", l_jump = "Yaz_NS_B_feet", number = 6  )
default Yaz_NS_ass = nsb(__("Play with Yazmin’s ass."),image_idle = "images/NS_B/Ass.png", image_hover = "images/NS_B/Ass_hover.png", l_jump = "Yaz_NS_B_ass", number = 4 )
default Yaz_NS_mouth = nsb(__("Let’s see if I can get Yazmin to suck my cock!"),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "Yaz_NS_B_mouth", number = 1 )

default Yaz_NS_Turn_bush = nsb(__("Play with her bush."),image_idle = "images/NS_B/Thighs.png", image_hover = "images/NS_B/Thighs_hover.png", l_jump = "Yaz_NS_B_turn_bush", number = 4  )
default Yaz_NS_Turn_tits = nsb(__("Play with her tits."),image_idle = "images/NS_B/Tits.png", image_hover = "images/NS_B/Tits_hover.png", l_jump = "Yaz_NS_B_turn_tits", number = 2  )
screen Yaz_NS_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377

    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.yaz_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.yaz_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.yaz_nsb_s)/9):
        $ prev_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 137
            if i%3==0:
                $ y += 133
                $ x = 55
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                if nsb.locked == False:
                    action [SetVariable("inv_page", 0),Hide("displayTextNS_B"), clickedNsb(nsb), Jump(nsb.l_jump)]
                else:
                    action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),]
                unhovered Hide("displayTextNS_B")
            if nsb.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y - 10
            if nsb.locked == True:
                add "images/NS_B/Locked_slot.png" xpos x ypos y
        $ i += 1
    if len(nsb_box.yaz_nsb_s)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Yaz_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Yaz_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Yaz_NS_scr"), Jump("LiR1_NS3_menu")]
        hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 1752
        ypos 940
        focus_mask True
        idle "images/NS_B/TurnHer.png"
        hover "images/NS_B/TurnHer_hover.png"
        action [SetVariable("inv_page", 0),Hide("displayTextNS_B"),Hide("Yaz_NS_scr"), Jump("Yaz_NS_turn_label")]
        hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=940, tt_xpos=1471, displayText2 = __("Turn her."),)]
        unhovered Hide("displayTextNS_B")

    for nsb in nsb_box.yaz_nsb_turn:
        if nsb.played == False:
            $ new_nsb_in_wake = True
        else:
            $ new_nsb_in_wake = False
    if new_nsb_in_wake == True:
        add "images/NS_B/New.png" xpos 1747 ypos 935

screen Yaz_NS_Turn_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377

    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.yaz_nsb_turn, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.yaz_nsb_turn)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.yaz_nsb_turn)/9):
        $ prev_inv_page = 0

    for nsb in sorted_nsb:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 137
            if i%3==0:
                $ y += 133
                $ x = 55
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb.image_idle
                hover nsb.image_hover
                if nsb.locked == False:
                    action [SetVariable("inv_page", 0),Hide("displayTextNS_B"), clickedNsb(nsb), Jump(nsb.l_jump)]
                else:
                    action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),]
                unhovered Hide("displayTextNS_B")
            if nsb.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y - 10
            if nsb.locked == True:
                add "images/NS_B/Locked_slot.png" xpos x ypos y
        $ i += 1
    if len(nsb_box.yaz_nsb_turn)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Yaz_NS_Turn_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Yaz_NS_Turn_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Yaz_NS_Turn_scr"), Jump("LiR1_NS3_Back1")]
        hovered Play ("sound", "sfx/click2.wav")
