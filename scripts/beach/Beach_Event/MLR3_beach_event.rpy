image MLR3_beach_event_p1 = "images/Beach/MLR3_beach_event/1.jpg"
image MLR3_beach_event_p2 = "images/Beach/MLR3_beach_event/2.jpg"
image MLR3_beach_event_p3 = "images/Beach/MLR3_beach_event/3.jpg"
image MLR3_beach_event_p4 = "images/Beach/MLR3_beach_event/4.jpg"
image MLR3_beach_event_p5 = "images/Beach/MLR3_beach_event/5.jpg"
image MLR3_beach_event_p6 = "images/Beach/MLR3_beach_event/6.jpg"
image MLR3_beach_event_p7 = "images/Beach/MLR3_beach_event/7.jpg"
image MLR3_beach_event_p8 = "images/Beach/MLR3_beach_event/8.jpg"
image MLR3_beach_event_p9 = "images/Beach/MLR3_beach_event/9.jpg"
image MLR3_beach_event_p10 = "images/Beach/MLR3_beach_event/10.jpg"
image MLR3_beach_event_p11 = "images/Beach/MLR3_beach_event/11.jpg"
image MLR3_beach_event_p12 = "images/Beach/MLR3_beach_event/12.jpg"
image MLR3_beach_event_p13 = "images/Beach/MLR3_beach_event/13.jpg"
image MLR3_beach_event_p14 = "images/Beach/MLR3_beach_event/14.jpg"
image MLR3_beach_event_p15 = "images/Beach/MLR3_beach_event/15.jpg"
image MLR3_beach_event_p16 = "images/Beach/MLR3_beach_event/16.jpg"
image MLR3_beach_event_p17 = "images/Beach/MLR3_beach_event/17.jpg"
image MLR3_beach_event_p18 = "images/Beach/MLR3_beach_event/18.jpg"
image MLR3_beach_event_p19 = "images/Beach/MLR3_beach_event/19.jpg"
image MLR3_beach_event_p20 = "images/Beach/MLR3_beach_event/20.jpg"
image MLR3_beach_event_p21 = "images/Beach/MLR3_beach_event/21.jpg"
image MLR3_beach_event_p22 = "images/Beach/MLR3_beach_event/22.jpg"
image MLR3_beach_event_p23 = "images/Beach/MLR3_beach_event/23.jpg"
image MLR3_beach_event_p24 = "images/Beach/MLR3_beach_event/24.jpg"
image MLR3_beach_event_p25 = "images/Beach/MLR3_beach_event/25.jpg"
image MLR3_beach_event_p26 = "images/Beach/MLR3_beach_event/26.jpg"
image MLR3_beach_event_p27 = "images/Beach/MLR3_beach_event/27.jpg"
image MLR3_beach_event_p28 = "images/Beach/MLR3_beach_event/28.jpg"
image MLR3_beach_event_p29 = "images/Beach/MLR3_beach_event/29.jpg"
image MLR3_beach_event_p30 = "images/Beach/MLR3_beach_event/30.jpg"
image MLR3_beach_event_p31 = "images/Beach/MLR3_beach_event/31.jpg"
image MLR3_beach_event_p32 = "images/Beach/MLR3_beach_event/32.jpg"
image MLR3_beach_event_p33 = "images/Beach/MLR3_beach_event/33.jpg"
image MLR3_beach_event_p34 = "images/Beach/MLR3_beach_event/34.jpg"
image MLR3_beach_event_p35 = "images/Beach/MLR3_beach_event/35.jpg"
image MLR3_beach_event_p36 = "images/Beach/MLR3_beach_event/36.jpg"

