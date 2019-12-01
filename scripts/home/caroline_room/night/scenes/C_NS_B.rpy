init python:

    class nsb(store.object):
        def __init__(self, name, number, image_idle= "", image_hover= "", l_jump= "", played = False, locked = False, t_played = 0000 ):
            self.name = name
            self.number = number
            self.image_idle = image_idle 
            self.image_hover = image_hover
            self.l_jump = l_jump
            self.played = played
            self.locked = locked
            self.t_played = t_played

    class Nsb_box(store.object):
        def __init__(self):
            
            self.c_nsb_s = []
            self.c_nsb_wake = []
            
            self.s_nsb_s = []
            self.s_nsb_wake = []
            
            self.ml_nsb_s = []
            self.ml_nsb_wake = []
            self.ml_nsb_sleep = []
            
            self.yaz_nsb_s = []
            self.yaz_nsb_turn = []
            
            self.li_nsb_s = []
        
        
        
        def add_c(self, nsb):
            self.c_nsb_s.append(nsb)
        def drop_c(self, nsb):
            self.c_nsb_s.remove(nsb)
        def add_c_wake (self,nsb):
            self.c_nsb_wake.append(nsb)
        def drop_c_wake (self,nsb):
            self.c_nsb_wake.remove(nsb)
        
        def add_s(self, nsb):
            self.s_nsb_s.append(nsb)
        def drop_s(self, nsb):
            self.s_nsb_s.remove(nsb)
        def add_s_wake (self,nsb):
            self.s_nsb_wake.append(nsb)
        def drop_s_wake (self,nsb):
            self.s_nsb_wake.remove(nsb)
        
        def add_ml(self, nsb):
            self.ml_nsb_s.append(nsb)
        def drop_ml(self, nsb):
            self.ml_nsb_s.remove(nsb)
        def add_ml_wake(self, nsb):
            self.ml_nsb_wake.append(nsb)
        def drop_ml_wake(self, nsb):
            self.ml_nsb_wake.remove(nsb)
        def add_ml_sleep(self, nsb):
            self.ml_nsb_sleep.append(nsb)
        def drop_ml_sleep(self, nsb):
            self.ml_nsb_sleep.remove(nsb)
        
        def add_yaz(self, nsb):
            self.yaz_nsb_s.append(nsb)
        def drop_yaz(self, nsb):
            self.yaz_nsb_s.remove(nsb)
        def add_yaz_turn (self,nsb):
            self.yaz_nsb_turn.append(nsb)
        def drop_yaz_turn (self,nsb):
            self.yaz_nsb_turn.remove(nsb)
        
        def add_li(self, nsb):
            self.li_nsb_s.append(nsb)
        def drop_li(self, nsb):
            self.li_nsb_s.remove(nsb)



    class clickedNsb(Action):
        
        def __init__(self, object):
            self.object = object
        
        def __call__(self):
            new_value2 = True
            new_value3 = self.object.t_played + 1
            if self.object.t_played <9999:
                
                setattr(self.object, "t_played", new_value3)
            setattr(self.object, "played", new_value2)

default nsb_box = Nsb_box()
default C_NS_cock = nsb(__("Slide your cock into her mouth."),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "CNS_1", number = 1  )
default C_NS_tits = nsb(__("Pull down her bra and play with her tits."),image_idle = "images/NS_B/Titsjob.png", image_hover = "images/NS_B/Titsjob_hover.png", l_jump = "CNS_2", number = 2  )
default C_NS_ass = nsb(__("Play with her ass."),image_idle = "images/NS_B/Ass.png", image_hover = "images/NS_B/Ass_hover.png", l_jump = "CNS_3", number = 4  )
default C_NS_feet = nsb(__("Rub your cock on her feet."),image_idle = "images/NS_B/Feet.png", image_hover = "images/NS_B/Feet_hover.png", l_jump = "CNS_4", number = 6 )

default C_NS_wake_hand = nsb(__("Could you give me a handjob, please?"),image_idle = "images/NS_B/Hand3.png", image_hover = "images/NS_B/Hand3_hover.png", l_jump = "CNS_wake_1", number = 3 )
default C_NS_wake_feet = nsb(__("Could you use your feet?"),image_idle = "images/NS_B/Footjob.png", image_hover = "images/NS_B/Footjob_hover.png", l_jump = "CNS_wake_2", number = 6)

