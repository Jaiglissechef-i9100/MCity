image sara_night_sleeping1_v1_p1 = "images/home/sara_room/night/scenes/sleeping1/1.jpg"
image sara_night_sleeping1_v1_p2 = "images/home/sara_room/night/scenes/sleeping1/2.jpg"
image sara_night_sleeping1_v1_p3 = "images/home/sara_room/night/scenes/sleeping1/3.jpg"
image sara_night_sleeping1_v1_p4 = "images/home/sara_room/night/scenes/sleeping1/4.jpg"

label sis_nerdy_night_sleeping1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if can_sis_nerdy_night_sleeping1_v1 == True:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene sara_night_sleeping1_v1_p1 with dissolve
        $ can_hide_windows = True
        MC "(Whispered) Sara?"
        Sara "…"
        MC "(Whispered) Are you asleep?"
        MC "(Sounds like she’s completely asleep. If I’m careful I might be able to touch her without waking her up.)"

        scene sara_night_sleeping1_v1_p2
        MC "(Carefully does it… I just have to get these blankets off her first.)"
        MC "(Perfect! Wow, I thought she’d be wearing pyjamas. This makes things easier!)"
        MC "(Next step is taking off that bra!)"

        scene sara_night_sleeping1_v1_p3
        MC "(Okay, here we go.)"
        Sara "*Snore*"
        MC "(Uh oh…)"
        MC "(Don’t wake up, don’t wake up…)"

        scene sara_night_sleeping1_v1_p4
        Sara "(Yawn!)"
        MC "(Crap! She’s starting to come to. I better get out of here.)"
        MC "(At least I got to see her in her underwear!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        scene black
        $ renpy.sound.play("sfx/door_open.mp3")
        $ renpy.pause(1, hard = True)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_sis_nerdy_night_sleeping1_v1 = False
        $ sis_nerdy_night_sleeping1_v1 = 3
        $ sara_room_night_sleeping2 = True
        $ can_hide_windows = False
        jump corridor_night1

