image CeR2_del_data_p1 = "images/CeR2/Monitoring/Deleting Data/1.jpg"
image CeR2_del_data_p2 = "images/CeR2/Monitoring/Deleting Data/2.jpg"
image CeR2_del_data_p3 = "images/CeR2/Monitoring/Deleting Data/3.jpg"
image CeR2_del_data_p4 = "images/CeR2/Monitoring/Deleting Data/4.jpg"
image CeR2_del_data_p5 = "images/CeR2/Monitoring/Deleting Data/5.jpg"
image CeR2_del_data_p6 = "images/CeR2/Monitoring/Deleting Data/6.jpg"
image CeR2_del_data_p7 = "images/CeR2/Monitoring/Deleting Data/7.jpg"
image CeR2_del_data_p8 = "images/CeR2/Monitoring/Deleting Data/8.jpg"
image CeR2_del_data_p9 = "images/CeR2/Monitoring/Deleting Data/9.jpg"
image CeR2_del_data_p10 = "images/CeR2/Monitoring/Deleting Data/10.jpg"
image CeR2_del_data_p11 = "images/CeR2/Monitoring/Deleting Data/11.jpg"

label CeR2_del_data:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CeR2_del_data_p1 with dissolve
    Celia "So… why is it they call you Big Jake?"
    B_J "I used to get bullied as a kid, I just sorta adopted it. *Wheeze* Made it my own."
    Celia "Oh… so it’s not because you have a massive cock?"

    scene CeR2_del_data_p2
    B_J "No! I mean, yes! *Wheeze* I… um!"
    MC "(Nicely done, Celia!)"
    B_J "I mean, when I say ‘no’ it’s not like it’s below average or anything. *Wheeze*"

    scene CeR2_del_data_p3
    "*Click*"
    MC "(And I’m in!)"
    Celia "Whoa, haha! Calm down! You’re going to have a heart attack on me, buddy. I was just flirting with you."

    scene CeR2_del_data_p4
    MC "(Bingo. Now, let’s try and find the video tapes. Once I get them deleted, I’ll be home free.)"
    MC "(Hmm, where to begin…)"

    scene CeR2_del_data_p5
    MC "(Okay… I guess the keyboard is as good a place to start as any.)"
    MC "(Let’s start searching for any security footage relating to the bathrooms.)"

    scene CeR2_del_data_p6
    "*Clack clack*"
    MC "Hmm…"
    MC "(Zero results? Dammit. I bet, that Big Jake doesn’t even know how to work this thing himself.)"

    scene CeR2_del_data_p7
    MC "(Let’s try searching for camera numbers…)"
    "*Clack Clack*"
    MC "(Nothing?! Fuck. I hope Celia can keep him occupied out there!)"

    scene CeR2_del_data_p8
    MC "(Think, [player_name], think! How can you handle this?!)"
    MC "Aha!"
    MC "(I’ll just wipe everything! No files, no problem!)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)

    scene CeR2_del_data_p9
    MC "(Hehe, you are one smart cookie!)"
    "*Clack Clack*"
    MC "(And… here we… go!)"
    MC "(All files deleted.)"

    scene CeR2_del_data_p10
    MC "(Good, now it’s guaranteed that I won’t be caught on camera.)"
    MC "(This couldn’t have panned out any better!)"
    MC "(It seems like Celia did a good job keeping Big Jake distracted. Hopefully he doesn’t develop an infatuation for her. That’d be awkward…)"

    scene CeR2_del_data_p11
    B_J "And that *Wheeze* is why smaller dicks can actually result in a more pleasurable experience for a woman."
    Celia "Okay, I better go back to class."
    B_J "Stop by *Wheeze* anytime - I still have to show you my extensive collection of hentai. We’ll do a binge *Wheeze* of Super Happy Tentacle Monster One to Twelve!"
    Celia "There’s… twelve movies in your hentai series."
    B_J "The lore is surprisingly deep."
    Celia "Uh huh…I’m sure it is. I can barely contain my excitement."

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ CeR2_moni = 6
    $ can_hide_windows = False
    $ CeR2_MS1_talk = False
    $ CeR2_MS1 = True
    jump school_corridor2_morning1