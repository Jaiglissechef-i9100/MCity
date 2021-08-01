label sara_pad_win_v1:
    hide screen scenes_gallery
    scene sara_room_evening_scene3_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "I said flank left! That’s the right flank, you dumbos!"
    MC "(Wow, looks like Sara’s teammates aren’t up to scratch today!)"
    Sara "Grr! We lost the match because of you guys! I’m off now. Chat later!"

    scene sara_room_evening_scene3_v1_p2
    Sara "Oh! Hey, [player_name]! Didn’t see you standing there. Do you fancy a rematch?"
    MC "(I’ve swapped the working controller for the cheap Chinese knock-off version! This should give me the edge I need to beat her!)"
    MC "Yeah, I’m ready whenever you are!"

    scene sara_room_evening_scene3_v1_p3
    Sara "Sweet! Let me get it set up here."
    Sara "Do you want to play Street Brawler VII again? Or something else this time?"
    MC "Street Brawler works for me."
    Sara "Coolio!"


    scene sara_room_evening_scene3_v1_p4
    Sara "Hehe - you do know you’re gonna lose again, right?"
    MC "Perhaps."
    Sara "And you know the penalty for losing?"
    MC "I lose a piece of clothing."
    Sara "Yup! Now let’s get started!"

    scene sara_room_evening_scene3_v1_p5
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    "(Three Minutes Later…)"
    $ renpy.pause(2.0)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Console "FATALITY!"
    Sara "Wh-What?! N-No way!"
    MC "That’s one-nil, Sara! Time to lose a piece of clothing."

    scene sara_room_evening_scene3_v1_p6
    Sara "B-But I’m n-not wearing a bra…"
    MC "Then lose your denim shorts."
    Sara "I… I’m not w-wearing any… *ahem* either…"
    MC "You’re not wearing ANY underwear?"
    Sara "Look away while I take my top off…"

    scene sara_room_evening_scene3_v1_p7
    MC "Fine."

    menu:
        "Sneak a peek while she is taking her top off.":
            window hide
            scene sara_room_evening_scene3_v1_p7a at pandown1
            $ renpy.pause(2.0, hard=True)
            MC "(Holy shit! She’s so fucking hot!)"
            Sara "(I can’t believe this… it’s so embarrassing!)"
            Sara "(Why didn’t I wear any underwear?! I was sooo consident that I was going to win again!)"
            MC "(Hehe - this broken controller is working like a charm! She doesn’t know what the hell is going on!)"
            jump after_choice_sis_nerdy_evening_scene31r
        "Be nice and let Sara undress without peeking.":


            scene sara_room_evening_scene3_v1_p7
            MC "Fine, I won’t look."
            Sara "Thank you…"
            MC "Are you done yet?"
            Sara "Almost..."
            jump after_choice_sis_nerdy_evening_scene31r

label after_choice_sis_nerdy_evening_scene31r:

    scene sara_room_evening_scene3_v1_p8
    MC "(Her nipples are pretty stiff! She must be secretly enjoying this!)"
    Console "ROUND 2! FIGHT!"
    Sara "I’m gonna beat your ass this time!"
    MC "Oh yeah? You really think so?"
    Sara "Dammit! I pressed X three times! Why didn’t it work?!"
    Console "C-C-COMBO BREAKER!"

    scene sara_room_evening_scene3_v1_p9
    Console "FATALITY! PLAYER 2 WINS AGAIN!"
    Sara "NOOOOOOO!"
    MC "Yesss!"
    Sara "N-No way! This c-can’t be happening!"
    MC "You know the rules, Sara! Time to lose those denim shorts!"
    MC "Or… you could just lose your shoes."

    scene sara_room_evening_scene3_v1_p10
    MC "Actually! Let’s make a deal - one more round. Sudden death rules."
    Sara "What do you mean?"
    MC "If you win, I take off EVERYTHING. If I win though… then you have to strip completely naked for me."
    MC "Deal?"
    Sara "… Deal."

    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    "(Thirty seconds later…)"
    $ renpy.pause(2.0)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    scene sara_room_evening_scene3_v1_p11
    Sara "AAAAAAHHHHHHH!!!"
    Sara "(WHAT’S HAPPENING?! Why aren’t I good at video games anymore?!)"
    MC "You lost the deal, Sara. Time to strip off!"

    scene sara_room_evening_scene3_v1_p12
    Sara "Ugh… Fine. I’ll do it on the bed."
    Sara "N-No photos though!"
    MC "That’s a bit hypocritical of you!"
    Sara "I… I don’t have that picture anymore. I… um… deleted it!"
    MC "(She’s lying… She definitely still has that picture of my dick!)"

    scene sara_room_evening_scene3_v1_p13
    MC "Fine, no photos. But I still want to see your whole body."
    Sara "(Gulp) S-Sure."
    Sara "(I can’t believe I lost… I thought this would just be an easy way to see [player_name]’s cock again.)"
    Sara "(God… what am I going to tell Lily if she asks what happend?!)"

    scene sara_room_evening_scene3_v1_p14
    MC "(Wow! There’s her pussy! I can see the hood of her clitoris, poking out the top.)"
    MC "(She wasn’t lying when she said she wasn’t wearing any panties. Was she seriously THAT confident that she was going to win?! Haha!)"
    Sara "W-Well? I-Is this enough?"

    scene sara_room_evening_scene3_v1_p15
    MC "We did agree, completely naked - but this is a rather sexy view."
    Sara "S-Sexy?"
    MC "I’m just teasing you."

    scene sara_room_evening_scene3_v1_p16
    Sara "W-Wait - You can’t just s-say something like that and walk away…"
    MC "Huh?"
    Sara "D… Do… you think I’m pretty?"

    scene sara_room_evening_scene3_v1_p17
    MC "Of course you’re pretty. I’d hardly be playing strip challenge games with you if you weren’t!"
    Sara "I… I guess…"
    MC "Anyway, I’ll let you get dressed again. See you later, Sara."
    MC "And for the record, you are very pretty."
    Sara "Th… Thank you..."
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label

