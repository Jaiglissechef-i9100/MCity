image MLR2_ES1_p1 = "images/home/kitchen/evening/scenes/MLR2_ES1/1.jpg"
image MLR2_ES1_p2a = "images/home/kitchen/evening/scenes/MLR2_ES1/2a.jpg"
image MLR2_ES1_p2aa = "images/home/kitchen/evening/scenes/MLR2_ES1/2aa.jpg"
image MLR2_ES1_p2aaa = "images/home/kitchen/evening/scenes/MLR2_ES1/2aaa.jpg"
image MLR2_ES1_p2b = "images/home/kitchen/evening/scenes/MLR2_ES1/2b.jpg"
image MLR2_ES1_p2bb = "images/home/kitchen/evening/scenes/MLR2_ES1/2bb.jpg"
image MLR2_ES1_p2bbb = "images/home/kitchen/evening/scenes/MLR2_ES1/2bbb.jpg"
image MLR2_ES1_p3 = "images/home/kitchen/evening/scenes/MLR2_ES1/3.jpg"
image MLR2_ES1_p4 = "images/home/kitchen/evening/scenes/MLR2_ES1/4.jpg"
image MLR2_ES1_p5 = "images/home/kitchen/evening/scenes/MLR2_ES1/5.jpg"
image MLR2_ES1_p6 = "images/home/kitchen/evening/scenes/MLR2_ES1/6.jpg"
image MLR2_ES1_p7 = "images/home/kitchen/evening/scenes/MLR2_ES1/7.jpg"
image MLR2_ES1_p8 = "images/home/kitchen/evening/scenes/MLR2_ES1/8.jpg"
image MLR2_ES1_p9 = "images/home/kitchen/evening/scenes/MLR2_ES1/9.jpg"

label MLR2_ES1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene MLR2_ES1_p1 with dissolve
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        MC "(Looks like Mom’s doing some cleaning. She probably hasn’t noticed I’m in the kitchen yet.)"
    else:
        MC "(Looks like Linda’s doing some cleaning. She probably hasn’t noticed I’m in the kitchen yet.)"
    MC "(Hmm… This could be my chance to prove how confident and forward I can be with her.)"
    MC "(Should I maybe grab her ass? Maybe that’s too much.)"
    MC "(I suppose I could just hold her waist?)"

    window hide
    menu:
        "Grab Mom’s ass." if persistent.incest_patch == True:
            jump MLR2_ES1_grab_ass

        "Grab Linda’s ass." if persistent.incest_patch == False:
            jump MLR2_ES1_grab_ass

        "Wrap your hands around Mom’s waist." if persistent.incest_patch == True:
            jump MLR2_ES1_waist
        "Wrap your hands around Linda’s waist." if persistent.incest_patch == False:
            jump MLR2_ES1_waist

label MLR2_ES1_grab_ass:
    scene MLR2_ES1_p2a

    MC "(Well… here goes nothing! Hopefully she’ll enjoy, me grabbing her ass!)"
    MC "(Firm, as always! She’s got a great butt!)"
    MC "(Hmm… she doesn’t seem to be reacting…)"

    scene MLR2_ES1_p2aa

    Mom "Not NOW. I’m NOT in the mood for this."
    Mom "Besides, I told you earlier how busy I am!"
    Mom "Don’t you have work you should be getting on with?"
    MC "Uh- S-Sorry! My bad!"

    scene MLR2_ES1_p2aaa

    Mom "Huh?! Oh shit!"
    if persistent.incest_patch == True:
        Mom "Sorry, I thought that was your father!"
        MC "Sorry, Mom. I-"
    else:
        Mom "Sorry, I thought you were Bob!"
        MC "Sorry, Linda. I-"
    Mom "No, don’t apologise! You didn’t do anything wrong!"
    Mom "Sorry. That bastard is just, ALWAYS looking for sex when he hasn’t even finished the housework I gave him to do!"
    jump after_menu_MLR2_ES1_label

label MLR2_ES1_waist:
    scene MLR2_ES1_p2b

    MC "(I think I’ll wrap my hands around her waist instead. It’s a little more romantic than just randomly grabbing her ass, out of the blue!)"
    MC "(Let’s see how this goes…)"

    scene MLR2_ES1_p2bb

    Mom "Not NOW. I’m NOT in the mood for this."
    Mom "Besides, I told you earlier how busy I am!"
    Mom "Don’t you have work you should be getting on with?"
    MC "Uh- S-Sorry! My bad!"

    scene MLR2_ES1_p2bbb

    Mom "Huh?! Oh shit!"
    if persistent.incest_patch == True:
        Mom "Sorry, I thought that was your father!"
        MC "Sorry, Mom. I-"
    else:
        Mom "Sorry, I thought you were Bob!"
        MC "Sorry Linda. I-"
    Mom "No, don’t apologise! You didn’t do anything wrong!"
    Mom "Sorry, that bastard is just ALWAYS looking for sex when he hasn’t even finished the housework I gave him to do!"
    jump after_menu_MLR2_ES1_label

label after_menu_MLR2_ES1_label:
    scene MLR2_ES1_p3

    Mom "Listen, I’m really really sorry, [player_name]."
    Mom "Can we just continue where we left off before I shouted?"
    MC "Uh… sure."

    scene MLR2_ES1_p4

    Mom "Now, if I remember, I was bent over like, this here."
    Mom "Go ahead and play with my ass. You’re allowed to."
    if persistent.incest_patch == True:
        MC "Thanks, Mom!"
    else:
        MC "Thanks, Linda!"
    MC "(Wow, she’s got a great ass!)"

    scene MLR2_ES1_p5

    Mom "Mmm… That’s it. You can squeeze a little harder if you like."
    MC "(Damn, she looks great in these tight jeans!)"

    scene MLR2_ES1_p6

    Mom "Ahh… You’re enjoying that, aren’t you, [player_name]?"
    MC "Of course! Haha!"
    Mom "Well, if you’re enjoying it that much, then maybe we should set down some rules."

    scene MLR2_ES1_p7

    MC "Rules? Like what?"
    Mom "Let me think… Hmm…"
    Mom "Well, you clearly enjoy touching my body. So, how about we make a deal?"

    scene MLR2_ES1_p8

    MC "A deal?"
    Mom "You can touch my body as much as you like and WHENEVER you want."
    MC "I like the sound of that A LOT!"

    scene MLR2_ES1_p9

    Mom "And in return, I get to touch you whenever I want, for as long as I want to."
    Mom "Does that sound like a good deal?"
    MC "Oh yeah. I’m looking forward to this!"
    Mom "Mmm... Me too."

    $ day_time = 4
    $ MLR2_ES1 = False
    $ MLR2_ES2 = True
    $ can_MLR2_ES2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump kitchen_morning1

