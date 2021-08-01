image mc_sara_night_scene1_v1_p1 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/1.jpg"
image mc_sara_night_scene1_v1_p2 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/2.jpg"
image mc_sara_night_scene1_v1_p3 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/3.jpg"
image mc_sara_night_scene1_v1_p4 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/4.jpg"
image mc_sara_night_scene1_v1_p5 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/5.jpg"
image mc_sara_night_scene1_v1_p6 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/6.jpg"
image mc_sara_night_scene1_v1_p7 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/7.jpg"
image mc_sara_night_scene1_v1_p8 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/8.jpg"
image mc_sara_night_scene1_v1_p9 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/9.jpg"
image mc_sara_night_scene1_v1_p10 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/10.jpg"
image mc_sara_night_scene1_v1_p11 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/11.jpg"
image mc_sara_night_scene1_v1_p12 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/12.jpg"
image mc_sara_night_scene1_v1_p13 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/13.jpg"
image mc_sara_night_scene1_v1_p14 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/14.jpg"
image mc_sara_night_scene1_v1_p15 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/15.jpg"
image mc_sara_night_scene1_v1_p16a = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/16a.jpg"
image mc_sara_night_scene1_v1_p17 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/17.jpg"
image mc_sara_night_scene1_v1_p18 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/18.jpg"
image mc_sara_night_scene1_v1_p19 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/19.jpg"

label mc_sara_night_scene1_v1_label:
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen mc_room_morning_notclickable
    hide screen mc_room_day_notclickable
    hide screen mc_room_night_notclickable
    hide screen mc_room_evening_notclickable
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "…"
    Sara "(I wonder if he’s definitely asleep.)"
    Sara "[player_name]? Are you up?"
    MC "…"

    scene mc_sara_night_scene1_v1_p2
    Sara "(Okay, you can do this, Sara. Be brave!)"
    Sara "(You have to get this picture of his cock, for Lily.)"
    Sara "(Then you can prove that you’re one of the cool kids, and not just a nerdy virgin!)"

    scene mc_sara_night_scene1_v1_p3
    Sara "(Hey, this is easier than I thought it would be! He’s only in his boxer shorts!)"
    Sara "(I just need to strip these off him, then start moving his cock until it gets, all stiff and hard…)"
    Sara "(...like that time in my bedroom, when he pressed it up against my belly.)"

    scene mc_sara_night_scene1_v1_p4
    Sara "(Wow… It always takes my breath away, each time I see it!)"
    Sara "(It feels like there’s a hundred tiny butterflies in my belly right now!)"
    Sara "(I don’t think I even need to move his cock at all… it’s already quite stiff!)"

    scene mc_sara_night_scene1_v1_p5
    Sara "(I’ll just take a quick picture of it, then sneak out of his bedroom.)"
    Sara "([player_name] won’t even know I was in here! Haha! Perfect!)"
    Sara "(On the other hand… maybe I could touch his cock, just a little bit…)"

    scene mc_sara_night_scene1_v1_p6
    Sara "(Yeah, I should rub it a bit - just to get a better picture, of course.)"
    Sara "(Wow… it’s getting so much bigger and harder!)"
    Sara "(I wonder how long I should do this for?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p7
    MC "Boo!"
    Sara "EEEKKK!"
    Sara "(AHHH! He woke up!)"

    scene mc_sara_night_scene1_v1_p8
    Sara "I- I- *Sniff* I’m s-so sorry!"
    MC "What are you doing?"
    Sara "I was… I was… *sob* t-trying to take a… picture…"
    MC "Don’t you already have one on your phone?"

    scene mc_sara_night_scene1_v1_p9
    Sara "I… wanted another…"
    Sara "Please forgive me. I’m sooo sorry! *Sob*"
    if persistent.incest_patch == True:
        Sara "I’ll- I’ll do anything! Just don’t tell Dad!"

        scene mc_sara_night_scene1_v1_p10
        MC "Hey - relax. I won’t tell Dad."
    else:
        Sara "I’ll- I’ll do anything! Just don’t tell Bob!"

        scene mc_sara_night_scene1_v1_p10
        MC "Hey - relax. I won’t tell Bob."
    Sara "Th-Thank you. *Sniff* I’ll do anything for you."
    Sara "O-Or to you!"

    scene mc_sara_night_scene1_v1_p11
    MC "Come on into bed and sleep beside me tonight."
    Sara "Th...that’s all?"
    MC "Yeah, come on in beside me. It’s warm under the covers."

    scene mc_sara_night_scene1_v1_p12
    Sara "Th...thank you… I’m so sorry. *Sniff*"
    MC "Hey - it’s alright. Dry your eyes. Try to breathe."
    MC "If you were THAT desperate for a picture of my junk, you could have just asked."

    scene mc_sara_night_scene1_v1_p13
    Sara "Hehe… You always make me laugh so easily…"
    MC "That’s better. Let’s get rid of those tears."
    MC "I’ll shuffle over here, so there’s room for you."

    scene mc_sara_night_scene1_v1_p14
    Sara "Thanks, [player_name]..."
    MC "You still look a little stressed. Is everything alright?"
    Sara "Actually… I wanted to ask you something..."

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)
    scene mc_sara_night_scene1_v1_p15
    Sara "D...Do you… like me?"
    Sara "B-Because after everything that happened - with the videogames, Lily, you.. and me..."
    Sara "Y-you said.. I’m nice.. s-sexy..."
    Sara "I… I just need to know…"

    menu:
        "Yes, Sara. I really like you.":

            Sara "(Please say yes…)"
            MC "Yes, Sara. I really like you."
            scene mc_sara_night_scene1_v1_p16a
            MC "Honestly, I thought it would have been pretty obvious."
            Sara "(Oh, my God!)"

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "I- I- I can’t believe I just asked you that. G-Go back to sleep."
            Sara "Forget what I just said!"
            if persistent.incest_patch == True:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your brother!)"
            else:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! )"
            MC "(Huh?! Women are strange…)"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice
        "Stay silent.":

            scene mc_sara_night_scene1_v1_p17
            if persistent.incest_patch == True:
                Sara "Because I think I like you… more than a brother..."
            else:
                Sara "Because I think I like you… more than a friend..."
            MC "…"
            Sara "(Please say yes…)"
            MC "…"
            Sara "(Please, [player_name]… say anything...)"
            MC "…"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "N-Nevermind! I- Forget I asked you about it!"
            if persistent.incest_patch == True:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your brother!)"
            else:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your friend!)"
            Sara "(You shouldn’t have put him in that position! You could ruin your relationship with him!)"
            MC "Are you okay, Sara?"
            Sara "J-Just go to sleep, you b-big dumbo!"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice

