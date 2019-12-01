label SR2_ES1_rep:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    scene SR2_ES1_p1 with dissolve

    Sara "Heeeeeey, [player_name]! Guess who finally got their webcam working!"
    MC "Hi, Sara! Does Mom know you’re using your webcam?"
    Sara "Absolutely not. She doesn’t even know I’m on my laptop. Hehe!"
    MC "Haha! You naughty girl!"

    scene SR2_ES1_p2

    Sara "How are things over there, in the land of the free?"
    MC "Eh, not much. I’m just doing a bit of work and then the same old shit at school each day."
    if persistent.incest_patch == True:
        Sara "At least you can go wherever you want. Mom’s got me completely grounded right now."
    else:
        Sara "At least you can go wherever you want. Linda’s got me completely grounded right now."

    scene SR2_ES1_p3

    MC "Hopefully, our late night chats will help relieve SOME of the boredom you’re facing right now."
    Sara "Mmm, I hope so too!"
    if persistent.incest_patch == True:
        MC "What's everything you have to do before Mom ungrounds you?"
    else:
        MC "What's everything you have to do before Linda ungrounds you?"

    scene SR2_ES1_p4

    Sara "Aaarrrghhh…."
    Sara "Do we HAVE to talk about this?"
    MC "I just want to know how long it is until I can properly hang out with you again!"

    scene SR2_ES1_p5

    Sara "Ugh, she wants me to re-read EVERY book that I’ve studied so far in school this year."
    Sara "And then I have to retake all the tests I didn’t score a B or higher on."
    Sara "And FINALLY, I have to score an A on my next two tests."

    scene SR2_ES1_p6

    Sara "I mean, just look at this crap! Why do I have to study some dead guy’s poetry?"
    Sara "He doesn’t even write in normal English! "
    Sara "‟I dare do all that may become a man; Who dares do more is none.” What the HECK does that even mean?!"
    MC "Ugh, I remember having to study Shakespeare too. I think it was Romeo and Juliet."
    Sara "That’s so unfair! You got a super romantic story - I got stuck with Macbeth. It’s just so… boring!"

    scene SR2_ES1_p7
    if persistent.incest_patch == True:
        Sara "Anyway! I’ll be able to enjoy some late night chats with my favourite brother from now on!"
    else:
        Sara "Anyway! I’ll be able to enjoy some late night chats with my favourite friend from now on!"
    Sara "So, at least I have something to look forward to at the end of each day!"
    if persistent.incest_patch == True:
        MC "Aren’t I your only brother?"
    else:
        MC "Aren’t I your only friend?"
    Sara "You are - but even if you weren’t, you’d still be my favourite."
    MC "(Aww, she really looks up to me!)"
    scene SR2_ES1_p8

    MC "So, what are you wearing tonight?"
    Sara "Ooohh, just my pyjamas. I was going to go to bed, after our call."
    MC "Can I see?"

    scene SR2_ES1_p9

    MC "No bottoms?"
    Sara "It’s too warm for those, right now!"
    MC "Step back and let me get a better look at you."

    scene SR2_ES1_p10

    Sara "How’s this?"
    MC "Perfect! Your legs are so sexy! You know that?"
    Sara "Hehe! Thanks, [player_name]!"

    scene SR2_ES1_p11

    Sara "Hey! Do you want to see something amazing?"
    MC "Sure!"
    Sara "You have to promise not to tell anyone, okay?"
    MC "Okay, I promise. (I wonder what she’s talking about…)"

    scene SR2_ES1_p12

    Sara "Boo!"
    MC "Mmm! Very nice!"
    Sara "These panties are a little too tight on me - they show off FAR too much of my ass."
    Sara "I can’t wear them to school on sports days because the other girls would see, when we’re getting changed."
    MC "They’re really hot!"

    scene SR2_ES1_p13

    Sara "Haha! I'm glad glad you like them, [player_name]!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    $ menu_q1 = True
    $ menu_q2 = True
    jump SR2_ES1_menu_rep

