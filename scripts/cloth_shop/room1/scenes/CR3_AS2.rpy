image CR3_AS2_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS2/1.jpg"
image CR3_AS2_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS2/2.jpg"
image CR3_AS2_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS2/3.jpg"

default CR3_AS2_first_talk = True

label CR3_AS2_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if CR3_AS2_first_talk == True:
        scene CR3_AS2_p1 with dissolve

        Violet "So then, I said to him, I know this trick. You deliberately forget the condom, and then you ask for - just the tip to go in. I mean, how naive does he think I am?"
        Caroline "What did you do?"
        Violet "Ugh..! He ended up saying, he’d just put the tip in, for a second. Then I got too horny, to tell him to take it out. Thank God, I was on my birth control."
        Caroline "Aww, that’s always how it is. The trick is to not let them get inside you. Don’t give guys an inch, or they’ll take a mile."
        $ CR3_AS2_first_talk = False

    scene CR3_AS2_p2

    MC "Hey, guys!"
    Caroline "Oh hey! We were just waiting for you. We’re ready to go, whenever you are."
    MC "Great! Let’s get changed."

    scene CR3_AS2_p3

    if CR3_deal_aff == True:
        scene CR3_AS2_p3
        Violet "Umm... before we begin. I have a degree in art - but I’m not entirely sure, what kinda of pictures Caroline is looking for. She told me that you’d helped her out, in the past. Could you maybe help me, direct the camera shots?"
        MC "Sure, Violet! Happy to help."
        Caroline "Alright... I guess we’re ready to start, whenever you are... *Gulp*"
        MC "(She seems a little hesitant and nervous. It’s probably, the fact that we’ll be really close to each other, when we’re taking the pictures.)"

        menu:
            "I’m ready to start.":
                jump cosplay_CR3_label
            "I need a few more minutes, to prepare myself.":

                MC "I need a few more minutes, to prepare myself."
                Caroline "Take your time. Violet and I can always work on other stuff, while we’re waiting for you."

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump cloth_shop_open_label

    if CR3_deal_aff == False:
        scene CR3_AS2_p2

        Caroline "Glad you could make it! Are you ready for the photoshoot?"
        MC "(She looks a little happier, this time - Even eager, maybe! Perhaps this is because the deal is back on, between us.)"

        menu:
            "I’m ready to start.":
                jump cosplay_CR3_label
            "I need a few more minutes to prepare myself.":

                MC "I need a few more minutes to prepare myself."
                Caroline "Take your time, Violet and I can always work on other stuff while we’re waiting for you."

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump cloth_shop_open_label
