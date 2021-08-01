image ML_NS_sleep_hand_p1 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/1.jpg"
image ML_NS_sleep_hand_p2 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/2.jpg"
image ML_NS_sleep_hand_p3 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/3.jpg"
image ML_NS_sleep_hand_p4 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/4.jpg"
image ML_NS_sleep_hand_p4anim = Movie(play="videos/05 Linda NV-5.webm", loop = True )
image ML_NS_sleep_hand_p5 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/5.jpg"
image ML_NS_sleep_hand_p6 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/6.jpg"
image ML_NS_sleep_hand_p7 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/7.jpg"
image ML_NS_sleep_hand_p8 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/8.jpg"
image ML_NS_sleep_hand_p8anim = Movie(play="videos/05 Linda NV-6.webm", loop = True )
image ML_NS_sleep_hand_p9 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/9.jpg"
image ML_NS_sleep_hand_p10 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/10.jpg"
image ML_NS_sleep_hand_p10a = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/10a.jpg"
image ML_NS_sleep_hand_p11 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/11.jpg"
image ML_NS_sleep_hand_p12 = "images/home/ml_and_f_bedroom/night/ML_NSB_sleep/Handjob/12.jpg"

label ML_NS_sleep_hand_label:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

    Mom "I’m going to take the lead tonight. Go ahead and lie back on the bed."
    MC "What about [Dad_name]?"

    scene ML_NS_sleep_hand_p1 with dissolve
    if persistent.incest_patch == True:
        Mom "Relax. Your father isn’t going to wake up. As long as you don’t wriggle about too much, or make a lot of noise, you’ll be fine."
    else:
        Mom "Relax. Bob isn’t going to wake up. As long as you don’t wriggle about too much, or make a lot of noise, you’ll be fine."
    MC "If you’re sure…"
    Mom "I’m certain. I’ve spent YEARS lying beside that fat oaf. I know exactly what it takes to rouse him."

    scene ML_NS_sleep_hand_p2

    Mom "Now, onto the important part. I’m going to give you the best handjob you’ll ever have."
    MC "That’s quite a bold claim to make!"
    Mom "Why? Have other girls been giving you handjobs to compare it to?"
    MC "Err… N-No!"

    scene ML_NS_sleep_hand_p3

    MC "Sorry, I’m just really nervous, lying so close to [Dad_name], here."
    if persistent.incest_patch == True:
        Mom "I already told you, your father’s not going to wake up. Heaven help us all if a burglar broke into our house. They’d be able to nick everything except the bed he was sleeping on."
    else:
        Mom "I already told you, Bob’s not going to wake up. Heaven help us all if a burglar broke into our house. They’d be able to nick everything except the bed Bob was sleeping on."

    scene ML_NS_sleep_hand_p4

    Mom "You’re nice and hard for me already - that’s good. I love it when I don’t have to help a guy get it up."
    scene ML_NS_sleep_hand_p4anim with dissolve
    MC "Heh, I’m almost always hard when I’m around you, [Mom_name]. Especially when you’re dressed like this."
    MC "You look so damn sexy in that skimpy bra."

    scene ML_NS_sleep_hand_p5

    Mom "It’s nice to be appreciated. How does this feel?"
    MC "Mmm… It’s so good, [Mom_name]. don’t stop."
    Mom "Oh, I’m not planning on stopping, anytime soon."

    scene ML_NS_sleep_hand_p6

    MC "(She’s so skilled with her hand. I thought she might not have been as good with her left, but she’s doing great!)"

    scene ML_NS_sleep_hand_p7
    MC "Ah... Keep doing that, [Mom_name]."
    Mom "You love so much my hand? What if I stop?"
    MC "No... Continue..."
    Mom "You have to ask for it nicely..."
    MC "Please... Do not stop, [Mom_name]."

    scene ML_NS_sleep_hand_p8
    scene ML_NS_sleep_hand_p8anim with dissolve
    Mom "Sure, Sweetie. I’ll get back to focusing on rubbing your cock now."
    Dad "Zzz...."

    scene ML_NS_sleep_hand_p9

    MC "Mmm… That’s good…"
    MC "I’m gonna cum pretty soon if you keep focusing on the tip like that."
    Mom "You mean, if I keep doing this?"

    scene ML_NS_sleep_hand_p10

    MC "Hnnng… Yes, that!"
    Mom "It must be REALLY sensitive when I rub it like this, here. I bet you it feels sooo good right now."
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene ML_NS_sleep_hand_p10 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene ML_NS_sleep_hand_p10a with dissolve

    MC "Oh fuck… Hnnng… ugh! I’m cumming!"

    scene ML_NS_sleep_hand_p11

    if persistent.incest_patch == True:
        Mom "Wow! You really must have enjoyed that. Sorry again, for scaring you with the sorority joke. I picked up my handjob skills from months of not wanting to fuck your father."
    else:
        Mom "Wow! You really must have enjoyed that. Sorry again, for scaring you with the sorority joke. I picked up my handjob skills from months of not wanting to fuck Bob."

    MC "Ahh… that makes sense."
    Mom "I love you so much, [player_name]. Thanks for taking the time to come and visit me."

    scene ML_NS_sleep_hand_p12

    MC "Mmm…"
    Mom "Mwah…"

    scene ML_NS_sleep_hand_p11

    Mom "You better sneak back into your room now. We’ve gotten away with a lot tonight and there’s no sense, tempting fate any more than we have."
    MC "Good call. I’ll see you tomorrow, [Mom_name]."

    jump ML_NS_sleep_back

