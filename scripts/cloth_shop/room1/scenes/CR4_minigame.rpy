default clothes6 = Clothes_item("Shirt and Jeans", c_image="images/clothes_minigame/6.png", c_hover="images/clothes_minigame/6_hover.png", c_text = "I need clothes that fully cover me and I can walk around town casually.")
default clothes8 = Clothes_item("Shirt and Jean Shorts", c_image="images/clothes_minigame/8.png", c_hover="images/clothes_minigame/8_hover.png", c_text = "I just shaved my legs. I need something that I can walk around in, that will show off my legs. But just my legs. I wAnt to be covered on top.")
default clothes12 = Clothes_item("Athletic Outfit", c_image="images/clothes_minigame/12.png", c_hover="images/clothes_minigame/12_hover.png", c_text = "I'm a really outgoing and sporty person. I go out jogging every day. I need clothes that can take a lot of wear.")
default clothes15 = Clothes_item("Top and Capri Pants", c_image="images/clothes_minigame/15.png", c_hover="images/clothes_minigame/15_hover.png", c_text = "I have a great tan and I want to walk around town in something to show it off without seeming too slutty.  Maybe just showing a little arm and leg.")
default clothes18 = Clothes_item("Bunny Outfit", c_image="images/clothes_minigame/18.png", c_hover="images/clothes_minigame/18_hover.png", c_text = "My husband spends all his nights at the strip club these days. I just ordered a dancing pole and I need a dress that will make him stay at home and take notice.")
default clothes23 = Clothes_item("Nurse Outfit", c_image="images/clothes_minigame/23.png", c_hover="images/clothes_minigame/23_hover.png", c_text = "My husband is at home in bed with a broken leg. He doesn't feel like doing anything naughty because he says he's in pain. I need something that will make him forget his injury and show more interest in me.")
default clothes29 = Clothes_item("Mime Costume", c_image="images/clothes_minigame/29.png", c_hover="images/clothes_minigame/29_hover.png", c_text = "My husband is really chatty when he gets back from work, but I just want to relax and don't want to hear about his shitty day. I need an outfit that says I'm not going to talk to him.")
default clothes40 = Clothes_item("Teddy Lingerie", c_image="images/clothes_minigame/40.png", c_hover="images/clothes_minigame/40_hover.png", c_text = "My husband wants me to wear less to bed as he thinks that will be sexy, but I keep saying I will get too cold. I need something that is sexy, and also keeps me warm at night.")
default clothes44 = Clothes_item("Schoolgirl Uniform", c_image="images/clothes_minigame/44.png", c_hover="images/clothes_minigame/44_hover.png", c_text = "My husband is pretty boring, he's the headmaster of a school. I need something that will spice things up in the bedroom.")
default clothes45 = Clothes_item("Maid Uniform", c_image="images/clothes_minigame/45.png", c_hover="images/clothes_minigame/45_hover.png", c_text = "My boyfriend gets turned on watching me clean, I want clothes that will make cleaning even more sexy.")
default clothes53 = Clothes_item("Builder Outfit", c_image="images/clothes_minigame/53.png", c_hover="images/clothes_minigame/53_hover.png", c_text = "My husband is really into DIY work. I can never pull him away enough to notice me. Do you have something that might interest him.")


image mc_wait1 = "images/clothes_minigame/Guests1.jpg"
image mc_wait2 = "images/clothes_minigame/Guests2.jpg"
image mc_wait3 = "images/clothes_minigame/Guests3.jpg"
image mc_wait4 = "images/clothes_minigame/Guests4.jpg"
image mc_wait5 = "images/clothes_minigame/Guests5.jpg"
image mc_wait6 = "images/clothes_minigame/Guests6.jpg"
image mc_wait7 = "images/clothes_minigame/Guests7.jpg"


image game_bg = "images/clothes_minigame/Game.jpg"

define Customer = Character("Customer")
default clothes_inv = Clothes_inv()
init -1 python:

    import renpy.store as store
    import renpy.exports as renpy
    from operator import attrgetter

    clo_page = 0
init python:
    clothes_item = None
    class Clothes_item(store.object):
        selected = False
        def __init__(self, c_name, c_image="", c_hover="", c_text=""):
            self.c_name = c_name
            self.c_image = c_image
            self.c_hover = c_hover
            self.c_text= c_text

    class Clothes_inv(store.object):
        def __init__(self):
            self.clothes = []
        
        def drop(self, clothes_item):
            self.clothes.remove(clothes_item)

    class testClothes(Action):
        
        def __init__(self, clothes_item, switch, value, remove = True):
            self.clothes_item = clothes_item
            self.switch = switch
            self.value = value
            self.remove = remove
        
        def __call__(self):
            if store.active_clothes != None and store.active_clothes == self.clothes_item:
                setattr(store, self.switch, self.value)
                if self.remove:
                    Clothes_inv.clothes.remove(self.clothes_item)
                    store.active_item = None
            renpy.restart_interaction()

style frame_gui4:
    padding gui.frame_borders.padding
    background Frame("gui/frame1.png", 25, 25)
    xmaximum 650

label start_clo_minigame:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    $ clo_money = 0
    $ clo_loop = 1
    $ mc_wait = [1,2,3,4,5,6,7]
    $ clothes_rool2 = [1,2,3,4]
    if CR4_AS3 == 4:
        $ clothes_rool2.remove(4)
        $ clo_loop = 2
    jump clothes_minigame


