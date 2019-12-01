image caroline_room_morning_scene3_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/1.jpg"
image caroline_room_morning_scene3_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/2.jpg"
image caroline_room_morning_scene3_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/3.jpg"
image caroline_room_morning_scene3_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/4.jpg"

label caroline_room_morning_scene3_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_can_room_morning_scenes == False:
        show screen caroline_room_morning_not_clickable
        MC "I've already talked to her."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene caroline_room_morning_scene3_p1 with dissolve
    $ can_hide_windows = True
    MC "(Huh? What’s wrong with Caroline?)"
    if persistent.incest_patch == True:
        MC "(This isn’t like her, at all. She’s usually one of the happiest, most upbeat people I’ve ever seen!)"
        MC "(Even Mom’s gotten involved - this must be serious.)"
    else:
        MC "(This isn’t like her, at all. She’s usually one of the happiest, most upbeat people I’ve ever met!)"
        MC "(Even Linda’s gotten involved - this must be serious.)"


    scene caroline_room_morning_scene3_p2
    Mom "Listen, I can afford to help out with the mortgage for a couple more months."
    if persistent.incest_patch == True:
        Mom "But after that, we’ll be relying, almost entirely on your father’s overtime, to make ends meet."
    else:
        Mom "But after that, we’ll be relying, almost entirely Bob’s overtime, to make ends meet."
    if persistent.incest_patch == True:
        Caroline "I know. (Sniff) I’m sorry, Mom."
    else:
        Caroline "I know. (Sniff) I’m sorry, Linda."
    Caroline "I really thought this shop idea would work!"

    scene caroline_room_morning_scene3_p3
    if persistent.incest_patch == True:
        Mom "Perhaps you should consider cutting your losses? Your father might be able to get you a job in Risk Management at the firm?"
    else:
        Mom "Perhaps you should consider cutting your losses? Bob might be able to get you a job in Risk Management at the firm?"
    Caroline "God no! Trust me - I have a plan to turn a profit at my store."
    Caroline "I can’t do it on my own though. I’m gonna need some help to get things off the ground."
    Caroline "Could I borrow [player_name], to help out at my shop a bit?"
    Mom "Sure - as long as he doesn’t mind."

    scene caroline_room_morning_scene3_p4
    Caroline "Would you be able to help me, [player_name]?"
    MC "What do you need me to do?"
    Caroline "Just pop by my shop, in the afternoon. I’ll have everything ready. Then we can begin."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 4
    $ cosplay_shop_unlocked = True
    $ cloth_shop_minigame_unlocked = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