label SR2_ES1_menu_rep:
    scene SR2_ES1_p13
    menu:
        "Can you show me your bra?" if menu_q1 == True:

            scene SR2_ES1_Bra_p1

            MC "You’ve turned me on now. Could you maybe go a little further and show me your bra?"
            Sara "My bra?"
            MC "Yeah, just pull your top down a bit and let me see it."
            Sara "We’ve got a problem, [player_name]… I can’t do that..."

            scene SR2_ES1_Bra_p2

            Sara "I’m not actually wearing a bra."
            MC "(Holy shit! Her tits are awesome!)"
            Sara "Sorry, most girls don’t wear a bra to bed."

            scene SR2_ES1_Bra_p3

            Sara "I’ll even pull down the other side of my shirt to prove it."
            MC "Yeah, you should do that!"
            if persistent.incest_patch == True:
                MC "(There’s nothing better than having your sister flash her tits on camera for you!)"

            scene SR2_ES1_Bra_p4

            Sara "See, [player_name]? No bra."
            MC "Your boobs are gorgeous, Sara. I’d love to suck on them now."
            MC "Do you think you could lift the camera up a bit so I can get a better view?"

            scene SR2_ES1_Bra_p5

            Sara "Sure, [player_name]. I’ll do that now."
            Sara "I’m really glad you like them. I was a bit worried that they were too small."
            MC "No, they’re absolutely perfect."

            scene SR2_ES1_Bra_p6

            Sara "How’s this?"
            MC "That’s brilliant. God, they’re so perky!"
            MC "You’d look so hot in a tiny bikini. Maybe I can get you to wear one to the pool sometime?"
            Sara "Hehe... We’ll see. I’m not gonna make any promises though!"
            $ menu_q1 = False
            if menu_q1 == False and menu_q2 == False:
                jump SR2_ES1_continue_rep
            else:
                jump SR2_ES1_menu_rep

        "Can you show me your panties?" if menu_q2 == True:

            scene SR2_ES1_Pant_p1
            MC "Damn, you’re so fucking sexy, Sara."
            Sara "Hehe... Thanks."
            MC "Seriously, I’m rocking the biggest boner right now. Do you think you could maybe show me a little more skin?"
            Sara "A little more skin? What are you thinking of?"
            MC "How about you flash me your panties?"

            scene SR2_ES1_Pant_p2

            Sara "Sure. Two seconds - I just need to adjust my webcam."
            MC "Take your time."
            MC "(This is gonna be great!)"

            scene SR2_ES1_Pant_p3

            Sara "Can you see me okay from this angle?"
            MC "Yeah, that’s perfect, Sara. Go ahead and lift your dress up."
            Sara "(I don’t know why I’m doing this so willingly for him. If it was ANY other guy at my school, I’d be trembling with anxiety right now!)"

            scene SR2_ES1_Pant_p4

            Sara "There you go, [player_name]. W-What do you think?"
            MC "Mmm! Hold your top there for a couple of minutes."
            MC "(I can just about make out her cameltoe through the thin pink fabric!)"
            Sara "D-Do you want to see the back too? "
            Sara "(Great… I’m starting to get nervous now.)"
            MC "Yes please!"

            scene SR2_ES1_Pant_p5

            Sara "There you go."
            MC "I can’t really see much. Can you lift your shirt up higher?"
            Sara "Oops, sorry! My bad!"

            scene SR2_ES1_Pant_p6

            Sara "How’s that?"
            MC "Much better! I can see everything now."
            Sara "Hehe…"
            MC "(She’s got such a cute little ass!)"

            scene SR2_ES1_Pant_p7

            Sara "Well? Did you enjoy that?"
            MC "Mmm, very much so!"
            Sara "In that case, let me give you one final parting gift."

            scene SR2_ES1_Pant_p8

            MC "Whoa, you’re gonna make me dizzy if you keep moving the webcam around like that!"
            Sara "Almost there!"

            scene SR2_ES1_Pant_p9

            Sara "You probably can’t tell - but I’m starting to get really… wet under these panties."
            Sara "Something about showing off my body to you on webcam, is really realy hot."
            MC "I’m looking forward to seeing you on webcam without those panties on."
            Sara "Hehe! I'm sure you are!"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False:
                jump SR2_ES1_continue_rep
            else:
                jump SR2_ES1_menu_rep

