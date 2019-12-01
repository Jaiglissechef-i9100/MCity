image MLR2_NS1_p1 = "images/home/salon/night/scenes/MLR2_NS1/1.jpg"
image MLR2_NS1_p2 = "images/home/salon/night/scenes/MLR2_NS1/2.jpg"
image MLR2_NS1_p3 = "images/home/salon/night/scenes/MLR2_NS1/3.jpg"
image MLR2_NS1_p4 = "images/home/salon/night/scenes/MLR2_NS1/4.jpg"
image MLR2_NS1_p5 = "images/home/salon/night/scenes/MLR2_NS1/5.jpg"
image MLR2_NS1_p6 = "images/home/salon/night/scenes/MLR2_NS1/6.jpg"
image MLR2_NS1_p7 = "images/home/salon/night/scenes/MLR2_NS1/7.jpg"
image MLR2_NS1_p8 = "images/home/salon/night/scenes/MLR2_NS1/8.jpg"

image MLR2_NS1_p1a = "images/home/salon/night/scenes/MLR2_NS1/1a.jpg"
image MLR2_NS1_p2a = "images/home/salon/night/scenes/MLR2_NS1/2a.jpg"

default MLR2_NS1_counter = 1

label MLR2_NS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ Linda_name = Mom_name
    if persistent.incest_patch == True:
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"
    if ml_points == 3 and MLR3_NS1 == 3 and MLR2_Sleep == True:
        jump MLR3_NS1
    if ml_points >= 3 and MLR2_Sleep == True and ML_NSB_sleep_can == True:
        jump ML_NS_sleep_label
    $ can_hide_windows = True
    if MLR2_NS2 == True and MLR2_Sleep == True:
        jump MLR2_NS2_label
    if MLR2_NS1_counter == 2 and MLR2_Sleep == True:
        scene MLR2_NS1_p1 with dissolve
        MC "I wonder what they're doing."
        MC "It's very quiet there today."
        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"
        scene MLR2_NS1_p2a
        MC "Hmm.. They're sleeping..."
        MC "I should leave. I don't want to wake up them."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1

    if MLR2_NS1_counter <= 2 and MLR2_Sleep == False:
        scene MLR2_NS1_p1 with dissolve
        MC "I wonder what they're doing."
        MC "It's very quiet there today."
        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"
        scene MLR2_NS1_p1a
        if persistent.incest_patch == True:
            MC "Ah! It's only Dad."
        else:
            MC "Ah! It's only Bob."
        if persistent.incest_patch == True:
            MC "I forgot! Mom is waiting for me in my bedroom!"
        else:
            MC "I forgot! Lnda is waiting for me in my bedroom!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1

    if MLR2_NS1_counter == 1 and MLR2_Sleep == True:
        scene MLR2_NS1_p1 with dissolve
        if persistent.incest_patch == True:
            $ Dad_name = __("Dad")
        else:
            $ Dad_name = "Bob"
        if persistent.incest_patch == True:
            MC "(I think I can hear Mom having sex. It’s fairly faint though.)"
        else:
            MC "(I think I can hear Linda having sex. It’s fairly faint though.)"
        MC "(I could risk opening the door to check.)"

        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"

        Mom "Ohh… Ah… Ahhh…"
        MC "(Yeah, she’s definitely having sex right now!)"

        scene MLR2_NS1_p3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

        Mom "AH! Ahhh! Ahhh!"
        Dad "Ugh! That’s it! I’m glad you’re enjoying this, for a change!"
        if persistent.incest_patch == True:
            MC "(For a change? Mom mustn’t enjoy sex with Dad, that much.)"
        else:
            MC "(For a change? Linda mustn’t enjoy sex with Bob that much.)"

        scene MLR2_NS1_p4

        Mom "Ah! Ah! Yes!"
        MC "(I wonder if she’s faking it?)"
        Mom "Harder! Faster!"
        Dad "I’m going as fast as I can right now!"
        Mom "Fuck me harder, [player_name]!"
        MC "…"
        MC "(Oh shit!)"

        scene MLR2_NS1_p5

        Dad "Wait… what?"
        Dad "Did you just call me [player_name]?"
        if persistent.incest_patch == True:
            MC "(Oh fuck… if he finds out that I’ve done stuff with Mom, he’ll kill me!)"
        else:
            MC "(Oh fuck… if he finds out that I’ve done stuff with Linda, he’ll kill me!)"
        scene MLR2_NS1_p6

        Mom "Ugh! Why did you stop?"
        Dad "You just said-"
        Mom "God! You’re useless! I’m going to sleep now! Goodnight!"
        Dad "B-But I haven’t cum yet."

        scene MLR2_NS1_p7

        Mom "It’s late, and I have work to do tomorrow."
        Dad "But-"
        Mom "Go and watch some porn."
        Dad "(Sigh…)"

        scene MLR2_NS1_p8

        Dad "(I could have sworn she called me [player_name])."
        if persistent.incest_patch == True:
            Dad "(Why the heck would she be thinking about our son when we’re having sex?)"
        else:
            Dad "(Why the heck would she be thinking about [player_name] when we’re having sex?)"
        Dad "(And why has she been so grumpy lately?)"
        Dad "(Ah well, time to boot up the laptop and search for some good old femdom hentai!)"
        $ MLR2_MS1_NS1 = True
        $ MLR2_NS1_counter = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1
