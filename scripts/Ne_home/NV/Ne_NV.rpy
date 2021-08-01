image Ne_NV_p1 = "images/Ne_1/NV/1.jpg"
image Ne_NV_p2 = "images/Ne_1/NV/2.jpg"
image Ne_NV_p3 = "images/Ne_1/NV/3.jpg"
image Ne_NV_p4 = "images/Ne_1/NV/4.jpg"

image Ne_NV_Isla_p1 = "images/Ne_1/NV/Isla/1.jpg"
image Ne_NV_Isla_p2 = "images/Ne_1/NV/Isla/2.jpg"

image Ne_NV_Sidra_p1 = "images/Ne_1/NV/Sidra/1.jpg"



default Sidra_visited = 0
default Isla_visited = 0


default Sidra_NS_tits = nsb1(__("Tits"),image_idle = "images/NS_B/Titsjob.png", image_hover = "images/NS_B/Titsjob_hover.png", l_jump = "Sidra_NV_tits_lab", number = "2")

default Isla_NS_tits = nsb1(__("Tits"),image_idle = "images/NS_B/Titsjob.png", image_hover = "images/NS_B/Titsjob_hover.png", l_jump = "Isla_NV_tits_lab", number = "2")
default Isla_NS_kissing = nsb1(__("Kissing"),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "Isla_NV_kiss_lab", number = "1a ")
default Isla_NS_pussy = nsb1(__("Pussy"),image_idle = "images/NS_B/Pussy.png", image_hover = "images/NS_B/Pussy_hover.png", l_jump = "Isla_NV_pussy_lab", number = "4" )

label Ne_NV_lab:
    if Ne_NV == False:
        show screen Ne_Bedroom_N_scr
        $ clickable = False
        MC "(I've already done something tonight. I’ll let them sleep.)"
        $ clickable = True
        hide screen Ne_Bedroom_N_scr
        jump Ne_Bedroom_M1

    if Ne_NV == True:

        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button


        $ Ne_NV = False
        $ inv_page = 0


        scene Ne_NV_p1 with dissolve
        Sidra "Zzz…"
        Isla "*Snore*"
        MC "(Okay, that's it I'm in. Time to get these bedsheets out of the way!)"
        scene Ne_NV_p2
        MC "(I wonder if they’re sleeping naked under this thing.)"
        MC "(It would certainly make my life a LOT easier if they are!)"
        scene Ne_NV_p3
        Sidra "Zzz…"
        MC "(And… voila!)"
        scene Ne_NV_p4
        MC "(Aww bugger. They’re both dressed.)"
        MC "(I guess I’m gonna have to take their clothes off first.) "
        MC "(Now, which girl should I start with…)"
        if not Isla_NS_tits in nsb_box1.ce2_nsb_s:
            $ nsb_box1.add_ce2(Isla_NS_tits)
            $ nsb_box1.add_ce2(Isla_NS_kissing)
            $ nsb_box1.add_ce2(Isla_NS_pussy)
        if not Sidra_NS_tits in nsb_box1.ce1_nsb_s:
            $ nsb_box1.add_ce1(Sidra_NS_tits)

        menu:
            "Play with Sidra tonight.":
                $ Sidra_visited +=1
                scene Ne_NV_Sidra_p1
                MC "(I guess it’s your turn tonight, Sidra.)"
                Sidra "*Snore*"


                $ renpy.block_rollback()
                $ can_hide_windows = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)
                call screen Ne_NV_Sidra_scr
            "Play with Isla tonight.":
                $ Isla_visited +=1
                scene Ne_NV_Isla_p1
                MC "(Sidra has already played with Isla’s body a lot. I think I deserve a turn too!)"
                MC "(Let’s see just how sensitive she really is!)"

                $ renpy.block_rollback()
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                call screen Ne_NV_Isla_scr

label Ne_NV_back:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene Ne_NV_Isla_p2 with dissolve
    MC "*Pant* *Pant*"
    MC "(Shit! I’ve gotta get out of here before she sees me!)"


    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump Ne_Bedroom_M1

label Ne_NV_back1:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black with dissolve


    $ renpy.pause(2, hard = True)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump Ne_Bedroom_M1

screen Ne_NV_Isla_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377



    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box1.ce2_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box1.ce2_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box1.ce2_nsb_s)/9):
        $ prev_inv_page = 0

    for nsb1 in sorted_nsb:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 137
            if i%3==0:
                $ y += 133
                $ x = 55
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb1.image_idle
                hover nsb1.image_hover
                if nsb1.locked == False:
                    action [SetVariable("inv_page", 0),Hide("displayTextNS_B"), clickedNsb1(nsb1), Jump(nsb1.l_jump)]
                else:
                    action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [nsb1.name]),]
                unhovered Hide("displayTextNS_B")
            if nsb1.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y - 10
            if nsb1.locked == True:
                add "images/NS_B/Locked_slot.png" xpos x ypos y
        $ i += 1
    if len(nsb_box1.ce2_nsb_s)>9:


        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Ne_NV_Isla_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Ne_NV_Isla_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Ne_NV_Isla_scr"), Jump("Ne_NV_back1")]
        hovered Play ("sound", "sfx/click2.wav")






    for nsb1 in nsb_box1.ce2_nsb_s:

        if nsb1.played == True:
            $ new_nsb_in_wake = False
        if nsb1.played == False:
            $ new_nsb_in_wake = True

screen Ne_NV_Sidra_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377



    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box1.ce1_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box1.ce1_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box1.ce1_nsb_s)/9):
        $ prev_inv_page = 0

    for nsb1 in sorted_nsb:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 137
            if i%3==0:
                $ y += 133
                $ x = 55
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle nsb1.image_idle
                hover nsb1.image_hover
                if nsb1.locked == False:
                    action [SetVariable("inv_page", 0),Hide("displayTextNS_B"), clickedNsb1(nsb1), Jump(nsb1.l_jump)]
                else:
                    action NullAction()
                hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [nsb1.name]),]
                unhovered Hide("displayTextNS_B")
            if nsb1.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y - 10
            if nsb1.locked == True:
                add "images/NS_B/Locked_slot.png" xpos x ypos y
        $ i += 1
    if len(nsb_box1.ce1_nsb_s)>9:


        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Ne_NV_Sidra_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Ne_NV_Sidra_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Ne_NV_scr"), Jump("Ne_NV_back1")]
        hovered Play ("sound", "sfx/click2.wav")






    for nsb1 in nsb_box1.ce1_nsb_s:

        if nsb1.played == True:
            $ new_nsb_in_wake = False
        if nsb1.played == False:
            $ new_nsb_in_wake = True

