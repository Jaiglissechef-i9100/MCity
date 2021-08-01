image SR2_AS4_p1 = "images/school/classroom2/day/scenes/SR2_AS4/1.jpg"
image SR2_AS4_p2 = "images/school/classroom2/day/scenes/SR2_AS4/2.jpg"
image SR2_AS4_p3 = "images/school/classroom2/day/scenes/SR2_AS4/3.jpg"
image SR2_AS4_p4 = "images/school/classroom2/day/scenes/SR2_AS4/4.jpg"
image SR2_AS4_p5 = "images/school/classroom2/day/scenes/SR2_AS4/5.jpg"
image SR2_AS4_p6 = "images/school/classroom2/day/scenes/SR2_AS4/6.jpg"

label SR2_AS4_label:
    if can_SR2_AS4 == False:
        $ clickable = False
        show screen classroom2_day
        MC "I've already talked with her."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS4_p1 with dissolve

        MC "(There’s Sara - it’s nice to see her smiling for a change.)"
        MC "Hey Sara! You’re looking in a better mood today!"
        Sara "Hi, [player_name]. Yeah, I’m feeling a bit better."

        scene SR2_AS4_p2

        MC "I’m happy to hear that. Is the studying getting easier?"
        Sara "Oh, God no. That’s still hell!"
        MC "What’s got you so happy then?"
        Sara "(Whispered) I was just thinking about lying beside you at night. It was so wonderful just lying there with my head on your chest, listening to your heart beating."
        Sara "I’d never felt, more at peace, in my life."
        MC "Aww, that’s so sweet. I loved cuddling you at night too."

        $ menu_q1 = True
        $ menu_q2 = True
        $ menu_q3 = True
        $ menu_q4 = True
        $ menu_q5 = True
        $ menu_ask = 0
        jump SR2_AS4_menu

label SR2_AS4_menu:
    scene SR2_AS4_p5
    Sara "So, why did you come to visit me?"
    menu:
        "How is your studying going?" if menu_q1 == True:
            scene SR2_AS4_p3

            MC "How’s your studying going? Have your grades improved at, all?"
            Sara "Ugh, do we HAVE to talk about this?"
            MC "The sooner you get your grades back on track, the sooner I get to spend more time with you again!"

            scene SR2_AS4_p5

            Sara "I know. I know... It’s just… every time you bring it up, it reminds me that I was super lazy."
            MC "Okay, I’ll try not to bring the topic up again. Just… try to get your grades up soon, okay? I don’t want you to be grounded forever."
            Sara "I’ll try to get back on track as soon as I can, I promise."
            $ menu_q1 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Did you enjoy me using the vibrator on you?" if menu_q2 == True:
            scene SR2_AS4_p5

            MC "Did you enjoy me using the vibrator on you?"

            scene SR2_AS4_p3

            Sara "Y-Yeah, kinda. It was just… very very sensitive."
            Sara "I suppose that’s because I’ve never really done anything like that before - so my body isn’t completely used to it."

            scene SR2_AS4_p4

            Sara "But don’t worry - I’ll be making sure to use it VERY regularly."
            Sara "Someday soon, you’ll be able to use it on me, for as long as you want."
            MC "I’m looking forward to that!"
            $ menu_q2 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "What’s your favourite subject?" if menu_q3 == True:
            scene SR2_AS4_p5

            MC "I don’t think I’ve ever asked you: What’s your favourite subject?"
            Sara "In school?"
            MC "Yeah."
            Sara "Hmm… To be honest, I haven’t really been interested in any of them at all, lately."
            Sara "I guess, before I really got into video games I enjoyed maths. It was nice knowing that your answer was either right or wrong - you didn’t have shades of grey, like in history or English literature."
            $ menu_q3 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "I just wanted to come by and say thanks for the amazing blowjob." if SR2_NS2_blow_ch == True and menu_q4 == True:
            scene SR2_AS4_p3

            MC "I just wanted to come by to say thanks for the amazing blowjob."
            Sara "[player_name]! We’re in class! Someone might hear us..."
            MC "Everyone’s talking to each other - nobody’s gonna be listening."
            MC "I just had to come and tell you that it felt absolutely amazing. Your technique was brilliant. And the way you swallowed it at the end... God… it felt so fucking great."

            scene SR2_AS4_p4

            Sara "Really? You enjoyed it that much?"
            MC "Oh yeah."
            Sara "Mmm, I guess I’ll just have to give you another one then. I’ll try and take your cock deeper into my mouth next time. Would you like that?"
            MC "That’d be awesome!"
            $ menu_q4 = False
            $ menu_q5 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "That footjob you gave me was sooo good!" if SR2_NS2_foot_ch == True and menu_q5 == True:
            scene SR2_AS4_p5

            MC "I just wanted to drop by and say that the footjob you gave me was sooo good."
            Sara "R-Really? You enjoyed it? It was my first time, so I wasn’t sure if I was doing it right."
            MC "Trust me, you were brilliant!"

            scene SR2_AS4_p6

            Sara "Yay! I guess it paid off then!"
            MC "Huh? What paid off?"

            scene SR2_AS4_p4

            Sara "Learning from the best teacher there is! You!"
            MC "Haha! You're very sweet."
            Sara "I also spent a few hours, searching sex techniques on the internet. I tried to teach myself as much as I could."
            MC "Seriously? Did you learn any new tricks?"
            Sara "Oh yeah! But that’s for me to know, and you to find out!"
            $ menu_q4 = False
            $ menu_q5 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Skip questions." if menu_ask >= 2:
            jump SR2_AS4_continue

label SR2_AS4_continue:
    scene SR2_AS4_p5

    MC "Okay, I better head on now. It was good seeing you today, Sara."
    Sara "Wait - before you go… Do you think we could chat on webcam this evening?"
    if persistent.incest_patch == True:
        Sara "I’m confined to my room, but Mom hasn’t taken away my laptop - so we could chat on that."
    else:
        Sara "I’m confined to my room, but I still have my laptop - so we could chat on that."
    MC "Yeah, sure. I’ll see you this evening."

    scene SR2_AS4_p6

    Sara "Yay! I’m looking forward to it!"
    MC "Great! See you later then, Sara!"
    Sara "See ya, [player_name]!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ can_SR2_AS4 = False
    $ S_inv_webcam = True
    $ SR2_ES1 = True

    $ menu_q1 = False
    $ menu_q2 = False
    $ menu_q3 = False
    $ menu_q4 = False
    $ menu_q5 = False
    $ menu_ask = 0
    jump classroom2_morning1

