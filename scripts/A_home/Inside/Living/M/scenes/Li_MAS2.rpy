image LiR1_MAS2_p1 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/1.jpg"
image LiR1_MAS2_p2 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/2.jpg"
image LiR1_MAS2_p3 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/3.jpg"
image LiR1_MAS2_p4 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/4.jpg"
image LiR1_MAS2_p5 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/5.jpg"
image LiR1_MAS2_p6 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/6.jpg"
image LiR1_MAS2_p7 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/7.jpg"
image LiR1_MAS2_p8 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/8.jpg"
image LiR1_MAS2_p9 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/9.jpg"
image LiR1_MAS2_p10 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/10.jpg"
image LiR1_MAS2_p11 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/11.jpg"
image LiR1_MAS2_p12 = "images/a_home/Inside/Living/M/Scenes/LiR1_MAS2/12.jpg"

label Li_MAS2_label:
    if renpy.loadable("patch.rpy"):
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene LiR1_MAS2_p1 with dissolve

    MC "Hey, [Liza2_name]. How’re you doing?"
    Liza2 "Hi, [player_name]! Not too bad! What’s up?"
    MC "I just had a few minutes free, so I thought I’d drop by to say hello!"
    Liza2 "Aww, that’s sweet. Take a seat!"

    if Li_MAS2_menu_visit <2:
        scene LiR1_MAS2_p2

        Liza2 "What’s new with you, then? Anything exciting or interesting, happening in your life?"
        MC "(Almost everything is too private or lewd for me to tell her! I better change the conversation topic, before I let something slip about my current romantic entanglements, or that cringeworthy kerfuffle with my teacher!)"
        MC "Err... nothing much."

    jump Li_MAS2_menu

