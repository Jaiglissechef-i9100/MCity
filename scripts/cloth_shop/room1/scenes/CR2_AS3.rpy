image CR2_AS3_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS3/1.jpg"
image CR2_AS3_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS3/2.jpg"
image CR2_AS3_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS3/3.jpg"
image CR2_AS3_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS3/4.jpg"
image CR2_AS3_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS3/5.jpg"
image CR2_AS3_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS3/6.jpg"
image CR2_AS3_p7 = "images/cloth_shop/room1/day/scenes/CR2_AS3/7.jpg"

image CR2_AS3a_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/1.jpg"
image CR2_AS3a_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/2.jpg"
image CR2_AS3a_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/3.jpg"
image CR2_AS3a_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/4.jpg"
image CR2_AS3a_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/5.jpg"
image CR2_AS3a_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/6.jpg"
image CR2_AS3a_p7 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/7.jpg"
image CR2_AS3a_p8 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/8.jpg"

default CR2_AS3_clean1 = False
default CR2_AS3_clean2 = False
default CR2_AS3_clean3 = False
default CR2_AS3_clean4 = False
default CR2_AS3_clean5 = False
default CR2_AS3_clean6 = False
default CR2_AS3_clean7 = False
default CR2_AS3_clean_after = False

label CR2_AS3_clean_counter_label:
    $ CR2_AS3_clean_counter += 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_robber_screen

label CR2_AS3_clean_counter_label2:
    $ CR2_AS3_clean_counter += 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_room2_robbery_screen

label CR2_AS3_label:

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_AS3_p1 with dissolve
    $ can_hide_windows = True
    Caroline "*Sniff Sniff*"
    MC "(Huh?! Is she crying?)"
    MC "Caroline? Are you okay?"

    scene CR2_AS3_p2

    MC "(Jesus Christ! She’s crying her eyes out!)"
    MC "(What the hell happened!?)"
    MC "Hey, I’m here, Caroline. What’s wrong?"

    scene CR2_AS3_p3

    Caroline "It’s… *Sniff* It’s all gone…"
    MC "What’s all gone?"
    Caroline "My money… Some of my stock…"
    MC "Wait- You’re not saying-"
    Caroline "I got robbed!"

    scene CR2_AS3_p4

    MC "Shit! It’s okay... C’mere, Caroline."
    MC "(She’s shaking like a leaf in the wind!)"
    MC "(I have to do something to try and calm her down.)"

    scene CR2_AS3_p5

    MC "It’s gonna be okay, Caroline. Just sit and compose yourself there."
    MC "Let me take a look around the shop and I’ll see what I can salvage for you, okay?"
    Caroline "Y-You don’t have to d-do this…"
    MC "Nonsense. Just sit back and relax. Let me do the cleaning."

    scene CR2_AS3_p6

    Caroline "Are you sure?"
    MC "Honestly, just leave this to me. I’ll pack away anything and sort the furniture back into its proper place."
    Caroline "Thank you, [player_name]. You’re so sweet."

    scene CR2_AS3_p7

    MC "Do you have any idea who might have done this?"
    Caroline "I… uh… I’m not sure."
    MC "Tell you what - leave the cleaning to me. You report the robbery to the police, okay?"
    Caroline "O-Okay."
    $ can_map = False
    $ CR2_AS3_clean = True
    $ CR2_AS3 = False
    $ CR2_AS3a = True
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    scene cloth_shop_empty
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_robber_screen

label CR2_AS3a_label:
    if CR2_AS3_clean_counter <7:
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I have to clean up the mess here first."
        $ clickable = True
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        call screen cloth_shop_robber_screen
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        scene CR2_AS3a_p1 with dissolve
        $ can_hide_windows = True

        MC "Okay! That’s me done with the cleaning. Your shop is almost back to normal!"
        Caroline "Thank you so much, [player_name]. You’re really taking the stress off me."
        MC "I’m happy to help. We’ll get you through this."

        scene CR2_AS3a_p2

        MC "Have you had a chance to call the police?"
        Caroline "Yeah, I reported the crime and was given an incident number. The police don’t have anyone available right now to tackle a non-urgent crime scene, but they say they’ll be in touch."
        MC "Non-urgent?"

        scene CR2_AS3a_p3

        Caroline "Not enough money was stolen, and nobody was physically hurt. So, it’s not an urgent case for them."
        MC "Damn."
        Caroline "I still have no money and I don’t know where to begin fixing things..."

        scene CR2_AS3a_p4

        MC "It’s okay, Caroline. I’ll be with you, every step of the way."
        Caroline "You don’t need to do this. I know this is a job for you, but I… I’m not even paying you in cash."
        if renpy.loadable("patch.rpy"):
            MC "Your're my sister. I’ve told you this before - No matter what happens, I’ll be there to help you."
        else:
            MC "No matter what happens, I’ll be there to help you."

        scene CR2_AS3a_p5
        if renpy.loadable("patch.rpy"):
            Caroline "*Sniff* Thank you so much! You’re the best brother I could ever ask for."
        else:
            Caroline "*Sniff* Thank you so much! You’re the best friend I could ever ask for."
        MC "(It looks like I’ve cheered her up a bit!)"
        MC "(I shouldn’t rest now though - I’ll find this burglar and get revenge on them!)"

        scene CR2_AS3a_p6

        MC "(I don’t think Caroline thought this through when she decided to give me a hug.)"
        MC "(Oh well! I’m not gonna complain! The view is amazing!)"

        scene CR2_AS3a_p7

        Caroline "Thanks again, [player_name]."
        Caroline "I don’t know what I’d do without, you in my life."
        Caroline "You’re my biggest - my ONLY - source of support, right now."

        scene CR2_AS3a_p8

        MC "We’ll get through this together, Caroline."
        MC "We just need to take it one day at a time. You focus on getting your shop back up and running."
        MC "I’ll focus on the criminal side of things. Okay?"
        Caroline "Okay, but be careful."

        $ day_time = 3
        $ CR2_AS3a = False
        $ CR2_AS4 = True
        $ CR2_AS5 = True
        $ CR2_MS2 = True
        $ CR2_ES2 = True
        $ cloth_shop_minigame_unlocked = False
        $ CR2_MS1 = False
        $ CR2_ES1 = False
        $ sms2_fromC = True
        $ CR2_AS3_clean_after = True
        $ can_hide_windows = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump map_label
