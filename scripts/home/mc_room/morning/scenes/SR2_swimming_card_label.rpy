image SR2_swimming_card_p1 = "images/home/mc_room/morning/scenes/SR2_swimming_card/1.jpg"
image SR2_swimming_card_p2 = "images/home/mc_room/morning/scenes/SR2_swimming_card/2.jpg"
image SR2_swimming_card_p3 = "images/home/mc_room/morning/scenes/SR2_swimming_card/3.jpg"
image SR2_swimming_card_p4 = "images/home/mc_room/morning/scenes/SR2_swimming_card/4.jpg"
image SR2_swimming_card_p5 = "images/home/mc_room/morning/scenes/SR2_swimming_card/5.jpg"
image SR2_swimming_card_p6 = "images/home/mc_room/morning/scenes/SR2_swimming_card/6.jpg"
image SR2_swimming_card_p7 = "images/home/mc_room/morning/scenes/SR2_swimming_card/7.jpg"
image SR2_swimming_card_p8 = "images/home/mc_room/morning/scenes/SR2_swimming_card/8.jpg"

label SR2_swimming_card_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
    $ renpy.hide("mc_sleep_night_bed", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ renpy.pause(3, hard= True)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    MC "(Snooore…)"
    $ Sara_name = "???"
    Sara "[player_name]? Are you asleep?"
    $ Sara_name = "Sara"
    MC "(Zzzzzz…)"

    scene SR2_swimming_card_p1 with dissolve

    Sara "[player_name]?"
    MC "(Yawn!)"
    MC "Hmm?"

    scene SR2_swimming_card_p2

    Sara "Yay! You’re finally up!"
    MC "Huh? What time is it? You’re never up before me. I must have slept in."
    Sara "Hey! There’s LOADS of times, I’ve been up before you!"
    MC "Oh really? Name me two times you’ve woken up before me."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_swimming_card_p1

    Sara "Err… There was that time we were on that school trip in Spain!"
    MC "That’s because a cockroach crawled into your bed, and woke you up at five in the morning!"
    Sara "I still woke up before you, so it still counts! And… uhh… today is number two! I win!"
    if persistent.incest_patch == True:
        MC "(Sigh) What do you want me for, then? Did Mom tell you to get me out of bed?"
    else:
        MC "(Sigh) What do you want me for, then? Did Linda tell you to get me out of bed?"
    scene SR2_swimming_card_p2

    Sara "No, silly! I got you something!"
    MC "OOh cool! What is it?"

    scene SR2_swimming_card_p3

    Sara "Ta-da! Here you go!"
    MC "What is it?"
    Sara "Just open it!"

    scene SR2_swimming_card_p4

    MC "(Hmm, it doesn’t feel too heavy. I wonder what it could be.)"

    MC "(I’m gonna try shaking it.)"

    "(RATTLE RATTLE)"

    Sara "…"
    Sara "Seriously? What age are you?"
    MC "C’mon! It’s perfectly natural to want to shake a present!"
    Sara "If you say so..."

    scene SR2_swimming_card_p5

    Sara "Now, hurry up and open it. I can’t wait around all morning!"
    MC "Fine, I’ll open it. Don’t get your panties in a twist!"
    Sara "(Ooh… That sounds kinda lewd…)"

    scene SR2_swimming_card_p6

    MC "Oh! Swimming Pool VIP Cards! Awesome!"
    Sara "Yeah. They let you-"
    MC "Unlimited access, right?"
    Sara "That’s right!"
    MC "These must have cost you a fortune, Sara! Where did you get this kind of money?!"

    scene SR2_swimming_card_p4
    if persistent.incest_patch == True:
        Sara "I’ve been saving up my allowance, that Dad gave me."
    else:
        Sara "I’ve been saving up my money."

    Sara "I didn’t know what I actually wanted though - Until we started… seeing each other."
    Sara "[player_name], I want to go to the swimming pool with you on the weekends, if you’re free."
    Sara "That’s why I got two - So we could spend some time together."

    scene SR2_swimming_card_p7

    MC "Aww, thank you so much, Sara. This is so thoughtful of you."
    MC "You keep this one, I’ll hold onto the other. Sometime, when we’re both free, we can organise, going to the pool together."
    Sara "Really?!"
    MC "Absolutely!"

    scene SR2_swimming_card_p8

    Sara "Thanks, [player_name]! You’re the best!"
    Sara "I’m gonna head downstairs and grab breakfast. See you later, [player_name]."
    MC "Thanks again, Sara! Catch you later!"
    $ inventory.add(swimming_poll_card)
    $ SR2_weekend_swimming_pool = True
    $ SR2_swimming_card = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1