label SR2_ES1_continue_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_ES1_Vib_p1

    MC "(She still looks rather downhearted after being grounded in her room.)"
    MC "(Let's see if I can't take her mind off things...)"
    MC "Are you enjoying that vibrator I bought for you?"

    scene SR2_ES1_Vib_p2

    Sara "Huh? Oh yeah, it's REALLY good."
    MC "Are you using it much?"
    Sara "Almost every day! Sometimes more than once. I like to imagine that it's your cock pressing up against my pussy, when I do it."
    MC "Do you still have it sitting in your room?"

    scene SR2_ES1_Vib_p3

    Sara "Yeah, it's right here. I hide it in my desk drawer."
    MC "Could you give me a show of how you use it?"
    Sara "Wh-What?"
    MC "I'd love to see how you use the vibrator on your body. Can you do that for me?"

    scene SR2_ES1_Vib_p4

    Sara "I... I guess so…"
    MC "(Woo! This is gonna be great!)"
    Sara "You have to promise… not to laugh, okay?"
    MC "Why would I laugh?"
    Sara "I tend to make… a lot of noises when I use it."
    MC "I’m not gonna laugh, I promise."

    scene SR2_ES1_Vib_p5

    Sara "(Deep breath) Okay…"
    Sara "I’ll just get my panties off here…"
    Sara "(I can’t believe I’m doing this on webcam…)"

    scene SR2_ES1_Vib_p6
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzzz*"
    Sara "Oooh…"
    MC "(I can hear the vibrator, and it looks like Sara has just found her clitoris!)"
    MC "(It’s a shame I can’t see anything though…)"
    MC "Sara, can you bring the webcam closer, so I can see?"

    scene SR2_ES1_Vib_p7

    Sara "Mmm! Uh huh! S-Sure! Ahh…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzzzzzz*"
    Sara "Oh… fuck…"
    MC "(That girl in the sex shop was right! A strong vibe was the way to go!)"

    scene SR2_ES1_Vib_p8

    Sara "C-Can you see it?"
    MC "Yeah! Your pussy looks amazing!"
    MC "I could just dive right in there and lick you for hours."
    Sara "[player_name]!"
    MC "Press the vibrator up close again. I want to watch you masturbate."

    scene SR2_ES1_Vib_p9
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzz*"
    Sara "Ah… Ah…. Ahhh!"
    MC "(It sounds like Sara’s having the time of her life right now!)"

    scene SR2_ES1_Vib_p10

    Sara "Mmm! Yes! MMM!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZZ*"
    MC "How does it feel, Sara?"

    scene SR2_ES1_Vib_p11

    Sara "Mmm! It’s soooo ahh…. fucking good!"
    Sara "Ugh! It’s like a- ahhh - w-warmth deep inside my belly! MMM!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZ*"
    Sara "God… it’s so fucking intense… Ahhh! AHHH!"
    MC "I want you to cum for me, Sara."

    scene SR2_ES1_Vib_p12

    Sara "God! Yes! I’m CUMMING! I’M CUMMING!"
    Sara "Hnnnngggg!!! AHHHHHHHHH!"
    MC "(Wow! She’s shaking and trembling! I’ve never seen a girl cum so intensely before!)"

    scene SR2_ES1_Vib_p13
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*KNOCK KNOCK*"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZ*"
    Sara "F-Fuck!"

    $ Mom_name = "???"

    Mom "Sara? What’s going on in there?"
    if persistent.incest_patch == True:
        $ Mom_name = __("Mom")
    else:
        $ Mom_name = "Linda"

    MC "(Oh shit!)"
    MC "Quick! Turn the vibe off and throw it under your bed!"

    scene SR2_ES1_Vib_p14

    Mom "Sara! I told you to study! You’re wasting your time with those online games again, aren’t you?"
    if persistent.incest_patch == True:
        Sara "N-No, M-Mom!"
    else:
        Sara "N-No, L-Linda!"

    Mom "Don’t you lie to me, young lady!"

    scene SR2_ES1_Vib_p15

    Sara "Whoaaaa!"
    "*THUD*"
    Mom "Pull yourself together and-"

    scene SR2_ES1_Vib_p16

    Mom "Why aren’t you wearing any panties?!"
    if persistent.incest_patch == True:
        Sara "I… uh… Mom!"
    else:
        Sara "I… uh… Linda!"
    Mom "Oh my God! Those WERE moans, I heard coming from your room!"

    scene SR2_ES1_Vib_p17

    Mom "Were you watching internet porn?!"
    if persistent.incest_patch == True:
        Sara "Mom, I-"
    else:
        Sara "Linda, I-"
    Mom "Right. That’s it. No more laptop for you. Turn it off, this instant."

    scene SR2_ES1_Vib_p18
    if persistent.incest_patch == True:
        Sara "B-But, Mom!"
    else:
        Sara "B-But, Linda!"
    Mom "Now, Sara! I said, turn off your laptop!"
    Sara "*Sniff* O-Okay…"

    scene SR2_ES1_Vib_p19

    Mom "Hold up - is your webcam on?"
    Mom "Have you been doing the cybersex with boys?!"
    MC "(Oh fuck!)"
    Sara "N-No! That red light means its turned off!"
    Mom "Ahh… Okay, that makes sense."
    Sara "*Sniff*"
    Mom "I swear to God! I will ground you for a year, if your grades do not improve, young lady."

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
