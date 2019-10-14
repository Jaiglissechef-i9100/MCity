image CR3_MS0_p1 = "images/home/mc_room/morning/scenes/CR3_MS0/1.jpg"
image CR3_MS0_p2 = "images/home/mc_room/morning/scenes/CR3_MS0/2.jpg"
image CR3_MS0_p3a = "images/home/mc_room/morning/scenes/CR3_MS0/3a.jpg"
image CR3_MS0_p3b = "images/home/mc_room/morning/scenes/CR3_MS0/3b.jpg"
image CR3_MS0_p4 = "images/home/mc_room/morning/scenes/CR3_MS0/4.jpg"
image CR3_MS0_p5 = "images/home/mc_room/morning/scenes/CR3_MS0/5.jpg"
image CR3_MS0_p6 = "images/home/mc_room/morning/scenes/CR3_MS0/6.jpg"
image CR3_MS0_p7 = "images/home/mc_room/morning/scenes/CR3_MS0/7.jpg"

label CR3_MS0_label:
    if renpy.loadable("patch.rpy"):
        $ Linda_name = __("Mom")
        $ Liza2_name = __("Auntie")
    else:
        $ Mom_name = "Linda"
        $ Liza2_name = "Liza"
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_MS0_p1 with dissolve

    MC "Morning, Caroline! Are you okay? Should you not be heading to work already?"
    Caroline "Morning. I... *sigh*"
    MC "Huh? Is something wrong? You look really worried, right now."

    scene CR3_MS0_p2

    Caroline "Yeah, something’s wrong. Listen - I made a huge mistake."
    MC "I can help! Do you need more money for your business or-"
    Caroline "It’s not a mistake that money can fix. I’ve REALLY fucked things up. You see… Pandora’s box has been opened, and I don’t think I can - ever fully close it again."
    MC "I’m not following you - What’s going on?"
    Caroline "This... deal that you and I made? It’s over..."
    if renpy.loadable("patch.rpy"):
        Caroline "I’ll hold my hands up and acknowledge, tha - I played my part - in causing this chaos, so I have a responsibility, to try and stop it. You’re my brother, for Christ’s sake! I shouldn’t have led you on, like I did."
    else:
        Caroline "I’ll hold my hands up and acknowledge, that - I played my part - in causing this chaos, so I have a responsibility, to try and stop it. There's a big gap between our ages - and in addition, we live under the same roof!"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    menu:
        "Wh-What? Why? This doesn’t make any sense!":
            scene CR3_MS0_p3a

            MC "Wh-What? Why? This doesn’t make any sense!"
            if renpy.loadable("patch.rpy"):
                Caroline "It does. The only thing that DIDN’T make sense, was the fact that a sister was fooling around with her brother!"
            else:
                Caroline "It does. The only thing that DIDN’T make sense, was the fact that, I was fooling around with you!"
            MC "Please! Can’t we talk about this? I thought we might evolve into - something more than just a deal!"

            jump CR3_MS0_continue
        "Y-You can’t do this! We had a deal!":

            scene CR3_MS0_p3b

            MC "Y-You can’t do this, Caroline! We had a deal!"
            Caroline "Not anymore, [player_name]."
            MC "I thought we could be - more than just a deal! You can’t just tear that away from me!"
            jump CR3_MS0_continue

label CR3_MS0_continue:
    scene CR3_MS0_p4

    Caroline "*Sigh* We were never going to be - more than - just two people, fooling around."
    Caroline "I don’t need you to take pictures for me, anymore. I’ll be employing a part-time member of staff - as of tomorrow."
    MC "W-Wait..! Please, don’t do this!"
    MC "(Fuck! I’m feeling sick...)"

    scene CR3_MS0_p5

    Caroline "Please don’t make this any harder than it has to be, [player_name]."
    Caroline "We both had some fun, while it lasted, but there was no way we could have - realistically - made this a long-term thing. You must have known that?"
    MC "(This can’t be happening...)"

    scene CR3_MS0_p6

    MC "Please! I’ll do anything! We can slow things down!"
    Caroline "There was nothing to slow down, [player_name]. We were never dating."
    Caroline "I accept - full responsibility - for this. I really AM sorry - I never meant to hurt you, I was selfish and greedy. I should have just hired another member of staff, to help me run my business."

    scene CR3_MS0_p7

    MC "Caroline! Wait!"
    Caroline "Goodbye, [player_name]..."
    MC "(Oh fuck... Does this mean that I’ll never, be able to be with her again? It can’t, seriously be over, can it?!)"
    MC "(If I’d known that it was all going to end I would have cherished - every last second - with her. Now I’ve lost her forever...)"

    $ CR3_deal_aff = True
    $ CR3_MS0 = False
    $ CR3_MS2 = True
    $ CR3_AS1 = True
    $ CR3_ES1 = False
    $ CR3_MS2_can3 = False

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1
