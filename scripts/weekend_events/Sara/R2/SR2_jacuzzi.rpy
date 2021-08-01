image SR2_weekend_jacuzzi_background = "images/Weekend_Events/Sara/R2/Map/2.jpg"

image SR2_weekend_jacuzzi_p1 = "images/Weekend_Events/Sara/R2/Jacuzzi/1.jpg"
image SR2_weekend_jacuzzi_p2 = "images/Weekend_Events/Sara/R2/Jacuzzi/2.jpg"
image SR2_weekend_jacuzzi_p3 = "images/Weekend_Events/Sara/R2/Jacuzzi/3.jpg"
image SR2_weekend_jacuzzi_p4 = "images/Weekend_Events/Sara/R2/Jacuzzi/4.jpg"
image SR2_weekend_jacuzzi_p5 = "images/Weekend_Events/Sara/R2/Jacuzzi/5.jpg"
image SR2_weekend_jacuzzi_p6 = "images/Weekend_Events/Sara/R2/Jacuzzi/6.jpg"
image SR2_weekend_jacuzzi_p7a = "images/Weekend_Events/Sara/R2/Jacuzzi/7a.jpg"
image SR2_weekend_jacuzzi_p7b = "images/Weekend_Events/Sara/R2/Jacuzzi/7b.jpg"
image SR2_weekend_jacuzzi_p7c = "images/Weekend_Events/Sara/R2/Jacuzzi/7c.jpg"
image SR2_weekend_jacuzzi_p7d = "images/Weekend_Events/Sara/R2/Jacuzzi/7d.jpg"
image SR2_weekend_jacuzzi_p8a = "images/Weekend_Events/Sara/R2/Jacuzzi/8a.jpg"
image SR2_weekend_jacuzzi_p8b = "images/Weekend_Events/Sara/R2/Jacuzzi/8b.jpg"
image SR2_weekend_jacuzzi_p8c = "images/Weekend_Events/Sara/R2/Jacuzzi/8c.jpg"
image SR2_weekend_jacuzzi_p9 = "images/Weekend_Events/Sara/R2/Jacuzzi/9.jpg"
image SR2_weekend_jacuzzi_p10 = "images/Weekend_Events/Sara/R2/Jacuzzi/10.jpg"
image SR2_weekend_jacuzzi_p11 = "images/Weekend_Events/Sara/R2/Jacuzzi/11.jpg"
image SR2_weekend_jacuzzi_p11anim = Movie(play="videos/02 Sara-Weekend-1.webm", loop = True )
image SR2_weekend_jacuzzi_p12 = "images/Weekend_Events/Sara/R2/Jacuzzi/12.jpg"
image SR2_weekend_jacuzzi_p13 = "images/Weekend_Events/Sara/R2/Jacuzzi/13.jpg"
image SR2_weekend_jacuzzi_p14 = "images/Weekend_Events/Sara/R2/Jacuzzi/14.jpg"
image SR2_weekend_jacuzzi_p15 = "images/Weekend_Events/Sara/R2/Jacuzzi/15.jpg"
image SR2_weekend_jacuzzi_p16 = "images/Weekend_Events/Sara/R2/Jacuzzi/16.jpg"
image SR2_weekend_jacuzzi_p16anim = Movie(play="videos/02 Sara-Weekend-2.webm", loop = True )
image SR2_weekend_jacuzzi_p17 = "images/Weekend_Events/Sara/R2/Jacuzzi/17.jpg"
image SR2_weekend_jacuzzi_p17anim = Movie(play="videos/02 Sara-Weekend-4.webm", loop = True )
image SR2_weekend_jacuzzi_p18 = "images/Weekend_Events/Sara/R2/Jacuzzi/18.jpg"
image SR2_weekend_jacuzzi_p19 = "images/Weekend_Events/Sara/R2/Jacuzzi/19.jpg"
image SR2_weekend_jacuzzi_p20 = "images/Weekend_Events/Sara/R2/Jacuzzi/20.jpg"
image SR2_weekend_jacuzzi_p21 = "images/Weekend_Events/Sara/R2/Jacuzzi/21.jpg"
image SR2_weekend_jacuzzi_p21anim = Movie(play="videos/02 Sara-Weekend-3.webm", loop = True )
image SR2_weekend_jacuzzi_p22 = "images/Weekend_Events/Sara/R2/Jacuzzi/22.jpg"
image SR2_weekend_jacuzzi_p23 = "images/Weekend_Events/Sara/R2/Jacuzzi/23.jpg"
image SR2_weekend_jacuzzi_p24a = "images/Weekend_Events/Sara/R2/Jacuzzi/24a.jpg"
image SR2_weekend_jacuzzi_p24b = "images/Weekend_Events/Sara/R2/Jacuzzi/24b.jpg"
image SR2_weekend_jacuzzi_p24c = "images/Weekend_Events/Sara/R2/Jacuzzi/24c.jpg"
image SR2_weekend_jacuzzi_p25a = "images/Weekend_Events/Sara/R2/Jacuzzi/25a.jpg"
image SR2_weekend_jacuzzi_p25b = "images/Weekend_Events/Sara/R2/Jacuzzi/25b.jpg"

