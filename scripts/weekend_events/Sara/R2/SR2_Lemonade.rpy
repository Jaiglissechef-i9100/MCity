image SR2_weekend_lemonade_p1 = "images/Weekend_Events/Sara/R2/Lemonade/1.jpg"
image SR2_weekend_lemonade_p2 = "images/Weekend_Events/Sara/R2/Lemonade/2.jpg"
image SR2_weekend_lemonade_p3 = "images/Weekend_Events/Sara/R2/Lemonade/3.jpg"
image SR2_weekend_lemonade_p4 = "images/Weekend_Events/Sara/R2/Lemonade/4.jpg"
image SR2_weekend_lemonade_p5 = "images/Weekend_Events/Sara/R2/Lemonade/5.jpg"
image SR2_weekend_lemonade_p6 = "images/Weekend_Events/Sara/R2/Lemonade/6.jpg"
image SR2_weekend_lemonade_p7 = "images/Weekend_Events/Sara/R2/Lemonade/7.jpg"

label SR2_Lemonade_label:
    if SR2_after_lemonade == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "We've already been there."
        $ music_continue = False

        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "Come to think of it, I’m actually quite thirsty."
        MC "Do you fancy grabbing something to drink?"
        Sara "Sure! There’s a lemonade stand on the other side of the complex."
        MC "Awesome! Let’s go."

        scene SR2_weekend_lemonade_p1

        MC "Good call, Sara. I haven’t had a decent lemonade in months."
        Sara "Yeah, I’ve been here with my friends when I was younger. It’s really good!"
        Sara "Hey, when was the last time you went to the swimming pool?"
        MC "Damn… Years ago? I can’t even remember."
        MC "All I know for certain, is that the last time I was there, I didn’t have a gorgeous girl sitting opposite me, in a cute swimsuit."

        scene SR2_weekend_lemonade_p2

        Sara "Hehe… Stop it! You’re gonna make me blush."
        Sara "And weren’t you the one who said to cut back on flirting, in case we get caught?"
        MC "Relax. There’s nobody else here. We’ll be fine."
        jump lemonade_menu

label lemonade_menu:
    scene SR2_weekend_lemonade_p2
    window hide
    menu:
        "Can I talk to you about what happened with Lily?" if menu_q1 == True:
            scene SR2_weekend_lemonade_p1

            MC "Actually, Sara, can we talk about what happened with Lily in your bedroom the other day?"

            scene SR2_weekend_lemonade_p4

            Sara "W-What?"
            MC "You threw a bottle across the room. It was quite clear that something we did pissed you off."

            scene SR2_weekend_lemonade_p3

            Sara "I… Um…."
            MC "Actually, if you’re feeling too anxious to talk about it, don’t worry. We can chat about something else."
            Sara "N-No, it’s fine."
            Sara "I guess I just couldn’t stand the thought of you being with her. I might not seem to appear that way, but I can get very… jealous."
            MC "Huh? Why?"

            scene SR2_weekend_lemonade_p4

            Sara "Why?! Just look at them with their perfect golden blonde hair and their big breasts."
            Sara "Then, take a look at me. What do I have? An A-cup, dull brown hair, and freckles."

            scene SR2_weekend_lemonade_p3

            Sara "I know that this thing between you and me won’t last forever."
            Sara "You’re gonna move on to one of those big boobed, blonde haired bimbos someday. And then you’ll forget about plain little me."
            MC "(Damn… I never realised she had confidence issues with her body. That’s another reason for her gross overreaction to Lily kissing me.)"
            MC "Sara… You’re not plain."
            window hide
            menu:
                "Compliment her personality.":
                    scene SR2_weekend_lemonade_p3

                    MC "There’s more to life than looks. Most of those ‘bimbos’ that you talk about have terrible personalities."
                    MC "You’re sweet, kind, and very very caring. I wouldn’t change you for the world."
                    Sara "… thanks. They’re still prettier than me though - and looks have to count for something."
                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu
                "Compliment her breasts.":

                    scene SR2_weekend_lemonade_p3

                    MC "I don’t know why you’re so worried about the size of your breasts."
                    Sara "They’re tiny. Why do you think I wear a one piece swimsuit instead of a bikini?"
                    Sara "I’ve got nothing to show off."
                    MC "What are you talking about? Your breasts are amazing!"
                    MC "Some guys like big boobs - I’ll give you that."

                    scene SR2_weekend_lemonade_p4

                    MC "Other guys LOVE small tits though; and yours are fucking adorable."
                    MC "Plus, smaller breasts tend to have more sensitive nipples."
                    Sara "[player_name]!"
                    MC "It’s just a fact! Haha!"

                    scene SR2_weekend_lemonade_p2

                    Sara "Well… maybe someday we can try out your small breast sensitivity theory."
                    MC "I’m looking forward to that."

                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu
                "Compliment her eyes.":

                    scene SR2_weekend_lemonade_p3

                    MC "Sara, look up at me."
                    Sara "Hmm?"

                    scene SR2_weekend_lemonade_p1

                    MC "They’re absolutely perfect."
                    Sara "Don’t lie. I’ve always wanted, AT LEAST a C-cup."
                    MC "I’m not talking about your breasts. I’m talking about your eyes."

                    scene SR2_weekend_lemonade_p4

                    Sara "Huh?"
                    MC "They’re the most stunning shade of emerald green."
                    MC "I think you’re focusing so much on the parts of you that you don’t like, that you don’t realise how amazing other parts of you actually are."
                    MC "You’ve got the most beautiful irises I’ve ever seen."
                    Sara "Th-thank you, [player_name]…"
                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu

        "Can we talk about that blowjob you gave me?" if menu_q2 == True:
            scene SR2_weekend_lemonade_p1

            MC "Can we talk about that blowjob you gave me?"

            scene SR2_weekend_lemonade_p5

            Sara "We’re in public! Shush!"
            Sara "What if someone from school hears us right now?!"
            Sara "It would be even more embarrassing than when you tried to ask your teacher out!"
            MC "Can we try not to talk about that?"
            Sara "Haha! Okay..."

            scene SR2_weekend_lemonade_p2

            Sara "We can talk about the blowjob in private someday."
            MC "I’m looking forward to that."
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False:
                jump after_lemonade_menu
            else:
                jump lemonade_menu

label after_lemonade_menu:
    scene SR2_weekend_lemonade_p5

    Sara "Anyway! We’ve spent long enough here."
    Sara "I’ll race you to finish your drink!"
    MC "Sure! Ready whenever you-"

    scene SR2_weekend_lemonade_p6

    Sara "*SHLURP SHLURP*"
    Sara "*GULP GULP*"

    scene SR2_weekend_lemonade_p7

    Sara "I win!"
    MC "(Holy shit! I barely had a chance to bring the straw to my mouth.)"
    MC "Fine - you win! "
    Sara "Yay! I’ll let you finish off there, then we can head elsewhere whenever you’re ready to go."
    $ SR2_after_lemonade = True
    $ can_hide_windows = False
    jump swimming_poll_label