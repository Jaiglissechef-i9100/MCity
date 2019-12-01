image celia_school_morning_scene1v1_p1 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/1.jpg"
image celia_school_morning_scene1v1_p2 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/2.jpg"
image celia_school_morning_scene1v1_p3 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/3.jpg"

image celia_school_morning_scene1v1_celia = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/RenPy.png"

image celia_school_morning_scene1av1_p1 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1av1/1.jpg"
image celia_school_morning_scene1av1_p2 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1av1/2.jpg"

label celia_school_morning_scene1v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        $ Classmates = __("Classmates")
        $ Blonde_Boy = __("Blonde Boy")
        $ Brunette_Girl= __("Brunette Girl")
    else:
        $ Classmates = __("Classmates")
        $ Blonde_Boy = __("Blonde Boy")
        $ Brunette_Girl= __("Brunette Girl")
    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 1:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1v1_p1 with dissolve
        Celia "Good morning, loverboy!"
        Celia "Any luck getting yourself a girl yet?"

        scene celia_school_morning_scene1v1_p2
        MC "(Fuck you! I promise I’ll get my revenge on you!)"
        Celia "Or were you thinking of asking out your teacher again?"
        MC "(Grr… She’s embarrassing me in front of the whole class!)"

        scene celia_school_morning_scene1v1_p3
        Classmates "Ahahahaha!"
        Celia "Go back to your classroom, [player_name]. Class is about to begin."
        MC "(God… Now I hate her! I wonder how long it will be until she forgets about this.)"

        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2

    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 2:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1v1_p1 with dissolve
        Celia "You again? Are you trying to ask me out again?"
        MC "Wh-What?! No!"

        scene celia_school_morning_scene1v1_p2
        Celia "So you don’t want to go out with me..?"
        MC "I- Wh- N-No? I mean y-yes?"
        Celia "Ugh, what a loser. Get back to your class."
        MC "..."

        scene celia_school_morning_scene1v1_p3
        Classmates "Hahahahaha!"
        Blonde_Boy "Wow! How pathetic!"
        Brunette_Girl "Oh, my God! That’s soooo cringeworthy!"
        MC "(Oh God… That was fucking terrible…)"
        MC "(I promise you, I’ll get my revenge on you, bitch!)"
        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2

    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 3:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1av1_p1 with dissolve
        MC "Hey, Mrs. Celia..."
        Celia "If you have any questions... just... just ask one of your classmates."

        scene celia_school_morning_scene1av1_p2
        MC "Are you sure?"
        Celia "Yeah. Just... get back to your class."
        MC "Huh? Okay."
        MC "(She’s acting less aggressive than before!)"
        MC "(I guess my blackmail strategy is working very well.)"
        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2

    if can_celia_school_morning_scene1v1 == False:

        show celia_school_morning_scene1v1_celia
        show screen classroom2_morning_notclickable
        $ can_hide_windows = False
        MC "I don’t want to talk to that... bitch."
        $ can_hide_windows = False
        jump classroom2_morning2
