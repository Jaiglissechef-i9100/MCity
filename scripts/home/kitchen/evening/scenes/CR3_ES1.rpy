image CR3_ES1_p1 = "images/home/kitchen/evening/scenes/CR3_ES1/1.jpg"
image CR3_ES1_p2 = "images/home/kitchen/evening/scenes/CR3_ES1/2.jpg"
image CR3_ES1_p3 = "images/home/kitchen/evening/scenes/CR3_ES1/3.jpg"
image CR3_ES1_p4 = "images/home/kitchen/evening/scenes/CR3_ES1/4.jpg"
image CR3_ES1_p5 = "images/home/kitchen/evening/scenes/CR3_ES1/5.jpg"
image CR3_ES1_p6 = "images/home/kitchen/evening/scenes/CR3_ES1/6.jpg"
image CR3_ES1_p7 = "images/home/kitchen/evening/scenes/CR3_ES1/7.jpg"
image CR3_ES1_p8 = "images/home/kitchen/evening/scenes/CR3_ES1/8.jpg"
image CR3_ES1_p9 = "images/home/kitchen/evening/scenes/CR3_ES1/9.jpg"
image CR3_ES1_p10 = "images/home/kitchen/evening/scenes/CR3_ES1/10.jpg"
image CR3_ES1_p11 = "images/home/kitchen/evening/scenes/CR3_ES1/11.jpg"
image CR3_ES1_p12 = "images/home/kitchen/evening/scenes/CR3_ES1/12.jpg"
image CR3_ES1_p13 = "images/home/kitchen/evening/scenes/CR3_ES1/13.jpg"
image CR3_ES1_p14 = "images/home/kitchen/evening/scenes/CR3_ES1/14.jpg"
image CR3_ES1_p15 = "images/home/kitchen/evening/scenes/CR3_ES1/15.jpg"
image CR3_ES1_p16 = "images/home/kitchen/evening/scenes/CR3_ES1/16.jpg"

label CR3_ES1_label:
    if CR3_ES1_q1 == False and CR3_ES1_q2 == False and CR3_ES1_q3 == False and CR3_ES1_q4 == False and CR3_ES1_q5 == False:
        hide screen map_button
        show screen kitchen_evening_notclickable
        MC "I've already talked to her."
        hide screen kitchen_evening_notclickable
        jump kitchen_morning1

    if CR3_ES1_can == False:
        hide screen map_button
        show screen kitchen_evening_notclickable
        MC "I've already talked to her."
        hide screen kitchen_evening_notclickable
        jump kitchen_morning1
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene CR3_ES1_p1 with dissolve

        MC "(What the heck is Caroline doing? I’ve never seen her sit and drink beer, by herself.)"
        MC "(She really rocks that outfit though! I love those super-tight denim shorts, she’s wearing!)"

        scene CR3_ES1_p2

        MC "(And that crop top, clings around her breasts perfectly! Goddamn! She’s so sexy...)"
        MC "(I don’t think she’s heard me enter the kitchen yet - I should probably announce myself.)"
        MC "H-Hey, Caroline… What’s up?"

        scene CR3_ES1_p3

        Caroline "Huh? Oh! Hey, [player_name]. Nothing much - just chilling out here."
        MC "Why aren’t you in your bedroom?"
        Caroline "Ugh! I’d spent far too long in there, working on the tax returns for my business. I needed a - change of scenery - Figured, the kitchen, would do fine."
        MC "Mind if I join you?"
        Caroline "Sure - grab a seat."

        scene CR3_ES1_p4

        MC "Something on your mind?"
        Caroline " A lotta shit - But you don’t need to concern yourself with it. "
        MC "Are you gonna drink both of those, or can I have one?"

        scene CR3_ES1_p5

        Caroline "Sure, go ahead. They were $2.50 each, or two for $4, at the store - and it seemed a waste to only buy one."
        MC "Thanks, Caroline."
        Caroline "No sweat."

        jump CR3_ES1_menu

