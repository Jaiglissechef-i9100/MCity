image SR3_MS1_p1 = "images/v71/2_WE/6_Home_End/penetrate/MS1/1.jpg"
image SR3_MS1_p2 = "images/v71/2_WE/6_Home_End/penetrate/MS1/2.jpg"
image SR3_MS1_p3 = "images/v71/2_WE/6_Home_End/penetrate/MS1/3.jpg"
image SR3_MS1_p4 = "images/v71/2_WE/6_Home_End/penetrate/MS1/4.jpg"
image SR3_MS1_p5 = "images/v71/2_WE/6_Home_End/penetrate/MS1/5.jpg"
image SR3_MS1_p6 = "images/v71/2_WE/6_Home_End/penetrate/MS1/6.jpg"
image SR3_MS1_p7 = "images/v71/2_WE/6_Home_End/penetrate/MS1/7.jpg"
image SR3_MS1_p8 = "images/v71/2_WE/6_Home_End/penetrate/MS1/8.jpg"
image SR3_MS1_p9 = "images/v71/2_WE/6_Home_End/penetrate/MS1/9.jpg"

label SR3_MS1:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene SR3_MS1_p1
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*Knock Knock*"
    $ renpy.music.stop(channel="sound")
    MC "Hey, Sara, I just wanted to check how you were doing."
    scene SR3_MS1_p2
    MC "(Is that a photo of Lily on the wall? What on Earth is she doing?)"
    MC "Umm… Sara?"
    scene SR3_MS1_p3
    Sara "She’s not gonna do it."
    MC "Pardon?"
    Sara "She’s NOT going to do it!"
    scene SR3_MS1_p4
    MC "Sara, what are you talking about?"
    Sara "She wants to take you from me! She wants you just for herself! I saw it that day when we played spin the bottle in my bedroom."

    if SR3_romantic_route == True:

        Sara "I saw the way she kissed you in my bedroom!"
        scene SR3_MS1_p5
        MC "Sara… I think you need to take a step back and take a deep breath."
        Sara "And you… you said ‘yes’ to going on a date with me. You built my hopes up!"
        Sara "You made me believe that I was the only one for you!"
        scene SR3_MS1_p6
        MC "Sara, you are! I had NOTHING to do with what Lily is trying to do right now!"
        Sara "I gave up my virginity for you! *Sob*"
        Sara "Lily was ALWAYS on your mind, wasn’t she?! *Sob*"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)
        MC "Sara, that’s not-"
    else:


        Sara "I saw the way she kissed you."
        scene SR3_MS1_p5
        MC "Sara… I think you need to take a step back and take a deep breath."
        Sara "I should have KNOWN that you had your eyes on someone else, [player_name]."
        Sara "You were the one who wanted our date to be a big secret!"
        scene SR3_MS1_p6
        if renpy.loadable("patch.rpy"):
            MC "Sara, I was ONLY worried about people noticing us as brother and sister!"
        else:
            MC "Sara, I was ONLY worried about people noticing us dating!"
        Sara "You’re… a fucking liar! It was Lily, wasn’t it?!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)
        Sara "It’s ALWAYS been Lily!"

    scene SR3_MS1_p7
    Sara "AAAHHHHH!!!"
    Sara "FUCKING BITCH! She’s trying to ruin my life!"
    scene SR3_MS1_p8
    MC "Jesus Christ… "
    MC "(I need to back off until she cools down. Maybe I should speak with [Mom_name] or Caroline or someone?)"
    scene SR3_MS1_p9
    Sara "Fuck you, Lily! FUCK YOU!"
    MC "*Gulp*"
    Sara "YOU MAN STEALING WHORE! I HATE YOU!"
    show workinprogress2
    "This is the end of current content in this version for this character."
    hide workinprogress2
    $ renpy.pause(3.0, hard=True)
    $ day_time = 2
    $ SR3_MS1 = False
    $ SR3_v71_end = True
    $ SR3_rep_v71 = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump corridor_day1