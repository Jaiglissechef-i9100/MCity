image LiR1_MAS3_p1 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/1.jpg"
image LiR1_MAS3_p2 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/2.jpg"
image LiR1_MAS3_p3 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/3.jpg"
image LiR1_MAS3_p4 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/4.jpg"
image LiR1_MAS3_p5 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/5.jpg"
image LiR1_MAS3_p6 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/6.jpg"
image LiR1_MAS3_p7 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/7.jpg"
image LiR1_MAS3_p8 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/8.jpg"
image LiR1_MAS3_p9 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/9.jpg"
image LiR1_MAS3_p10 = "/images/a_home/Inside/Office/M/scenes/LiR1_MAS3/10.jpg"

label Li_MAS3_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene LiR1_MAS3_p1 with dissolve

    Yazmin "Hey there, [player_name]. What’s up?"
    MC "I just thought I’d drop by to say hello. Are you free for a few minutes?"
    Yazmin "Of course! I just finished, booking a course. What can I do for you?"

    jump Li_MAS3_menu

label Li_MAS3_menu:
    scene LiR1_MAS3_p1
    menu:
        "What’s it like, working as a supermodel?" if Li_MAS3_q1 == True:
            scene LiR1_MAS3_p3

            MC "So, what’s it like, working as a supermodel?"

            scene LiR1_MAS3_p6

            Yazmin "Supermodel?! Haha! God, I wish I was one!"
            Yazmin "That’s a bit of an exaggeration. Honestly, I’m not that famous... yet. I’ll get there, someday. But right now, I’m just your - regular old - fashion model."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q1 = False
            jump Li_MAS3_menu

        "Have you always been a model?" if Li_MAS3_q2 == True:
            scene LiR1_MAS3_p3
            MC "Have you always been a fashion model?"


            scene LiR1_MAS3_p5

            Yazmin "Hmm... Not always. I started in my early twenties - after college."
            Yazmin "I also held a couple of other jobs, when I was younger. When I was twenty, I worked for a congressman, for six months."
            MC "That’s pretty cool! What did you do for him?"
            Yazmin "Public relations, accompanied him to formal events, some light secretarial stuff."

            scene LiR1_MAS3_p4

            Yazmin "Honestly - I left because he was using me as - eye candy - rather than as an actual employee. Not that I mind being eye-candy, I just really needed proper work experience, and I wasn’t getting it."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q2 = False
            jump Li_MAS3_menu

        "Where’s your favourite place?" if Li_MAS3_q3 == True:
            scene LiR1_MAS3_p3

            MC "Where’s your favourite place?"

            scene LiR1_MAS3_p4

            Yazmin "My favourite place? What do you mean?"
            MC "Y’know - I’m sure you’ve travelled around, a lot. Where’s your favourite city or country?"
            Yazmin "What a bizarre question. Are you usually this bad at small talk?"
            MC "Yeah, I guess so."

            scene LiR1_MAS3_p7

            Yazmin "Fine. Let me think... Hmm..."
            Yazmin "I travelled to so many places, after I turned eighteen. I’m struggling to remember - half of them! Granted... I was rather drunk, for a lot of them."

            scene LiR1_MAS3_p8

            Yazmin "Barcelona! Yeah, that’s where I enjoyed, the most."
            MC "What’s in Barcelona?"
            Yazmin "It’s a city in Catalonia in Spain. Absolutely stunning city! It’s filled with all this really old architecture - if you’re into that kinda thing."
            Yazmin "Plus - Spanish guys are soooo hot! I had a couple of amazing... ‘encounters’ in youth hostels."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q3 = False
            jump Li_MAS3_menu

        "What’s it like, working on the catwalk?" if Li_MAS3_q4 == True:
            scene LiR1_MAS3_p3

            MC "What’s it like, working on the catwalk?"

            scene LiR1_MAS3_p2

            Yazmin "Honestly? It’s far less glamorous, than you would imagine."
            MC "Really?"
            Yazmin "When you turn on the TV and see a girl walking down the runway, or when you look at a beautiful woman in an advertisement, you’re only seeing the very end of the process."
            Yazmin "Prior to that, is hours, or even days - of excruciatingly difficult work."
            MC "Like what?"
            Yazmin "Exercising, having clothes fitted and refitted, DOZENS of rejected photoshoots and retries! It’s an exhausting process."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q4 = False
            jump Li_MAS3_menu

        "What did you study at college?" if Li_MAS3_q5 == True:
            scene LiR1_MAS3_p3

            MC "What did you study at college?"

            scene LiR1_MAS3_p6

            Yazmin "I did a - joint major - at a small regional college, down in Texas - Art and Public Relations. I loved the art part. Absolutely HATED the public relations half of my degree, though."
            MC "That sounds cool! What kind of art did you do?"
            Yazmin "Mostly photography stuff. It’s how I met most of my contacts, for my current job."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q5 = False
            jump Li_MAS3_menu

        "I don’t see you and Auntie Liza coming to visit, very often. Why is that?" if Li_MAS3_q6 == True and renpy.loadable("patch.rpy"):
            scene LiR1_MAS3_p3

            MC "I don’t see you and Auntie Liza coming up to visit us, very often. Why is that?"


            scene LiR1_MAS3_p7

            Yazmin "Ooh, that’s a touchy subject. Honestly, I’m not comfortable talking about this. It’s something you’d need to take up with your auntie."
            Yazmin "Let’s just say... your mother isn’t my biggest fan."


            MC "(Yikes... It sounds like I’ve touched a nerve here!)"

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q6 = False
            jump Li_MAS3_menu

        "I don’t see you and Liza coming to visit, very often. Why is that?" if Li_MAS3_q6 == True and not renpy.loadable("patch.rpy"):

            scene LiR1_MAS3_p3

            MC "I don’t see you and Liza coming up to visit us, very often. Why is that?"

            scene LiR1_MAS3_p7

            Yazmin "Ooh... that’s a touchy subject. Honestly, I’m not comfortable talking about this. It’s something you’d need to take up with Liza."
            Yazmin "Let’s just say... Linda isn’t my biggest fan."

            MC "(Yikes... It sounds like I’ve touched a nerve here!)"

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q6 = False
            jump Li_MAS3_menu

        "It’s a personal question - but does being a model pay well?" if Li_MAS3_q7 == True:
            scene LiR1_MAS3_p3

            MC "It’s a personal question - but does being a model pay well?"

            scene LiR1_MAS3_p8

            Yazmin "Ahahaha! It SHOULD! But there are some crazy stories I could tell you!"
            MC "Go on! Tell me some!"


            scene LiR1_MAS3_p4

            Yazmin "There are a lot of designers and companies out there, who try to get girls like me, to model for free."
            Yazmin "“How would you like to be the new face of our exclusive line of dresses? We can’t pay you right now, but think of the exposure you’ll get, for your portfolio!”"
            MC "Really?!"


            scene LiR1_MAS3_p2

            Yazmin "A lot of people don’t realise, that being an artist or a model is a full time job. They seem to have this opinion that they are entitled to take photos of us, and use them for free. It’s only gotten worse, with the rise of the internet."
            MC "Damn. I’m sorry to hear that."
            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q7 = False
            jump Li_MAS3_menu

        "Are you and [Liza2_name] thinking of trying for kids in the future?" if Li_MAS3_q8 == True:
            scene LiR1_MAS3_p3

            MC "Are you and [Liza2_name] thinking of trying for kids in the future?"

            scene LiR1_MAS3_p5

            Yazmin "You mean, though IVF or a sperm donor?"
            MC "Yeah. Either way."
            Yazmin "Maybe? I haven’t put a lot of thought into it. I obviously need to find a really good guy, who would want to donate to us."
            if renpy.loadable("patch.rpy"):
                Yazmin "And then there’s the issue about which of us would carry the baby. I don’t know if your auntie would be too fond of it - And I certainly can’t, or my modelling career would be put on hold, for several months!"
            else:
                Yazmin "And then there’s the issue about which of us would carry the baby. I don’t know if Liza would be too fond of it - and I certainly can’t, or my modelling career would be put on hold, for several months!"

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q8 = False
            jump Li_MAS3_menu

        "Why doesn’t my mother like you?" if Li_MAS3_q9 == True and renpy.loadable("patch.rpy"):
            scene LiR1_MAS3_p3

            MC "Why doesn’t my mother like you?"

            scene LiR1_MAS3_p4

            Yazmin "It’s a loooong story. Your mom hasn’t always had the friendliest of relationships with gay people - like your auntie. She didn’t approve of our “lifestyle”."
            Yazmin "I think your mother had a few lesbian flings, in her younger days - but she always sort of viewed women as fun, rather than the basis for a permanent relationship."

            scene LiR1_MAS3_p5

            Yazmin "Then - I came into the picture - and started dating her sister. Prior to me coming along - your mother and Liza were inseparable. They might has well have been best friends."
            Yazmin "Your mother has mellowed, in recent years, but it’s still left some open wounds between her and your auntie. I think she still views me - as stealing Liza away from her."
            MC "Fuck... I’m sorry... I never knew she was like that..."

            scene LiR1_MAS3_p7

            Yazmin "Don’t take it to heart. Your mother is NOT a bad person. People are complex individuals. And trying to fit them into narrow categories of ‘good’ and ‘bad’..."
            Yazmin "Your mother, clearly experienced some kind of emotional agony when I dated - and later married - her sister."
            Yazmin "She - evidently - isn’t over it yet. But rather than see a therapist, she seems to be redirecting her frustration towards gay people and bisexuals, like myself."
            MC "Do you want me to talk to-"
            Yazmin "Absolutely not! DO NOT bring this up with her. I have been walking a - very fine tightrope - for months, on this subject. Please don’t endanger - the little amount of progress - I have made."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q9 = False
            jump Li_MAS3_menu

        "Why doesn’t Linda like you?" if Li_MAS3_q9 == True and not renpy.loadable("patch.rpy"):
            scene LiR1_MAS3_p3

            MC "Why doesn’t my Linda like you?"

            scene LiR1_MAS3_p4

            Yazmin "It’s a loooong story. Linda hasn’t always had the friendliest of relationships with gay people - like Liza. She didn’t approve of our “lifestyle”."
            Yazmin "I think Linda had a few lesbian flings, in her younger days - but she always sort of viewed women as fun, rather than the basis for a permanent relationship."

            scene LiR1_MAS3_p5

            Yazmin "Then - I came into the picture - and started dating with Liza. Prior to me coming along - Linda and Liza were inseparable. They might has well have been best friends."
            Yazmin "Linda has mellowed, in recent years, but it’s still left some open wounds between her and Liza. I think she still views me - as stealing Liza away from her."
            MC "Fuck... I’m sorry... I never knew she was like that..."

            scene LiR1_MAS3_p7

            Yazmin "Don’t take it to heart. Linda is NOT a bad person. People are complex individuals. And trying to fit them into narrow categories of ‘good’ and ‘bad’..."
            Yazmin "She has clearly experienced some kind of emotional agony when I dated, and later married - her very close friend."
            Yazmin "She - evidently - isn’t over it yet. But rather than see a therapist, she seems to be redirecting her frustration towards gay people and bisexuals, like myself."
            MC "Do you want me to talk to-"
            Yazmin "Absolutely not! DO NOT bring this up with her. I have been walking a - very fine tightrope - for months, on this subject. Please don’t endanger the - little amount of progress - I have made."

            if can_LiR1_MAS3 == True:
                $ Li_MAS3_menu_visit += 1
                $ can_LiR1_MAS3 = False

            $ Li_MAS3_q9 = False
            jump Li_MAS3_menu

        "Bye." if Li_MAS3_menu_visit >1:
            scene LiR1_MAS3_p8

            MC "Well, I’ve taken up enough of your time. I should probably head on."
            Yazmin "No problem, kiddo. I’m sure we’ll chat again soon."

            scene LiR1_MAS3_p9

            Yazmin "(And maybe - if I’m lucky, I’ll see you with less clothes, the next time!)"
            Yazmin "(God... it’s been so long since I’ve been able to fuck a man. I could just strip him down, right here, plant him in my chair, and ride his cock, till he came inside me.)"

            scene LiR1_MAS3_p10

            Yazmin "(Dammit Yazmin! You need to calm down. You’ve still got preparation to do, before your next photoshoot!)"
            Yazmin "(Okay, now where was I, before I left off...)"

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump a_office_M1