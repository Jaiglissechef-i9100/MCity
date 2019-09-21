image ML_NS_sleep_p1 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/1.jpg"

default ML_NSB_sleep_can = True

label ML_NS_sleep_label:
    $ Linda_name = Mom_name
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ML_NS_sleep_p1 with dissolve
    Mom "Zzz..."
    Dad "*Snore*"
    MC "(They’re both fast asleep. Let’s see if I can wake up [Linda_name] - and bring her back to my bedroom for some fun!)"

    $ can_hide_windows = True

    if not ML_NS_sleep_hand in nsb_box.ml_nsb_wake:
        $ nsb_box.add_ml_wake(ML_NS_sleep_hand)
        $ nsb_box.add_ml_wake(ML_NS_sleep_foot_job)

    if not ML_NS_sleep_her in nsb_box.ml_nsb_wake:
        $ nsb_box.add_ml_wake(ML_NS_sleep_her)

    $ Ml_stats_visited += 1
    $ inv_page = 0
    call screen ML_NS_sleep_scr

label ML_NS_sleep_back:
    $ ML_NSB_sleep_can = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black with dissolve
    $ renpy.pause(2, hard = True)
    $ renpy.sound.play("sfx/door_open.mp3")
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump salon_morning1
