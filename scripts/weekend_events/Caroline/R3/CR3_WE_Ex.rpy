image CR3_WE_Ex_p1 = "images/Weekend_Events/Caroline/R3/Ex/1.jpg"
image CR3_WE_Ex_p2 = "images/Weekend_Events/Caroline/R3/Ex/2.jpg"
image CR3_WE_Ex_p3 = "images/Weekend_Events/Caroline/R3/Ex/3.jpg"
image CR3_WE_Ex_p4 = "images/Weekend_Events/Caroline/R3/Ex/4.jpg"
image CR3_WE_Ex_p5 = "images/Weekend_Events/Caroline/R3/Ex/5.jpg"
image CR3_WE_Ex_p6 = "images/Weekend_Events/Caroline/R3/Ex/6.jpg"

label CR3_WE_Ex_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_WE_Ex_p1 with dissolve

    MC "(There’s Caroline’s ex at the center of the dancefloor.)"
    MC "(Jesus Christ, that guy’s perfect. Just look at his sense of fashion, his haircut, his confidence!)"
    MC "(How could I possibly compare against that?)"

    scene CR3_WE_Ex_p2

    MC "Hey there, Charles!"
    Charles "Who are you?"
    MC "I’m [player_name] - we literally just spoke, like two minutes ago."

    scene CR3_WE_Ex_p3

    Charles "Sorry kid, it’s not ringing a bell."
    MC "(Look how fit he is, as well! If Caroline had to choose between me and him - there wouldn’t be any contest!)"
    MC "*Sigh* I was sitting, right over there."

    scene CR3_WE_Ex_p4

    Charles "Listen, kid - I really don’t remember you."
    MC "(He’s either being obtuse, or simply cares so little about me, that he has genuinely forgotten who I am.)"
    if renpy.loadable("patch.rpy"):
        MC "I’m Caroline's brother!"
    else:
        MC "I’m Caroline's friend!"

    scene CR3_WE_Ex_p5

    Charles "Oh shit! What was your name, kid? Humphrey or something?"
    MC "[player_name]."
    Charles "Yeah, I knew I was close!"
    MC "(What a fucking tool...)"

    scene CR3_WE_Ex_p6

    Charles "Whoa! Hottie alert!"
    MC "What?"
    Charles "I gotta bail, kid. Catch you around! Woohoo!"
    MC "..."
    if renpy.loadable("patch.rpy"):
        MC "(My sister has dreadful taste in men.)"
    else:
        MC "(Caroline has dreadful taste in men.)"

    $ CR3_Ex = 3
    $ CR3_WE += 1

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    jump night_club_we_label