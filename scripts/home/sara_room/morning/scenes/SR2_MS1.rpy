image SR2_MS1_p1 = "images/home/sara_room/morning/SR2_MS1/1.jpg"
image SR2_MS1_p2 = "images/home/sara_room/morning/SR2_MS1/2.jpg"
image SR2_MS1_p3 = "images/home/sara_room/morning/SR2_MS1/3.jpg"
image SR2_MS1_p4 = "images/home/sara_room/morning/SR2_MS1/4.jpg"
image SR2_MS1_p5 = "images/home/sara_room/morning/SR2_MS1/5.jpg"
image SR2_MS1_p6 = "images/home/sara_room/morning/SR2_MS1/6.jpg"
image SR2_MS1_p7 = "images/home/sara_room/morning/SR2_MS1/7.jpg"
image SR2_MS1_p8 = "images/home/sara_room/morning/SR2_MS1/8.jpg"

label SR2_MS1_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen sister_nerdy_morning_notclickable

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    MC "Sara, it’s almost time to go to school. Are you ready?"
    Sara "…"
    MC "Sara?"
    hide screen sister_nerdy_morning_notclickable
    scene SR2_MS1_p1 with dissolve
    $ can_hide_windows = True

    MC "Sara?"
    Sara "Zzz…"
    MC "(Has she just fallen asleep at her desk?)"

    scene SR2_MS1_p2

    MC "Hey Sara… You’ve got five minutes until we have to leave for school."
    Sara "Mmm…"
    MC "Sara, you have to wake up!"

    scene SR2_MS1_p3

    Sara "Hmm?"
    MC "(Jesus, she looks exhausted! Is she sick or something?)"
    MC "Are you okay, Sara? You don’t look well."
    Sara "N-No… I’m fine. I’m good. Don’t worry."

    scene SR2_MS1_p4

    MC "Are you sure? You look completely exhausted!"
    Sara "I… don’t think I went to bed last night. Last thing I remember was grinding online with my clan… I must have dozed off during a raid."
    MC "Ahh, that explains it, then. "
    Sara "Ugh, do I have to go to school today?"
    if renpy.loadable("patch.rpy"):
        MC "If you miss class, Mom’s gonna freak out."
    else:
        MC "If you miss class, Linda’s gonna freak out."

    scene SR2_MS1_p5

    Sara "(Sigh) You’re right."
    MC "Go and take a shower. I’ll see you in school."
    Sara "Okay… (YAWN!) See you there, [player_name]."

    scene SR2_MS1_p6

    MC "Sara, watch out for the doo-"
    $ renpy.sound.play("sfx/door_hit.wav")
    "*THUD*"
    Sara "Oww!"
    MC "(Well, I guess that’s one way to wake someone up!)"

    scene SR2_MS1_p7

    MC "Are you alright?"
    Sara "Y-Yeah, my nose isn’t bleeding. I’m okay."
    MC "You’ve still got your headphones on too - make sure you don’t go into the shower with them on!"

    scene SR2_MS1_p8

    Mom "ARE YOU TWO ALMOST READY? YOU’RE GOING TO BE LATE FOR SCHOOL!"
    if renpy.loadable("patch.rpy"):
        Sara "(Yawn!) Y-Yeah, Mom! I’m almost ready…"
    else:
        Sara "(Yawn!) Y-Yeah, Linda! I’m almost ready…"
    Sara "Okay, I’m gonna take a quick shower. I might be a few minutes late to class. You head on, first."
    MC "Catch you later, Sara!"
    MC "(I hope these all-nighters she’s pulling, don’t impact her grades too much…)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_MS1 = False
    $ SR2_MS2 = True
    $ can_SR2_MS2 = False
    $ SR2_bath = True
    jump sister_nerdy_morning1