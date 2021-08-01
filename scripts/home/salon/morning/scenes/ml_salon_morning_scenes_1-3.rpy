image ml_morning_salon_scene1_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/1.jpg"
image ml_morning_salon_scene1_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/2.jpg"
image ml_morning_salon_scene1_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/3.jpg"
image ml_morning_salon_scene1_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/4.jpg"
image ml_morning_salon_scene1_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/5.jpg"
image ml_morning_salon_scene1_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/6.jpg"
image ml_morning_salon_scene1_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/7.jpg"
image ml_morning_salon_scene1_v1_p8 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/8.jpg"
image ml_morning_salon_scene1_v1_p9 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/9.jpg"
image ml_morning_salon_scene1_v1_p10 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/10.jpg"

image ml_morning_salon_scene2_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/1.jpg"

image ml_morning_salon_scene3_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/1.jpg"
image ml_morning_salon_scene3_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/2.jpg"
image ml_morning_salon_scene3_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/3.jpg"
image ml_morning_salon_scene3_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/4.jpg"
image ml_morning_salon_scene3_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/5.jpg"
image ml_morning_salon_scene3_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/6.jpg"
image ml_morning_salon_scene3_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/7.jpg"
image ml_morning_salon_scene3_v1_p8 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/8.jpg"
image ml_morning_salon_scene3_v1_p9 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/9.jpg"
image ml_morning_salon_scene3_v1_p10 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/10.jpg"
image ml_morning_salon_scene3_v1_p11 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/11.jpg"
image ml_morning_salon_scene3_v1_p12 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/12.jpg"
image ml_morning_salon_scene3_v1_p13 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/13.jpg"
image ml_morning_salon_scene3_v1_p14 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/14.jpg"
image ml_morning_salon_scene3_v1_p15 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/15.jpg"

screen ml_morning_salon_scenes1to3_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_morning_salon_scenes1to3_v1_screen"),Jump("salon_morning1")]

