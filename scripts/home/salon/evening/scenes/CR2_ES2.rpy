image CR2_ES2_p1 = "images/home/salon/evening/scenes/CR2_ES2/1.jpg"
image CR2_ES2_p2 = "images/home/salon/evening/scenes/CR2_ES2/2.jpg"
image CR2_ES2_p3 = "images/home/salon/evening/scenes/CR2_ES2/3.jpg"
image CR2_ES2_p4 = "images/home/salon/evening/scenes/CR2_ES2/4.jpg"
image CR2_ES2_p5 = "images/home/salon/evening/scenes/CR2_ES2/5.jpg"
image CR2_ES2_p6 = "images/home/salon/evening/scenes/CR2_ES2/6.jpg"
image CR2_ES2_p7 = "images/home/salon/evening/scenes/CR2_ES2/7.jpg"
image CR2_ES2_p8 = "images/home/salon/evening/scenes/CR2_ES2/8.jpg"
image CR2_ES2_p9 = "images/home/salon/evening/scenes/CR2_ES2/9.jpg"
image CR2_ES2_p10 = "images/home/salon/evening/scenes/CR2_ES2/10.jpg"
image CR2_ES2_p11 = "images/home/salon/evening/scenes/CR2_ES2/11.jpg"
image CR2_ES2_p12 = "images/home/salon/evening/scenes/CR2_ES2/12.jpg"
image CR2_ES2_p13 = "images/home/salon/evening/scenes/CR2_ES2/13.jpg"
image CR2_ES2_p14 = "images/home/salon/evening/scenes/CR2_ES2/14.jpg"

default can1_CR2_MS2 = False
default CR2_ES2_day = 1
default CR2_ES2_q1 = True
default CR2_ES2_q2 = True
default CR2_ES2_q3 = True
default CR2_ES2_q4 = False
default CR2_ES2_q5 = False
default CR2_ES2_q6 = False
default CR2_ES2_q7 = False
default can_CR2_ES2_day2 = False
default can_CR2_ES2_day3 = False
default CR2_ES2_day2_firsttime = True
default CR2_ES2_day3_firsttime = True
default can_CR2_ES2 = True

label CR2_ES2_label:
    if can_CR2_ES2 == False:
        show screen salon_evening_notclickable
        MC "I shouldn't bother her. She wants to be alone."
        jump salon_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ can_hide_windows = True
        if CR2_ES2_day == 1:
            scene CR2_ES2_p1 with dissolve

            MC "(Caroline is looking very downhearted there. Maybe I should go over and see how she’s doing.)"
            MC "(I know I’d be devastated if I owned a business that got robbed.)"

            scene CR2_ES2_p2

            MC "(She didn’t even seem to notice me walking over. She must be REALLY deep in thought.)"
            MC "(I’ll just approach this gently. I don’t want to upset her, any more than she already is.)"

            scene CR2_ES2_p3

            MC "Hey Caroline, how are you holding up?"
            Caroline "Oh hey, [player_name]. I’m good! Don’t you worry."
            MC "Promise?"

            scene CR2_ES2_p4

            Caroline "Honestly. I’m fine."
            Caroline "C’mon over and take a seat beside me."
            MC "Okay."
            jump CR2_ES2_menu

        if CR2_ES2_day == 2:
            scene CR2_ES2_p1 with dissolve

            MC "(Caroline’s on the couch with hot chocolate again.)"
            MC "(I should probably check up on her, to make sure she isn’t feeling too depressed.)"

            scene CR2_ES2_p3

            MC "Hey, it’s just me again."
            MC "I thought I’d go in just to see how you’re feeling."

            scene CR2_ES2_p4

            Caroline "Hi, [player_name]."
            MC "Are you okay if I sit down beside you? Or would you rather spend some time alone?"
            Caroline "Honestly? I’d rather be alone right now. But feel free to sit with me for a few minutes, if you want."
            if CR2_ES2_day2_firsttime == True:
                $ CR2_ES2_q4 = True
                $ CR2_ES2_q5 = True
                $ CR2_ES2_q6 = True
                $ CR2_ES2_day2_firsttime = False
                jump CR2_ES2_menu
        if CR2_ES2_day == 3:
            scene CR2_ES2_p1 with dissolve

            MC "(She’s still moping around the house with a hot chocolate.)"
            MC "(It seems like this robbery seriously affected her.)"

            scene CR2_ES2_p3

            MC "Hey, Caroline. How are you today?"

            scene CR2_ES2_p4

            Caroline "Oh. Hi, [player_name]."
            MC "Have you been outside, at all?"
            Caroline "Nah, I’m comfy in here."
            MC "(Caroline needs to find some closure on this robbery situation. She’s evidently not moving on with her life right now.)"
            if CR2_ES2_day3_firsttime == True:
                $ CR2_ES2_q7 = True
                $ CR2_ES2_day3_firsttime = False
                jump CR2_ES2_menu
        jump CR2_ES2_menu

