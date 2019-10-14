image ml_work_day_scene1_v1_p1 = "/images/ml_work/room1/scenes/1.jpg"
image ml_work_day_scene1_v1_p2 = "/images/ml_work/room1/scenes/2.jpg"
image ml_work_day_scene1_v1_p3 = "/images/ml_work/room1/scenes/3.jpg"
image ml_work_day_scene1_v1_p4 = "/images/ml_work/room1/scenes/4.jpg"
image ml_work_day_scene1_v1_p5 = "/images/ml_work/room1/scenes/5.jpg"
image ml_work_day_scene1_v1_p6 = "/images/ml_work/room1/scenes/6.jpg"
image ml_work_day_scene1_v1_p7 = "/images/ml_work/room1/scenes/7.jpg"
image ml_work_day_scene1_v1_p8 = "/images/ml_work/room1/scenes/8.jpg"
image ml_work_day_scene1_v1_p9 = "/images/ml_work/room1/scenes/9.jpg"
image ml_work_day_scene1_v1_p10 = "/images/ml_work/room1/scenes/10.jpg"
image ml_work_day_scene1_v1_p11 = "/images/ml_work/room1/scenes/11.jpg"
image ml_work_day_scene1_v1_p12 = "/images/ml_work/room1/scenes/12.jpg"
image ml_work_day_scene1_v1_p13 = "/images/ml_work/room1/scenes/13.jpg"
image ml_work_day_scene1_v1_p14 = "/images/ml_work/room1/scenes/14.jpg"
image ml_work_day_scene1_v1_p15 = "/images/ml_work/room1/scenes/15.jpg"

label ml_work_day_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_work_day_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Hey, Mom! I’m free to do some work for you now."
    if not renpy.loadable("patch.rpy"):
        MC "Hey, Linda! I’m free to do some work for you now."
    Mom "Good afternoon, Sweetie. Great! Let me see what I need done."
    Mom "Hmm…"

    scene ml_work_day_scene1_v1_p2
    Mom "We’re on top of paperwork and databasing right now."
    Mom "However, we lost our cleaner last week. She badly twisted her ankle, and will be off work for a couple of months."
    Mom "I’ll tell you what - if you can clean the offices for me, I’ll give you $25."
    MC "What do I need to do?"
    Mom "Take out the trash, pick up any rubbish, tidy up loose papers."
    Mom "Just make sure you don’t throw away anything important!"
    if renpy.loadable("patch.rpy"):
        MC "Okay, Mom. I’ll be careful!"
    if not renpy.loadable("patch.rpy"):
        MC "Okay, Linda. I’ll be careful!"

    $ renpy.music.stop(channel="music1", fadeout=1)

    if persistent.skip_mg == True:
        jump ml_work_day_scene1_v1_label_after_minigame

    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_room1_label

label ml_work_day_scene1_v1_label_after_minigame:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    MC "Phew! (That looks like the last of it.)"
    if renpy.loadable("patch.rpy"):
        MC "(Mom’s offices are looking, in pretty good shape right now!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Linda’s offices are looking, in pretty good shape right now!)"
    MC "(I’ll go and let her know I’m finished.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene1_v1_p3 with dissolve
    MC "Hi again! That’s me done."
    Mom "Great work! Here’s the $25, as promised."
    $ inventory.earn(25)
    if renpy.loadable("patch.rpy"):
        MC "(It’s not much, but it's better than having to constantly beg Dad!)"
    if not renpy.loadable("patch.rpy"):
        MC "(It’s not much, but it's better than having to constantly beg Bob!)"

    scene ml_work_day_scene1_v1_p4
    Mom "(The cleaner was getting $40 for the work [player_name] just did - but now that I’ve got his attention, I can reel him in with the big money!)"
    Mom "Say - how would you like to earn another $50?"
    MC "(Another $50? That’ll bring me up to $75. I could really use the cash.)"
    MC "Yeah, what do you want me to do?"
    Mom "I want… to play the game again."
    MC "The game?"
    Mom "The one we played in the car - but this time you must stay still for two minutes."
    MC "(Gulp.)"

    scene ml_work_day_scene1_v1_p1
    $ ml_work_day_scene1_v1_q1 = True
    $ ml_work_day_scene1_v1_q2 = True
    $ ml_work_day_scene1_v1_q3 = True
    jump ml_work_day_scene1_v1_menu

label ml_work_day_scene1_v1_menu:
    scene ml_work_day_scene1_v1_p1
    Mom "Well? What do you say?"
    menu:

        "Do you… love me more than a son?" if ml_work_day_scene1_v1_q1 == True and renpy.loadable("patch.rpy"):
            MC "Before I say “yes”, I want to know… do you love me more than a son?"
            Mom "I don’t know what you mean."
            scene ml_work_day_scene1_v1_p2
            MC "I mean, do you- are you attracted to me?"
            Mom "Oh, come on. You’re being silly now, [player_name]."
            $ ml_work_day_scene1_v1_q1 = False
            jump ml_work_day_scene1_v1_menu

        "Do you… love me?" if ml_work_day_scene1_v1_q1 == True and not renpy.loadable("patch.rpy"):
            MC "Before I say “yes”, I want to know… do you love?"
            Mom "I don’t know what you mean."
            scene ml_work_day_scene1_v1_p2
            MC "I mean, do you- are you attracted to me?"
            Mom "Oh, come on. You’re being silly now, [player_name]."
            $ ml_work_day_scene1_v1_q1 = False
            jump ml_work_day_scene1_v1_menu

        "Why do you want to play this game again?" if ml_work_day_scene1_v1_q2 == True:
            MC "Why do you want to play this weird game again?"
            Mom "Why does it matter to you? It’s an easy $50 if you agree."
            MC "(Hmm... She’s being evasive with her answers.)"
            $ ml_work_day_scene1_v1_q2 = False
            jump ml_work_day_scene1_v1_menu

        "Are you going to kiss me again?" if ml_work_day_scene1_v1_q3 == True:
            MC "If I stand still, are you going to try and kiss me again?"
            scene ml_work_day_scene1_v1_p4
            Mom "Who knows what will happen?"
            Mom "And why do you care? It’s not like I haven’t kissed you before."
            $ ml_work_day_scene1_v1_q3 = False
            jump ml_work_day_scene1_v1_menu
        "{color=#00ff00}Okay, I’m ready.{/color}":
            jump ml_work_day_scene1_v1_menu_after

