image CeR2_MS3_p1 = "images/CeR2/MS3/1.jpg"
image CeR2_MS3_p2 = "images/CeR2/MS3/2.jpg"
image CeR2_MS3_p3 = "images/CeR2/MS3/3.jpg"
image CeR2_MS3_p4 = "images/CeR2/MS3/4.jpg"
image CeR2_MS3_p5 = "images/CeR2/MS3/5.jpg"
image CeR2_MS3_p6 = "images/CeR2/MS3/6.jpg"
image CeR2_MS3_p7 = "images/CeR2/MS3/7.jpg"
image CeR2_MS3_p8 = "images/CeR2/MS3/8.jpg"
image CeR2_MS3_p9 = "images/CeR2/MS3/9.jpg"
image CeR2_MS3_p10 = "images/CeR2/MS3/10.jpg"
image CeR2_MS3_p11 = "images/CeR2/MS3/11.jpg"
image CeR2_MS3_p12 = "images/CeR2/MS3/12.jpg"
image CeR2_MS3_p13 = "images/CeR2/MS3/13.jpg"

image CeR2_MS3_lick_p1 = "images/CeR2/MS3/Lick/1.jpg"
image CeR2_MS3_lick_p2 = "images/CeR2/MS3/Lick/2.jpg"
image CeR2_MS3_lick_p3 = "images/CeR2/MS3/Lick/3.jpg"
image CeR2_MS3_lick_p4 = "images/CeR2/MS3/Lick/4.jpg"
image CeR2_MS3_lick_p5 = "images/CeR2/MS3/Lick/5.jpg"
image CeR2_MS3_lick_p6 = "images/CeR2/MS3/Lick/6.jpg"
image CeR2_MS3_lick_p7 = "images/CeR2/MS3/Lick/7.jpg"

image CeR2_MS3_refuse_p1 = "images/CeR2/MS3/Refuse/1.jpg"
image CeR2_MS3_refuse_p2 = "images/CeR2/MS3/Refuse/2.jpg"
image CeR2_MS3_refuse_p3 = "images/CeR2/MS3/Refuse/3.jpg"
image CeR2_MS3_refuse_p4 = "images/CeR2/MS3/Refuse/4.jpg"
image CeR2_MS3_refuse_p5 = "images/CeR2/MS3/Refuse/5.jpg"
image CeR2_MS3_refuse_p6 = "images/CeR2/MS3/Refuse/6.jpg"
image CeR2_MS3_refuse_p7 = "images/CeR2/MS3/Refuse/7.jpg"
image CeR2_MS3_refuse_p8 = "images/CeR2/MS3/Refuse/8.jpg"
image CeR2_MS3_refuse_p9 = "images/CeR2/MS3/Refuse/9.jpg"
image CeR2_MS3_refuse_p10 = "images/CeR2/MS3/Refuse/10.jpg"
image CeR2_MS3_refuse_p11 = "images/CeR2/MS3/Refuse/11.jpg"