label ml_morning_salon_scenes1to3_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_salon_morning_scene_dish_wash == True and ml_can_salon_morning_scene == False:
        show screen salon_morning
        show screen ml_morning_salon_scenes1to3_v1_screen
        MC "I should go wash the dishes."
        jump salon_morning1
    if ml_can_salon_morning_scene == False:
        show screen salon_morning
        show screen ml_morning_salon_scenes1to3_v1_screen
        MC "I've already talked to her."
        jump salon_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    if ml_salon_morning_visit == 1 and ml_can_salon_morning_scene == True:
        scene ml_morning_salon_scene1_v1_p1 with dissolve
        Television "...are in a high speed pursuit with three masked men."
        Television "The vehicle was stolen from a local bank parking lot."

        if persistent.incest_patch == True:
            MC "(Looks like Mom’s watching the morning news.)"
            scene ml_morning_salon_scene1_v1_p2
            MC "Morning, Mom!"
        else:
            MC "(Looks like Linda’s watching the morning news.)"

            scene ml_morning_salon_scene1_v1_p2
            MC "Morning, Linda!"
        Mom "Good morning, [player_name]. Where are you off to?"
        MC "It’s a school day, remember?"
        Mom "Oh! Right."
        Mom "You’ve still got some time. Come and sit beside me for a while."
        MC "Uh, okay."

        scene ml_morning_salon_scene1_v1_p3
        MC "I’ve only got a few minutes - I can’t stay too long, or I’ll-"
        Mom "I know - you’ll be late for class."
        Mom "I’m going to teach you a very important lesson right now. One that you should have learnt YEARS ago."
        if persistent.incest_patch == True:
            Mom "Never let your work get in the way of, quality family time."
        else:
            Mom "Never let your work get in the way of, quality friendships."

        scene ml_morning_salon_scene1_v1_p4
        if persistent.incest_patch == True:
            Mom "Even if that means, just a few minutes in front of the TV with your son, before he goes to school."
        else:
            Mom "Even if that means, just a few minutes in front of the TV with me, before you go to school."
        MC "Uh… Okay. I’ll remember that."
        Mom "Please do. Your own children will thank you for it someday."

        scene ml_morning_salon_scene1_v1_p5
        if persistent.incest_patch == True:
            MC "(Holy shit! Mom’s not wearing a bra!)"
        else:
            MC "(Holy shit! Linda’s not wearing a bra!)"
        MC "(Why isn’t she wearing one?!)"
        MC "(She’s leaning so close that I can almost feel her left nipple!)"
        Mom "...and I’ll never make that mistake again."

        scene ml_morning_salon_scene1_v1_p6
        Mom "Are you listening, [player_name]?"
        MC "Huh?! Oh! Y-Yeah!"
        Mom "Here, let me give you a kiss, before you rush off to class."

        scene ml_morning_salon_scene1_v1_p7
        MC "(Uh oh… Is she going to-)"
        MC "(Oh, it’s just on the cheek. My heart started racing there!)"
        if persistent.incest_patch == True:
            MC "(Maybe I am over analyzing things? Perhaps that kiss before, was her being a loving mother?)"
        else:
            MC "(Maybe I am over analyzing things? Perhaps that kiss before, was her being a loving friend?)"
        MC "(I’ve got to stop replaying it in my mind.)"

        scene ml_morning_salon_scene1_v1_p8
        MC "(Huh?! She’s turning my head! This ISN’T a peck on the cheek!)"
        MC "(What should I do?!)"
        if persistent.incest_patch == True:
            MC "(I can’t kiss her back like this - she’s my mother! It’s FAR too intimate!)"
        else:
            MC "(I can’t kiss her back like this - she’s my friend! It’s FAR too intimate!)"
        scene ml_morning_salon_scene1_v1_p9
        Mom "Mmm…"
        MC "(She’s biting my lower lip!)"
        MC "(That’s it - any chances of this just being a regular kiss are out the window.)"

        scene ml_morning_salon_scene1_v1_p10
        Mom "(Oh fuck! I almost did it again!)"
        Mom "I- um… I have to rush to work now. See you tonight!"
        if persistent.incest_patch == True:
            MC "Uh… S-See you later, Mom…"
        else:
            MC "Uh… S-See you later, Linda…"
        Mom "(Maybe I got lucky, and I broke off the kiss off before he got suspicious?)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_salon_morning_visit = 2
        $ ml_can_salon_morning_scene = False
        $ ml_can_salon_morning_scene2 = False
        jump salon_morning1

    if ml_salon_morning_visit == 2 and ml_can_salon_morning_scene == True:

        scene ml_morning_salon_scene2_v1_p1 with dissolve
        Mom "Morning, [player_name]."
        if persistent.incest_patch == True:
            MC "Hey, Mom."
        else:
            MC "Hey, Linda."
        Mom "Are you about to leave for school?"
        MC "In a few minutes, yeah."
        Mom "Do you have time to wash a few dishes before you go?"
        menu:
            "Yes":

                MC "Sure, no problem."
                Mom "Thanks! You’re a sweetie."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_can_salon_morning_scene = False
                $ ml_can_salon_morning_scene_dish_wash = True
                jump salon_morning1
            "No":

                if persistent.incest_patch == True:
                    MC "Sorry, Mom. I’m in a bit of a rush. I can’t afford to be late."
                    Mom "Don’t worry, I’ll get them later. Enjoy your day!"
                    MC "Thanks, Mom!"
                else:
                    MC "Sorry, Linda. I’m in a bit of a rush. I can’t afford to be late."
                    Mom "Don’t worry, I’ll get them later. Enjoy your day!"
                    MC "Thanks, Linda!"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_can_salon_morning_scene = False
                jump salon_morning1

    if ml_salon_morning_visit == 3 and ml_can_salon_morning_scene == True:
        scene ml_morning_salon_scene3_v1_p1 with dissolve
        if persistent.incest_patch == True:
            MC "Morning, Mom! I’m heading to school now."
        else:
            MC "Morning, Linda! I’m heading to school now."
        Mom "Wait - don’t go yet!"

        scene ml_morning_salon_scene3_v1_p2
        Mom "Sit with me awhile."
        MC "I don’t want to be late."
        Mom "You won’t be late - just a few minutes."
        MC "Okay."

        scene ml_morning_salon_scene3_v1_p3
        Mom "So, have you got your eye on any girls right now?"

        menu:
            "I’ve seen a few cute ones around.":

                scene ml_morning_salon_scene3_v1_p4
                MC "I’ve seen a few cute girls about. You know how guys are."
                Mom "Oooh, I hope you’re not going to turn into one of those playboys who chases all the girls!!"
                if persistent.incest_patch == True:
                    MC "Mom!"
                else:
                    MC "Linda!"
                Mom "Hehe, I’m just teasing you."
                scene ml_morning_salon_scene3_v1_p5
                if persistent.incest_patch == True:
                    Mom "You know that no matter what you do, I’ll always be proud of my boy."
                else:
                    Mom "You know that no matter what you do, I’ll always be proud of my little guy."
                if persistent.incest_patch == True:
                    MC "Haha! You’re gonna make me blush, Mom."
                else:
                    MC "Haha! You’re gonna make me blush, Linda."
                MC "(She seems… different today. I wonder what’s gotten into her.)"

                scene ml_morning_salon_scene3_v1_p6
                if persistent.incest_patch == True:
                    MC "Umm… Mom?"
                else:
                    MC "Umm… Linda?"
                Television "Up next - are lattes making you fat? Barry McSwindon investigates."
                Mom "(Slowly does it… I’m going to move my hand, right up to his crotch and see how he reacts.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "The truth is, Barry - drinking more than fifty lattes a day, greatly increases your risk of obesity."
                Television "But, Sonja - who the hell drinks fifty cups of coffee a day?!"
                Television "That’s not the point I’m trying to make, Barry."
                if persistent.incest_patch == True:
                    MC "(Mom looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                else:
                    MC "(Linda looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(HUH?!)"
                Television "A typical latte from StarFucks has 190 calories. If you multiply that by fifty-"
                Television "Jesus Fucking Christ, Sonja! You’re missing the point!"

                scene ml_morning_salon_scene3_v1_p9
                if persistent.incest_patch == True:
                    MC "M-Mom! Your hand!"
                else:
                    MC "L-Linda! Your hand!"
                Mom "Huh? Oops! Sorry, I was trying to grab your arm. I thought you had it resting on your lap."
                Mom "I should have looked."

                scene ml_morning_salon_scene3_v1_p10
                MC "Why did you want to grab my arm?"
                Mom "Here, let me show you."

                scene ml_morning_salon_scene3_v1_p11
                MC "What?!"
                Mom "Do you feel that?"
                MC "Y-Yeah - but I don’t think I should!"
                Mom "My heartbeat."
                MC "Oh! R-Right."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Do you feel, how fast it beats around you?"
                Mom "It’s only around you. You’re special to me."
                if persistent.incest_patch == True:
                    MC "M-Mom…"
                else:
                    MC "L-Linda…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Always remember my heartbeat, and you’ll know how much you mean to me."
                Mom "I really do love you, [player_name]."
                if persistent.incest_patch == True:
                    MC "I will, Mom."
                else:
                    MC "I will, Linda."
                MC "(What’s gotten into her today? I’ve never seen her act this emotionally before.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Okay, you better get to school. I’m gonna make you late."
                if persistent.incest_patch == True:
                    MC "It’s okay, Mom."
                else:
                    MC "It’s okay, Linda."
                Mom "See you later on."

                scene ml_morning_salon_scene3_v1_p15
                if persistent.incest_patch == True:
                    MC "Bye, Mom. See you later…"
                else:
                    MC "Bye, Linda. See you later…"
                MC "(She’s acting really bizarre lately. I wonder if there’s something she’s not telling me.)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1
            "Just one right now.":
                scene ml_morning_salon_scene3_v1_p4
                MC "I’ve kinda got my eye on one right now."
                Mom "Oh… You do?"
                MC "Yeah. Are you alright?"
                Mom "Oh yeah! I’m fine! I’m great."
                scene ml_morning_salon_scene3_v1_p5
                if persistent.incest_patch == True:
                    Mom "You know that no matter what you do, I’ll always be proud of my boy."
                else:
                    Mom "You know that no matter what you do, I’ll always be proud of my little guy."
                if persistent.incest_patch == True:
                    MC "Haha! You’re gonna make me blush, Mom."
                else:
                    MC "Haha! You’re gonna make me blush, Linda."
                MC "(She seems… different today. I wonder what’s gotten into her.)"

                scene ml_morning_salon_scene3_v1_p6
                if persistent.incest_patch == True:
                    MC "Umm… Mom?"
                else:
                    MC "Umm… Linda?"
                Television "Up next - are lattes making you fat? Barry McSwindon investigates."
                Mom "(Slowly does it… I’m going to move my hand, right up to his crotch and see how he reacts.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "The truth is, Barry - drinking more than fifty lattes a day, greatly increases your risk of obesity."
                Television "But, Sonja - who the hell drinks fifty cups of coffee a day?!"
                Television "That’s not the point I’m trying to make, Barry."
                if persistent.incest_patch == True:
                    MC "(Mom looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                else:
                    MC "(Linda looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(HUH?!)"
                Television "A typical latte from StarFucks has 190 calories. If you multiply that by fifty-"
                Television "Jesus Fucking Christ, Sonja! You’re missing the point!"

                scene ml_morning_salon_scene3_v1_p9
                if persistent.incest_patch == True:
                    MC "M-Mom! Your hand!"
                else:
                    MC "L-Linda! Your hand!"
                Mom "Huh? Oops! Sorry, I was trying to grab your arm. I thought you had it resting on your lap."
                Mom "I should have looked."

                scene ml_morning_salon_scene3_v1_p10
                MC "Why did you want to grab my arm?"
                Mom "Here, let me show you."

                scene ml_morning_salon_scene3_v1_p11
                MC "What?!"
                Mom "Do you feel that?"
                MC "Y-Yeah - but I don’t think I should!"
                Mom "My heartbeat."
                MC "Oh! R-Right."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Do you feel, how fast it beats around you?"
                Mom "It’s only around you. You’re special to me."
                if persistent.incest_patch == True:
                    MC "M-Mom…"
                else:
                    MC "L-Linda…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Always remember my heartbeat, and you’ll know how much you mean to me."
                Mom "I really do love you, [player_name]."
                if persistent.incest_patch == True:
                    MC "I will, Mom."
                else:
                    MC "I will, Linda."
                MC "(What’s gotten into her today? I’ve never seen her act this emotionally before.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Okay, you better get to school. I’m gonna make you late."
                if persistent.incest_patch == True:
                    MC "It’s okay, Mom."
                else:
                    MC "It’s okay, Linda."
                Mom "See you later on."

                scene ml_morning_salon_scene3_v1_p15
                if persistent.incest_patch == True:
                    MC "Bye, Mom. See you later…"
                else:
                    MC "Bye, Linda. See you later…"
                MC "(She’s acting really bizarre lately. I wonder if there’s something she’s not telling me.)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1
            "No, I’d rather be single for a while.":
                scene ml_morning_salon_scene3_v1_p4
                MC "Nah, I’d rather be single for a while. Especially after that embarrassing situation with Mrs. Celia."
                Mom "Good."
                MC "Good?"
                Mom "Err… I mean, it’s good that you’re… taking things slow and recovering."
                MC "Oh, right."

                scene ml_morning_salon_scene3_v1_p5
                if persistent.incest_patch == True:
                    Mom "You know that no matter what you do, I’ll always be proud of my boy."
                else:
                    Mom "You know that no matter what you do, I’ll always be proud of my little guy."
                if persistent.incest_patch == True:
                    MC "Haha! You’re gonna make me blush, Mom."
                else:
                    MC "Haha! You’re gonna make me blush, Linda."
                MC "(She seems… different today. I wonder what’s gotten into her.)"

                scene ml_morning_salon_scene3_v1_p6
                if persistent.incest_patch == True:
                    MC "Umm… Mom?"
                else:
                    MC "Umm… Linda?"
                Television "Up next - are lattes making you fat? Barry McSwindon investigates."
                Mom "(Slowly does it… I’m going to move my hand, right up to his crotch and see how he reacts.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "The truth is, Barry - drinking more than fifty lattes a day, greatly increases your risk of obesity."
                Television "But, Sonja - who the hell drinks fifty cups of coffee a day?!"
                Television "That’s not the point I’m trying to make, Barry."
                if persistent.incest_patch == True:
                    MC "(Mom looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                else:
                    MC "(Linda looks engrossed in her show… I don’t think she’s paying attention to what she’s doing.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(HUH?!)"
                Television "A typical latte from StarFucks has 190 calories. If you multiply that by fifty-"
                Television "Jesus Fucking Christ, Sonja! You’re missing the point!"

                scene ml_morning_salon_scene3_v1_p9
                if persistent.incest_patch == True:
                    MC "M-Mom! Your hand!"
                else:
                    MC "L-Linda! Your hand!"
                Mom "Huh? Oops! Sorry, I was trying to grab your arm. I thought you had it resting on your lap."
                Mom "I should have looked."

                scene ml_morning_salon_scene3_v1_p10
                MC "Why did you want to grab my arm?"
                Mom "Here, let me show you."

                scene ml_morning_salon_scene3_v1_p11
                MC "What?!"
                Mom "Do you feel that?"
                MC "Y-Yeah - but I don’t think I should!"
                Mom "My heartbeat."
                MC "Oh! R-Right."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Do you feel, how fast it beats around you?"
                Mom "It’s only around you. You’re special to me."
                if persistent.incest_patch == True:
                    MC "M-Mom…"
                else:
                    MC "L-Linda…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Always remember my heartbeat, and you’ll know how much you mean to me."
                Mom "I really do love you, [player_name]."
                if persistent.incest_patch == True:
                    MC "I will, Mom."
                else:
                    MC "I will, Linda."
                MC "(What’s gotten into her today? I’ve never seen her act this emotionally before.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Okay, you better get to school. I’m gonna make you late."
                if persistent.incest_patch == True:
                    MC "It’s okay, Mom."
                else:
                    MC "It’s okay, Linda."
                Mom "See you later on."

                scene ml_morning_salon_scene3_v1_p15
                if persistent.incest_patch == True:
                    MC "Bye, Mom. See you later…"
                else:
                    MC "Bye, Linda. See you later…"
                MC "(She’s acting really bizarre lately. I wonder if there’s something she’s not telling me.)"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1

