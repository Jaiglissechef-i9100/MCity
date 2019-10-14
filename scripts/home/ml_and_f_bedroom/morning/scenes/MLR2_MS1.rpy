image MLR2_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/1.jpg"
image MLR2_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/2.jpg"


image MLR2_MS1_talk_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/1.jpg"
image MLR2_MS1_talk_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/2.jpg"
image MLR2_MS1_talk_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/3.jpg"
image MLR2_MS1_talk_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/4.jpg"
image MLR2_MS1_talk_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/5.jpg"
image MLR2_MS1_talk_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/6.jpg"
image MLR2_MS1_talk_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/7.jpg"
image MLR2_MS1_talk_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/8.jpg"


image MLR2_MS1_kiss_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/1.jpg"
image MLR2_MS1_kiss_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/2.jpg"
image MLR2_MS1_kiss_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/3.jpg"
image MLR2_MS1_kiss_p4a = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4a.jpg"
image MLR2_MS1_kiss_p4b = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4b.jpg"
image MLR2_MS1_kiss_p4c = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4c.jpg"
image MLR2_MS1_kiss_p5a = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5a.jpg"
image MLR2_MS1_kiss_p5b = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5b.jpg"
image MLR2_MS1_kiss_p5c = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5c.jpg"
image MLR2_MS1_kiss_p5d = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5d.jpg"
image MLR2_MS1_kiss_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/6.jpg"

image MLR2_MS1_Bob_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/1.jpg"
image MLR2_MS1_Bob_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/2.jpg"
image MLR2_MS1_Bob_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/3.jpg"

image MLR2_R3_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/1.jpg"
image MLR2_R3_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/2.jpg"
image MLR2_R3_MS1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/3.jpg"
image MLR2_R3_MS1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/4.jpg"
image MLR2_R3_MS1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/5.jpg"
image MLR2_R3_MS1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/6.jpg"
image MLR2_R3_MS1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/7.jpg"
image MLR2_R3_MS1_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/8.jpg"
image MLR2_R3_MS1_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/9.jpg"
image MLR2_R3_MS1_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/R3/10.jpg"

default can_MLR2_MS1_talk = True
default MLR2_MS1_talk_count = 1
default MLR2_MS1_kiss_count = 1
default can_MLR2_MS1_kiss = True
default MLR2_MS1_NS1 = False
default MLR2_MS1_ES3 = False
default MLR2_MS1_BCalendar = False
default MLR2_MS1_visit = 1

default MLR2_R3_MS1_q1 = False
default MLR2_R3_MS1_q2 = False
default MLR2_R3_MS1_q3 = False
default MLR2_R3_MS1_q4 = False

default MLR2_R3_MS1_q5 = False
default MLR2_R3_MS1_q6 = False
default MLR2_R3_MS1_q7 = False
default MLR2_R3_MS1_q8 = False
default MLR2_R3_MS1_q9 = False
label MLR2_MS1_label:
    if MLR2_can_MS1 == False:
        show screen parents_bedroom_morning_notclickable
        MC "I've already talked to her."
        hide screen parents_bedroom_morning_notclickable
        $ can_hide_windows = False
        jump parents_bedroom_morning1
    else:
        $ can_hide_windows = True
        if MLR2_MS1_visit == 5:
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            scene MLR2_MS1_talk_p1
            Mom "Hello again! Thanks for dropping by again, Sweetie. It’s nice to be visited by a man in the morning."
            if renpy.loadable("patch.rpy"):
                Mom "Your father just rolls out of bed and goes to work. He’s probably not a morning person, but it just doesn’t feel like he’s making the effort."
            else:
                Mom "Bob just rolls out of bed and goes to work. He’s probably not a morning person, but it just doesn’t feel like he’s making the effort."
            MC "No problem, [Mom_name]. I’m sure he isn’t doing it maliciously. He’s probably just tired, and dreading the thought of having to go to another day at work."
            Mom "Eh, perhaps."

            scene MLR2_MS1_talk_p3

            MC "Are you free for a few minutes to chat?"
            Mom "*Slurp*"
            Mom "Uh huh!"
            scene MLR2_MS1_talk_p4
            jump MLR2_MS1_menu
        if MLR2_MS1_visit == 4:
            scene MLR2_MS1_p1
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            MC "Hi [Mom_name], what you up to?"

            scene MLR2_MS1_talk_p3

            Mom "Not much, just reading the morning news. What’s got you out of bed so early?"
            MC "I just thought I’d make a head start on the day!"
            MC "Are you free for a chat at the minute?"
            Mom "Sure."

            jump MLR2_MS1_menu
        if MLR2_MS1_visit == 2:
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button
            scene MLR2_MS1_p2
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            Mom "Good morning, Sweetie. What’s up?"
            jump MLR2_MS1_menu
        if MLR2_MS1_visit == 1:
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button

            scene MLR2_MS1_p1 with dissolve
            if renpy.loadable("patch.rpy"):
                MC "(Damn, Mom looks hot in that black lingerie.)"
                MC "Morning, Mom! Looking good there!"
            else:

                MC "(Damn, Linda looks hot in that black lingerie.)"
                MC "Morning, Linda! Looking good there!"



            scene MLR2_MS1_p2

            Mom "Good morning, Sweetie. What’s up?"
            $ MLR2_MS1_visit += 1
            jump MLR2_MS1_menu

