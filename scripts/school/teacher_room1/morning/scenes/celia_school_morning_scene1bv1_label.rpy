image celia_school_morning_scene1bv1_p1 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/1.jpg"
image celia_school_morning_scene1bv1_p2 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/2.jpg"
image celia_school_morning_scene1bv1_p3 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/3.jpg"
image celia_school_morning_scene1bv1_p4 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/4.jpg"
image celia_school_morning_scene1bv1_p5 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/5.jpg"

label celia_school_morning_scene1bv1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    scene celia_school_morning_scene1bv1_p1 with dissolve
    $ can_hide_windows = True
    Celia "[player_name]? Oh, thank God you’re here."
    MC "Huh? Is everything alright, Mrs. Celia?"
    Celia "Everything’s fine… Actually, no. No, it really isn’t. We need to talk."

    scene celia_school_morning_scene1bv1_p2
    Celia "You may be wondering why I have been acting so… interested in you lately."
    MC "You mean like in the toilet when we-"
    Celia "Yes! You don’t need to describe it to me. The truth of the matter is, I’m being blackmailed."
    MC "Blackmailed?! By who?"

    scene celia_school_morning_scene1bv1_p3
    Celia "That’s the crux of the problem. I don’t know who."
    MC "Huh... There’s nothing you can do then?"
    Celia "There most certainly is. I need your help though."
    MC "What’s in it for me? Tracking down some creepy blackmailer, doesn’t sound too safe."

    scene celia_school_morning_scene1bv1_p4
    Celia "If you help me catch him, there will be a reward in it for you."
    Celia "If you catch my drift?"
    MC "I’ll get to fuck you?"
    Celia "It depends on how good you are at catching this bastard."

    scene celia_school_morning_scene1bv1_p5
    MC "Count me in!"
    Celia "Excellent! Please, take this. It’s my address. I want you to come over."
    Celia "I’m usually at home in the evening... No, make it at night."
    Celia "My husband’s away on a business trip, so we’ll sit down and hammer out a solid strategy for catching this prick."
    MC "Cool. See you later on then, Mrs. Celia."
    Celia "Goodbye, [player_name]."
    show relationship_plus
    $ renpy.pause(3.0, hard=True)
    $ Celia_points += 1
    $ celia_school_morning_scene1bv1 = 3
    $ celia_work_in_progress_v1 = 1
    $ can_celia_school_morning_scene1bv1 = 3
    $ celia_house_unlocked = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump teacher_room1_morning2