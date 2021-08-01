image caroline_room_morning_scene4_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/1.jpg"
image caroline_room_morning_scene4_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/2.jpg"
image caroline_room_morning_scene4_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/3.jpg"

label caroline_room_morning_scene4_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if caroline_room_morning_scene4 == False:
        show screen caroline_room_morning_not_clickable
        MC "I've already talked to her."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_room_morning_scene4_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Caroline’s on her phone, but it looks like she’s just texting.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Caroline’s on her phone, but it looks like she’s just texting.)"
    MC "(Hopefully she’s in a better mood, now that I’ve helped out a bit!)"
    MC "Hey, Caroline!"


    scene caroline_room_morning_scene4_p2
    Caroline "Oh! Hiiii, [player_name]!"
    Caroline "Thanks again for your help, down at the store. I really believe we’re gonna see things turn around soon!"
    Caroline "It’s too early to tell if I’ll turn a profit - but I’ve definitely seen more customers browsing."
    Caroline "The online store has started taking off too."

    scene caroline_room_morning_scene4_p3
    Caroline "Thank you so much for everything you’ve done!"
    if renpy.loadable("patch.rpy"):
        Caroline "You’re the best little brother in the whole world!"
    if not renpy.loadable("patch.rpy"):
        Caroline "You’re my best friend in the whole world.!"
    MC "Awww... Thanks, Caroline!"

    scene caroline_room_morning_scene4_p2
    Caroline "If you fancy visiting me again at work, I’m sure I could use your help more often."
    Caroline "Just drop by whenever you’re free."
    MC "No problem! I’m sure you’ll see me again, soon enough."
    $ caroline_room_morning_scene4 = 6
    $ caroline_can_room_morning_scenes = False
    $ caroline_room_morning_scene4 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1