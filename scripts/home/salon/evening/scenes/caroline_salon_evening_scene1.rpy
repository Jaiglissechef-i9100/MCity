image caroline_salon_evening_scene1_p1 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/1.jpg"
image caroline_salon_evening_scene1_p2 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/2.jpg"
image caroline_salon_evening_scene1_p3 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/3.jpg"
image caroline_salon_evening_scene1_p4 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/4.jpg"

label caroline_salon_evening_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_salon_can_evening_scene1 == False:
        show screen salon_evening_notclickable
        MC "I've already talked to her."
        jump salon_morning1
    if caroline_salon_can_evening_scene1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_salon_evening_scene1_p1 with dissolve
        $ can_hide_windows = True
        MC "Hey, Caroline!"
        Caroline "Hiiii!"
        MC "Are you not getting dressed?"
        Caroline "What do you mean? I’m wearing a top."
        MC "(Huh, I guess she considers a pair of panties “casual clothes”.)"
        MC "Nevermind - How’re you doing?"
        Caroline "I’ve got a few things on my mind - but they’re not worth complaining about."
        Caroline "How about you? What’re you doing home at this hour? A guy your age should be out partying."
        window hide
        menu:
            "I came home to see the best sister in the world." if renpy.loadable("patch.rpy"):
                scene caroline_salon_evening_scene1_p2
                MC "I just came home to see the best sister in the world."
                Caroline "Oh really? How sweet."
                MC "Yeah, I still haven’t found Sara yet though. Haha!"

                scene caroline_salon_evening_scene1_p1
                Caroline "Ahh, you bastard! Haha!"
                MC "Sorry, Caroline. Couldn’t resist."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "I came home to see my best friend in the world." if not renpy.loadable("patch.rpy"):
                scene caroline_salon_evening_scene1_p2
                MC "I just came home to see my best friend in the world."
                Caroline "Oh really? How sweet."
                MC "Yeah, I still haven’t found Sara yet though. Haha!"

                scene caroline_salon_evening_scene1_p1
                Caroline "Ahh, you bastard! Haha!"
                MC "Sorry, Caroline. Couldn’t resist."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "Nah, no one’s inviting me out to any parties after that fiasco with Mrs. Celia.":
                scene caroline_salon_evening_scene1_p3
                MC "Yeah… I’m not really getting invited out to any parties recently."
                MC "Probably has to do with that Mrs. Celia fiasco."
                Caroline "Oh God... I’m sorry to hear that."

                scene caroline_salon_evening_scene1_p4
                Caroline "I wish I could give you some advice that would fix this."
                Caroline "But… honestly, don’t even know where to begin."
                MC "It’s okay, Caroline. Thanks anyway."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "I just came home to chill.":
                scene caroline_salon_evening_scene1_p2
                MC "I just came home to chill and relax for a while."
                Caroline "Coooool. Have fun with that."
                MC "Thanks, Caroline. You up to much?"

                scene caroline_salon_evening_scene1_p3
                Caroline "Just researching marketing ideas."
                Caroline "Y’know [player_name], I have to tell you..."

                scene caroline_salon_evening_scene1_p4
                Caroline "I never thought running a business would be this hard!"
                Caroline "I wish there was some easy way to crowdfund a business. Perhaps with a monthly subscription for users, y’know? Like a website!"
                Caroline "Heck - such a system could even be used to fund, small indie games developers and artists!"

                scene caroline_salon_evening_scene1_p2
                Caroline "Am I being crazy, [player_name], or does this sound like a good idea?"

                scene caroline_salon_evening_scene1_p4
                Caroline "Actually, don’t answer that! It would just be another bad financial investment from me!"
                MC "Don’t be too harsh on yourself, Caroline!"
                MC "It sounds like a good idea - but you’d probably have to start making difficult decisions, like arbitrarily banning certain content creators if you don’t like their stuff."
                Caroline "True - it would probably get flooded with perverts, making dirty sex games."
                MC "You’re better off just sticking with your clothes shop."

                scene caroline_salon_evening_scene1_p1
                Caroline "Yeah, you’re right, [player_name]. Thanks!"
                MC "Cool. See you later, Caroline!"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1