label clothes_minigame:
    if clo_loop ==5:
        scene CR4_AS3_p8
        call screen clo_end_screen
    $ mc_wait_roll = renpy.random.choice(mc_wait)
    $ mc_wait.remove(mc_wait_roll)

    if mc_wait_roll == 1:
        scene mc_wait1
    if mc_wait_roll == 2:
        scene mc_wait2
    if mc_wait_roll == 3:
        scene mc_wait3
    if mc_wait_roll == 4:
        scene mc_wait4
    if mc_wait_roll == 5:
        scene mc_wait5
    if mc_wait_roll == 6:
        scene mc_wait6
    if mc_wait_roll == 7:
        scene mc_wait7

    $ renpy.pause(2, hard = True)




    $ clothes_rolled3 = renpy.random.choice(clothes_rool2)
    $ clothes_rool2.remove(clothes_rolled3)

    if clothes_rolled3 == 1:

        if CR4_AS3 == 2:
            $ clothes_rolled = clothes6
            $ clothes_inv.clothes = [clothes6,clothes8,clothes12,clothes53]
        if CR4_AS3 == 3:
            $ clothes_rolled = clothes15
            $ clothes_inv.clothes = [clothes15,clothes8,clothes12,clothes53]
        if CR4_AS3 == 4:
            $ clothes_rolled = clothes29
            $ clothes_inv.clothes = [clothes29,clothes44,clothes12,clothes53]

    if clothes_rolled3 == 2:

        if CR4_AS3 == 2:
            $ clothes_rolled = clothes18
            $ clothes_inv.clothes = [clothes18,clothes6,clothes15,clothes12]
        if CR4_AS3 == 3:
            $ clothes_rolled = clothes23
            $ clothes_inv.clothes = [clothes23,clothes8,clothes6,clothes44]
        if CR4_AS3 == 4:
            $ clothes_rolled = clothes12
            $ clothes_inv.clothes = [clothes12,clothes40,clothes23,clothes15]

    if clothes_rolled3 == 3:

        if CR4_AS3 == 2:
            $ clothes_rolled = clothes40
            $ clothes_inv.clothes = [clothes40,clothes12,clothes23,clothes15]
        if CR4_AS3 == 3:
            $ clothes_rolled = clothes45
            $ clothes_inv.clothes = [clothes45,clothes44,clothes12,clothes18]
        if CR4_AS3 == 4:
            $ clothes_rolled = clothes44
            $ clothes_inv.clothes = [clothes44,clothes45,clothes12,clothes18]

    if clothes_rolled3 == 4:

        if CR4_AS3 == 2:
            $ clothes_rolled = clothes53
            $ clothes_inv.clothes = [clothes53,clothes45,clothes29,clothes44]
        if CR4_AS3 == 3:
            $ clothes_rolled = clothes8
            $ clothes_inv.clothes = [clothes8,clothes45,clothes40,clothes53]

    $ clo_loop += 1
    scene game_bg
    $ renpy.block_rollback()
    show screen clothes_minigame_cust_scr
    call screen clothes_minigame_scr



screen clothes_minigame_scr:
    modal True
    key "hide_windows" action NullAction()
    add "images/clothes_minigame/Outfits.png" xpos 147 ypos 83

    vbox xpos 10 ypos 10 spacing 20:
        frame:
            style "frame_gui1"
            text "[clo_money]$" size 30

    $ x = 800
    $ y = -100
    $ i = 0
    $ sorted_clothes = sorted(clothes_inv.clothes, key=attrgetter('c_name'))
    $ next_clo_page = clo_page + 1
    if next_clo_page > int(len(clothes_inv.clothes)/4):
        $ next_clo_page = 0

    for clothes_item in sorted_clothes:
        if i+1 <= (clo_page+1)*4 and i+1>clo_page*4:
            $ x += 250
            if i%2==0:
                $ y += 300
                $ x = 250
            $ pic = clothes_item.c_image

            $ pich = clothes_item.c_hover
            imagebutton:
                xpos x
                ypos y
                idle pic
                hover pich
                if clothes_rolled == clothes_item:

                    action [SetVariable("clothes_item", clothes_item),Hide("clothes_minigame_cust_scr"),Hide("displayTextNS_B"),Jump("clo_money_add")]
                else:
                    action [SetVariable("clothes_item", clothes_item), Hide("clothes_minigame_cust_scr"),Hide("displayTextNS_B"),Show("clothes_minigame_cust_bad_scr")]
                hovered [Play ("sound", "sfx/click2.wav"), Show("displayTextNS_B",tt_ypos=y, tt_xpos=x, displayText2 = [clothes_item.c_name]),]
                unhovered Hide("displayTextNS_B")
        $ i += 1

screen clothes_minigame_cust_scr:

    vbox:
        xpos 1200
        ypos 150
        frame:
            style "frame_gui4"
            text "{color=#66ff66}Customer:{/color} \n[clothes_rolled.c_text]"

screen clothes_minigame_cust_bad_scr:
    modal True
    timer 2.0 action [Hide("clothes_minigame_cust_bad_scr"),Jump("clo_money_lose")]
    vbox:
        xpos 1200
        ypos 150
        frame:
            style "frame_gui4"
            text "{color=#66ff66}Customer:{/color} \nIt's not what I wanted!? What the fuck is wrong with you!?"

label clo_money_add:
    $ clo_money += 5
    $ renpy.block_rollback()
    jump clothes_minigame

label clo_money_lose:
    if clo_money >=5:
        $ clo_money -= 5
    else:
        $ clo_money = 0
    $ renpy.block_rollback()
    jump clothes_minigame

screen clo_end_screen:
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "work2minigame/bob_done.png"
        hover "work2minigame/bob_done.png"
        action [Hide("clo_end_screen"), Jump("clo_minigame_end"),]

    text "{size=+25}[clo_money]${/size}" xpos 1090 ypos 455


label clo_minigame_end:
    $ inventory.earn(clo_money)
    $ CR4_AS3 += 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    if CR4_AS3 == 5:
        jump CR4_AS3_ex_label
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ day_time = 3
    jump map_label