label SR2_jacuzzi_label:
    if SR2_after_swimming == True and SR2_after_lemonade == True and SR2_after_sunbed == True and SR2_after_waterslide == True:
        scene SR2_weekend_jacuzzi_background
        $ can_hide_windows = False
        call screen SR2_jacuzzi_scr
    else:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        Sara "[player_name]... It’s too soon for a jacuzzi! Relaxing should come last."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label

screen SR2_jacuzzi_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 810
        ypos 422
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b6.png"
        hover "images/Weekend_Events/Sara/R2/Map/b6_hover.png"
        hovered Show("displayTextScreen", displayText = "Jacuzzi")
        action [Hide("displayTextScreen"),SetVariable("music_continue", False),Jump("SR2_jacuzzi_scene_label")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("swimming_poll_label")]
        unhovered Hide("displayTextScreen")

label SR2_jacuzzi_scene_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)

    scene SR2_weekend_swimming_pool_p2
    $ can_hide_windows = True
    MC "I saw a sign when I was coming in that mentioned something about jacuzzis."
    MC "Do they actually have jacuzzis in here?"
    Sara "Oh yeah! They’re awesome!"
    Sara "Plus, we get private access for 30 minutes each day with our VIP membership cards!"
    MC "What are we waiting for, then? Let’s go!"

    scene SR2_weekend_jacuzzi_p1

    MC "This is even better than I thought it would be."
    MC "A warm jacuzzi, a beautiful woman, and a private room. It’s brilliant!."
    Sara "Aww... I’m glad you like it."

    scene SR2_weekend_jacuzzi_p2

    Sara "(Sigh…)"
    MC "(Huh? What’s gotten into her?)"
    MC "Are you okay, Sara?"
    Sara "I guess so…"
    MC "What’s wrong?"
    Sara "Our date today... I mean.. Is it even a date? …We haven’t really done anything."

    if renpy.loadable("patch.rpy"):
        Sara "It kinda feels like we’ve reverted back to brother and sister, when we’re out."

    MC "Well, to be honest - it would be very risky to act like we’re dating."

    scene SR2_weekend_jacuzzi_p3

    Sara "Screw it!"
    MC "Huh?!"
    Sara "It’s just you and me. Nobody else can come in for twenty five more minutes."
    Sara "That’s enough time, right?"
    MC "Enough time for what?!"

    scene SR2_weekend_jacuzzi_p4

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

    Sara "I want to feel the way I did when I gave you that first blowjob."
    MC "Sara, I-"
    Sara "Kiss me."

    scene SR2_weekend_jacuzzi_p5

    MC "(I thought Sara was happy, taking things slowly - especially when we were out in public.)"
    MC "(It looks like she’s been repressing her sex drive though!)"
    Sara "You can touch wherever you want."

    scene SR2_weekend_jacuzzi_p6

    MC "(I guess that’s an open invitation to hold her ass while I make out with her.)"
    MC "(I wonder how far Sara is willing to go today. Maybe I’ll get to finger her?)"
    MC "(I’m overthinking this now. I should just lie back and enjoy whatever happens.)"
    window hide
    menu:
        "Touch her ass.":
            scene SR2_weekend_jacuzzi_p7a

            Sara "Mmm!"
            MC "Mmm…"
            MC "(Sounds like she’s enjoying having her ass groped!)"

            scene SR2_weekend_jacuzzi_p7b

            MC "(Let’s give it a hard squeeze and see how she reacts!)"

            scene SR2_weekend_jacuzzi_p7c

            Sara "MMMMM!!!!"

            scene SR2_weekend_jacuzzi_p7d

            Sara "(Holy shit, that felt good!)"
            MC "(Yup! Looks like I found the right spot there!)"
            jump after_menu_SR2_jacuzzi_scene_label
        "Wait for her move.":

            scene SR2_weekend_jacuzzi_p4

            Sara "[player_name], I want you to… It’s embarrassing... Nevermind."
            MC "Go ahead. I promise I won’t laugh."
            Sara "Can you… pinch my nipples?"
            MC "Sure! Sit up for me."

            scene SR2_weekend_jacuzzi_p8a

            MC "How’s that?"
            Sara "Ah… it’s g-good…"
            Sara "Ooh…"

            scene SR2_weekend_jacuzzi_p8b

            MC "Should I keep going?"
            Sara "Yeah, don’t s-stop."
            MC "Harder?"
            Sara "Could… you use your whole hand?"

            scene SR2_weekend_jacuzzi_p8c

            MC "Like this?"
            Sara "Oooh yeah… That’s amazing…"
            MC "See, smaller breasts like yours are MUCH more sensitive."
            Sara "Mmm… I’m glad they’re smaller now."
            jump after_menu_SR2_jacuzzi_scene_label


