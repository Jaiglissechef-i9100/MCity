image CR4_MS1_p1 = "/images/home/caroline_room/morning/scenes/CR4_MS1/1.jpg"
image CR4_MS1_p2 = "/images/home/caroline_room/morning/scenes/CR4_MS1/2.jpg"
image CR4_MS1_p3 = "/images/home/caroline_room/morning/scenes/CR4_MS1/3.jpg"
image CR4_MS1_p4 = "/images/home/caroline_room/morning/scenes/CR4_MS1/4.jpg"
image CR4_MS1_p5 = "/images/home/caroline_room/morning/scenes/CR4_MS1/5.jpg"
image CR4_MS1_p6 = "/images/home/caroline_room/morning/scenes/CR4_MS1/6.jpg"
image CR4_MS1_p7 = "/images/home/caroline_room/morning/scenes/CR4_MS1/7.jpg"
image CR4_MS1_p8 = "/images/home/caroline_room/morning/scenes/CR4_MS1/8.jpg"
image CR4_MS1_p9 = "/images/home/caroline_room/morning/scenes/CR4_MS1/9.jpg"
image CR4_MS1_p10 = "/images/home/caroline_room/morning/scenes/CR4_MS1/10.jpg"
image CR4_MS1_p11 = "/images/home/caroline_room/morning/scenes/CR4_MS1/11.jpg"
image CR4_MS1_p12 = "/images/home/caroline_room/morning/scenes/CR4_MS1/12.jpg"
image CR4_MS1_p13 = "/images/home/caroline_room/morning/scenes/CR4_MS1/13.jpg"
image CR4_MS1_p14 = "/images/home/caroline_room/morning/scenes/CR4_MS1/14.jpg"



image CR4_MS1_blow_p1 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/1.jpg"
image CR4_MS1_blow_p2 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/2.jpg"
image CR4_MS1_blow_p3 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/3.jpg"
image CR4_MS1_blow_p4 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/4.jpg"
image CR4_MS1_blow_p5 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/5.jpg"
image CR4_MS1_blow_p6 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/6.jpg"
image CR4_MS1_blow_p7 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/7.jpg"
image CR4_MS1_blow_p8 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/8.jpg"
image CR4_MS1_blow_p9 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/9.jpg"
image CR4_MS1_blow_p10 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/10.jpg"
image CR4_MS1_blow_p11 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/11.jpg"
image CR4_MS1_blow_p12 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/12.jpg"
image CR4_MS1_blow_p13 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/13.jpg"
image CR4_MS1_blow_p14 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/14.jpg"
image CR4_MS1_blow_p15 = "/images/home/caroline_room/morning/scenes/CR4_MS1//Blowjob/15.jpg"

default CR4_MS1 = True
default CR4_MS1_talked = False


