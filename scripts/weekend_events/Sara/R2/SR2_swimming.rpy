image SR2_weekend_swimming_p1 = "images/Weekend_Events/Sara/R2/Swimming/1.jpg"
image SR2_weekend_swimming_p2 = "images/Weekend_Events/Sara/R2/Swimming/2.jpg"
image SR2_weekend_swimming_p3 = "images/Weekend_Events/Sara/R2/Swimming/3.jpg"
image SR2_weekend_swimming_p4 = "images/Weekend_Events/Sara/R2/Swimming/4.jpg"
image SR2_weekend_swimming_p5 = "images/Weekend_Events/Sara/R2/Swimming/5.jpg"
image SR2_weekend_swimming_p6 = "images/Weekend_Events/Sara/R2/Swimming/6.jpg"
image SR2_weekend_swimming_p7 = "images/Weekend_Events/Sara/R2/Swimming/7.jpg"

label SR2_swimming_label:
    if SR2_after_swimming == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "We've already been there."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)

        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "How about, I go swimming, and you can sit, safely in the pink flamingo toy?"
        Sara "Hmm… I don’t know. It’s pretty scary."
        MC "Relax - I’ll stay beside you the whole time, to make sure you don’t fall off."
        Sara "Err… Okay then."

        scene SR2_weekend_swimming_p1

        MC "See? Nothing to worry about."
        Sara "I… I guess so..."
        MC "You still look a little nervous."
        Sara "Yeah, I’m a bit scared of the water."

        scene SR2_weekend_swimming_p2

        MC "Oh, so it would be really scary if the float started to tip over?"
        Sara "NO! Don’t you dare!"
        MC "Uh oh! Mayday! Mayday! We’re going down!"
        Sara "STOP THAT, [player_name]!"

        scene SR2_weekend_swimming_p3

        Sara "AAAHHHH!"
        MC "This is the USS Pink Flamingo. We have taken on water and are sinking!"
        Sara "STOP! STOP! NOOOO!"
        MC "Hahahahaha!"

        scene SR2_weekend_swimming_p4

        Sara "Grrr! That’s NOT funny, [player_name]!"
        Sara "I could have LITERALLY drowned!"
        MC "The pool is like six feet deep!"
        Sara "And I’m only five foot four on a GOOD day!"
        MC "Alright. I’m sorry, Sara. I won’t do it again."
        Sara "You better not."
        MC "Huh?"
        Sara "I said, you better not do it again!"
        MC "I can’t hear you. It’s too loud in here now. Can you lean in closer?"

        scene SR2_weekend_swimming_p5

        MC "(Hehe. She fell for it!)"
        Sara "I said, you better not try and tip the float aga-"

        scene SR2_weekend_swimming_p6

        Sara "Mmpff!"
        MC "Mwah…"
        Sara "(Bastard! He tricked me!)"
        MC "Hehe. Gotcha!"

        scene SR2_weekend_swimming_p7
        if persistent.incest_patch == True:
            Sara "Bro…"
            MC "Maybe don’t call me ‘Bro’ too loudly. We are in a public place, after all."
        else:
            Sara "[player_name]…"
        Sara "Hehe... Oh yeah."
        MC "Still angry at me?"
        Sara "No. Apology accepted. Just… don’t do it again, okay?"
        MC "Okay."

        scene SR2_weekend_swimming_p6

        MC "Mwah!"
        Sara "(OH MY GOD! AGAIN?!)"

        scene SR2_weekend_swimming_p7

        MC "Haha! Sorry! I couldn’t resist. I love that cute, shocked expression you get, every time I kiss you."
        Sara "Hehe… You’re bad, you know that?"
        MC "I know."
        Sara "Haha! Okay, let’s call it a day."
        $ SR2_after_swimming = True
        $ can_hide_windows = False
        jump swimming_poll_label
