image celia_webcam_evening_scene1_v1_p1 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/1.jpg"
image celia_webcam_evening_scene1_v1_p2 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/2.jpg"
image celia_webcam_evening_scene1_v1_p3 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/3.jpg"
image celia_webcam_evening_scene1_v1_p4 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/4.jpg"
image celia_webcam_evening_scene1_v1_p5 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/5.jpg"
image celia_webcam_evening_scene1_v1_p6 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/6.jpg"
image celia_webcam_evening_scene1_v1_p7 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/7.jpg"
image celia_webcam_evening_scene1_v1_p8 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/8.jpg"

screen celia_webcam_evening_screen_v1:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("celia_webcam_evening_screen_v1"),Jump("celia_webcam_evening_scene1_v1_label")]
screen celia_webcam_evening_screen1_v1:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        clicked [Jump("celia_webcam_evening_scene1_v1_label2")]
    timer 4.00 action [Hide ("celia_webcam_evening_screen1_v1"),Jump("celia_webcam_evening_scene1_v1_label2")]

label celia_webcam_scenes:
    if celia_webcam_introdution_v1 == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music1", loop=True, fadein = 2)
        show screen live_camera_screen
        show screen celia_webcam_evening_screen1_v1
        show screen celia_webcam_evening_screen_v1
        MC "(Oh God… she’s online! My heart is racing!)"
    if celia_webcam_menuv1 == True:
        hide screen main_deskop_pcv1
        hide screen live_camera_screen
        jump celia_webcam_scenes_menu1

label celia_webcam_evening_scene1_v1_label:
    $ renpy.sound.play('/sfx/phone_call.mp3', loop=False)
    MC "(Okay, I better make sure my webcam is covered up.)"

label celia_webcam_evening_scene1_v1_label2:
    $ renpy.sound.stop(channel="sound")
    hide screen main_deskop_pcv1
    hide screen live_camera_screen
    hide screen celia_webcam_evening_screen1_v1
    hide screen celia_webcam_evening_screen_v1
    scene celia_webcam_evening_scene1_v1_p1 with dissolve
    Celia "Hello?! Is this thing on?"
    MC "(I better try using a deeper voice than usual.)"
    MC "I see you got my letter, Mrs. Celia."
    Celia "I don’t know who the HELL you think you are, but when I find you, I will beat the crap out of you!"

    scene celia_webcam_evening_scene1_v1_p2
    Celia "And where the hell are you?! Turn your webcam on, you coward!"
    Celia "If you’re going to threaten me, then at least show me your face, while you do it!"
    MC "I won’t be doing that, Mrs. Celia."
    Celia "Fine! Then I’m going."

    scene celia_webcam_evening_scene1_v1_p3
    MC "You can walk away - but if you do, I will publish the picture of you selling grades, on social media."
    MC "And I won't stop there. I’ll make sure the Principal gets a copy, as well as the police."
    MC "You’re a corrupt woman, Mrs. Celia. And now you will have to pay the price."

    scene celia_webcam_evening_scene1_v1_p4
    Celia "God dammit… What do you want from me?"
    MC "Not too much. I only have a couple of demands."
    MC "Firstly, I want to chat with you every evening. Let’s make this a regular thing."
    Celia "…"
    Celia "Ugh! Fine! (It’s not like I have a choice..)"
    Celia "And your second demand?"
    MC "I want you to strip down to your underwear. Lose the grey dress."

    scene celia_webcam_evening_scene1_v1_p5
    Celia "WHAT?! I swear to God, I will find out who you are, you fucking pervert!"
    MC "That’s hardly the proper way to talk to the guy, who holds enough evidence to get you fired from your job."
    MC "Now, how about you take that dress off, before I get in touch with the Principal?"
    Celia "…"

    scene celia_webcam_evening_scene1_v1_p6
    MC "Mmm... Nice ass, Mrs. Celia."
    Celia "Fuck you…"
    MC "(Damn, Mrs. Celia has a REALLY nice ass! Maybe I’ll get to fuck it someday?)"

    scene celia_webcam_evening_scene1_v1_p7
    MC "(Mmm! And nice tits too! I can’t wait to see her without her bra on.)"
    MC "(I should probably wait until later on though - I should follow Judy’s advice, and take things in gradual steps.)"

    scene celia_webcam_evening_scene1_v1_p8
    Celia "Well? That’s my dress off. What do you want now, you pervert?"
    MC "That’s enough for tonight. I just wanted you to know who holds the power here."
    MC "We’re going to chat again, tomorrow night. I’d like to see you in your underwear, when we begin chatting."
    Celia "(Fuck… I need to figure out who this creep is, or I’m in serious shit.)"
    MC "See you tomorrow, beautiful."
    $ day_time = 4
    $ celia_webcam_introdution_v1 = 3
    $ celia_webcam_menuv1 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump mc_room_night1
