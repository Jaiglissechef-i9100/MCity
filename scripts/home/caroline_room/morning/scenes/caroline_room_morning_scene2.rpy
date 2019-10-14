image caroline_room_morning_scene2_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/1.jpg"
image caroline_room_morning_scene2_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/2.jpg"
image caroline_room_morning_scene2_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/3.jpg"
image caroline_room_morning_scene2_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/4.jpg"

label caroline_room_morning_scene2_label:
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
    $ can_hide_windows = True
    scene caroline_room_morning_scene2_p1 with dissolve

    MC "(Caroline did say I could come and talk with her any time.)"
    MC "(I guess it wouldn’t hurt to chat with someone, other than my therapist.)"
    MC "(Plus, Caroline tends to hang around in her underwear when she’s in her bedroom.)"

    scene caroline_room_morning_scene2_p2
    MC "Uh, hey Caroline. Remember you said that I could come and chat-"
    Caroline "I’m sorry, [player_name]. I know I promised, but... "
    Caroline "...I just can’t handle it right now."
    MC "Is everything okay?"

    scene caroline_room_morning_scene2_p3
    Caroline "…"
    MC "Caroline?"
    MC "(She might not be free to chat, but at least I get to check out her ass.)"

    scene caroline_room_morning_scene2_p4
    Caroline "I’m sorry, [player_name]. I’m under a LOT of pressure right now."
    MC "Are you behind on those heavy business textbooks you read?"
    Caroline "No, it’s my shop. I… I can’t make the finances balance."
    Caroline "Listen, would you mind leaving me alone for a while?"
    Caroline "I know I promised you that I’d be here to chat, but I’m in no fit state right now."
    MC "Sorry, Caroline. I’ll give you some space."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1