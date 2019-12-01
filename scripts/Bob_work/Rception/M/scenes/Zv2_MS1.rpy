image Zv2_MS1_p1 = "images/Bob_work/reception/M/scenes/Zv2_MS1/1.jpg"
image Zv2_MS1_p2 = "images/Bob_work/reception/M/scenes/Zv2_MS1/2.jpg"
image Zv2_MS1_p3 = "images/Bob_work/reception/M/scenes/Zv2_MS1/3.jpg"
image Zv2_MS1_p4 = "images/Bob_work/reception/M/scenes/Zv2_MS1/4.jpg"
image Zv2_MS1_p5 = "images/Bob_work/reception/M/scenes/Zv2_MS1/5.jpg"
image Zv2_MS1_p6 = "images/Bob_work/reception/M/scenes/Zv2_MS1/6.jpg"
image Zv2_MS1_p6a = "images/Bob_work/reception/M/scenes/Zv2_MS1/6a.jpg"
image Zv2_MS1_p7 = "images/Bob_work/reception/M/scenes/Zv2_MS1/7.jpg"

default Zuri_name = "Zuri"

label Zv2_MS1_label:
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
        if persistent.incest_patch == True:
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
        if persistent.incest_patch == True:
            MC "No- What?! I AM actually his son."
        else:
            MC "No- What?! I AM actually his tennant.."

        scene Zv2_MS1_p1

        Zuri "Really?"
        MC "Yes!"
        Zuri "Oh! Sorry! My bad!"
        $ Zv2_MS1_ask_boob_office = False
        jump Zv2_MS1_label2

    if Zv2_MS1_ask_boob_office == False:
        jump Zv2_MS1_label2

label Zv2_MS1_label2:
    if Zv2_MS1_ask_boob_office1 == 3:
        scene Zv2_MS1_p1 with dissolve
        Zuri "Hello, and welcome to Bayside Business Consultants."
        MC "There is someone in the office?"
        scene Zv2_MS1_p4 at pandown3
        if persistent.incest_patch == True:
            Zuri "Please follow me. I’ll take you to your Dad's office."
        else:
            Zuri "Please follow me. I’ll take you to Bob's office."
        MC "Thank you."
        jump Zv2_MS1_label3

    if Zv2_MS1_ask_boob_office == False:
        scene Zv2_MS1_p4 at pandown3

        Zuri "In that case - please follow me. I’ll take you to his office."
        MC "(Finally!)"
        MC "Thank you."

label Zv2_MS1_label3:
    scene Zv2_MS1_p5

    Zuri "Now, I do have to warn you - he is rather busy today, so you might not be able to stay with him for too long."
    Zuri "The company is going through a very delicate restructuring of our contracts right now."
    MC "I see. That’s not a problem."

    scene Zv2_MS1_p6
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*Knock Knock Knock*"
    $ renpy.music.stop(channel="sound", fadeout=1)
    Zuri "Sir? I have a visitor for you."
    Dad "Who is it?"
    MC "(She’s got such a short skirt on! Maybe I could steal a chance to peek at her panties?)"
    window hide
    menu:
        "Bend down and peek up her skirt.":
            scene Zv2_MS1_p6a

            MC "(Oh, very nice!)"
            MC "(Those panties are sooo thin: they barely cover anything!)"
            if persistent.incest_patch == True:
                MC "(I’d love to get into that ass! But there’s a fat chance of that happening - she’s Dad’s secretary!) "
            else:
                MC "(I’d love to get into that ass! But there’s a fat chance of that happening - she’s Bob’s secretary!)"
            jump Zv2_MS1_after_menu
        "It’s not worth the risk. Just play it safe.":

            scene Zv2_MS1_p6
            if persistent.incest_patch == True:
                MC "(I better just play it safe. If she catches me, she’ll likely never let me visit Dad again!)"
            else:
                MC "(I better just play it safe. If she catches me, she’ll likely never let me visit Bob again!)"

            if persistent.incest_patch == True:
                Zuri "It’s your son, Sir."
            else:
                Zuri "It’s your tennant, Sir."
            scene Zv2_MS1_p7
            Dad "Oh! [player_name]! Come on in!"
            if persistent.incest_patch == True:
                Zuri "On you go, Sir. Just try not to keep your father distracted from his job for too long, please."
            else:
                Zuri "On you go, Sir. Just try not to keep the boss distracted from his job for too long, please."
            MC "I’ll be mindful of that. Thanks, Zuri."
            Zuri "My pleasure."
            jump Zv2_MS1_after_menu

label Zv2_MS1_after_menu:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ Zv2_first_meet = False
    $ bob_office_locked = True
    $ can_hide_windows = False
    jump bob_office_M1
