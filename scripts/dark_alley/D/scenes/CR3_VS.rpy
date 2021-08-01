image CR3_VS_p1 = "/images/dark_alley/D/scenes/CR3_VS/1.jpg"
image CR3_VS_p2 = "/images/dark_alley/D/scenes/CR3_VS/2.jpg"
image CR3_VS_p3 = "/images/dark_alley/D/scenes/CR3_VS/3.jpg"
image CR3_VS_p4 = "/images/dark_alley/D/scenes/CR3_VS/4.jpg"
image CR3_VS_p5 = "/images/dark_alley/D/scenes/CR3_VS/5.jpg"
image CR3_VS_p6 = "/images/dark_alley/D/scenes/CR3_VS/6.jpg"
image CR3_VS_p7 = "/images/dark_alley/D/scenes/CR3_VS/7.jpg"
image CR3_VS_p8 = "/images/dark_alley/D/scenes/CR3_VS/8.jpg"

label CR3_VS_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_VS_p1 with dissolve
    if persistent.incest_patch == True:
        MC "Hey, Violet! My sister said I could probably, find you hanging out around here."
    else:
        MC "Hey, Violet! Caroline said I could probably, find you hanging out around here."
    Violet "Oh hey, [player_name]. Is Caroline looking for me?"
    MC "Yeah, but we can get to that later. It’s nothing urgent."

    $ menu_q1 = True
    $ menu_q2 = True
    $ menu_q3 = True
    $ menu_q4 = True

    jump CR3_VS_menu

label CR3_VS_menu:

    scene CR3_VS_p1
    menu:
        "Why do you always hang out in this filthy alley?" if menu_q1 == True:
            scene CR3_VS_p2

            MC "Why are you always hanging out in this filthy alley?"
            Violet "Filthy alley?!"

            scene CR3_VS_p3

            Violet "My house is in this alleyway!"

            MC "(Oops!)"
            MC "Shit! Sorry, I didn’t mean to insult you."

            scene CR3_VS_p5

            Violet "*Sigh* You’re right... It’s a shithole. I just can’t afford a better place, right now."
            MC "What are you working as?"
            Violet "I’m mostly doing - random one-off - jobs. My art degree didn’t make me very lucrative, to the job market. I should have seen it coming, to be honest."

            $ menu_q1 = False

            jump CR3_VS_menu

        "How are you keeping?" if menu_q2 == True:
            scene CR3_VS_p4

            MC "How are you keeping?"
            Violet "*Sigh* I’ve been better, My mother is struggling to pay rent, I’m struggling to find a permanent job, and my brother is..."

            scene CR3_VS_p7

            Violet "...well, you know how my brother is."
            MC "Damn, I’m sorry to hear that. Is there anything I can do to help you?"
            Violet "If you can line me up with a job - or even work experience - I’d really appreciate it. Aside from that, I’m just waiting for a miracle."

            $ menu_q2 = False

            jump CR3_VS_menu

        "How are things with your brother? Do you need any help?" if menu_q3 == True:
            scene CR3_VS_p6

            MC "How are things with your brother?"
            Violet "He’s still an asshole. Nothing has changed there."
            MC "He hasn’t beaten you again, has he?"

            scene CR3_VS_p7

            Violet "...I don’t want to talk about it."
            MC "How have you been handling things by yourself, so far? Have you tried speaking to him?"
            Violet "Umm... not successfully."

            scene CR3_VS_p8

            MC "Do you need my help to sort things out with him?"
            Violet "M-Maybe... I’ll come back to you, when I figure out what’s going on. My head’s not in a great place, right now."

            $ menu_q3 = False

            jump CR3_VS_menu

        "{color=#00ff00}Caroline wants to know if you’d like to come and help out, at her shop.{/color}" if menu_q4== True:
            scene CR3_VS_p4

            MC "Caroline wants to know if you’d like to come and help out, at her shop."
            Violet "Really? What would I be doing?"
            MC "Photography, I think."

            scene CR3_VS_p7

            Violet "Hmm, I don’t really have a lot of experience - in that area of art."
            MC "It’ll be fine - besides, you definitely owe her, after stealing from her shop."

            scene CR3_VS_p6

            Violet "*Sigh* That’s true. Fine. I’ll help out. When does she need me there?"
            MC "I’m not sure. You’ll need to talk with her."
            Violet "No problem. I’ll do that soon."
            MC "Thanks, Violet. I really appreciate it. Caroline is struggling to find a good employee - I reckon you’re exactly the person she needs."
            $ CR3_MS1_q4 = False

            $ menu_q4 = False
            $ CR3_AS1 = False
            jump CR3_VS_menu

        "Bye." if menu_q4 == False:
            $ CR2_VS = False
            $ day_time +=1
            $ menu_q1 = False
            $ menu_q2 = False
            $ menu_q3 = False

            $ CR3_AS2 = True

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump dark_alley_label