label MLR2_MS1_menu:
    scene MLR2_MS1_p2
    window hide
    menu:

        "{color=#00ff00}Talk with Mom.{/color}" if renpy.loadable("patch.rpy") and can_MLR2_MS1_talk == True and MLR2_MS1_talk_count < 4:
            jump MLR2_MS1_talk_label

        "Talk with Linda." if not renpy.loadable("patch.rpy") and can_MLR2_MS1_talk == True and MLR2_MS1_talk_count < 4:
            jump MLR2_MS1_talk_label

        "{color=#00ff00}Ask for a kiss. {/color}" if can_MLR2_MS1_kiss == True and MLR2_MS1_kiss_count == 1:
            jump MLR2_MS1_kiss_label
        "Ask for a kiss." if can_MLR2_MS1_kiss == True and MLR2_MS1_kiss_count == 2:
            jump MLR2_MS1_kiss_label

        "{color=#00ff00}Talk about Dad.{/color}" if renpy.loadable("patch.rpy") and MLR2_MS1_NS1 == True:
            jump MLR2_MS1_Bob_label
        "{color=#00ff00}Talk about Bob.{/color}" if not renpy.loadable("patch.rpy") and MLR2_MS1_NS1 == True:
            jump MLR2_MS1_Bob_label



        "{color=#00ff00}Talk about Dad.{/color} " if renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == True:
            jump MLR2_MS1_Bob_Trip_label
        "{color=#00ff00}Talk about Bob.{/color} " if not renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == True:
            jump MLR2_MS1_Bob_Trip_label


        "Talk about Dad. (disabled)" if renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == False and MLR2_NS2 == True:
            jump MLR2_MS1_Bob_Trip_label
        "Talk about Bob. (disabled)" if not renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == False and MLR2_NS2 == True:
            jump MLR2_MS1_Bob_Trip_label


        "Are you missing our holiday at the beach? I know I am." if MLR2_R3_MS1_q1 == True:
            jump MLR2_R3_MS1_q1
        "What happens if I accidentally get you pregnant?" if MLR2_R3_MS1_q2 == True:
            $ MLR2_R3_MS1_talk += 1
            jump MLR2_R3_MS1_q2
        "Hypothetically… how would you feel about me dating another girl?" if MLR2_R3_MS1_q3 == True:
            $ MLR2_R3_MS1_talk += 1
            jump MLR2_R3_MS1_q3
        "When did you first develop a crush on me?" if MLR2_R3_MS1_q4 == True:
            $ MLR2_R3_MS1_talk += 1
            jump MLR2_R3_MS1_q4
        "How would you feel about me dating Sara or Caroline?" if MLR2_R3_MS1_q5 == True:
            jump MLR2_R3_MS1_q5
        "Umm, if you don’t mind me asking. Have you ever cheated on [Dad_name] before?" if MLR2_R3_MS1_q6 == True:
            jump MLR2_R3_MS1_q6
        "What’s your favourite sex position?" if MLR2_R3_MS1_q7 == True:
            jump MLR2_R3_MS1_q7
        "Have you ever done anal, [Mom_name]?" if MLR2_R3_MS1_q8 == True:
            jump MLR2_R3_MS1_q8
        "[Mom_name], why did you lift up Sara’s skirt in the kitchen?" if MLR2_R3_MS1_q9 == True:
            jump MLR2_R3_MS1_q9

        "{color=#00ff00}Talk about Dad trip.{/color}" if renpy.loadable("patch.rpy") and MLR2_MS1_BCalendar == True and MLR2_MS1_ES3 == 3:
            jump MLR2_MS1_Bob_Trip2_label
        "{color=#00ff00}Talk about Bob trip.{/color}" if not renpy.loadable("patch.rpy") and MLR2_MS1_BCalendar == True and MLR2_MS1_ES3 == 3:
            jump MLR2_MS1_Bob_Trip2_label
        "Bye. ":


            jump MLR2_MS1_Cancel_label
