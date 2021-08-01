image sis_nerdy_school_scene2_v1_p1 = "images/school/school_entrance/day/scenes/sara_scene2_v1/1.jpg"
image sis_nerdy_school_scene2_v1_p2 = "images/school/school_entrance/day/scenes/sara_scene2_v1/2.jpg"
image sis_nerdy_school_scene2_v1_p3 = "images/school/school_entrance/day/scenes/sara_scene2_v1/3.jpg"
image sis_nerdy_school_scene2_v1_p4 = "images/school/school_entrance/day/scenes/sara_scene2_v1/4.jpg"

label sis_nerdy_school_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    hide screen school_entrance_day_notclickable
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)

    scene sis_nerdy_school_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Oh! There’s Lily and Sara. They must be waiting for their next class to start.)"
    Lily "What was it you were sooo desperate to show me, Sara?"
    MC "(Huh? Is Sara getting her phone out?)"
    Lily "Oh, my God! Is this Dan from Chemistry?"

    scene sis_nerdy_school_scene2_v1_p2
    if persistent.incest_patch == True:
        Sara "No! It’s… my brother…"
    else:
        Sara "No! It’s… [player_name]"
    Lily "No way! Show me again!"
    Sara "Not in school… I’ll text you later."
    Lily "Oh, my God!"
    MC "(She’s showing off that picture she took, of my dick!)"

    scene sis_nerdy_school_scene2_v1_p3
    Lily "Like, what the hell happened? Why was he showing you his junk?"
    Sara "We… We were playing a game… It got a little out of hand."
    Lily "No kidding! You NEED to get another one!"
    Sara "Another pic?"
    Lily "Yeah, and make sure he is fully hard this time."

    scene sis_nerdy_school_scene2_v1_p4
    MC "(Jeez… I should have forced her to delete it when I had the chance. I should head on to my next class.)"
    Sara "How exactly am I supposed to do that?"
    Lily "Easy - wait until he goes to sleep. Rub your hand over his junk a bit, to get him all hot and horny - then snap a pic. Easy!"
    Sara "Eh… I don’t know… It sounds a bit risky."
    Lily "Don’t pussy out on me now, Sara!"

    $ sis_nerdy_school_scene2_v1 = 3
    $ can1_mc_sara_night_scene1_v1 = True
    $ mc_sara_night_scene1_v1 = 1
    $ can2_sis_nerdy_school_scene1_v1 = False
    $ can_lily_scene = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump school_entrance_day1

