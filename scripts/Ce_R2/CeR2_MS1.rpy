image CeR2_MS1_p1 = "images/CeR2/MS1/1.jpg"
image CeR2_MS1_p2 = "images/CeR2/MS1/2.jpg"
image CeR2_MS1_p3 = "images/CeR2/MS1/3.jpg"
image CeR2_MS1_p4 = "images/CeR2/MS1/4.jpg"
image CeR2_MS1_p5 = "images/CeR2/MS1/5.jpg"
image CeR2_MS1_p6 = "images/CeR2/MS1/6.jpg"
image CeR2_MS1_p7 = "images/CeR2/MS1/7.jpg"
image CeR2_MS1_p8 = "images/CeR2/MS1/8.jpg"
image CeR2_MS1_p9 = "images/CeR2/MS1/9.jpg"
image CeR2_MS1_p10 = "images/CeR2/MS1/10.jpg"

image CeR2_MS1_moni_p1 = "images/CeR2/MS1/Asking Security/1.jpg"
image CeR2_MS1_moni_p2 = "images/CeR2/MS1/Asking Security/2.jpg"
image CeR2_MS1_moni_p3 = "images/CeR2/MS1/Asking Security/3.jpg"
image CeR2_MS1_moni_p4 = "images/CeR2/MS1/Asking Security/4.jpg"
image CeR2_MS1_moni_p5 = "images/CeR2/MS1/Asking Security/5.jpg"
image CeR2_MS1_moni_p6 = "images/CeR2/MS1/Asking Security/6.jpg"
default CeR2_MS2 = False
default CeR2_MS1 = False
default CeR2_MS1_day = 1
default CeR2_MS1_talk = False
label CeR2_MS1_lab:



    if CeR2_moni == 6:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)

        scene CeR2_MS1_p1 with dissolve
        Celia "Did you get a copy of the tape?"
        MC "I tried my best, Mrs. Celia. There must have been some kind of failsafe though!"
        scene CeR2_MS1_p2

        Celia "Why, what happened?"
        MC "As soon as I tried to access the files it asked me for a password. I tried a few times and then…"
        scene CeR2_MS1_p6
        Celia "Then what?"
        MC "Everything just deleted! The whole system!"
        Celia "Are you serious?!"
        scene CeR2_MS1_p7
        MC "There’s nothing left at all."
        Celia "That was our BEST chance at catching the blackmailer red handed!"
        Celia "Ugh! You idiot! You’ve cost us our best chance at fixing this."
        scene CeR2_MS1_p10
        Celia "God dammit… I’m out of here."
        Celia "(This is REALLY fishy. How could you accidentally delete the entire security camera footage?)"
        Celia "(I wonder if [player_name] is an accomplice to the blackmailer - or even worse, the blackmailer himself.)"
        MC "(Heh, that worked like a charm! She doesn’t suspect a thing!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

        $ can_hide_windows = False
        $ CeR2_moni = 7
        $ CeR2_MS1_talk = True

        jump school_entrance_morning1

    if CeR2_moni == 4:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene CeR2_MS1_moni_p1 with dissolve
        Celia "Well?"
        MC "Well what?"
        Celia "Have you found the security footage yet?"

        scene CeR2_MS1_moni_p2
        MC "I’m getting blocked from seeing it."
        Celia "What do you mean you’re getting blocked?!"
        Celia "Do you not realise how damn serious it is?"

        scene CeR2_MS1_moni_p3
        MC "It’s not my fault!"
        Celia "Then whose fault is it?"

        scene CeR2_MS1_moni_p4
        MC "Big Jake! The fat guy who operates the security suite."
        Celia "Hold up, let me get this straight."
        Celia "You’re getting pushed around by Big Jake?"

        scene CeR2_MS1_moni_p5
        MC "Yes! He won’t let me anywhere near the security system. I can’t access any videos if he is there."
        Celia "…"
        MC "He threatened to call the Principal on me! I just need you to distract him for five minutes. I’ll slip inside, grab the footage, and then we’ll know who the dickhead blackmailing you is. Okay?"

        scene CeR2_MS1_moni_p6
        Celia "You got intimidated by an obese blob of lard that weighs at least six hundred pounds."
        MC "Yeah, but-"
        Celia "That guy wheezes more than a fucking whoopee cushion!"
        Celia "Christ almighty… Fine! I’ll distract Big Jake. This was SUPPOSED to be YOUR job though!"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

        $ can_hide_windows = False
        $ CeR2_moni = 5
        $ CeR2_MS1 = False
        $ CeR2_MS1_talk = True
        jump school_entrance_morning1

    if CeR2_MS1_day == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene CeR2_MS1_p1 with dissolve
        MC "Hi Celia, are you free to talk for a minute?"
        Celia "I was just about to begin my class, but I can spare a minute."

        scene CeR2_MS1_p2
        Celia "What’s up, [player_name]?"
        MC "I just wanted to update you on what I’ve found out about the blackmailer."
        Celia "Oh yeah? Tell me! What did you find out?"

        scene CeR2_MS1_p3
        MC "Umm… Nothing so far."
        Celia "Seriously? You came over to tell me you found NOTHING?!"
        MC "Well, not exactly nothing. There’s nobody suspicious in my class. This leads me to believe the blackmailer is in ANOTHER classroom."

        scene CeR2_MS1_p4
        Celia "Hmm…"
        Celia "(He has a good point. Even though he didn’t find me the actual asshole, [player_name] has helped me tighten the net on them.)"
        Celia "(I’ll have [player_name] search the other classes. As soon as he notifies me of anyone even remotely suspicious, I’ll take them down.)"

        scene CeR2_MS1_p5
        MC "Sorry I couldn’t be of more help."
        Celia "No… this is good. I can work with this."
        Celia "I need you to expand your search to other classrooms. Speak to your classmates, ask around, see if anyone knows anything."

        scene CeR2_MS1_p6
        MC "Are you sure? What if people grow suspicious about me sticking my nose into their business?"
        Celia "It’s a risk we’ll have to take. I can’t let this blackmail go on any longer."

        scene CeR2_MS1_p7
        MC "I understand that. Do you have any idea about who would want to do this to you though?"
        Celia "Do you honestly think I know any more than you do?!"
        Celia "If I even had a slight inclination about who was behind this I would have already hunted them down."

        scene CeR2_MS1_p8
        MC "Fair enough, but what could you actually do? Getting a confession mightn’t be easy-"
        Celia "I’m not going to the police with this. I’m not going to handle him myself. By the time I’m finished with them, their classmates will be wondering who used to sit in that empty chair. "
        Celia "This punk won’t be on any attendance register, their name won’t be in the front of any textbooks, their photo won’t be in any fucking yearbooks."
        Celia "I’m going to fucking erase them from existence."

        scene CeR2_MS1_p9
        MC "*Gulp*"
        Celia "Now, I have to get to class. I expect to hear from you tomorrow about what you find out."
        MC "S-Sure, no problem."
        Celia "God willing I’ll catch this bastard, and when I do, I’ll tear him limb from fucking limb."

        scene CeR2_MS1_p10
        MC "(Yikes… She can be pretty damn scary when she’s angry.)"
        MC "(Ah well, time to pretend to search for the blackmailer.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

        $ can_hide_windows = False
        $ CeR2_MS1_day = 2
        $ CeR2_MS1_talk = True
        jump school_entrance_morning1

    if CeR2_MS1_day == 4:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene CeR2_MS1_p1
        MC "Hey Mrs. Celia, can I borrow you for a minute?"
        Celia "Yes, did you find out anything?"
        MC "Nothing, I’m afraid."

        scene CeR2_MS1_p2
        Celia "Nothing? Seriously?"
        MC "Yeah, I’m sorry."
        Celia "*Sigh* I don’t believe it. You’re telling me that there are NO students acting suspicious in ANY of the classes?"
        MC "None that I could see."

        scene CeR2_MS1_p5
        Celia "Shit."
        MC "I really am sorry. I want to get to the bottom of this as much as you do."
        MC "(I know that Mrs Celia can’t go to the police. If she does, then they’ll catch her selling those grades for money.)"
        MC "How about we just give up and call the police? They’re professionals and they can-"

        scene CeR2_MS1_p6
        Celia "No! No cops!"
        MC "What? Are you su-"
        Celia "I swear to God, if you let the police know about this I will lose my fucking shit! This is embarrassing enough as it is."

        scene CeR2_MS1_p7
        Celia "*Sigh* No cops. Understand?"
        MC "Yes, Mrs. Celia. "
        MC "(Hehe, if she thinks I want to call the police then she won’t suspect me of being the blackmailer!)"

        scene CeR2_MS1_p8
        MC "Is there anything else you would like me to do?"
        Celia "I don’t fucking know. Grr…"
        Celia "I’ll call you if I need you. Right now, I’ve got a class to teach."

        scene CeR2_MS1_p10
        Celia "Jesus… fucking… Christ…"
        Celia "(Could it be one of the other professors? They do have access to the staffroom, and it is conceivable that one of them might have stolen my password.)"
        MC "(Hehe, another victory for [player_name].)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

        $ can_hide_windows = False
        $ CeR2_MS1_day = 5
        $ CeR2_MS1_talk = True

        jump school_entrance_morning1
    else:


        hide screen map_button
        show screen school_entrance_morning

        $ clickable = False
        MC "I've already talked with her."
        $ clickable = True
        hide screen school_entrance_morning
        jump school_entrance_morning1