label MLR2_MS1_talk_label:
    if MLR2_MS1_talk_count == 1:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Nothing much, Mom. I just dropped by to say hello."
        else:
            MC "Nothing much, Linda. I just dropped by to say hello."
        Mom "Aww, that’s kind of you."
        Mom "Would you like some coffee? I think there’s still some in the kettle."

        scene MLR2_MS1_talk_p2

        MC "Nah, I’m good."
        Mom "How are things with Sara? Are you two getting up to any adventures together?"

        scene MLR2_MS1_talk_p3
        if Sara_points >=2:

            MC "(Oh shit! There’s no way she knows that Sara and I have been dating… right?)"
            MC "(I’ve got to think up an excuse quickly.)"
            MC "Uhh… yeah, we’ve been hanging out together. I realised I didn’t really spend a whole lot of time with Sara when I was younger - so I’m trying to make up for that now."

            scene MLR2_MS1_talk_p2

            Mom "Aww, that’s sweet. I’m glad you two are getting along well."
        if Sara_points ==1:

            MC "Adventures? I wish."
            MC "It’s just been constant work in school, for both of us."

            scene MLR2_MS1_talk_p4
            if renpy.loadable("patch.rpy"):
                Mom "You should think about spending more time with your younger sister. She really looks up to you, you know that?"
                MC "I know, I know. I’m just super busy, with everything right now, Mom."
            if not renpy.loadable("patch.rpy"):
                Mom "You should think about spending more time with Sara. She really looks up to you, you know that?"
                MC "I know, I know. I’m just super busy, with everything right now, Linda."
        $ MLR2_MS1_talk_count = 2
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

    if MLR2_MS1_talk_count == 2:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Busy, as usual, Mom?"
        if not renpy.loadable("patch.rpy"):
            MC "Busy as usual, Linda."
        MC "Working from bed today, I see?"

        scene MLR2_MS1_talk_p6

        Mom "Haha! You caught me. Yeah, I’m just checking over our European accounts."
        MC "Anything interesting?"

        scene MLR2_MS1_talk_p8

        Mom "Not unless you’re fascinated by European Union internal market regulations."
        MC "Uh... No, I can’t say I am."

        scene MLR2_MS1_talk_p2

        Mom "Speaking of being busy with work - Caroline seems up to her eyes in that store she’s opened."
        Mom "I hope you’re not distracting her too much when you visit her shop."
        if Caroline_points >= 2:

            MC "(Uh oh… I hope she hasn’t worked out, I’ve gotten freaky with Caroline too!)"
            MC "I… Uh… No! No, I’m not distracting her."
            MC "If anything, she’s the one distracting me!"

            scene MLR2_MS1_talk_p8

            Mom "Huh? What does that mean?"
            MC "(Fuck!)"
            MC "I… uh… I mean… she’s a distracting… inspiration for me, to start my… own business."

            scene MLR2_MS1_talk_p4

            Mom "Ooookay then…"
            Mom "I guess that’s alright, as long as you aren’t bothering her too much."
            MC "(Phew! Dodged a bullet there!)"

        if Caroline_points == 1:

            MC "Honestly? I’ve been too busy to really help her out that much."
            Mom "That’s understandable. Your school studies do come first after all."
            MC "Yeah, that’s true."

        scene MLR2_MS1_talk_p1

        Mom "I know you’re both busy, but do try to make time for each other."
        Mom "If you make good friendships, they will serve you well all of your life.."
        if renpy.loadable("patch.rpy"):
            MC "Okay, Mom. I’ll keep that in mind."
        if not renpy.loadable("patch.rpy"):
            MC "Okay, Linda. I’ll keep that in mind."

        $ MLR2_MS1_talk_count = 3
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

    if MLR2_MS1_talk_count == 3:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Eh, I’m alright. A little worried about Dad, to be honest."
        else:
            MC "Eh, I’m alright. A little worried about Bob, to be honest."
        scene MLR2_MS1_talk_p4

        Mom "Worried? Did something happen? Did he say something to you?"
        MC "No! No! Not yet… I’m just worried about getting caught."
        Mom "Well, I don’t think you’ve got anything to be worried about right now."
        Mom "If we-"

        "(BING! One New Email!)"

        scene MLR2_MS1_talk_p7

        Mom "Sorry, that’s mine. Can we talk about this later?"
        if renpy.loadable("patch.rpy"):
            MC "Sure, Mom."
        else:
            MC "Sure, Linda."
        $ MLR2_MS1_talk_count = 4
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

