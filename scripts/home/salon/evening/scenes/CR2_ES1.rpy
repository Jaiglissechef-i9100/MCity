image CR2_ES1_p1 = "images/home/salon/evening/scenes/CR2_ES1/1.jpg"
image CR2_ES1_p2 = "images/home/salon/evening/scenes/CR2_ES1/2.jpg"
image CR2_ES1_p3 = "images/home/salon/evening/scenes/CR2_ES1/3.jpg"
image CR2_ES1_p4 = "images/home/salon/evening/scenes/CR2_ES1/4.jpg"
image CR2_ES1_p5 = "images/home/salon/evening/scenes/CR2_ES1/5.jpg"
image CR2_ES1_p6 = "images/home/salon/evening/scenes/CR2_ES1/6.jpg"
image CR2_ES1_p7 = "images/home/salon/evening/scenes/CR2_ES1/7.jpg"
image CR2_ES1_p8 = "images/home/salon/evening/scenes/CR2_ES1/8.jpg"
image CR2_ES1_p9 = "images/home/salon/evening/scenes/CR2_ES1/9.jpg"
image CR2_ES1_p10 = "images/home/salon/evening/scenes/CR2_ES1/10.jpg"
image CR2_ES1_p11 = "images/home/salon/evening/scenes/CR2_ES1/11.jpg"
image CR2_ES1_p12 = "images/home/salon/evening/scenes/CR2_ES1/12.jpg"

default CR2_ES1_day = 1
default CR2_ES1_q1 = True
default CR2_ES1_q2 = True
default CR2_ES1_q3 = False
default CR2_ES1_q4 = False
default CR2_ES1_q5 = False
default CR2_ES1_q6 = False
default CR2_ES1_q7 = False
default CR2_ES1_q8 = False
default can_CR2_ES1 = True
default can_CR2_ES1_day2 = False
default can_CR2_ES1_day3 = False
default CR2_ES1_day2_firsttime = True
default CR2_ES1_day3_firsttime = True
default CR2_ES1_q1Sara = False

label CR2_ES1_label:
    if can_CR2_ES1 == False:
        show screen salon_evening_notclickable
        MC "I shouldn't bother her. She wants to be alone."
        jump salon_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ can_hide_windows = True
        if CR2_ES1_day == 1:
            scene CR2_ES1_p1 with dissolve

            MC "(There’s Caroline! It looks like she’s spending the day relaxing in front of the TV.)"
            MC "(Let’s see how she’s doing.)"

            scene CR2_ES1_p2

            MC "Hey, Caroline! What’s up?"
            Caroline "Oh! Hey, [player_name]! Nothing much. Just treating myself, now that I’ve got some disposable income."
            MC "Awesome! The job must be really working out for you."

            scene CR2_ES1_p3

            Caroline "It really is!"
            Caroline "What can I do for you?"
            jump CR2_ES1_menu
        if CR2_ES1_day == 2:
            scene CR2_ES1_p1 with dissolve

            MC "(Just like she said - she’s still hanging out in the Living Room in her free time.)"
            MC "(I may as well drop by and say hello.)"

            scene CR2_ES1_p2

            MC "Hey again!"
            Caroline "Hi, [player_name]."
            if CR2_ES1_day2_firsttime == True:
                $ CR2_ES1_q3 = True
                $ CR2_ES1_q4 = True
                $ CR2_ES1_q5 = True
                $ CR2_ES1_day2_firsttime = False
                jump CR2_ES1_menu

        if CR2_ES1_day == 3:
            scene CR2_ES1_p1 with dissolve

            MC "(I think this must be Caroline's favourite thing to do after work!)"
            MC "(Does she ever go anywhere, apart from here and work?!)"

            scene CR2_ES1_p2

            MC "Here again?"
            Caroline "Haha! Just putting my feet up, after work."

            scene CR2_ES1_p3

            Caroline "So, what brings you here?"
            if CR2_ES1_day3_firsttime == True:
                $ CR2_ES1_q6 = True
                $ CR2_ES1_q7 = True
                $ CR2_ES1_q8 = True
                $ CR2_ES1_day3_firsttime = False
                jump CR2_ES1_menu
        jump CR2_ES1_menu

