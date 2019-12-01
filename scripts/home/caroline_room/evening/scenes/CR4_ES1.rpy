image CR4_ES1_p1 = "/images/home/caroline_room/evening/scenes/CR4_ES1/1.jpg"
image CR4_ES1_p2 = "/images/home/caroline_room/evening/scenes/CR4_ES1/2.jpg"
image CR4_ES1_p3 = "/images/home/caroline_room/evening/scenes/CR4_ES1/3.jpg"
image CR4_ES1_p4 = "/images/home/caroline_room/evening/scenes/CR4_ES1/4.jpg"
image CR4_ES1_p5 = "/images/home/caroline_room/evening/scenes/CR4_ES1/5.jpg"
image CR4_ES1_p6 = "/images/home/caroline_room/evening/scenes/CR4_ES1/6.jpg"
image CR4_ES1_p7 = "/images/home/caroline_room/evening/scenes/CR4_ES1/7.jpg"
image CR4_ES1_p7a = "/images/home/caroline_room/evening/scenes/CR4_ES1/7a.jpg"
image CR4_ES1_p7b = "/images/home/caroline_room/evening/scenes/CR4_ES1/7b.jpg"
image CR4_ES1_p8 = "/images/home/caroline_room/evening/scenes/CR4_ES1/8.jpg"
image CR4_ES1_p9 = "/images/home/caroline_room/evening/scenes/CR4_ES1/9.jpg"
image CR4_ES1_p10 = "/images/home/caroline_room/evening/scenes/CR4_ES1/10.jpg"
image CR4_ES1_p11 = "/images/home/caroline_room/evening/scenes/CR4_ES1/11.jpg"
image CR4_ES1_p12 = "/images/home/caroline_room/evening/scenes/CR4_ES1/12.jpg"
image CR4_ES1_p13 = "/images/home/caroline_room/evening/scenes/CR4_ES1/13.jpg"
image CR4_ES1_p14 = "/images/home/caroline_room/evening/scenes/CR4_ES1/14.jpg"
image CR4_ES1_p15 = "/images/home/caroline_room/evening/scenes/CR4_ES1/15.jpg"
image CR4_ES1_p16 = "/images/home/caroline_room/evening/scenes/CR4_ES1/16.jpg"
image CR4_ES1_p17 = "/images/home/caroline_room/evening/scenes/CR4_ES1/17.jpg"
image CR4_ES1_p18 = "/images/home/caroline_room/evening/scenes/CR4_ES1/18.jpg"

image CR4_ES1_kiss_p1 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/1.jpg"
image CR4_ES1_kiss_p2 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/2.jpg"
image CR4_ES1_kiss_p3 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/3.jpg"
image CR4_ES1_kiss_p4 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/4.jpg"
image CR4_ES1_kiss_p4anim = Movie(play="videos/06 Caroline ES1-1.webm", loop = True )
image CR4_ES1_kiss_p5 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/5.jpg"
image CR4_ES1_kiss_p6 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/6.jpg"
image CR4_ES1_kiss_p6anim = Movie(play="videos/06 Caroline ES1-2.webm", loop = True )
image CR4_ES1_kiss_p7 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/7.jpg"
image CR4_ES1_kiss_p9 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/9.jpg"
image CR4_ES1_kiss_p10 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/10.jpg"
image CR4_ES1_kiss_p11 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/11.jpg"
image CR4_ES1_kiss_p12 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/12.jpg"
image CR4_ES1_kiss_p13 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/13.jpg"
image CR4_ES1_kiss_p14 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/14.jpg"
image CR4_ES1_kiss_p15 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/15.jpg"
image CR4_ES1_kiss_p16 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/16.jpg"
image CR4_ES1_kiss_p17 = "/images/home/caroline_room/evening/scenes/CR4_ES1/Kissing/17.jpg"



