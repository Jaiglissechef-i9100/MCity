image sara_room_evening_scene3_v1_p1 = "images/home/sara_room/evening/scene3_v1/1.jpg"
image sara_room_evening_scene3_v1_p2 = "images/home/sara_room/evening/scene3_v1/2.jpg"
image sara_room_evening_scene3_v1_p3 = "images/home/sara_room/evening/scene3_v1/3.jpg"
image sara_room_evening_scene3_v1_p4 = "images/home/sara_room/evening/scene3_v1/4.jpg"
image sara_room_evening_scene3_v1_p5 = "images/home/sara_room/evening/scene3_v1/5.jpg"
image sara_room_evening_scene3_v1_p6 = "images/home/sara_room/evening/scene3_v1/6.jpg"
image sara_room_evening_scene3_v1_p7 = "images/home/sara_room/evening/scene3_v1/7.jpg"
image sara_room_evening_scene3_v1_p7a = "images/home/sara_room/evening/scene3_v1/7a.jpg"
image sara_room_evening_scene3_v1_p8 = "images/home/sara_room/evening/scene3_v1/8.jpg"
image sara_room_evening_scene3_v1_p9 = "images/home/sara_room/evening/scene3_v1/9.jpg"
image sara_room_evening_scene3_v1_p10 = "images/home/sara_room/evening/scene3_v1/10.jpg"
image sara_room_evening_scene3_v1_p11 = "images/home/sara_room/evening/scene3_v1/11.jpg"
image sara_room_evening_scene3_v1_p12 = "images/home/sara_room/evening/scene3_v1/12.jpg"
image sara_room_evening_scene3_v1_p13 = "images/home/sara_room/evening/scene3_v1/13.jpg"
image sara_room_evening_scene3_v1_p14 = "images/home/sara_room/evening/scene3_v1/14.jpg"
image sara_room_evening_scene3_v1_p15 = "images/home/sara_room/evening/scene3_v1/15.jpg"
image sara_room_evening_scene3_v1_p16 = "images/home/sara_room/evening/scene3_v1/16.jpg"
image sara_room_evening_scene3_v1_p17 = "images/home/sara_room/evening/scene3_v1/17.jpg"


transform pandown1:
    crop (0, 1080, 1920, 2160)
    linear 2 crop (0, 0, 1920, 2160)


label sis_nerdy_evening_scene2a_v1_label:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0:

        scene sara_room_evening_scene2_v1_p1 with dissolve
        MC "Hi Sara, are you-"
        Sara "Oh hey! Just let me pause, [player_name]."

        scene sara_room_evening_scene2_v1_p2
        Sara "Are you looking for a rematch?"
        Sara "Whaddya say? Same rules? Each time you die you lose a piece of clothing?"
        MC "(If I accept, she’ll just kick my ass again… I need to find a way to guarantee that I win.)"
        MC "Nah, not today. Enjoy the rest of your match!"

        scene sara_room_evening_scene2_v1_p1
        Sara "Your loss! See ya later!"

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_sis_nerdy_gamepad_change = 1
        $ can_sis_nerdy_evening_scene1_v1 == False
        jump sister_nerdy_morning1
    if can_sis_nerdy_evening_scene1_v1 == False:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "I've already talked to her."
        jump sister_nerdy_morning1
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 1:

        scene sara_room_evening_scene3_v1_p1 with dissolve
        Sara "I said flank left! That’s the right flank, you dumbos!"
        MC "(Wow, looks like Sara’s teammates aren’t up to scratch today!)"
        Sara "Grr! We lost the match because of you guys! I’m off now. Chat later!"

        scene sara_room_evening_scene3_v1_p2
        Sara "Oh! Hey, [player_name]! Didn’t see you standing there. Do you fancy a rematch?"
        MC "(I’ve swapped the working controller for the cheap Chinese knock-off version! This should give me the edge I need to beat her!)"
        MC "Yeah, I’m ready whenever you are!"

        scene sara_room_evening_scene3_v1_p3
        Sara "Sweet! Let me get it set up here."
        Sara "Do you want to play Street Brawler VII again? Or something else this time?"
        MC "Street Brawler works for me."
        Sara "Coolio!"


        scene sara_room_evening_scene3_v1_p4
        Sara "Hehe - you do know you’re gonna lose again, right?"
        MC "Perhaps."
        Sara "And you know the penalty for losing?"
        MC "I lose a piece of clothing."
        Sara "Yup! Now let’s get started!"


        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Three Minutes Later…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        Console "FATALITY!"
        scene sara_room_evening_scene3_v1_p5
        Sara "Wh-What?! N-No way!"
        MC "That’s one-nil, Sara! Time to lose a piece of clothing."

        scene sara_room_evening_scene3_v1_p6
        Sara "B-But I’m n-not wearing a bra…"
        MC "Then lose your denim shorts."
        Sara "I… I’m not w-wearing any… *ahem* either…"
        MC "You’re not wearing ANY underwear?"
        Sara "Look away while I take my top off…"

        scene sara_room_evening_scene3_v1_p7
        MC "Fine."

        menu:
            "Sneak a peek while she is taking her top off.":
                window hide
                scene sara_room_evening_scene3_v1_p7a at pandown1
                $ renpy.pause(2.0, hard=True)
                MC "(Holy shit! She’s so fucking hot!)"
                Sara "(I can’t believe this… it’s so embarrassing!)"
                Sara "(Why didn’t I wear any underwear?! I was sooo confident that I was going to win again!)"
                MC "(Hehe - this broken controller is working like a charm! She doesn’t know what the hell is going on!)"
                jump after_choice_sis_nerdy_evening_scene3
            "Be nice and let Sara undress without peeking.":


                scene sara_room_evening_scene3_v1_p7
                MC "Fine, I won’t look."
                Sara "Thank you…"
                MC "Are you done yet?"
                Sara "Almost..."
                jump after_choice_sis_nerdy_evening_scene3