label CR2_ES1_menu:
    scene CR2_ES1_p3
    window hide
    menu:
        "I was looking for you." if CR2_ES1_q1 == True:
            scene CR2_ES1_p3

            MC "I was looking for you."

            scene CR2_ES1_p4

            Caroline "Oh yeah? And what did you need me for?"

            $ CR2_ES1_q1 = False
            $ CR2_ES1_q2 = False
            $ can_CR2_ES1_day2 = True
            jump CR2_ES1_menu_cancel

        "How’s work going?" if CR2_ES1_q3 == True:
            scene CR2_ES1_p3

            MC "How’s everything at work?"
            Caroline "Sales are booming. In fact, the biggest problem I’m having right now, is getting stock delivered to ME fast enough."
            MC "Oh yeah?"

            scene CR2_ES1_p6

            Caroline "Seriously - I order in a bunch of clothes - and before I can even display them, they’ve been purchased online!"
            MC "That’s amazing, Caroline! Congratulations!"

            scene CR2_ES1_p8

            Caroline "Haha! It’s high-stress though."
            Caroline "I swear - these lazy days are the only thing keeping me sane right now!"
            MC "Don’t push yourself too hard!"
            $ CR2_ES1_q3 = False
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "Have you spoken with Sara, lately?" if CR2_ES1_q4 == True:
            scene CR2_ES1_p3

            MC "Have you spoken with Sara, lately?"

            scene CR2_ES1_p9

            Caroline "It’s… a bit sad. Sara and I have never really shared any common interests."
            MC "Really?"
            Caroline "I don’t really like video games, and I’m not into the nerdy stuff that she is."
            MC "Hmm..."

            scene CR2_ES1_p3

            Caroline "I mean, we still say hello to each other. But it’s not like we’d have, a deep meaningful conversation."
            MC "Yeah, I know what you mean."
            $ CR2_ES1_q4 = False
            $ CR2_ES1_q1Sara = True
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "What are your plans for the business, going forward?" if CR2_ES1_q5 == True:
            scene CR2_ES1_p4

            MC "What are your plans for your business, going forward?"
            Caroline "I’m not sure."

            scene CR2_ES1_p7

            Caroline "Honestly, I’m a bit overwhelmed right now. I am still the ONLY employee!"
            Caroline "Maybe someday, I’d look into designing my own clothing line? Or opening up a chain of stores."

            scene CR2_ES1_p8

            Caroline "Right now though, I’m content to focus on ensuring that my current store stays profitable."
            $ CR2_ES1_q5 = False
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "I wanted to talk about the deal we made." if CR2_ES1_q6 == True:
            scene CR2_ES1_p10

            MC "I wanted to talk about the deal we made."
            Caroline "What?!"
            MC "The deal where-"

            scene CR2_ES1_p6

            Caroline "Shush! Not in public."
            MC "Oh, come on! There’s nobody around to hear us."
            Caroline "I am NOT talking about this with you in the middle of the living room!"
            MC "Fine! We’ll chat later."
            $ CR2_ES1_q6 = False
            jump CR2_ES1_menu

        "Are Mom and Dad fighting?" if CR2_ES1_q7 == True and persistent.incest_patch == True:
            jump CR2_ES1_menu_bobfight
        "Are Linda and Bob fighting?" if CR2_ES1_q7 == True and not persistent.incest_patch == True:
            jump CR2_ES1_menu_bobfight

        "Have you any advice for finding a girlfriend?" if CR2_ES1_q8 == True:
            scene CR2_ES1_p4

            MC "Caroline, I was wondering - do you have any advice for finding a girlfriend?"
            Caroline "Sure. What part are you having trouble with?"
            MC "All of it."

            scene CR2_ES1_p7

            Caroline "Haha! Okay then!"
            Caroline "Let’s start with the basics."

            scene CR2_ES1_p5

            Caroline "Make sure you wash, wear clean clothes, and take care of your appearance."
            Caroline "After that, you can work on your personality. People like confidence."

            scene CR2_ES1_p11

            Caroline "Just go up to a girl that you like, put your hand on her shoulder and ask if you can buy her a coffee."
            Caroline "It’s that easy."

            scene CR2_ES1_p10

            MC "It didn't work that way with Mrs. Celia."
            Caroline "That’s because she was your teacher! There’s certain boundaries you shouldn’t cross."

            scene CR2_ES1_p12

            Caroline "Don’t stress about all this too much. It’ll come to you eventually."
            Caroline "Just focus on doing what you enjoy."
            $ CR2_ES1_q8 = False
            jump CR2_ES1_menu
        "Bye.":

            if CR2_ES1_q1Sara == True:
                scene CR2_ES1_p10

                Caroline "So, what about you and Sara? I’ve seen you two hanging out together, more than usual."
                window hide
                menu:
                    "We’re fairly close.":
                        scene CR2_ES1_p5

                        MC "Sara and I have always been fairly close. "
                        Caroline "Yeah, you’re lucky to have that connection with her!"
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel
                    "I don’t really feel connected to her.":

                        scene CR2_ES1_p6

                        MC "I don’t really feel connected to Sara."
                        MC "I don’t know if it’s an age thing perhaps, but we don’t seem to have that much in common."
                        Caroline "Aww, I’m sorry to hear that. Hopefully she’ll mature more, in the coming years."
                        MC "Yeah, I hope so too."
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel

                    "Sara and I are having an incestuous relationship." if Sara_points >= 2 and persistent.incest_patch == True:
                        scene CR2_ES1_p10

                        MC "Yeah, Sara and I have been having an incestuous relationship."
                        Caroline "[player_name]!"

                        scene CR2_ES1_p5

                        Caroline "Haha! You have a SICK sense of humour!"
                        MC "(If only she knew the truth!)"
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel

                    "Sara and I have been having a friends with benefits relationship." if Sara_points >= 2 and not persistent.incest_patch == True:
                        scene CR2_ES1_p10

                        MC "Yeah, Sara and I have been having a friends with benefits relationship."
                        Caroline "[player_name]!"

                        scene CR2_ES1_p5

                        Caroline "Haha! You have a SICK sense of humour!"
                        MC "(If only she knew the truth!)"
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel
            else:
                jump CR2_ES1_menu_cancel

