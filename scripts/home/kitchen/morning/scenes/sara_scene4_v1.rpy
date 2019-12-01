image scene4_v1p1 = "images/home/kitchen/morning/scenes/sara_scene4_v1/1.jpg"
image scene4_v1p2 = "images/home/kitchen/morning/scenes/sara_scene4_v1/2.jpg"
image scene4_v1p3 = "images/home/kitchen/morning/scenes/sara_scene4_v1/3.jpg"
image scene4_v1p3a = "images/home/kitchen/morning/scenes/sara_scene4_v1/3a.jpg"
image scene4_v1p4 = "images/home/kitchen/morning/scenes/sara_scene4_v1/4.jpg"

default first_visit_sister_nerdy_scene4_v1 = 1
default second_visit_sister_nerdy_scene4_v1 = 0
default third_visit_sister_nerdy_scene4_v1 = 0
default fourth_visit_sister_nerdy_scene4_v1 = 0

label sister_nerdy_scene4_v11:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if next_day_sister_nerdy_scene4_v1 == False:
        show screen kitchen_morning_notclickable
        MC "I already know who's there."
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 1 and first_visit_sister_nerdy_scene4_v1 == 1 and next_day_sister_nerdy_scene4_v1 == True:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)

        scene scene4_v1p1
        $ can_hide_windows = True
        MC "(Looks like I made it just in time.)"
        MC "(Hey, those are the panties I almost stole from her!)"
        MC "(She’s got a matching bra too - it must be a set she likes.)"
        MC "(Maybe tomorrow there will be a better view!)"

        $ next_day_sister_nerdy_scene4_v1 = False
        $ first_visit_sister_nerdy_scene4_v1 = 2
        $ second_visit_sister_nerdy_scene4_v1 = 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 1 and next_day_sister_nerdy_scene4_v1 == True and second_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)

        scene scene4_v1p2
        $ can_hide_windows = True
        MC "(Mmm, even better this time! I get a front row seat to her naked ass!)"
        MC "(Damn, she has such sexy thighs too.)"
        MC "(I’d love to spread those cheeks and fuck her silly.)"
        MC "(Let’s watch her again some other time.)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ second_visit_sister_nerdy_scene4_v1 = 2
        $ third_visit_sister_nerdy_scene4_v1 = 1
        $ first_sis_nerdy_scene4_v1 += 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 2 and next_day_sister_nerdy_scene4_v1 == True and  third_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)
        scene scene4_v1p3
        $ can_hide_windows = True
        MC "(Perfect timing! It looks like she’s just about to take a shower!)"
        MC "(I can almost see her pussy from this angle!)"
        if persistent.incest_patch == True:
            MC "(Please, if there’s a God up there, I’m begging you! Let my sister bend over right now!)"
        else:
            MC "(Please, if there’s a God up there, I’m begging you! Let my friend bend over right now!)"

        scene scene4_v1p3a
        Sara "(Huh, looks like I missed a hair when I was shaving my legs.)"
        MC "(There is a God!)"
        MC "(Damn, she looks so tight! I would love to bury my cock in her cunt.)"
        MC "(It would feel fucking amazing!)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 3 and next_day_sister_nerdy_scene4_v1 == True and fourth_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)
        scene scene4_v1p4
        $ can_hide_windows = True
        Sara "Ah! Ah… Ahh… Mmm… Ooh…"
        MC "(Just in time! Looks like she is masturbating!)"
        MC "(I wonder what she’s looking at on her phone. Could it be that picture of my cock?)"
        Sara "Ohh… [player_name]! Yes…!"
        if persistent.incest_patch == True:
            MC "(She’ll need to be quieter than that, if she doesn’t want Mom to hear her!)"
        else:
            MC "(She’ll need to be quieter than that, if she doesn’t want Linda to hear her!)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ sis_nerdy_scene4_v1 = False
        $ can_toilet_after_sara_scene4_1 = False
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

label sister_nerdy_scene4_v1_l_door_locked:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if next_day_sister_nerdy_scene4_v1 == False:
        show screen kitchen_morning_notclickable
        MC "I already know who's there."
        jump kitchen_morning1
    show screen kitchen_morning_notclickable
    MC "It’s locked! I wonder who is there…?"
    MC "If I only had some spy camera I could use it to see through the door!"
    jump kitchen_morning1
