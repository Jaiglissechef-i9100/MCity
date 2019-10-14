image CR3_MS3_p1 = "/images/home/caroline_room/morning/scenes/CR3_MS3/1.jpg"
image CR3_MS3_p2 = "/images/home/caroline_room/morning/scenes/CR3_MS3/2.jpg"
image CR3_MS3_p3 = "/images/home/caroline_room/morning/scenes/CR3_MS3/3.jpg"
image CR3_MS3_p4 = "/images/home/caroline_room/morning/scenes/CR3_MS3/4.jpg"
image CR3_MS3_p5 = "/images/home/caroline_room/morning/scenes/CR3_MS3/5.jpg"
image CR3_MS3_p6 = "/images/home/caroline_room/morning/scenes/CR3_MS3/6.jpg"
image CR3_MS3_p7 = "/images/home/caroline_room/morning/scenes/CR3_MS3/7.jpg"
image CR3_MS3_p8 = "/images/home/caroline_room/morning/scenes/CR3_MS3/8.jpg"

label CR3_MS3_label:
    if CR3_MS3_can == False:
        hide screen map_button
        show screen caroline_room_morning_not_clickable
        MC "She asks me to leave her alone."
        hide screen caroline_room_morning_not_clickable
        jump caroline_room_morning1
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR3_MS3_p1 with dissolve

        Caroline "Twenty, forty, sixty, eighty…"
        MC "(What’s she doing with all that money on her bed?)"
        MC "Holy crap, Caroline! Did you win big, on a scratchcard?!"

        scene CR3_MS3_p2

        Caroline "Haha! Not quite! This is today’s takings from the cosplay shop."
        MC "Wow... How much is there?"
        Caroline "Well, before you interrupted me, I’d counted to $780."
        MC "HOLY SHIT!"

        scene CR3_MS3_p3

        Caroline "It sounds a lot - but you have to remember, I probably spent $350, buying the outfits. I then have to pay, tax, rent, insurance, and put money into my pension."
        MC "Ugh... That sounds rough. How much do your reckon you’ll be left with?"
        Caroline "Maybe $150 -ish. It isn’t too bad. Multiply that out, and I’m pulling home $750, in profit each week. "

        scene CR3_MS3_p4

        Caroline "Not too bad, for a a girl in her early twenties, is it?"
        MC "That’s amazing, Caroline!"
        Caroline "I know! And it keeps growing, each week!"

        scene CR3_MS3_p5

        MC "Out of interest - why have you got it all over your bed? I’ve never seen you waving around money before."
        Caroline "Honestly? I used to store everything at the shop. After the robbery, I just don’t feel safe, leaving my valuables there anymore."
        MC "Yeah, I get that. It makes sense. What are you planning to do with it now?"
        Caroline "I’m putting some in the bank, but the rest, I’m stashing away in my room."

        scene CR3_MS3_p6

        MC "Why aren’t you putting it all in the bank?"
        Caroline "Haha! I have a couple of reasons. Firstly, if my business ever goes bankrupt, then I can hide some assets from them. Did you know that thirty percent of new businesses, fail during their first two years?"
        MC "Wow! I didn’t know that."
        Caroline "Almost half fail, in the first five years. Keeping cash, over a liquid asset, only makes sense. Even if it isn’t generating me interest I’ve got a nest egg, that I can fall back on."

        scene CR3_MS3_p7

        MC "So, what are you doing with that all, now?"
        Caroline "I’m about to look for a new hiding place. So, I’m gonna need you to do something for me."
        MC "Sure! Anything!"

        scene CR3_MS3_p8

        Caroline "Turn around and leave my room, so I can hide my money! Haha!"
        MC "Aww... Fine!"
        Caroline "Haha! See you later, [player_name]!"
        $ CR3_MS3_can = False
        $ CR3_AS7a_can2 = True

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump caroline_room_morning1