label CR2_ES1_menu_cancel:
    if CR2_ES1_day == 2:
        scene CR2_ES1_p11

        Caroline "Let me finish watching my program. I’ll see you later on."

        scene CR2_ES1_p12

        Caroline "Be good, okay?"
        MC "Don’t worry, I will! See you later, Caroline!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1
    if CR2_ES1_day == 3:

        scene CR2_ES1_p12
        Caroline "Time for me to rest my feet. I’ll see you later, [player_name]."
        MC "Bye, Caroline!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1
    else:
        scene CR2_ES1_p12
        Caroline "Let me finish watching my TV series. I’ll see you later on."
        MC "Bye, Caroline."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1

label CR2_ES1_menu_bobfight:
    scene CR2_ES1_p9
    if persistent.incest_patch == True:
        MC "Are Mom and Dad fighting at the minute?"
    else:
        MC "Are Linda and Bob fighting at the minute?"
    Caroline "What makes you think that?"
    MC "Things have just seemed… tense between them."
    Caroline "They go through ups and downs."

    scene CR2_ES1_p4

    Caroline "For as long as I can remember, those two have always had their good moments and their bad moments."
    Caroline "At the end of the day, they’ve always pulled through. I don’t see any reason why this bad moment should be any different."
    MC "Yeah, hopefully you’re right."
    $ CR2_ES1_q7 = False
    $ can_hide_windows = False
    jump CR2_ES1_menu

