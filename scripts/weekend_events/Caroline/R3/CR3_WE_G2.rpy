image CR3_WE_G2_p1 = "images/Weekend_Events/Caroline/R3/Girl2/1.jpg"
image CR3_WE_G2_p2 = "images/Weekend_Events/Caroline/R3/Girl2/2.jpg"
image CR3_WE_G2_p3 = "images/Weekend_Events/Caroline/R3/Girl2/3.jpg"
image CR3_WE_G2_p4 = "images/Weekend_Events/Caroline/R3/Girl2/4.jpg"
image CR3_WE_G2_p5 = "images/Weekend_Events/Caroline/R3/Girl2/5.jpg"

label CR3_WE_G2_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_WE_G2_p1 with dissolve

    MC "(Oh wow! She’s pretty damn sexy! I reckon I should ask her out!)"
    MC "(Her breasts look fucking amazing!)"

    scene CR3_WE_G2_p2

    MC "(Okay, let’s open this with a - totally original - chat up line, that she’s never heard before, in her life!)"
    MC "(Hmm... Aha! Got one!)"
    MC "Hey there - are you superglue? Because my eyes are stuck to you."

    scene CR3_WE_G2_p3

    Woman "Did you just make that line up, there, now?"
    MC "Yeah, I did!"
    Woman "I can tell - just because it’s orignal, doesn’t stop it being shit."
    MC "(Ouch! I’ll try again!)"
    MC "I’m [player_name] - it’s nice to meet you."
    Woman "Yeah, you’re about - twenty shades paler - than the guys I usually fuck. I ain’t spending my weekend with some, tiny-dicked white dude."

    scene CR3_WE_G2_p4

    MC "Huh?! What? You haven’t even seen my-"
    Woman "Bubye, honey."
    MC "I, uh..."

    scene CR3_WE_G2_p5

    Woman "I said, goodbye. That means, you can walk away now and leave me alone."
    MC "*Sigh* Fine..."
    MC "(Yeah, there was no way I stood a chance with her. I’m not her type, at all!)"

    $ CR3_G2 = False
    $ CR3_WE += 1

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    jump night_club_we_label