default C_NS_wake_butt = nsb(__("Buttjob."),image_idle = "images/NS_B/Ass.png", image_hover = "images/NS_B/Ass_hover.png", l_jump = "CNS_wake_butt_label", number = "4" )
default C_NS_wake_kissing = nsb(__("Kissing."),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "CNS_wake_kissing_label", number = "1" )
default C_NS_wake_licking = nsb(__("Licking."),image_idle = "images/NS_B/Licking.png", image_hover = "images/NS_B/Licking_hover.png", l_jump = "CNS_wake_licking_label", number = "4a" )
default C_NS_wake_titsjob = nsb(__("Titsjob."),image_idle = "images/NS_B/Tits.png", image_hover = "images/NS_B/Tits_hover.png", l_jump = "CNS_wake_Titsjob_label", number = "2" )

default C_NS_wake_butt_loc = nsb(__("Required: Weekend event with her."),image_idle = "images/NS_B/Ass.png", image_hover = "images/NS_B/Ass_hover.png", l_jump = "CNS_wake_butt_label", played = True, locked = True,  number = "4" )
default C_NS_wake_kissing_loc = nsb(__("Required: Weekend event with her."),image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "CNS_wake_kissing_label", played = True, locked = True,  number = "1" )
default C_NS_wake_licking_loc = nsb(__("Required: Story progress with her."),image_idle = "images/NS_B/Licking.png", image_hover = "images/NS_B/Licking_hover.png", l_jump = "CNS_wake_licking_label", played = True, locked = True,  number = "4a" )
default C_NS_wake_titsjob_loc = nsb(__("Required: Weekend event with her."),image_idle = "images/NS_B/Tits.png", image_hover = "images/NS_B/Tits_hover.png", l_jump = "CNS_wake_Titsjob_label", played = True, locked = True,  number = "2" )

default new_nsb_in_wake = False
screen C_NS_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377
    add "images/NS_B/Wake.png" xpos 1705 ypos 25

    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.c_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.c_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.c_nsb_s)/9):
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
    if len(nsb_box.c_nsb_s)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("C_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("C_NS_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("C_NS_scr"), Jump("CNS_back")]
        hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 1738
        ypos 110
        focus_mask True
        idle "images/NS_B/WakeUp.png"
        hover "images/NS_B/WakeUp_hover.png"
        if Caroline_points >=2:
            action [SetVariable("inv_page", 0),Hide("C_NS_scr"), Jump("CR2_NS_label")]
            hovered Play ("sound", "sfx/click2.wav")
        else:
            action NullAction()
            hovered [Play ("sound", "sfx/click2.wav"),Show("displayTextNS_B",tt_ypos=110, tt_xpos=1171, displayText2 = __("Required 2 relation points."),)]
            unhovered Hide("displayTextNS_B")

    if Caroline_points <2:
        add "images/NS_B/Locked_slot.png" xpos 1738 ypos 110

    for nsb in nsb_box.c_nsb_wake:

        if nsb.played == True:
            $ new_nsb_in_wake = False
        if nsb.played == False:
            $ new_nsb_in_wake = True

    if new_nsb_in_wake == True:
        add "images/NS_B/New.png" xpos 1732 ypos 98

screen C_NS_wake_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377
    $ my_tt_ypos = 0
    $ my_tt_xpos = 0
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box.c_nsb_wake, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box.c_nsb_wake)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box.c_nsb_wake)/9):
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
    if len(nsb_box.c_nsb_wake)>9:

        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("C_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("C_NS_wake_scr")]
            hovered Play ("sound", "sfx/click2.wav")

    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("C_NS_wake_scr"), Jump("CNS_back_wake")]
        hovered Play ("sound", "sfx/click2.wav")

screen displayTextNS_B:

    default displayText2 = ""

    vbox:
        xpos tt_xpos + 121
        ypos tt_ypos

        frame:
            style "frame_gui2"
            text displayText2 style "date_s"

style date_s is text:
    size 31
    text_align 0.5
style frame_gui2:
    padding gui.frame_borders.padding
    background Frame("gui/frame2.png", 25, 25)
    xmaximum 520
