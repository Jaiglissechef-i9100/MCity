image ML_morning_scene0_v1_p1 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/1.jpg"
image ML_morning_scene0_v1_p2 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/2.jpg"
image ML_morning_scene0_v1_p3 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/3.jpg"
image ML_morning_scene0_v1_p4 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/4.jpg"
image ML_morning_scene0_v1_p5 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/5.jpg"

label ML_morning_scene0_v1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene ML_morning_scene0_v1_p1 with dissolve
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        MC "(Huh, that’s unusual. That’s Mom’s office suit.)"
    else:
        MC "(Huh, that’s unusual. That’s Linda’s office suit.)"
    MC "(She’s doesn’t normally dress and leave, for AT LEAST another hour.)"
    scene ML_morning_scene0_v1_p2 at pandown3
    $ renpy.pause(2)
    MC "(Her legs DO look really good in it though…)"
    MC "(Wait - what am I thinking?!)"
    MC "(Ever since she kissed me on the mouth the other morning, these lewd thoughts about her have kept creeping into my mind.)"
    MC "(Perhaps I should just address her about this, face-to-face?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    scene ML_morning_scene0_v1_p3
    Mom "Oh! You startled me there, [player_name]!"
    Mom "I was just about to head into work early, today."
    Mom "What’s up with you? Something on your mind?"
    MC "Uhh… Y-Yeah actually - I wanted to talk to you about that… umm… kiss you gave me, the other day."

    scene ML_morning_scene0_v1_p4
    Mom "Oh, that… Haha… That was… nothing."
    MC "It was… just... It was the first time I’ve ever kissed a girl."
    Mom "Aww, I’m sorry. C’mere."

    scene ML_morning_scene0_v1_p5
    Mom "Sorry - you were just so sad there, back then. And I wanted to try and make my boy happy."
    Mom "I guess I got a little too emotional, and caught up in the moment."
    Mom "Can you forgive me?"
    if persistent.incest_patch == True:
        MC "Y-Yeah, Mom. It’s alright."
    else:
        MC "Y-Yeah, Linda. It’s alright."
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ salon_ml_first_visit = True
    $ ml_salon_morning_visit = 1
    $ ml_can_salon_morning_scene = False
    $ ml_can_salon_morning_scene2 = False
    $ can_hide_windows = False
    jump salon_morning1

