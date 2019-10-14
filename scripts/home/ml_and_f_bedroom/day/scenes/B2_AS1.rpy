image B2_AS1_p1 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/1.jpg"
image B2_AS1_p2 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/2.jpg"
image B2_AS1_p3 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/3.jpg"
image B2_AS1_p4 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/4.jpg"
image B2_AS1_p5 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/5.jpg"
image B2_AS1_p6 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/6.jpg"
image B2_AS1_p7 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/7.jpg"

default B2_AS1_day = 1
default B2_AS1_q1 = True
default B2_AS1_q2 = True
default can_B2_AS1_day = True
default bob_payment_money = 0
label B2_AS1_label:
    if B2_AS1_day == 4:
        if money_from_bob > 0:
            scene B2_AS1_p2
            window hide
            menu:
                "{color=#00ff00}I sorted the documents. Could you pay me?{/color}" if money_from_bob > 0:
                    $ bob_payment_money = 0
                    scene B2_AS1_p2
                    MC "I sorted the documents. Could you pay me?"
                    Dad "Ah! Good job, [player_name]! Here, take it."
                    MC "Thanks!"
                    scene B2_AS1_p5
                    Dad "No, I thank you! I hate doing that! "
                    Dad "After so many times, it started to be incredibly boring."
                    MC "Haha!"
                    jump B2_AS1_payment2
        else:

            show screen parents_bedroom_day_notclickable
            Dad "Not now, [player_name]."
            jump parents_bedroom_morning1


    if can_B2_AS1_day == False:
        if money_from_bob > 0:
            scene B2_AS1_p2
            window hide
            menu:
                "{color=#00ff00}I sorted the documents. Could you pay me?{/color}" if money_from_bob > 0:
                    $ bob_payment_money = 0
                    scene B2_AS1_p2
                    MC "I sorted the documents. Could you pay me?"
                    Dad "Ah! Good job, [player_name]! Here, take it."
                    MC "Thanks!"
                    scene B2_AS1_p5
                    Dad "No, I thank you! I hate doing that! "
                    Dad "After so many times, it started to be incredibly boring."
                    MC "Haha!"
                    jump B2_AS1_payment2
        else:
            show screen parents_bedroom_day_notclickable
            Dad "Not now, [player_name]."
            jump parents_bedroom_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene B2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Hey, Dad!"
    else:
        MC "Hey, Bob!"
    Dad "Hello there, champ. What’s cooking?"

    scene B2_AS1_p2

    MC "What’s… cooking?"
    Dad "It’s an old expression… nevermind. What’s up?"
    jump B2_AS1_menu_label