label Li_MAS2_menu:
    if renpy.loadable("patch.rpy"):
        $ Mom_name = __("Mom")
        $ Liza2_name = __("Auntie")
    else:
        $ Mom_name = "Linda"
        $ Liza2_name = "Liza"

    scene LiR1_MAS2_p2
    menu:
        "How long have you and Yazmin been married?" if Li_MAS2_q1 == True:
            scene LiR1_MAS2_p3

            MC "So, how long have you and Yazmin been married?"

            scene LiR1_MAS2_p4

            Liza2 "Oh wow... It must be... five or six years, now. Wait - it’s definitely six. We celebrated our - five year anniversary - last July."
            MC "That’s lovely to hear."

            scene LiR1_MAS2_p3

            Liza2 "I know! Yazmin’s like a - dream come true!"
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q1 = False
            jump Li_MAS2_menu

        "How come [Mom_name] and you, don’t really hang out, that often?" if Li_MAS2_q2 == True:
            scene LiR1_MAS2_p2

            MC "How come [Mom_name] and you, don’t really hang out, that often?"

            scene LiR1_MAS2_p5

            Liza2 "..."
            MC "[Liza2_name]?"
            Liza2 "We DO hang out!"
            MC "But-"
            Liza2 "You saw me at your house, the other morning, right?"

            scene LiR1_MAS2_p6

            Liza2 "We’re both adults with... full time jobs, and we’re... um... very busy people."
            Liza2 "I mean, Linda owns her own business, for Christ’s sake!"
            if renpy.loadable("patch.rpy"):
                MC "(What’s going on?! I’ve clearly struck a nerve here! I should probably leave this topic alone, until I get to know Auntie Liza better.)"
            else:
                MC "(What’s going on?! I’ve clearly struck a nerve here! I should probably leave this topic alone, until I get to know Liza better.)"
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q2 = False
            jump Li_MAS2_menu

        "How did you and Yazmin meet?" if Li_MAS2_q3 == True:
            scene LiR1_MAS2_p2

            MC "How did you and Yazmin meet each other?"

            scene LiR1_MAS2_p9

            Liza2 "Well... I was a freshman in college - almost nineteen years old. I was heavily involved in my local sorority. The building we lived in was a wreck - it hadn’t been properly maintained, in decades!"
            Liza2 "Anyway - the President of the sorority, organised a cleanup project. I volunteered to do some painting - and Yazmin got assigned to my group. It ended up just being - me and her - painting the second floor."
            MC "Aww, that’s really nice? What happened next?"

            scene LiR1_MAS2_p8

            Liza2 "(Honestly? She pushed me, up against the wall and started making out with me, before she’d even asked my name.)"
            Liza2 "(I was wearing these really tight leggings, and she STILL somehow managed, to slip her hand inside them. God... she had me soaking my panties, for almost an hour.)"

            scene LiR1_MAS2_p6

            Liza2 "Err... She asked me out for coffee, and we went to the local Barstucks, for our first date."
            MC "Aww, that sounds really sweet!"
            Liza2 "Yeah, it was... exhilarating."
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q3 = False
            jump Li_MAS2_menu

        "How did [Mom_name] react, when she found out you were a lesbian?" if Li_MAS2_q4 == True:

            scene LiR1_MAS2_p4

            MC "So, how did [Mom_name] react, when she found out you were a lesbian?"

            scene LiR1_MAS2_p5

            Liza2 "It wasn’t - me being a lesbian - that bothered her!"
            MC "(Huh... What a strange way to phrase her answer. Why didn’t she just say that it didn’t bother [Mom_name]?)"
            Liza2 "You know, Linda isn’t as - straight - as she makes herself out to be. She was a real locomotive, back in her youth!"
            MC "A... locomotive?"
            Liza2 "Yeah - she could go both ways."
            MC "Oh, I understand now. What did you mean when you said, “It wasn’t me being a lesbian that bothered her!” Was there something else that bothered [Mom_name]?"

            scene LiR1_MAS2_p7
            if renpy.loadable("patch.rpy"):
                Liza2 "Ah... I misspoke. I MEANT to say that it didn’t bother my sister at all, at the time."
            else:
                Liza2 "Ah... I misspoke. I MEANT to say that it didn’t bother Linda at all, at the time."
            MC "At the time?"
            Liza2 "Err - I think we should change the subject. This isn’t appropriate for us to be discussing."
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q4 = False
            jump Li_MAS2_menu

        "Are you two planning to have a child?" if Li_MAS2_q5 == True:
            scene LiR1_MAS2_p2

            MC "Are you and Yazmin planning to have a child, in the future?"

            scene LiR1_MAS2_p6

            Liza2 "I guess the thought, has... crossed my mind, once or twice. It would be nice to have - a little one - to take care of, once we get settled down."
            MC "That’s awesome! Have you thought about how you’ll do it?"
            Liza2 "My mind has been so set on - the end result - that I haven’t really thought about the process, at all. I wouldn’t mind doing - IVF - as long as Yazmin could support us both, financially."

            scene LiR1_MAS2_p9

            Liza2 "Then again... there are A LOT of young children, who need adopting. We could help, change a life."
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q5 = False
            jump Li_MAS2_menu

        "Are you enjoying your job? You mentioned you were a secretary for a law firm, didn’t you?" if Li_MAS2_q6 == True:
            scene LiR1_MAS2_p2

            MC "Are you enjoying your job? You mentioned you were a secretary for a law firm, didn’t you?"

            scene LiR1_MAS2_p9

            Liza2 "It’s alright - but I’m keeping an eye open for other posts."
            MC "Have you thought about becoming a paralegal?"
            Liza2 "It’s funny you should mention that - My firm, actually offers training to become paralegals."
            Liza2 "I was thinking of - taking them up - on the offer. The only downside is, that you have to go to nightschool."
            MC "Ugh... sounds rough. Is the pay any better?"

            scene LiR1_MAS2_p3

            Liza2 "About $5,000 more, per annum. Not too shabby!"
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q6 = False
            jump Li_MAS2_menu

        "What’s REALLY going on, between you and [Mom_name]? You hardly ever visit each other." if Li_MAS2_q7 == True:

            scene LiR1_MAS2_p4

            MC "What’s REALLY going on, between you and [Mom_name]? You hardly ever visit each other."

            scene LiR1_MAS2_p6

            Liza2 "*Sigh* You asked me about this, a few days ago."
            MC "You weren’t completely honest with me, were you?"
            Liza2 "... No."
            MC "Hmm... I thought so."

            scene LiR1_MAS2_p8
            if renpy.loadable("patch.rpy"):
                Liza2 "My sister and I... We were always so close. We did everything together."
            else:
                Liza2 "Linda and I... We were always so close. We did everything together."

            Liza2 "She never minded that I was gay."
            if renpy.loadable("patch.rpy"):
                Liza2 "She never minded when I snuck girls home without Mom and Dad knowing."
            Liza2 "It all changed, when Linda met Yazmin. She took an intense, irrational dislike towards her."

            scene LiR1_MAS2_p5

            Liza2 "And when I told Linda that Yazmin and I were engaged, she had the AUDACITY to tell me, that I needed to grow out of my ‘gay phase’."
            Liza2 "I mean - how damn rude can you be?!"
            MC "Oh, my God... I’m so sorry, [Liza2_name]..."

            scene LiR1_MAS2_p6
            if renpy.loadable("patch.rpy"):
                Liza2 "Your mom and me, barely spoke after that. Months went by - when we didn’t exchange a word. You might have noticed that we didn’t really interact, at the beach barbeque, all those years ago."
            else:
                Liza2 "Linda and me, barely spoke after that. Months went by - when we didn’t exchange a word. You might have noticed that we didn’t really interact, at the beach barbeque, all those years ago."
            MC "Yeah - come to mention it - that makes sense."
            if renpy.loadable("patch.rpy"):
                Liza2 "Things have thawed, since then, but I try to keep Yazmin out of the picture. There’s no need to antagonise my sister, any more than, my wedding ring already does. I think she views Yazmin - as stealing away her best friend."
            else:
                Liza2 "Things have thawed, since then, but I try to keep Yazmin out of the picture. There’s no need to antagonise Linda, any more than, my wedding ring already does. I think she views Yazmin - as stealing away her best friend."
            if renpy.loadable("patch.rpy"):
                Liza2 "So yeah - that’s the story, with all the gory details. There are a few other things your mother may have called - Yazmin and I - but they don't need repeating. There’s no sense in reopening old wounds."
            else:
                Liza2 "So yeah - that’s the story, with all the gory details. There are a few other things Linda may have called - Yazmin and I - but they don't need repeating. There’s no sense in reopening old wounds."
            MC "I’m... so sorry. I never realised."
            Liza2 "It’s okay. We’re slowly getting over it."
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q7 = False
            jump Li_MAS2_menu

        "You feel nothing towards men?" if Li_MAS2_q8 == True:
            scene LiR1_MAS2_p7

            MC "So, you feel nothing towards men?"
            Liza2 "Wow! That’s quite a... personal question."
            MC "I’m just curious! Sorry, I didn’t mean to offend you."
            Liza2 "N-No, you didn’t offend me."

            scene LiR1_MAS2_p8

            Liza2 "Umm... What’s the best way to explain this? Hmm..."
            Liza2 "Have you ever heard of the Kinsey Scale?"
            MC "I’m not familiar with it."
            Liza2 "It’s a scale to measure sexuality. It runs from one to six. Someone who is a one on the scale is ONLY attracted to the opposite sex. Someone who is a six, is exclusively attracted to the same sex."

            scene LiR1_MAS2_p2

            MC "Ah, so ones are straight and sixes are gay?"
            Liza2 "Bingo!"
            MC "So, where do you fall, on that scale?"

            scene LiR1_MAS2_p9

            Liza2 "I’m basically a six. Maybe a five point five - at a push. I can count the number of men that I have found sexually attractive, in my whole life, on one hand. Haha!"
            MC "What about me?"

            scene LiR1_MAS2_p8

            Liza2 "What do you mean?"
            MC "Do you find me attractive?"
            Liza2 "Umm... That’s a little awkward to answer, don’t you think?"
            MC "I’m just curious! This is the first time I’ve ever heard about this Kinder Scale stuff!"
            Liza2 "Kin-SEY scale. And... honestly - not really. Perhaps if you had, long dark hair, C-Cup breasts, and a vagina. I might find you attractive."
            MC "(Damn, it really doesn’t sound like there’s much hope, for me seducing her!)"
            if can_LiR1_MAS2 == True:
                $ Li_MAS2_menu_visit += 1
                $ can_LiR1_MAS2 = False
            $ Li_MAS2_q8 = False
            jump Li_MAS2_menu

        "{color=#00ff00}I finished cleaning the pool.{/color}" if LiR1_poll_event_end == True:

            scene LiR1_MAS2_p11

            MC "That’s me finished cleaning the pool, by the way!"
            Liza2 "Really?! Fantastic work!"
            Liza2 "You’re such a great help! It’s nice to have someone around the house, that I can put my trust in!"

            scene LiR1_MAS2_p12

            Liza2 "*Mwah!*"
            if renpy.loadable("patch.rpy"):
                MC "Aww, thanks, Auntie Liza!"
            else:
                MC "Aww, thanks, Liza!"
            Liza2 "The pool gets dirty, very quickly - feel free to drop by, if you want to earn some more cash."
            MC "Will do! Catch you later, [Liza2_name]!"
            $ LiR1_poll_event_end = False
            $ LiR1_MAS6_can1 = True
            jump Li_MAS2_menu
        "Bye." if Li_MAS2_menu_visit >1:
            MC "Well, I’ve taken up enough of your time. I should probably head on."
            MC "See you later, [Liza2_name]."
            Liza2 "Bye, [player_name]."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump a_living_M1
