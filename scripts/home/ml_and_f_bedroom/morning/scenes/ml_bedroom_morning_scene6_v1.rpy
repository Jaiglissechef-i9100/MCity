image ml_bedroom_morning_scene6_v1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/1.jpg"
image ml_bedroom_morning_scene6_v1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/2.jpg"
image ml_bedroom_morning_scene6_v1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/3.jpg"
image ml_bedroom_morning_scene6_v1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/4.jpg"
image ml_bedroom_morning_scene6_v1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/5.jpg"
image ml_bedroom_morning_scene6_v1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/6.jpg"
image ml_bedroom_morning_scene6_v1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/7.jpg"
image ml_bedroom_morning_scene6_v1_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/8.jpg"
image ml_bedroom_morning_scene6_v1_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/9.jpg"
image ml_bedroom_morning_scene6_v1_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/10.jpg"
image ml_bedroom_morning_scene6_v1_p11 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/11.jpg"
image ml_bedroom_morning_scene6_v1_p12 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/12.jpg"
image ml_bedroom_morning_scene6_v1_p13 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/13.jpg"
image ml_bedroom_morning_scene6_v1_p13a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/13a.jpg"
image ml_bedroom_morning_scene6_v1_p14 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/14.jpg"
image ml_bedroom_morning_scene6_v1_p15 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/15.jpg"
image ml_bedroom_morning_scene6_v1_p16 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/16.jpg"
image ml_bedroom_morning_scene6_v1_p16a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/16a.jpg"
image ml_bedroom_morning_scene6_v1_p17 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/17.jpg"
image ml_bedroom_morning_scene6_v1_p18 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/18.jpg"
image ml_bedroom_morning_scene6_v1_p19a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19a.jpg"
image ml_bedroom_morning_scene6_v1_p19b = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19b.jpg"
image ml_bedroom_morning_scene6_v1_p19c = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19c.jpg"
image ml_bedroom_morning_scene6_v1_p20 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/20.jpg"
image ml_bedroom_morning_scene6_v1_p21 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/21.jpg"
image ml_bedroom_morning_scene6_v1_p22 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/22.jpg"
image ml_bedroom_morning_scene6_v1_p23 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/23.jpg"
image ml_bedroom_morning_scene6_v1_p24 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/24.jpg"
image ml_bedroom_morning_scene6_v1_p25 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/25.jpg"
image ml_bedroom_morning_scene6_v1_p26 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/26.jpg"

image ml_bedroom_morning_scene6_v1_p11anim = Movie(play="videos/Linda-MorningS6-1.webm", loop = True )

label ml_bedroom_morning_scene6_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_bedroom_morning_scene6_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Hey, Mom. I’m here to talk to you about… the thing from yesterday."
    if not renpy.loadable("patch.rpy"):
        MC "Hey, Linda. I’m here to talk to you about… the thing from yesterday."
    Mom "(Gulp) Y-Yes?"
    MC "Is now a good time for you? Or do you want me to come back later?"
    Mom "I… I’m going to work soon, but I have a few minutes."

    scene ml_bedroom_morning_scene6_v1_p2
    menu:
        "I love you too.":
            if renpy.loadable("patch.rpy"):
                MC "Mom, I… I love you too."
                MC "And not just in the way a son normally loves his Mom. I mean, I really love you."
            if not renpy.loadable("patch.rpy"):
                MC "Linda, I… I love you too."
                MC "And not just in the normal way. I mean, I really love you."
            jump ml_bedroom_morning_scene6_v1_label_after_ch
        "I think I want the… same thing.":


            MC "After, all you said yesterday, and the way you’ve acted around me… I think…"
            MC "I think I want the same thing that you do."
            jump ml_bedroom_morning_scene6_v1_label_after_ch
        "You should have told me sooner.":

            if renpy.loadable("patch.rpy"):
                MC "Mom… You really should have told me sooner."
            if not renpy.loadable("patch.rpy"):
                MC "Linda… You really should have told me sooner."
            MC "You said that you’ve always felt this way. If I’d known, then I would have been able to understand, why you were acting the way you were."
            MC "Everything would have made sense."
            jump ml_bedroom_morning_scene6_v1_label_after_ch

