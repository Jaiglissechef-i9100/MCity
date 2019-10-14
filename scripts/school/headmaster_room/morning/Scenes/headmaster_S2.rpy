image headmaster_S2_p1 = "images/school/headmaster_room/morning/S2/1.jpg"
image headmaster_S2_p2 = "images/school/headmaster_room/morning/S2/2.jpg"
image headmaster_S2_p3 = "images/school/headmaster_room/morning/S2/3.jpg"
image headmaster_S2_p4 = "images/school/headmaster_room/morning/S2/4.jpg"
image headmaster_S2_p5 = "images/school/headmaster_room/morning/S2/5.jpg"
image headmaster_S2_p6 = "images/school/headmaster_room/morning/S2/6.jpg"
image headmaster_S2_p7 = "images/school/headmaster_room/morning/S2/7.jpg"
image headmaster_S2_p8 = "images/school/headmaster_room/morning/S2/8.jpg"
image headmaster_S2_p9 = "images/school/headmaster_room/morning/S2/9.jpg"
image headmaster_S2_p10 = "images/school/headmaster_room/morning/S2/10.jpg"
image headmaster_S2_p11 = "images/school/headmaster_room/morning/S2/11.jpg"
image headmaster_S2_p12 = "images/school/headmaster_room/morning/S2/12.jpg"
image headmaster_S2_p13 = "images/school/headmaster_room/morning/S2/13.jpg"
image headmaster_S2_p14 = "images/school/headmaster_room/morning/S2/14.jpg"
image headmaster_S2_p15 = "images/school/headmaster_room/morning/S2/15.jpg"
image headmaster_S2_p16 = "images/school/headmaster_room/morning/S2/16.jpg"
image headmaster_S2_p17 = "images/school/headmaster_room/morning/S2/17.jpg"
image headmaster_S2_p18 = "images/school/headmaster_room/morning/S2/18.jpg"
image headmaster_S2_p19 = "images/school/headmaster_room/morning/S2/19.jpg"
image headmaster_S2_p20 = "images/school/headmaster_room/morning/S2/20.jpg"
image headmaster_S2_p21 = "images/school/headmaster_room/morning/S2/21.jpg"
label headmaster_S2:
    if headmaster_door_locked == True:
        hide screen map_button
        $ clickable = False
        if day_time == 1:
            show screen school_corridor3_morning
        if day_time == 2:
            show screen school_corridor3_day
        MC "I can’t go in. Judy is there."
        $ clickable = True
        hide screen school_corridor3_morning
        hide screen school_corridor3_day
        jump school_corridor3_morning1
    else:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
        $ clickable = False
        if day_time == 1:
            show screen school_corridor3_morning
        if day_time == 2:
            show screen school_corridor3_day
        $ renpy.sound.play("sfx/knock_knock.wav")
        "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        $ clickable = True
        hide screen school_corridor3_morning
        hide screen school_corridor3_day

        Headmaster "Hold up, give me a minute!"
        MC "…"
        Headmaster "Okay, c’mon in!"
        $ renpy.sound.play("sfx/door_open.mp3")
        scene black
        $ renpy.pause(0.5, hard = True)
        $ renpy.music.stop(channel="sound")
        scene headmaster_S1_p1 with dissolve

        Headmaster "Why, hello again [player_name]. What brings you back?"
        MC "Hi sir, sorry to bother you again. Judy told me to-"

        scene headmaster_S1_p3

        Headmaster "Oh yeah! That hot piece of ass stopped by earlier. Something about needing permission to leave school?"
        MC "Yes, sir. She didn’t give me any other instructions than to show up today."

        scene headmaster_S2_p1

        Headmaster "That’s fair, just hold up I’ve got it somewhere here in my drawers."
        MC "(Awesome! It sounds like Judy got the slip approved! Nothing’s going to stand in the way of me going on holiday with [Mom_name] now!)"
        Headmaster "Aha! There it is, buried under that joint-"
        Headmaster "Umm, I mean… joint checking account. Yeah..."

        scene headmaster_S2_p2

        Headmaster "Anyway! Whaddya need this permission slip for? Judy wasn’t actually very clear with me. Patient confidentiality and all that I suppose."
        MC "It’s… uh…"

        scene headmaster_S2_p3

        MC "(Shit, I can’t tell him that I’m going away for the day to fuck my Mom’s brains out.)"
        Headmaster "Yes?"
        MC "I… um… remember what you said last time about caring for my mental health?"

        scene headmaster_S2_p4

        Headmaster "Oh shit, why didn’t you say earlier?! How long did Judy request for?"
        MC "Just a day I think."
        Headmaster "Is that long enough? I can up it to four or five if you like."
        MC "Is that… legal?"
        Headmaster "I’m the goddamn headmaster, I don’t follow the rules - I make ‘em."

        scene headmaster_S2_p5

        MC "Thanks, sir. That’s very kind. Honestly, one day should do me just fine though."
        Headmaster "If you’re certain. Take this one with you - that’s your copy."
        MC "Thanks again, sir."

        scene headmaster_S2_p6

        Headmaster "No sweat, homie. Oh, before I forget, have you been keeping away from the ladies?"
        MC "Huh?"
        Headmaster "Heh, I’m just kidding you. Celia hasn’t filed any more complaints with me. Hopefully that means you two are getting along reasonably well together again."

        scene headmaster_S2_p7

        MC "Yes, we-"
        Headmaster "Hnng… *Cough*"
        MC "Are you okay, sir?"

        scene headmaster_S2_p8

        Headmaster "Y-Yeah, just a- Mmm- *Cough* chesty cough."
        MC "Do you need a glass of water?"
        Headmaster "Ah… I’ll be fine. Just, quickly leave. And close the door behind you!"

        scene headmaster_S2_p9

        Headmaster "Mmm! *Cough*"
        MC "See you later, sir…"
        Headmaster "Later, [player_name]. Don’t forget to close the door! Ah…"
        $ renpy.sound.play("sfx/door_open.mp3")
        scene black
        $ renpy.pause(0.5, hard = True)
        scene school_corridor3_morning
        $ clickable = False
        if day_time == 1:
            show screen school_corridor3_morning
        if day_time == 2:
            show screen school_corridor3_day
        MC "(Well, THAT was weird… I wonder what got into him all of a sudden.)"

        menu:
            "Go away.":
                $ clickable = True
                hide screen school_corridor3_morning
                hide screen school_corridor3_day
                $ MLR3_Bob_AS1_q7 = True
                $ inventory.add(permission)
                $ headmaster_door_locked = True
                $ headmaster_S2 = False
                $ can_hide_windows = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

                jump school_corridor3_morning1
            "Stand in front of the door.":
                $ clickable = True
                hide screen school_corridor3_morning
                hide screen school_corridor3_day
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
                scene headmaster_S2_p10

                Headmaster "Ugh… (I thought he’d NEVER leave!)"
                Headmaster "It’s okay, you can continue Cindy, he’s finally gone. "
                Cindy "*Suck Suck*"

                scene headmaster_S2_p11

                Cindy "Hehe! That was fun!"
                Headmaster "It was goddamn nerve wracking, girl! I came THIS close to blowing my load while he was standing right in front of me!"
                Cindy "And that’s bad because…?"
                Headmaster "Because if he saw you there and decided to tell anyone that I’m fucking a student I would lose my job!"
                Cindy "Hey - look on the bright side! You didn’t get caught! Now, where do you wanna cum?"
                Headmaster "Just the usual."

                scene headmaster_S2_p12

                Cindy "*Suck Suck*"
                Headmaster "Mmm… Damn…"
                Headmaster "(Cindy is fucking incredible with that tongue of hers!)"

                scene headmaster_S2_p13

                Cindy "*Shluuuurrrrp*"
                Cindy "*Suck Suck Suck*"

                Headmaster "Mmm..."

                scene headmaster_S2_p14

                Headmaster "Ahh… Dayum girl, they should be calling YOU the headmaster!"
                Cindy "Hehe! I love your jokes, sir!"
                Headmaster "Y’know Cindy, you don’t HAVE to suck my cock every time you want another ‘package.’"
                Cindy "Don’t be silly - I’m doing this because it’s FUN! Now grab my hair and pull my face down. I LOVE it when you facefuck me really roughly!"

                scene headmaster_S2_p15

                Headmaster "Well, if you insist. Hnng…"
                Cindy "*SHLURP SHLURP*"
                Headmaster "(Fuck, her mouth is so hot. Cindy seems to get better at giving blowjobs each time she visits my office!)"

                scene headmaster_S2_p16

                Headmaster "Hnnng! Fuck! I’m cumming! Swallow it all, girl. Ugh! Yes!"
                Cindy "*Shlurp Suck*"
                Cindy "*Gulp* *Gulp*"

                scene headmaster_S2_p17

                Headmaster "Ohh… fuck…"
                Headmaster "That was great, Cindy. Fucking fantastic as always. I hope that load wasn’t too much for your little mouth to handle."
                Cindy "*GULP*"

                scene headmaster_S2_p18

                Cindy "*Cough* A-All done!"
                Cindy "You mustn’t have cum for DAYS, sir. I don’t remember the last time you came so much!"
                Headmaster "Yeah, I was too busy to beat one out. Tissues are over there if you need one."
                Cindy "I’m good, hehe."

                scene headmaster_S2_p19

                Cindy "Oh! Don’t forget to drop the package in my locker. I’ll pick it up at the end of school."
                Headmaster "Have I ever forgotten before?"
                Cindy "No, I guess not."
                Headmaster "Your headmaster ALWAYS delivers. That’s why I’m the goddamn kingpin in this town."

                scene headmaster_S2_p20

                Cindy "I know, I know. You’re the big boss."
                Headmaster "Your teacher is gonna get suspicious of your absence. Which class are you missing right now?"
                Cindy "Umm… Algebra, I think."
                Headmaster "Tell her you were being… disciplined by the Principal. I’ll verify it if your teacher wants to check it out."

                scene headmaster_S2_p21

                Cindy "Coolio! See you later, sir!"
                Headmaster "See you later, Cindy. I’ll prepare the package now. Make sure you close the door behind you."
                Cindy "Thanks, sir! And thanks for your OTHER package too, hehe!"

                $ inventory.add(permission)
                $ MLR3_Bob_AS1_q7 = True
                $ headmaster_door_locked = True
                $ headmaster_S2 = False
                $ can_hide_windows = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

                jump school_corridor3_morning1