label ml_work_day_scene1_v1_menu_after:
    scene ml_work_day_scene1_v1_p4
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    MC "Okay, I’m ready."
    Mom "Don’t move a muscle. The two minutes begins now."

    scene ml_work_day_scene1_v1_p5
    MC "(One… Two… Three…)"
    MC "(Oh, my God! Is she lifting up my t-shirt?!)"
    Mom "(My heart’s racing. I wonder how far I can get in two minutes.)"
    Mom "(Will I have enough time to see his hard dick?)"

    scene ml_work_day_scene1_v1_p6
    Mom "Ah ah - no moving!! We’ve only just started, Sweetie."
    MC "I… ah…"
    Mom "No talking either. Your tongue counts as a muscle too, you know!"

    scene ml_work_day_scene1_v1_p7
    if renpy.loadable("patch.rpy"):
        MC "(Sh-Shit! She’s my mother!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Sh-Shit! She’s my friend!)"
    MC "(I mean… I’m definitely getting hard right now… but it’s wrong. Isn’t it?)"
    MC "C-Careful! I’m falling back!"

    scene ml_work_day_scene1_v1_p8
    MC "Whoooaaaa!"
    Mom "(Oooh! Exciting!)"
    if renpy.loadable("patch.rpy"):
        MC "(Jesus! Mom’s completely lost control of herself!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Jesus! Linda’s completely lost control of herself!)"

    scene ml_work_day_scene1_v1_p9
    Mom "(Mmm! I like this position!)"
    if renpy.loadable("patch.rpy"):
        MC "M-Mom! Wait!"
    if not renpy.loadable("patch.rpy"):
        MC "L-Linda! Wait!"
    Mom "(Huh? What’s gotten into him? He’s resisting, a lot, this time.)"

    scene ml_work_day_scene1_v1_p10
    Mom "What’s wrong, Sweetie?"
    Mom "Do you want me to continue or not?"
    menu:
        "Yes.":
            scene ml_work_day_scene1_v1_p10

            MC "Y-Yeah… I do."
            MC "I’m just a little stunned at-"
            jump ml_work_day_scene1_v1_menu_after2
        "No.":

            MC "I don’t know…"
            MC "It’s a bit too… intense…."
            jump ml_work_day_scene1_v1_menu_after2

label ml_work_day_scene1_v1_menu_after2:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene1_v1_p11
    Mom "(Oh, God… What am I doing?)"
    if renpy.loadable("patch.rpy"):
        Mom "(I can’t believe I’ve sunk this low. What kind of mother tries to rape her own son?!)"
    if not renpy.loadable("patch.rpy"):
        Mom "(I can’t believe I’ve sunk this low... To even try to rape him?!)"
    Mom "I… I’m so sorry."
    if renpy.loadable("patch.rpy"):
        MC "Mom, I-"
    if not renpy.loadable("patch.rpy"):
        MC "Linda, I-"

    scene ml_work_day_scene1_v1_p12
    Mom "I’m so so sorry, [player_name]."
    if renpy.loadable("patch.rpy"):
        MC "It’s okay, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "It’s okay, Linda."
    Mom "No, it’s not okay."
    Mom "I’ve always felt this way."

    scene ml_work_day_scene1_v1_p13
    Mom "I’ve been able to contain my emotions for so long."
    Mom "I kept it all inside - and sometimes, I allowed myself to fantasise about being with you."
    Mom "But I always felt SO guilty afterwards."
    Mom "It was when you started wanting to date other women, that I finally cracked."
    Mom "I… (sniff) I couldn’t stand the thought of you being romantically involved with someone else."

    scene ml_work_day_scene1_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Shush - it’s okay, Mom. Breathe and relax."
    if not renpy.loadable("patch.rpy"):
        MC "Shush - it’s okay Linda. Breathe and relax."
    MC "You know that I lov-"

    scene ml_work_day_scene1_v1_p15
    Mom "No. No."
    Mom "I don’t want to hear it right now."
    Mom "I’m feeling like a compelte piece of shit, after what I did to you today."
    Mom "Just… think about everything I told you and… let me know tomorrow morning. Okay?"
    if renpy.loadable("patch.rpy"):
        MC "O-Okay, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "O-Okay, Linda."
    $ inventory.earn(50)
    $ day_time += 1
    $ ml_work_day_scene1 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_morning_scene6 = True
    $ can_hide_windows = False
    jump map_label
