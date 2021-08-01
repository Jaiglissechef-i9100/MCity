image CR4_AS1_p1 = "images/cloth_shop/room1/day/scenes/CR4_AS1/1.jpg"
image CR4_AS1_p2 = "images/cloth_shop/room1/day/scenes/CR4_AS1/2.jpg"
image CR4_AS1_p3 = "images/cloth_shop/room1/day/scenes/CR4_AS1/3.jpg"
image CR4_AS1_p4 = "images/cloth_shop/room1/day/scenes/CR4_AS1/4.jpg"
image CR4_AS1_p5 = "images/cloth_shop/room1/day/scenes/CR4_AS1/5.jpg"
image CR4_AS1_p6 = "images/cloth_shop/room1/day/scenes/CR4_AS1/6.jpg"
image CR4_AS1_p7 = "images/cloth_shop/room1/day/scenes/CR4_AS1/7.jpg"
image CR4_AS1_p8 = "images/cloth_shop/room1/day/scenes/CR4_AS1/8.jpg"
image CR4_AS1_p9 = "images/cloth_shop/room1/day/scenes/CR4_AS1/9.jpg"
image CR4_AS1_p10 = "images/cloth_shop/room1/day/scenes/CR4_AS1/10.jpg"
image CR4_AS1_p11 = "images/cloth_shop/room1/day/scenes/CR4_AS1/11.jpg"
default CR4_AS1 = False
default CR4_NS1 = False
label CR4_AS1_label:
    if renpy.loadable("patch.rpy"):
        $ Bob_name = "Dad"
        $ Linda_name = "Mom"
    else:
        $ Bob_name = "Bob"
        $ Linda_name = "Linda"
    if CR4_AS1 == 2:
        hide screen map_button
        show screen cloth_shop_room2_robbery_screen
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen cloth_shop_room2_robbery_screen
        jump cloth_shop_room2_label
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene CR4_AS1_p1 with dissolve

        Caroline "Hey there, handsome! Glad you could make it!"
        MC "Hey, Caroline! Did you honestly doubt that I would come?"
        Caroline "Nah, I’m just teasing you."

        scene CR4_AS1_p2

        Caroline "Can I get you something to drink? A tea? Maybe a coffee?"

        MC "Sure, I’ll take a coffee if you’re having one."
        Caroline "Great! I’ll put the kettle on."

        scene CR4_AS1_p3

        Caroline "I’ll close the shop up for fifteen minutes. Go ahead into the staff room. I’ll see you back there."
        MC "Are you not worried about losing customers?"
        Caroline "Pfft! If my shop can’t survive a fifteen minute break then I must be running a very shoddy business. I’ll be fine!"

        $ renpy.music.stop(channel="music1", fadeout=1)
        scene black with dissolve
        $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
        $ renpy.pause(1.5, hard = True)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene CR4_AS1_p4 with dissolve

        Caroline "Be careful with that coffee - it’s scalding!"
        MC "And still not as hot as you are!"
        Caroline "Very funny! Do you need any sugar?"
        MC "I’ll be fine thanks, Caroline."

        scene CR4_AS1_p5

        Caroline "So, you’re here to plan our date with me, aren't you?"
        MC "Yeah, I was thinking of-"
        Caroline "Before you get carried away, I actually had an idea that I think you’ll REALLY like!"

        scene CR4_AS1_p6

        MC "Oh yeah?"
        Caroline "So, do you remember where we had our first kiss?"
        MC "(That was the time we made out by the lake in the park!)"
        MC "Yeah, that was-"

        scene CR4_AS1_p7

        Caroline "No need to check with me - I hope you remembered."
        MC "Yeah, I do. Are we meeting there?"
        Caroline "Yup. I thought that would be a nice place to start everything together. What do you think?"

        scene CR4_AS1_p8

        MC "It sounds like a lovely idea. What time do you want to meet?"
        Caroline "Let’s meet at night. After [Linda_name], [Bob_name], and [Sara_name] have all gone to bed. It means we won’t be disturbed."
        MC "Great, it’s a date!"

        scene CR4_AS1_p9

        MC "*Slurp*"
        Caroline "(I really hope he remembers where our first kiss was… If he doesn’t remember he's clearly just another asshole like Charles.)"
        Caroline "(I wonder what he’s thinking about right now. He’s probably trying to remember the exact place we kissed to make sure he doesn’t fuck this up.)"
        Caroline "(God… I wish I could read guys’ minds.)"

        scene CR4_AS1_p10

        MC "*Slurp*"
        MC "(I wonder when the next version of DefinitelyNotRelatedPeopleFucking comes out on Patreon. That game feels like it’s been on v0.04 for YEARS now!)"

        scene CR4_AS1_p11

        Caroline "Anyway, I better get the shop opened up again. I’ll see you tonight."
        MC "I’m looking forward to it, [Caroline_name]. I’ll see you at the school gates tonight."

        scene CR4_AS1_p6

        Caroline "Wait- the school gates?!"
        Caroline "(Does this dickhead think our first time was making out in front of his school?!)"
        MC "Haha! I’m kidding - sorry, I couldn’t resist. I know that’s not where we had our first kiss."

        scene CR4_AS1_p11

        Caroline "Ahaha, you’re awful!"
        MC "Haha, I’ll let you get back to work. I’ll see you tonight at the actual spot where we first kissed!"
        Caroline "See you then, [player_name]."

        $ CR4_AS1 = 2
        $ CR4_NS1 = True
        $ C_NS_locked = True
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump cloth_shop_room2_label