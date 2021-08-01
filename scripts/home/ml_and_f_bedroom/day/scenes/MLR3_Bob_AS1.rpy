image MLR3_Bob_AS1_p1 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/1.jpg"
image MLR3_Bob_AS1_p2 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/2.jpg"
image MLR3_Bob_AS1_p3 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/3.jpg"
image MLR3_Bob_AS1_p4 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/4.jpg"
image MLR3_Bob_AS1_p5 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/5.jpg"
image MLR3_Bob_AS1_p6 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/6.jpg"
image MLR3_Bob_AS1_p7 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/7.jpg"
image MLR3_Bob_AS1_p8 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/8.jpg"
image MLR3_Bob_AS1_p9 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/9.jpg"
image MLR3_Bob_AS1_p10 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/10.jpg"
image MLR3_Bob_AS1_p11 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/11.jpg"
image MLR3_Bob_AS1_p12 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/12.jpg"
image MLR3_Bob_AS1_p13 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/13.jpg"
image MLR3_Bob_AS1_p14 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/14.jpg"
image MLR3_Bob_AS1_p15 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/15.jpg"
image MLR3_Bob_AS1_p16 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/16.jpg"
image MLR3_Bob_AS1_p17 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/17.jpg"
image MLR3_Bob_AS1_p18 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/18.jpg"

image MLR3_Bob_Trip_AS1_p1 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/1.jpg"
image MLR3_Bob_Trip_AS1_p2 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/2.jpg"
image MLR3_Bob_Trip_AS1_p3 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/3.jpg"
image MLR3_Bob_Trip_AS1_p4 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/4.jpg"
image MLR3_Bob_Trip_AS1_p5 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/5.jpg"
image MLR3_Bob_Trip_AS1_p6 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/6.jpg"
image MLR3_Bob_Trip_AS1_p7 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/7.jpg"
image MLR3_Bob_Trip_AS1_p8 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/8.jpg"
image MLR3_Bob_Trip_AS1_p9 = "/images/home/ml_and_f_bedroom/day/scenes/MLR3_Bob_AS1/Trip/9.jpg"

