image MLR3_Bob_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/1.jpg"
image MLR3_Bob_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/2.jpg"
image MLR3_Bob_MS1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/3.jpg"
image MLR3_Bob_MS1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/4.jpg"
image MLR3_Bob_MS1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/5.jpg"
image MLR3_Bob_MS1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/6.jpg"
image MLR3_Bob_MS1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/Bob/7.jpg"

label MLR3_Bob_MS1:
    if persistent.incest_patch == True:
        $ Dad_name = __("Dad")
    else:
        $ Dad_name = "Bob"
    hide screen displayTextScreen
    hide screen map_button
    if MLR3_Bob_MS1_can == False:
        show screen parents_bedroom_morning
        $ clickable = False
        MC "I've already talked with him."
        $ clickable = True
        hide screen parents_bedroom_morning
        jump parents_bedroom_morning1
    if MLR3_Bob_MS1_q1 == False and MLR3_Bob_MS1_q2 == False and MLR3_Bob_MS1_q3 == False and MLR3_Bob_MS1_q4 == False:
        show screen parents_bedroom_morning
        $ clickable = False
        MC "I've already talked with him."
        $ clickable = True
        hide screen parents_bedroom_morning
        jump parents_bedroom_morning1
    else:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        if MLR3_Bob_MS1_day ==1:
            scene MLR3_Bob_MS1_p1 with dissolve

            "*VROOOM*"
            MC "Hey, [Dad_name]?"
            "*VROOOOOMMM*"
            MC "Hey! [Dad_name]!"

            scene MLR3_Bob_MS1_p2

            Bob "Hey, sorry champ. Couldn’t hear you with the old vacuum on, there."
            Bob "What’s up?"
            MC "Are you free to talk right now?"

            scene MLR3_Bob_MS1_p3

            Bob "Yeah, shoot."
            Bob "What do you want to discuss?"
            jump MLR3_Bob_MS1_menu
        if MLR3_Bob_MS1_day == 2:
            scene MLR3_Bob_MS1_p2 with dissolve

            Bob "Hello again, champ. Looking to chat with your old man?"
            MC "Yeah, you busy?"

            if persistent.incest_patch == True:
                Bob "I can always spare some time for my favourite son."
            else:
                Bob "I can always spare some time for you, [player_name]."
            scene MLR3_Bob_MS1_p3

            Bob "So, what’s up?"
            jump MLR3_Bob_MS1_menu

label MLR3_Bob_MS1_menu:
    if persistent.incest_patch == True:
        $ Dad_name = __("Dad")
    else:
        $ Dad_name = "Bob"
    scene MLR3_Bob_MS1_p3
    menu:
        "{color=#00ff00}(Whisper) Is everything okay between you and [Mom_name]?{/color}" if MLR3_Bob_MS1_q2 == True:
            scene MLR3_Bob_MS1_p6

            MC "(Whispered) Is everything okay between you and [Mom_name]?"
            Bob "Umm… Y-Yeah, all good. All good."
            MC "(Whispered) I thought I heard you two arguing the other day."


            scene MLR3_Bob_MS1_p5

            Bob "(Whispered) We um… might have had a teensy disagreement."
            Linda "*Slurp*"
            Bob "(Whispered) I better get back to vacuuming here. I’m getting the evil eyes from her right now."
            MC "Oops, sorry."

            $ MLR3_Bob_MS1_q2 = False
            $ MLR3_Bob_MS1_day = 2
            $ MLR3_Bob_MS1_can = False
            $ MLR3_Bob_MS1_day_can = True
            $ MLR3_Bob_MS1_q3 = True
            $ MLR3_Bob_MS1_q4 = True
            jump MLR3_Bob_MS1_menu

        "Could you give me some advice on finding a job?" if MLR3_Bob_MS1_q1 == True:
            scene MLR3_Bob_MS1_p4

            MC "I was wondering if you could give me some advice for finding a job. I’m about to graduate fairly soon."
            Bob "Hmm… That’s a tough one. The labour market has changed massively from my day."
            Bob "It used to be you got a solid union job for life, or you started your own business. I opted for the latter. It’s not like that anymore."

            scene MLR3_Bob_MS1_p6

            Bob "The biggest growth is in STEM right now. Science, Technology, Engineering, and Maths."
            Bob "Train yourself in those and you’ll go far. That’s where you earn the big bucks!"
            MC "Great! Thanks, [Dad_name]."

            $ MLR3_Bob_MS1_q1 = False
            jump MLR3_Bob_MS1_menu

        "Any tips on dealing with stress, [Dad_name]?" if MLR3_Bob_MS1_q3 == True:
            scene MLR3_Bob_MS1_p7

            MC "Any tips on dealing with stress, [Dad_name]?"
            Bob "Stress? At your age?"
            MC "Yeah… exams and stuff can be stressful."

            scene MLR3_Bob_MS1_p4

            Bob "Hmm… I guess you’re right. "
            Bob "Honestly, the best way, is to get yourself involved in a hobby. That’ll be a long term solution. Make it a weekly thing, if you can."
            Bob "Something that you really enjoy and can work into your routine."
            MC "Yeah, that sounds good!"

            scene MLR3_Bob_MS1_p4

            Bob "In the short term, you just need to learn how to take a breather."
            Bob "Go for a walk on your lunch. Stuff like that."
            $ MLR3_Bob_MS1_q3 = False
            $ MLR3_Bob_MS1_can = False
            jump MLR3_Bob_MS1_menu

        "Why have you been vacuuming so often, lately?" if MLR3_Bob_MS1_q4 == True:
            scene MLR3_Bob_MS1_p4

            MC "Why have you been vacuuming so often, lately?"
            Bob "Ah… haha! Yes, that’s a very good question."

            scene MLR3_Bob_MS1_p5
            if persistent.incest_patch == True:
                Bob "I was told to- I… volunteered to help out more around the house. Your mother was getting tired of having to do the cooking and the cleaning AND hold down a full time job."
            else:
                Bob "I was told to- I… volunteered to help out more around the house. My wife was getting tired of having to do the cooking and the cleaning AND hold down a full time job."
            Bob "Right, Honey?"
            Linda "…"

            scene MLR3_Bob_MS1_p3

            Bob "So, yeah… That’s why I’m being so helpful around the house lately…"
            Bob "I had to cancel a fishing trip - but this is… just as fun. It’s great fun spending the day with you, Linda."
            MC "(Jesus, I’ve never heard a man sound more depressed in my life before.)"
            $ MLR3_Bob_MS1_q4 = False
            $ MLR3_Bob_MS1_can = False
            $ MLR3_Bob_MS1_day = 3
            jump MLR3_Bob_MS1_menu

        "Bye." if MLR3_Bob_MS1_can == False:
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1

