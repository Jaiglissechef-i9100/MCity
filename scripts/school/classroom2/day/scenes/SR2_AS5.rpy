image SR2_AS5_p1 = "images/school/classroom2/day/scenes/SR2_AS5/1.jpg"
image SR2_AS5_p2 = "images/school/classroom2/day/scenes/SR2_AS5/2.jpg"
image SR2_AS5_p3 = "images/school/classroom2/day/scenes/SR2_AS5/3.jpg"
image SR2_AS5_p4 = "images/school/classroom2/day/scenes/SR2_AS5/4.jpg"
image SR2_AS5_p5 = "images/school/classroom2/day/scenes/SR2_AS5/5.jpg"
image SR2_AS5_p6 = "images/school/classroom2/day/scenes/SR2_AS5/6.jpg"
image SR2_AS5_p7 = "images/school/classroom2/day/scenes/SR2_AS5/7.jpg"

label SR2_AS5_label:
    if can_SR2_AS5 == False:
        $ clickable = False
        show screen classroom2_day
        MC "I've already talked with her."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True

        scene SR2_AS5_p1 with dissolve

        Sara "Haha!"
        MC "(It’s nice to see her laughing for a change. I wonder what she’s reading.)"
        Sara "Aries… You will..."

        scene SR2_AS5_p2

        MC "Hey, Sara! What’s up?"
        Sara "Hi, [player_name]!"
        MC "What are you reading there?"
        Sara "Just some silly rubbish."

        scene SR2_AS5_p3

        MC "Let me see."
        Sara "Trust me, you won’t be interested in it."
        MC "Does that say ‘Zodiac Signs’?"

        scene SR2_AS5_p4

        Sara "Yeah, it’s all about predicting who you should matched with, based on your star sign."
        MC "I didn’t know you were into astrology and the star signs."
        Sara "It’s not so much the star sign part of things… I don’t really believe that nonsense. It’s just a silly bit of fun."
        MC "Why are you reading it then?"

        scene SR2_AS5_p5

        Sara "Honestly? It’s going to be a really clear night sky, for the next few days…"
        Sara "I kinda wanted to go stargazing with you at the town tower."
        MC "Aww, that’s so sweet. I’d love to go."

        scene SR2_AS5_p4

        Sara "It doesn’t matter. It isn’t happening anymore."
        MC "Huh? Why?"
        if persistent.incest_patch == True:
            Sara "Mom grounded me, remember? I’m not allowed to leave the house."
        else:
            Sara "Linda grounded me, remember? I’m not allowed to leave the house."

        menu:
            "How about we sneak up onto the garage roof together and watch the stars at home?":
                scene SR2_AS5_p5

                MC "How about we sneak up on the garage roof together and watch the stars tonight?"

                scene SR2_AS5_p6

                Sara "Are you serious?"
                MC "Yeah!"
                Sara "Yes! Yes! Yes! Let’s do it! I’m so excited!"

                jump SR2_AS5_continue
            "It’s okay, Sara. We’ll just have to wait until you’re not grounded anymore. We’ll watch the stars together someday.":

                scene SR2_AS5_p4

                MC "I’m sorry, Sara. We’re just going to have to wait until you’re not grounded anymore."
                MC "I promise, we’ll go to the town tower together someday to watch the stars."
                Sara "(Sigh…)"

                scene SR2_AS5_p6

                Sara "Actually, hold on! I’ve got an idea!"
                Sara "How about we climb up onto the garage roof tonight and watch the stars from there?"
                MC "Yeah! That’s a great idea!"

                jump SR2_AS5_continue

label SR2_AS5_continue:
    scene SR2_AS5_p7

    Sara "This is going to be amazing, [player_name]! I can’t wait! I’m so excited!"
    MC "Where do you want to meet?"
    if persistent.incest_patch == True:
        Sara "I’ll sneak out of my bedroom after Mom goes to sleep. Then we’ll meet up at the garage?"
    else:
        Sara "I’ll sneak out of my bedroom after Linda goes to sleep. Then we’ll meet up at the garage?"
    MC "Sounds great! I’ll see you there tonight."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    $ can_SR2_AS5 = False
    $ SR2_NS3 = True
    $ S_N_inbed = False
    jump classroom2_morning1
