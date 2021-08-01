label MLR3_NS1_rep:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)

    $ can_hide_windows = True
    scene black
    $ renpy.pause(2,hard= True)

    scene MLR2_NS1_p1 with dissolve
    MC "(Let’s see what [Mom_name] and [Dad_name] are up to now. I can’t hear anything, so they’re probably both asleep anyway.)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    $ renpy.sound.play("sfx/door_squeak.mp3")
    scene MLR3_NS1_p1

    Dad "Zzz..."
    Mom "*Heavy Breathing*"
    Mom "(Why do I feel so damn hot right now? I can’t get [player_name] out of my head."

    scene MLR3_NS1_p2

    Mom "(And every single time I close my eyes, I think back to that night in the beach house.)"
    Mom "(His raw hard cock, felt so good, deep inside me. It’s like a damn addiction, I need to feel it again. I NEED to be fucked by [player_name] again.)"
    Mom "*Heavy Breathing*"

    MC "([Mom_name]’s breathing really loudly. I wonder if she’s alright.)"

    scene MLR3_NS1_p3

    Mom "(Fuck… I loved it when I felt his thick shaft, pushing up against my pussy for the first time.)"
    Mom "Mmm…"
    MC "(Is [Mom_name] masturbating?!)"

    scene MLR3_NS1_p4

    Mom "Ah…"
    MC "(She’s moaning right now! There’s no doubt about it - she’s fingering herself while [Dad_name] sleeps.)"
    Mom "(Oh God… I need to book another night away with [player_name]. It needs to be longer next time though.)"

    scene MLR3_NS1_p5

    Mom "(One night wasn’t enough. I don’t want to feel rushed into leaving, when I wake up the next day.)"
    Mom "(I want to be able to hold him and cuddle beside him without stressing about having to come back to Bob.)"
    Mom "Ah… Ohh… Yes..."

    scene MLR3_NS1_p6

    Mom "(I can just imagine him, thrusting his thick cock, deep into me. No condom; just his hard dick, plunging again and again, into my soaking wet pussy.)"
    scene MLR3_NS1_p6anim with dissolve
    Mom "Ah! Ahhh!"
    MC "(Wow! She’s really getting loud now!)"

    scene MLR3_NS1_p7

    Mom "Oh! AH! AHHH!"
    MC "(It’s weird that [Dad_name] hasn’t woken up yet! Caroline and Sara can probably hear her, from the other side of the house!)"
    Dad "Hmm…"

    scene MLR3_NS1_p8

    Mom "AH! AHHH! OHH FUCK!"
    Dad "Huh? What the…"
    Dad "(Is she… masturbating in the middle of the night?!)"

    scene MLR3_NS1_p9

    Mom "(I can’t wait until I can feel his, steaming hot cum, flowing into my pussy again. The warmth spreading, deep inside me, as my boy fills me up.)"
    Mom "Ah! AHHHHHH! Mmmmmmm! OHHHHH!!!"
    MC "(Uh oh… It looks like she’s woken up [Dad_name]!)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)

    scene MLR3_NS1_p10

    Dad "Jesus Christ, Linda. What in God’s name are you doing? It’s the middle of the night?!"
    Dad "I don’t know about you, but I’m exhausted from my job, and if I can’t have sex in this bed, then for the love of God, at least let me have a good night’s sleep in it!"
    Dad "I mean, seriously, Linda. You don’t want to have sex with me, but you’re creaming yourself, at two am in the bloody morning!"

    scene MLR3_NS1_p11

    Mom "Shit… Sorry for waking you. My bad."
    Dad "My bad? Is that all you have to say about this?"
    Mom "Yeah, I was too loud. My fault. Sorry."

    scene MLR3_NS1_p12

    Dad "Linda… I know this relationship is headed the way of the Titanic, but can we at least TRY to resolve our issues."
    Dad "The only thing I want right now, is for you to open up and actually talk to me."
    Dad "Please... "

    scene MLR3_NS1_p13

    Mom " …"
    Mom "I’m tired, Bob. I’m going to go to sleep now."
    Dad "*Sigh*"
    Mom "I’m sorry for waking you up."
    Dad "Goodnight, Linda."

    MC "(Jesus Christ, they’re getting worse with each passing day. I wonder if I am the only cause of this. Maybe they were already on the rocks, before [Mom_name] and me hit it off?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label