label MLR2_MS1_kiss_label:

    if renpy.loadable("patch.rpy"):
        MC "Could I kiss you, Mom?"
    else:
        MC "Could I kiss you, Linda?"
    scene MLR2_MS1_kiss_p1
    Mom "Of course, Sweetie. You don’t have to ask, you know that?"
    MC "I don’t?"
    Mom "Not at all. I want you to kiss me."
    Mom "You can do ANYTHING you want to me. If you want to touch my ass or grab my tits, just go ahead."
    Mom "Be confident and forward. Girls love that."
    MC "S-Should I not ask for permission first?"
    Mom "Of course you should. This is me giving you permission right now."

    scene MLR2_MS1_kiss_p2

    Mom "Now, shut up and kiss me."
    if renpy.loadable("patch.rpy"):
        MC "(Okay, it sounds like, Mom really wants me to act more dominant in this relationship.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Okay, it sounds like Linda really wants me to act more dominant in this relationship.)"

    MC "(Or maybe just more confident? I’ve never properly dated a girl before.)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene MLR2_MS1_kiss_p3

    Mom "Mmm…"
    MC "Mmm!"
    MC "(I wonder if I should be more forward, right now, and try to grab her tits or ass while we’re kissing?)"
    window hide
    menu:
        "Grab her tits.":
            scene MLR2_MS1_kiss_p5a
            if renpy.loadable("patch.rpy"):
                MC "(I’ll give Mom’s tits a squeeze and see how she enjoys it.)"
            if not renpy.loadable("patch.rpy"):
                MC "(I’ll give Linda’s tits a squeeze and see how she enjoys it.)"
            if renpy.loadable("patch.rpy"):
                MC "(She’s got great breasts - my poor sister Sara never inherited those genes though!)"
            else:
                MC "(She’s got great breasts - it’s a shame about Sara’s breasts!)"

            scene MLR2_MS1_kiss_p5b

            MC "(That’s my hands resting on her breasts now. Time to give them a firm squeeze.)"
            if renpy.loadable("patch.rpy"):
                MC "(I’ve heard that girls have really sensitive breasts - I wonder if Mom will feel pleasure if I squeeze them while I make out with her?)"
            else:
                MC "(I’ve heard that girls have really sensitive breasts - I wonder if Linda will feel pleasure if I squeeze them while I make out with her?)"

            scene MLR2_MS1_kiss_p5c

            Mom "Mmmmmm!"
            MC "(Well, that answers that question!)"
            Mom "(Yes! It looks like he’s finally gaining a bit of confidence!)"
            jump after_menu_MLR2_MS1_kiss
        "Grab her ass.":

            scene MLR2_MS1_kiss_p4a

            MC "(Let’s grab her ass and see how she reacts.)"
            MC "(She’s not wearing any pyjama bottoms, so I’ve got a great opportunity to feel around down there.)"

            scene MLR2_MS1_kiss_p4b

            Mom "Mmm!"
            MC "(Sounds like she’s enjoying that! Let’s give it a harder squeeze!)"
            Mom "(Yes! It looks like he’s finally starting to understand how to treat a woman!)"

            scene MLR2_MS1_kiss_p4c

            Mom "Ooohhhmmmmm!"
            MC "(Yeah, I was bang on the money there! Grabbing her ass was the way to go!)"
            jump after_menu_MLR2_MS1_kiss

label after_menu_MLR2_MS1_kiss:
    scene MLR2_MS1_kiss_p5d

    MC "Mmm…"
    Mom "Mmm!"
    Mom "(Oh God… If I keep this up, I’ll lose my whole morning!)"

    scene MLR2_MS1_kiss_p6

    Mom "O-Okay, time to stop now. Haha! I have work to do."
    Mom "You can be VERY distracting, you know that?"
    MC "Sorry. My bad. Haha!"
    Mom "Remember what I said, okay? You have permission to be more forward and confident with me."
    Mom "Do what you want - and if you’re unsure, please ask. Healthy sexual relationships are built on openness and honesty."
    if renpy.loadable("patch.rpy"):
        Mom "(Some great advice from friend right there!)"
    else:
        Mom "(Some great great friendly advice!)"
    if renpy.loadable("patch.rpy"):
        MC "Okay, Mom. Thanks for letting me know."
    if not renpy.loadable("patch.rpy"):
        MC "Okay, Linda. Thanks for letting me know."
    $ can_MLR2_MS1_kiss = False
    if MLR2_MS1_kiss_count == 1:
        $ MLR2_ES1 = True
        $ MLR2_MS1_kiss_count = 2
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        jump MLR2_MS1_menu
    $ MLR2_MS1_kiss_count = 2
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    jump MLR2_MS1_menu

