
default ML_NS_sleep_her = nsb("Her Choice.",image_idle = "images/NS_B/Choice.png", image_hover = "images/NS_B/Choice_hover.png", l_jump = "ML_NS_sleep_her_label", number = 1  )
default ML_NS_sleep_her_loc = nsb("Required: 3 relation points.",image_idle = "images/NS_B/Choice.png", image_hover = "images/NS_B/Choice_hover.png", l_jump = "ML_NS_sleep_her_label", number = 1, played = True, locked = True,  )
default ML_NS_sleep_foot_job = nsb("Foot Job.",image_idle = "images/NS_B/Feet2.png", image_hover = "images/NS_B/Feet2_hover.png", l_jump = "ML_NS_sleep_foot_job_label", number = 1  )
default ML_NS_sleep_foot_job_lock = nsb("Foot Job.",image_idle = "images/NS_B/Feet2.png", image_hover = "images/NS_B/Feet2_hover.png", l_jump = "ML_NS_sleep_foot_job_label", number = 1, played = True, locked = True,  )
default ML_NS_sleep_hand = nsb("Hand Job.",image_idle = "images/NS_B/Hand3.png", image_hover = "images/NS_B/Hand3_hover.png", l_jump = "ML_NS_sleep_hand_label", number = 1  )
default ML_NS_sleep_hand_lock = nsb("Hand Job.",image_idle = "images/NS_B/Hand3.png", image_hover = "images/NS_B/Hand3_hover.png", l_jump = "ML_NS_sleep_hand_label", number = 1, played = True, locked = True,  )
screen ML_NS_sleep_scr:

    add "images/NS_B/Wake.png" xpos 1705 ypos 25


    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0



    imagebutton:
        xpos 1738
        ypos 110
        focus_mask True
        idle "images/NS_B/WakeUp.png"
        hover "images/NS_B/WakeUp_hover.png"

        action [SetVariable("inv_page", 0),Hide("ML_NS_sleep_scr"), Jump("ML_NS_wake_label")]
        hovered Play ("sound", "sfx/click2.wav")




    for nsb in nsb_box.ml_nsb_wake:
        if nsb.played == False:
            $ new_nsb_in_wake = True
        else:
            $ new_nsb_in_wake = False
    if new_nsb_in_wake == True:
        add "images/NS_B/New.png" xpos 1732 ypos 98


screen ML_NS_wake_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377
    $ my_tt_ypos = 0
    $ my_tt_xpos = 0
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.ml_nsb_wake, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.ml_nsb_wake)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.ml_nsb_wake)/9):
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
    if len(nsb_box.ml_nsb_wake)>9:


        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("ML_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("ML_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("C_NS_wake_scr"), Jump("ML_NS_sleep_back")]
        hovered Play ("sound", "sfx/click2.wav")