image CR2_AS5_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS5/1.jpg"
image CR2_AS5_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS5/2.jpg"
image CR2_AS5_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS5/3.jpg"
image CR2_AS5_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS5/4.jpg"
image CR2_AS5_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS5/5.jpg"
image CR2_AS5_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS5/6.jpg"

default CR2_AS5_q1 = True
default CR2_AS5_q2 = True
default CR2_AS5_q3 = True
default CR2_AS5_q4 = True
label CR2_AS5_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_AS5_p1
    $ can_hide_windows = True
    MC "(I thought her laptop was stolen...)"
    MC "(I thought she didn't have any money left.)"

    scene CR2_AS5_p2

    MC "Hey, Caroline. Wha-"

    scene CR2_AS5_p3

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Caroline "Ah! [player_name]! "
    Caroline "You scared me!"

    scene CR2_AS5_p4

    MC "Haha!"
    Caroline "Is something wrong?"
    MC "No. I just noticed that the shop was open."
    Caroline "At the current moment, it's not like there's a reason to close it."
    jump CR2_AS5_menu

label CR2_AS5_menu:
    scene CR2_AS5_p4
    window hide
    menu:
        "How could you afford that laptop? " if CR2_AS5_q1 == True:
            scene CR2_AS5_p5
            MC "How could you afford that laptop? Did you get your money back?"
            if renpy.loadable("patch.rpy"):
                Caroline "No... It's Mom's laptop. I only borrowed it."
            else:
                Caroline "No... It's Linda's laptop. I only borrowed it."
            if renpy.loadable("patch.rpy"):
                MC "Does Mom know?"
            else:
                MC "Does Linda's know?"
            Caroline "N-No..."
            Caroline "I’ll return it to her today. I only needed it for a couple of hours."
            MC "Okay. I understand."
            $ CR2_AS5_q1 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False:
                jump CR2_AS5_continue
            else:
                jump CR2_AS5_menu

        "What are you doing?" if CR2_AS5_q2 == True:
            scene CR2_AS5_p6
            Caroline "I'm checking all the incoming shipments. "
            Caroline "I have some good news and some bad news for you. Which one do you want to hear first?"
            jump CR2_AS5_menu_g_b

label CR2_AS5_menu_g_b:

    window hide
    menu:
        "Good." if CR2_AS5_q3 == True:
            Caroline "There's one shipment that I already paid for online! So I'll have new customers for the new catalog."
            MC "That's good. I can still be your photographer."
            Caroline "Yes.. No..."
            MC "What?"
            $ CR2_AS5_q3 = False
            if CR2_AS5_q4 == True:
                jump CR2_AS5_menu_g_b
            if CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                $ CR2_AS5_q2 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False and CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                jump CR2_AS5_continue
            if CR2_AS5_q1 == True:
                jump CR2_AS5_menu

        "Bad" if CR2_AS5_q4 == True:
            scene CR2_AS5_p5
            Caroline "The bad news, is that this new catalog will have costumes for both, men and ladies."
            MC "I think... I know where this is going..."
            Caroline "Yes. We both will be wearing costumes, which leaves us with a need for one more person, as a photographer."
            Caroline "But no need to panic. I have some time to find someone."
            $ CR2_AS5_q4 = False
            if CR2_AS5_q3 == True:
                jump CR2_AS5_menu_g_b
            if CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                $ CR2_AS5_q2 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False and CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                jump CR2_AS5_continue
            if CR2_AS5_q1 == True:
                jump CR2_AS5_menu

label CR2_AS5_continue:
    scene CR2_AS5_p1
    if renpy.loadable("patch.rpy"):
        Caroline "Oh no! It’s nearly time! Mom will be back at home soon!"
    else:
        Caroline "Oh no! It’s nearly time! Linda will be back at home soon!"
    Caroline "Come on! Turn off!"
    if renpy.loadable("patch.rpy"):
        MC "You better hurry up. Mom will be really mad if she notices her laptop missing."
    else:
        MC "You better hurry up. Linda will be really mad if she notices her laptop missing."
    Caroline "I know!"
    if renpy.loadable("patch.rpy"):
        Caroline "I should have finished a while ago! But there were just too many incest stories on the desktop and it made it hard to find every new file I downloaded!"
    else:
        Caroline "I should have finished a while ago! But there were just too many shota stories on the desktop and it made it hard to find every new file I downloaded!"
    MC "(What!?)"
    Caroline "I wonder what they were all for anyway!?"
    MC "M-maybe some kind of Virus..."
    MC "Well.. A-anyway.. See you later."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ day_time = 3
    $ CR2_AS5 = False
    $ can_hide_windows = False
    jump map_label
