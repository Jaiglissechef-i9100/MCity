image ML_NS_wake_p2 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/2.jpg"
image ML_NS_wake_p3 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/3.jpg"
image ML_NS_wake_p4 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/4.jpg"
image ML_NS_wake_p5 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/5.jpg"
image ML_NS_wake_p6 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/6.jpg"
image ML_NS_wake_p7 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/7.jpg"
image ML_NS_wake_p8 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/8.jpg"
image ML_NS_wake_p9 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/9.jpg"
image ML_NS_wake_p10 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/10.jpg"
image ML_NS_wake_p11 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/11.jpg"
image ML_NS_wake_p12 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/12.jpg"
image ML_NS_wake_p13 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/13.jpg"
image ML_NS_wake_p14 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/14.jpg"
image ML_NS_wake_p15 = Movie(play="videos/04 Linda-NS1-1.webm", loop = True )

image ML_NS_wake_p16 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/16.jpg"
image ML_NS_wake_p17 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/17.jpg"
image ML_NS_wake_p17anim = Movie(play="videos/04 Linda-NS1-3.webm", loop = True )
image ML_NS_wake_p18 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/18.jpg"
image ML_NS_wake_p18anim = Movie(play="videos/04 Linda-NS1-4.webm", loop = True )
image ML_NS_wake_p19 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/19.jpg"
image ML_NS_wake_p20 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/20.jpg"
image ML_NS_wake_p20anim = Movie(play="videos/04 Linda-NS1-2.webm", loop = True )
image ML_NS_wake_p21 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/21.jpg"
image ML_NS_wake_p22 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/22.jpg"
image ML_NS_wake_p23 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/23.jpg"
image ML_NS_wake_p24 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/24.jpg"
image ML_NS_wake_p24anim = Movie(play="videos/04 Linda-NS1-5.webm", loop = True )
image ML_NS_wake_p25anim = Movie(play="videos/04 Linda-NS1-6.webm", loop = True )
image ML_NS_wake_p25 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/25.jpg"
image ML_NS_wake_p26 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/26.jpg"
image ML_NS_wake_p27 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/27.jpg"
image ML_NS_wake_p28 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/28.jpg"
image ML_NS_wake_p29 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/HerCHoice/29.jpg"

label ML_NS_wake_label:
    $ Linda_name = Mom_name
    scene ML_NS_wake_p2

    MC "(Whispered) [Linda_name]?"
    Mom "Zzz..."
    MC "(If I touch her lips, she might wake up?)"

    scene ML_NS_wake_p3

    Mom "Hmm? What time is it..?"
    MC "(Whispered) Shush - it’s me."
    Mom "Huh?"

    scene ML_NS_wake_p4

    Mom "(Whispered) [player_name], what are you doing here? It’s the middle of the night?"
    if persistent.incest_patch == True:
        MC "(Whispered) I wanted to spend some time with you. C’mon back to my bedroom with me. We’ll sneak out before Dad wakes up."
    else:
        MC "(Whispered) I wanted to spend some time with you. C’mon back to my bedroom with me. We’ll sneak out before Bob wakes up."
    Mom "(Whispered) And what if he wakes up, and finds me missing?"
    MC "(Whispered) Just tell him you went to the bathroom - when you get back."

    scene ML_NS_wake_p5

    Mom "(Whispered) I don’t think so..."
    Mom "(Whispered) I want to have you - in MY bedroom - tonight."
    if persistent.incest_patch == True:
        MC "(Whispered) Are you crazy?! Dad’s LITERALLY right there?"
    else:
        MC "(Whispered) Are you crazy?! Bob’s LITERALLY right there?"

    scene ML_NS_wake_p6

    Dad "Zzz..."
    Mom "(Whispered) Please... That old coot, could sleep through a car crash! I’ve seen him fall asleep with the TV blaring, on full volume."
    MC "(Whispered) Are you sure?"
    Mom "(Whispered) Yeah - don’t worry about waking him up."

    call screen ML_NS_wake_scr

