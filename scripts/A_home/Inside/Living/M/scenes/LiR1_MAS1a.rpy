image LiR1_MAS1a_p1 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/1.jpg"
image LiR1_MAS1a_p2 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/2.jpg"
image LiR1_MAS1a_p3 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/3.jpg"
image LiR1_MAS1a_p4 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/4.jpg"
image LiR1_MAS1a_p5 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/5.jpg"
image LiR1_MAS1a_p6 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/6.jpg"
image LiR1_MAS1a_p7 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/7.jpg"
image LiR1_MAS1a_p8 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/8.jpg"
image LiR1_MAS1a_p9 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/9.jpg"
image LiR1_MAS1a_p10 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/10.jpg"
image LiR1_MAS1a_p11 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/11.jpg"
image LiR1_MAS1a_p12 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/12.jpg"
image LiR1_MAS1a_p13 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/13.jpg"
image LiR1_MAS1a_p14 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/14.jpg"
image LiR1_MAS1a_p15 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS1a/15.jpg"

label LiR1_MAS1a_label:
    hide screen displayTextScreen

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if renpy.loadable("patch.rpy"):
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"

    scene black
    $ can_hide_windows = True
    $ renpy.pause (1, hard = True)
    scene LiR1_MAS1a_p1 with dissolve

    Yazmin "I caught him, lurking around the back of the house. He was perving on me, while I was sunbathing, Liza."
    MC "WHAT?!"
    Yazmin "Haha! I’m teasing!"

    scene LiR1_MAS1a_p2

    Liza "Oh, c’mon, Yazmin - you’re gonna scare the poor kid."
    if renpy.loadable("patch.rpy"):
        Liza "Long time no see! How’s my favourite nephew been doing?!"
        MC "I’m keeping well, Auntie Liza! I gotta say - I love your new place. This house looks amazing!"
    else:
        Liza "Long time no see! How’ve you been doing?!"
        MC "I’m keeping well, miss Liza! I gotta say - I love your new place. This house looks amazing!"
    Liza "Oh please - you can just call me Liza. "

    scene LiR1_MAS1a_p3

    Liza "I’m guessing you’ve already caught up with Yazmin. Has she told you about, her new line of work?"
    MC "We spoke briefly, outside, but she didn’t mention her new job."
    Liza "She’s a supermodel now!"
    Yazmin "You’re exaggerating, Liza. The only thing - I - really do, is model clothes, for local chains."
    Liza "Well, you look like a supermodel to me. Take a seat, [player_name]. Can I get you something to drink? "
    MC "I’m alright - thanks for offering."
    $ q1 = True
    $ q2 = True

    jump LiR1_MAS1a_menu

