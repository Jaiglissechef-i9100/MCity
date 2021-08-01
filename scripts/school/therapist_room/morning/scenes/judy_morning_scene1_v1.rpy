image judy_scene1_v1_p1 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/1.jpg"
image judy_scene1_v1_p2 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/2.jpg"
image judy_scene1_v1_p3 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/3.jpg"
image judy_scene1_v1_p4 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/4.jpg"
image judy_scene1_v1_p5 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/5.jpg"
image judy_scene1_v1_p6 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/6.jpg"
image judy_scene1_v1_p7 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/7.jpg"

image judy_MLask_p1 = "images/school/therapist_room/morning/scenes/judy_ML_ask/1.jpg"
image judy_MLask_p2 = "images/school/therapist_room/morning/scenes/judy_ML_ask/2.jpg"
image judy_MLask_p3 = "images/school/therapist_room/morning/scenes/judy_ML_ask/3.jpg"
image judy_MLask_p4 = "images/school/therapist_room/morning/scenes/judy_ML_ask/4.jpg"

image judy_q3_p1 = "images/school/therapist_room/morning/scenes/HeadMaster/1.jpg"
image judy_q3_p2 = "images/school/therapist_room/morning/scenes/HeadMaster/2.jpg"
image judy_q3_p3 = "images/school/therapist_room/morning/scenes/HeadMaster/3.jpg"
image judy_q3_p4 = "images/school/therapist_room/morning/scenes/HeadMaster/4.jpg"
image judy_q3_p5 = "images/school/therapist_room/morning/scenes/HeadMaster/5.jpg"
image judy_q3_p6 = "images/school/therapist_room/morning/scenes/HeadMaster/6.jpg"

label judy_menu_v1_label:
    hide screen map_button
    scene judy_scene1_v1_p7
    $ can_hide_windows = True
    menu:
        "{color=#00ff00}Ask Judy for help with Celia.{/color}" if CeR2_J_q == True:
            jump CeR2_J_q_lab

        "{color=#00ff00}Tell Judy what you found out about Celia.{/color}" if CeR2_J_q == 3:
            jump CeR2_J_q_lab2
        "{color=#00ff00}Talk about an exemption from school.{/color}" if judy_q3 == True:
            jump judy_q3_label
        "Talk about Celia being selling grades." if Judy_scene1_v1 == 1:
            jump judy_morning_scene1_v1_label
        "Talk about Mom." if judy_q2 == True and persistent.incest_patch == True:
            jump judy_lindadeal
        "Talk about Linda." if judy_q2 == True and not persistent.incest_patch == True:
            jump judy_lindadeal
        "Cancel":

            jump therapist_room_morning1

label judy_morning_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene judy_scene1_v1_p1
    Judy "Welcome back, [player_name]. I’m always glad to see students decide to continue their therapy."
    Judy "Is there anything in-particular you would like to discuss today?"
    MC "Thanks, Judy. Yeah, actually. I was wondering though… Is everything that is said in therapy confidential?"
    Judy "Unless you’re planning to kill yourself or somebody else, then yes. It is entirely confidential."

    scene judy_scene1_v1_p2
    MC "Awesome! Right, I think I’ve figured out a way to get revenge on Celia."
    Judy "Oh, really?"
    MC "I was on her computer, when I found out she has been selling top grades for THOUSANDS of dollars! She must have made at LEAST $10,000!"
    MC "I’m gonna use this information to blackmail her into-"

    scene judy_scene1_v1_p3
    Judy "Okay, I’m gonna stop you right there."
    MC "Huh?"
    Judy "This is a TERRIBLE idea."
    MC "What? Why?!"

    scene judy_scene1_v1_p4
    Judy "You can’t just walk in and blackmail her. Celia is a formidable woman. There will be consequences."
    MC "B-But I worked so hard to get this evidence…"
    Judy "You can still use it. You just need to be smart about HOW you blackmail her."
    MC "What do you mean?"

    scene judy_scene1_v1_p5
    Judy "You need to work in gradual steps. Begin by buying yourself a webcam. I’ll give you her Skipe address and you can anonymously blackmail her from there."
    Judy "It’s really important that you only push her a little bit at a time. You don’t want to scare her off or cause her to go to the police."
    MC "Good idea! But, why are you helping me?"
    Judy "Celia voted against, giving the school support staff a pay rise, at the last teacher’s conference. Let’s just say that this is my way of getting my own revenge on that, stuck-up bitch!"
    MC "Huh, I never knew that."

    scene judy_scene1_v1_p5
    Judy "First thing though - go and write her a letter and put it in her cabinet in the teacher’s break room. You can take my envelope from the table near the door."
    Judy "Then, create a fake webcam account, and stay logged in this evening. She should contact you."
    MC "Thanks, Judy. I really hope this works."
    Judy "Trust me, it will. Now hurry up and write your blackmail note."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ Judy_scene1_v1 = 3
    $ can_envelope_from_Judy_v1 = 1
    $ can_hide_windows = False
    jump therapist_room_morning1

