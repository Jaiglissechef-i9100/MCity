image CR3_AS4_O2_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/1.jpg"
image CR3_AS4_O2_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/2.jpg"
image CR3_AS4_O2_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/3.jpg"
image CR3_AS4_O2_p4 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/4.jpg"
image CR3_AS4_O2_p5 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/5.jpg"
image CR3_AS4_O2_p6 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/6.jpg"
image CR3_AS4_O2_p7 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/7.jpg"
image CR3_AS4_O2_p8 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/8.jpg"
image CR3_AS4_O2_p9 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/9.jpg"
image CR3_AS4_O2_p10 = "images/cloth_shop/room1/day/scenes/CR3_AS4_O2/10.jpg"


label CR3_AS4_O2:
    $ outfit_start = 2
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2,hard=True)
    $ can_hide_windows = True
    if C_R3_outfit2.t_played == 1:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

        scene CR3_AS4_O2_p1 with dissolve

        MC "(Is this supposed to be one of those British school uniforms?)"
        MC "(I’m not even sure if I’ve got this, damn tie - done up - properly...)"
        Violet "Stop! Don’t pull it up, any further - just leave your tie like that."
        MC "Are you sure?"
        Violet "Yeah. It gives you that - delinquent schoolboy - look! That’s EXACTLY what we’re looking for."
        Violet "Caroline! Are you almost ready? I need my - naughty teacher - out here!"

        scene CR3_AS4_O2_p2

        Caroline "I’m coming! I’m coming!"
        Caroline "(Jesus Christ! Has Violet forgotten, that I’m supposed to be HER boss?!)"
        Violet "Perfect! Okay, if you two could just approach each other - just like the lifeguard scene, from last time."
        MC "(Holy shit! Caroline was right when she said, these new clothes were too tight for her! I can see the edges of her areolas! I wonder if she’s even noticed that?)"

        scene CR3_AS4_O2_p3

        Violet "Okay - good. Hmm... How can I set the scene?"
        MC "(Whispered) Wow... You look stunning, Caroline."
        Caroline "(Whispered) I wish... This damn outfit, makes my ass look fat."
        MC "(Whispered) It wasn’t your ass, I was looking at."
        Caroline "What?!"

        scene CR3_AS4_O2_p4

        Violet "Okay, I’ve got it! This delinquent schoolboy hadn’t been doing his homework properly."
        Violet "The seductive teacher comes up with a plan to reward him. For every A he gets - she will give him a naughty prize. He just got his first A today - so she is rubbing her ass, up against his pants!"
        Violet "Hurry up! Get in your places, people!"

        scene CR3_AS4_O2_p5

        Caroline "*Sigh* Just like this?"
        Violet "Can you bend over, just a little bit more? Keep your head, looking up at me. I want to see your eyes, in the picture."
        MC "(Heh. I’ve got quite the view now!)"

        scene CR3_AS4_O2_p6

        MC "(Maybe Caroline was right, her ass DOES look big in this dress - but I don’t see how that’s a bad thing!)"
        MC "(I’ll just enjoy her, rubbing up against me for a while.)"
        Violet "[player_name], I need you to put your hands up, on Caroline’s hips. Actually, go a little higher than her hips. Wrap them around her belly."

        scene CR3_AS4_O2_p7

        MC "How’s this?"
        Violet "Absolutely perfect!"
        MC "(Damn, I can feel myself starting to get hard... Hopefully, Caroline will be too focused on the photoshoot, to notice.)"

        scene CR3_AS4_O2_p8

        Caroline "(Oh, my God… Is [player_name] getting an erection, right now?!)"
        Caroline "(He IS! I can feel it poking at my ass! Dammit! I can’t say a word, without Violet finding out... If she hears about this, she’ll never stop tormenting me about it.)"
        Caroline "(On the other hand, it doesn't exactly feel... bad? I mean, I could just endure it, for a few more minutes.)"

        scene CR3_AS4_O2_p9
        if persistent.incest_patch == True:
            Caroline "(What the hell am I thinking?! OF COURSE it is bad! He’s my little brother!)"
        else:
            Caroline "(What the hell am I thinking?! OF COURSE it is bad!)"
        Caroline "(Whispered) Umm... You couldn’t... move your hips a little bit, could you? I think there might be a... pen or something, in your pocket."
        MC "(Whispered) Oops! Sorry - I’ll do that now."
        MC "(Damn, I think she might have felt my erection...)"

        scene CR3_AS4_O2_p10

        Violet "Annnnnd.... Showtime!"
        Violet "Hold that position, guys! We are good to start!"
        $ CR3_AS5_can += 1

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump outfit_R3_start
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump outfit_R3_start

