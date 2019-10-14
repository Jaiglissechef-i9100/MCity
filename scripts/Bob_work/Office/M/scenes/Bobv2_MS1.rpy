image Bobv2_MS1_p1 = "images/Bob_work/office/M/scenes/Bobv2_MS1/1.jpg"
image Bobv2_MS1_p2 = "images/Bob_work/office/M/scenes/Bobv2_MS1/2.jpg"
image Bobv2_MS1_p3 = "images/Bob_work/office/M/scenes/Bobv2_MS1/3.jpg"
image Bobv2_MS1_p4 = "images/Bob_work/office/M/scenes/Bobv2_MS1/4.jpg"
image Bobv2_MS1_p5 = "images/Bob_work/office/M/scenes/Bobv2_MS1/5.jpg"
image Bobv2_MS1_p6 = "images/Bob_work/office/M/scenes/Bobv2_MS1/6.jpg"
image Bobv2_MS1_p7 = "images/Bob_work/office/M/scenes/Bobv2_MS1/7.jpg"
image Bobv2_MS1_p8 = "images/Bob_work/office/M/scenes/Bobv2_MS1/8.jpg"
image Bobv2_MS1_p9 = "images/Bob_work/office/M/scenes/Bobv2_MS1/9.jpg"
image Bobv2_MS1_p10 = "images/Bob_work/office/M/scenes/Bobv2_MS1/10.jpg"

default Bobv2_MS1_q1 = True
default Bobv2_MS1_first_talk = True
default Bobv2_MS1_q2 = True
default Bobv2_MS1_q3 = False
default Bobv2_MS1_q4 = False
default Bobv2_MS1_q5 = False
default Bob_work_minigame = False
default Zv2_MS2 = False
default can_Zv2_MS2_q = False
default can2_Zv2_MS2_q = True
default bob_give_money_first_time = True
label Bobv2_MS1_label:
    hide screen map_button
    if MLR3_Bob_AS1_q7 == True:
        $ clickable = False
        show screen bob_office_M_scr
        MC "I don't want to bother him with it right now. Let's speak with him at home."
        $ clickable = True
        hide screen bob_office_M_scr
        jump bob_office_M1
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer


    scene Bobv2_MS1_p1 with dissolve

    if Bobv2_MS1_first_talk == True:
        if renpy.loadable("patch.rpy"):
            MC "Morning, Dad!"
        else:
            MC "Morning, Bob!"
        Dad "Why, hello there, champ. What brings you over to my office?"
        MC "Not much. Just thought I’d drop by to say hello."

        scene Bobv2_MS1_p2
        if renpy.loadable("patch.rpy"):
            Dad "Well, I’ll never say no to a visit from my favourite son!"
            MC "I’m your ONLY son."
        else:
            Dad "Well, I’ll never say no to a visit from my favourite male tennant!"
            MC "I’m your ONLY male tennant."
        Dad "And thus, my favourite."
        $ Bobv2_MS1_first_talk = False

        jump Bobv2_MS1_menu
    else:
        if renpy.loadable("patch.rpy"):
            MC "Morning, Dad!"
        else:
            MC "Morning, Bob!"

        Dad "Helo there, [player_name]"
        MC "What's up?"
        Dad "Ah! Nothing important. Same day as always."

        jump Bobv2_MS1_menu


