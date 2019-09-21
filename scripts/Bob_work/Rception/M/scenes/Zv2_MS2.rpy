image Zv2_MS2_p1 = "images/Bob_work/reception/M/scenes/Zv2_MS2/1.jpg"
image Zv2_MS2_p2 = "images/Bob_work/reception/M/scenes/Zv2_MS2/2.jpg"
image Zv2_MS2_p3 = "images/Bob_work/reception/M/scenes/Zv2_MS2/3.jpg"
image Zv2_MS2_p4 = "images/Bob_work/reception/M/scenes/Zv2_MS2/4.jpg"
image Zv2_MS2_p5 = "images/Bob_work/reception/M/scenes/Zv2_MS2/5.jpg"
image Zv2_MS2_p6 = "images/Bob_work/reception/M/scenes/Zv2_MS2/6.jpg"
image Zv2_MS2_p7 = "images/Bob_work/reception/M/scenes/Zv2_MS2/7.jpg"
image Zv2_MS2_p8 = "images/Bob_work/reception/M/scenes/Zv2_MS2/8.jpg"
image Zv2_MS2_p9 = "images/Bob_work/reception/M/scenes/Zv2_MS2/9.jpg"

default Zv2_MS2_q1 = True
default Zv2_MS2_q2 = True
default Zv2_MS2_q3 = True
default Zv2_MS2_q4 = True
default Zv2_MS2_q5 = False
default Zv2_MS2_q6 = False
default Zv2_MS2_q7 = False
default Zv2_MS2_q8 = False
default Zv2_MS2_q9 = False
default Zv2_MS2_q10 = False
default Zv2_MS2_companyname = 0
default Zv2_MS2_companyname_found = 0
default Zv2_MS2_truth = False
default Zv2_ES1 = False
default Zv2_lie_counter = 0
default Zv2_true_counter = 0
default Zv2_Truth = False

label Zv2_MS2_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if Zv2_Truth == True:
        scene Zv2_MS2_p1 with dissolve

        MC "Hi, Zuri!"
        Zuri "Oh! Hello, [player_name]."

        scene Zv2_MS2_p9

        Zuri "Your help with those names, earned me and my sister MILLIONS. We’re both VERY thankful for what you did for us."
        MC "It was nothing, Zuri. Thanks again for everything the TWO OF YOU did for ME."
        jump Zv2_MS2_cancel_label
    else:

        scene Zv2_MS2_p1 with dissolve

        Zuri "Ahh! Hello again, [player_name]! How are you?"
        MC "I’m good, Zuri. Busy today?"
        Zuri "We’re always busy in here."

        jump Zv2_MS2_menu

label Zv2_MS2_menu:
    scene Zv2_MS2_p1
    window hide
    menu:
        "How long have you worked for Dad for?" if Zv2_MS2_q1 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q1_label
        "How long have you worked for Bob for?" if Zv2_MS2_q1 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q1_label

        "Where did you meet Dad?" if Zv2_MS2_q2 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q2_label
        "Where did you meet Bob?" if Zv2_MS2_q2 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q2_label

        "What’s it like working for Dad? " if Zv2_MS2_q3 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q3_label
        "What’s it like working for Bob? " if Zv2_MS2_q3 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q3_label

        "{color=#00ff00}Ask her for magnet card for Dad's office doors.{/color}" if Zv2_MS2_q4 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_magnetcard_label
        "{color=#00ff00}Ask her for magnet card for Bob's office doors.{/color}" if Zv2_MS2_q4 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_magnetcard_label

        "{color=#00ff00}Ask her when Dad has a business trip, or something.{/color}" if Zv2_MS2_q5 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_bobtrip_label
        "{color=#00ff00}Ask her when Bob has a business trip, or something.{/color}" if Zv2_MS2_q5 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_bobtrip_label

        "Zuri is an unusual name. Where are you from?" if Zv2_MS2_q6 == True:
            jump Zv2_MS2_zuriname_label

        "Is the pay good?" if Zv2_MS2_q7 == True:
            jump Zv2_MS2_pay_label

        "{color=#00ff00}Talk about Zuri proposition.{/color}" if Zv2_MS2_q9 == True:
            jump Zv2_MS2_zuriproposition_label

        "{color=#00ff00}Talk about company name.{/color}" if Zv2_MS2_q10 == True:
            jump Zv2_MS2_companyname1_label
        "Cancel":

            jump Zv2_MS2_cancel_label

