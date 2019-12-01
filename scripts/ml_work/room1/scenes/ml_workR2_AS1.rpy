image ml_workR2_AS1_p1 = "/images/ml_work/room1/scenes/ml_workR2_AS1/1.jpg"
image ml_workR2_AS1_p2 = "/images/ml_work/room1/scenes/ml_workR2_AS1/2.jpg"
image ml_workR2_AS1_p3 = "/images/ml_work/room1/scenes/ml_workR2_AS1/3.jpg"
image ml_workR2_AS1_p4 = "/images/ml_work/room1/scenes/ml_workR2_AS1/4.jpg"
image ml_workR2_AS1_p5 = "/images/ml_work/room1/scenes/ml_workR2_AS1/5.jpg"
image ml_workR2_AS1_p6 = "/images/ml_work/room1/scenes/ml_workR2_AS1/6.jpg"
image ml_workR2_AS1_p7 = "/images/ml_work/room1/scenes/ml_workR2_AS1/7.jpg"
image ml_workR2_AS1_p8 = "/images/ml_work/room1/scenes/ml_workR2_AS1/8.jpg"
image ml_workR2_AS1_p9 = "/images/ml_work/room1/scenes/ml_workR2_AS1/9.jpg"


label ml_workR2_AS1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Hi, Mom!"
    else:
        MC "Hi, Linda!"
    Mom "Good afternoon, Sweetie. Are you here for work?"
    MC "Yeah, do you have anything for me?"

    scene ml_workR2_AS1_p2

    Mom "Just more cleaning, if you’re happy to do that."
    MC "Sure. I’ll get started on that now."
    Mom "Thanks, Sweetie! Come back and let me know when you’re done."
    $ renpy.music.stop(channel="music1", fadeout=1)
    if persistent.skip_mg == True:
        jump after_ml_workR2_AS1_label
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_R2_room1_label


label after_ml_workR2_AS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ inventory.earn(25)
    $ renpy.pause(3, hard = True)


    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p3 with dissolve

    MC "Alright, that’s me done!"
    MC "You’ve got some REALLY messy employees! Do they not know what a bin is?! Haha!"
    Mom "Yeah, there’s a couple of men that are complete slobs. I’d sack them if they weren’t so good at their jobs."
    MC "So… now that I’ve finished that for you, perhaps we could…"

    scene ml_workR2_AS1_p4

    Mom "I’m sorry, Sweetie. I’m up to my eyes in work today."
    Mom "See this folder?"
    MC "Yeah?"
    Mom "This will take me an hour to process. And after I’ve finished, I have FIVE more folders to go through."

    scene ml_workR2_AS1_p5

    MC "Aww, jeez. That sounds tough."
    MC "Is there any way I can help you with this?"
    Mom "Thanks for the offer. But unless you’re a qualified accountant, I can’t legally let you work with them."
    MC "Oh, fair enough then. Well, if there’s anything I can do, just give me a text, okay?"

    scene ml_workR2_AS1_p6

    Mom "C’mon, Sweetie! Don’t look so downhearted. Once we get through tax season, then I will have a LOT of free time for you."
    Mom "I’ll just be busy for a couple more days. I promise."

    scene ml_workR2_AS1_p7

    Mom "In the meantime, just let your imagination wander, with thoughts of all the dirty things I’ll do to you."
    MC "(Holy shit! That is a LOT of pent up sexual frustration, right there!)"
    MC "(It sounds like I’ll be in for a treat when she has finished!)"

    scene ml_workR2_AS1_p8

    Mom "Anyway, I better let you go, before I get distracted."
    Mom "I’ll see you later on. Love you, Sweetie."
    if renpy.loadable("patch.rpy"):
        MC "See you later, Mom. Love you too!"
    else:
        MC "See you later, Linda. Love you too!"
    $ ml_workR2_AS1 = False
    $ can_ml_workR2 = False
    $ ml_workR2_AS2 = True
    $ day_time = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label