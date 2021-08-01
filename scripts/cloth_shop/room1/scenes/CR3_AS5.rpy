image CR3_AS5_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS5/1.jpg"
image CR3_AS5_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS5/2.jpg"
image CR3_AS5_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS5/3.jpg"
image CR3_AS5_p4 = "images/cloth_shop/room1/day/scenes/CR3_AS5/4.jpg"
image CR3_AS5_p5 = "images/cloth_shop/room1/day/scenes/CR3_AS5/5.jpg"
image CR3_AS5_p6 = "images/cloth_shop/room1/day/scenes/CR3_AS5/6.jpg"
image CR3_AS5_p7 = "images/cloth_shop/room1/day/scenes/CR3_AS5/7.jpg"
image CR3_AS5_p8 = "images/cloth_shop/room1/day/scenes/CR3_AS5/8.jpg"
image CR3_AS5_p9 = "images/cloth_shop/room1/day/scenes/CR3_AS5/9.jpg"

label CR3_AS5_label:

    hide screen map_button

    if CR3_AS5_can > 2 and CR3_AS5_can < 6:
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "She told me to wait a few days."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    if CR3_weekend_event == True:
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I should meet up with her at the weekend."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music1", loop=True, fadein = 2)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    if CR3_AS5_can == 2:

        scene CR3_AS5_p1 with dissolve

        Caroline "Thanks for coming to see me, [player_name]. I wanted to talk with you."
        MC "(Oh, my God! Is she thinking of starting a new deal? I’ve definitely felt some - sexual tension - during out photoshoots. She HAS to have felt the same way!)"
        MC "No problem, Caroline. What’s up?"

        scene CR3_AS5_p2

        Caroline "I’ve sent off, my sales figures and stock details, to my accountant. I’m waiting for him to get back to me."
        Caroline "I can’t guarantee it, yet - but I think we’re set, to post - record profits."
        MC "Really?!"
        Caroline "Oh yeah!"

        scene CR3_AS5_p3

        Caroline "Come back and speak with me, in a few days time. I should have my accountant’s breakdown then. If things are as good as I hope, then we’ll go out and celebrate together. How does that sound?"
        MC "Sounds great! I’ll come back in a few days."
        MC "(Sweet! I think I’ve just scored a date with Caroline!)"

        $ CR3_AS5_can = 3

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump cloth_shop_open_label

    if CR3_AS5_can >= 6:
        scene CR3_AS5_p2 with dissolve

        MC "Hey again! Did you get your accountant’s breakdown yet?"
        Caroline "Oh yeah! And it was even better, than I hoped! The new clothes are selling faster, than guns in Texas!"
        MC "That’s quite the inappropriate metaphor."

        scene CR3_AS5_p3

        Caroline "Haha! It was the first thing to come into my head."
        Caroline "I just wanted to say, thanks for your help. I know I promised that we would celebrate together, so I’ve come up with a great idea, for both of us."
        MC "Yeah? What is it?"

        scene CR3_AS5_p4

        Caroline "Well, before I tell you, I just wanted to do - one quick thing - to show my appreciation, for all you’ve done for me."
        MC "(Oh wow! She’s getting pretty close to me now.)"
        Caroline "Seriously - that’s twice now, you’ve helped save and grow my business. I owe you - big time - for that."

        scene CR3_AS5_p5
        if persistent.incest_patch == True:
            Caroline "I couldn’t have asked for a better brother. I know I used to be, quite hard on you, when you were younger and growing up, but I wanted to let you know, that I really do care about you."
        else:
            Caroline "I couldn’t have asked for a better friend. I know I used to be, quite hard on you, when you were younger and growing up, but I wanted to let you know, that I really do care about you."
        MC "You don’t have to do anyth-"

        scene CR3_AS5_p6

        Caroline "*Mwah*"
        MC "Oh wow..."
        MC "(She just kissed me on the cheek! The deal is back on! Is has to be! Right?!)"

        scene CR3_AS5_p7

        Caroline "Haha! You’re blushing!"
        Caroline "Anyway - I wanted to let you know that I’m taking us out to celebrate."
        MC "Where are we going? Dinner? Movie?"

        scene CR3_AS5_p8

        Caroline "Ahaha... Not quite. Those are a bit too romantic, for the two of us - especially after what has happened."
        MC "Oh, so it’s not a date?"
        Caroline "No - at least, not between you and me."
        MC "Huh? I’m not following you."

        scene CR3_AS5_p9

        Caroline "We’re going to go out clubbing together. And - using my womanly intuition, I’m gonna help you find a girlfriend - or at the very least, get you laid."
        MC "(I... never saw that one coming. I guess the deal between us, really is dead then.)"
        MC "That’s... great. What about you, though? Will it not be really awkward for you, just - watching me - chat up girls?"
        Caroline "Don’t be silly - YOU’RE gonna help ME, find a boyfriend too!"
        MC "Oh... that’s... great!"
        MC "(Caroline is looking for a boyfriend? If she’s that serious about it, then the deal is definitely dead, for good. I’ll never be with her again...)"
        Caroline "Let's go at the weekend. Just let me know, a little ahead of time. And bring about $200, to spend."
        MC "G-Good! I’m looking forward to it..."
        $ CR3_weekend_event = True
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump cloth_shop_open_label