label Zv2_MS2_q1_label:
    scene Zv2_MS2_p3
    if renpy.loadable("patch.rpy"):
        MC "How long have you worked for Dad, Zuri?"
    else:
        MC "How long have you worked for Bob, Zuri?"
    Zuri "It must be… three or four months now?"
    MC "Huh? You’re fairly new here, then?"

    scene Zv2_MS2_p1

    Zuri "Yes, I got lucky. This is a great company to work for. Much better than my old job!"
    MC "I’m glad to hear that!"
    $ Zv2_MS2_q1 = False
    jump Zv2_MS2_menu

label Zv2_MS2_q2_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "Where did you meet Dad, then?"
    else:
        MC "Where did you meet Bob. then?"

    scene Zv2_MS2_p4

    Zuri "The interview was only five months ago - but I’d known him before that."
    Zuri "We met in France, at a business conference in Toulouse. That must have been three or four years ago."
    MC "Cool. The two of you go way back, then?"

    scene Zv2_MS2_p2

    Zuri "Not really. We lost touch, shortly after the conference. It wasn’t until I met him again in New York that he told me he was looking for a new secretary."
    MC "Well, congrats on the job!"
    Zuri "Thanks!"
    $ Zv2_MS2_q2 = False
    jump Zv2_MS2_menu

label Zv2_MS2_q3_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "So, what’s it like working for Dad?"
    else:
        MC "So, what’s it like working for Bob?"

    scene Zv2_MS2_p5

    if renpy.loadable("patch.rpy"):
        Zuri "I really enjoy working for your father. There are some bosses who pile work on their employees."
        Zuri "Your father isn’t like that - he takes a LOT of work on, himself."
    else:
        Zuri "I really enjoy working for Bob. There are some bosses who pile work on their employees."
        Zuri "Bob isn’t like that - he takes a LOT of work on, himself."
    Zuri "He leads by example, and I’m really proud to work for him."
    $ Zv2_MS2_q3 = False
    jump Zv2_MS2_menu

label Zv2_MS2_magnetcard_label:
    if renpy.loadable("patch.rpy"):
        MC "Hi, Zuri. I just spoke with Dad there. He said I could grab your magnetic card."
    else:
        MC "Hi, Zuri. I just spoke with Bob there. He said I could grab your magnetic card."
    Zuri "Really?"
    MC "Yeah, he probably sent you an email explaining the situation."

    scene Zv2_MS2_p6

    Zuri "Let me check…"
    Zuri "Ah! There it is. Okay, no problem. Let me get it for you now."
    MC "Thanks, Zuri!"

    scene Zv2_MS2_p7
    if renpy.loadable("patch.rpy"):
        Zuri "Did your father say anything about getting me a new card?"
    else:
        Zuri "Did Bob say anything about getting me a new card?"
    MC "Yeah, he did. Hopefully it won’t take too long."
    Zuri "It’s okay - I don’t need it soon anyway."
    $ Zv2_MS2_q4 = False
    $ inventory.add(zuri_magentcard )
    jump Zv2_MS2_menu

label Zv2_MS2_bobtrip_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "Zuri, I was wondering… Does Dad have any business trips coming up soon?"
    else:
        MC "Zuri, I was wondering… Does Bob have any business trips coming up soon?"
    scene Zv2_MS2_p3

    Zuri "Probably? Why do you want to know?"
    if renpy.loadable("patch.rpy"):
        MC "I uh… We’re planning to do a family dinner some night, and we want to make sure he’s at home for it."
    else:
        MC "I uh… We’re planning to do a dinner some night, and we want to make sure he’s at home for it."

    scene Zv2_MS2_p9

    Zuri "Aww, that’s nice. I’m sure he’d love that!"
    Zuri "Let me check his diary for you, to see when he’s busy…"

    scene Zv2_MS2_p8

    Zuri "Okay… It looks like he is away THIS weekend. I can’t see any other business trips."
    MC "That’s perfect, Zuri! That’s all I need to know."
    if renpy.loadable("patch.rpy"):
        Zuri "Happy I could help. Enjoy your family dinner!"
        MC "(Great! I just have to let Mom know that Dad is away this weekend now!)"
    else:
        Zuri "Happy I could help. Enjoy your dinner!"
        MC "(Great! I just have to let Linda know that Bob is away this weekend now!)"

    $ MLR2_MS1_BCalendar = True
    $ Zv2_MS2_q8 = True
    $ Zv2_MS2_q5 = False
    jump Zv2_MS2_menu

