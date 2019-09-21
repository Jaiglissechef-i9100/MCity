default Zv2_MS1_ask_boob_office = True
default Zv2_MS1_ask_boob_office1 = 1

label Zv2_MS1_daymeet_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if Zv2_MS1_ask_boob_office == True:
        scene Zv2_MS1_p1 with dissolve
        $ Zuri_name = "???"
        Zuri "Hello, and welcome to Bayside Business Consultants. My name is Zuri. How can I help you?"
        $ Zuri_name = "Zuri"

        scene Zv2_MS1_p2
        if renpy.loadable("patch.rpy"):
            MC "(Wow! That must be Dad’s secretary! She’s REALLY hot!)"
            MC "Hi, Zuri. My name is [player_name]. I was coming to visit my dad."
            Zuri "And who is your dad?"
        else:
            MC "(Wow! That must be Bob’s secretary! She’s REALLY hot!)"
            MC "Hi, Zuri. My name is [player_name]. I was coming to visit Bob."
            Zuri "And who is Bob?"
        MC "Uhh… The one who runs this company?"

        scene Zv2_MS1_p3

        Zuri "Ahahaha! How funny!"
        Zuri "Let me guess - you’re with one of those online prank videos, aren’t you?"
        MC "Huh?"
        Zuri "You’ve got a secret camera and you’re going to humiliate the boss and put it online?"
        if renpy.loadable("patch.rpy"):
            MC "No- What?! I AM actually his son."
        else:
            MC "No- What?! I AM actually his tennant."

        scene Zv2_MS1_p1

        Zuri "Really?"
        MC "Yes!"
        Zuri "Oh! Sorry! My bad!"
        Zuri "I'm sorry but he's not in the office at the moment. He's only there in the mornings. Please come back tomorrow."
        $ Zv2_MS1_ask_boob_office = False
        $ Zv2_MS1_ask_boob_office1 = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1

    if Zv2_MS1_ask_boob_office == False:
        scene Zv2_MS1_p1 with dissolve
        Zuri "Hello, and welcome to Bayside Business Consultants."
        MC "There is someone in the office?"
        Zuri "I'm sorry but nobody is in the office at the moment. He's only there in the mornings. Please come back tomorrow."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
