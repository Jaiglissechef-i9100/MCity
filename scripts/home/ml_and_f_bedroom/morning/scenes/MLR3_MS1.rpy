image MLR3_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/1.jpg"
image MLR3_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/2.jpg"
image MLR3_MS1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/3.jpg"
image MLR3_MS1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/4.jpg"
image MLR3_MS1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/5.jpg"
image MLR3_MS1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/6.jpg"
image MLR3_MS1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/7.jpg"
image MLR3_MS1_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/8.jpg"
image MLR3_MS1_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/9.jpg"
image MLR3_MS1_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/10.jpg"
image MLR3_MS1_p11 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/11.jpg"
image MLR3_MS1_p12 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/12.jpg"

label MLR3_MS1:
    if renpy.loadable("patch.rpy"):
        $ Linda_name = "Linda"
        $ Liza2_name = __("Auntie")
        $ Mom_name = __("Mom")
    else:
        $ Mom_name = "Linda"
        $ Linda_name = "Linda"
        $ Liza2_name = "Liza"

    hide screen displayTextScreen
    hide screen map_button
    if MLR3_MS1_can == False:
        show screen salon_morning
        $ clickable = False
        MC "I should probably leave them alone."
        $ clickable = True
        hide screen salon_morning
        jump salon_morning1
    else:

        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene MLR3_MS1_p1 with dissolve

        Bob "Aww, c’mon, Linda, I need you to open up to me. Can’t we just talk about this?"
        Linda "There’s NOTHING to talk about!"
        if renpy.loadable("patch.rpy"):
            MC "(Huh? It sounds like Mom and Dad are having an argument. I wonder what’s going on…)"
        else:
            MC "(Huh? It sounds like Linda and Bob are having an argument. I wonder what’s going on…)"

        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)

        scene MLR3_MS1_p2

        Bob "Relationships are built on communication, Linda. I know you’re angry or maybe frustrated, right now, but if you don’t tell me why, I can’t fix whatever the problem is."
        Linda "*Shlurp*"
        Bob "*Sigh*"
        Bob "Linda, you’re killing me right now. Please, throw me a bone here!"

        scene MLR3_MS1_p3

        Bob "I’ve done everything I can - I’ve helped out around the house. I’ve been working my ass off in overtime to help pay our bills. I mean, what more do you want from me?"
        Linda "..."
        Bob "Please don’t give me the silent treatment, Dear. You’re better than that. This isn’t going to help us address these problems."

        scene MLR3_MS1_p4

        Linda "You’re blowing this WAY out of proportion, Bob. Seriously, you need to calm the fuck down."
        Bob "But, I-"
        Linda "There are NO problems in this relationship."

        scene MLR3_MS1_p5
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

        Bob "Forgive my french, Linda - but you and I both know that is complete bullcrap."
        Bob "Things haven’t been normal between you and me, for a while now. But it seems in the past few weeks, things have taken a REAL nosedive between us."
        Bob "I’m willing to go to therapy with you, if that’s what you need. You’ve got that friend who’s a therapist, right? What’s her name again? Judy?"

        scene MLR3_MS1_p6

        Linda "Ugh! I am NOT bringing my friends into our marital issues."
        Bob "Aha! So you admit it, we ARE having issues!"
        Linda "I said ‘issues’, Bob, not ‘problems’."
        Bob "They’re the same damn thing!"
        Bob "*Sigh* Sorry for raising my voice at you there. Listen, we need to talk about-"
        Linda "There’s nothing to talk about, Bob."

        scene MLR3_MS1_p7

        Bob "YOU’RE TEARING ME APART, LINDA!"
        Bob "Do you know how I feel right now?! Do you have any idea?!"
        Bob "I spend every single day, dealing with problems and issues at work. I can FIX problems and resolve issues. What I can’t deal with, is this silent treatment!"
        Bob "It leaves me feeling physically sick… this horrible sensation of not knowing what is wrong. It’s like you’re slipping between my fingers and I can’t hold onto you - and I don’t know why!"

        scene MLR3_MS1_p8

        Linda "For God’s sake, pull yourself together, Bob! You’re a forty eight year old man. Act like one!"
        Linda "And don’t you DARE raise your voice to me again. "

        scene MLR3_MS1_p9

        Bob "*Sigh* I’m sorry, I’m just..."
        Bob "I’ve just been stressed with work lately. There’s a lot of pressure to post record profits before the next shareholders meeting."
        Bob "I shouldn’t be taking that stress out on you, but I can’t spend all day busting my ass at work and then come home to a wife who… who..."
        Linda "Yes, Bob..?"
        Bob "...who may not even love me."

        scene MLR3_MS1_p10

        Bob "I know it sounds pathetic. But, when was the last time we had sex?"
        Linda "We did it last we-"
        Bob "No, we didn’t. I fucked YOU last week. You just lay there and took it, while you read your book."
        Linda "That was sex."
        Bob "It wasn’t. You know as well as I do, that we haven’t had real proper sex in a long time."

        scene MLR3_MS1_p11

        Bob "Remember the first time we got to third base? I picked you up in my old red cadillac. Your father was glaring at me from the porch. I was terrified he was gonna shoot me that night."
        Bob "We drove along those winding roads, up Wilridge Mountain. The government didn’t have barriers on the roadside back in those days. You could lean out the window and see a four hundred foot drop off the mountain edge."
        Bob "It was dangerous and stupid - but we were teenagers, and the view was to die for. Do you remember that night, Linda?"
        Linda "…"

        scene MLR3_MS1_p12

        Bob "You wore that purple miniskirt with no panties underneath. We sixty-nined in the back seats, under the starlight."
        Bob "We were loud back then, Linda. We were loud, and we were frisky, and we were… honest with each other."
        Bob "*Sniff* We fooled around so much, we steamed the damn windows up. That was real sex."
        Linda "That was decades ago. Nothing lasts forever, Bob."
        Bob "*Sob* You threw a fucking pillow at me when I came into the room. You looked at me like I DISGUSTED you."
        if renpy.loadable("patch.rpy"):
            Bob "*Sniff* This isn’t just about me, Linda. For Christ’s sake… think of our kids."
            Bob "Think of Sara - she probably sees more than you know, and her parents fighting is going to break her little heart."
        else:
            Bob "Sniff This isn’t just about me, Linda. For Christ’s sake… think about others."
            Bob "Think of Sara - she probably sees more than you know, and if we keep fighting is going to break her little heart."
        MC "(Fuck… This is too tough to listen to. I gotta go.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ MLR3_MS1_can = False
        $ Bob_in_work = False
        $ MLR3_ES1 = True
        jump salon_morning1
