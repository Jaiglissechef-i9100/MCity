image MLR3_b_house_leaving_p1 = "images/Beach/MLR3_beach_event/House/Leaving/1.jpg"
image MLR3_b_house_leaving_p2 = "images/Beach/MLR3_beach_event/House/Leaving/2.jpg"
image MLR3_b_house_leaving_p3 = "images/Beach/MLR3_beach_event/House/Leaving/3.jpg"
image MLR3_b_house_leaving_p4 = "images/Beach/MLR3_beach_event/House/Leaving/4.jpg"
image MLR3_b_house_leaving_p5 = "images/Beach/MLR3_beach_event/House/Leaving/5.jpg"
image MLR3_b_house_leaving_p6 = "images/Beach/MLR3_beach_event/House/Leaving/6.jpg"
image MLR3_b_house_leaving_p7 = "images/Beach/MLR3_beach_event/House/Leaving/7.jpg"

label MLR3_b_house_leaving:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
    scene b_house_living_M_map
    scene MLR3_b_house_leaving_p1 with dissolve
    $ can_hide_windows = True

    Mom "Okay, I think that’s all my stuff packed up in the car. Have you got all your clothes?"
    MC "Yeah, everything’s in my bag."
    Mom "You haven’t left any underwear or socks lying around?"
    MC "No, [Mom_name]. I’ve got everything."
    if persistent.incest_patch == True:
        Mom "Good - I just don’t want the landlord finding men’s clothes in here, after I’ve been staying over. I don’t know if he’s the kind of man who would try to get in touch with your father, but it’s not worth the risk."
    else:
        Mom "Good - I just don’t want the landlord finding men’s clothes in here, after I’ve been staying over. I don’t know if he’s the kind of man who would try to get in touch with Bob, but it’s not worth the risk."

    scene MLR3_b_house_leaving_p2

    MC "You look amazing, by the way, [Mom_name]."
    Mom "Aww, you’re very sweet. *Sigh* I’m going to miss these past two days."
    Mom "I loved the scent of you, lying in bed beside me, while my eyes were closed. And the rustle of the sheets, as you moved during the night."
    if persistent.incest_patch == True:
        Mom "I don’t know why - but when I’m sleeping with your father, it always feels like I’m sleeping alone. Last night, was the first time in years, that it’s felt like another man is sleeping beside me."
    else:
        Mom "I don’t know why - but when I’m sleeping with Bob, it always feels like I’m sleeping alone. Last night, was the first time in years, that it’s felt like another man is sleeping beside me."
    Mom "Anyway, I’m rambling and being silly. We should hit the road."

    scene MLR3_b_house_leaving_p3

    Mom "Got your seatbelt on?"
    MC "Yes, [Mom_name]."
    Mom "And both suitcases in the car?"
    MC "All bags are in the car, [Mom_name]. You’re worrying too much!"
    Mom "*Sigh* I know, I know."
    Mom "I guess… I guess I just want to make excuses, to stay here a while longer. I know we can’t though."
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(2,hard=True)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR3_b_house_leaving_p4

    Mom "And… that’s us home."
    MC "Why are we in the alley?"
    Mom "You’re gonna need to walk, a bit. It’ll look suspicious if I drive home with you."

    scene MLR3_b_house_leaving_p5

    MC "Ahh, that makes sense. Good point."
    Mom "Just wait one or two minutes, after I drive off. You should make it home about fifteen minutes after me. That’ll eliminate any suspicion."
    MC "No problem, [Mom_name]."

    scene MLR3_b_house_leaving_p6

    Mom "…"
    MC "Are you okay?"
    Mom "I just want you to know that… yesterday was the best day of my whole life."

    scene MLR3_b_house_leaving_p7

    Mom "I haven’t felt so much excitement and joy in life, since I was a little girl. It was like Christmas all over again."
    Mom "Except, this wasn’t all Santa and magic because… everything we had was so real."
    MC "I love you, [Mom_name]. I really do."
    Mom "I know. Right, I better drive on. I’ll see you when we both get home."
    $ clickable = True
    $ day_time = 2
    $ MLR3_beach_event = False
    $ can_hide_windows = False
    $ beach_unlocked = True
    $ MLR2_MS1_active = True
    $ MLR3_AS3 = 2
    $ MLR3_NS1 = 2
    $ can_MLR2_MS1_ES3 = False
    $ MLR2_R3_MS1_q1 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump map_label

