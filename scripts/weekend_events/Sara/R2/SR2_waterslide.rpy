image SR2_weekend_waterslide_p1 = "images/Weekend_Events/Sara/R2/WaterSlide/1.jpg"
image SR2_weekend_waterslide_p2 = "images/Weekend_Events/Sara/R2/WaterSlide/2.jpg"
image SR2_weekend_waterslide_p3a = "images/Weekend_Events/Sara/R2/WaterSlide/3a.jpg"
image SR2_weekend_waterslide_p3aa = "images/Weekend_Events/Sara/R2/WaterSlide/3aa.jpg"
image SR2_weekend_waterslide_p3b = "images/Weekend_Events/Sara/R2/WaterSlide/3b.jpg"
image SR2_weekend_waterslide_p3bb = "images/Weekend_Events/Sara/R2/WaterSlide/3bb.jpg"
image SR2_weekend_waterslide_p4 = "images/Weekend_Events/Sara/R2/WaterSlide/4.jpg"
image SR2_weekend_waterslide_p5 = "images/Weekend_Events/Sara/R2/WaterSlide/5.jpg"
image SR2_weekend_waterslide_p6 = "images/Weekend_Events/Sara/R2/WaterSlide/6.jpg"
image SR2_weekend_waterslide_p7 = "images/Weekend_Events/Sara/R2/WaterSlide/7.jpg"
image SR2_weekend_waterslide_p8 = "images/Weekend_Events/Sara/R2/WaterSlide/8.jpg"
image SR2_weekend_waterslide_p9 = "images/Weekend_Events/Sara/R2/WaterSlide/9.jpg"
image SR2_weekend_waterslide_p10 = "images/Weekend_Events/Sara/R2/WaterSlide/10.jpg"
image SR2_weekend_waterslide_p11 = "images/Weekend_Events/Sara/R2/WaterSlide/11.jpg"
image SR2_weekend_waterslide_p12 = "images/Weekend_Events/Sara/R2/WaterSlide/12.jpg"
image SR2_weekend_waterslide_p13 = "images/Weekend_Events/Sara/R2/WaterSlide/13.jpg"
image SR2_weekend_waterslide_p14 = "images/Weekend_Events/Sara/R2/WaterSlide/14.jpg"

label SR2_waterslide_label:
    if SR2_after_waterslide == True:
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
        MC "How about we try out the waterslides?"
        Sara "Eh… I don’t know… I can’t swim very well."
        MC "Relax. We’ll go down it together, and I’ll hold you when we go into the pool, okay?"
        Sara "Promise?"
        MC "I promise."
        Sara "(Gulp) I… I guess so, then…"

        scene SR2_weekend_waterslide_p1

        MC "Here we go. Do you want to climb up first?"
        Sara "It’s really high…"
        MC "I can be right behind you."
        Sara "And you’ll definitely hold onto me when we get into the water?"
        window hide
        scene SR2_weekend_waterslide_p2
        menu:
            "Offer to climb up first.":

                MC "Would you prefer it if I climbed up first?"
                Sara "Honestly? Yeah."
                MC "No problem. I’ll start climbing the ladder now."

                scene SR2_weekend_waterslide_p3b

                MC "See? It’s perfectly safe."
                MC "You aren’t scared of heights as well, are ya?"
                Sara "Only when the heights are over water."

                scene SR2_weekend_waterslide_p3bb

                MC "Like I said - I’ll be here and I’ll hold onto you once we get into the pool."
                Sara "(Wow… Those shorts are so tight on him. I can almost see the outline of his junk.)"
                MC "Is that okay, Sara?"
                Sara "Huh?"
                MC "I said, I’ll hold onto you when we get into the pool."
                Sara "Oh yeah! That’s okay."
                jump SR2_after_waterslide_menu
            "Tell Sara to start climbing, and that you’ll be right behind her.":

                MC "Go ahead - start climbing. I’ll be right behind you, to catch you if you fall."

                scene SR2_weekend_waterslide_p3a

                Sara "Thanks, [player_name]."
                Sara "I’ve been here so many times with friends, but I’ve never actually been in the deep part of the pool."
                Sara "And I’ve definitely NEVER been on these slides before."
                MC "There’s a first time for everything."

                scene SR2_weekend_waterslide_p3aa

                MC "(Damn, she’s got a cute little ass.)"
                MC "(I’d love to squeeze and grope those asscheeks!)"
                Sara "I hope you’re not staring at my ass! Haha!"
                MC "Err… nope!"
                jump SR2_after_waterslide_menu