default CR4_ES1 = False
default CR4_ES1_q1 = True
default CR4_ES1_q2 = False
default CR4_ES1_q3 = True
default CR4_ES1_q4 = False
default CR4_ES1_q5 = False
default CR4_ES1_q6 = True
default CR4_ES1_q7 = True
default CR4_ES1_q8 = False
label CR4_ES1_label:
    if CR4_ES1 == 2:

        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene CR4_ES1_p1 with dissolve
        MC "(Looks like Caroline is kicking back and relaxing, for a change!)"
        MC "(It’s certainly better than her, constantly being uptight all the time.)"
        MC "Hey there, Caroline. How are things?"

        scene CR4_ES1_p2
        Caroline "Oh hey, come on in! Make yourself comfortable."
        MC "Thanks."
        Caroline "I’m not too bad. What’s up? Grab yourself a beer!"
        scene CR4_ES1_p3
        MC "Nothing much, I just dropped by to say hi."
        Caroline "Well, ‘hi’ then. Hehe!"
        if Li_points >= 2 and CR4_ES1_q4 == False:
            $ CR4_ES1_q4 = True
        if SR2_grounded == True and  CR4_ES1_q2 == False:
            $ CR4_ES1_q2 = True
        jump CR4_ES1_menu

    if CR4_ES1 == 4:
        hide screen map_button
        show screen caroline_room_evening
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen caroline_room_evening
        jump caroline_room_morning1


