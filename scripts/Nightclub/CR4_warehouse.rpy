image CR4_warehouse_p1 = "images/Nightclub/Warehouse/1.jpg"
image CR4_warehouse_p2 = "images/Nightclub/Warehouse/2.jpg"
image CR4_warehouse_p2a = "images/Nightclub/Warehouse/2a.jpg"
image CR4_warehouse_p3 = "images/Nightclub/Warehouse/3.jpg"
image CR4_warehouse_p4 = "images/Nightclub/Warehouse/4.jpg"
image CR4_warehouse_p5 = "images/Nightclub/Warehouse/5.jpg"
image CR4_warehouse_p6 = "images/Nightclub/Warehouse/6.jpg"
image CR4_warehouse_p7 = "images/Nightclub/Warehouse/7.jpg"
image CR4_warehouse_p8 = "images/Nightclub/Warehouse/8.jpg"
image CR4_warehouse_p9 = "images/Nightclub/Warehouse/9.jpg"
image CR4_warehouse_p10 = "images/Nightclub/Warehouse/10.jpg"
image CR4_warehouse_p11 = "images/Nightclub/Warehouse/11.jpg"
image CR4_warehouse_p12 = "images/Nightclub/Warehouse/12.jpg"
image CR4_warehouse_p13 = "images/Nightclub/Warehouse/13.jpg"


label CR4_warehouse:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    hide screen map
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)

    scene CR4_warehouse_p1 with dissolve
    MC "(Christ almighty… Is this a warehouse? It looks like a damn supervillain’s lair!)"
    MC "Hmm… (Where the hell would I store a pink box in a place like this?)"

    scene CR4_warehouse_p2
    MC "(Shit… there’s security guards too.)"
    MC "(I’m gonna have to be careful with how I proceed.)"

    $ can_hide_windows = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    call screen CR4_warehouse_scr

    screen CR4_warehouse_scr:
        add "images/Nightclub/Warehouse/Map.jpg"
        imagebutton:
            xpos 288
            ypos 461
            focus_mask True
            idle "images/Nightclub/Warehouse/B1.png"
            hover "images/Nightclub/Warehouse/B1_hover.png"
            hovered Show("displayTextScreen", displayText = "Barrels")
            if clickable == True:
                action [Hide("displayTextScreen"),Hide("CR4_warehouse_scr"),Jump("start_w_minigame")]
            unhovered Hide("displayTextScreen")


label CR4_warehouse_con:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    $ can_hide_windows = True
    scene CR4_warehouse_p2a
    MC "(Phew. I finally made it past those guys.)"
    MC "(This must be some serious operation they’re running here.)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music2", loop=True, fadein = 2)
    scene CR4_warehouse_p3
    MC "*Whistle* Holy moly!"
    MC "There’s NO way someone makes this much money running a nightclub…"

    scene CR4_warehouse_p4
    MC "(Who the HELL have you gotten yourself involved with, Cindy?)"
    MC "(I mean, there’s guns, drugs, bars of gold… Fuck me… This is insane.)"
    MC "(No wonder there is a password to speak with the Boss!)"

    scene CR4_warehouse_p5
    MC "(That must be… cocaine, right?)"
    MC "(Sweet Jesus, there’s dozens of bricks of the stuff! Whoever owns this would make Pablo Escobar jealous!)"

    scene CR4_warehouse_p6
    MC "(This place is a COD fanboy’s wet dream…)"
    MC "(This has to be an organised crime gang. There’s just no other explanation for it, right?)"

    scene CR4_warehouse_p7
    MC "(This must be where they prepare the bricks prior to shipping them out.)"
    MC "(There’s no other explanation for it - I’m in the central hub of their operation right now.)"

    scene CR4_warehouse_p8
    MC "If anyone catches me here, I’m a dead man…"
    MC "I just have to find this pink box and get the fuck out of here as fast as possible."

    scene CR4_warehouse_p9
    MC "(Delivery schedules? Yeah, this isn’t just some run-of-the-mill street corner drug dealer.)"
    MC "(I wonder if Caroline’s necklace is hidden in this room.)"

    scene CR4_warehouse_p10
    MC "(It’s probably not worth the risk, searching for it. If I can meet with the Boss I can probably talk him into returning it.)"
    MC "(I just hope he doesn’t want me to buy it back. I don’t know if I could afford it…)"
    scene black
    $ can_hide_windows = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    call screen CR4_warehouse_scr2

    screen CR4_warehouse_scr2:
        add "images/Nightclub/Warehouse/Map3.jpg"
        if cindy_box not in inventory.items:
            imagebutton:
                xpos 591
                ypos 599
                focus_mask True
                idle "images/Nightclub/Warehouse/B2.png"
                hover "images/Nightclub/Warehouse/B2_hover.png"
                hovered Show("displayTextScreen", displayText = "Pink box")
                if clickable == True:
                    action [Hide("displayTextScreen"),addItem(cindy_box),Jump("CR4_warehouse_box")]
                    unhovered Hide("displayTextScreen")
label CR4_warehouse_box:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    $ can_hide_windows = True
    scene CR4_warehouse_p11
    MC "(Well, this looks like the box that Cindy was describing.)"
    MC "(I wonder what’s in here - it seems so out of place compared to the guns and gold.)"
    MC "(I guess it wouldn't hurt to take a peek...)"

    scene CR4_warehouse_p12
    MC "…"
    MC "Blunts? Seriously? This is what I’m risking my life for?"

    scene CR4_warehouse_p13
    MC "(That girl, Cindy, is a nutcase!)"
    MC "(There must be A HUNDRED safer ways to score some weed in this city!)"
    MC "(Here’s hoping I don’t get shot to pieces, trying to escape this damn warehouse.)"

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ warehouse_unlocked = False
    $ CR4_Cindy_S1 = 3

    jump map_label