label MLR3_beach_event:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.sound.play("sfx/door_squeak.mp3")
    "*Creak*"

    scene MLR3_beach_event_p1 with dissolve

    $ renpy.sound.play("sfx/clothes.mp3")
    "*Thud*"

    MC "Zzz…"
    $ renpy.sound.play("sfx/wood1.wav")

    "*Thud*"
    MC "Hmm? (What the hell is all that banging?)"

    $ renpy.music.stop(channel="sound")
    scene MLR3_beach_event_p2

    MC "Huh? [Mom_name]?"
    MC "*Yawn*"
    MC "(What’s she doing in my room, this early in the morning?)"

    scene MLR3_beach_event_p3

    MC "(Not that I’m complaining - the view is great!)"
    MC "(Why is she rummaging through my drawers? Maybe she’s putting some ironing away?)"

    scene MLR3_beach_event_p4

    Mom "Ah, you’re finally awake."
    MC "Ugh… morning. *YAWN*"
    Mom "You looked tired, so I let you sleep in, and packed your clothes for you."

    scene MLR3_beach_event_p5

    MC "Sweet! Thanks, [Mom_name]!"
    Mom "No problem, Honey. That’s us, all ready to go to the beach now. I was thinking that we should probably leave in the next five minutes, before people start waking up."
    Mom "I don’t want them to see us leaving the house together and get suspicious."

    scene MLR3_beach_event_p6

    MC "Yeah, no problem. I understand. Let me get dressed quickly and I’ll meet you out by the car."
    Mom "Great, thanks. We’re going to have an amazing time together - I promise!"

    scene MLR3_beach_event_p7

    Mom "*Mwah*"
    MC "(Mom just kissed my forehead there. She used to do that, when I was really young, before I went to sleep.)"
    MC "(I never appreciated the view that came with those kisses, when I was that age.)"

    scene MLR3_beach_event_p8

    Mom "Throw some clothes on and creep out to the car. I’ll be waiting in the driver’s seat."
    MC "Sure. No problem."
    Mom "And don’t forget your luggage! It’d be awful if you didn't have any clothes to wear."
    Mom "(Actually… that would be kind of fucking hot.)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR3_beach_event_p9

    "*Brummm*"

    Mom "This is the first time you’ve been on holiday this year, isn't it?"
    if renpy.loadable("patch.rpy"):
        MC "Yeah, the last time I think I went was… Hmm… Where did we all go last year, as a family?"
    else:
        MC "Yeah, the last time I think I went was… Hmm… Where did we all go last year, as a group?"
    scene MLR3_beach_event_p10

    Mom "It was Peurto Rico. Remember we all went camping in the El Yunque national forest?"
    MC "Oh yeah! Was that a year ago? It seems so much longer."
    if renpy.loadable("patch.rpy"):
        Mom "It was a year. I went hiking with the girls while you hung out with your father. What did you two end up doing?"
    else:
        Mom "It was a year. I went hiking with the girls while you hung out with Bob. What did you two end up doing?"
    scene MLR3_beach_event_p11

    MC "[Dad_name] snuck his rod with him, so we ended up illegally fishing. He kept throwing them back in after he caught them."
    if renpy.loadable("patch.rpy"):
        Mom "Haha! That’s so your father: Nothing can get between him and his fishing."
    else:
        Mom "Haha! That’s so Bob: Nothing can get between him and his fishing."
    MC "It wasn’t amazing fun, but I did kinda enjoy hanging out with him."
    Mom "It’ll be quite a long drive. I’d suggest closing your eyes and catching up on your sleep. I’ll wake you up when we get there."
    MC "*Yawn* Thanks, [Mom_name]."

    $ can_hide_windows = False
    scene map_day1
    show screen map
    show screen car_move_beach_notclickable
    call screen car_move_beach

screen car_move_beach_notclickable:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
    timer 9 action [Jump("MLR3_beach_event2")]

screen car_move_beach:
    modal True

    button action NullAction()

    add "images/Beach/MLR3_beach_event/car_map.png" at carbeach

transform carbeach:

    rotate 90
    xalign 0.3
    yalign 0.55
    linear 1.8 xalign 0.48

    linear 0.3 rotate 0
    linear 2.4 yalign 0.1

    linear 0.3 rotate 90
    linear 3.5 xalign 0.93