label Zv2_MS2_zuriname_label:
    scene Zv2_MS2_p1

    MC "Zuri is quite an unusual name. Where did you get it from?"

    scene Zv2_MS2_p2

    Zuri "Unusual? What do you mean?"
    MC "I don’t mean in a bad way! It’s really cute actually!"

    scene Zv2_MS2_p9

    Zuri "Aww... you’re sweet. It’s French actually. I was born, just outside Marseille."
    MC "Cool! Do you miss France, at all?"
    Zuri "Sometimes… I really enjoy living over here though."
    $ Zv2_MS2_q6 = False
    jump Zv2_MS2_menu

label Zv2_MS2_pay_label:
    scene Zv2_MS2_p1

    MC "Is the pay good, working here?"
    scene Zv2_MS2_p3

    Zuri "Haha! What makes you think I’d talk about my pay with you?"
    if renpy.loadable("patch.rpy"):
        MC "I’m just curious if my dad pays his staff well."
    else:
        MC "I’m just curious if Bob pays his staff well."

    Zuri "Let me promise you something - no staff in this company are paid badly. There’s a reason why so few people here leave for other jobs."
    $ Zv2_MS2_q7 = False
    jump Zv2_MS2_menu

label Zv2_MS2_zuriproposition_label:
    scene Zv2_MS2_p1

    Zuri "I take it you’ve considered my proposition."

    scene Zv2_MS2_p2

    Zuri "I’m eagerly awaiting your answer. What’s it going to be? "
    window hide
    menu:
        "{color=#00ff00}Yes, I’ll help you get the company name.{/color}":
            scene Zv2_MS2_p3

            MC "Yes, I’ll help you get the company name."
            Zuri "Brilliant! Thank you so much!"
            Zuri "I will make sure you are handsomely rewarded for your help."
            if renpy.loadable("patch.rpy"):
                Zuri "Your dad is always out of the office in the afternoon. Go inside and then you can search for the company name."
            else:
                Zuri "Bob is out of the office always in the afternoon. Go inside and then you can search for the company name."
            MC "Why can’t YOU just search his office?"
            Zuri "He has installed a few cameras in there, so it’s too risky for me, but he will never suspect YOU! Or even that you’d be searching his office, when he monitors your access."
            $ Zv2_MS2_q9 = False
            $ Zv2_MS2_q10 = True
            $ Zv2_MS2_companyname = 1

            jump Zv2_MS2_menu
        "No, I’m not gonna help with this.":


            scene Zv2_MS2_p4

            MC "I’ve thought about it… and I’d rather not get involved in this."
            Zuri "I’m sorry to hear that. If you change your mind, please come back and speak to me."
            Zuri "I could REALLY make it worth your while."
            jump Zv2_MS2_menu

