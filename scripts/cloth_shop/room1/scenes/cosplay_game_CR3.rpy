init python:

    class outfit(store.object):
        def __init__(self, number, image_idle= "", image_hover= "", l_jump= "", played = False, locked = False,t_played = 0 ):
            self.number = number
            self.image_idle = image_idle 
            self.image_hover = image_hover
            self.l_jump = l_jump
            self.played = played
            self.locked = locked
            self.t_played = t_played

    class Outfit_box(store.object):
        def __init__(self):
            
            self.outfit_store = []
        
        def add_outfit(self, outfit):
            self.outfit_store.append(outfit)
        def drop_outfit(self, outfit):
            self.outfit_store.remove(outfit)

default outfit_box = Outfit_box()
default C_R3_outfit1 = outfit(image_idle = "images/cosplay_minigame/R3/1.png", image_hover = "images/cosplay_minigame/R3/1a.png", l_jump = "CR3_AS3_O1", number = "1")
default C_R3_outfit2 = outfit(image_idle = "images/cosplay_minigame/R3/2.png", image_hover = "images/cosplay_minigame/R3/2a.png", l_jump = "CR3_AS4_O2", number = "2")
default C_R3_outfit3 = outfit(image_idle = "images/cosplay_minigame/R3/3.png", image_hover = "images/cosplay_minigame/R3/3a.png", l_jump = "CR3_AS8_O3", number = "3")
default C_R3_outfit4 = outfit(image_idle = "images/cosplay_minigame/R3/4.png", image_hover = "images/cosplay_minigame/R3/4a.png", l_jump = "CR3_AS9_O4", number = "4")

default C_R3_outfit2_loc = outfit(image_idle = "images/cosplay_minigame/R3/2.png", image_hover = "images/cosplay_minigame/R3/2a.png", l_jump = "CNS_1", number = "3",locked = True, played = True)
default C_R3_outfit3_loc = outfit(image_idle = "images/cosplay_minigame/R3/3.png", image_hover = "images/cosplay_minigame/R3/3a.png", l_jump = "CNS_1", number = "3",locked = True, played = True)
default C_R3_outfit4_loc = outfit(image_idle = "images/cosplay_minigame/R3/4.png", image_hover = "images/cosplay_minigame/R3/4a.png", l_jump = "CNS_1", number = "4", locked = True, played = True)

label cosplay_CR3_label:
    if Caroline_points == 3 and not C_R3_outfit1 in outfit_box.outfit_store:
        $ outfit_box.add_outfit(C_R3_outfit1)
        $ outfit_box.add_outfit(C_R3_outfit2_loc)
        $ outfit_box.add_outfit(C_R3_outfit3_loc)
        $ outfit_box.add_outfit(C_R3_outfit4_loc)
    call screen cosplay_CR3_scr

screen cosplay_CR3_scr:
    modal True
    add "images/cosplay_minigame/R2/CosplaySelect/Outfits.png"
    imagebutton:
        xpos 1104
        ypos 209
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [Hide ("cosplay_CR3_scr"),Jump("cosplay_CR3_close")]

    $ new_nsb_in_wake = False
    $ x = 699
    $ y = 130
    $ i = 0
    $ sorted_nsb = sorted(outfit_box.outfit_store, key=attrgetter('number'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(outfit_box.outfit_store)/4):
        $ next_inv_page = 0
    if prev_inv_page < int(len(outfit_box.outfit_store)/4):
        $ prev_inv_page = 0

    for outfit in sorted_nsb:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 180
            if i%2==0:
                $ y += 200
                $ x = 793
            imagebutton:
                xpos x
                ypos y
                focus_mask True
                idle outfit.image_idle
                hover outfit.image_hover
                if outfit.locked == False and outfit.t_played == 0:
                    action [clickedNsb(outfit), Jump(outfit.l_jump)]
                else:
                    action NullAction()
                hovered [Play ("sound", "sfx/click2.wav")]

            if outfit.t_played == 1:
                add "images/cosplay_minigame/R3/Done.png" xpos x - 10 ypos y - 10
            if outfit.played == False:
                add "images/NS_B/New.png" xpos x - 6 ypos y - 10
            if outfit.locked == True:
                add "images/cosplay_minigame/R3/Loc.png" xpos x ypos y
        $ i += 1

label cosplay_CR3_close:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump cloth_shop_open_label