label LiR1_MAS1a_menu:
    if renpy.loadable("patch.rpy"):
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"
    scene LiR1_MAS1a_p4

    menu:
        "How long have you been living in your new house, [Liza2_name]?" if q1 == True:
            scene LiR1_MAS1a_p5

            MC "So, how long have you been living here then, [Liza2_name]? Last time I visited you - was back in that old bungalow."

            scene LiR1_MAS1a_p4

            Liza2 "Wow, has it really been that long?! I must have been living here for... three or four years now."
            MC "Seriously? Has it been that long?! I’m feeling bad now, for not visiting sooner!"
            Liza2 "Hehe - don’t worry about it! I remember how busy I was, as a teenager. Honestly, it just felt like a video game at times, jumping from one event to the next. Do you know what I mean?"
            MC "Uhh... Yeah, I think so."

            scene LiR1_MAS1a_p9

            Liza2 "Anyway! Truth be told - I’m just glad to be out of that bungalow. The whole place stunk of dampness and mould. Moving into a new building was the best decision, I ever made, in my life!"
            MC "Great to hear! Glad it’s going well for you."

            $ q1 = False
            jump LiR1_MAS1a_menu

        "What are you working as, [Liza2_name]?" if q2 == True:
            scene LiR1_MAS1a_p5

            MC "So, what are you working as, now, [Liza2_name]?"
            Liza2 "I’m a secretary for a local law firm - Answering calls, taking minutes, organising meetings - That kind of drudgery!"
            MC "Do you enjoy it?"

            scene LiR1_MAS1a_p4

            Liza2 "Eh... not really. But it pays the bills. Does anyone really love their job?"
            Yazmin "I could always get you into my line of work. There’s plenty of work for models in-"
            Liza2 "No! I don’t have the body for that!"

            $ q2 = False
            jump LiR1_MAS1a_menu
        "{color=#00ff00}Did you want me to come over, to take a look at your swimming pool?{/color}":

            scene LiR1_MAS1a_p6

            MC "Did you want me to take a look at your swimming pool? I’m pretty good with my hands, and I can probably get it cleaned up for you, pretty quickly!"
            Liza2 "Definitely! It’s an absolute pigsty, right now! I’m happy to pay you, if you can maintain it for us, regularly."

            scene LiR1_MAS1a_p7

            MC "Sure - happy to help. Out of interest... did you not think about, hiring a professional maid or handyman, to do this?"
            if renpy.loadable("patch.rpy"):
                Yazmin "Yeah... your aunt hired a handyman, a month ago. Tell [player_name] what happened, Liza."
            else:
                Yazmin "Yeah... Liza hired a handyman, a month ago. Tell [player_name] what happened, Liza."
            Liza2 "(Sigh) I caught the bastard stealing my underwear, when it was drying on the line."
            MC "Haha! Wow! That’s insane!"
            if renpy.loadable("patch.rpy"):
                Liza2 "So yeah - in order to avoid any more... inappropriate situations, I’ve decided to reserve this particular job, in the family. Does that make sense?"
            else:
                Liza2 "So yeah - in order to avoid any more... inappropriate situations, I’ve decided to reserve this particular job, for someone I know personaly. Does that make sense?"

            scene LiR1_MAS1a_p8

            MC "Yeah, I understand completely. I’d be creeped out too, if someone was stealing MY underwear."
            Liza2 "Great! When are you free to start?"
            MC "Whenever you want."

            scene LiR1_MAS1a_p10

            Liza2 "Hmm... In that case, you can start tomorrow. We have all the cleaning stuff you’ll need, in the garage."
            Liza2 "The handyman left it behind, when Yazmin chased him away. He hasn’t shown up to collect it - so I guess it’s ours now."
            MC "Cool! I’ll go and grab that."

            scene LiR1_MAS1a_p11

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)

            Yazmin "It’s going to be so nice to be able to use our pool, together again. Especially with the warmer weather we’ve been having."
            Liza "If he finishes it tomorrow, perhaps you and me could take a swim together, tomorrow night. How does that sound?"
            Yazmin "Absolutely perfect, darling."
            Yazmin "But unfortunately, I think it will take him more than one day, to clean the whole pool, though."
            Liza "I can wait... If you keep me occupied, the whole time..."

            scene LiR1_MAS1a_p12

            Liza "I love you so much."
            Yazmin "I love you too, my sugar pie."
            MC "(Hmm... Well, this is starting to get a little bit awkward...)"

            scene LiR1_MAS1a_p13

            MC "(They’re not going to - seriously - start making out in front of me... are they?)"
            if renpy.loadable("patch.rpy"):
                MC "(I mean, Auntie Liza and Yazmin have been married for quite a few years now - but they’re not going to just start snogging each other, right in front of their nephew.)"
            else:
                MC "(I mean, Liza and Yazmin have been married for quite a few years now - but they’re not going to just start snogging each other, right in front of me.)"
            Yazmin "Mmm..."

            scene LiR1_MAS1a_p14

            Liza "Mmm!"
            Yazmin "Ohmmmm!"
            MC "(And... I guess it’s time for me to leave.)"

            scene LiR1_MAS1a_p15

            MC "I’ll... erm... just go. I’ll be back tomorrow, to start cleaning the swimming pool. Okay?"
            Yazmin "Mmm!"
            MC "(Yeah, I don’t think they can hear me. I’ll just sneak out...) "
            scene black
            $ q1 = False
            $ q2 = False

            $ LiR1_MAS1a = False
            $ LiR1_MAS2 = True
            $ LiR1_MAS3 = True
            $ can_LiR1_MAS2 = False
            $ can_LiR1_MAS3 = False
            $ Li_door_locked = True
            $ LiR1_poll_minigame = True
            $ LiR1_poll_minigame_can = 0

            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
            $ renpy.pause(1.5, hard = True)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump a_home_outside_M1