label judy_lindadeal:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene judy_MLask_p1
    Judy "It’s good to see you again, [player_name]. It is important for - people experiencing trauma - to attend therapy on a regular basis."
    Judy "Far too many of my other patients skip sessions - or even drop out."
    MC "Hey, Judy. I wasn’t actually here for therapy today."

    scene judy_MLask_p2

    Judy "No? Is something wrong?"
    MC "Yes... No... Maybe? I’m not sure right now."
    Judy "Calm down, and breathe. What is it you want to say?"
    if persistent.incest_patch == True:
        MC "I… I overheard my mom talking to you on the phone."
    else:
        MC "I… I overheard Linda talking to you on the phone."
    if persistent.incest_patch == True:
        Judy "Okay... There’s nothing unusual about that. Parental involvement can be very important in therapy."
    MC "The two of you were talking about some kind of deal involving me."

    scene judy_MLask_p3
    if persistent.incest_patch == True:
        Judy "Ahh! You’re more aware of the situation than I thought. Did you learn about this by eavesdropping on your mom’s conversations?"
    else:
        Judy "Ahh! You’re more aware of the situation than I thought. Did you learn about this by eavesdropping on Linda’s conversations?"
    MC "Yeah."
    Judy "Hmm… Fine. I’ll tell you about it - but not here."

    scene judy_MLask_p4

    Judy "Come over to my house, and I’ll explain it, in person. Here’s my address."
    MC "Why can’t you just tell me right now?"
    Judy "I would be violating - SO many departmental HR policies - if I did! I’ll speak with you at my home. Okay?"
    MC "Fine. I’ll see you there."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ judy_q2 = False
    $ J_home_unlocked = True
    $ can_hide_windows = False
    jump therapist_room_morning1

label judy_q3_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    scene judy_q3_p1 with dissolve
    MC "Hey Judy, can I bother you for a minute?"
    Judy "Of course, [player_name]. You know my office is always open to you while you’re undergoing your treatment. Please, take a seat."
    MC "Thanks for the offer, but I’ll only be a minute."

    scene judy_q3_p2

    Judy "What can I do for you, then?"
    MC "Well, I was wondering if you could maybe approve an exemption from school for me?"
    Judy "An exemption? Why would you need that?"

    scene judy_q3_p3

    MC "It’s just a… quick getaway for my mental health. I wanted to take a break and focus on recovering."
    if persistent.incest_patch == True:
        Judy "(Hmm, he’s being especially evasive with that answer. I wonder if this has anything to do with Linda making moves on her son. I’ll try prying a little deeper.)"
    else:
        Judy "(Hmm, he’s being especially evasive with that answer. I wonder if this has anything to do with Linda making moves on [player_name]. I’ll try prying a little deeper.)"
    Judy "How long do you need off?"
    MC "Just the one day."

    scene judy_q3_p4

    Judy "(One day for a mental health break? Most students would need a week or two off for something like that. Come to think of it - wasn’t Linda going away for a day soon? I tried to organise lunch, and she said she was out of town.)"
    Judy "(This has Linda’s fingerprints ALL over it!)"
    if persistent.incest_patch == True:
        Judy "(She must be taking her son away to a hotel somewhere, for the night. Then again, there’s nothing at all wrong with that. This is something I should be encouraging!)"
    else:
        Judy "(She must be taking [player_name] away to a hotel somewhere, for the night. Then again, there’s nothing at all wrong with that. This is something I should be encouraging!)"
    Judy "Hmm… I guess that’s something I could look into for you. I’ll need to speak with the headmaster about this, to get his consent."

    scene judy_q3_p5

    Judy "How about I go and have a chat with him now, and then you visit him tomorrow?"
    MC "Do you think he’ll approve it?"
    Judy "Don’t worry - I can be VERY persuasive."
    MC "Thanks, Judy! I owe you one!"
    Judy "(After this holiday with Linda, you’re going to owe me WAY more than one, kiddo!)"

    scene judy_q3_p6
    Judy "You can thank me later. I’ll pop off to the headmaster’s office now."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ Judy_in_her_Office = False
    $ judy_q3 = False
    $ headmaster_door_locked = True
    $ headmaster_S2 = True
    jump therapist_room_morning1

