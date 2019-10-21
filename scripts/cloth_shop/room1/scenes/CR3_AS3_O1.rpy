image CR3_AS3_O1_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/1.jpg"
image CR3_AS3_O1_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/2.jpg"
image CR3_AS3_O1_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/3.jpg"
image CR3_AS3_O1_p4 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/4.jpg"
image CR3_AS3_O1_p5 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/5.jpg"
image CR3_AS3_O1_p6 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/6.jpg"
image CR3_AS3_O1_p7 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/7.jpg"
image CR3_AS3_O1_p8 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/8.jpg"
image CR3_AS3_O1_p9 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/9.jpg"
image CR3_AS3_O1_p10 = "images/cloth_shop/room1/day/scenes/CR3_AS3_O1/10.jpg"

label CR3_AS3_O1:
    $ outfit_start = 1
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2,hard=True)
    $ can_hide_windows = True
    if C_R3_outfit1.t_played == 1:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

        scene CR3_AS3_O1_p1 with dissolve

        MC "(When Caroline told me that she had new costumes, for couples, I imagined that they were going to be - super sexy!)"
        MC "(What - even - is this thing?! I look like a damn bumblebee!)"
        Violet "Are you ready there, [player_name]?"
        MC "Yeah! Coming now!"

        scene CR3_AS3_O1_p2

        Violet "Okay everyone - let me set the stage, for you two. It’s a beautiful beach, on the USA’s West Coast, Golden sand, azure waves, sapphire skies-"
        Caroline "Yeah yeah, we get it. Can we just - cut to the chase?"
        Violet "Absolutely not! We’re doing this properly!"
        Caroline "*Sigh* (I knew there was a reason, why she wasn’t higher up my list of potential photographers.)"

        scene CR3_AS3_O1_p3

        Violet "The brave lifeguard, played by [player_name], is hanging out with his beautiful girlfriend, at the water’s edge. They embrace together, as the California sun sets behind them."
        Violet "I’m going to need you two to hug, and look lovingly into each others eyes. Can you do that for me?"
        Caroline "Don't you think you’re taking this, a little too seriously?"

        scene CR3_AS3_O1_p4

        Violet "Too seriously?! I am an ARTIST!"
        Violet "I spent FOUR YEARS in art school for a degree! This is the first time, I have EVER been able to put it to use!"
        Caroline "Ugh..! Fine! Let’s just get this over with..."
        MC "(I can see why Caroline didn't go to her first, when she was desperate for a photographer!)"

        scene CR3_AS3_O1_p5

        Caroline "Umm? How’s this?"
        Violet "No! No! No! Closer! You’re not making any effort to look like a couple! It just looks... awkward."
        Caroline "*Sigh* Sorry. Let me try again."

        scene CR3_AS3_O1_p6

        Caroline "(I can’t believe I’m doing this again... Hopefully Violet’s presence, will act as a restraint, on both of us doing - stupid stuff again.)"
        Caroline "(God... I can’t even look him in the eye, right now.)"
        Caroline "(His hands feel, so good, holding my body like that though...)"
        Violet "Could you raise your head a bit, Caroline?"

        scene CR3_AS3_O1_p7

        Violet "Yeah, just like that!"
        Violet "Hold it, right there! I’m gonna focus the camera lens, and we’ll be ready to shoot."
        Caroline "(I can feel - every single breath - he makes, against my skin.)"

        scene CR3_AS3_O1_p8

        MC "(Whispered) I’m sorry..."
        Caroline "Huh?"
        MC "(Whispered) I said I’m sorry. I know this - deal thing - didn’t work out for you. I kept asking about it and pushing it. I should have just let it go."

        scene CR3_AS3_O1_p9
        if renpy.loadable("patch.rpy"):
            MC "(Whispered) You’re my sister, and I would never want to hurt you or drive you away. I’m gonna miss what we had - every single day - for the rest of my life, but that would - pale in comparison - to the pain of losing you as a sister."
        else:
            MC "(Whispered) You’re my friend, and I would never want to hurt you or drive you away. I’m gonna miss what we had - every single day - for the rest of my life, but that would - pale in comparison - to the pain of losing you as a friend."
        Caroline "..."
        Caroline "(Whispered) Shut up, you bastard... You’re gonna make me cry on camera."

        scene CR3_AS3_O1_p10

        Violet "Okay, you two - that’s me ready!"
        Violet "Let’s see you strike a pose!"
        $ CR3_AS5_can += 1
        $ outfit_box.drop_outfit(C_R3_outfit2_loc)
        $ outfit_box.add_outfit(C_R3_outfit2)

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump outfit_R3_start
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump outfit_R3_start