label Bobv2_MS1_menu:
    scene Bobv2_MS1_p2
    window hide
    menu:
        "{color=#00ff00}I sorted the documents. Could you pay me?{/color}" if money_from_bob > 0:
            $ bob_payment_money = 0
            if bob_give_money_first_time == True:
                scene Bobv2_MS1_p1
                MC "I sorted the documents. Could you pay me?"
                scene Bobv2_MS1_p2
                Dad "Ah! Good job, [player_name]! Here, take it."
                MC "Thanks!"
                Dad "No, I thank you! I hate doing that! "
                scene Bobv2_MS1_p7
                Dad "After so many times, it started to be incredibly boring."
                MC "Haha!"
                Dad "I'll be more than happy, if you'd start doing it more regularly."
                if renpy.loadable("patch.rpy"):
                    MC "No problem, Dad."
                else:
                    MC "No problem, Bob."
                $ bob_give_money_first_time = False
                jump bob_work_money_give

            if bob_give_money_first_time == False:
                scene Bobv2_MS1_p1
                MC "I sorted the documents yesterday. Could you pay me?"
                scene Bobv2_MS1_p7
                Dad "Again!?"
                Dad "Brilliant! Here, take it."
                Dad "(Now I'll have more time to read my books!)"
                if renpy.loadable("patch.rpy"):
                    MC "Thanks, Dad."
                else:
                    MC "Thanks, Bob."
                jump bob_work_money_give



        "{color=#00ff00}Do you have any work for me?{/color}" if Bobv2_MS1_q1 == True:
            scene Bobv2_MS1_p2

            MC "I was wondering if you had any work I could help with."

            scene Bobv2_MS1_p3

            Dad "You’re looking to get paid, I assume?"
            MC "Yeah, I was kinda hoping that."
            Dad "Come to think of it, I usually need some documents sorted in the afternoon. I'm always in the house at that time, so you can work here if you want. "

            scene Bobv2_MS1_p10

            Dad "The documents to sort will always be lying on my desk after I leave."
            MC "How difficult is this gonna be?"

            scene Bobv2_MS1_p7

            Dad "Difficult? Haha! Not at all! Simply match the documents to the corresponding number."
            MC "What about the payment?"
            Dad "Whenever you finish the job, always come to me."
            Dad "Just remember that I'm only here in the morning!"
            MC "I have to wait another day for a payment?"
            Dad "Haha! Impatience is a very bad habit, [player_name]."
            Dad "You can also ask me at home in the afternoon. I should be in my bedroom smoking my delicious cigars."
            MC "Ugh..!"
            Dad "Don't judge!"
            Dad "I only smoke recreationally - not by addction."
            MC "Yeah... (Every addicted person probably is saying that...)"
            $ Bob_work_minigame = True
            $ Bobv2_MS1_q1 = False
            jump Bobv2_MS1_menu

        "{color=#00ff00}Could you give me the key card for your office?{/color}" if Bobv2_MS1_q2 == True:
            scene Bobv2_MS1_p2

            MC "Could I get the key card to your office?"

            scene Bobv2_MS1_p3

            Dad "Huh… That’s… gonna be a problem. I only have one - and I NEED mine, almost every day."
            MC "Oh. Nevermind, then."

            scene Bobv2_MS1_p8

            Dad "No - hold right there for just one minute. I’ve got an idea."
            Dad "Go over to Zuri and ask for her keycard. It has the same access levels as mine."
            MC "Thanks. But what about her?"

            scene Bobv2_MS1_p7

            Dad "I’ll just order a new one for her."
            if renpy.loadable("patch.rpy"):
                MC "Cool. Thanks, Dad! I’ll go and speak to Zuri now."
            else:
                MC "Cool. Thanks, Bob! I’ll go and speak to Zuri now."
            $ bob_office_locked = False
            $ Bobv2_MS1_q2 = False
            $ Zv2_MS2 = True
            $ can_Zv2_MS2_q = True
            jump Bobv2_MS1_menu
        "{color=#00ff00}Ask about company name.{/color}" if Zv2_MS2_companyname == 4 and Zv2_MS2_companyname_found == 2:
            scene Bobv2_MS1_p1
            if renpy.loadable("patch.rpy"):
                MC "Hey Dad, I know you’re super into investing. I was wondering if I could get some advice from you?"
            else:
                MC "Hey Bob, I know you’re super into investing. I was wondering if I could get some advice from you?"
            Dad "Sure, what do you wanna know, champ?"
            MC "I know all the big investors have companies that they KNOW will do really well, at market. Sort of like, trade secrets."
            scene Bobv2_MS1_p2
            Dad "Haha! Yeah, that’s true."
            MC "Well? Do you have one?"
            Dad "I definitely do."
            MC "Cool! What’s it called?"
            scene Bobv2_MS1_p4

            Dad "Sorry - trade secret. I can’t possibly tell, until we close the deal."
            if renpy.loadable("patch.rpy"):
                MC "Aww, c’mon Dad! I won’t tell anyone. I just want to know more about the business!"
            else:
                MC "Aww, c’mon Bob! I won’t tell anyone. I just want to know more about the business!"
            MC "To be honest, I’m kinda thinking of getting involved in this, when I grow up!"
            scene Bobv2_MS1_p2
            Dad "Really?"
            MC "Yeah!"
            Dad "Hmm... In that case… I suppose."
            Dad "Alright! I’ve got this tip from a member of the European Council. "
            Dad "He’s told me that Nottingham Legal and Commercial Incorporated are getting a massive contract, for a rail network running from Portugal to Germany. We’re talking a multi-billion dollar contract!"
            MC "Wow!"
            MC "(That’s what I need to know!)"
            if renpy.loadable("patch.rpy"):
                MC "I’ll talk to you more about this later, Dad."
            else:
                MC "I’ll talk to you more about this later, Bob."
            Dad "No problem! See you later!"
            $ Zv2_MS2_companyname_found = 3

            jump Bobv2_MS1_menu


        "Ask Dad if he knows about Zuri’s twin sister. " if Bobv2_MS1_q4 == True:
            jump Bobv2_MS1_zurisuri_label



        "{color=#00ff00}Ask Dad how work is going.{/color}" if Bobv2_MS1_q5 == True and renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_work_label
        "{color=#00ff00}Ask Bob how work is going.{/color}" if Bobv2_MS1_q5 == True and not renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_work_label
        "Cancel":

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bob_office_M1