label CR2_ES2_menu:
    $ can_hide_windows = True
    scene CR2_ES2_p5
    window hide
    menu:
        "{color=#00ff00}Do you know where I can find Violet?{/color}" if CR2_ES2_qViolet == True:

            scene CR2_ES2_p9

            MC "Do you know where I’d be able to find Violet?"

            scene CR2_ES2_p14

            Caroline "Hmm… I know she usually hangs out around that old dark alley, in the city."
            Caroline "You’d need to be careful around that area though."

            scene CR2_ES2_p5

            Caroline "Why do you want to find her, by the way? You can’t seriously be interested in pursuing a relationship with her?"
            MC "Uh… She… left some of her makeup behind, by accident. I just wanted to return it."

            scene CR2_ES2_p6

            Caroline "Ohh, that’s very nice of you. Tell her I say hello! I haven’t heard from her in a few days."
            MC "(Caroline hasn’t heard from Violet? That makes sense. Violet is probably feeling too guilty, after robbing her friend.)"
            MC "Will do, Caroline."
            $ CR2_ES2_qViolet = False
            $ dark_alley_unlocked = True
            $ violetV2_scene = True
            $ can1_CR2_MS2 = True
            jump CR2_ES2_menu

        "I didn’t know you liked coffee." if CR2_ES2_q1 == True:
            scene CR2_ES2_p5

            MC "I didn’t know you liked coffee, Caroline."
            if renpy.loadable("patch.rpy"):
                MC "Whenever we went out as a family, you always used to order something cold, like pineapple juice."
            else:
                MC "Whenever we went out together, you always used to order something , like pineapple juice."

            scene CR2_ES2_p6

            Caroline "That’s because this isn’t coffee. But very well remembered!"
            Caroline "I made myself some hot chocolate. Would you like some?"
            MC "Sure, I’ll have a sip."

            scene CR2_ES2_p7

            Caroline "I’m a little disappointed that there were no marshmallows in the house."
            Caroline "I love the way the mallows go all gooey and start to melt."
            MC "Yeah, I know what you mean."

            scene CR2_ES2_p8

            MC "Shlurp!"
            Caroline "I should really buy some cream as well, to go on top."
            Caroline "That would be perfect…"

            scene CR2_ES2_p9

            MC "That tastes great! Thanks, Caroline."
            Caroline "You’re very welcome, [player_name]."
            $ CR2_ES2_q1 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "Are you sure you’re feeling okay? You looked a bit sad when I came in." if CR2_ES2_q2 == True:
            scene CR2_ES2_p5

            MC "Are you feeling okay? You looked a bit sad when I entered the room."

            scene CR2_ES2_p9

            Caroline "I’m great! Honestly - nothing wrong at all."
            MC "You’re not telling me the truth, Caroline."

            scene CR2_ES2_p10

            Caroline "I’m not a great liar, am I?"
            MC "No, you’re not. Tell me what’s bothering you though. It’s about the robbery, isn’t it?"
            Caroline "(Sigh) It is."

            scene CR2_ES2_p11

            Caroline "I spent sooo long working on that shop."
            Caroline "I sometimes worked, twelve hours a day, to get it up and running."
            Caroline "And now, some STUPID burglar has gone and screwed it all up on me!"

            scene CR2_ES2_p10

            MC "It’s okay, Caroline. I understand how you feel. We’ll get through it, together."
            Caroline "(Sniff) Thanks, [player_name]."
            $ CR2_ES2_q2 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "Have you any plans for today?" if CR2_ES2_q3 == True:
            scene CR2_ES2_p5

            MC "Have you got any plans for today?"

            scene CR2_ES2_p13

            Caroline "Err… not really. I was just going to spend the day at home, relaxing."
            MC "You don't feel like visiting the salon, to take your mind off things?"

            scene CR2_ES2_p10

            Caroline "I don’t have the money to do that, right now."
            Caroline "I can’t even afford to buy myself marshmallows and cream, for this hot chocolate!"
            MC "It’s okay, Caroline. We’ll get your life back on track."

            scene CR2_ES2_p10

            Caroline "Thanks, [player_name]."
            $ CR2_ES2_q3 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "Have you heard from the police yet?" if CR2_ES2_q4 == True:
            scene CR2_ES2_p5

            MC "Have you heard back from the police yet, about the robbery?"
            Caroline "Shlurp"

            scene CR2_ES2_p10

            Caroline "Nothing good."
            MC "Crap."
            Caroline "They told me that this wasn’t an urgent case for them."
            Caroline "I rang up this morning, and they told me that it’s been too long since the incident, for them to investigate."
            Caroline "Apparently, any evidence that existed, could have been tampered with or lost."

            scene CR2_ES2_p11

            Caroline "They said they’d keep my case file open, but it isn’t any going to go anywhere, unless I can name a suspect."
            Caroline "I mean - why am I being expected to do the police’s job?!"
            MC "Shit, I’m sorry to hear that."
            $ CR2_ES2_q4 = False
            $ can_CR2_ES2_day3 = True
            jump CR2_ES2_menu
        "When are you thinking of going back to work?" if CR2_ES2_q5 == True:
            scene CR2_ES2_p13

            MC "When are you thinking of going back to work?"
            Caroline "I’m kinda stuck between a rock and a hard place, right now."
            Caroline "I can’t stock my shop without money - and I can’t get money from the bank, unless I can provide evidence that I have a good cash flow."

            scene CR2_ES2_p10

            Caroline "So, to put things mildly - I’m fucked."
            MC "Shit. I’m sorry to hear that."
            Caroline "I’ll get back on my feet - but it’s gonna take me a lot of time to get there."
            $ CR2_ES2_q5 = False
            $ can_CR2_ES2_day3 = True
            jump CR2_ES2_menu

        "Have you spoken to Mom or Dad about this robbery yet?" if CR2_ES2_q6 == True and renpy.loadable("patch.rpy"):
            jump CR2_ES2_bobtalk

        "Have you spoken to Linda or Bob about this robbery yet?" if CR2_ES2_q6 == True and not renpy.loadable("patch.rpy"):
            jump CR2_ES2_bobtalk

        "Are you feeling any better today?" if CR2_ES2_q7 == True:
            scene CR2_ES2_p12

            MC "Are you feeling any better today, Caroline?"
            Caroline "I… think so."
            Caroline "I’m not feeling as depressed as I was, a couple of days ago."

            scene CR2_ES2_p14

            Caroline "I think this is what they call, the acceptance stage? Although, I’ve never studied a day of psychology in my life - so I’m just guessing."
            MC "(I hate seeing Caroline like this. A few days ago she was all excited about expanding her business and opening new stores.)"
            MC "(Now she’s been reduced to, moping around on a sofa. Whoever robbed her deserves to pay for what they did!)"

            scene CR2_ES2_p9

            MC "If you ever want someone to talk to, you know I’m always free to listen."
            Caroline "I know that. Thanks, [player_name]."
            $ CR2_ES2_q7 = False
            jump CR2_ES2_menu
        "Bye.":

            jump CR2_ES2_bye