label MLR2_MS1_Bob_label:
    scene MLR2_MS1_talk_p2
    if renpy.loadable("patch.rpy"):
        MC "Can we talk about Dad?"
    else:
        MC "Can we talk about Bob?"
    Mom "Hmm? Sure, what about him?"
    MC "It’s about the two of you… having sex each night."

    scene MLR2_MS1_talk_p4
    Mom "Oh... right..."
    Mom "Is it making you jealous that I’m still sleeping with him?"

    window hide
    menu:
        "No, not at all.":


            scene MLR2_MS1_talk_p4

            MC "Honestly, it doesn’t bother me at all."

            scene MLR2_MS1_talk_p8
            if renpy.loadable("patch.rpy"):
                Mom "So… it doesn’t bother you that I have sex with my husband… but you wanted to talk about it?"
            else:
                Mom "So… it doesn’t bother you that I have sex with Bob… but you wanted to talk about it?"
            MC "Uhh…"
            Mom "Can you see where I’m coming from?"
            MC "Kinda…"

            scene MLR2_MS1_talk_p2

            Mom "Anyway, you say it doesn’t bother you - but I’m not planning to have sex with him again, anytime soon."
            Mom "I don’t know if that will put your mind at ease."
            MC "Really? Why?"
            Mom "We just aren’t connecting like we used to."
            jump after_menu_MLR2_MS1_Bob_label
        "Yeah, it really does.":


            scene MLR2_MS1_talk_p4

            MC "Yeah, it’s really making me feel… I don’t know."
            Mom "Jealous?"
            MC "Yeah, I guess so."

            scene MLR2_MS1_talk_p2

            Mom "Well, in that case, I can promise not to do anything for a while."
            Mom "But we can’t leave this as an unresolved issue forever."
            MC "Yeah, I understand that."
            Mom "Good - that shows real maturity, on your part."
            jump after_menu_MLR2_MS1_Bob_label
        "It doesn’t bother me too much.":

            scene MLR2_MS1_talk_p2

            MC "Honestly? It doesn’t bother me too much."

            scene MLR2_MS1_talk_p8

            Mom "Really?"
            MC "Maybe a little bit - but not enough to upset me, or anything."
            Mom "Hmm…"

            scene MLR2_MS1_talk_p2

            Mom "I could give you a trial run of not having sex with him, and see how you feel."
            Mom "Obviously that can’t go on forever, and we’ll need to revisit it. But it might help you make up your mind about what you want."
            if renpy.loadable("patch.rpy"):
                MC "Thanks, Mom."
            else:
                MC "Thanks, Linda."
            jump after_menu_MLR2_MS1_Bob_label

label after_menu_MLR2_MS1_Bob_label:
    scene MLR2_MS1_talk_p8

    Mom "And one last thing..."
    if renpy.loadable("patch.rpy"):
        Mom "How did you know I was still having sex with your father? Our relationship hasn’t been that great lately."
    else:
        Mom "How did you know I was still having sex with Bob? Our relationship hasn’t been that great lately."
    MC "I… uh…"
    Mom "You haven’t been SPYING on us, have you?"
    MC "Ah… I… um… Just an educated guess!"

    scene MLR2_MS1_talk_p4

    Mom "Uh huh. Sure."
    $ MLR2_MS1_NS1 = 3
    $ MLR2_NS2 = True
    jump MLR2_MS1_menu


label MLR2_MS1_Bob_Trip_label:
    scene MLR2_MS1_Bob_p1

    MC "Do you remember what we talked about in the car?"
    Mom "We talked about A LOT of things."

    if renpy.loadable("patch.rpy"):
        MC "About us spending more romantic time together, but Dad being around too much."
    else:
        MC "About us spending more romantic time together, but Bob being around too much."
    MC "Also in that night.. Where you caught me in your room, and we did... some... things..."
    Mom "I know... He was always around... Stopping us."

    scene MLR2_MS1_Bob_p2
    if renpy.loadable("patch.rpy"):
        Mom "Come to think of it… I have an idea. Would you be able to sneak into your Dad’s workplace and check his calendar?"
    else:
        Mom "Come to think of it… I have an idea. Would you be able to sneak into Bob’s workplace and check his calendar?"
    MC "Why?"
    Mom "We can find out when he goes on another of his business trips."
    MC "Ahh! And then we’ll have the house to ourselves!"

    scene MLR2_MS1_Bob_p3

    Mom "Bingo!"
    MC "Why can’t you do it?"
    if renpy.loadable("patch.rpy"):
        Mom "He’ll just get suspicious. When a marriage is slowly failing - things like checking your partner’s schedule become warning signs."
    else:
        Mom "He’ll just get suspicious. When a relationship is slowly failing - things like checking your partner’s schedule become warning signs."
    Mom "And then, when he’s away, we’ll have this wonderful double bed to ourselves."
    Mom "So will you do it, Sweetie?"
    MC "Of course!"
    Mom "Perfect! Do you remember where he works?"
    MC "That big building below the beach?"
    Mom "Yes."
    MC "I'll take care of that. I promise."

    scene MLR2_MS1_kiss_p2

    MC "(Wow! That came out of nowhere!)"
    Mom "Mwah!"

    scene MLR2_MS1_Bob_p3

    Mom "Okay, I have to calm down and concentrate. I have work to do."
    MC "I won’t distract you, then!"
    Mom "Haha! You ALWAYS distract me, Sweetie."
    $ MLR2_MS1_ES3 = 3

    $ Bob_workplace_unlocked = True
    $ Bob_v2_scenes = True
    jump MLR2_MS1_menu

