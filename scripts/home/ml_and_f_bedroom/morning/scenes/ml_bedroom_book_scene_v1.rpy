image ml_bedroom_book_scene_v1_p1 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/1.jpg"
image ml_bedroom_book_scene_v1_p2 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/2.jpg"
image ml_bedroom_book_scene_v1_p3 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/3.jpg"
image ml_bedroom_book_scene_v1_p4 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/4.jpg"

label ml_bedroom_book_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_bedroom_book_scene_v1_p1 with dissolve
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        MC "(Ahh, this looks like the book Mom was reading when she was fucking Dad the other night!)"
    else:
        MC "(Ahh, this looks like the book Linda was reading when she was fucking Bob the other night!)"
    MC "(I wonder what could possibly be more interesting than having sex?)"
    MC "(Let’s turn this over…)"

    if persistent.incest_patch == True:
        scene ml_bedroom_book_scene_v1_p2
        MC "Dating your… son?"
    else:
        MC "Dating your… much younger friend?"
    MC "How to tell if he… is SEXUALLY ATTRACTED to you?!"

    scene ml_bedroom_book_scene_v1_p3
    MC "Holy moly!"
    MC "(Is she just reading this for fun?)"
    MC "(No… she must be serious.)"
    MC "(The way she kissed me, so intensely that morning, and the weird way she’s been acting around me.)"
    if persistent.incest_patch == True:
        MC "(Is she thinking about fucking me when she’s with Dad?)"
    else:
        MC "(Is she thinking about fucking me when she’s with Bob?)"
    scene ml_bedroom_book_scene_v1_p4
    MC "Fuck… It all makes sense now."
    if persistent.incest_patch == True:
        MC "(My own mother wants to fuck me!)"
        MC "(How the heck am I even supposed to respond to this?!)"
        MC "(God… I’ll never be able to look her straight, in the eyes again!)"
        MC "(Mom’s lucky that Dad isn’t paying attention to the books she reads! If he caught her with this, he’d be furious!)"
    else:
        MC "(Linda wants to fuck me!)"
        MC "(How the heck am I even supposed to respond to this?!)"
        MC "(God… I’ll never be able to look her straight, in the eyes again!)"
        MC "(Linda’s lucky that Bob isn’t paying attention to the books she reads! If he caught her with this, he’d be furious!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_book_scene = False
    $ can_hide_windows = False
    jump salon_morning1