label after_mc_sara_night_scene1_v1_choice:

    scene mc_sara_night_scene1_v1_p19
    MC "(YAWN!)"
    MC "(Looks like Sara left during the night. I wonder when she snuck out. I’ll probably see her around school today anyway.)"
    MC "(I’ve never seen her that emotional before.)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ mc_sara_night_scene1_v1 = 3
    $ can1_mc_sara_night_scene1_v1 = False
    $ can2_mc_sara_night_scene1_v1 = False
    $ can2_sis_nerdy_school_scene3_v1 = True
    $ sis_nerdy_school_scene3_v1 = 1
    $ can_lily_scene = False

    $ can_ml_work_day_scene1 = True
    $ can_school_intercom = True
    $ next_day = True
    $ next_day_sister_nerdy_scene4_v1 = True
    $ can_sis_nerdy_school_scene1_v1 = True
    $ can2_sis_nerdy_school_scene1_v1 = True
    $ can_sis_nerdy_evening_scene1_v1 = True
    $ can_sis_nerdy_night_sleeping1_v1 = True
    $ can_lily_work_in_progress = True
    $ sara_door_open = True
    $ can_celia_school_morning_scene1v1 = True
    $ ml_can_salon_morning_scene = True
    $ ml_can_salon_morning_scene2 = True
    $ ml_can_salon_morning_scene_dish_wash = False
    $ ml_can_kitchen_morning_scene4 = True
    $ ml_can_bedroom_morning_scene5 = True
    $ ml_can_evening_bathroom_scene_v1 = True
    $ ml_can_ml_and_f_bedroom_night_scene_v1 = True
    $ d__can_ml_and_f_bedroom_mornig_scene = True
    $ caroline_can_room_morning_scenes = True
    $ caroline_can_door_locked = True
    $ caroline_room_can_night_scene1 = True
    $ caroline_salon_can_evening_scene1 = True
    $ caroline_mc_room_can_evening_scene3 = True
    $ can_sara_scene3_v1 = True
    $ can_caroline_morning_scene4_after = False
    $ can_toilet_after_sara_scene4_1 = True
    $ can_ml_work_day_scene2 = True
    $ can_celia_morning_school_work_in_pr = True

    if can_CR2_MS1 == False:
        $ CR2_MS1  = False

    if can_CR2_MS2 == False:
        $ CR2_MS2  = False
        $ CR2_MS3 = True
        $ can_CR2_MS2 = True

    if can_CR2_MS3a == True:
        $ CR2_MS3a = True
        $ can_CR2_MS3a = False

    if can_CR2_ES1_day2 == True and CR2_ES1_day2_firsttime == True:
        $ CR2_ES1_day = 2

    if can_CR2_ES1_day3 == True and CR2_ES1_day3_firsttime == True:
        $ CR2_ES1_day = 3

    if can_CR2_ES2_day2 == True and CR2_ES2_day2_firsttime == True:
        $ CR2_ES2_day = 2

    if can_CR2_ES2_day3 == True and CR2_ES2_day3_firsttime == True:
        $ CR2_ES2_day = 3
    if CR2_NS3 == True:
        $ CR2_NS3 = False
    $ can_Bob_work_minigame = True
    $ can_CR2_ES2 = True
    $ can_CR2_ES1 = True
    $ can_MLR2_MS1_talk = True
    $ can_MLR2_MS1_kiss = True
    $ can_ml_workR2 = True
    $ can_MLR2_ES2 = True
    $ MLR2_Sleep = True
    $ can_B2_AS1_day = True
    $ MLR2_can_MS1 = True
    if can_Zv2_MS2_q == True and can2_Zv2_MS2_q == True:

        $ Zv2_MS2_q5 = True
        $ Zv2_MS2_q6 = True
        $ Zv2_MS2_q7 = True
        $ can2_Zv2_MS2_q = False
    if Zv2_ES4 == 1:
        $ Zv2_ES4_counter += 1
        if Zv2_ES4_counter == 3:
            $ Zv2_ES4 = True
            $ Bobv2_MS1_q5 = True
            if Zv2_lie_counter > 1:
                $ sms1_fromZuri = True
                $ company_profit = 2
            if Zv2_true_counter > 1:
                $ sms2_fromZuri = True
                $ company_profit = 1

    $ can_SR2_MS2 = True
    $ SR2_bath = False

    $ LiR1_poll_minigame_can = True
    $ can_LiR1_NS = True
    $ can_LiR1_NS3 = True
    if LiR1_MAS2 == True:
        $ can_LiR1_MAS2 = True
        $ Li_door_locked = False
        $ LiR1_key = True
        if Li_MAS2_menu_visit == 2:
            $ Li_MAS2_q4 = True
            $ Li_MAS2_q5 = True
            $ Li_MAS2_q6 = True

        if Li_MAS2_menu_visit == 3:
            $ Li_MAS2_q7 = True
            $ Li_MAS2_q8 = True

    if LiR1_MAS3 == True:
        $ can_LiR1_MAS3 = True
        if Li_MAS3_menu_visit == 2:
            $ Li_MAS3_q4 = True
            $ Li_MAS3_q5 = True
            $ Li_MAS3_q6 = True

        if Li_MAS3_menu_visit == 3:
            $ Li_MAS3_q7 = True
            $ Li_MAS3_q8 = True
            $ Li_MAS3_q9 = True

    if Li_MAS3_menu_visit >= 2 and Li_MAS2_menu_visit >= 2 and LiR1_MAS4 == 0:
        $ LiR1_MAS4 = True

    if LiR1_MAS5_can1 == True and LiR1_MAS5_can2 == True and clean_loop >1:
        $ LiR1_MAS5 = True
        $ LiR1_MAS3 = False

    if LiR1_MAS6_can1 == True:
        $ LiR1_MAS6 = True
        $ LiR1_MAS2 = False
        $ a_pool_empty = False

    if LiR1_MAS7_can1 == True and LiR1_MAS7_can2 == True:
        $ LiR1_MAS7 = True
        $ LiR1_MAS2 = False
        $ LiR1_MAS3 = False

    if LiR1_MAS8_can1 == True:

        $ LiR1_MAS3 = False
        $ LiR1_MAS2 = False
        $ LiR1_MAS8 = True
    $ can2_LiR1_NS = True

    if CR3_MS2_can == True and CR3_deal_aff == True:
        $ CR3_MS1 = False
        $ CR3_MS2 = True

    if CR3_MS1_can == True and CR3_deal_aff == True:
        $ CR3_MS1 = True
    if CR3_MS1_can == 3:

        $ CR3_MS1_q4 = True
        $ CR3_MS1_q5 = True
        $ CR3_MS1_q6 = True
        $ CR3_MS1_can = False

    if celia_school_morning_scene2v1 == 1 and can1_celia_school_morning_scene2v1 == True:
        $ can1_celia_school_morning_scene2v1 = False
        $ celia_school_morning_scene1v1 = 1
        $ celia_school_morning_scene2v1 = 0
    if celia_school_morning_scene2v1 == 1:
        $ can1_celia_school_morning_scene2v1 = True
        $ can_school_intercom = False
        $ can_celia_morning_school_work_in_pr = False
    if CR3_AS5_can >= 3:
        $ CR3_AS5_can +=1
    if CR3_MS3_can == False:
        $ CR3_MS3 = False

    if CR3_NS2_can == False and CR3_NS2 == True:
        $ CR3_NS2 = False
        $ C_NS_locked = False

    if CR3_NS3_can == False and CR3_NS3 == True:
        $ CR3_NS3 = False
        $ C_NS_locked = False
    $ ML_NSB_sleep_can = True
    $ CR3_MS1_talked = False
    if CR3_ES1_can == False:
        $ CR3_ES1 = False
    if MLR3_MS1_can == False:
        $ MLR3_MS1 = False
        $ MLR3_Bob_MS1 = True
        $ MLR3_Linda_MS1 = True
        $ MLR2_MS1_active = False
        $ MLR3_MS1_can = 4
    $ MLR3_Bob_MS1_can = True
    if MLR3_Bob_MS1_day_can == True:
        $ MLR3_Bob_MS1_q3 = True
        $ MLR3_Bob_MS1_q4 = True
        $ MLR3_Bob_MS1_day_can = False

    if MLR3_Linda_MS1_day == 3:
        $ MLR3_Linda_MS1 = False
        $ MLR3_Bob_MS1 = False
        $ Bob_in_work = True
        $ MLR3_MS2 = True
        $ MLR3_Linda_MS1_day = False
    $ MLR3_Linda_MS1_can = True
    if MLR3_MS3 == 2:
        $ MLR3_MS3 = True
        $ MLR3_MS2 = False
    $ MLR3_Bob_AS1_can = True
    $ headmaster_door_locked = False
    $ Judy_in_her_Office = True
    if MLR3_AS3 == 2:
        $ MLR3_AS3 = 3
    if MLR3_NS1 == 2:
        $ MLR3_NS1 = 3
    if MLR3_NS1 == 5:
        $ MLR3_NS2 = True
        $ MLR3_NS1 = 6
    if MLR3_NS1 == 4 and MLR3_AS3 == 4:

        $ MLR3_NS1 = 5
        $ MLR3_AS3 = 5
    if MLR3_ES1_end == True:
        $ MLR3_ES1 = False
        $ MLR3_ES1_end = False
    if MLR2_R3_MS1_talk >= 2 and MLR2_R3_MS1_talk_new_q == True:
        $ MLR2_R3_MS1_q5 = True
        $ MLR2_R3_MS1_q6 = True
        $ MLR2_R3_MS1_q7 = True
        $ MLR2_R3_MS1_q8 = True
        $ MLR2_R3_MS1_talk_new_q = False
        $ MLR2_MS1_visit = 5
    if MLR3_AS2_event_can == True:
        $ MLR3_AS2_event = 1
        $ MLR3_AS2_event_can = False

    if week_day == 1:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 2:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 3:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 4:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 5:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 6:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 7:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1