label MLR2_MS1_Bob_Trip2_label:
    scene MLR2_MS1_talk_p1
    if renpy.loadable("patch.rpy"):
        MC "Mom! Good news! Dad goes on a business trip soon!"
    else:
        MC "Linda! Good news! Bob goes on a business trip soon!"
    Mom "Great! How soon?"
    MC "This weekend!"

    scene MLR2_MS1_Bob_p3

    Mom "Brilliant! I can’t wait!"
    Mom "Okay - so here’s the plan. You’re going to come around to my bedroom as soon as he leaves."
    Mom "Then we’ll spend the night, making love in my bed!"
    Mom "I haven’t felt this excited since I was a teenager!"

    scene MLR2_MS1_Bob_p2

    MC "Should I bring you a present or a gift?"
    Mom "Just some red wine. That would be perfect."

    scene MLR2_MS1_Bob_p3
    if renpy.loadable("patch.rpy"):
        MC "Okay, Mom. I’ll make sure to do that."
    else:
        MC "Okay, Linda. I’ll make sure to do that."
    Mom "Yay! This is going to be the best night of my life!"
    MC "(Wow! I’ve never seen anyone this excited about something before! She’s like a child at Christmas!)"
    $ MLR2_MS1_BCalendar = 3
    $ MLR2_weekend_event = True
    jump MLR2_MS1_menu

label MLR2_MS1_Cancel_label:
    scene MLR2_MS1_p2

    Mom "So, would you like me to come to your room tonight?"

    window hide
    menu:
        "Yes.":

            MC "Yes, please!"
            Mom "Okay, I’ll see you tonight, Dear."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ MLR2_Sleep = False
            $ MLR2_can_MS1 = False
            $ can_hide_windows = False
            if Ml_stats_in_your_room < 9999:
                $ Ml_stats_in_your_room += 1
            jump parents_bedroom_morning1
        "Not today.":
            if renpy.loadable("patch.rpy"):
                MC "Not today. I’m a bit tired, Mom."
            else:
                MC "Not today. I’m a bit tired, Linda."
            Mom "Aww, that’s okay. I understand. I hope, tommorow you'll change your mind."
            $ MLR2_Sleep = True
            $ MLR2_can_MS1 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1

label MLR2_R3_MS1_q1:
    scene MLR2_R3_MS1_p1 with dissolve

    MC "Are you missing our holiday at the beach, [Mom_name]? I know I am."
    Mom "Of course I am, Sweetie. It was honestly one of the best days of my life."
    Mom "I’d give anything to relive those memories again. Everything was just so… perfect with you."

    scene MLR2_R3_MS1_p2

    Mom "I may as well have been in heaven, as I lay back on that golden sand."
    Mom "It’s a strange thing to say… but I think I could have died happy, back then. I was completely content, and I’ve never felt that way in my life before."
    Mom "I want to be with you, [player_name]. I want to be with you, and only you."

    scene MLR2_R3_MS1_p3

    MC "I wish that could be true…"
    Mom "What do you mean?"
    MC "[Dad_name]’s still here. Isn’t he? You’re not gonna divorce him, I mightn't be as mature as you guys are, but even I can see you’ll pick him over me. It’s the smart choice."

    scene MLR2_R3_MS1_p4

    Mom "[player_name], what are you talking about?"
    MC "Think about it logically, [Mom_name]. He’s the breadwinner in this house, if you divorce him you’re gonna need to find a way to double your income, if we want to keep living here."
    MC "I mean, how close are you to even paying off the mortgage on this place?"
    MC "And then there’s Sara and Caroline - they’re going to despise you if you kick [Dad_name] out. Then, when they find out I AM the reason why, they’re gonna hate my guts too."

    scene MLR2_R3_MS1_p5

    Mom "[player_name], relax. We’ve almost paid off the mortgage. I think we’ve only got ten thousand dollars or something left. It’ll be gone by the end of the year."
    Mom "And as for Sara and Caroline, leave that to me."
    if renpy.loadable("patch.rpy"):
        Mom "Besides, I haven’t ever said I’m going to divorce or kick out your father. I might not be in love with him anymore, but I wouldn’t kick him to the curb either."
    else:
        Mom "Besides, I haven’t ever said I’m going to divorce or kick out Bob. I might not be in love with him anymore, but I wouldn’t kick him to the curb either."

    scene MLR2_R3_MS1_p6

    Mom "Try to relax, [player_name]. I’m just as nervous as you are - and truth be told, I don’t know what the future holds for any of us."
    Mom "All I know for certain, is that my life has gotten ten times better, with you as a romantic partner. I know I’m treading on fragile ice, but I’m not willing to give you up."
    MC "Thanks, [Mom_name]. I love you."

    scene MLR2_R3_MS1_p7

    Mom "That night we spent together at the beach, has played over and over in my head, on repeat."
    if renpy.loadable("patch.rpy"):
        Mom "I want us to be able to relax together, without having to constantly worry about your father, butting his big head in."
    else:
        Mom "I want us to be able to relax together, without having to constantly worry about Bob, butting his big head in."
    MC "Yeah, that time you threw me off the bed was a real boner killer."

    scene MLR2_R3_MS1_p8

    MC "I don’t remember everything that happened, since I was a little dazed, at you chucking me off the bed. I vaguely recall you tossing a pillow at [Dad_name] though. Did that happen?"
    Mom "Yeah, it was a panicked response. Kinda stupid, in hindsight. But it scared him off, long enough for you to get away."
    MC "True."

    scene MLR2_R3_MS1_p9

    MC "Y’know, that door has a keyhole on it. Why don’t we just lock it, in future?"
    if renpy.loadable("patch.rpy"):
        Mom "Your father has his own copy. Besides, it would only create suspicion if I started locking myself in here, by myself. Your father would probably think I’m preparing divorce papers, in secret."
    else:
        Mom "Bob has his own copy. Besides, it would only create suspicion if I started locking myself in here, by myself. Bob would probably think I’m preparing divorce papers, in secret."
    MC "Yeah… you’re right. Getting away to the beach house was definitely safer."

    scene MLR2_R3_MS1_p10
    if renpy.loadable("patch.rpy"):
        Mom "I know you’re stressed about what’s going to happen to this family. All I can say is… try not to worry."
    else:
        Mom "I know you’re stressed about what’s going to happen to everyone. All I can say is… try not to worry."
    Mom "Nobody can predict the future, and all we can do is try to mitigate the damages, when bad things happen."
    if renpy.loadable("patch.rpy"):
        Mom "I have my own business, and my relationship with your father is on the rocks anyway. If he leaves, we’ll struggle in the short term. I’m like a cat, I always land on my feet."
    else:
        Mom "I have my own business, and my relationship with Bob is on the rocks anyway. If he leaves, we’ll struggle in the short term. I’m like a cat, I always land on my feet."
    MC "Okay, I think that’s what I needed to hear. I was kinda freaking out about this, but I’m feeling a little better now."
    Mom "We’ll do our best to keep our relationship hidden from everyone else, for the meantime."
    MC "Just… uh… if our goal to keep things low-key, maybe don’t try to make me cum, in a restaurant again."
    Mom "Haha! Point taken… but, to be honest, your face was really sweet in that moment..."
    $ MLR2_R3_MS1_q1 = False
    $ MLR2_R3_MS1_talk = True
    $ MLR2_MS1_visit = 4
    $ MLR2_R3_MS1_q2 = True
    $ MLR2_R3_MS1_q3 = True
    $ MLR2_R3_MS1_q4 = True
    jump MLR2_MS1_menu