label SR2_after_waterslide_menu:
    scene SR2_weekend_waterslide_p4

    MC "Okay, here we are. You’re holding onto my arm pretty tightly. Are you feeling okay?"
    Sara "J-Just a little n-n-nauseous."
    MC "Try to relax. Take some deep breaths."

    scene SR2_weekend_waterslide_p5

    MC "You’re going to be fine. This isn’t a very deep pool, and you’re with one of the best swimmers in the world."
    Sara "YOU are one of the best swimmers in the world?!"
    MC "Of course I am! Haven’t you heard of [player_name] the fish?"
    Sara "Hahaha!"
    MC "(I’ve got her laughing. Hopefully that takes her mind off her fears.)"

    scene SR2_weekend_waterslide_p6

    MC "Just hold my hand and we’ll get into a position you feel safe with."
    Sara "Umm… Am I too heavy to sit on your knee?"
    MC "Of course not. You’re light as a feather."

    scene SR2_weekend_waterslide_p7

    MC "See? You fit on my knee perfectly."
    Sara "Hehe…"
    Sara "(I love the feeling of his warm hands wrapped around my belly.)"
    Sara "(I just wish I could cuddle him like that every night.)"
    MC "Ready to go?"

    scene SR2_weekend_waterslide_p8

    Sara "Yup!"
    MC "I’ll hold on tight - don’t worry!"
    Sara "(Huh? What’s that hard thing poking at my ass?)"

    scene SR2_weekend_waterslide_p9

    MC "Wooo!"
    Sara "Woo-oooohhh!"
    Sara "(Oh my God! He’s got a boner again! It’s pressing into my vulva!)"
    MC "(Sounds like she’s enjoying this, waaaay more than I am!)"

    scene SR2_weekend_waterslide_p10

    MC "(Hopefully she hasn’t noticed my hard on.)"
    MC "(I haven’t been able to shift it since I first saw her in her tight pink swimsuit.)"
    Sara "Gulp!"
    Sara "The water! Don’t let gooo!"

    scene SR2_weekend_waterslide_p11

    "SPLASH!"
    Sara "Ahh! Cold!"
    MC "There we go! That’s your first time sliding into the pool!"
    Sara "Don’t let go! Don’t let go!"
    MC "Relax! This is the shallow end! You can probably touch the bottom with your toes."
    Sara "Huh?"

    scene SR2_weekend_waterslide_p12

    MC "See? Your nose is still above water."
    Sara "(Thank God… That was scary.)"
    Sara "(I should probably confront [player_name] about his boner…)"

    scene SR2_weekend_waterslide_p14
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    Sara "Umm… going down the slide, I felt something hard."
    MC "(Uh oh…)"
    Sara "[player_name]… did you have an erection?"

    scene SR2_weekend_waterslide_p13

    MC "Yeah… and I still do."
    Sara "Is it because… because..."
    MC "Because I’m with you?"
    Sara "Yeah?"
    MC "Yeah, it is."

    scene SR2_weekend_waterslide_p14

    Sara "But I’m not even naked…"
    MC "You’re still gorgeous. Whenever I see something really sexy, my cock decides to go hard. I have no control over it."
    MC "It’s basically got a mind of its own."
    Sara "Huh?! Is that how penises really work? Or are you just shitting me?"
    MC "No, it’s true. Guys can’t really control when they get an erection."
    Sara "Huh… That’s really strange."
    MC "Is it? Can you control when you get wet?"

    scene SR2_weekend_waterslide_p12

    Sara "[player_name]…."
    MC "Haha! You’re adorable when you get shy."
    MC "Alright, let’s head out of the pool now."
    $ SR2_after_waterslide = True
    $ can_hide_windows = False
    jump swimming_poll_label

