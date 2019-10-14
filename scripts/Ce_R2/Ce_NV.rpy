image Ce_NV_p1 = "images/CeR2/NV/1.jpg"
image Ce_NV_p2 = "images/CeR2/NV/2.jpg"
image Ce_NV_p3 = "images/CeR2/NV/3.jpg"
image Ce_NV_p4 = "images/CeR2/NV/4.jpg"
image Ce_NV_p5 = "images/CeR2/NV/5.jpg"
image Ce_NV_p6 = "images/CeR2/NV/6.jpg"
image Ce_NV_p7 = "images/CeR2/NV/7.jpg"
image Ce_NV_p8 = "images/CeR2/NV/8.jpg"

init python:

    class nsb1(store.object):
        def __init__(self, name, number, image_idle= "", image_hover= "", l_jump= "", played = False, locked = False, t_played = 0000 ):
            self.name = name
            self.number = number
            self.image_idle = image_idle 
            self.image_hover = image_hover
            self.l_jump = l_jump
            self.played = played
            self.locked = locked
            self.t_played = t_played

    class Nsb_box1(store.object):
        def __init__(self):
            
            
            
            
            self.ce_nsb_s = []
            self.ce_nsb_s_wake = []
            
            self.ce1_nsb_s = []
            self.ce1_nsb_s_wake = []
            
            self.ce2_nsb_s = []
            self.ce2_nsb_s_wake = []
            
            self.ce3_nsb_s = []
            self.ce3_nsb_s_wake = []
        
        
        def add_ce(self, nsb1):
            self.ce_nsb_s.append(nsb1)
        def drop_ce(self, nsb1):
            self.ce_nsb_s.remove(nsb1)
        
        def add_ce_wake(self, nsb1):
            self.ce_nsb_s_wake.append(nsb1)
        def add_ce_wake(self, nsb1):
            self.ce_nsb_s_wake.remove(nsb1)
        
        
        def add_ce1(self, nsb1):
            self.ce1_nsb_s.append(nsb1)
        def drop_ce1(self, nsb1):
            self.ce1_nsb_s.remove(nsb1)
        
        def add_ce1_wake(self, nsb1):
            self.ce1_nsb_s_wake.append(nsb1)
        def add_ce1_wake(self, nsb1):
            self.ce1_nsb_s_wake.remove(nsb1)
        
        def add_ce2(self, nsb1):
            self.ce2_nsb_s.append(nsb1)
        def drop_ce2(self, nsb1):
            self.ce2_nsb_s.remove(nsb1)
        
        def add_ce2_wake(self, nsb1):
            self.ce2_nsb_s_wake.append(nsb1)
        def add_ce2_wake(self, nsb1):
            self.ce2_nsb_s_wake.remove(nsb1)
        
        def add_ce3(self, nsb1):
            self.ce3_nsb_s.append(nsb1)
        def drop_ce3(self, nsb1):
            self.ce3_nsb_s.remove(nsb1)
        
        def add_ce3_wake(self, nsb1):
            self.ce3_nsb_s_wake.append(nsb1)
        def add_ce3_wake(self, nsb1):
            self.ce3_nsb_s_wake.remove(nsb1)



    class clickedNsb1(Action):
        
        def __init__(self, object):
            self.object = object
        
        def __call__(self):
            new_value2 = True
            new_value3 = self.object.t_played + 1
            if self.object.t_played <9999:
                
                setattr(self.object, "t_played", new_value3)
            setattr(self.object, "played", new_value2)

