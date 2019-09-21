image MLR3_AS2_p1 = "/images/ml_work/room1/scenes/MLR3_AS2/1.jpg"
image MLR3_AS2_p2 = "/images/ml_work/room1/scenes/MLR3_AS2/2.jpg"
image MLR3_AS2_p3 = "/images/ml_work/room1/scenes/MLR3_AS2/3.jpg"
image MLR3_AS2_p4 = "/images/ml_work/room1/scenes/MLR3_AS2/4.jpg"
image MLR3_AS2_p5 = "/images/ml_work/room1/scenes/MLR3_AS2/5.jpg"
image MLR3_AS2_p6 = "/images/ml_work/room1/scenes/MLR3_AS2/6.jpg"
image MLR3_AS2_p7 = "/images/ml_work/room1/scenes/MLR3_AS2/7.jpg"
image MLR3_AS2_p8 = "/images/ml_work/room1/scenes/MLR3_AS2/8.jpg"
image MLR3_AS2_p9 = "/images/ml_work/room1/scenes/MLR3_AS2/9.jpg"
image MLR3_AS2_p10 = "/images/ml_work/room1/scenes/MLR3_AS2/10.jpg"
image MLR3_AS2_p11 = "/images/ml_work/room1/scenes/MLR3_AS2/11.jpg"
image MLR3_AS2_p12 = "/images/ml_work/room1/scenes/MLR3_AS2/12.jpg"
image MLR3_AS2_p13 = "/images/ml_work/room1/scenes/MLR3_AS2/13.jpg"

