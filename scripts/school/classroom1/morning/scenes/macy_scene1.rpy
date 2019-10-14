image macy_scene1_p1 = "images/school/classroom1/morning/scenes/macy_scene1/1.jpg"
image macy_scene1_p2 = "images/school/classroom1/morning/scenes/macy_scene1/2.jpg"
image macy_scene1_p3 = "images/school/classroom1/morning/scenes/macy_scene1/3.jpg"
image macy_scene1_p4 = "images/school/classroom1/morning/scenes/macy_scene1/4.jpg"
image macy_scene1_p5 = "images/school/classroom1/morning/scenes/macy_scene1/5.jpg"
image macy_scene1_p6 = "images/school/classroom1/morning/scenes/macy_scene1/6.jpg"
image macy_scene1_p7 = "images/school/classroom1/morning/scenes/macy_scene1/7.jpg"
image macy_scene1_p8 = "images/school/classroom1/morning/scenes/macy_scene1/8.jpg"
image macy_scene1_p9 = "images/school/classroom1/morning/scenes/macy_scene1/9.jpg"

label macy_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if macy_work_inprogress == True:
        show screen classroom1_morning_notclickable
        $ renpy.show("workinprogress2", layer="screens",)
        " Available soon."
        $ renpy.hide("workinprogress2", layer="screens",)
        jump classroom1_morning1

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene macy_scene1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Ah! There she is! Macy. She's the kindest person in this school...)"
    MC "(She’s was the only one who believed in me and told me that I've got a chance with Celia!)"
    scene macy_scene1_p2
    MC "Hey, Macy! What’s up?"
    Macy "…"
    MC "Macy?"
    Macy "(I can hold it! I CAN HOLD IT!)"
    scene macy_scene1_p3
    Macy "Hahahahaah! I-I can't believe you actually did this! Haha!"
    Macy "Asking our teacher- Haha! You've got balls, I must admit that! Haha!"
    MC "Hey! You promised not to laugh about it!"
    Macy "Sorry! Haha! Don’t be mad!"
    scene macy_scene1_p4
    MC "Shut up!"
    Macy "Okay, okay!"
    Macy "..."
    Macy "You even had to go and talk with a therapist! N-No it’s too much! Haha!"
    MC "I had enough! You know what? Fuck you! "
    scene macy_scene1_p5
    MC "(Ehh.. This is going to be a long day..)"
    scene black
    $ renpy.pause(3, hard=True)
    scene macy_scene1_p6
    Macy "…"
    Macy "BOO!"
    MC "I’m not sleeping."
    MC "Did yo-"
    Macy "Wait! Let me say something first."
    scene macy_scene1_p7
    Macy "I'm sorry. I shouldn’t have laughed at you. It was bad, I know."
    Macy "You know me! I'm not like that.. It's just.. everyone was talking about it.."
    MC "Relax. It’s okay."
    scene macy_scene1_p8
    Macy "So.. Do you hate me now!?"
    MC "N-No! We’re fine."
    Macy "Good…"
    MC "I know now that it was stupid to even ask her that… In addition, in the school..."
    scene macy_scene1_p9
    Macy "{size=-15}You could just ask me, moron...{/size}"
    $ macy_work_inprogress = True
    $ day_time += 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom1_morning1
