image MLR3_Linda_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/1.jpg"
image MLR3_Linda_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/2.jpg"
image MLR3_Linda_MS1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/3.jpg"
image MLR3_Linda_MS1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/4.jpg"
image MLR3_Linda_MS1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/5.jpg"
image MLR3_Linda_MS1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/6.jpg"
image MLR3_Linda_MS1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/7.jpg"
image MLR3_Linda_MS1_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/8.jpg"
image MLR3_Linda_MS1_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/9.jpg"
image MLR3_Linda_MS1_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/10.jpg"
image MLR3_Linda_MS1_p11 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/11.jpg"
image MLR3_Linda_MS1_p12 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/12.jpg"
image MLR3_Linda_MS1_p13 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/13.jpg"
image MLR3_Linda_MS1_p14 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS1/ML/14.jpg"

label MLR3_Linda_MS1:
    hide screen displayTextScreen
    hide screen map_button
    if MLR3_Linda_MS1_can == False:
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
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        if MLR3_Linda_MS1_day == 1:
            scene MLR3_Linda_MS1_p1 with dissolve

            MC "(I love it when she wears low-cut tops like that.)"
            MC "(I always get a great view when I’m standing over her like this.)"

            scene MLR3_Linda_MS1_p2

            Mom "Need something?"
            MC "I - uh… Just wanted to say… hi!"
            Mom "(Haha! I knew exactly what he was up to there. Does he not think I can tell when he’s looking down my top?)"
            Mom "Sit down beside me. I’m taking a break to enjoy my coffee."
            scene MLR3_Linda_MS1_p4

            jump MLR3_Linda_MS1_menu

label MLR3_Linda_MS1_menu:
    scene MLR3_Linda_MS1_p4
    menu:

        "{color=#00ff00}What’s going on between you and [Dad_name]? Are you fighting?{/color}" if MLR3_Linda_MS1_q2 == True:
            scene MLR3_Linda_MS1_p4

            MC "What’s going on between you and [Dad_name]? Are you fighting?"

            scene MLR3_Linda_MS1_p10

            Mom "*Sigh* It’s a little rough right now."
            Mom "I wouldn’t say we’re fighting… but things haven’t been too hot lately."
            Mom "That said, there’s nothing new there."

            scene MLR3_Linda_MS1_p11

            Mom "The fires of our love burnt out years ago. It’s just embers now."
            MC "Are you not worried he’ll hear you?"
            Mom "Not over the sound of that vacuum cleaner."

            "*VROOOOM*"
            $ MLR3_Linda_MS1_q2 = False
            $ MLR3_Linda_MS1_day = 2
            $ MLR3_Linda_MS1_can = False

            jump MLR3_Linda_MS1_menu

        "{color=#00ff00}It’s good to see [Dad_name] helping more around the house.{/color}" if MLR3_Linda_MS1_can == False:
            MC "It’s good to see [Dad_name] helping more around the house. It gives you a chance to relax and do other things around the house, for a change."

            scene MLR3_Linda_MS1_p5

            Mom "Mmm, that’s true."
            Mom "*Shlurp*"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

            scene MLR3_Linda_MS1_p9

            Mom "Hey, [player_name], before you go. Do you know what I’d really like to do around the house?"
            MC "Hmm?"

            scene MLR3_Linda_MS1_p12

            Mom "You."
            MC "(Whispered) [Mom_name]! He’s right over there!"
            Mom "So what? He won’t hear us."

            scene MLR3_Linda_MS1_p13

            Mom "I would love to do you, all over this house."
            Mom "In the shower… in the bedroom…"
            Mom "Maybe even on the kitchen table."
            Mom "God, if I had a weekend with you, with no one else around, I would fuck you silly."
            MC "(Wow! She’s getting VERY brazen lately!)"

            scene MLR3_Linda_MS1_p11

            Dad "*Phew* Okay, that’s the hoovering almost finished."
            Mom "That’s good to hear, Bob. I think you missed a few spots though."

            scene MLR3_Linda_MS1_p14
            Mom "..."
            $ MLR3_Linda_MS1_day = 3
            $ MLR3_Linda_MS1_can = False
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1

        "How did you and [Dad_name] first meet?" if MLR3_Linda_MS1_q1 == True:
            scene MLR3_Linda_MS1_p4
            MC "How did you and [Dad_name] first meet?"
            Mom "Oh wow… I haven’t thought about that in a LONG time…"
            Mom "God… it must have been… Venice, I think?"

            scene MLR3_Linda_MS1_p8

            Mom "I think we were on a business trip to Venice together. I don’t remember when we first spoke to each other though."
            MC "Huh, it sounds quite nice! Did you go on the gondolas together?"
            Mom "Wait - there were no gondolas. Maybe it wasn’t Venice?"

            scene MLR3_Linda_MS1_p5

            MC "(She doesn’t seem to remember this very well. Or maybe she just doesn’t care enough to?)"
            Mom "..."

            $ MLR3_Linda_MS1_q1 = False

            jump MLR3_Linda_MS1_menu