label after_choice_sis_nerdy_evening_scene3:

    scene sara_room_evening_scene3_v1_p8
    MC "(Her nipples are pretty stiff! She must be secretly enjoying this!)"
    Console "ROUND 2! FIGHT!"
    Sara "I’m gonna beat your ass this time!"
    MC "Oh yeah? You really think so?"
    Sara "Dammit! I pressed X three times! Why didn’t it work?!"
    Console "C-C-COMBO BREAKER!"

    scene sara_room_evening_scene3_v1_p9
    Console "FATALITY! PLAYER 2 WINS AGAIN!"
    Sara "NOOOOOOO!"
    MC "Yesss!"
    Sara "N-No way! This c-can’t be happening!"
    MC "You know the rules, Sara! Time to lose those denim shorts!"
    MC "Or… you could just lose your shoes."

    scene sara_room_evening_scene3_v1_p10
    MC "Actually! Let’s make a deal - one more round. Sudden death rules."
    Sara "What do you mean?"
    MC "If you win, I take off EVERYTHING. If I win though… then you have to strip completely naked for me."
    MC "Deal?"
    Sara "… Deal."

    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    "(Thirty seconds later…)"
    $ renpy.pause(2.0)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    scene sara_room_evening_scene3_v1_p11
    Sara "AAAAAAHHHHHHH!!!"
    Sara "(WHAT’S HAPPENING?! Why aren’t I good at video games anymore?!)"
    MC "You lost the deal, Sara. Time to strip off!"

    scene sara_room_evening_scene3_v1_p12
    Sara "Ugh… Fine. I’ll do it on the bed."
    Sara "N-No photos though!"
    MC "That’s a bit hypocritical of you!"
    Sara "I… I don’t have that picture anymore. I… um… deleted it!"
    MC "(She’s lying… She definitely still has that picture of my dick!)"

    scene sara_room_evening_scene3_v1_p13
    MC "Fine, no photos. But I still want to see your whole body."
    Sara "(Gulp) S-Sure."
    Sara "(I can’t believe I lost… I thought this would just be an easy way to see [player_name]’s cock again.)"
    Sara "(God… what am I going to tell Lily if she asks what happend?!)"

    scene sara_room_evening_scene3_v1_p14
    MC "(Wow! There’s her pussy! I can see the hood of her clitoris, poking out the top.)"
    MC "(She wasn’t lying when she said she wasn’t wearing any panties. Was she seriously THAT confident that she was going to win?! Haha!)"
    Sara "W-Well? I-Is this enough?"

    scene sara_room_evening_scene3_v1_p15
    MC "We did agree, completely naked - but this is a rather sexy view."
    Sara "S-Sexy?"
    MC "I’m just teasing you."

    scene sara_room_evening_scene3_v1_p16
    Sara "W-Wait - You can’t just s-say something like that and walk away…"
    MC "Huh?"
    Sara "D… Do… you think I’m pretty?"

    scene sara_room_evening_scene3_v1_p17
    MC "Of course you’re pretty. I’d hardly be playing strip challenge games with you if you weren’t!"
    Sara "I… I guess…"
    MC "Anyway, I’ll let you get dressed again. See you later, Sara."
    MC "And for the record, you are very pretty."
    Sara "Th… Thank you..."
    $ day_time +=1
    $ sis_nerdy_evening_scene2a_v1 = 3
    $ sis_nerdy_evening_scene1_v1 = 1
    $ can2_mc_sara_night_scene1_v1 = True
    $ can1_sis_nerdy_school_scene3_v1 = True
    $ sis_nerdy_evening_scene1_v1 = 3
    $ can_lily_scene = False
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump corridor_night1

label sis_nerdy_evening_gamepad_change_scene3_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "I can't do it while she's around."
        jump sister_nerdy_evening1
    else:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "That’s her controller. What should I do with it to win next time?"
    jump sister_nerdy_evening1


label sis_nerdy_evening_gamepad_change_scene3_v1_label_can:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = False
    if day_time == 1:
        show screen sister_nerdy_morning_notclickable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Gamepad changed."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "That’s her controller. What should I do with it to win next time?"
            jump sister_nerdy_morning1
    if day_time == 2:
        show screen sister_nerdy_day_notclickable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Gamepad changed."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "That’s her controller. What should I do with it to win next time?"
            jump sister_nerdy_morning1

    if day_time == 4:
        show screen sister_nerdy_night_notclikcable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Gamepad changed."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "That’s her controller. What should I do with it to win next time?"
            jump sister_nerdy_morning1