label MLR3_Bob_AS1:
    hide screen displayTextScreen
    hide screen map_button
    if MLR3_Bob_AS1_can == False:
        show screen parents_bedroom_day
        $ clickable = False
        MC "I've already talked with him."
        $ clickable = True
        hide screen parents_bedroom_day
        jump parents_bedroom_morning1
    else:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        if MLR3_Bob_AS1 == 1:
            scene MLR3_Bob_AS1_p1 with dissolve

            MC "(Looks like [Dad_name] just got out of the shower.)"
            MC "Hey [Dad_name], what’s up?"

            scene MLR3_Bob_AS1_p2

            Dad "Oh, hey there, [player_name]. Nothing much. Just chilling."
            Dad "Something I can help you with?"
            MC "I just wanted to chat with you about a few things."

            scene MLR3_Bob_AS1_p3
            if persistent.incest_patch == True:
                Dad "Ahh, some father-son time."
            else:
                Dad "Some quality time with your father-figure."
            Dad "I’ll tell you what - grab me a cigar from beside my bed, then you and me will have a good chat."
            MC "No problem, [Dad_name]."

            scene MLR3_Bob_AS1_p4

            MC "(This looks like his cigar box here. I know [Mom_name] hates it when he smokes these in the house.)"

            scene MLR3_Bob_AS1_p5

            MC "Any one at all, [Dad_name]?"
            Dad "Yeah, they are all the same. Sometimes I’ll get a few special ones ordered, from Cuba. But right now, I’m down to the local cigars."

            scene MLR3_Bob_AS1_p6

            MC "(I don’t get why [Dad_name] likes these so much. They look awful, and smell even worse.)"
            MC "(Maybe I’ll ask him about it someday.)"

            scene MLR3_Bob_AS1_p7

            MC "(This one will do.)"
            Dad "Did you find them, there?"
            MC "Yeah, got one. Coming back now, [Dad_name]."

            scene MLR3_Bob_AS1_p8

            Dad "Top notch! Thanks, [player_name]."
            MC "No problem, [Dad_name]."

            scene MLR3_Bob_AS1_p9

            Dad "So… *Puff* What was it you wanted to ask me?"
            Dad "I’m all ears."

            jump MLR3_Bob_AS1_menu
        if MLR3_Bob_AS1 == 2:
            $ MLR3_Bob_AS1_q4 = True
            $ MLR3_Bob_AS1_q5 = True
            $ MLR3_Bob_AS1_q6 = True
            $ MLR3_Bob_AS1_q8 = True
            jump MLR3_Bob_AS1_menu
        if MLR3_Bob_AS1 == 3:
            scene MLR3_Bob_AS1_p3

            Dad "Hey again, [player_name]. Grab me another cigar, would you? I’ve got a few questions for you today."
            MC "Oh, sure, [Dad_name]!"

            scene MLR3_Bob_AS1_p8

            Dad "Thanks, [player_name]."
            MC "(I wonder what [Dad_name] wants to ask me about.)"

            scene MLR3_Bob_AS1_p9

            Dad "*Puff*"
            MC "(Those cigars really do stink! No wonder they drive [Mom_name] crazy!)"
            scene MLR3_Bob_AS1_p10
            Dad "So, girls… Have you got your eye on one yet?"
            menu:
                "Yeah, I’ve got my eye on one.":
                    scene MLR3_Bob_AS1_p14

                    MC "Yeah, I’ve got my eye on one, [Dad_name]."
                    Dad "Ohh, lucky lady! I’ll have to hear more about her!"

                    $ MLR3_Bob_AS1_answer += 1
                    jump MLR3_Bob_AS1_menu2
                "No, not yet.":
                    scene MLR3_Bob_AS1_p11

                    MC "No, not yet, [Dad_name]."
                    Dad "Oh… Shame. You’re at the prime of your life right now. Try now to waste your youth."
                    Dad "Get out there and meet some people. I’m sure there’s dozens of women that are dying to meet you!"

                    $ MLR3_Bob_AS1_answer += 1
                    jump MLR3_Bob_AS1_menu
                "I’ve met a few I like.":
                    scene MLR3_Bob_AS1_p15

                    MC "I’ve met a few girls that I like."
                    Dad "A few?! Now we’re talking! Let’s hear some stuff about them!"

                    $ MLR3_Bob_AS1_answer += 1
                    jump MLR3_Bob_AS1_menu2
        if MLR3_Bob_AS1 == 4:
            scene MLR3_Bob_AS1_p10

            Dad "Hey again, [player_name]. I forgot to ask you the last time we met - think of your ideal woman."
            MC "Okay?"
            Dad "What kinda rack does she have?"
            MC "Hmm…"
            menu:
                "Massive tits!":
                    scene MLR3_Bob_AS1_p17

                    MC "Honestly, the bigger the better!"
                    if persistent.incest_patch == True:
                        Dad "Nice! Good man! That’s just another reason I fell in love with your mother: her tits are amazing!"
                    else:
                        Dad "Nice! Good man! That’s just another reason I fell in love with Linda: her tits are amazing!"
                    MC "I know!"

                    scene MLR3_Bob_AS1_p16
                    if persistent.incest_patch == True:
                        Dad "… Did you just say, you know that your own mother’s tits are amazing?"
                        MC "Uh… (FUCK!) N-No! I meant… I know that… you are… in love with Mom for many reasons!"
                    else:
                        Dad "… Did you just say you know that Linda’s tits are amazing?"
                        MC "Uh… (FUCK!) N-No! I meant… I know that… you are… in love with Linda for many reasons!"
                    scene MLR3_Bob_AS1_p15

                    Dad "Ahh! That makes sense! Haha! We had a breakdown in communication there!"
                    jump MLR3_Bob_AS1_menu3
                "Average sized breasts.":
                    scene MLR3_Bob_AS1_p15

                    MC "Honestly, not too big, not to small."
                    Dad "I can respect that. Are we talking a C/D cup?"
                    MC "Yeah, about that."
                    jump MLR3_Bob_AS1_menu3
                "I like really small breasts, an A or B cup.":
                    scene MLR3_Bob_AS1_p16

                    MC "I really like small breasts: an A or B cup."
                    Dad "Really? Small breasts? Huh? I never pictured you for a tiny tits guy."
                    Dad "Don’t take this the wrong way, but are we talking the size of Sara’s?"
                    MC "Yeah, about that size is good."
                    Dad "Huh, different strokes for different folks, I guess!"
                    jump MLR3_Bob_AS1_menu3
        if MLR3_Bob_AS1 > 4:
            jump MLR3_Bob_AS1_menu

