default Li_NS_feet = nsb(__("Play with Liza’s feet while she’s asleep."),image_idle = "images/NS_B/Feet2.png", image_hover = "images/NS_B/Feet2_hover.png", l_jump = "Li_NS_B_feet", number = 6  )
default Li_NS_mouth = nsb(__("Play with Liza’s mouth - make her give you a blowjob while she’s sleeping."),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "Li_NS_B_mouth", number = 1 )
default Li_NS_pussy = nsb(__("Pull down Liza’s panties and eat out her pussy."),image_idle = "images/NS_B/Thighs.png", image_hover = "images/NS_B/Thighs_hover.png", l_jump = "Li_NS_B_pussy", number = 4  )

screen Li_NS_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377

    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.li_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.li_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.li_nsb_s)/9):
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
    if len(nsb_box.li_nsb_s)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Li_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Li_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Li_NS_scr"), Jump("LiR1_NS3_menu")]
        hovered Play ("sound", "sfx/click2.wav")