label MLR3_beach_event2:
    hide screen map
    hide screen car_move_beach_notclickable
    hide screen car_move_beach
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(2,hard=True)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    MC "Zzz…"
    scene MLR3_beach_event_p12 with dissolve
    Mom "Hey [player_name]! Wake up, we’re almost there."
    MC "Hmm?"
    MC "Oh cool! Wow, it’s stunning!"
    Mom "Let’s pull up and get changed into our swimwear."
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR3_beach_event_p13 with dissolve

    MC "The views are spectacular!"
    Mom "Yup! The first time I ever came to this place, I thought, I have to bring [player_name] here someday."
    MC "Really? You thought that?"

    scene MLR3_beach_event_p14

    Mom "Honestly? I’ve had a lot of thoughts about you and me visiting this place together."
    MC "That’s so sweet, [Mom_name]."
    Mom "Well, if you knew ALL my thoughts, you’d probably not think of me as ‘sweet’. Some of them were pretty dirty."

    scene MLR3_beach_event_p15

    MC "Haha, I already know that."
    Mom "This was where I was planning to make my move on you for the first time. I wanted to bring you here one day."
    MC "Oh yeah? How were you planning to do that?"

    scene MLR3_beach_event_p16

    Mom "I had a couple of tricks… Most of them were just silly fantasies that would have scared you off though."
    MC "Aww, c’mon! I wanna hear them!"
    Mom "No, they’re embarrassing!"

    scene MLR3_beach_event_p17

    MC "Please tell me! I really wanna know!"
    Mom "Haha, fine! You have to promise not to laugh, though. These were SILLY ideas!"
    MC "Okay, I swear I’m not going to laugh."
    Mom "Alright… *Deep breath*"

    scene MLR3_beach_event_p18
    if renpy.loadable("patch.rpy"):
        Mom "I had a few plans. My original goal was to get you SO turned on that you needed to fool around with a girl, even if it meant your own mother."
    else:
        Mom "I had a few plans. My original goal was to get you SO turned on that you needed to fool around with a girl, even if it would be me."
    Mom "I was planning to take you away on a holiday up here, but deliberately leave my bikini top behind. I was going to act all disappointed about not being able to go swimming."
    Mom "Eventually, I was hoping you’d cave and agree to let me swim topless with you."

    scene MLR3_beach_event_p19

    Mom "You’d see my naked breasts, but you would be too nervous to say anything. The longer we swam around together, the hornier you would get."
    Mom "I was planning to tease you throughout the day too. Seductively eating a banana, sucking a drink through a straw, showering with the door open. Stuff like that."
    Mom "I had to get you SO horny that you couldn’t resist my advances that would happen that night."

    scene MLR3_beach_event_p20

    MC "How were you actually going to initiate something with me though? I mean, were you not worried I’d freak out and run away?"
    Mom "Of course, I was! Sometimes… Sometimes I still am."
    MC "You’re still scared I’ll run away?"

    scene MLR3_beach_event_p21
    if renpy.loadable("patch.rpy"):
        Mom "I guess so… Not very often - just sometimes. It’s not normal for a mother to be dating her son like this. I’m scared peer pressure might get to you, and you’ll just freak out and leave me someday."
    else:
        Mom "I guess so… Not very often - just sometimes. It’s not normal for me to be dating someone as young as you like this. I’m scared peer pressure might get to you, and you’ll just freak out and leave me someday."
    MC "[Mom_name], that’s not going to happen. I’m in love with you."
    Mom "Thank you, [player_name]. It’s reassuring to hear you say that."

    scene MLR3_beach_event_p22

    MC "(Her hand is so warm against mine. I love just lying beside her like this. No fear of who sees us, or worries about getting caught.)"
    MC "So yeah, how were you planning to kick things off with me?"
    Mom "Ahh…"

    scene MLR3_beach_event_p23

    Mom "Well… once I knew you were extremely horny I was going to give you some time alone. I know that a guy your age couldn’t resist an opportunity to start masturbating."
    MC "Oh, c’mon! We’re not THAT bad!"
    Mom "Haha! Yes you are!"

    scene MLR3_beach_event_p24

    Mom "Are you gonna let me finish the story?"
    MC "Sorry, my bad."
    Mom "C’mon closer beside me."

    scene MLR3_beach_event_p25

    Mom "Anyway, I’d planned to give you some time alone. I knew you’d start masturbating."
    Mom "My plan was to walk in on you, completely topless, and act surprised."
    Mom "As for what happens next… I’ve had a dozen different fantasies play through my head while I finger myself and think about it."

    scene MLR3_beach_event_p26

    Mom "In some of them, I sit down and spread my legs for you, letting you gaze at me while I masturbate in front of you."
    Mom "You’re a little hesitant at first, but you soon get into it."
    MC "Mmm, I like that one."

    scene MLR3_beach_event_p27

    Mom "Another one of my fantasies is that I pretend to trip when I catch you masturbating, accidentally falling face-first into your lap."
    Mom "I’d ‘accidentally’ let your cock slip into my mouth, and you just wouldn’t be able to resist the sudden pleasure it gave you."
    MC "You’ve got a really dirty mind, you know that, [Mom_name]?"
    Mom "Hehe, I know. It’s filthy."
    MC "So, what if I didn’t like this sudden blowjob out of nowhere?"
    Mom "Whether you wanted it or not, I was probably going to pin you down and keep sucking, and sucking, and sucking until you came."

    scene MLR3_beach_event_p28

    MC "Mmm… Fuck… that’s so hot."
    Mom "I know, right?"
    Mom "I’ve got YEARS of pent up sexual frustration, and tonight I’m taking them all out on you."
    Mom "You lucky bastard."

    scene MLR3_beach_event_p29

    MC "Mmm!"
    Mom "Mmm…"
    Mom "(My fantasies are finally coming true!)"

    scene MLR3_beach_event_p30

    MC "Y’know, I’m really enjoying these fantasies about how you planned to seduce me. Could you tell me a couple more?"
    Mom "Haha, sure. Hmm…"
    Mom "Another favourite of mine was a little… rapey."

    scene MLR3_beach_event_p31

    MC "Rapey?"
    Mom "Y’know… tying your wrists and ankles to the bed, riding your cock, just jumping at you and taking what I wanted."
    MC "Yeah, I’m kinda glad you didn’t open with that idea."
    Mom "Haha, me too!"

    scene MLR3_beach_event_p32

    Mom "I also thought about paying a girl about your age to seduce you."
    MC "Huh?! Why?"
    Mom "She’d get you all turned on, then blindfold you. Once that was all done I’d pay her the money and take over myself."

    scene MLR3_beach_event_p33
    if renpy.loadable("patch.rpy"):
        Mom "I’d be able to suck and fuck you all I wanted and you’d never know that you were fooling around with your own mother."
    else:
        Mom "I’d be able to suck and fuck you all I wanted and you’d never know that you were fooling around with me."
    Mom "After you climaxed I’d bring the girl back in and you’d think nothing was out of the ordinary."
    Mom "The best part about this idea was that I could have kept it going, over and over. At least until you got fed up with the blindfold."
    MC "You’ve put WAY too much time into thinking about this stuff!"

    scene MLR3_beach_event_p34

    Mom "I know, tell me about it. Sometimes I get so damn horny that I even have to masturbate at work!"
    MC "You finger yourself at work?"

    scene MLR3_beach_event_p35

    Mom "Sometimes. I’ve got my own private office, so I can do it without people noticing me."
    Mom "The hardest part is, keeping my voice down."
    Mom "I don't know why, but something about having sex in public places and the thrill of getting caught gets me SOOOO wet."

    scene MLR3_beach_event_p36

    MC "Thanks again for bringing me to the beach, [Mom_name]. It’s really nice here."
    MC "And for the record, I love the other ideas you had for seducing me. They were really hot."
    Mom "Hehe, I’m glad you enjoyed them. I know I have!"

    scene MLR3_beach_event_p33

    Mom "Okay, let’s check other stuff at the beach, unless you're trying to keep me in the full sun until evening."
    MC "What? Of course not. "
    Mom "I’ll be just behind you."
    $ day_time = 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ MLR3_beach_cliff = True
    $ MLR3_beach_drink = True
    $ MLR3_beach_ice = True
    $ MLR3_beach_sun = True
    jump beach_M1
