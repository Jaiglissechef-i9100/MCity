image CNS_wake_kissing_p1 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/1.jpg"
image CNS_wake_kissing_p2 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/2.jpg"
image CNS_wake_kissing_p3 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/3.jpg"
image CNS_wake_kissing_p4 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/4.jpg"
image CNS_wake_kissing_p5 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/5.jpg"
image CNS_wake_kissing_p6 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/6.jpg"
image CNS_wake_kissing_p6anim = Movie(play="videos/04 Caroline-NV-K1.webm", loop = True )
image CNS_wake_kissing_p7 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/7.jpg"
image CNS_wake_kissing_p8 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/8.jpg"
image CNS_wake_kissing_p9 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/9.jpg"
image CNS_wake_kissing_p10 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/10.jpg"
image CNS_wake_kissing_p11 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/11.jpg"
image CNS_wake_kissing_p12 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/12.jpg"
image CNS_wake_kissing_p13 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/13.jpg"
image CNS_wake_kissing_p13anim = Movie(play="videos/04 Caroline-NV-K2.webm", loop = True )
image CNS_wake_kissing_p14 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/14.jpg"
image CNS_wake_kissing_p15 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/15.jpg"
image CNS_wake_kissing_p16 = "images/home/caroline_room/night/scenes/CR2_NS/Kissing/16.jpg"

label CNS_wake_kissing_label:
    $ Linda_name = Mom_name
    scene CNS_wake_kissing_p1

    MC "Do you fancy making out tonight?"
    Caroline "Here on the bed?"
    MC "Of course! Where else did you think we could go? Haha!"

    scene CNS_wake_kissing_p2

    Caroline "Hehe, sure. Let’s do it. I only have one request."
    MC "What is it?"
    Caroline "Let me lead this time."

    scene CNS_wake_kissing_p3

    MC "Be my guest, Caroline."
    Caroline "Mmm… just like that. Perfect."

    scene CNS_wake_kissing_p4

    Caroline "Mmm…"
    MC "(Wow! She’s a better kisser than I imagined she would be!)"
    MC "(I love the way she’s running her fingers through my hair while she makes out with me.)"

    scene CNS_wake_kissing_p5

    Caroline "(A couple of months ago the very thought of this happening with him would have been a nightmare.)"
    Caroline "(Now it’s a wet dream come true…)"
    if persistent.incest_patch == True:
        Caroline "(I know he’s my brother and that it’s wrong, but there’s just something different when I kiss him. It’s not like any of the other guys I’ve been with before.)"
    else:
        Caroline "(I know he’s my close friend and that it’s wrong, but there’s just something different when I kiss him. It’s not like any of the other guys I’ve been with before.)"

    scene CNS_wake_kissing_p6

    Caroline "Mmm!"
    scene CNS_wake_kissing_p6anim with dissolve
    Caroline "(Sure my first ever kiss was exciting. It gave me a few butterflies in my stomach as we snuck behind the school bike shed.)"
    Caroline "(And the first time I ever kissed a guy while having sex was amazing too. It was this nervous thrill.)"

    scene CNS_wake_kissing_p7

    MC "Mmm!"
    Caroline "(But those butterflies never came back after the first kiss, and the sex was emotionless.)"
    Caroline "(There’s something different about the time I spend with, [player_name].)"

    scene CNS_wake_kissing_p8

    Caroline "Wow… That was… something else!"
    MC "Heh, I’m glad you enjoyed it as much as I did!"
    Caroline "We’re not finished yet!"

    scene CNS_wake_kissing_p9

    Caroline "Down you go!"
    MC "Wow! Oof!"
    Caroline "Hehe, gotcha!"

    scene CNS_wake_kissing_p10

    MC "You have to keep your voice down, [Linda_name] might hear us!"
    Caroline "Screw them all! I’m here to enjoy myself!"
    MC "That’s really not a wise-"

    scene CNS_wake_kissing_p11

    Caroline "Shut up and let me kiss you."
    MC "(Wow, it’s not like Caroline to throw caution to the wind. She must be insanely horny right now!)"

    scene CNS_wake_kissing_p12

    Caroline "(Every other guy I have ever dated pales in comparison to the one guy I can’t date.)"
    Caroline "(With them, the butterflies in my stomach never came back after the first kiss.)"
    Caroline "(But with, [player_name], they never left.)"

    scene CNS_wake_kissing_p13

    Caroline "Mmm!"
    scene CNS_wake_kissing_p13anim with dissolve
    MC "Mmm!"
    Caroline "(Every single kiss is as thrilling and exciting as our first! Each one sets my heart racing. My whole body feels weightless when he wraps his arms around me.)"

    scene CNS_wake_kissing_p14

    Caroline "(It’s perfect - except for the fact he’s one guy in my age range that I’m not allowed to date.)"
    Caroline "(If anyone ever found out how I truly felt about him I would be shunned and despised.)"
    if persistent.incest_patch == True:
        Caroline "(Why does the best relationship I’ve ever had have to be a clandestine affair with my own brother?)"
    else:
        Caroline "(Why does the best relationship I’ve ever had have to be a clandestine affair with my friend?)"
    scene CNS_wake_kissing_p15

    Caroline "(Why couldn’t my heart just choose a nice single guy my age?)"
    Caroline "(With each passing day I find myself growing more and more attracted to him. Wanting to do more intense things together.)"
    Caroline "(If this continues could things extend beyond a simple deal?)"

    scene CNS_wake_kissing_p16

    Caroline "*Sigh*"
    MC "What’s wrong, Caroline?"
    Caroline "Nothing at all, [player_name]. I just need to stop overthinking things and live in the moment with you."

    scene black
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.pause(2, hard = True)
    $ renpy.sound.play("sfx/door_open.mp3")
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ caroline_room_can_night_scene1 = False
    $ can_hide_windows = False
    jump corridor_morning1

