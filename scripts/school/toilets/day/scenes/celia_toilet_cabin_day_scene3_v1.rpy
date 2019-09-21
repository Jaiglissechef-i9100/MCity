image celia_toilet_cabin_day_scene3_v1_p1 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/1.jpg"
image celia_toilet_cabin_day_scene3_v1_p2 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/2.jpg"
image celia_toilet_cabin_day_scene3_v1_p3 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/3.jpg"
image celia_toilet_cabin_day_scene3_v1_p4 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/4.jpg"
image celia_toilet_cabin_day_scene3_v1_p5 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/5.jpg"
image celia_toilet_cabin_day_scene3_v1_p6 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/6.jpg"
image celia_toilet_cabin_day_scene3_v1_p7 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/7.jpg"
image celia_toilet_cabin_day_scene3_v1_p8 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/8.jpg"
image celia_toilet_cabin_day_scene3_v1_p9 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/9.jpg"
image celia_toilet_cabin_day_scene3_v1_p10 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/10.jpg"
image celia_toilet_cabin_day_scene3_v1_p11 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/11.jpg"
image celia_toilet_cabin_day_scene3_v1_p12 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/12.jpg"
image celia_toilet_cabin_day_scene3_v1_p13 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/13.jpg"
image celia_toilet_cabin_day_scene3_v1_p14 = "images/school/toilets/day/scenes/celia_toilet_cabin_day_scene3_v1/14.jpg"

label celia_toilet_cabin_day_scene3_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)

    scene celia_toilet_cabin_day_scene3_v1_p1
    $ can_hide_windows = True
    Celia "(There he is…)"
    Celia "(God… I can’t believe I have to go through with this.)"
    Celia "(Sigh...)"

    scene celia_toilet_cabin_day_scene3_v1_p2
    Celia "[player_name]?"
    MC "(Mwahaha! She came, after all!)"
    MC "Huh?! M-Mrs. Celia?! What are you doing in here?"

    scene celia_toilet_cabin_day_scene3_v1_p3
    MC "This is the men’s bathroom! I think you’ve got the wrong room!"
    Celia "That’s… not what I’m here for."
    MC "What do you mean?"

    scene celia_toilet_cabin_day_scene3_v1_p4
    MC "(Wow… she pushed me up against the stall wall.)"
    MC "What are YOU doing?"
    Celia "Just… shut up."

    scene celia_toilet_cabin_day_scene3_v1_p5
    MC "What’s going on? Are you-"
    Celia "I’m going to kiss you. And you’re not going to tell anyone. Do you understand?"
    MC "But I thought you hated me?"
    Celia "Just shut up and let it happen."

    scene celia_toilet_cabin_day_scene3_v1_p6
    MC "(Mwahahaha! As long as I keep playing innocent, she doesn’t know who to believe or how to react!)"
    MC "(Now that I know she’s willing to kiss me, perhaps I can push her to do naughtier things in the future?)"

    scene celia_toilet_cabin_day_scene3_v1_p7
    Celia "Mmm…"
    MC "Mmm!"
    Celia "(God… I can’t believe I’m being blackmailed into kissing this creep.)"

    scene celia_toilet_cabin_day_scene3_v1_p8
    Celia "(When I find the bastard who has that picture, I’ll break his fucking legs!)"
    Celia "(This has to be one of the most humiliating experiences of my life! It’s even worse than that lesbian hazing at my sorority house!)"
    MC "Mmm!"

    scene celia_toilet_cabin_day_scene3_v1_p9
    MC "(She’s properly kissing me - tongue and everything!)"
    MC "(And she doesn’t seem to mind me putting my hands on her ass!)"
    MC "(Let’s see how she reacts if I pull her skirt up.)"

    scene celia_toilet_cabin_day_scene3_v1_p10
    Celia "(Gah! This little pervert is lifting my skirt. But if I try to stop him, I might cause that blackmailing bastard to release the picture.)"
    Celia "(I’ll just have to endure it for a while.)"

    scene celia_toilet_cabin_day_scene3_v1_p11
    Celia "(Okay, this has been going on long enough. I’ve done MORE than what was requested of me.)"
    Celia "(I just hope that creep considers this make-out session enough…)"

    scene celia_toilet_cabin_day_scene3_v1_p12
    MC "W-Wow! Wh-What was that for, Mrs. Celia?"
    Celia "Shut up."
    MC "Huh?"
    Celia "Don’t say a word to anyone about this."
    MC "I’m confused."

    scene celia_toilet_cabin_day_scene3_v1_p13
    Celia "This is our little secret."
    MC "R-Really? Will it be happening again?"
    Celia "(I fucking hope not!)"
    Celia "…"

    scene celia_toilet_cabin_day_scene3_v1_p14
    MC "(Mwahahah! It worked! Her kissing technique is amazing!)"
    MC "(Now I can try, pushing her to go further!)"
    $ unlock_celia_toilet_cabin_day_scene3_v1 = 3
    $ can_unlock_celia_toilet_cabin_day_scene3_v1 = 3
    $ can_unlock_celia_toilet_cabin_day_scene4_v1 = 1
    $ talking_celia_school_morning_scene1v1 = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump toilets_day1