label CR4_MS1_label:
    if CR4_MS1_talked == True:
        hide screen map_button
        show screen caroline_room_morning
        $ clickable = False
        MC "Not now, [player_name]."
        $ clickable = True
        hide screen caroline_room_morning
        jump caroline_room_morning1
    else:

        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene CR4_MS1_p1 with dissolve


        MC "(Holy shit! Those are the tightest booty shorts I’ve ever seen in my life!)"
        MC "(Her ass looks fucking incredible. I wonder if she realises that herself.)"
        MC "(She’s wearing a pair of high-heel shoes as well - she must have deliberately chosen to dress this sexily.)"

        scene CR4_MS1_p2

        MC "(And seeing that I’m the only guy around to see her - she’s probably chosen to dress nice for me!)"
        MC "(I wonder if she’s even wearing a bra beneath that tight white top?)"
        MC "Hey, Caroline. Up to anything interesting? Just working on your makeup?"

        scene CR4_MS1_p3

        Caroline "Morning [player_name]. Sorry, I didn’t hear you come in there. I finished my makeup a few minutes ago. I WAS in the middle of tidying everything up, then I ended up getting distracted by this book. Haha!"
        MC "Anything interesting?"
        Caroline "Investing for Dummies. I’m planning to reinvest my profits into the stock market. Or maybe open up another store in another city."
        MC "Oh, that sounds really good! Have you thought about expanding overseas?"

        scene CR4_MS1_p4

        Caroline "I’ve toyed with the idea. Perhaps the UK or Ireland. I might just be safer opening up another one over here."
        Caroline "What was it you wanted me for by the way?"
        MC "I got your text about organising a date sometime. I was wondering if tonight suited you?"

        scene CR4_MS1_p5

        Caroline "Oh!"
        Caroline "(Shit! I was so engrossed in my work I completely forgot that I sent that text!)"
        MC "Umm, you okay? I can come back later if now isn’t a good time."

        scene CR4_MS1_p6

        Caroline "No, now is fine."
        Caroline "(Crap - I was so busy that I completely forgot to organize anything!)"
        MC "(Damn, she is so fucking hot!)"
        Caroline "Listen, I just need a little bit longer to finish planning our date. Are you free to meet up this afternoon?"

        scene CR4_MS1_p7

        MC "Sure, not a problem. I’ll catch you then. Where do you want to meet?"
        Caroline "I’m going to be at work, so would it be okay if you dropped by the store?"
        MC "Of course, I’ll see you then."

        scene CR4_MS1_p8

        MC "Do I need to bring anything with me?"
        Caroline "Don’t worry, you’ve been so good to me; I’ll take care of everything this time."
        MC "Well, if you’re sure!"

        scene CR4_MS1_p9

        Caroline "Say… before you go, would you like some… relief?"
        MC "Relief? Oh! Do you mean like a-"
        Caroline "Yes, I’m talking about unzipping your pants and sucking your fat cock."

        $ CR4_AS1 = True
        $ CR4_MS1_talked = True
        menu:
            "Yeah, definitely!":

                scene CR4_MS1_p10

                MC "Well, how could a guy ever say no to that?"
                MC "(Especially when you’re dressed up like that!)"
                Caroline "Hehe, that’s the spirit."

                scene CR4_MS1_p11

                MC "Where do you want me to go?"
                Caroline "Hmm… How about you lie back on my bed? We’ll take it from there."
                MC "Awesome!"

                jump CR4_MS1_blow
            "No thanks, but maybe later on.":


                scene CR4_MS1_p9

                MC "No thanks, maybe later on though."
                Caroline "Are you sure?"
                MC "Yeah, I’m fine at the minute. How about you sit on my knee for a while?"

                scene CR4_MS1_p12

                Caroline "I’m not too heavy, am I? I don’t want to hurt your legs."
                MC "Relax! You’re as light as a feather."
                Caroline "Haha, you and I both know that’s not true!"

                scene CR4_MS1_p13

                MC "(Caroline seems to have become much more intimate since becoming my girlfriend.)"
                MC "(She’s warmer now - almost as if she’s finally letting her guard down. It certainly took her long enough, but with an ex boyfriend like Charles I can understand why she put up so many barriers.)"
                Caroline "Y’know… you don’t have to call me Caroline all the time. If you’d prefer, you could just…"
                MC "Yeah?"
                Caroline "Nevermind, it’s silly."
                MC "No, go ahead. Please."

                scene CR4_MS1_p12

                Caroline "You can refer to me as “your girl” if you want."
                Caroline "Actually, forget that! It’s really cringey!"
                MC "No, I like it. It’s really cute."

                scene CR4_MS1_p13

                MC "I’m glad I can finally call you ‘my girl.’"
                MC "I love you, Caroline."

                Caroline "I love you too, [player_name]."

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump caroline_room_morning1