label MLR3_Bob_AS1_menu3:
    scene MLR3_Bob_AS1_p15

    Dad "What about the ideal age?"
    MC "Hmm…"
    menu:
        "I like them more mature than me.":
            scene MLR3_Bob_AS1_p17

            MC "I like my women a bit more mature than me."
            Dad "Ahh, you’re into MILFs. I remember I was too, at your age."
            Dad "I had a wonderful few encounters with a Ms. Bridgend, during my time working in Scotland. Wonderful lady - amazing skils with her mouth."
            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu
        "I like them to be around my age.":
            scene MLR3_Bob_AS1_p15

            MC "I like them to be around my age. Maybe a couple of years either side."
            Dad "That’s fair enough. A healthy attitude to have. It means you’re both of a similar level of maturity too, for relationships."

            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu
        "I like my women a little bit younger than me.":

            scene MLR3_Bob_AS1_p18

            MC "I like my women a little bit younger than me."
            Dad "A little younger? Sara’s age?"
            MC "Yeah, around that."

            scene MLR3_Bob_AS1_p15

            Dad "I guess you can’t beat wild sex with a teenager!"
            Dad "You must be SPOILED for choice with all those girls at your school!"

            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu

label MLR3_Bob_AS1_menu2:
    scene MLR3_Bob_AS1_p18
    Dad "So, what kinda hair colour do you go for in women?"
    menu:
        "Blondes.":
            MC "I’m quite fond of blondes, [Dad_name]."
            Dad "Ahh, I’m sure there’s quite a few blonde girls at your school!"
            MC "Yeah, there’s a couple!"
            jump MLR3_Bob_AS1_menu
        "Brunettes.":
            scene MLR3_Bob_AS1_p17

            MC "I’m more into brunettes."
            Dad "Oh yeah? Like Caroline?"
            MC "Wh-What?!"

            scene MLR3_Bob_AS1_p16

            Dad "Oops! I meant Caroline’s hair colour. Sorry, that came out wrong!"
            MC "Uh, yeah, brunette like her. Maybe a bit lighter."

            jump MLR3_Bob_AS1_menu
        "Gingers.":
            scene MLR3_Bob_AS1_p15

            MC "Gingers and redheads are my thing."
            Dad "Ohh, like bright ginger, or more muted like Sara’s hair?"
            MC "Either. I’m not really fussy."

            jump MLR3_Bob_AS1_menu
        "Black Hair":

            MC "I like really dark hair, almost black."
            if persistent.incest_patch == True:
                Dad "Ahh, same as me. That’s one of the many reasons I fell for your mother!"
            else:
                Dad "Ahh, same as me. That’s one of the many reasons I fell for Linda!"
            jump MLR3_Bob_AS1_menu

