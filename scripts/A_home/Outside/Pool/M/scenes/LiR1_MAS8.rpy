image LiR1_MAS8_p1 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/1.jpg"
image LiR1_MAS8_p2 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/2.jpg"
image LiR1_MAS8_p3 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/3.jpg"
image LiR1_MAS8_p4 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/4.jpg"
image LiR1_MAS8_p5 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/5.jpg"
image LiR1_MAS8_p6 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/6.jpg"
image LiR1_MAS8_p7 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS8/7.jpg"

default LiR1_MAS8_talked = False
label LiR1_MAS8_label:
    if LiR1_MAS8_talked == True:
        if day_time == 1:
            show screen a_pool_M_scr
        if day_time == 2:
            show screen a_pool_D_scr
        $ clickable = False
        MC "I've aleredy talked to her. I should go talk to [Liza2_name]."
        $ clickable = True
        jump a_pool_M1
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene LiR1_MAS8_p1 with dissolve

        Yazmin "(Ohh... here comes the star of the show!)"
        MC "(Yazmin’s looking pretty intently at me! I wonder what’s on her mind, after the - last fiasco - when I fucked her, in front of [Liza2_name].)"

        scene LiR1_MAS8_p2

        Yazmin "Hello there, handsome."
        MC "Hey, Yazmin."
        Yazmin "Have you recovered, after your last round with me?"
        MC "Huh? What do you mean?"

        scene LiR1_MAS8_p3

        Yazmin "I seem to recall you, cumming - very... very... hard. And honestly - ...rather quickly - when I was riding you."
        MC "Shush! [Liza2_name] might hear you! Was she not - super pissed off at you - afterwards?"
        Yazmin "No? Why would she be?"

        scene LiR1_MAS8_p4

        MC "It REALLY sounded like she was going to be furious with you. I mean - you were practically cheating on her - RIGHT in front of her face!"
        Yazmin "Hehe... I guess I kinda was. At least I was blatantly honest about it though."
        MC "Umm... you kinda weren’t. Remember the ice lolly and the blindfold?"

        scene LiR1_MAS8_p5

        Yazmin "Heeeey! This isn’t ALL my fault! You participated in this too! - Don’t make ME out to be - the bad guy - here!"
        if renpy.loadable("patch.rpy"):
            Yazmin "(Sigh) Anyway - I’m not here to get into an argument with you. Your Aunt Liza has calmed down."
        else:
            Yazmin "(Sigh) Anyway - I’m not here to get into an argument with you. Liza has calmed down."
        MC "Really? She’s not angry at me?"

        scene LiR1_MAS8_p6

        Yazmin "I’m - almost certain - she’s not..."
        MC "Almost certain?"
        Yazmin "I mean, she’s probably still A LITTLE bit pissed at me - for making her suck your cock... But that was- Ugh... fine! I’ll admit it - That was my bad."

        scene LiR1_MAS8_p7

        Yazmin "Anyway - half my degree - was in public relations. I’m EXTREMELY good, at swaying people’s opinions."
        MC "What are you getting at?"
        if renpy.loadable("patch.rpy"):
            Yazmin "Your aunt is now waiting for you in the bathroom - for round two."
        else:
            Yazmin "Liza is now waiting for you in the bathroom - for round two."
        MC "Round two of what?"
        Yazmin "Just go inside and talk with her. Please...?"
        MC "(I hope she’s not gonna kill me, and Yazmin is not lying...)"
        $ LiR1_MAS9 = True
        $ LiR1_MAS8_talked = True
        $ LiR1_MAS8_can1 = False

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump a_pool_M1
