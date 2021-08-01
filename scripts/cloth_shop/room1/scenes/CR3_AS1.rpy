image CR3_AS1_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS1/1.jpg"
image CR3_AS1_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS1/2.jpg"
image CR3_AS1_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS1/3.jpg"
image CR3_AS1_p4 = "images/cloth_shop/room1/day/scenes/CR3_AS1/4.jpg"
image CR3_AS1_p5 = "images/cloth_shop/room1/day/scenes/CR3_AS1/5.jpg"

label CR3_AS1_label:

    if CR3_AS1_can == 4:

        hide screen map_button
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "(Maybe I should speak to her while she's not in the shop? She probably thinking about the stuff we did in here...)"
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    if CR3_AS1_can == 3:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR3_AS1_p1 with dissolve
        MC "Hey, Caroline. I was walking past, so I thought I’d drop in to check how you’re doing."
        Caroline "Sorry, I’m up to my eyeballs with work at the minute. Please leave."
        MC "Huh? So cold.. Did I do something wrong?"
        scene CR3_AS1_p2
        Caroline "You know that the deal is over... I.. I just want to move on. Give me a few days."
        MC "(Maybe I should speak to her while she's not in the shop? She probably thinking about the stuff we did in here...)"
        $ clickable = True
        $ CR3_AS1_can = 4
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    if CR3_AS1_can == False:
        hide screen map_button
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I've promised Caroline that I'll talk with Violet. She should be in the dark alley."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label
    else:

        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music1", loop=True, fadein = 2)

        scene CR3_AS1_p1 with dissolve


        MC "Hey, Caroline. I was walking past, so I thought I’d drop in, to check how you’re doing."
        Caroline "Hi, [player_name]. Sorry, I’m - up to my eyeballs - with work, at the minute."
        MC "You look stressed, what’s wrong?"
        Caroline "*Sigh* I still haven’t found a staff member to replace you. The worst part is, I bought a whole new set of clothes, but these ones are for couples - so I’m going to need another model."

        scene CR3_AS1_p2

        MC "I could help! I don’t mind!"
        Caroline "Listen - I really appreciate the offer. You need to understand that the deal is NOT coming back. I’ll find another way to pay you for your time - but things can’t go back to the way they were."
        MC "Fine... I understand. If I volunteer to help, model the clothes, are we good to start work, then?"


        scene CR3_AS1_p3

        Caroline "Eh, not quite. We’re halfway there, though!"
        MC "Huh? What’s missing?"
        Caroline "Think about it? If we’re BOTH modelling clothes, then who is there to take the pictures?"
        MC "Ahh... bugger."

        scene CR3_AS1_p4

        Caroline "I’ve burned through, my list of potential candidates. None of them are free to work for me. It leaves me with only two options."
        MC "Who?"
        Caroline "Well, the first choice was you. So that leaves my second... Violet."

        scene CR3_AS1_p5

        Caroline "Can you see if you can track Violet down? Last I heard, she was still hanging around - that mangy old alleyway."
        MC "Sure! No problem. I’ll see if I can find her, then we can - get cracking - on photographing this new range."
        MC "I’m super excited to see what you’ve bought!"
        Caroline "Trust me - these new clothes are going to sell like hotcakes!"

        $ CR3_AS1_can = False
        $ CR2_VS = True

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump cloth_shop_open_label