label MLR2_R3_MS1_q2:
    scene MLR2_MS1_talk_p4

    MC "Listen, [Mom_name]. I’m a little worried about me accidentally getting you pregnant."
    Mom "Goodness me, that’s a heavy question for the morning."
    MC "Heh, I know. Sorry to drop that on you. There really wasn’t an easy way to raise the subject."
    MC "I was just thinking, what if we do it, some day, and… the protection doesn’t work."

    scene MLR2_MS1_talk_p8

    Mom "Put that out of your head, for the meantime. We’ll cross that bridge IF we come to it."
    MC "Are you sure?"

    scene MLR2_MS1_talk_p3

    Mom "Honey, if I don’t look worried about this topic, then you don’t need to be. Okay?"
    MC "Alright, [Mom_name]. If you’re sure."

    $ MLR2_R3_MS1_q2 = False
    jump MLR2_MS1_menu
label MLR2_R3_MS1_q3:
    scene MLR2_MS1_Bob_p2

    MC "Hypothetically speaking, how would you feel about me dating another girl?"
    Mom "..."
    Mom "Are you dating someone?"
    MC "It was a hypothetical question!"

    scene MLR2_MS1_talk_p1

    Mom "Honestly? Not too pleased at all."
    MC "Oh, right…"
    Mom "I mean, am I not enough for you?"
    MC "Of course you are, [Mom_name]! Sorry, it was just a hypothetical."

    $ MLR2_R3_MS1_q3 = False
    jump MLR2_MS1_menu

