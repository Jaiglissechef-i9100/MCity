image MLR2_ES2_p1 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/1.jpg"
image MLR2_ES2_p2 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/2.jpg"
image MLR2_ES2_p3 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/3.jpg"
image MLR2_ES2_p4 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/4.jpg"
image MLR2_ES2_p5 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/5.jpg"
image MLR2_ES2_p6 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/6.jpg"
image MLR2_ES2_p7 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/7.jpg"
image MLR2_ES2_p8 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/8.jpg"
image MLR2_ES2_p9 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/9.jpg"

label MLR2_ES2_label:
    $ renpy.music.stop(channel="music2", fadeout=1)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(3,hard = True)
    scene MLR2_ES2_p1 with dissolve
    $ can_hide_windows = True
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    Mom "Boo!"
    MC "Ahh!"
    if renpy.loadable("patch.rpy"):
        MC "Jesus, you scared me there, Mom!"
    else:
        MC "Jesus, you scared me there, Linda!"

    scene MLR2_ES2_p2

    Mom "Well… YOU are the one sneaking into MY room!"
    MC "Err… I suppose so."
    Mom "You must already be missing me."

    scene MLR2_ES2_p3
    if renpy.loadable("patch.rpy"):
        MC "Haha! Of course I do, Mom. I love spending time with you."
    else:
        MC "Haha! of course I do, Linda. I love spending time with you."
    Mom "You’re such a sweetheart."
    Mom "I could just push you back on the bed, right now. Strip off your jeans and-"
    $ renpy.sound.play('/sfx/phone_ringing.wav', loop=False)
    "RING RING! RING RING!"
    $ renpy.sound.stop(channel="sound")
    scene MLR2_ES2_p4

    MC "Huh?"
    $ renpy.sound.play('/sfx/phone_ringing.wav', loop=False)
    "RING RING! RING RING!"
    $ renpy.sound.stop(channel="sound")
    Mom "Crap - that’s my phone. Hang on. I’ll only be two minutes."

    scene MLR2_ES2_p5

    Mom "Actually… can you leave? It’s a work call. I’m sorry."
    if renpy.loadable("patch.rpy"):
        MC "Sure, Mom. No problem."
    else:
        MC "Sure, Linda. No problem."
    MC "(Huh? I wonder what made her change her mind so quickly.)"

    scene MLR2_ES2_p6

    Mom "Hello, Judy. What’s up?"
    "…"
    Mom "Uh huh. Now’s not a great time."


    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    scene MLR2_ES2_p7

    MC "(Judy? I wonder if it’s the same Judy that’s my therapist.)"
    Mom "Yes, of course. The deal is still on."
    "…."
    Mom "Sure, we can meet up again for a coffee soon."

    scene MLR2_ES2_p8

    Mom "How about you? Is the book coming along well?"
    "...."
    Mom "Writer’s block? I’m sorry to hear that."
    "…"

    scene MLR2_ES2_p9

    Mom "Of course. I did promise I would help you."
    Mom "Don’t you worry, Judy. I’ll give you some ideas, as soon as I can."
    "...."
    Mom "Chat later!"
    MC "(Crap, she’s almost finished. I better go, so she doesn’t think I’ve been eavesdropping on her!)"
    $ can_ml_workR2_AS2 = True
    $ MLR2_ES2 = False
    $ day_time = 4
    $ judy_q2 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump salon_morning1