label CeR2_MS3_lab:
    if CeR2_MS3 == 2:
        $ clickable = False
        hide screen map_button
        show screen teacher_room1_morning
        Celia "What do you want? I'll be waiting for you in the toilets in afternoon."
        hide screen teacher_room1_morning
        $ clickable = True
        jump teacher_room1_morning1
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CeR2_MS3_p1
        MC "I got your text message. What do you want from me?"
        Celia "That’s hardly a good way to talk to your teacher."
        Celia "Especially when you were late to my class."
        scene CeR2_MS3_p2
        MC "Listen, I’m sorry about being late. I’ve got a lot of shit going on right-"
        Celia "Hush, I’m not here to listen to your lame excuses."
        scene CeR2_MS3_p3
        Celia "Get down on your knees."
        MC "What?! I’m not gonna do that!"
        Celia "Kneel, boy! Or I’ll tell Sara everything that has happened."
        scene CeR2_MS3_p4
        MC "Grr…"
        MC "What the hell are you expecting me to do right now? Lick your cunt again?"
        scene CeR2_MS3_p5
        Celia "I wish I could. Unfortunately though, there are far too many people who could walk in and interrupt us."
        MC "Lucky for me."
        Celia "Oh, come on now, [player_name]. There’s no need for the sarcasm."
        scene CeR2_MS3_p6
        Celia "All you’re going to do today is lick my hand. It’s really that simple."
        MC "Yeah, fuck that. It ain’t happening."
        scene CeR2_MS3_p7
        Celia "*Sigh*"
        MC "Ahh!"
        scene CeR2_MS3_p8
        "*WHACK*"
        MC "Ow!"
        scene CeR2_MS3_p9
        Celia "That is just an appetizer of what’s to come if you refuse to obey me."
        Celia "Have I made myself crystal clear?"
        scene CeR2_MS3_p10
        MC "..."
        Celia "I said, have I made myself crystal clear?"
        MC "Yes, Ma’am."
        scene CeR2_MS3_p11
        Celia "There is only one person to blame for the situation you find yourself in right now."
        Celia "That is you, and you alone."
        MC "..."
        scene CeR2_MS3_p12
        Celia "Now, let’s stop wasting time. We both have places to be."
        Celia "Get over here and lick my hand."
        scene CeR2_MS3_p13
        MC "(Fuck, I don’t know what to do. I really don’t want to give in to this bitch.)"
        MC "(But she’s already slapped me. I don’t want her to do anything worse…)"
        Celia "I’m waiting, [player_name]."
        $ CeR2_MS3 = 2
        $ CeR2_AS3 = True
        menu:
            "Lick Celia's hand.":
                scene CeR2_MS3_lick_p1
                MC "*Lick*"
                Celia "Come on boy, I know you can do better than that!"
                scene CeR2_MS3_lick_p2
                Celia "Seriously? Is this the best you’ve got?"
                Celia "I know how well you can lick a pussy. Put some effort into it!"
                scene CeR2_MS3_lick_p3
                MC "*Lick Lick*"
                Celia "Mmmmm, yes! That is soooo much better!"
                scene CeR2_MS3_lick_p4
                Celia "Hehe, such an obedient little pet. Aren’t you?"
                MC "(Grr… This is fucking humiliating!)"
                Celia "Okay, you can leave now."
                scene CeR2_MS3_lick_p5
                Celia "Oh, be a darling and meet me in the cubicles in afternoon."
                Celia "The same place you tried to blackmail me will be fine."
                MC "(What the hell does she have planned?!)"
                scene CeR2_MS3_lick_p6
                Celia "Mmm…"
                Celia "(He doesn't taste half bad.)"
                scene CeR2_MS3_lick_p7
                Celia "(I’m looking forward to playing with him later on today.)"
                Celia "(If he only knew what I had in store for him.)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

                $ can_hide_windows = False
                jump school_corridor2_morning1
            "Refuse.":


                scene CeR2_MS3_refuse_p1
                MC "If you think I’m going to do anything for you after you slapped me, then you must be out of your fucking mind."
                Celia "..."
                scene CeR2_MS3_refuse_p2
                Celia "I shall give you one final chance, boy."
                Celia "Lick my hand, or you’ll face the consequences!"
                MC "No!"
                scene CeR2_MS3_refuse_p3
                Celia "Very well, it seems my disobedient pet needs to be disciplined."
                MC "Fuck. You."
                scene CeR2_MS3_refuse_p4
                Celia "Such a grumpy and immature boy."
                Celia "Oh well, you’ll come around."
                scene CeR2_MS3_refuse_p5
                MC "*Gasp*"
                MC "(Here we go again.)"
                scene CeR2_MS3_refuse_p6
                "*SLAP*"
                MC "Aahh!"
                scene CeR2_MS3_refuse_p7
                Celia "Today could have been so simple, [player_name]. All you had to do was bend the knee and lick my hand."
                Celia "But no, you HAD to make things difficult for yourself. Didn’t you?"
                scene CeR2_MS3_refuse_p8
                MC "Wait-"
                "*WHACK*"
                MC "Ooof!"
                scene CeR2_MS3_refuse_p9
                MC "Ugh… Oww…"
                Celia "Stand up. Pull yourself together and get the fuck out of my office."
                scene CeR2_MS3_refuse_p10
                MC "Ah… Ugh…"
                Celia "I said, get the fuck out of here. Do you want me to kick you again?!"
                scene CeR2_MS3_refuse_p11
                Celia "Oh, and I expect to see you in the cubicles in afternoon. The same one you attempted to blackmail me in."
                Celia "I’ve got more punishment to dish out to you."

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

                $ can_hide_windows = False
                jump school_corridor2_morning1