label MLR3_Bob_AS1_menu:
    if MLR3_Bob_AS1_q1 == False and MLR3_Bob_AS1_q2 == False and MLR3_Bob_AS1_q3 == False and MLR3_Bob_AS1_q4 == False and MLR3_Bob_AS1_q5 == False and MLR3_Bob_AS1_q6 == False:
        $ MLR3_Bob_AS1_answer += 1
    scene MLR3_Bob_AS1_p10

    menu:
        "{color=#00ff00}Talk about the trip.{/color}" if MLR3_Bob_AS1_q7 == True:
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)

            scene MLR3_Bob_Trip_AS1_p1

            MC "Hey, [Dad_name]. Can I steal you for a minute?"
            Bob "Hmm? Sure, champ. What’s up?"
            MC "I just got an exemption for school for a one day trip."

            scene MLR3_Bob_Trip_AS1_p2

            Bob "A school trip, eh? What’s it for?"
            MC "Umm… team building and leadership skills, I think."
            Bob "Hmm, that’s a good course to be on. Employers REALLY value strong team players. I’m glad to see you going on this, son. You’re staying overnight as well?"
            MC "Yeah, we’re staying overnight and coming back the day after."

            scene MLR3_Bob_Trip_AS1_p3

            Bob "So, is this a guy’s only trip, then? Or are there gonna be a few girls there too?"
            MC "I, uh… I’m not sure."
            Bob "Ahh c’mon, you can tell me!"

            scene MLR3_Bob_Trip_AS1_p4

            MC "Yeah, there’s… there’s probably gonna be at least one woma- girl there too."
            Bob "You know, I remember going on these when I was your age. These field trips are great for hooking up with your classmates."
            Bob "Why, I remember cuddling up with this ginger bombshell on a bus trip to the Grand Canyon. We had this blanket over us."

            scene MLR3_Bob_Trip_AS1_p5

            Bob "I must have fingered her, half the way there. She was trembling and shaking, trying not to moan, in a bus full of fellow classmates."
            Bob "She was kind enough to return the favour on the way back home! Heh heh!"
            Bob "Now, where did I leave it? I could have sworn I set it down here…"

            scene MLR3_Bob_Trip_AS1_p6

            Bob "Aha! Here we go! This is for you!"
            MC "What is it?"

            scene MLR3_Bob_Trip_AS1_p7

            Bob "It’s a condom - I know what lads your age are like. Heck, I was your age once!"
            Bob "Abstinence only sex education, is horse shit. Anyone with half a brain knows that. If anything happens, and I’m keeping my fingers crossed for you that it does, make sure you use this."
            MC "[Dad_name], I-"

            scene MLR3_Bob_Trip_AS1_p8

            Bob "Go and get yourself laid, [player_name]."

            MC "What about you? Do you not need it?"
            if persistent.incest_patch == True:
                Bob " Relax, I’ve got plenty. Plus, your mother is also away on some business trip. Ironically, it's the same time as yours, so I’ve got no use for it at all."
            else:
                Bob " Relax, I’ve got plenty. Plus, Linda is also away on some business trip. Ironically, it's the same time as yours, so I’ve got no use for it at all."

            scene MLR3_Bob_Trip_AS1_p9

            Bob "Oh, and before you go - remember the two rules of safe sex."
            Bob "One: always use protection, and two: don’t pressure someone into doing something they don’t want to do."
            Bob "If you follow those two rules, you’ll keep yourself safe. As for actually picking up chicks - a guy who looks like you should have no problem at all. Good luck, [player_name]."
            MC "Thanks, [Dad_name]… (I guess.)"

            $ inventory.add(condom)
            $ inventory.drop(permission)
            $ MLR3_Bob_AS1_q7 = False
            $ MLR3_beach_event = True
            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu
        "{color=#00ff00}Why were you yelling at [Mom_name]? Are you planning to get a divorce?{/color}" if MLR3_Bob_AS1_q8 == True:
            scene MLR3_Bob_AS1_p11

            MC "Why were you yelling at [Mom_name]? You two aren’t planning to get divorced, are you?"
            Dad "I uh… well…"
            if persistent.incest_patch == True:
                Dad "There’s a lot of complex issues going on between your mother and me right now."
            else:
                Dad "There’s a lot of complex issues going on between Linda and me right now. "
            scene MLR3_Bob_AS1_p14

            MC "Like what?"
            Dad "It’s… ah… bedroom stuff. Not really appropriate to talk about with you. Sorry."

            scene MLR3_Bob_AS1_p15

            Dad "To answer your second question though - no. There are NO divorce plans on the table."
            Dad "We’re both mature adults and we’re going to work through this. "

            scene MLR3_Bob_AS1_p16
            if persistent.incest_patch == True:
                Dad "At least… we will when your mother finally agrees to go to mediation and therapy with me."
            else:
                Dad "At least… we will when Linda finally agrees to go to mediation and therapy with me."
            Dad "She can be very stubborn. A real wild stallion!"
            $ MLR3_Bob_AS1_q8 = False
            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu

        "Could you give me some advice for finding a girlfriend? I’m worried that a girl I like isn’t interested in me." if MLR3_Bob_AS1_q1 == True:

            MC "Could you give me some advice for finding a girlfriend? I’m worried that a girl I like isn’t interested in me."
            Dad "Oh, so there IS a girl you like. That’s good!"

            scene MLR3_Bob_AS1_p11

            Dad "Hmm, if she isn’t interested in you, then there really isn’t much you can do. If you’ve already tried speaking with her."
            Dad "I suppose it wouldn’t hurt, formally asking her to go out for dinner or drinks, and see how she reacts. Perhaps she just doesn’t know that you like her."

            scene MLR3_Bob_AS1_p12

            MC "Or the cinema?"
            Dad "*Puff*"

            scene MLR3_Bob_AS1_p13

            Dad "Oh, God no. The cinema is an awful first date idea. The two of you can’t speak during the movie."
            Dad "It means you never properly break the ice. Hold off on the cinema until the two of you have gone on a few dates."
            MC "Ahh, that’s good advice."

            scene MLR3_Bob_AS1_p14

            Dad "If she isn’t interested in you, or doesn’t want to date… well… I’m afraid you’re just going to have to man up and move on."
            Dad "There’s billions of women in the world. Just because the chemicals in your brain make you think she’s the one, doesn’t make it necessarily true."
            MC "Thanks, [Dad_name]."

            $ MLR3_Bob_AS1_q1 = False
            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu

        "Why do you always smoke cigars?" if MLR3_Bob_AS1_q2 == True:

            scene MLR3_Bob_AS1_p12

            MC "Why do you always smoke cigars?"
            Dad "*Puff*"

            scene MLR3_Bob_AS1_p13

            Dad "Why do you play computer games?"
            Dad "It’s just a way for me to kick back and relax."

            scene MLR3_Bob_AS1_p14

            MC "Are you not worried that you might be addicted to the nicotine?"
            Dad "Haha, there’s a MASSIVE difference between cigars and cigarettes. With cigars, you draw the smoke into your mouth, taste the flavours, and then exhale."
            Dad "I’ll let you try one, someday - these ones might be a little too strong for a first try."

            $ MLR3_Bob_AS1_q2 = False
            $ MLR3_Bob_AS1_answer += 1
            jump MLR3_Bob_AS1_menu

        "What did you think of Caroline opening up her own shop?" if MLR3_Bob_AS1_q3 == True:
            scene MLR3_Bob_AS1_p15

            MC "What did you think of Caroline opening up her own shop?"

            if persistent.incest_patch == True:
                Dad "I’m a capitalist, at heart. And nothing makes my heart beat prouder, than seeing my own daughter, launch her own business."
            else:
                Dad "I’m a capitalist, at heart. And nothing makes my heart beat prouder, than seeing someone I saw growing up, launch her own business."
            if Caroline_points == 2:
                scene MLR3_Bob_AS1_p17

                Dad "Oh, I heard through the grapevine that YOU’VE been helping her."
                if persistent.incest_patch == True:
                    Dad "Nice work, champ! Doing your old man proud. You always gotta stick by your siblings. They’ll be with you longer than your mother or I will."
                else:
                    Dad "Nice work, [player_name]! Doing me proud. You always gotta stick by your siblings. They’ll be with you longer than Linda or I will."
                $ MLR3_Bob_AS1_q3 = False
                $ MLR3_Bob_AS1_answer += 1

                jump MLR3_Bob_AS1_menu
            else:
                $ MLR3_Bob_AS1_q3 = False
                $ MLR3_Bob_AS1_answer += 1

                jump MLR3_Bob_AS1_menu
        "How did you and [Mom_name] meet?" if MLR3_Bob_AS1_q4 == True:
            scene MLR3_Bob_AS1_p13

            MC "How did you and [Mom_name] meet?"

            Dad "How did we meet? God… We met at a young business leaders conference in Vienna."

            scene MLR3_Bob_AS1_p15
            if persistent.incest_patch == True:
                Dad "It was an international event for young entrepreneurs under twenty five. Your mom and I hit it off on the first night of the conference."
            else:
                Dad "It was an international event for young entrepreneurs under twenty five. Linda and I hit it off on the first night of the conference."
            Dad "We lived on opposite sides of the country, but we kept in touch after the conference and eventually found our way back together."

            $ MLR3_Bob_AS1_q4 = False
            $ MLR3_Bob_AS1_answer += 1

            jump MLR3_Bob_AS1_menu
        "When did you fall in love with [Mom_name]?" if MLR3_Bob_AS1_q5 == True:
            scene MLR3_Bob_AS1_p16

            MC "When did you fall in love with [Mom_name]?"
            Dad "God… that’s a tough one. It just sorta naturally evolved over time. I can’t put a specific date on it."
            Dad "I remember the first time I told her. It was in Times Square, New York. She was holding my hand as we walked under the neon lights and flashing billboards."

            scene MLR3_Bob_AS1_p18

            Dad "Her eyes were so beautiful. I grabbed her and spilled my heart out to her."
            Dad "Turns out she felt the same way!"
            $ MLR3_Bob_AS1_q5 = False
            $ MLR3_Bob_AS1_answer += 1

            jump MLR3_Bob_AS1_menu

        "What did you do to win [Mom_name] over?" if MLR3_Bob_AS1_q6 == True:
            scene MLR3_Bob_AS1_p15

            MC "What did you do to win [Mom_name] over?"
            if persistent.incest_patch == True:
                Dad "Your mother was a tough cookie, at first. I’m not gonna lie: she turned me down when I asked her out for drinks, at first."
            else:
                Dad "Linda was a tough cookie, at first. I’m not gonna lie: she turned me down when I asked her out for drinks, at first."
            Dad "It wasn’t until I saw her getting harassed by a creep, at the bar in Vienna, that things kicked off."
            MC "What did you do?!"
            Dad "I went up to him, shook his hand, and introduced myself as her boyfriend."
            Dad "The creep quickly backed down."
            MC "You didn’t fight him?"

            scene MLR3_Bob_AS1_p16

            Dad "Not everything needs to be solved with violence. You can talk people down, or just bluff them into backing off ninety nine percent of the time."
            Dad "Try it sometime - life isn’t a video game where you need to go punching everyone! Haha!"
            $ MLR3_Bob_AS1_q6 = False
            $ MLR3_Bob_AS1_answer += 1

            jump MLR3_Bob_AS1_menu
        "Bye.":

            if MLR3_Bob_AS1_answer > 0:
                $ MLR3_Bob_AS1 += 1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            $ MLR3_Bob_AS1_answer = 0
            $ MLR3_Bob_AS1_can = False
            jump parents_bedroom_morning1