label after_menu_SR2_jacuzzi_scene_label:
    scene SR2_weekend_jacuzzi_p9

    Sara "I love you so much, [player_name]."
    MC "I love you too, Sara. Thanks again for buying me the VIP pass."
    Sara "You don’t need to thank me. It’s been an amazing present for me too."

    scene SR2_weekend_jacuzzi_p10

    Sara "Oooh! It feels like someone’s all hard again!"
    MC "Oops... Sorry! Haha!"
    Sara "I’m gonna go pay [player_name] Junior a visit!"
    Sara "Let’s get these swim shorts off you."
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3,hard=True)

    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_weekend_jacuzzi_p11

    Sara "Wow… I forgot how big it was!"
    Sara "Hey [player_name], how does it feel if I touch your balls?"

    MC "Go ahead and find out. Just… be gentle!"

    scene SR2_weekend_jacuzzi_p12

    Sara "*Suck Suck*"
    MC "Ahh…"
    Sara "(Aha! So it DOES feel good when a guy has his balls played with!)"

    scene SR2_weekend_jacuzzi_p13

    MC "Oh yeah, that’s it. Keep going, Sara..."
    scene SR2_weekend_jacuzzi_p11anim
    Sara "*Suck Suck*"
    Sara "(Wow! He’s wanking himself off while I suck on his balls.)"

    scene SR2_weekend_jacuzzi_p14

    MC "Ugh! Mmm…. Ah…."
    Sara "(Sounds like he’s REALLY enjoying this!)"
    Sara "(I just hope he doesn’t cum too quickly!)"

    scene SR2_weekend_jacuzzi_p15

    Sara "Would you like me to give you a blowjob now?"
    MC "Definitely!"
    Sara "Okay, let me get into position."

    scene SR2_weekend_jacuzzi_p16

    Sara "How’s this?"
    scene SR2_weekend_jacuzzi_p16anim
    MC "Perfect!"
    MC "Your eyes are amazing, you know that?"
    Sara "Hehe... Thanks. I’m ready whenever you are."

    scene SR2_weekend_jacuzzi_p17

    Sara "Mwah!"

    MC "(She’s so cute. I love the way she begins her blowjobs with a kiss.)"
    Sara "(Okay, I’ll have to do everything I can, to make sure [player_name] REALLY enjoys this one!)"

    scene SR2_weekend_jacuzzi_p18

    Sara "*Suck Suck*"
    MC "Mmm… Oh… That’s good…"
    Sara "(It tastes a little bit salty!)"

    scene SR2_weekend_jacuzzi_p19

    Sara "(Okay - time to start taking his cock in my mouth.)"
    MC "That feels great, Sara."
    MC "Ahh… Wow…"

    scene SR2_weekend_jacuzzi_p20

    MC "Wow!"
    scene SR2_weekend_jacuzzi_p17anim
    MC "(The feeling of her hot mouth - wrapped tightly around my glans - is indescribable.)"
    MC "(I’m having to fight off the urge to blow my load, straight away!)"

    scene SR2_weekend_jacuzzi_p21

    MC "Ohh… Ohhhh… Mmm…."
    scene SR2_weekend_jacuzzi_p21anim
    Sara "*Suck* *Shlurp* *Suck*"
    Sara "*SHLUUUURRRRP*"

    scene SR2_weekend_jacuzzi_p22

    MC "(Fuck! I’m not gonna last much longer! I wonder if she’ll mind taking it deeper!)"
    MC "(Let’s thrust my hips forward and see.)"
    Sara "*Suck Suck*"

    scene SR2_weekend_jacuzzi_p23

    Sara "*Suck* *GAG*"
    MC "AHHHH! SHIT! YES!"
    MC "Fuck! I’m gonna cum!"

    window hide
    menu:
        "Blow your hot load deep inside your younger sister’s mouth." if renpy.loadable("patch.rpy"):
            scene SR2_weekend_jacuzzi_p24a

            MC "Open wide, Sara!"
            Sara "Ahhhh…."
            MC "HNNNNNGGG! YES!"

            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24b with dissolve

            MC "AHHHHHHHHH!"
            MC "Ugh!! Ahhh…."
            MC "Phew… That was incredible!"
            Sara "Mmm…"

            scene SR2_weekend_jacuzzi_p24c

            Sara "(I wonder why it always tastes so salty.)"
            Sara "(Gulp)"
            MC "Thanks, Sara. You’re amazing at that!"
            jump after_menu2_SR2_jacuzzi_scene_label

        "Blow your hot load deep inside Sara’s mouth." if not renpy.loadable("patch.rpy"):
            scene SR2_weekend_jacuzzi_p24a

            MC "Open wide, Sara!"
            Sara "Ahhhh…."
            MC "HNNNNNGGG! YES!"

            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24b with dissolve

            MC "AHHHHHHHHH!"
            MC "Ugh!! Ahhh…."
            MC "Phew… That was incredible!"
            Sara "Mmm…"

            scene SR2_weekend_jacuzzi_p24c

            Sara "(I wonder why it always tastes so salty.)"
            Sara "(Gulp)"
            MC "Thanks, Sara. You’re amazing at that!"
            jump after_menu2_SR2_jacuzzi_scene_label

        "Spray your seed over your younger sister’s pretty face." if renpy.loadable("patch.rpy"):
            scene SR2_weekend_jacuzzi_p25a

            Sara "You don’t want me to keep sucking?"
            MC "Just stay like that! Hnnnnng!"
            Sara "Are you sur-"
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25b with dissolve

            Sara "Eww!"
            MC "AHHHH! Ugh!"
            MC "Fuck! That’s good!"
            Sara "Yuck! (I almost got it in my eye!)"
            jump after_menu2_SR2_jacuzzi_scene_label

        "Spray your seed over Sara’s pretty face." if not renpy.loadable("patch.rpy"):
            scene SR2_weekend_jacuzzi_p25a

            Sara "You don’t want me to keep sucking?"
            MC "Just stay like that! Hnnnnng!"
            Sara "Are you sur-"
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25b with dissolve

            Sara "Eww!"
            MC "AHHHH! Ugh!"
            MC "Fuck! That’s good!"
            Sara "Yuck! (I almost got it in my eye!)"
            jump after_menu2_SR2_jacuzzi_scene_label


