image neighboor_spy_v1_p2 = "images/home/mc_room/morning/scenes/neighboor_spy/2.jpg"
image neighboor_spy_v1_p3 = "images/home/mc_room/morning/scenes/neighboor_spy/3.jpg"
image neighboor_spy_v1_p4 = "images/home/mc_room/morning/scenes/neighboor_spy/4.jpg"
image neighboor_spy_v1_p5 = "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"
image neighboor_spy_v1_p6 = "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
image neighboor_spy_v1_p7 = "images/home/mc_room/morning/scenes/neighboor_spy/7.jpg"
image neighboor_spy_v1_p8 = "images/home/mc_room/morning/scenes/neighboor_spy/8.jpg"

image mc_spy_morning = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingMorningAfternoon.png"
image mc_spy_evening = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingEvening.png"
image mc_spy_night = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingNight.png"

image neighboor_spy_v1_p5and6_animation:
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

define Neighbor2 = Character("???", color="#66CC33")
define Neighbor1 = Character("???", color="#CC00CC")
init -1 python:
    def play_effect(trans, st, at):
        renpy.play("sfx/slap.mp3", channel="sound")
label neighboor_spy_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if binoculars.selected:
        if day_time == 1:
            show screen mc_room_morning_notclickable
        if day_time == 2:
            show screen mc_room_day_notclickable
        if day_time == 3:
            show screen mc_room_evening_notclickable
        if day_time == 4:
            show screen mc_room_night_notclickable
        menu:
            "Spy on the Neighbor on the right.":

                if day_time == 2:
                    $ renpy.show("mc_spy_morning", layer="screens")
                    $ renpy.music.stop(channel="music2", fadeout=1)
                    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
                    MC "Okay. Let’s see if there’s anything interesting happening."
                    MC "Ah! Yep! There’s some action!"

                    hide screen mc_room_day_notclickable
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    scene neighboor_spy_v1_p2 with dissolve
                    $ can_hide_windows = True
                    Neighbor1 "You’ve been a very bad girl! You need a painful punishment!"
                    Neighbor2 "No! Please no! I promise I'll try harder at school!"
                    Neighbor1 "Do you know how many times you have already promised me that?"
                    Neighbor2 "This time will be different!! "
                    Neighbor1 "I was too soft on you, since the beginning! "
                    Neighbor2 "… "

                    scene neighboor_spy_v1_p3
                    Neighbor2 "I’ll be not able to sit for a few days, again!"
                    Neighbor1 "You should have thought about that earlier!"
                    Neighbor2 "I was! I was studying for hours! But I’m telling you, that Math teacher hates me!"
                    Neighbor1 "*Sigh* Excuse after excuse."
                    Neighbor1 "It seems, this time, you need a better example of what I will do to you, if you do not start learning properly!"

                    scene neighboor_spy_v1_p4
                    Neighbor2 "(Gosh! Why!? Why me!? This fucking whore, Celia! Stuuuuupid bitch!)"
                    Neighbor1 "Please don't hate me, after this - I’m doing it for your own good."
                    Neighbor2 "(I’m sure you do... Why can’t you just believe me!?)"

                    scene neighboor_spy_v1_p5
                    Neighbor2 "(Oh, no! It’s going to start in a moment!)"
                    Neighbor1 "Here it comes!"
                    $ renpy.sound.play("sfx/slap.mp3", channel="sound")

                    scene neighboor_spy_v1_p6
                    Neighbor2 "Ahh!!! NOOO!!"
                    Neighbor1 "Please be quiet! Handle it like a woman!"

                    scene neighboor_spy_v1_p5and6_animation
                    $ renpy.pause(6, hard= True)

                    scene neighboor_spy_v1_p7
                    Neighbor2 "Enough! That’s ENOUGH! I BEG YOU! N-No!"
                    Neighbor1 "*Sigh* Fine."

                    scene neighboor_spy_v1_p8
                    Neighbor1 "It’s now time to apologize for your bad behavior."
                    Neighbor1 "You know what you have to do, isn’t that right?"
                    Neighbor2 "*Snip* Yes… "
                    Neighbor1 "Then stand up, and straight to the bedroom. I ALSO have my needs."
                    Neighbor2 "*Snip* Okay… "
                    scene mc_room_day
                    show screen mc_room_day_notclickable
                    $ renpy.show("mc_spy_morning", layer="screens")
                    MC "Damn... They went to another room…."
                    MC "I seriously need to investigate them! "
                    MC "I could talk to her at school or go to their house and say ‘hello', since I’m their neighbor."
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    $ Neighboor_spy_mc_room = False
                    $ neighboor_unlocked = True
                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False
                    jump mc_room_morning1
                else:



                    if day_time == 1:
                        $ renpy.show("mc_spy_morning", layer="screens")


                    if day_time == 3:
                        $ renpy.show("mc_spy_evening", layer="screens")


                    if day_time == 4:
                        $ renpy.show("mc_spy_night", layer="screens")


                    MC "Okay. Let’s see if there’s anything interesting happening."
                    MC "Hmm… Nothing. Well maybe at a different time of the day."
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    $ renpy.hide("mc_spy_night", layer="screens")
                    $ renpy.hide("mc_spy_evening", layer="screens")
                    $ can_hide_windows = False
                    jump mc_room_morning1
            "Back.":
                $ can_hide_windows = False
                jump mc_room_morning1


    if not binoculars.selected:
        if day_time == 1:
            show screen mc_room_morning_notclickable
        if day_time == 2:
            show screen mc_room_day_notclickable
        if day_time == 3:
            show screen mc_room_evening_notclickable
        if day_time == 4:
            show screen mc_room_night_notclickable
        $ renpy.hide("mc_spy_morning", layer="screens")
        $ renpy.hide("mc_spy_night", layer="screens")
        $ renpy.hide("mc_spy_evening", layer="screens")
        MC "It’s just a window... with a nice view to my neighbour’s. But they're too far away, to see anything with just my eyes."
        $ can_hide_windows = False
        jump mc_room_morning1