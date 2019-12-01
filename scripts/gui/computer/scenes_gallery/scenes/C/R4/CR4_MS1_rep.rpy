label CR4_MS1_rep:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.stop(channel="music2", fadeout=1)
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
    scene CR4_MS1_blow_p4anim with dissolve
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
    scene CR4_MS1_blow_p7anim with dissolve
    Caroline "*Shlurp*"

    scene CR4_MS1_blow_p8

    Caroline "*SHHLLLURRRRP*"
    scene CR4_MS1_blow_p8anim with dissolve
    MC "Oh yeah! Mmm! Deeper!"
    Caroline "(Maybe I should just let [player_name] take control this time? If he’s not satisfied with my technique then he can direct me it himself!)"

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
    scene CR4_MS1_blow_p10anim with dissolve
    Caroline "(Jesus, [player_name]! Give a girl a warning! Or at least let her finish her sentence!)"

    scene CR4_MS1_blow_p11

    MC "Ugh! Ahh! Oh fuck!"
    Caroline "MMPFF! GLMPPFF!"
    Caroline "*SHLURP* *SUCK*"
    MC "Mmm! Ahhhh! Yes! Ohhh!"

    scene CR4_MS1_blow_p12anim

    menu:
        "Fuck, that’s it! Suck on my cock, you fucking slut!":


            MC "Fuck, that’s it! Suck on my cock, you fucking slut!"
            Caroline "MPPLFFFF!!!"
            MC "Ugh! Fuck! Ahh!"

            jump CR4_MS1_blow_con1_rep
        "...":


            Caroline "MPPLFFFF!!!"
            MC "Ugh! Fuck! Ahh!"

            jump CR4_MS1_blow_con1_rep

label CR4_MS1_blow_con1_rep:
    scene CR4_MS1_blow_p13
    menu:
        "Oh yeah, just like that! Hnnnggg! Suck it, you whore!":

            MC "Oh yeah, just like that! Hnnnggg! Suck it, you whore!"
            Caroline "(Hearing [player_name] talk so dirty is getting me all wet! Maybe this wasn’t such a good idea to do in the morning! I’m going to have to spend another hour with my dildo before I head out to work!)"
            jump CR4_MS1_blow_con2
        "...":

            jump CR4_MS1_blow_con2_rep

label CR4_MS1_blow_con2_rep:


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
    Caroline "I’m glad you liked it. Don’t forget to drop by the shop later on today to discuss our date."
    MC "Oh yeah, I won’t. I’ll catch up with you in the afternoon."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label