label MLR3_AS2:
    if MLR3_AS2_event == 3:
        hide screen map_button
        show screen ml_work_room1_day
        $ clickable = False
        Mom "Not now, [player_name]."
        hide screen ml_work_room1_day
        $ clickable = True
        jump ml_work_room1_day1

    if MLR3_AS2_event == 1:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene MLR3_AS2_p1 with dissolve
        $ can_hide_windows = True

        Mom "Hi, Sweetie. I’m glad you could make it today."
        MC "Afternoon, [Mom_name]. I’ll just get started on the cleaning here."
        Mom "Try and be quick with it today: we need to have a talk."
        MC "Huh? Is something wrong?"
        Mom "No, nothing’s wrong. We can talk about it later on. Right now, I need you to finish tidying the office."
        MC "(Weird, I wonder what that’s about.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump ML_workR3

    if MLR3_AS2_event == 2:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        $ renpy.pause(2, hard=True)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene MLR3_AS2_p1 with dissolve

        Mom "Is that you all finished?"
        MC "Yeah, that’s the office tidy again."

        scene MLR3_AS2_p2 with dissolve

        MC "(I swear to God though, I think [Mom_name]’s staff are wrecking the place on purpose! Every time I come back to clean it, the whole place is filthy!)"
        Mom "Excellent! C’mon over here and grab a seat with me on the couch."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
        scene MLR3_AS2_p3

        Mom "Okay, I’m gonna be proposing an idea - and I want you to hear me out."
        MC "Alright… Shoot."
        if renpy.loadable("patch.rpy"):
            Mom "You know the way that your father is always around the house and we can never get any time alone together?"
        else:
            Mom "You know the way that Bob is always around the house and we can never get any time alone together?"
        MC "Wait - you aren’t gonna kick him out, are you?!"

        scene MLR3_AS2_p4
        if renpy.loadable("patch.rpy"):
            Mom "Relax! I’m not going to kick your father out! Let me finish, and you’ll understand where I’m coming from."
            MC "(Thank God… if I was responsible for having Dad kicked out of the house, I’d feel so damn guilty right now.)"
            Mom "Your father and me both work long hours. We’re not home till the evenings, and the only private time you and I get together, is when he goes on one of his increasingly rare business trips."
        else:
            Mom "Relax! I’m not going to kick him out! Let me finish, and you’ll understand where I’m coming from."
            MC "(Thank God… if I was responsible for having Bob kicked out of the house, I’d feel so damn guilty right now.)"
            Mom "Bob and me both work long hours. We’re not home till the evenings, and the only private time you and I get together, is when he goes on one of his increasingly rare business trips."
        scene MLR3_AS2_p5

        Mom "I want more than rushed quickies, always panicking that he’ll come home from work early."
        Mom "I want to actually be able to snuggle up next to you after sex, to fall asleep with you in my arms, to have a proper romantic relationship."
        if renpy.loadable("patch.rpy"):
            Mom "I can’t do ANY of those things with your father around… but I can’t kick him out either."
        else:
            Mom "I can’t do ANY of those things with Bob around… but I can’t kick him out either."

        scene MLR3_AS2_p6
        if renpy.loadable("patch.rpy"):
            Mom "I might not… feel the same way I have always felt about him, but you three still need a father."
            Mom "Caroline’s strong. She’ll get by fine if he leaves and you might even be okay. But Sara… I don’t know how she’d react if he left. She loves her dad."
            Mom "So, no. I’m not kicking your father out. He’s staying with us, at least until all three of you are ready to move out to your own places."
        else:
            Mom "I might not… feel the same way I have always felt about him, but you three still need him."
            Mom "Caroline’s strong. She’ll get by fine if he leaves and you might even be okay. But Sara… I don’t know how she’d react if he left. She loves him"
            Mom "So, no. I’m not kicking Bob out. He’s staying with us, at least until all three of you are ready to move out to your own places."

        if renpy.loadable("patch.rpy"):
            MC "That’s… actually kinda relieving to hear, [Mom_name]. I know you probably don’t love him much anymore - but he’s still a good dad."
        else:
            MC "That’s… actually kinda relieving to hear, [Mom_name]. I know you probably don’t love him much anymore - but he’s still a good guy."

        scene MLR3_AS2_p7
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        Mom "ANYWAY! That wasn’t what I wanted to talk to you about. Sorry for killing the mood there."
        Mom "I’ve got a plan to get us a whole day and night to ourselves - just you and me. Nobody else."
        MC "Really?! How?"

        scene MLR3_AS2_p8
        if renpy.loadable("patch.rpy"):
            Mom "I’m gonna tell your dad that I’ve got a work trip coming up. I’ll have to be away for a full day."
            Mom "He won’t mind - I’m sure that your dad will love having the house to himself, for a change. He can sit back and smoke his goddamn cigars, without me nagging him!"
        else:
            Mom "I’m gonna tell Bob that I’ve got a work trip coming up. I’ll have to be away for a full day."
            Mom "He won’t mind - I’m sure Bob will love having the house to himself, for a change. He can sit back and smoke his goddamn cigars, without me nagging him!"
        Mom "You’re gonna secretly come with me, and we’ll sneak away together on a romantic getaway!"

        scene MLR3_AS2_p9

        MC "Okay, but what about my school?"
        if renpy.loadable("patch.rpy"):
            Mom "I’ll tell your dad that you have a school trip coming up. Something like a team building and leadership course."
            Mom "That will erase any suspicion that your dad has, about us disappearing on the same day. (Although, to be honest, I think that dolt is too dense for suspicion.)"
        else:
            Mom "I’ll tell Bob that you have a school trip coming up. Something like a team building and leadership course."
            Mom "That will erase any suspicion Bob has, about us disappearing on the same day. (Although, to be honest, I think that dolt is too dense for suspicion.)"

        scene MLR3_AS2_p10

        MC "It’s a good idea - but I’m not gonna be able to just skip school..."
        MC "Especially after my last incident with the teacher..."
        Mom "I know, I know. That’s the ONLY kink in my plan right now. As soon as I figure that part out, we’ll be good to go."
        Mom "I haven’t told you where I wanted to take us yet, have I?"

        scene MLR3_AS2_p11

        MC "Does it matter? If I can’t get an exemption from school, then I’ll not be able to go anyway."
        Mom "..."
        MC "..."
        Mom "It was the beach, Sweetie. I wanted to take us far away to the coast and enjoy relaxing on the sunny sands together."
        Mom "As for your school, I think I have an idea. See if you can get an exemption for a day."
        Mom "Maybe try to speak with your therapist?"
        MC "My therapist? Do you know her?"
        Mom "W-what? No.. I think it's just the best choice."
        scene MLR3_AS2_p12

        MC "Hmm... An exemption?"
        Mom "I don’t care what nonsense you have to tell her. Call it a family emergency, or a medical appointment."
        Mom "Just say whatever you need to in order to get that day off. I’ll back you up."
        if renpy.loadable("patch.rpy"):
            Mom "See if you can get it in writing too - and then give it to your dad. It’ll help keep him off our trail."
        else:
            Mom "See if you can get it in writing too - and then give it to Bob. It’ll help keep him off our trail."

        scene MLR3_AS2_p13

        MC "No problem, [Mom_name]. I’ll get that done as soon as possible."
        Mom "Thank you, Sweetie. I really do love you. You know that?"
        MC "I know, [Mom_name]. I love you too."
        $ MLR3_AS2_event = 3

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ day_time = 3
        $ judy_q3 = True
        jump map_label
