image d_ml_and_f_bedroom_mornig_scene_v1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/1.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/2.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/3.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/4.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/5.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/6.jpg"

screen d_ml_and_f_bedroom_mornig_scene_v1_screen:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("d_ml_and_f_bedroom_mornig_scene_v1_screen"), Hide("parents_bedroom_day_notclickable"), Jump("parents_bedroom_morning1")]
label d_ml_and_f_bedroom_mornig_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if d_ml_and_f_bedroom_mornig_scene_visit == 4 and d__can_ml_and_f_bedroom_mornig_scene == True:
        show screen parents_bedroom_day_notclickable
        show screen d_ml_and_f_bedroom_mornig_scene_v1_screen
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Bob"
        Dad "Not now, [player_name]."
        jump parents_bedroom_morning1
    if d__can_ml_and_f_bedroom_mornig_scene == False:
        show screen parents_bedroom_day_notclickable
        show screen d_ml_and_f_bedroom_mornig_scene_v1_screen
        Dad "Not now, [player_name]."
        jump parents_bedroom_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Aces High.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    if d_ml_and_f_bedroom_mornig_scene_visit == 1 and d__can_ml_and_f_bedroom_mornig_scene == True:
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Bob"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Uhh… Hey Dad, you busy right now?"
        if not renpy.loadable("patch.rpy"):
            MC "Uhh… Hey Bob, you busy right now?"
        Dad "Hmm?"

        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "Oh! Hello, champ! What’s kickin’?"
        MC "Huh?"
        Dad "What’s kickin’? That’s what you young kids say nowadays, ain’t it?"
        MC "Um… Sure."

        scene d_ml_and_f_bedroom_mornig_scene_v1_p5
        Dad "What did you want, then?"

        menu:
            "{color=#00ff00}Can you give me some money?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                if renpy.loadable("patch.rpy"):
                    MC "I’m actually a bit short on cash, Dad. Could you maybe lend me some?"
                if not renpy.loadable("patch.rpy"):
                    MC "I’m actually a bit short on cash, Bob. Could you maybe lend me some?"
                Dad "Haha! You’ve spent all your money chasing girls, haven’t you?"
                Dad "Let me take a look in my wallet…"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p4
                Dad "Alright, here you go. Don’t spend it all in one place, now!"
                if renpy.loadable("patch.rpy"):
                    MC "Thanks, Dad!"
                if not renpy.loadable("patch.rpy"):
                    MC "Thanks, Bob!"
                "+15$"
                $ inventory.earn(15)
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 2
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "How are things at work?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                MC "How are things at work?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p6
                Dad "Aww, jeez. Where to begin?!"
                Dad "Emily, from human resources, has just been sacked for selling private medical data."
                Dad "So now, I have to carry out a whole risk assessment on the company’s entire Eastern Branch!"
                MC "Ugh, sounds rough!"
                MC "(I have no idea what he even works as…)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "Have you got anything fun planned?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                MC "Have you got anything fun planned for today, then?"
                if renpy.loadable("patch.rpy"):
                    Dad "Nothing much today. I’ll probably help your mom vacuum, later on."
                if not renpy.loadable("patch.rpy"):
                    Dad "Nothing much today. I’ll probably help Linda vacuum, later on."
                Dad "Tomorrow though, I’m gonna go to a lecture on fly fishing at the local library."
                MC "Err… Wow! Sounds… exciting."
                Dad "I know, right? In fact, did you know that there are seven different species of salmon, in the Pacific alone!"
                MC "Fascinating. (God, I better get out of here or change the subject, before he starts another one of his fishing rants.)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1

    if d_ml_and_f_bedroom_mornig_scene_visit == 2 and d__can_ml_and_f_bedroom_mornig_scene == True:
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Hey, Dad!"
        if not renpy.loadable("patch.rpy"):
            MC "Hey, Bob!"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "Hey there, champ. What’s up?"
        menu:
            "What do you actually work as?":

                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                MC "I just realised that I don’t actually know what you work as."
                Dad "Really? I’m a company risk assessor."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                Dad "It’s my job to travel to our various sites and take steps to minimise risk."
                Dad "I’m also in charge of managing our insurance policies for the Eastern Business Centres."
                MC "(Damn… I’m sorry I asked.)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "{color=#00ff00}Can I borrow some more money?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                if renpy.loadable("patch.rpy"):
                    MC "Could I borrow some more money, Dad?"
                if not renpy.loadable("patch.rpy"):
                    MC "Could I borrow some more money, Bob?"
                Dad "What happened to the money I just lent you?"
                MC "Err… I had to spend it on… essential school stuff."
                Dad "Damn, schools are getting expensive nowadays!"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p4
                Dad "I haven’t had a chance to go to an ATM - so this is all I have on me right now."
                if renpy.loadable("patch.rpy"):
                    MC "Thanks, Dad."
                if not renpy.loadable("patch.rpy"):
                    MC "Thanks, Bob."
                Dad "No problem, champ."
                "+15$"
                $ inventory.earn(15)
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 3
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "How was that fly fishing lecture?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                MC "So, how was the fly fishing lecture?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                Dad "You should have been there! It was INCREDIBLE!"
                MC "(Oh God… I’ve set him off again.)"
                "(Fifteen Minutes Later…)"
                scene black
                $ renpy.pause()
                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                Dad "And THAT was just the guest speaker!"
                MC "(Now’s my chance to finally change the conversation topic!)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1

    if d_ml_and_f_bedroom_mornig_scene_visit == 3 and d__can_ml_and_f_bedroom_mornig_scene == True:
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Hi, Dad!"
        if not renpy.loadable("patch.rpy"):
            MC "Hi, Bob!"
        Dad "Hey, champ!"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "What can I do for you?"
        menu:
            "{color=#00ff00}Could I borrow some more money?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                MC "Could I borrow some more money?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                Dad "Huh? Again?"
                Dad "You should try finding a way to earn an honest living. It’s not good to just beg and beg."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p6
                if renpy.loadable("patch.rpy"):
                    Dad "I think your mother is always looking extra help, here and there. I’m sure she’d be happy to pay you for your time."
                if not renpy.loadable("patch.rpy"):
                    Dad "I think Linda is always looking extra help, here and there. I’m sure she’d be happy to pay you for your time."
                MC "Aww, okay. Thanks anyway."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                Dad "Don’t look so down, champ! A little hard work never killed anybody!"
                MC "(I’m not quite sure that’s completely true…)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 4
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1