default nsb_box1 = Nsb_box1()
default Ce_NV = True
default Ce_visited = 0
default Ce_NS_cock = nsb1("Slide your cock into her mouth.",image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "Ce_NV_blow", number = "1"  )
default Ce_NS_feet = nsb1("Footjob.",image_idle = "images/NS_B/Feet.png", image_hover = "images/NS_B/Feet_hover.png", l_jump = "Ce_NV_foot", number = "6" )
default Ce_NS_kissing = nsb1("Kissing.",image_idle = "images/NS_B/Blowjob.png", image_hover = "images/NS_B/Blowjob_hover.png", l_jump = "Ce_NV_kiss", number = "1a ")
default Ce_NS_pussy = nsb1("Pussy",image_idle = "images/NS_B/Pussy.png", image_hover = "images/NS_B/Pussy_hover.png", l_jump = "Ce_NV_pussy", number = "4" )
default Ce_NS_tits = nsb1("Tits",image_idle = "images/NS_B/Titsjob.png", image_hover = "images/NS_B/Titsjob_hover.png", l_jump = "Ce_NV_tits", number = "2"  )
label Ce_NV_lab:
    if Ce_NV == False:
        show screen Ce_bedroom_N_scr
        $ clickable = False
        MC "(I've already done something tonight.. I’ll let her sleep.)"
        $ clickable = True
        hide screen Ce_bedroom_N_scr
        jump Ce_bedroom_M1

    if Ce_NV == True:

        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene Ce_NV_p1 with dissolve

        MC "(Judy giving me a key to Celia’s home was the best thing that therapy ever did for me!)"
        MC "(I guess you could call it a ‘break in’ rather than a ‘breakthrough.’)"
        scene Ce_NV_p2
        Celia "Zzz..."
        MC "(Let’s strip these sheets back and see what I’ve got to play with.)"
        scene Ce_NV_p3
        MC "(And voila!)"
        MC "(Very nice! She sleeps in her underwear; that makes things so much easier for me!)"
        scene Ce_NV_p4
        Celia "*Snore*"
        MC "(Okay, now to figure out what I’m going to do to this bitch!)"
        scene Ce_NV_p5
        MC "(I could play with her pussy or her tits.)"
        MC "(But then again, it would be fun to make her give me a footjob.)"
        scene Ce_NV_p6
        MC "(Alternatively, I could just make her lips suck my cock.)"
        MC "(Or I could make out with her.)"
        scene Ce_NV_p7
        MC "(I really am spoiled for choice. I guess I’ll roll her over first and just take things from there.)"
        Celia "Ugh… Mmm… Zzz…"
        scene Ce_NV_p8
        Celia "*Snore*"
        MC "*Phew* (I thought I’d woken her up for a second there!)"
        MC "(Alright, it’s party time!)"
        $ can_hide_windows = False
        jump Ce_NV_menu


label Ce_NV_menu:
    $ Ce_NV = False
    $ inv_page = 0
    $ Ce_visited +=1
    if not Ce_NS_cock in nsb_box1.ce_nsb_s:
        $ nsb_box1.add_ce(Ce_NS_cock)
        $ nsb_box1.add_ce(Ce_NS_feet)
        $ nsb_box1.add_ce(Ce_NS_kissing)
        $ nsb_box1.add_ce(Ce_NS_tits)

    $ renpy.block_rollback()
    call screen Ce_NV_scr

label Ce_NV_back:

    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black with dissolve
    $ renpy.pause(2, hard = True)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump Ce_bedroom_M1
screen Ce_NV_scr:
    add "images/NS_B/Ground.png" xpos 25 ypos 377



    $ new_nsb_in_wake = False
    $ x = 44
    $ y = 350
    $ i = 0
    $ sorted_nsb = sorted(nsb_box1.ce_nsb_s, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(nsb_box1.ce_nsb_s)/9):
        $ next_inv_page = 0
    if prev_inv_page < int(len(nsb_box1.ce_nsb_s)/9):
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
    if len(nsb_box1.ce_nsb_s)>9:


        imagebutton:
            xpos 55
            ypos 902
            focus_mask True
            idle "images/NS_B/NextL.png"
            hover "images/NS_B/NextL_hover.png"
            action [SetVariable('inv_page', prev_inv_page), Show("Ce_NV_scr")]
            hovered Play ("sound", "sfx/click2.wav")
        imagebutton:
            xpos 328
            ypos 902
            focus_mask True
            idle "images/NS_B/NextR.png"
            hover "images/NS_B/NextR_hover.png"
            action [SetVariable('inv_page', next_inv_page), Show("Ce_NV_scr")]
            hovered Play ("sound", "sfx/click2.wav")
    imagebutton:
        xpos 191
        ypos 902
        focus_mask True
        idle "images/NS_B/Cancel.png"
        hover "images/NS_B/Cancel_hover.png"
        action [SetVariable("inv_page", 0),Hide("Ce_NV_scr"), Jump("Ce_NV_back")]
        hovered Play ("sound", "sfx/click2.wav")






    for nsb1 in nsb_box1.ce_nsb_s:

        if nsb1.played == True:
            $ new_nsb_in_wake = False
        if nsb1.played == False:
            $ new_nsb_in_wake = True