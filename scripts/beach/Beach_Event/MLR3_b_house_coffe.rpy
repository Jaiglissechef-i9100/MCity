image MLR3_b_house_coffe_p1 = "images/Beach/MLR3_beach_event/House/MorningCoffie/1.jpg"
image MLR3_b_house_coffe_p2 = "images/Beach/MLR3_beach_event/House/MorningCoffie/2.jpg"
image MLR3_b_house_coffe_p3 = "images/Beach/MLR3_beach_event/House/MorningCoffie/3.jpg"
image MLR3_b_house_coffe_p4 = "images/Beach/MLR3_beach_event/House/MorningCoffie/4.jpg"
image MLR3_b_house_coffe_p5 = "images/Beach/MLR3_beach_event/House/MorningCoffie/5.jpg"
image MLR3_b_house_coffe_p6 = "images/Beach/MLR3_beach_event/House/MorningCoffie/6.jpg"
image MLR3_b_house_coffe_p7 = "images/Beach/MLR3_beach_event/House/MorningCoffie/7.jpg"
image MLR3_b_house_coffe_p8 = "images/Beach/MLR3_beach_event/House/MorningCoffie/8.jpg"
image MLR3_b_house_coffe_p9 = "images/Beach/MLR3_beach_event/House/MorningCoffie/9.jpg"
image MLR3_b_house_coffe_p10 = "images/Beach/MLR3_beach_event/House/MorningCoffie/10.jpg"
image MLR3_b_house_coffe_p11 = "images/Beach/MLR3_beach_event/House/MorningCoffie/11.jpg"
image MLR3_b_house_coffe_p12 = "images/Beach/MLR3_beach_event/House/MorningCoffie/12.jpg"
image MLR3_b_house_coffe_p13 = "images/Beach/MLR3_beach_event/House/MorningCoffie/13.jpg"

label MLR3_b_house_coffe:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene b_house_living_M_map
    scene MLR3_b_house_coffe_p1 with dissolve
    $ can_hide_windows = True
    Mom "*Sniff*"
    Mom "Ahh…"
    Mom "(The landlord always buys good coffee for this place. This new Colombian variety is excellent!)"

    scene MLR3_b_house_coffe_p2

    Mom "Ah, you’re finally awake. How are you feeling?"
    MC "Honestly? Absolutely drained…"
    Mom "Hehe, you really did give it your all last night. Grab a cup and help yourself to some coffee. I filled up a pot on the table."

    scene MLR3_b_house_coffe_p3

    MC "Thanks, [Mom_name]. This smells really strong."
    Mom "Trust me, it’s exactly what you need to pick you up after last night."
    MC "I hope it’s not too bitter..."

    scene MLR3_b_house_coffe_p4

    Mom "It’s fine, honestly, it’s only the first couple of sips that taste bitter. After that your senses adjust."
    Mom "Mine’s a tad hot though. Kinda like you last night."

    scene MLR3_b_house_coffe_p5

    MC "Haha… okay…"
    Mom "God you were so hot. I loved bouncing up and down on that big fat cock of yours."
    MC "Umm, can I at least finish my coffee before we start thinking about a round three?"

    scene MLR3_b_house_coffe_p6

    MC "If you keep this up there’ll be nothing left of me! Haha!"
    Mom "Think of it as good exercise."
    Mom "And on that subject, I think you and me will be doing a LOT more exercise together in future."

    scene MLR3_b_house_coffe_p7

    MC "Mmm, I’ll be looking forward to that. It’s a shame that we won’t have as much free time together when we get back home."
    Mom "Yeah, I know…"
    Mom "I’m trying not to think about that right now to be honest."

    scene MLR3_b_house_coffe_p8

    MC "*Sip*"
    Mom "*Sip*"
    MC "(Huh, this stuff isn’t actually that bad!)"

    scene MLR3_b_house_coffe_p9

    Mom "Well, that’s me done. I’ll leave you here to finish yours - make sure you drink it all."
    MC "Don’t worry, I will."
    Mom "There’s extra in the pot if you want second round."

    scene MLR3_b_house_coffe_p10

    Mom "In the meantime I’ll be washing down my body in the shower."
    Mom "Lathering up my big breasts with soap and scrubbing them clean."

    scene MLR3_b_house_coffe_p11

    Mom "Enjoying the hot water flowing over my naked voluptuous body."
    Mom "Trying not to think about you and your hard dick as I feel the shower blast against me."

    scene MLR3_b_house_coffe_p12

    Mom "Well, I’ll see you after you finish your coffee."
    MC "(Huh, that was weird… why was [Mom_name] being so descriptive about her shower? Is she just trying to turn me on again?)"

    scene MLR3_b_house_coffe_p13

    MC "(Wait a minute - maybe she wants me to shower WITH her?!)"
    MC "(I’m not certain, but I think I should go and check. What’s the worst thing that could happen? She might laugh and kick me out of the shower.)"
    MC "(If I’m right that she wants to have shower sex, then I better down a second cup of coffee quickly!)"
    $ clickable = True
    $ MLR3_b_house_wait = 5
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump b_house_living_M1

