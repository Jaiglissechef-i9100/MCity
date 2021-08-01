image CR3_WE_G1_p1 = "images/Weekend_Events/Caroline/R3/Girl1/1.jpg"
image CR3_WE_G1_p2 = "images/Weekend_Events/Caroline/R3/Girl1/2.jpg"
image CR3_WE_G1_p3 = "images/Weekend_Events/Caroline/R3/Girl1/3.jpg"
image CR3_WE_G1_p4 = "images/Weekend_Events/Caroline/R3/Girl1/4.jpg"
image CR3_WE_G1_p5 = "images/Weekend_Events/Caroline/R3/Girl1/5.jpg"
image CR3_WE_G1_p6 = "images/Weekend_Events/Caroline/R3/Girl1/6.jpg"
image CR3_WE_G1_p7 = "images/Weekend_Events/Caroline/R3/Girl1/7.jpg"

label CR3_WE_G1_label:

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_WE_G1_p1 with dissolve

    MC "(Oh yeah! She looks perfect! I’ll try my luck with her now!)"
    MC "(I think this is the first time in my life, I’ve seen denim shorts THAT small! They may as well be - denim panties!)"

    scene CR3_WE_G1_p2

    $ Juliett_name = "???"

    MC "Hey there. I’m [player_name]. Nice to meet you."
    Juliett "Hi, I’m Juliett. What brings you out tonight?"

    $ Juliett_name = "Juliett"
    if persistent.incest_patch == True:
        MC "I’m out, celebrating with my sister."
    else:
        MC "I’m out, celebrating with my roomate."

    scene CR3_WE_G1_p3

    Juliett "That’s cool. Is it a birthday or something?"
    MC "Nah, she runs her own business - and finally started making a profit."
    Juliett "Awesome! Congrats to her."

    scene CR3_WE_G1_p4

    MC "Say, would you fancy joining me for a few drinks?"
    Juliett "Eh... not really. I’m not gonna be here, much longer tonight."
    MC "Aww c’mon - just one drink!"

    scene CR3_WE_G1_p5

    Juliett "Perhaps you didn’t hear me properly, over the loud music - I said I’m heading out soon."
    MC "Yeah, but-"

    scene CR3_WE_G1_p6

    Juliett "Listen - maybe another time, if I see you here again. But right now, I’m not interested, and don’t have a whole lotta free time. Capiche?"
    MC "*Sigh* Yeah, I got it."

    scene CR3_WE_G1_p7

    Juliett "Hey - keep your chin up. I didn’t say ‘no’ - just not tonight."
    Juliett "See you around, [player_name]."

    $ CR3_G1 = 3
    $ CR3_WE += 1

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump night_club_we_label