label ml_bedroom_morning_scene6_v1_label_after_ch:

    scene ml_bedroom_morning_scene6_v1_p3
    if renpy.loadable("patch.rpy"):
        MC "Anyway, I should go now. But… I really do love you, Mom. "
    if not renpy.loadable("patch.rpy"):
        MC "Anyway, I should go now. But… I really do love you, Linda. "
    MC "And I might be interested in… doing some of the… um…. stuff… that..."
    MC "Sorry, I’m getting all nervous and stumbling over my words. I should just go."

    scene ml_bedroom_morning_scene6_v1_p4
    Mom "Don’t go! Please!"
    MC "Wow!"
    Mom "S-Sorry, I didn’t mean to frighten you."
    if renpy.loadable("patch.rpy"):
        Mom "I was… just, so sure that you were going to tell me, that you only loved me like a mother."
    if not renpy.loadable("patch.rpy"):
        Mom "I was… just, so sure that you were going to tell me, that you only loved me like a friend."
    Mom "I was scared that I might have pushed you away, with those silly games I made you play."
    Mom "I know everything’s moving quite fast… but if you want, we could be intimate together, in our underwear. How does that sound?"
    MC "R-Really?"
    Mom "Sit down on the sofa at the end of my bed."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene ml_bedroom_morning_scene6_v1_p5
    Mom "I want you to see this."
    Mom "I want you to look at my body and enjoy watching it."
    Mom "This is just for you."

    scene ml_bedroom_morning_scene6_v1_p6
    Mom "Well? What do you think?"
    Mom "(I hope he likes my body… I know I’m not THAT young anymore…)"
    if renpy.loadable("patch.rpy"):
        MC "Wow… You’re stunning, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "Wow… You’re stunning, Linda."

    scene ml_bedroom_morning_scene6_v1_p7
    Mom "You really think so?"
    MC "Yeah - your body is incredible! And that lingerie you’re wearing, fits you perfectly!"
    Mom "I’m glad you like it."

    scene ml_bedroom_morning_scene6_v1_p8
    Mom "How about you strip off now too?"
    Mom "I’ve shown you what I’ve got - it’s only fair that you show me yours."
    MC "Okay, hang on…"

    scene ml_bedroom_morning_scene6_v1_p9
    MC "Well? Is it as good as you imagined?"
    Mom "Mmm… Almost. The part I spent, most time fantasising about, is still covered up right now."

    scene ml_bedroom_morning_scene6_v1_p10
    Mom "It’s going to feel so good, to finally kiss you without feeling like a creep."
    MC "You did have me wondering what was going on, for a few days there."
    Mom "Hehe... I’m sorry. I just couldn’t resist you."

    scene ml_bedroom_morning_scene6_v1_p11
    MC "Mmm…"
    Mom "(How can something so wrong, feel so right?)"
    scene ml_bedroom_morning_scene6_v1_p11anim with dissolve
    Mom "(It’s like… my dreams are finally beginning to come true.)"
    Mom "(Whenever I kiss [player_name], there’s butterflies in my tummy… I’ve never felt this way, when I’ve kissed anyone else, in my life.)"

    scene ml_bedroom_morning_scene6_v1_p12
    Mom "Lie down on the bed. Just like that."
    Mom "(I can see how hard he already is… but I have to feel it with my own hand.)"

    scene ml_bedroom_morning_scene6_v1_p13
    Mom "Do you mind if I… touch you with my hand?"
    MC "S-Sure… I don’t mind."

    scene ml_bedroom_morning_scene6_v1_p13a
    Mom "(Wow… He’s huge…)"
    Mom "(If only he wasn’t wearing these boxer shorts…)"
    Mom "(I’d love to take his cock in my mouth right now, and suck on it until he came.)"

    scene ml_bedroom_morning_scene6_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Ahh… M-Mom..."
    if not renpy.loadable("patch.rpy"):
        MC "Ahh… L-Linda..."
    MC "(She’s being so gentle with her tongue…)"

    scene ml_bedroom_morning_scene6_v1_p15
    MC "Ah! Ahh..."
    Mom "(It sounds like his nipples are especially sensitive.)"
    Mom "(He’s clearly enjoying me flicking my tongue over them.)"

    scene ml_bedroom_morning_scene6_v1_p16
    if renpy.loadable("patch.rpy"):
        MC "(I’m so hard right now… I can’t believe, Mom was this attracted to me for so long.)"
    if not renpy.loadable("patch.rpy"):
        MC "(I’m so hard right now… I can’t believe, Linda was this attracted to me for so long.)"
    MC "(I wonder if this was one of the fantasies she had, about me and her?)"

    scene ml_bedroom_morning_scene6_v1_p16a
    if renpy.loadable("patch.rpy"):
        MC "Ooh... Oh, Mom!"
    if not renpy.loadable("patch.rpy"):
        MC "Ooh... Oh, Linda!"
    Mom "Do you like it when I kiss your neck like this?"
    MC "Yes…"

    scene ml_bedroom_morning_scene6_v1_p17
    Mom "You can do whatever you want now. I’ve had my fun - it’s time for you to have some too."
    MC "What do you mean?"
    Mom "I’ll lie back, on the bed. The rest is up to you."

    scene ml_bedroom_morning_scene6_v1_p18
    menu:
        "Give Mom a foot massage to begin." if renpy.loadable("patch.rpy"):

            scene ml_bedroom_morning_scene6_v1_p19a
            MC "You’ve got beautiful feet."
            Mom "Hehe... Thanks. Have you got a bit of a foot fetish, then?"
            MC "W-What?!"

            scene ml_bedroom_morning_scene6_v1_p19b
            Mom "Relax - I’m just teasing you."
            Mom "Mmm… It’s nice when you massage them like that."
            MC "You like that? I’ll do the soles too, then."

            scene ml_bedroom_morning_scene6_v1_p19c
            Mom "Ahh… Your father never does ANYTHING like this, for me."
            Mom "God… your fingers are amazing."
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

        "Give Linda a foot massage to begin." if not renpy.loadable("patch.rpy"):

            scene ml_bedroom_morning_scene6_v1_p19a
            MC "You’ve got beautiful feet."
            Mom "Hehe... Thanks. Have you got a bit of a foot fetish, then?"
            MC "W-What?!"

            scene ml_bedroom_morning_scene6_v1_p19b
            Mom "Relax - I’m just teasing you."
            Mom "Mmm… It’s nice when you massage them like that."
            MC "You like that? I’ll do the soles too, then."

            scene ml_bedroom_morning_scene6_v1_p19c
            Mom "Ahh… Bob never does ANYTHING like this, for me."
            Mom "God… your fingers are amazing."
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

        "Start with Mom’s hips, and work up her body." if renpy.loadable("patch.rpy"):
            jump ml_bedroom_morning_scene6_v1_label_after_ch2
        "Start with Linda’s Hips, and work up her body." if not renpy.loadable("patch.rpy"):
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