label CR4_ES1_menu:
    scene CR4_ES1_p3
    menu:
        "How’s business going?" if CR4_ES1_q1 == True:

            scene CR4_ES1_p3
            MC "How’s business going?"
            Caroline "It’s on the up and up! I can barely keep stock on the shelves right now."
            MC "Cheers to that!"

            scene CR4_ES1_p4
            Caroline "Yeah, cheers!"
            Caroline "Thanks again for all your help, [player_name]. I couldn’t have done this without you."
            MC "It’s my pleasure, Caroline."

            scene CR4_ES1_p5
            MC "*Glug*"
            Caroline "*Glug*"

            $ CR4_ES1_q1 = 3
            jump CR4_ES1_menu

        "Have you spoken with Sara lately? " if CR4_ES1_q2 == True:

            scene CR4_ES1_p6
            MC "Have you spoken with Sara lately?"
            Caroline "No, why?"

            scene CR4_ES1_p7
            MC "She got grounded by, [Mom_name]! Didn’t you hear?"
            Caroline "Oh! Of course. Yeah, I remember. It’s her own fault really. She spends far too much time playing video games."

            scene CR4_ES1_p7a
            Caroline "It’s kinda sad. She has so much potential. She just needs a kick up the ass!"
            MC "Haha, I know, I know."

            $ CR4_ES1_q2 = 3
            jump CR4_ES1_menu

        "Did you enjoy our date the other night?" if CR4_ES1_q3 == True:

            scene CR4_ES1_p6
            MC "Did you enjoy our date the other night?"
            Caroline "How could I not? It was amazing."
            MC "Yeah, it was one of the best nights of my entire life!"

            scene CR4_ES1_p8
            Caroline "Really? Even better than your birthday a few years back, when you got that stupid computer?"
            MC "Hey! That was a top-of-the-line gaming machine!"

            scene CR4_ES1_p9
            MC "But no. Our date was much better."
            Caroline "And that, is the correct answer. Hehe!"

            $ CR4_ES1_q3 = 3
            jump CR4_ES1_menu

        "Yazmin is self employed too. Perhaps you two should get in touch?" if CR4_ES1_q4 == True:

            scene CR4_ES1_p14
            MC "Yazmin is self employed too, you know?"
            Caroline "Oh yeah?"
            MC "I think she’s a model or something."

            scene CR4_ES1_p15
            MC "Perhaps you two should get in touch? Share some business tips with each other."
            Caroline "Huh, that’s not a bad idea actually. I might actually take you up on that offer."

            scene CR4_ES1_p16
            Caroline "God… it’s so relaxing just lying back like this."
            Caroline "Yazmin probably feels it too; the sheer exhaustion of working your ass off."
            MC "*Glug*"

            $ CR4_ES1_q4 = 3
            jump CR4_ES1_menu

        "I’m sorry about your necklace. " if CR4_ES1_q5 == True:

            scene CR4_ES1_p11
            Caroline "*Glug*"
            MC "I… uh… I’m sorry again about Charles stealing your necklace."
            Caroline "*COUGH*"

            scene CR4_ES1_p12
            MC "I know it meant an awful lot to you."
            MC "And if there was a way I could snap my fingers and get it back where it belongs, I would."

            scene CR4_ES1_p13
            Caroline "Sorry, *cough* you took me by surprise there."
            Caroline "Listen… I’m slowly working my way through the stages of grief. I just want to blitzkrieg my way to acceptance as quickly as possible."
            MC "I understand that. If there’s anything I can do, please let me know."
            Caroline "… I will."

            $ CR4_ES1_q5 = 3
            jump CR4_ES1_menu

        "Why did you even date that asshole Charles?" if CR4_ES1_q6 == True:

            scene CR4_ES1_p14
            MC "Why did you even date that asshole?"
            Caroline "Charles?"
            MC "Yeah."

            scene CR4_ES1_p13
            if persistent.incest_patch == True:
                Caroline "I uh… I wasn’t in a great place after Grandma passed away."
            else:
                Caroline "I uh… I wasn’t in a great place after my grandma passed away."
            Caroline "Believe it or not, he actually seemed… nice. At that particular time, at least."
            Caroline "Of course, he quickly changed. He became… nasty."

            scene CR4_ES1_p12
            MC "…"
            Caroline "That’s when the shouting and the hitting began…"

            scene CR4_ES1_p11
            MC "Christ… I’m sorry for bringing this up."
            Caroline "*Glug Glug*"

            scene CR4_ES1_p13
            Caroline "When you’re on the outside seeing a relationship like that- it’s easy to say, “just walk away!”"
            Caroline "But then you’re in it and… you just can’t escape those things. It’s like… fucking quicksand."

            scene CR4_ES1_p6
            Caroline "But - hey! I’m here now. A free woman! Hehe!"
            MC "I’m just glad you made it out of that. It sounds like a living hell."

            scene CR4_ES1_p7
            Caroline "For a while, sure. But it really makes you appreciate a good relationship when you open yourself up to one."
            Caroline "Do you know what I mean?"

            scene CR4_ES1_p12
            MC "I think so."

            scene CR4_ES1_p7b
            MC "*Glug*"
            Caroline "*Glug*"

            $ CR4_ES1_q6 = 3
            jump CR4_ES1_menu

        "Where do you see things going between us?" if CR4_ES1_q7 == True:

            scene CR4_ES1_p8
            MC "So, where do you see things going?"
            Caroline "In my business? The global economy? "
            MC "No, haha! Between us! Our relationship. Where do you think it’s headed?"

            scene CR4_ES1_p9
            Caroline "Hehe, I knew what you were talking about. I just couldn’t resist teasing you."
            MC "You’re terrible."
            Caroline "Hehe, I know!"

            scene CR4_ES1_p6
            MC "So..."
            Caroline "Can we just take things one day at a time?"
            Caroline "I’m enjoying this, I really am. Well, a lot more than just “enjoying” it."
            Caroline "I’m happy with you, [player_name]. I think this could be… the start of a really healthy relationship. Let’s just let it grow naturally, and see where we end up?"

            $ CR4_ES1_q7 = 3
            jump CR4_ES1_menu

        "{color=#00ff00}Continue.{/color}" if CR4_ES1_q8 == True:
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

            scene CR4_ES1_p16
            MC "*Glug*"
            Caroline "Hehe… I’m… (Hic) getting a little bit drunk now."

            scene CR4_ES1_p17
            Caroline "I think I might have (Hic) had a bit too much…"
            MC "Haha, me too."

            scene CR4_ES1_p18
            Caroline "Say… how about we have another round right now?"
            MC "You mean, fuck again?"
            Caroline "Hehe, uh huh!"

            scene CR4_ES1_kiss_p1
            Caroline "Fuck it, let’s do it!"
            MC "B-But, Caroline-"
            Caroline "Thinking about what we did down by the lake has got me all horny and wet. I can’t take it any longer!"

            scene CR4_ES1_kiss_p2
            Caroline "I need to feel your cock inside me again!"
            MC "(Shit, she’s drunk and horny! This is NOT a good combo!)"

            scene CR4_ES1_kiss_p3
            MC "Caroline, can we wait until tonight?"
            Caroline "Hehe, why wait?"
            MC "Everyone else is at home right now. Literally anyone, could walk in on us!"
            MC "How would you explain this to Sara or [Mom_name]?"

            scene CR4_ES1_kiss_p4
            MC "Mppff!"

            Caroline "Mmm!"

            scene CR4_ES1_kiss_p5
            MC "Mmm…"
            scene CR4_ES1_kiss_p4anim with dissolve
            MC "(Oh God, she is so fucking hot when she gets aggressive like this!)"

            scene CR4_ES1_kiss_p6
            Caroline "(Fuck, I’m so wet right now…)"
            Caroline "Mmm…"
            scene CR4_ES1_kiss_p6anim with dissolve
            Caroline "(He’s right though. If anyone caught us right now, it would fuck everything up!)"

            scene CR4_ES1_kiss_p7
            Caroline "*Lick*"
            Caroline "(Just a little bit of fun won’t hurt though!)"
            MC "Ahh..."

            scene CR4_ES1_kiss_p10
            Caroline "*Lick* *Lick*"
            MC "(Fuck… it feels so good, having her lick my nipples like that! I never imagined they would be THIS sensitive!)"
            Caroline "Hehe, are you enjoying this?"

            scene CR4_ES1_kiss_p11
            MC "Mmm! Uh huh! Ohhh..."
            Caroline "*Lick*"
            MC "Ahh.."

            scene CR4_ES1_kiss_p12
            Caroline "How about I go even lower now?"
            Caroline "Would you like me to wrap my lips around your hard cock?"
            if persistent.incest_patch == True:
                MC "Mmm… (Damn, she’s so hard to resist. But this is a TERRIBLE idea with all our family home!)"
            else:
                MC "Mmm… (Damn, she’s so hard to resist. But this is a TERRIBLE idea with all of our roommates home!)"
            Caroline "I would suck it so hard… just like this!"

            scene CR4_ES1_kiss_p13
            Caroline "*Suck*"
            MC "Oh fuck! Ahhh…"
            MC "*Gasp*"

            scene CR4_ES1_kiss_p14
            Caroline "*Mwah*"
            MC "Oh God… Ohh…"
            Caroline "Hehe, you’re so hard!"

            scene CR4_ES1_kiss_p15
            MC "W-Wait, stop!"
            Caroline "Huh?"
            MC "Can we wait until everyone falls asleep?"

            scene CR4_ES1_kiss_p16
            Caroline "But I’m gonna leave you unsatisfied…"
            Caroline "Will you come back quickly?"

            scene CR4_ES1_kiss_p17
            menu:
                "Yes, I’ll be back as soon as possible.":
                    MC "Yes, I’ll be back as soon as possible."
                    Caroline "Don’t keep a girl waiting."
                    $ CR4_ES1 = 4
                    $ CR4_NS3 = 1
                    $ CR4_AS2 = False
                    $ CR4_AS3 = 2
                    $ CR4_ES1_q8 = 3
                    jump caroline_room_morning1
                "No, not tonight. We both need our sleep.":

                    MC "Sorry Caroline, I can’t do tonight. We both need our sleep."
                    Caroline "Okay… I understand..."

                    $ CR4_ES1 = 4
                    $ CR4_NS3 = 1
                    $ CR4_AS2 = False
                    $ CR4_AS3 = 2
                    $ CR4_ES1_q8 = 3
                    jump caroline_room_morning1
        "Bye":

            $ CR4_ES1 = 4
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump caroline_room_morning1