label B2_AS1_menu_label:
    scene B2_AS1_p2
    window hide
    menu:
        "{color=#00ff00}I sorted the documents. Could you pay me?{/color}" if money_from_bob > 0:
            $ bob_payment_money = 0
            scene B2_AS1_p2
            MC "I sorted the documents. Could you pay me?"
            Dad "Ah! Good job, [player_name]! Here, take it."
            MC "Thanks!"
            scene B2_AS1_p5
            Dad "No, I thank you! I hate doing that! "
            Dad "After so many times, it started to be incredibly boring."
            MC "Haha!"
            jump B2_AS1_payment

        "I didn’t know you smoked." if B2_AS1_day == 1 and B2_AS1_q1 == True:
            scene B2_AS1_p2

            MC "I didn’t know you smoked."
            Dad "I don’t. At least, not cigarettes. They’re awful for your lungs."
            MC "Aren’t cigars really bad for you too?"

            scene B2_AS1_p4

            Dad "A lot of people think that, but the truth is that you don’t inhale a cigar."
            MC "Really?"

            scene B2_AS1_p6

            Dad "You just gently draw it into your mouth to taste it…"

            scene B2_AS1_p7

            Dad "...then exhale it."
            Dad "It’s all about the taste; not the nicotine."

            scene B2_AS1_p5

            MC "Huh? Interesting! I never knew that."
            Dad "The more you know..!"
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 2
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Have you heard about Caroline’s shop?" if B2_AS1_q2 == True and B2_AS1_day == 1:
            scene B2_AS1_p2

            MC "Have you heard about Caroline’s shop?"
            if renpy.loadable("patch.rpy"):
                Dad "Oh yeah! Your mom mentioned that a while back. How’s it going?"
            else:
                Dad "Oh yeah! Linda mentioned that a while back. How’s it going?"
            MC "Pretty good! She’s moved into online sales."

            scene B2_AS1_p3

            Dad "That’s the dream, right there. Minimal costs for rent and FAR less staff to deal with."
            Dad "Let me tell you something, champ. Take a seat."

            scene B2_AS1_p4

            Dad "This is a lesson I want you to NEVER forget."
            MC "I’m listening."
            Dad "Work is easy. It’s managing staff that’s the hard part."
            MC "Really?"
            Dad "You can control work and be responsible for it - but staff are human beings, and VERY unpredictable at times."

            scene B2_AS1_p5
            if renpy.loadable("patch.rpy"):
                MC "Thanks, Dad. I’ll remember that!"
            else:
                MC "Thanks, Bob. I’ll remember that!"
            Dad "Good lad."
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 2
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label


        "You look very relaxed!" if B2_AS1_day == 2 and B2_AS1_q1 == True and can_B2_AS1_day == True:

            scene B2_AS1_p2
            MC "You look very relaxed!"
            Dad "I work hard. I think I deserve to take a little time off, every now and then."

            scene B2_AS1_p6

            Dad "And what more could I ask for? It’s a gorgeous day. And I’ve got a brilliant cigar, and a comfortable couch."
            MC "Heh... I guess you’re right."

            scene B2_AS1_p7

            Dad "Whenever you’re young, make the most of your free time, and enjoy your days off work."
            Dad "You’ll never be able to truly appreciate them, until they’re gone - but still, try to enjoy them."

            scene B2_AS1_p5

            Dad "When you get to my age, you’ll have maybe, an hour here and there to relax."
            Dad "But each one becomes much more special. Like this moment right now."
            Dad "I know it’s few and far between - but I can sit back, kick my feet up, and enjoy every last second."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Doesn’t Mom get angry with you smoking cigars in the bedroom?" if B2_AS1_day == 2 and B2_AS1_q2 == True and can_B2_AS1_day == True and renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Doesn’t Mom get angry when you smoke cigars in the bedroom?"

            scene B2_AS1_p7

            Dad "I only started recently. A couple of boys recommended them on my last fishing trip."

            scene B2_AS1_p5

            Dad "It took me a while to really learn to appreciate them - but I think I’m getting there."
            MC "What about the smell?"
            Dad "A bit of air freshener and an open window sorts that out."
            Dad "Your mom hasn’t complained so far, at least!"
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label
        "Doesn’t Linda get angry with you smoking cigars in the bedroom?" if B2_AS1_day == 2 and B2_AS1_q2 == True and can_B2_AS1_day == True and not renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Doesn’t Linda get angry when you smoke cigars in the bedroom?"

            scene B2_AS1_p7

            Dad "I only started recently. A couple of boys recommended them on my last fishing trip."

            scene B2_AS1_p5

            Dad "It took me a while to really learn to appreciate them - but I think I’m getting there."
            MC "What about the smell?"
            Dad "A bit of air freshener and an open window sorts that out."
            Dad "Linda hasn’t complained so far, at least!"
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label




        "Is everything okay between you and Mom? " if B2_AS1_day == 3 and B2_AS1_q1 == True and can_B2_AS1_day == True and renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Is everything okay between you and Mom?"

            scene B2_AS1_p4

            Dad "Why would you ask that?"
            MC "I’m just curious. The two of you just seem a little more… distant than usual."
            Dad "When you’ve been in a marriage as long as we have, you’ll learn that there are peaks and troughs."
            Dad "Your mother is a complex woman - one of the many reasons I fell in love with her."


            scene B2_AS1_p3

            Dad "Sometimes she becomes withdrawn and needs to ‘find herself.’ I’ve found that it’s best to let her get on with it, and give her some space."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Is everything okay between you and Linda? " if B2_AS1_day == 3 and B2_AS1_q1 == True and can_B2_AS1_day == True and not renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Is everything okay between you and Linda?"

            scene B2_AS1_p4

            Dad "Why would you ask that?"
            MC "I’m just curious. The two of you just seem a little more… distant than usual."
            Dad "When you’ve been in a relationship as long as we have, you’ll learn that there are peaks and troughs."
            Dad "Linda is a complex woman - one of the many reasons I fell in love with her."


            scene B2_AS1_p3

            Dad "Sometimes she becomes withdrawn and needs to ‘find herself’. I’ve found that it’s best to let her get on with it and give her some space."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Have you got any advice for finding a girlfriend?" if B2_AS1_day == 3 and B2_AS1_q2 == True and can_B2_AS1_day == True:
            scene B2_AS1_p1
            if renpy.loadable("patch.rpy"):
                MC "Have you got any advice for finding a girlfriend, Dad?"
            else:
                MC "Have you got any advice for finding a girlfriend, Bob?"

            scene B2_AS1_p2

            Dad "A girlfriend? Hmm…"
            Dad "Put yourself out there."

            scene B2_AS1_p3

            Dad "Be open and honest about your interests. If you’re a videogamer, then state that you are."
            Dad "If you’re into sports or movies, then be upfront about it."
            if renpy.loadable("patch.rpy"):
                MC "But what if they don’t like the same things as me, Dad."
            else:
                MC "But what if they don’t like the same things as me, Bob."

            scene B2_AS1_p5

            Dad "Opposites attract, champ."
            Dad "Contrary to what you may believe, people aren’t looking for carbon copies of themselves when they go dating."
            Dad "They’re looking for individuals, with get-up-and-go. People who embrace life and enjoy it."

            scene B2_AS1_p4

            Dad "The only thing I need to warn you about, is that solitary hobbies won’t help you meet girls."
            Dad "If your hobby is painting models - then go to a gaming club. If your hobby is watching movies, then go to a movie club."
            Dad "You NEED to get yourself out there. And then, when you’re out there, say hello."
            Dad "Be polite, introduce yourself, be charming. That’s all there is to it."

            scene B2_AS1_p6

            MC "But, what if I get rejected?"

            scene B2_AS1_p7

            Dad "Suck it up and move on. It’ll happen."
            Dad "You can take solace in the fact that you did your absolute best - you put your best foot forward and you tried."
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label
        "Cancel":

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1


label B2_AS1_payment:
    if money_from_bob > 0:
        $ inventory.earn(25)
        $ bob_payment_money += 25
        $ money_from_bob -=1
        jump B2_AS1_payment
    else:
        "You recive {color=#00ff00}[bob_payment_money]${/color}."
        jump B2_AS1_menu_label

label B2_AS1_payment2:
    if money_from_bob > 0:
        $ inventory.earn(25)
        $ bob_payment_money += 25
        $ money_from_bob -=1
        jump B2_AS1_payment2
    else:
        "You recive {color=#00ff00}[bob_payment_money]${/color}."
        jump parents_bedroom_morning1