label CR2_ES2_bye:
    if CR2_ES2_day == 1:
        scene CR2_ES2_p10

        Caroline "I think I’d rather spend some time alone now."
        Caroline "Is that okay?"

        scene CR2_ES2_p11

        MC "Of course, Caroline. If you need anything, just call for me, okay?"
        Caroline "I will. See you later, [player_name]."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1

    if CR2_ES2_day == 2:
        scene CR2_ES2_p13

        Caroline "I think I’d rather be alone again right now."
        Caroline "I’ll talk to you later, okay?"
        MC "No problem, Caroline. See you later."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1
    if CR2_ES2_day == 3:
        scene CR2_ES2_p11

        Caroline "Are you okay if I spend a little bit of time alone?"
        MC "Yeah, that’s not a problem."
        Caroline "Sorry, I just have a lot of things in my head I need to think about right now."
        MC "It’s okay, I understand. I’ll see you later, Caroline."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1

label CR2_ES2_bobtalk:
    scene CR2_ES2_p12
    if renpy.loadable("patch.rpy"):
        MC "Have you told Mom or Dad about the robbery yet?"
    else:
        MC "Have you told Linda or Bob about the robbery yet?"
    Caroline "No! Absolutely not."
    MC "Why?"

    scene CR2_ES2_p10
    if renpy.loadable("patch.rpy"):
        Caroline "I’m supposed to be the independent successful daugther."
    else:
        Caroline "I’m supposed to be the independent successful woman."
    if renpy.loadable("patch.rpy"):
        Caroline "I was the first born, and they both have high hopes for me."
    MC "Have they not asked why you’re, not at work right now?"

    scene CR2_ES2_p11
    if renpy.loadable("patch.rpy"):
        Caroline "Mom asked me, this morning…"
    else:
        Caroline "Linda asked me, this morning…"
    MC "What did you tell her?"
    Caroline "I said that business was going so well, that I could afford to take a few days off…"

    scene CR2_ES2_p13

    MC "Shit…"
    Caroline "Yeah, I shouldn’t have lied like that."
    $ CR2_ES2_q6 = False
    $ can_CR2_ES2_day3 = True
    jump CR2_ES2_menu
