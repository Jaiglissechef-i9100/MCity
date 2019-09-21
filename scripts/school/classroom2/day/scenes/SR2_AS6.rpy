label SR2_AS6_label:
    if can_SR2_AS6 == False:
        $ clickable = False
        show screen classroom2_day
        MC "I've already talked with her."
        $ clickable = True
        jump classroom2_morning1

    if not lube in inventory.items:
        $ clickable = False
        show screen classroom2_day
        MC "I still did not buy a lubricant."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

        scene SR2_AS3_p1 with dissolve

        MC "I finally got it, Sara. I’ll keep it in the house until later tonight."
        Sara "Huh? What did you get? I don’t know what you’re talking about."
        MC "The lube, Sara! Remember?"

        scene SR2_AS3_p2

        Sara "You actually bought lube?!"
        MC "(Shit! This is like the vibrator, all over again!)"
        MC "Shush! Keep your voice down!"

        scene SR2_AS3_p3

        MC "Remember, we talked about this on the roof? It’ll make things easier, for when we finally do it."
        MC "Can I take my hand off your mouth now?"
        Sara "Mmm hmm."

        scene SR2_AS3_p4

        Sara "Wh-What happens now?"
        MC "Come over to my room tonight, and we’ll try it out."
        Sara "I’m scared… it was soooo painful last time."

        scene SR2_AS3_p5

        MC "It’ll be better this time, I promise. We weren’t properly prepared last time."
        MC "And if it hurts you at all - we’ll just stop. Okay?"
        Sara "Okay… I guess so. I’ll see you tonight in your bedroom, then."
        MC "I’m looking forward to it. Catch you later, Sara."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        $ can_SR2_AS6 = False
        $ SR2_NS4 = True
        $ S_N_inbed = False
        jump classroom2_morning1
