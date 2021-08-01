image ml_ml_and_f_bedroom_night_scene1_v1_p1 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/1.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p2 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/2.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p3 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/3.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p4 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/4.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p5 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/5.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p6 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/6.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p7 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/7.jpg"

image ml_ml_and_f_bedroom_night_scene2_v1_p1 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/1.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p2 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/2.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p3 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/3.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p4 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/4.jpg"

screen ml_ml_and_f_bedroom_night_scene_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_ml_and_f_bedroom_night_scene_v1_screen"),Jump("salon_night1")]

label ml_ml_and_f_bedroom_night_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if ml_ml_and_f_bedroom_night_visit_scene_v1 == 1 and ml_can_ml_and_f_bedroom_night_scene_v1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        scene ml_ml_and_f_bedroom_night_scene1_v1_p1 with dissolve
        $ Dad_name = "???"
        Dad "(Ugh! Yeah!)"

        if renpy.loadable("patch.rpy"):
            MC "(Huh… Sounds like my parents are having sex.)"
            MC "(Maybe I could take this chance to sneak a peek at Mom!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Huh… Sounds like Linda and Bob are having sex.)"
            MC "(Maybe I could take this chance to sneak a peek at Linda!)"
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        scene ml_ml_and_f_bedroom_night_scene1_v1_p2
        MC "(Shit… I hope they didn’t hear the door opening!)"
        Dad "Oh! Ahhh!"
        MC "(Apparently not!)"
        if renpy.loadable("patch.rpy"):
            $ Dad_name = "Dad"
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Bob"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p3
        Dad "Oh yeah, that’s it!"
        Dad "Aww, crap..."
        if renpy.loadable("patch.rpy"):
            MC "(Huh, it’s only Dad moaning.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Huh, it’s only Bob moaning.)"
        Dad "Hang on, I’ll get my boner back. Just give me a minute and I’ll go in again!"
        Mom "Uh huh… No problem, Dear."

        scene ml_ml_and_f_bedroom_night_scene1_v1_p4
        if renpy.loadable("patch.rpy"):
            MC "(It looks like Mom’s… bored?)"
        if not renpy.loadable("patch.rpy"):
            MC "(It looks like Linda’s… bored?)"
        MC "(No way! Why would she be bored having sex?!)"
        MC "(It doesn’t make sense…)"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p5

        if renpy.loadable("patch.rpy"):
            MC "(Looks like Mom is more interested in her book. I wonder what it is?)"
            MC "(Dad probably doesn’t even know or care right now.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Looks like Linda is more interested in her book. I wonder what it is?)"
            MC "(Bob probably doesn’t even know or care right now.)"
        scene ml_ml_and_f_bedroom_night_scene1_v1_p6
        Dad "Ahhh! Oh yeah, that’s it! Ugh!"
        Dad "You feeling this, Honey?"
        Mom "Mmm hmm... "
        Mom "(Yawn!)"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p7
        MC "(That must be one, damn good book, if she’s managing to read it in the middle of sex!)"
        MC "(I should check out what it is, later on.)"
        MC "(Anyway, I better sneak away now, before I get caught!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_ml_and_f_bedroom_night_scene_v1 = False
        $ ml_ml_and_f_bedroom_night_visit_scene_v1 = 2
        $ ml_bedroom_book_scene = True
        $ can_hide_windows = False
        jump salon_night1
    if ml_ml_and_f_bedroom_night_visit_scene_v1 == 2 and ml_can_ml_and_f_bedroom_night_scene_v1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        scene ml_ml_and_f_bedroom_night_scene2_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "(I wonder if Mom’s gonna be reading again.)"
        if not renpy.loadable("patch.rpy"):
            MC "(I wonder if Linda’s gonna be reading again.)"
        MC "(At the very least, I’ll get a good peek at her tits!)"
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        scene ml_ml_and_f_bedroom_night_scene2_v1_p2
        MC "(Damn! Fuck this door! Someone needs to oil those hinges!)"

        scene ml_ml_and_f_bedroom_night_scene2_v1_p3
        Dad "Ooooh God! Ooooh yeah! That’s it!"
        Dad "Take my cock! Ahh!"
        Mom "(Snoooooorrreee)"
        MC "(Is she… asleep?)"

        scene ml_ml_and_f_bedroom_night_scene2_v1_p4
        if renpy.loadable("patch.rpy"):
            MC "(Holy crap! Mom’s ACTUALLY fallen asleep during sex!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Holy crap! Linda’s ACTUALLY fallen asleep during sex!)"
        MC "(And she hasn’t even gotten fully undressed either.)"
        MC "(Gee… I didn’t know she had such a terrible sex life.)"
        Dad "Ahh! I’m cumming!"
        if renpy.loadable("patch.rpy"):
            MC "(Uh oh! I better leg it out of here before Dad finishes!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Uh oh! I better leg it out of here before Bob finishes!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_ml_and_f_bedroom_night_scene_v1 = False
        $ ml_ml_and_f_bedroom_night_visit_scene_v1 = 2
        $ ml_ml_and_f_bedroom_night_scene_v1 = True
        $ can_hide_windows = False
        jump salon_night1

    if ml_can_ml_and_f_bedroom_night_scene_v1 == False:
        $ can_hide_windows = False
        show screen salon_night
        show screen ml_ml_and_f_bedroom_night_scene_v1_screen
        MC "It's too risky. I should leave them alone."
        jump salon_night1