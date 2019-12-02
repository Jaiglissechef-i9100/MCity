image Ne_MS1_p1 = "images/Ne_1/MS1/1.jpg"
image Ne_MS1_p2 = "images/Ne_1/MS1/2.jpg"
image Ne_MS1_p3 = "images/Ne_1/MS1/3.jpg"
image Ne_MS1_p4 = "images/Ne_1/MS1/4.jpg"
image Ne_MS1_p6 = "images/Ne_1/MS1/6.jpg"
image Ne_MS1_p7 = "images/Ne_1/MS1/7.jpg"

image Ne_MS1a_p1 = "images/Ne_1/MS1/2/1.jpg"
image Ne_MS1a_p2 = "images/Ne_1/MS1/2/2.jpg"
image Ne_MS1a_p3 = "images/Ne_1/MS1/2/3.jpg"
image Ne_MS1a_p4 = "images/Ne_1/MS1/2/4.jpg"
image Ne_MS1a_p5 = "images/Ne_1/MS1/2/5.jpg"
image Ne_MS1a_p6 = "images/Ne_1/MS1/2/6.jpg"
image Ne_MS1a_p7 = "images/Ne_1/MS1/2/7.jpg"
image Ne_MS1a_p8 = "images/Ne_1/MS1/2/8.jpg"
image Ne_MS1a_p9 = "images/Ne_1/MS1/2/9.jpg"

