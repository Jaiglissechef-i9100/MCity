image MLR3_MS2_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/1.jpg"
image MLR3_MS2_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/2.jpg"
image MLR3_MS2_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/3.jpg"
image MLR3_MS2_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/4.jpg"
image MLR3_MS2_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/5.jpg"
image MLR3_MS2_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/6.jpg"
image MLR3_MS2_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/7.jpg"
image MLR3_MS2_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/8.jpg"
image MLR3_MS2_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/9.jpg"
image MLR3_MS2_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS2/10.jpg"

label MLR3_MS2:
    hide screen displayTextScreen
    hide screen map_button
    if MLR3_MS2_can == False:
        show screen parents_bedroom_morning
        $ clickable = False
        MC "I've already talked with her."
        $ clickable = True
        hide screen parents_bedroom_morning
        jump parents_bedroom_morning1
    else:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
        scene MLR3_MS2_p1 with dissolve

        MC "(I wonder what [Mom_name]’s doing home at this time. She doesn’t normally just hang around in her room like this.)"
        MC "Hey [Mom_name], are you making tea?"
        Mom "…"

        scene MLR3_MS2_p2

        MC "Umm, [Mom_name]?"
        Mom "Huh? Oh! Sorry, I didn’t hear you come in there, [player_name]."
        MC "I just asked if you were making tea."

        scene MLR3_MS2_p3

        Mom "Oh, yeah. Would you like a cup put on? I can refill the kettle."
        MC "Nah, don’t worry about it. Are you okay? You look a little anxious."
        Mom "I’m, uh…"

        scene MLR3_MS2_p4

        Mom "Of course, I’m fine. Never been better."
        MC "Cool, what are you doing home at the minute?"
        Mom "Just working on a few projects I can’t bring into the office. I’ll have them cleared up soon enough."
        MC "Is it something I can help with?"

        scene MLR3_MS2_p5

        Mom "Not this time, Sweetie. I’ll keep you in mind if something comes up that you can help me with though."
        MC "No problem. I love your dress, by the way! Is it a new one?"
        Mom "This thing? I’ve had it for a couple of years. I used to wear it to company functions, but the other men would sometimes get a bit too feely when the drinks started to flow."
        MC "Well, it certainly shows off your best assets!"

        scene MLR3_MS2_p6

        Mom "…"
        Mom "(Yes... Now when I look at him I know this will be a perfect idea!)"
        MC "…"
        scene MLR3_MS2_p7

        Mom "Hmm? Sorry, what did you say?"

        scene MLR3_MS2_p4

        MC "I said, that dress shows off your best assets. Are you okay?"
        Mom "Sorry, just lost in thought."
        MC "You seem rather distracted today. Is everything okay? Something on your mind?"

        scene MLR3_MS2_p7

        Mom "I.. uh… y-yeah, everything is fine. Why? Did something happen?"
        MC "Hmm, as long as you’re okay."

        scene MLR3_MS2_p8

        Mom "Really, I’m fine. I just have a lot on my plate right now. I’ll be more focused when things calm down."
        MC "No sweat."
        Mom "Err… random question, are you planning to go away anytime soon?"
        MC "Away? What do you mean?"

        scene MLR3_MS2_p9

        Mom "You know… like a holiday or weekend break?"
        MC "Umm… I don’t think so. Why?"
        Mom "No reason!"

        scene MLR3_MS2_p10

        MC "(She’s acting so bizarre right now!)"
        MC "Okay, is it a problem if I had something booked?"
        Mom "Can you hold off on making plans? I might need your help for something soon."
        MC "Huh, no problem."
        Mom "Just put it out of your head. I’ll talk about it with you later on."

        $ MLR3_MS3 = 2
        $ MLR3_MS2_can = False

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump parents_bedroom_morning1