label ml_bedroom_morning_scene6_v1_label_after_ch2:
    scene ml_bedroom_morning_scene6_v1_p20
    if renpy.loadable("patch.rpy"):
        MC "Can you spread your legs a little more, Mom?"
    if not renpy.loadable("patch.rpy"):
        MC "Can you spread your legs a little more, Linda?"
    Mom "Of course. Like this?"
    MC "Perfect."

    scene ml_bedroom_morning_scene6_v1_p21
    Mom "Ooh..."
    Mom "(His fingers are so close to my pussy… I wish he’d go a little bit closer, and just slip them inside me.)"
    MC "Your skin’s so soft."

    scene ml_bedroom_morning_scene6_v1_p22
    Mom "The trick is, an exfoliating scrub and moisturiser, twice a day."
    MC "Are you okay if I touch your breasts?"
    Mom "Please, go ahead."

    scene ml_bedroom_morning_scene6_v1_p23
    MC "Wow…"
    Mom "You can give them a squeeze, if you want."
    Mom "Just don’t be too rough, okay?"

    scene ml_bedroom_morning_scene6_v1_p24
    Mom "Ahh…"
    MC "(This is freaking awesome!)"
    MC "(I hope I get to play with them, without the bra, soon!)"

    scene ml_bedroom_morning_scene6_v1_p25
    Mom "If we weren’t wearing our underwear, I would just pull you inside me, right now."
    Mom "Mmm... I’d love to feel your cock, thrusting, deep into my wet pussy."

    scene ml_bedroom_morning_scene6_v1_p26
    Mom "I can already feel your hard cock, pressing against my black panties."
    Mom "Sadly, I have to go. If I spend, another minute in bed, I’ll be late for work."
    Mom "I’ll see you tonight, Sweetie."
    if renpy.loadable("patch.rpy"):
        MC "I love you, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "I love you, Linda."
    Mom "I love you too."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_morning_scene6 = False
    $ day_time +=1
    $ ml_work_day_scene2 = True
    $ can_ml_work_day_scene2 = False
    $ can_sms2_from_ml = True
    $ can_hide_windows = False
    jump parents_bedroom_morning1