label after_menu2_SR2_jacuzzi_scene_label:
    scene SR2_weekend_jacuzzi_p9

    MC "Well? How was this date?"
    Sara "The BEST so far!"
    MC "Really?"
    Sara "Yeah, [player_name]. I was kinda hoping to get intimate with you again sooner."

    scene SR2_weekend_jacuzzi_p10

    Sara "I really do love you."
    Sara "But I want more than just words… I need an intimate physical relationship with you. Like what we just did today."
    MC "Let me think about it and I’ll see if I can think of ways we can safely be intimate, without others noticing."
    Sara "Thanks, [player_name]. You’re the best!"
    MC "I love you, Sara."
    $ can_hide_windows = False
    $ SR2_after_swimming = False
    $ R2_after_lemonade = False
    $ SR2_after_sunbed = False
    $ SR2_after_waterslide = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    if can_sms4_sara == True:
        $ sms4_sara = True
        $ can_sms4_sara = False
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

    if Li_MAS3_menu_visit >= 2 and Li_MAS2_menu_visit >= 2 and LiR1_MAS4can3 == True:
        $ LiR1_MAS4 = True

    if LiR1_MAS5_can1 == True and LiR1_MAS5_can2 == True and clean_loop >1:
        $ LiR1_MAS5 = True
        $ LiR1_MAS3 = False

    if LiR1_MAS6_can1 == True:
        $ LiR1_MAS6 = True
        $ LiR1_MAS2 = False
        $ LiR1_MAS3 = False
        $ a_pool_empty = False

    if LiR1_MAS7_can1 == True and LiR1_MAS7_can2 == True:
        $ LiR1_MAS7 = True
        $ LiR1_keyMAS7 = True
        $ LiR1_MAS2 = False
        $ LiR1_MAS3 = False

    if LiR1_MAS8_can1 == True:

        $ LiR1_MAS3 = False
        $ LiR1_MAS2 = False
        $ LiR1_MAS8 = True
    $ can2_LiR1_NS = True


    $ CR3_MS2_can3 = True
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