label CR4_MS1_blow:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    scene CR4_MS1_blow_p1


    Caroline "Oh wow! You are really, really hard right now!"
    MC "Well, that cute outfit you are wearing certainly helped!"
    Caroline "Well, if I’m the one that’s caused this problem, then it’s MY responsibility to fix it."

    scene CR4_MS1_blow_p2

    Caroline "*Mwah*"

    MC "Mmm… "
    MC "(Her lips are so warm and wet!)"

    scene CR4_MS1_blow_p3

    MC "(I honestly can’t think of a better way to start the day!)"
    Caroline "(I almost forgot how delicious his cock looks. I could suck on his thick dick all morning!)"

    scene CR4_MS1_blow_p4

    Caroline "(Time to blow [player_name]’s mind!)"
    Caroline "*Shlurp*"
    MC "Ohhh..."

    scene CR4_MS1_blow_p5

    Caroline "Mmmpfff!"
    MC "Uggghh! Ahh…"
    Caroline "*Shlurp*"
    Caroline "(Sounds like he’s really enjoying this!)"

    scene CR4_MS1_blow_p6

    MC "Oh yeah… Mmm! Just like that! Ugh! Don’t stop!"
    Caroline "*Suck* *Suck*"
    MC "Can you go deeper? Ahh…"

    scene CR4_MS1_blow_p7

    Caroline "Mmm hmm!"
    MC "Uhh, I guess that means, ‘yes’?"
    Caroline "*Shlurp*"

    scene CR4_MS1_blow_p8

    Caroline "*SHHLLLURRRRP*"
    MC "Oh yeah! Mmm! Deeper!"
    Caroline "(Maybe I should just let [player_name] take control this time? If he’s not satisfied with my technique then he manage it himself!)"

    scene CR4_MS1_blow_p9

    Caroline "Y’know what? You’re in charge now, big guy."
    MC "Huh? What do you mean?"
    Caroline "Just grab my hair and hold my head however you want it. Then thrust your hips and fuck my face."
    MC "Seriously?"
    Caroline "That’s what you want, isn’t it? To feel your sensitive cock slide down my tight little throat? You can even talk dirty to me, if that’s what you’re into."
    MC "Hell yeah!"
    Caroline "Then what are you waiting for? Man up and-"

    scene CR4_MS1_blow_p10

    Caroline "GLLLUMPPFFF!!!"
    MC "Thanks, Caroline! This is gonna be awesome!"
    Caroline "(Jesus, [player_name]! Give a girl a warning! Or at least let her finish her sentence!)"

    scene CR4_MS1_blow_p11

    MC "Ugh! Ahh! Oh fuck!"
    Caroline "MMPFF! GLMPPFF!"
    Caroline "*SHLURP* *SUCK*"
    MC "Mmm! Ahhhh! Yes! Ohhh!"

    scene CR4_MS1_blow_p12

    menu:
        "Fuck, that’s it! Suck on my cock you fucking slut!":


            MC "Fuck, that’s it! Suck on my cock you fucking slut!"
            Caroline "MPPLFFFF!!!"
            MC "Ugh! Fuck! Ahh!"

            jump CR4_MS1_blow_con1
        "...":


            Caroline "MPPLFFFF!!!"
            MC "Ugh! Fuck! Ahh!"

            jump CR4_MS1_blow_con1

label CR4_MS1_blow_con1:
    scene CR4_MS1_blow_p13
    menu:
        "Oh yeah, just like that! Hnnnggg! Suck it, you whore!":

            MC "Oh yeah, just like that! Hnnnggg! Suck it, you whore!"
            Caroline "(Hearing [player_name] talk so dirty is getting me all wet! Maybe this wasn’t such a good idea to do in the morning! I’m going to have to spend another hour with my dildo before I head out to work!)"
            jump CR4_MS1_blow_con2
        "...":

            jump CR4_MS1_blow_con2

label CR4_MS1_blow_con2:


    Caroline "*Shlluurrrp*"

    scene CR4_MS1_blow_p14

    MC "Oh shit! I’m cumming! Hnnnggg! Ugh!"
    Caroline "(Holy crap! I can feel his shaft pulsating on my tongue - he’s about to blow his load in my mouth!)"
    Caroline "*SUCK SUCK*"

    scene white with dissolve

    $ renpy.pause(0.7, hard = True)
    scene CR4_MS1_blow_p14 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR4_MS1_blow_p15 with dissolve

    MC "Aahhhhh!"
    Caroline "*GULP GULP*"
    MC "Ohhh… fuck... Mmm! Your mouth is incredible, Caroline."

    scene CR4_MS1_p14

    Caroline "Well, it certainly felt like you enjoyed facefucking me!"
    MC "It was the best! *Pant* I’m still catching my breath! Haha!"
    Caroline "I’m glad you liked it; don’t forget to drop by the shop later on today to discuss our date."
    MC "Oh yeah, I won’t. I’ll catch up with you in the afternoon."


    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
    $ can_hide_windows = False
    jump corridor_morning1