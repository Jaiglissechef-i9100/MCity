image SR2_AS2_p1 = "images/school/classroom2/day/scenes/SR2_AS2/1.jpg"
image SR2_AS2_p2 = "images/school/classroom2/day/scenes/SR2_AS2/2.jpg"
image SR2_AS2_p3 = "images/school/classroom2/day/scenes/SR2_AS2/3.jpg"
image SR2_AS2_p4 = "images/school/classroom2/day/scenes/SR2_AS2/4.jpg"
image SR2_AS2_p5 = "images/school/classroom2/day/scenes/SR2_AS2/5.jpg"
image SR2_AS2_p6 = "images/school/classroom2/day/scenes/SR2_AS2/6.jpg"

label SR2_AS2_label:
    if can_SR2_AS2 == False:
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
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS2_p1 with dissolve

        MC "Hey, Sara! How’s it going?"
        Sara "Hi, [player_name]! Not too great, to be honest."

        scene SR2_AS2_p2
        if persistent.incest_patch == True:
            Sara "Mom has me up, at the crack of dawn, for school. And then, as soon as I get home, she’s making me work ALL evening!"
        else:
            Sara "Linda has me up, at the crack of dawn, for school. And then, as soon as I get home, she’s making me work ALL evening!"
        Sara "I can’t STAND reading any more of these textbooks! It’s driving me mad!"
        $ menu_q1 = True
        $ menu_q2 = True
        $ menu_q3 = True
        jump SR2_AS2_menu

label SR2_AS2_menu:
    scene SR2_AS2_p2

    menu:
        "Maybe you should have just studied, instead of playing video games?" if menu_q1 == True:

            MC "Maybe you should have studied, instead of playing video games?"
            scene SR2_AS2_p3

            Sara "Uuuggghhh…. Not you too!"
            if persistent.incest_patch == True:
                Sara "That’s EXACTLY what Mom said."
            else:
                Sara "That’s EXACTLY what Linda said."
            MC "Maybe she’s right?"
            Sara "God… I’m so stupid! Stupid, stupid, Sara!"
            MC "(Gee, she’s beating herself up, pretty hard about this.)"

            scene SR2_AS2_p4

            MC "(I have to comfort her - I can’t stand seeing her like this.)"
            MC "Hey, don’t worry, Sara. You’ll be back on track with your studies in no time!"
            MC "You’re one of the smartest people I know. We just need to get you back in the saddle. Then you’ll be, top of the class again!"

            scene SR2_AS2_p5

            Sara "Thanks, [player_name]. I appreciate it."
            Sara "Whenever I get my grades back up, we'll play some more video games together. Deal?"
            MC "Deal."
            $ menu_q1 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

        "Have you tried speaking to Mom about giving you some freedom again?" if menu_q2 == True and persistent.incest_patch == True:
            scene SR2_AS2_p1

            MC "Have you tried speaking to Mom about getting some freedoms back?"
            MC "Maybe she’d ease up and give you a break, for a change?"

            scene SR2_AS2_p2

            Sara "Nah, I tried that already. I practically BEGGED her to let me have an hour of ‘me time’ before I went to bed."
            MC "How’d that go?"
            Sara "Disastrously. I’ve never seen her so furious before."
            MC "(Well, Sara did kinda bring it on, herself.)"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

        "Have you tried speaking to Linda about giving you some freedom again?" if menu_q2 == True and not persistent.incest_patch == True:
            scene SR2_AS2_p1

            MC "Have you tried speaking to Linda about getting some freedoms back?"
            MC "Maybe she’d ease up and give you a break, for a change?"

            scene SR2_AS2_p2

            Sara "Nah, I tried that already. I practically BEGGED her to let me have an hour of ‘me time’ before I went to bed."
            MC "How’d that go?"
            Sara "Disastrously. I’ve never seen her so furious before."
            MC "(Well, Sara did kinda bring it on, herself.)"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

        "Do you have ANY free time?" if menu_q3 == True:

            MC "Do you have ANY free time, at all, right now?"
            Sara "If you count my break and lunch at school, then yeah, I have a total of forty five minutes."
            MC "Aww, jeez."

            scene SR2_AS2_p3

            Sara "I know. It sucks!"
            Sara "The worst part of it is - my friends are all going out and having fun! I’m stuck in the house with my books and homework!"
            MC "Umm… Didn’t you spend most nights in the house, anyway - playing video games?"

            scene SR2_AS2_p6

            Sara "That’s… not relevant."
            MC "(I’m pretty sure it’s VERY relevant. No point in arguing with her, right now though. She’s learning a painful lesson.)"
            if persistent.incest_patch == True:
                MC "Fine. Just try and make the most of it, to get your grades back to the high A’s again. Okay? If not for Mom, then do it for me."
            else:
                MC "Fine. Just try and make the most of it, to get your grades back to the high A’s again. Okay? If not for Linda, then do it for me."

            scene SR2_AS2_p5

            Sara "It’s really exhausting! But I’ll try, [player_name]."
            MC "Thanks, Sara."
            $ menu_q3 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

label SR2_AS2_cantinue:
    scene SR2_AS2_p5

    MC "I guess I’ll catch you later, then."
    Sara "Wait - before you go… Can I sneak over to your room tonight?"
    if persistent.incest_patch == True:
        MC "Will Mom allow that? I thought you were grounded."
    else:
        MC "Will Linda allow that? I thought you were grounded."

    scene SR2_AS2_p6

    Sara "I am. That’s why I said SNEAK!"
    MC "Ahh…"
    Sara "I wanted to talk with you about… some things that I can't... say out loud in class."
    if persistent.incest_patch == True:
        MC "No problem. Come over whenever you’re free. Just make sure that Mom doesn’t see you!"
    else:
        MC "No problem. Come over whenever you’re free. Just make sure that Linda doesn’t see you!"
    Sara "Cool! Catch you later, [player_name]."
    MC "See ya, Sara."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ can_SR2_AS2 = False
    $ SR2_NS1 = True
    $ S_N_inbed = False
    jump classroom2_morning1