label CR3_ES1_menu:
    scene CR3_ES1_p10
    menu:
        "How about we - drink to something?" if CR3_ES1_q1 == True:
            scene CR3_ES1_p6

            MC "How about we - drink to something?"
            Caroline "Sure! What do you want to drink to?"

            menu:
                "Let’s drink to - the success of your business!":
                    scene CR3_ES1_p6

                    MC "Let’s drink to - the success of your business!"

                    scene CR3_ES1_p9

                    Caroline "Now, that’s a drink I can - get behind!"
                    Caroline "Bottoms up - [player_name]!"

                    scene CR3_ES1_p7

                    "*GLUG GLUG GLUG*"
                    MC "(I think that was a - wise choice - to drink to. If I’d asked her about the deal, I might have - pissed her off - or upset her.)"
                    $ CR3_ES1_q1 = False
                    jump CR3_ES1_menu
                "Let’s drink - to good health.":
                    scene CR3_ES1_p6

                    MC "Let’s drink - to good health."

                    scene CR3_ES1_p10

                    Caroline "To good health? Haha! What age are you?! You’re talking like an old man!"
                    MC "It was the best I could think of!"
                    Caroline "Hehe... Fine! To good health!"

                    scene CR3_ES1_p7

                    "*GLUG GLUG*"
                    MC "(Maybe I shouldn’t have chosen such a - vague, generic - thing, to drink to.)"

                    $ CR3_ES1_q1 = False
                    jump CR3_ES1_menu
                "Let’s drink in memory of the great deal we had together.":

                    scene CR3_ES1_p6

                    MC "Let’s drink - in memory - of the great deal we had together."

                    scene CR3_ES1_p8

                    Caroline "P-Pardon?"
                    MC "I said, we should drink - in memory - of the de-"
                    Caroline "I heard what you said - I just can’t believe you said it."

                    scene CR3_ES1_p13

                    Caroline "For fuck’s sake, [player_name]... Did you REALLY have to bring - that deal - up?"
                    MC "I, uh... Sorry. Should we drink to something else..?"
                    Caroline "Just forget it - and drink your damn beer..."

                    scene CR3_ES1_p14

                    "*GLUG*"

                    MC "(Damn... Maybe bringing up the deal - wasn’t the best decision - I have ever made...)"
                    $ CR3_ES1_q1 = False
                    jump CR3_ES1_menu

        "What have you got a towel for, there?" if CR3_ES1_q2 == True:
            scene CR3_ES1_p12

            MC "What have you got a towel for, there?"
            Caroline "Huh? Oh! I wasn’t crying!"
            MC "What? I never asked if you were crying..."

            scene CR3_ES1_p15

            Caroline "I... uh... Oops - I must have misheard you. What did you say?"
            MC "I asked what the towel was for."
            Caroline "Umm... Oh, I was using it to... get a grip on the bottles - to open them. They were difficult to unscrew."

            scene CR3_ES1_p11

            MC "(Weird... Her answer doesn’t make any sense. These AREN’T screw-top bottles.)"
            MC "(What on earth - was she upset about enough, to cry over?)"

            $ CR3_ES1_q2 = False
            jump CR3_ES1_menu

        "You seem stressed. Is there anything I can help with?" if CR3_ES1_q3 == True:
            scene CR3_ES1_p11

            MC "You seem stressed. Is there anything I can help with?"
            Caroline "Absolutely not... I’ll be fine, I can sort this all out myself. I just need to, take tonight, to clear my head and get my thoughts straight."
            MC "Okay, but if you ever need me, you know I’m there, right?"

            scene CR3_ES1_p12

            Caroline "(I know you’re always there… but I can’t go to you, ever again. Not after what happened between us - with that fucking deal.)"
            Caroline "Sure."

            $ CR3_ES1_q3 = False
            jump CR3_ES1_menu

        "What’s got you feeling so down?" if CR3_ES1_q4 == True:
            scene CR3_ES1_p16

            MC "What’s got you feeling so down?"
            Caroline "(Damn, I was hoping he wouldn’t ask this. Now I’m gonna have to try and avoid his question.)"
            Caroline "Eh… Y’know - life in general."

            scene CR3_ES1_p10

            Caroline "But, don’t worry - I’m not depressed or anything. This is just a blip, [player_name]."
            MC "Are you sure? Is it about us?"

            scene CR3_ES1_p8

            Caroline "N-No! Absolutely not! It’s got nothing to do with - that damned deal!"
            MC "(Jesus, she can get VERY defensive - pretty damn fast!)"
            MC "O-Okay, no problem. If you ever want to talk - I’m there."

            $ CR3_ES1_q4 = False
            jump CR3_ES1_menu

        "Why did you end the deal so suddenly? What happened?" if CR3_ES1_q5 == True:
            scene CR3_ES1_p10

            MC "Caroline?"
            Caroline "Yeah?"
            MC "Why did you end our deal, so suddenly? What actually happened?"

            scene CR3_ES1_p12

            Caroline "..."
            MC "It just seemed to - come out of nowhere. I mean - one week, things are going incredible. We’re both having fun, and then suddenly, the deal is dead."
            MC "I mean - I just don’t understand. Did I do something wrong?"

            scene CR3_ES1_p13

            Caroline "Jesus Christ, [player_name]! Will you - shut the fuck up - about that goddamned deal?!"
            Caroline "It wasn’t normal! And as far as I am concerned - it NEVER fucking happened!"
            Caroline "Are we clear?"
            MC "Y-Yeah... we’re clear."

            scene CR3_ES1_p14

            MC "(Holy shit! That’s a - raw nerve - if I’ve ever seen one!)"
            MC "(I’ve obviously done something wrong, but I don’t have the faintest idea what it is!)"
            "*GLUG GLUG*"

            $ CR3_ES1_q5 = False
            jump CR3_ES1_menu
        "Bye.":

            scene CR3_ES1_p16

            MC "Well, I guess I better go now. I’ll see you later, Caroline."
            Caroline "Yeah... see you tomorrow, [player_name]."

            $ CR3_ES1_can = False
            $ CR3_NS1_can = True
            if not sms_Caroline7 in sms_box.sms_s:
                $ C_SMS4 = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump kitchen_morning1