label Zv2_MS2_companyname1_label:
    if Zv2_MS2_companyname == 1:
        scene Zv2_MS2_p2

        Zuri "Do you have it? Do you have the company name?"
        window hide
        menu:
            "No, not yet.":

                MC "No, I don’t have it yet."
                Zuri "Please, hurry up and get it!"
                jump Zv2_MS2_menu

            "{color=#00ff00}Yes.{/color}" if Zv2_MS2_companyname_found == 1:
                MC "Yes, I have it."

                scene Zv2_MS2_p5

                Zuri "Great! I knew I could trust you! What’s the name?"
                window hide
                menu:
                    "{color=#00ff00}Tell the truth.{/color}":
                        MC "The company is called Charterhouse Investments."
                        Zuri "Amazing! Please come over to my house again this evening and I’ll make sure you get your reward."
                        $ Zv2_MS2_companyname = 2
                        $ Zv2_ES2 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Lie about the name.{/color}":


                        MC "The company is called Beerhouse Investments."
                        Zuri "Amazing! Please come over to my house again this evening and I’ll make sure you get your reward."
                        $ Zv2_MS2_companyname = 2
                        $ Zv2_ES2 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu

    if Zv2_MS2_companyname == 2:
        scene Zv2_MS2_p2

        Zuri "Hello, [player_name]! "
        Zuri "Well? Did you have any luck getting the second company name?"
        window hide
        menu:
            "No, not yet.":
                MC "No, I don’t have it yet."
                Zuri "You were a great help with the first name. Please get it as soon as possible for me."
                jump Zv2_MS2_menu

            "{color=#00ff00}Yes.{/color}" if Zv2_MS2_companyname_found == 2:
                MC "Yes, I have it. It was written on a note in the safe."

                scene Zv2_MS2_p5

                Zuri "Great! You’re proving a brilliant asset! What’s the second company’s name?"
                window hide
                menu:
                    "{color=#00ff00}Tell the truth.{/color}":
                        MC "The second company trades under the name of Jakarta Legal Procurements."
                        Zuri "Brilliant! As before, come over to my place and I’ll make sure you’re properly rewarded."
                        $ Zv2_MS2_companyname = 3
                        $ Zv2_ES3 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Lie about the name.{/color}":


                        MC "The company name is… Indian Railway and Infrastructure Investments."
                        Zuri "Brilliant! As before, come over to my place and I’ll make sure you’re properly rewarded."
                        $ Zv2_MS2_companyname = 3
                        $ Zv2_ES3 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu

    if Zv2_MS2_companyname == 3:

        scene Zv2_MS2_p9

        Zuri "[player_name]! Ready for some action?"
        MC "Huh? What do you mean?"
        Zuri "Work! We’re not done yet.. I’m sure you want... more?"
        MC "*Gulp* What’s the plan?"

        scene Zv2_MS2_p2

        Zuri "The third and final company name is going to be more difficult to get."
        if renpy.loadable("patch.rpy"):
            Zuri "It’s a complete secret - the only person who knows is your father. And he’s not writing it down anywhere."
        else:
            Zuri "It’s a complete secret - the only person who knows is Bob. And he’s not writing it down anywhere."
        Zuri "That’s why I need you. I need you to speak with him and get him to give you the name. Understand?"
        MC "I got it. I’ll see what I can do."

        $ Zv2_MS2_companyname = 4
        jump Zv2_MS2_menu

    if Zv2_MS2_companyname == 4:
        scene Zv2_MS2_p5
        if renpy.loadable("patch.rpy"):
            Zuri "Well? Did you get the final name from your father?"
        else:
            Zuri "Well? Did you get the final name from Bob?"
        window hide
        menu:
            "No, not yet.":
                MC "No, I don’t have it yet. It’s proving more difficult than I thought to make him tell me."
                Zuri "Please keep trying. It’s really important that we get this name."
                jump Zv2_MS2_menu

            "{color=#00ff00}Yes.{/color}" if Zv2_MS2_companyname_found == 3:
                MC "Yes, I have it."

                scene Zv2_MS2_p5

                Zuri "Great! I knew I could trust you! What’s the last name?"
                window hide
                menu:
                    "{color=#00ff00}Tell the truth.{/color}":
                        MC "The final company is Nottingham Legal and Commercial Incorporated."
                        Zuri "You’re absolutely amazing! God! I could kiss you right now! Please come over to my house, this evening, and I’ll give you another reward."
                        $ Zv2_MS2_companyname = False
                        $ Zv2_ES3a = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Lie about the name.{/color}":

                        MC "The final company is… Manchester Aviation and Aeronautics Engineering."
                        Zuri "You’re absolutely amazing! God! I could kiss you right now! Please come over to my house, this evening, and I’ll give you another reward."
                        $ Zv2_MS2_companyname = False
                        $ Zv2_ES3a = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu

label Zv2_MS2_cancel_label:
    if Zv2_MS2_q8 == True:
        scene Zv2_MS2_p1

        Zuri "Wait- before you leave, [player_name]."
        Zuri "Would you like to come over to my house, this evening?"
        MC "Huh? Why?"
        Zuri "Oh, come on. A pretty girl is asking you over to her place. How could you possibly say no?"

        scene Zv2_MS2_p6

        Zuri "Just let me.. Hmm.. Ah!"

        scene Zv2_MS2_p7

        Zuri "This is my address."
        MC "Is this… a… a date?"

        scene Zv2_MS2_p9

        Zuri "Haha! Just come over and find out for yourself."
        $ Zv2_MS2_q8= False
        $ Z_home_unlocked = True
        $ Zv2_ES1 = True
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
    else:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