label Bobv2_MS1_zurisuri_label:
    scene Bobv2_MS1_p1
    if renpy.loadable("patch.rpy"):
        MC "Hey, Dad. Did you know Zuri had a twin sister?"
    else:
        MC "Hey, Bob. Did you know Zuri had a twin sister?"


    scene Bobv2_MS1_p7

    Dad "Really?"
    MC "Yeah, a girl named Suri."
    Dad "Strange. I’ve never heard her talk about her."

    scene Bobv2_MS1_p5

    Dad "How did you find out she had a twin?"


    MC "I… uh… She mentioned it to me in the lobby there."

    scene Bobv2_MS1_p3

    Dad "Huh... Alright then. Good for her, I guess."
    $ Bobv2_MS1_q4 = False
    jump Bobv2_MS1_menu

label Bobv2_MS1_work_label:
    scene Bobv2_MS1_p2
    if renpy.loadable("patch.rpy"):
        MC "How’s work going, Dad?"
    else:
        MC "How’s work going, Bob?"
    if Zv2_true_counter > 1:
        scene Bobv2_MS1_p9
        Dad "Ahh, jeez. I wish you hadn’t asked. The whole company is screwed right now."
        MC "(Uh oh…)"
        Dad "Profits are nose diving into the red, and corporate headquarters are on my ass, demanding to know why."
        Dad "I’m gonna have to work TWICE as hard from now on, to turn this ship around."
        if renpy.loadable("patch.rpy"):
            MC "Crap! I’m sorry to hear that, Dad."
        else:
            MC "Crap! I’m sorry to hear that, Bob."

    if Zv2_lie_counter > 1:

        Dad "I’m glad you asked! Things are REALLY turning around over here!"
        Dad "Y’know - I though the market would never recover after that 2009 crash. But look - here we are. And by the looks of things, we’re about to post record profits!"
        if renpy.loadable("patch.rpy"):
            MC "Congratulations, Dad!"
        else:
            MC "Congratulations, Bob!"
        Dad "If all goes according to plan, I should finally start get my annual bonus again!"

    $ Bobv2_MS1_q5 = False
    $ Bob_v3_scenes = True

    jump Bobv2_MS1_menu

label bob_work_money_give:
    if money_from_bob > 0:
        $ inventory.earn(25)
        $ bob_payment_money += 25
        $ money_from_bob -=1
        jump bob_work_money_give
    else:
        "You recive {color=#00ff00}[bob_payment_money]${/color}."
        jump Bobv2_MS1_menu