default can_ml_workR2_AS2_talk = True
default can_ml_workR2_AS2 = False

label ml_workR2_AS2_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        MC "Afternoon, Mom! I’m here for some work."
    else:
        MC "Afternoon, Linda! I’m here for some work."
    if can_ml_workR2_AS2 == False and can_ml_workR2_AS2_talk == True:
        Mom "I'm sorry, Sweetie. I don't have any work for you today."
        MC "That's fine."
        Mom "Try again some other day."
        MC "No problem."
        Mom "Now, let me finish this stupid work, so I'll have more time for my pumpkin."
        MC "Okay."
        if persistent.incest_patch == True:
            MC "(Hmm.. Mom seems very busy.. Maybe I should visit her in the evening, to give her a relaxing massage, after work? She should be in the kitchen or in the bedroom.)"
        else:
            MC "(Hmm.. Linda seems very busy.. Maybe I should visit her in the evening, to give her a relaxing massage, after work? She should be in the kitchen or in the bedroom.)"
        $ can_ml_workR2_AS2_talk = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump ml_work_room1_day1

    if can_ml_workR2_AS2 == False and can_ml_workR2_AS2_talk == False:
        Mom "I'm sorry, Sweetie. I don't have any work for you today."
        MC "That's fine."
        Mom "Try again some other day."
        MC "No problem."
        Mom "Now, let me finish this stupid work, so I'll have more time for my pumpkin."
        MC "Okay."
        if persistent.incest_patch == True:
            MC "(Hmm.. Mom seems very busy.. Maybe I should visit her in the evening, to give her a relaxing massage, after work? She should be in the kitchen or in the bedroom.)"
        else:
            MC "(Hmm.. Linda seems very busy.. Maybe I should visit her in the evening, to give her a relaxing massage, after work? She should be in the kitchen or in the bedroom.)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump ml_work_room1_day1
    else:

        Mom "Hey, Sweetie. Do you mind cleaning the office again for me?"
        MC "Sure, no sweat."

        scene ml_workR2_AS1_p2

        Mom "Thank you so much. I’ll be working in here. Just come on back in when you’re done."
        if persistent.incest_patch == True:
            MC "Okay, Mom!"
        else:
            MC "Okay, Linda!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump work_minigame_R2room2_label

label after_ml_workR2_AS2_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ inventory.earn(25)
    $ renpy.pause(3, hard = True)

    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p3 with dissolve

    MC "Aaannnd… that’s me all done!"
    Mom "Nice work - my staff are really appreciating, coming into a tidy office in the morning."
    Mom "(And hopefully that will be enough, to shut down talk of them unionising!)"

    scene ml_workR2_AS1_p4

    Mom "I’ve got good news for you today - I’m almost finished. This is the last file!"
    MC "Awesome!"
    MC "(Hopefully this means I’ll be able to get intimate with her again!)"

    scene ml_workR2_AS1_p5

    MC "When do you think you’ll be finished?"
    Mom "Soon. Just give me until time this evening."
    MC "Oh cool. What are your plans for this evening, then?"

    scene ml_workR2_AS1_p6

    Mom "Well… I was thinking about, taking you and me, to a gorgeous little restaurant on the far side of town."
    Mom "It’s an Italian place - one of the best in town. You’ll love the food."
    if persistent.incest_patch == True:
        Mom "I could NEVER get your father to go. He’s never been interested in, anything other than American burgers."
    else:
        Mom "I could NEVER get Bob to go. He’s never been interested in, anything other than American burgers."
    Mom "(I’ve got more culture in my little toe than the fat idiot has in his whole damn body!) "

    scene ml_workR2_AS1_p8

    Mom "So, what do you say? Interested?"
    MC "Definitely!"

    scene ml_workR2_AS1_p9

    Mom "Great! In that case, we’ll meet in the garage. "
    Mom "I’ll see you there, early this evening. Please don't be late."
    if persistent.incest_patch == True:
        MC "I won’t be - don’t worry, Mom!"
    else:
        MC "I won’t be - don’t worry, Linda!"

    if MLR2_ES1 == True:
        $ MLR2_ES1 = False

    $ can1_MLR2_ES1 = True
    $ ml_workR2_AS2 = False
    $ day_time = 3
    $ MLR2_ES3 = True
    $ can_map = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump garage_evening1
