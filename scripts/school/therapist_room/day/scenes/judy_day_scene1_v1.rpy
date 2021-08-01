label judy_day_menu_v1_label:
    hide screen map_button
    scene judy_scene1_v1_p7
    $ can_hide_windows = True
    menu:
        "Talk about Celia’s been selling grades." if Judy_scene1_v1 == 1:
            jump judy_day_scene1_v1_label
        "Cancel":
            jump therapist_room_morning1

label judy_day_scene1_v1_label:
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

