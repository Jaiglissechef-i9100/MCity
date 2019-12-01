image lily_school_day_scene1_v1_p1 = "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/1.jpg"
image lily_school_day_scene1_v1_p2 = "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/2.jpg"

label lily_school_day_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    scene lily_school_day_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    Lily "Hey, [player_name]!"
    MC "Oh, hey Lily!"
    $ lily_school_day_scene1_v1q1a1 = True
    $ lily_school_day_scene1_v1q1a2 = True
    $ lily_school_day_scene1_v1q1a3 = True
    jump questions_lily_school_day_scene1_v1

label questions_lily_school_day_scene1_v1:

    scene lily_school_day_scene1_v1_p1
    menu:

        "What’s up?" if lily_school_day_scene1_v1q1a1 == True:

            scene lily_school_day_scene1_v1_p2
            MC "What’s up?"
            Lily "Eh, kinda bored right now. I think I’m gonna sneak out early and try to miss Chemistry."
            MC "Aren’t you worried about getting caught?"
            Lily "Nah - what’s the worst that could happen? Mr. Jackon keeps threatening to discipline me - but he’s all bark and no bite!"
            MC "(Everyone probably has a little bite in them if you push them hard enough. Lily ought to be careful!)"
            $ lily_school_day_scene1_v1q1a1 = False
            if lily_school_day_scene1_v1q1a2 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

        "Have you seen my sister?" if lily_school_day_scene1_v1q1a2 == True and persistent.incest_patch == True:

            scene lily_school_day_scene1_v1_p2
            MC "Have you seen my sister?"
            Lily "Sara? Sure - she’s probably still in the corridor. At least, that’s where I last seen her before I came into class."
            MC "Thanks, Lily."
            Lily "No sweat, [player_name]."
            $ lily_school_day_scene1_v1q1a2 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

        "Have you seen Sara?" if lily_school_day_scene1_v1q1a2 == True and not persistent.incest_patch == True:

            scene lily_school_day_scene1_v1_p2
            MC "Have you seen Sara?"
            Lily "Sara? Sure - she’s probably still in the corridor. At least, that’s where I last seen her before I came into class."
            MC "Thanks, Lily."
            Lily "No sweat, [player_name]."
            $ lily_school_day_scene1_v1q1a2 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1
        "You up to anything interesting after school?" if lily_school_day_scene1_v1q1a3 == True:

            scene lily_school_day_scene1_v1_p2
            MC "Are you up to anything interesting after school?"
            Lily "I’m gonna go shopping for a new bikini. Aside from that, I don’t have big plans."
            Lily "I’m thinking of going for something really… skimpy. Small and tight."
            MC "Uh… Wow! (I’d love to see her dressed like that!)"
            $ lily_school_day_scene1_v1q1a3 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a2 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

label after_questions_lily_school_day_scene1_v1:
    $ lily_bath_event_unlock = True
    $ lily_school_day_scene1_v1 = 3
    $ lily_bath_event_unlock = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom2_day1
