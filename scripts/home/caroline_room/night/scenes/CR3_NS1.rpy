image CR3_NS1_p1 = "images/home/caroline_room/night/scenes/CR3_NS1/1.jpg"
image CR3_NS1_p2 = "images/home/caroline_room/night/scenes/CR3_NS1/2.jpg"
image CR3_NS1_p3 = "images/home/caroline_room/night/scenes/CR3_NS1/3.jpg"
image CR3_NS1_p4 = "images/home/caroline_room/night/scenes/CR3_NS1/4.jpg"
image CR3_NS1_p5 = "images/home/caroline_room/night/scenes/CR3_NS1/5.jpg"
image CR3_NS1_p6 = "images/home/caroline_room/night/scenes/CR3_NS1/6.jpg"
image CR3_NS1_p7 = "images/home/caroline_room/night/scenes/CR3_NS1/7.jpg"
image CR3_NS1_p8 = "images/home/caroline_room/night/scenes/CR3_NS1/8.jpg"
image CR3_NS1_p9 = "images/home/caroline_room/night/scenes/CR3_NS1/9.jpg"
image CR3_NS1_p10 = "images/home/caroline_room/night/scenes/CR3_NS1/10.jpg"
image CR3_NS1_p11 = "images/home/caroline_room/night/scenes/CR3_NS1/11.jpg"
image CR3_NS1_p12 = "images/home/caroline_room/night/scenes/CR3_NS1/12.jpg"

label CR3_NS1_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if CR3_NS1_can == 3:
        scene CR3_NS1_p1 with dissolve
        MC "It's not a good idea, to wake her up."
        $ can_hide_windows = False
        jump caroline_room_morning1

    if CR3_NS1_can == False:
        scene CR3_NS1_p1 with dissolve
        MC "It's not a good idea, to wake her up again. She was mad the last time - so now she will probably be furious..."
        $ can_hide_windows = False
        jump caroline_room_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

        scene CR3_NS1_p1 with dissolve

        MC "(Whispered) Caroline?"
        Caroline "Zzz..."
        MC "(She’s asleep. Hopefully she won’t mind, me waking her up.)"

        scene CR3_NS1_p2

        MC "(I know, the deal between us is off, but I can’t get her out of my head. If I’m never going to be with her again, then I want our last time together to be - something special and memorable.)"
        MC "(I was hoping that what we had would - develop into something more - that maybe, one day, she would start to feel attracted to me, and love me.)"
        MC "(Perhaps, that just wasn’t supposed to happen.)"

        scene CR3_NS1_p3

        MC "(Whispered) Hey, Caroline?"
        Caroline "*Snore*"
        MC "(She’s fast asleep. I don’t want to shake her awake - I guess I could try and pull the covers back. Maybe that will wake her up.)"

        scene CR3_NS1_p4

        MC "(There we go. I’ll just fold them, over here for her.)"
        MC "(Whispered) Caroline? Wake up... It’s just me."
        Caroline "Hmm…"

        scene CR3_NS1_p5

        MC "(Whispered) Hey, Caroline!"
        Caroline "Huh? [player_name]? What are you doing in my room? What time is it?"
        MC "It’s… quite late."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)
        scene CR3_NS1_p6

        Caroline "Ugh… I’ve got to get up, early in the morning. What did you wake me for?"
        MC "I’m sorry, Caroline. I just..."
        Caroline "Just what..?"

        scene CR3_NS1_p7

        MC "I just wanted... to know..."
        MC "I can’t stop thinking about - what we had together, all the fun of that deal, how happy it, made BOTH of us."
        MC "And don’t tell me that you didn’t enjoy it too - I KNOW you did. You were always smiling, when we were together."

        scene CR3_NS1_p8

        MC "Please, Caroline... I know it’s over now, but can we, at least, just mark it with - one final night - between the two of us?"
        Caroline "[player_name]..."
        MC "Please... I never had any closure. This all ended so suddenly - and to be honest, I’m not even certain why!"

        scene CR3_NS1_p9

        Caroline "[player_name], you have to leave..."

        MC "B-But-"
        Caroline "No buts! Please don’t make this, any harder for yourself. You need to move on."
        MC "Don’t you want - one last-"
        if renpy.loadable("patch.rpy"):
            Caroline "No, I don’t. You’re my brother, [player_name]. Anything that we did together, was completely wrong. Go back to bed."
        else:
            Caroline "No, I don’t. You’re my very close friend, [player_name]. Anything that we did together, was - completely wrong. Go back to bed!"

        scene CR3_NS1_p10

        MC "(I can’t believe it... It’s really over.)"
        MC "(I’m never going to be with her again.)"
        MC "(Jesus Christ... I don’t even know what I did, to fuck this up! It’s like - a switch was suddenly flicked - and now she hates me!)"

        scene CR3_NS1_p11

        Caroline "*Sniff*"
        MC "(Is she crying? Fuck! Now I’ve gone and upset her too.)"
        MC "(How the fuck did I make this - awful situation - any worse than already was?)"
        $ CR3_NS1_can = False

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump corridor_morning1
