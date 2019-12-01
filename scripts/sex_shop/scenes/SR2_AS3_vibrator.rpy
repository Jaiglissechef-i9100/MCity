image SR2_AS3_vibrator_p1 = "images/sex_shop/scenes/SR2_AS3_v/1.jpg"
image SR2_AS3_vibrator_p2 = "images/sex_shop/scenes/SR2_AS3_v/2.jpg"
image SR2_AS3_vibrator_p3 = "images/sex_shop/scenes/SR2_AS3_v/3.jpg"
image SR2_AS3_vibrator_p4 = "images/sex_shop/scenes/SR2_AS3_v/4.jpg"
image SR2_AS3_vibrator_p5 = "images/sex_shop/scenes/SR2_AS3_v/5.jpg"
image SR2_AS3_vibrator_p6 = "images/sex_shop/scenes/SR2_AS3_v/6.jpg"

label SR2_AS3_vibrator_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ can_hide_windows = True
    if persistent.incest_patch == True:
        $ S = __("Saleswoman")
    else:
        $ S = __("Saleswoman")

    if SR2_AS3_v_loop == True:
        if inventory.money >= 80:
            scene SR2_AS3_vibrator_p1 with dissolve
            S "Do you have the $80?"
            MC "Here you are."
            S "Thank you very much! Come again!"
            $ inventory.buy(SR2_vibrator)
            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:
            scene SR2_AS3_vibrator_p1 with dissolve
            S "Do you have the $80??"
            MC "Not yet."
            $ can_hide_windows = False
            jump sex_shop_evening_label
    else:
        scene SR2_AS3_vibrator_p1 with dissolve

        MC "(This is probably the best place to get a vibrator for Sara. I’ve no idea which type to get her though.)"
        MC "(I should probably ask the girl behind the counter. She might be able to to give me some advice.)"
        MC "(Damn, she’s so fucking sexy! Just look at how much cleavage she’s showing off!)"
        S "Hello there? Can I help you? Or are you just gonna keep staring at me?"
        MC "I- uh… I… wanted to buy a vibrator."

        scene SR2_AS3_vibrator_p2

        S "Ooh, a guy buying a vibrator... Kinky."
        if persistent.incest_patch == True:
            MC "No! It’s not for me! It’s for my sister!"
            S "Your sister?!"
        else:
            MC "No! It’s not for me! It’s for my friend!"
            S "Your friend?!"
        MC "(FUCK!)"
        MC "S-Sorry! I mean, my… uh… my girlfriend. I’m sorry, I’m just really nervous right now."

        scene SR2_AS3_vibrator_p1
        if persistent.incest_patch == True:
            S "Hehe... It’s okay. So, has your sister- I mean, “girlfriend”, used a vibrator before?"
        else:
            S "Hehe... It’s okay. So, has your friend- I mean, “girlfriend”, used a vibrator before?"
        MC "No - my GIRLFRIEND - hasn't. I was thinking of getting her something weak, for a beginner?"
        MC "Y’know, one that isn’t too strong and maybe smaller than average?"

        scene SR2_AS3_vibrator_p2

        S "Oh no, honey. You don’t want to do that."
        S "Go big or go home! That’s what I always say."

        scene SR2_AS3_vibrator_p3

        MC "Err… Are you sure?"
        S "Ab-so-lutely!"
        S "You sit tight, honey. I'm just gonna check what I still have in stock."
        S "Hmm… Too small… Too thin…"
        S "AHA!"

        scene SR2_AS3_vibrator_p4

        S "This baby is the Double Deluxe 9000. Made in California, from the highest quality materials."
        MC "(Jesus Christ… That thing’s massive!)"
        MC "I… uh…"
        S "Here, hold it!"

        scene SR2_AS3_vibrator_p5

        MC "It’s… um… very pink."
        S "Your girlfriend will love it!"
        S "It’s also one of the most intense vibrators on the market."
        MC "Just how powerful IS this thing?"
        S "Well, if the average vibrator on the market is a five out of then; this thing is an eight or nine."

        scene SR2_AS3_vibrator_p6

        MC "Are you sure I shouldn’t settle for a less powerful one?"
        S "Trust me, honey. She’ll appreciate, you going big, for her first time."
        MC "(Gulp) If you’re sure. How much do I owe you?"
        S "That’ll be 80$."
        $ SR2_AS3_v_loop = True
        if inventory.money >= 80:
            S "Thank you very much! Come again!"
            $ inventory.buy(SR2_vibrator)
            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:
            MC "I don't have enough money now."
            MC "I'll come back later."
            $ can_hide_windows = False
            jump sex_shop_evening_label
