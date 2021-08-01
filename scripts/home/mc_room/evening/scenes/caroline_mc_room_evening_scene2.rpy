image caroline_mc_room_evening_scene2_p1 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/1.jpg"
image caroline_mc_room_evening_scene2_p2 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/2.jpg"
image caroline_mc_room_evening_scene2_p3 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/3.jpg"

label caroline_mc_room_evening_scene2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_mc_room_evening_scene2_p1 with dissolve
    $ can_hide_windows = True
    MC "Caroline? I- I’m sorry about earlier today."
    MC "I’ll make it up to you, I swear. If you just let me-"
    Caroline "Shush."

    scene caroline_mc_room_evening_scene2_p2
    Caroline "I’m the one who should be apologising. I completely overreacted."
    MC "Y-You are?"
    Caroline "It’s completely normal - and probably even healthy - for a guy your age."
    Caroline "And to be fair, my outfit wasn’t leaving a lot to the imagination."
    MC "(Yeah, she’s right, there!)"

    scene caroline_mc_room_evening_scene2_p3
    Caroline "So, I’m sorry, [player_name]. Are we cool?"
    MC "Yeah, we’re cool."
    MC "And for the record… I’m sorry too."
    Caroline "Oh! Before I forget - I’m planning a little surprise, to make it up to you."

    scene caroline_mc_room_evening_scene2_p2
    MC "Aww, you don’t have to do that."
    Caroline "Trust me. I think you’ll enjoy it!"
    Caroline "Catch you later, [player_name]."
    MC "See ya, Caroline!"
    $ caroline_mc_room_evening_scene2 = False
    $ caroline_mc_room_evening_scene3 = True
    $ caroline_mc_room_can_evening_scene3 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1

