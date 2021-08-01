default S_NS_pussy = nsb(__("Let’s finger her pussy a bit."),image_idle = "images/NS_B/Pussy.png", image_hover = "images/NS_B/Pussy_hover.png", l_jump = "SNS_4", number = 4 )
default S_NS_thigh = nsb(__("I’ll start by rubbing my cock between her thighs."),image_idle = "images/NS_B/Thigh2.png", image_hover = "images/NS_B/Thigh2_hover.png", l_jump = "SNS_5", number = 5)
default S_NS_mouth = nsb(__("I’ll put my cock in her mouth while she sleeps."),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "SNS_1", number = 1 )
default S_NS_hand = nsb(__("I’m gonna make her wank me off while she sleeps."),image_idle = "images/NS_B/Hand2.png", image_hover = "images/NS_B/Hand2_hover.png", l_jump = "SNS_3", number = 3)

default S_NS_wake_thigh = nsb(__("Thighjob."),image_idle = "images/NS_B/Ass.png", image_hover = "images/NS_B/Ass_hover.png", l_jump = "SNS_wake_5",  number = 5)

screen S_NS_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377
    add "images/NS_B/Wake.png" xpos 1705 ypos 25


    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.s_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.s_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.s_nsb_s)/9):
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
    if len(nsb_box.s_nsb_s)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("S_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("S_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("S_NS_scr"), Jump("CNS_back")]
        hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 1738
        ypos 110
        focus_mask True
        idle "images/NS_B/WakeUp.png"
        hover "images/NS_B/WakeUp_hover.png"
        if Sara_points >=2:
            action [SetVariable("inv_page", 0),Hide("S_NS_scr"), Jump("SR2_NSwake_label")]
            hovered Play ("sound", "sfx/click2.wav")
        else:
            action NullAction()
            hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=110, tt_xpos=1171, displayText2 = __("Required 2 relation points."),)]
            unhovered Hide("displayTextNS_B")

    if Sara_points <2:
        add "images/NS_B/Locked_slot.png" xpos 1738 ypos 110

    for nsb in nsb_box.s_nsb_wake:

        if nsb.played == True:
            $ new_nsb_in_wake = False

        if nsb.played == False:
            $ new_nsb_in_wake = True

    if new_nsb_in_wake == True:
        add "images/NS_B/New.png" xpos 1732 ypos 98

screen S_NS_wake_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377
    $ my_tt_ypos = 0
    $ my_tt_xpos = 0
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.s_nsb_wake, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.s_nsb_wake)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.s_nsb_wake)/9):
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
                hovered [Play ("sound", "sfx/click2.wav"), Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [nsb.name]),]
                unhovered Hide("displayTextNS_B")
            if nsb.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y -10
            if nsb.locked == True:
                add "images/NS_B/Locked_slot.png" xpos x ypos y
        $ i += 1
    if len(nsb_box.s_nsb_wake)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("S_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("S_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("S_NS_wake_scr"), Jump("S_NS_wake")]
        hovered Play ("sound", "sfx/click2.wav")