label Ne_MS1_lab:
    hide screen map_button
    if Ne_MS1 == 2:

        $ clickable = False
        show screen Ne_entrance_M_scr
        MC "I should try tomorrow."
        hide screen Ne_entrance_M_scr
        $ clickable = True
        jump Ne_entrance_M1

    if Ne_MS1 == 5:

        $ clickable = False
        show screen Ne_entrance_M_scr
        MC "I should try tomorrow."
        hide screen Ne_entrance_M_scr
        $ clickable = True
        jump Ne_entrance_M1

    if Ne_MS1 == 4:

        $ clickable = False
        show screen Ne_entrance_M_scr
        MC "I have to talk with that younger girl. Maybe I should look for her at school."
        hide screen Ne_entrance_M_scr
        $ clickable = True
        jump Ne_entrance_M1

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)



    if Ne_MS1 == 1:

        $ clickable = False
        show screen Ne_entrance_M_scr

        MC "(Let’s go and meet these neighbours!)"
        "*Ding Dong*"

        $ clickable = True
        hide screen Ne_entrance_M_scr
        $ Sidra_name = "???"
        $ can_hide_windows = True

        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        scene Ne_MS1_p1 with dissolve
        Sidra "Good morning, can I help you?"
        MC "Uh, yeah. I know we had new neighbours move in a while ago. I thought I’d just drop over to say hi!"

        scene Ne_MS1_p2
        Sidra "…"
        MC "So, hi?"
        MC "(Yikes, tough crowd. I never realised the woman would be THIS awkward!)"

        scene Ne_MS1_p3
        Sidra "Hmm. Thank you for dropping by to introduce yourself, but I’m afraid I prefer my privacy."
        MC "Sorry, I didn’t introduce myself properly, my name is [player_name]."
        Sidra "I honestly do not care."

        scene Ne_MS1_p4
        MC "I… uh…"
        MC "(Geez, this woman hasn’t got a stick up her ass - she’s got an entire fucking tree up there!)"
        Sidra "You’re still here."

        scene Ne_MS1_p6
        Sidra "Please vacate my home."
        MC "But, I was-"
        Sidra "I do not know you. I do not wish to know you. And unless you are someone who can help me, like the manager of the local supermarket, then I do not wish to speak with you."
        scene Ne_MS1_p7
        MC "(Fuck me…)"
        MC "Fine, I was just trying to be nice though!"
        Sidra "(I know EXACTLY what men like you want.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ Ne_MS1 = 2
        $ Ne_MS2 = 2
        jump Ne_entrance_M1

    if Ne_MS1 == 3:
        $ clickable = False
        show screen Ne_entrance_M_scr

        MC "(Maybe she was just having a bad day. I’ve got to have more luck this time, right?)"
        "*Ding Dong*"

        $ clickable = True
        hide screen Ne_entrance_M_scr
        $ can_hide_windows = True

        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        scene Ne_MS1_p1
        MC "Hey there!"
        Sidra "Oh, it is you again. Do you require something?"

        scene Ne_MS1_p2
        MC "No, I don’t need anything."
        MC "I just wanted to come back seeing as we got off on the wrong foot last time. Maybe there was a bit of a misunderstanding"

        scene Ne_MS1_p3
        Sidra "Au contraire, things went exactly how I intended them to."
        MC "(Yikes… This isn’t going any better than last time I came over!)"

        scene Ne_MS1_p4
        MC "(What the hell is this woman’s problem?!)"
        MC "B-But I was just being polite…"

        scene Ne_MS1_p6
        Sidra "Thank you. Now if you could politely turn around and leave it would be most appreciated."
        MC "*Sigh*"

        scene Ne_MS1_p7
        Sidra "Please do not return. This is now two minutes of my life you have wasted."
        MC "(This woman is cold as ice! There’s no getting past her!)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ Ne_MS1 = 4
        jump Ne_entrance_M1

    if Ne_MS1 == 6:
        $ clickable = False
        show screen Ne_entrance_M_scr
        hide screen map_button
        MC "(I wonder if Isla is home right now. Perhaps that woman won’t be so stuck up if I say I’m there to visit Isla.)"
        "*Ding Dong*"

        $ clickable = True
        hide screen Ne_entrance_M_scr
        $ can_hide_windows = True

        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        scene Ne_MS1a_p1 with dissolve
        Sidra "What on Earth are you doing back here? Do I have to contact my lawyer for a restraining order?"
        MC "H-Hey! Calm down, I’m just here to see Isla."
        scene Ne_MS1a_p2
        Sidra "Isla?"
        MC "Yeah."
        Sidra "You’re here to see Isla?"
        scene Ne_MS1a_p3
        MC "Yeah, we met at school and I was wondering if she was home."
        Sidra "Let me tell you something. [player_name], wasn’t it?"
        MC "Y-Yeah, [player_name]."
        scene Ne_MS1a_p4
        Sidra "Well, [player_name]..."
        Sidra "Let me tell you something about Isla."
        MC "*Gulp*"
        scene Ne_MS1a_p5

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music2", loop=True, fadein = 2)

        Sidra "That girl is mine. She belongs to me!"
        MC "(What the everliving fuck?!)"
        Sidra "I am NOT having some boy from her school jumped up on hormones trying to work his way into her panties!"
        scene Ne_MS1a_p6
        MC "C-Calm down! I’m not-"
        Sidra "Listen to me, boy!"
        Sidra "I have protected her for eighteen years from guys like you. Guys who want to take her precious virginity!"
        MC "(She’s a fucking psycho!)"
        scene Ne_MS1a_p7
        Sidra "Oh yes, I know there’s only one thing on the minds of men like you. You want to screw her!"
        Sidra "You’ll screw her, you’ll get her pregnant, and then you’ll leave her!"
        Sidra "But I won’t let you! "
        scene Ne_MS1a_p8
        MC "I don’t even know who you are!"
        Sidra "My name is Sidra! That’s all you need to know!"
        $ Sidra_name = "Sidra"
        Sidra "Now, get the hell out of my house, and stay the heck away from Isla. Is that clear?"
        scene Ne_MS1a_p9
        MC "(It’s clear that you’re absolutely and utterly insane!)"
        MC "Yeah, sure…"
        Sidra "Now go. Out!"
        MC "(It's pointless trying to talk with her.)"
        MC "(Maybe I should check somehow what's going on in their house in the evening or night?)"

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ Ne_MS1 = False
        $ Ne_ES1 = True
        $ Ne_NV = True
        $ Ne_fence = True
        jump Ne_entrance_M1