label MLR2_R3_MS1_q4:
    scene MLR2_MS1_talk_p2

    MC "When did you first develop a crush on me, [Mom_name]?"
    Mom "The first time? Hmm…"

    scene MLR2_MS1_talk_p8

    Mom "It was probably two or three years ago, when I started feeling… urges for you."
    Mom "The romantic attraction came much later."

    scene MLR2_MS1_talk_p4

    Mom "At first, I spent a long time beating myself up over it. It’s hard to describe, in full, just how guilty I felt."
    if renpy.loadable("patch.rpy"):
        Mom "I mean, what kind of mother has THOSE feelings for her own son? Do you know what I mean?"
    else:
        Mom "I mean, what kind of old women has THOSE feelings for so much younger boy? Do you know what I mean?"
    MC "Yeah, I understand, [Mom_name]. I’m sorry you had to go through that."

    scene MLR2_MS1_talk_p2

    Mom "I’m okay now! I went to a professional, back when things were bad. She helped me work through it."
    MC "That’s good to hear. Are you still in therapy? If you don’t mind me asking."
    Mom "Very infrequent sessions. They used to be weekly. The guilt has almost completely gone now."
    MC "That’s good to hear. I’m sorry I never realised this before, [Mom_name]."

    scene MLR2_MS1_talk_p5

    Mom "Shush. You don’t need to be sorry, Sweetie. You were far too young for me, to involve you in my silly romantic interests."
    Mom "Besides, I’m all better now."

    scene MLR2_MS1_Bob_p3

    Mom "Would you mind if we changed the topic?"
    MC "Sorry, yeah, let’s do that."
    $ MLR2_R3_MS1_q4 = False
    jump MLR2_MS1_menu

label MLR2_R3_MS1_q5:

    MC "How would you feel about me dating Sara or Caroline?"
    MC "Of course that’s only a hypothetical question!"

    if renpy.loadable("patch.rpy"):
        Mom "You mean your sisters, Sara and Caroline?"
    else:
        Mom "You mean your roommates, Sara and Caroline?"
    MC "Yeah."

    scene MLR2_MS1_talk_p8

    Mom "I, uh… What a weird question in the morning..."
    Mom "Hmm... Maybe let’s leave that question for another occasion."
    MC "Does that mean, you would be mad?"

    scene MLR2_MS1_talk_p7

    Mom "Mad? No... More like hap- I mean, it’s not the best time to talk about it, first thing in the morning."
    MC "Okay. We can talk about it some other time."
    $ MLR2_R3_MS1_q5 = False
    jump MLR2_MS1_menu

label MLR2_R3_MS1_q6:
    scene MLR2_MS1_Bob_p2
    MC "Umm, if you don’t mind me asking. Have you ever cheated on [Dad_name] before?"
    Mom "Oh goodness, no!"
    if renpy.loadable("patch.rpy"):
        Mom "You were the first time I ever thought about cheating on your father."
    else:
        Mom "You were the first time I ever thought about cheating on Bob."
    MC "Really?!"

    scene MLR2_MS1_talk_p2

    Mom "Don’t look so surprised! It took me almost three years to build up to, finally attempting to kiss you!"
    Mom "Three years of holding back my emotions, while living under the same roof as you. I think I did a pretty damn fine job, no?"
    MC "I guess you’re right."
    $ MLR2_R3_MS1_q6 = False
    jump MLR2_MS1_menu

label MLR2_R3_MS1_q7:
    scene MLR2_MS1_talk_p2

    MC "So, what’s your favourite sex position, [Mom_name]?"
    Mom "Oh, that’s easy. Almost all of them. I like to switch things up."
    Mom "If you ABSOLUTELY FORCED me to choose though, I think I’d have to settle for…"

    scene MLR2_MS1_talk_p5

    Mom "…cowgirl."
    Mom "I just love the sensation of being in control."
    MC "Cowgirl? I think that was our first position at the beach."
    Mom "I know, Sweetie. That’s why it was even more amazing."
    $ MLR2_R3_MS1_q7 = False
    jump MLR2_MS1_menu
label MLR2_R3_MS1_q8:
    scene MLR2_MS1_talk_p4

    MC "Have you ever done anal before, [Mom_name]?"
    Mom "Haha, why do you want to know? Have you been thinking about fucking me in the ass?"
    MC "Maybe, a bit."

    scene MLR2_MS1_talk_p5

    Mom "I think I’ll keep that secret a little longer."
    Mom "Someday you’ll get to find out if I’m a “virgin” back there, but not today."
    MC "Aww…"

    scene MLR2_MS1_talk_p2

    Mom "Haha! Don’t look so downhearted. It’s not like you’ll have to wait MONTHS before we advance to the next stage in our relationship."
    MC "Haha, true. I’d hate to have to wait months, between dates with a girl."
    MC "Anyway, we’ve gotten off topic!"
    $ MLR2_R3_MS1_q8 = False
    jump MLR2_MS1_menu
label MLR2_R3_MS1_q9:
    scene MLR2_MS1_talk_p1

    MC "[Mom_name], why did you lift up Sara’s skirt in the kitchen?"

    scene MLR2_MS1_talk_p2

    Mom "Hehe, I think the question that needs asked here is why were YOU looking up Sara’s skirt?"
    MC "I… uh… I wasn’t!"
    Mom "Haha! Of course you were! Nobody takes that long to pick a can!"

    scene MLR2_MS1_talk_p5

    Mom "And… as for why I did it? Did you not enjoy the show?"
    MC "Heh, yeah, I guess I did… but-"
    Mom "See? Everything worked out perfectly then."

    $ MLR2_R3_MS1_q9 = False
    jump MLR2_MS1_menu