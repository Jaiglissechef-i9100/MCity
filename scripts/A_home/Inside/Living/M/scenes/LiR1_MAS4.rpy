image LiR1_MAS4_p1 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/1.jpg"
image LiR1_MAS4_p2 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/2.jpg"
image LiR1_MAS4_p3 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/3.jpg"
image LiR1_MAS4_p4 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/4.jpg"
image LiR1_MAS4_p5 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/5.jpg"
image LiR1_MAS4_p6 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/6.jpg"
image LiR1_MAS4_p7 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/7.jpg"
image LiR1_MAS4_p8 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/8.jpg"
image LiR1_MAS4_p9 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/9.jpg"
image LiR1_MAS4_p10 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/10.jpg"
image LiR1_MAS4_p11 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/11.jpg"
image LiR1_MAS4_p12 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/12.jpg"
image LiR1_MAS4_p13 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/13.jpg"
image LiR1_MAS4_p14 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/14.jpg"
image LiR1_MAS4_p15 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/15.jpg"
image LiR1_MAS4_p16 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/16.jpg"
image LiR1_MAS4_p17 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/17.jpg"
image LiR1_MAS4_p18 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/18.jpg"
image LiR1_MAS4_p19 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/19.jpg"
image LiR1_MAS4_p20 = "/images/a_home/Inside/Bathroom/M/scenes/LiR1_MAS4/20.jpg"

label LiR1_MAS4_label:
    hide screen displayTextScreen
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if renpy.loadable("patch.rpy"):
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"
    scene black
    $ renpy.pause (1, hard = True)
    scene LiR1_MAS4_p1 with dissolve

    if renpy.loadable("patch.rpy"):
        MC "Hello? Auntie Liza? Yazmin?"
    else:
        MC "Hello? Liza? Yazmin?"
    MC "Anybody?!"
    MC "(Where the heck has everyone gone? Maybe they’re at work.)"

    scene LiR1_MAS4_p2

    "*Thud*"
    MC "Huh?"
    MC "(I think I heard a footstep from the bathroom.)"

    scene LiR1_MAS4_p3

    MC "(Holy shit! It’s [Liza2_name]!)"
    MC "(She must have just finished, having a bath. It looks like she’s getting changed.)"
    MC "(Wow! Just look at - the ass on her! It’s amazing!)"

    scene LiR1_MAS4_p4

    MC "(Goddamn... It’s a shame that she’s a lesbian. If she was bi, then I would have at least had - a small chance - of getting into her.)"
    MC "(Her skin is so smooth, as well. I’m getting so hard, just staring at those pantyhose, she’s wearing.)"
    Liza "C’mon... hook into place, for me..."

    scene LiR1_MAS4_p5

    Liza "There we go... Perfect!"
    MC "(Her tits are fucking huge! They might even be larger than [Mom_name]’s!)"
    MC "(Yazmin is a lucky woman. Imagine, getting to suck and lick those breasts, every night.)"

    scene LiR1_MAS4_p6

    Liza "Yeah... the white ones, suit me much better."
    Liza "(I don’t know why I ever thought, I should switch to grey.)"
    Liza "(Yazmin is going to LOVE these! I can’t wait to strip down to these, tonight, and go down on her. She’s going to cum soooo hard!)"

    scene LiR1_MAS4_p7

    MC "(Okay, this is getting a little bit dangerous... I should probably back away now, before [Liza2_name] catches me peeping in at her.)"
    MC "(She does have an incredible body though... I wish I had a camera with me, to snap some pictures.)"

    scene LiR1_MAS4_p8

    MC "(Mmm... It looks like she keeps her bush - trimmed neatly - as well.)"
    MC "(My cock would fit - so perfectly - in there. It would be so tight, too - she’s never been with a guy before, after all.)"

    scene LiR1_MAS4_p9

    Yazmin "(Well, well, well... What do we have here?)"
    Yazmin "Ahem!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    MC "Huh?!"
    MC "(Oh shit!)"

    scene LiR1_MAS4_p10

    Liza "Is that you home, Yazmin?"
    Yazmin "Yeah, that’s me home! I’m just going upstairs to the bedroom. I’ll see you in fifteen minutes?"
    Liza "Perfect! See you then, darling!"
    Yazmin "(Whispered) Okay, you little perv - follow me upstairs. We’re going to sort this out, right now."
    MC "(Fuck! I am in so much shit... At least Yazmin hasn’t given me up to [Liza2_name] yet.)"
    scene black
    $ renpy.pause(3,hard= True)
    scene LiR1_MAS4_p11
    if renpy.loadable("patch.rpy"):
        Yazmin "So... What am I to do with - the little pervert - spying on his auntie?"
    else:
        Yazmin "So... What am I to do with - the little pervert - spying on my wife?"
    MC "I... uh... was just looking for the... pool cleaning... stuff."
    Yazmin "You’re a miserable liar, kid. I should just - turn you in - to the cops, right now. Y’know that?"
    MC "W-wait! You don’t have to-"

    scene LiR1_MAS4_p12

    Yazmin "I’ll tell you what - I’ll make you a deal."
    MC "Anything!"
    Yazmin "Pull down your pants."
    MC "M-My pants?! Why?"

    scene LiR1_MAS4_p13

    Yazmin "Because I need to check something. Now, hurry up and do it, before I lose my patience with you."
    MC "Alright fine! Two seconds."
    MC "(What the hell does she want?)"
    MC "(Crap... I’m still hard from watching [Liza2_name]...)"

    scene LiR1_MAS4_p14

    Yazmin "Okay - that’s perfect... Hmm..."
    Yazmin "It’s been so long since I last saw one, in real life."
    MC "Are you not a lesbian?"
    Yazmin "I go both ways, kid. Now, just you stand right there."

    scene LiR1_MAS4_p15

    Yazmin "Yes... That’s probably about the right thickness."
    Yazmin "I just need to double check the length, then we can get this show on the road."

    scene LiR1_MAS4_p16

    Yazmin "Aha! There we go! I knew I had it - lying around in there - somewhere."
    MC "W-Wait! Is that a dildo?! You’re not planning to use that on me, are you?!"
    Yazmin "Hmm... I wasn’t - but you know something - that’s not a bad idea!"

    scene LiR1_MAS4_p17

    MC "WHAT?!"
    Yazmin "I’m teasing you..! Now, hold still. This will only take a second..."
    MC "Well, that’s a slight relief."

    scene LiR1_MAS4_p18

    Yazmin "Okay... your cock is, only a little bit bigger than my toy. Hardly noticeable - in the heat of the moment..."
    MC "Heat of the moment? What do you mean?"
    Yazmin "Oh yeah - this is perfect. Mmm... I can’t wait for tonight..."
    MC "Hello?"
    MC "(She can’t wait for tonight...?)"

    scene LiR1_MAS4_p19

    Yazmin "All done. You can go now!"
    MC "Wait - just like that? What about - you catching me-"
    if renpy.loadable("patch.rpy"):
        Yazmin "I said you can go now. Your aunt will be coming upstairs soon - and I HIGHLY doubt, you want to be standing in front of me with no pants on, when she comes in."
    else:
        Yazmin "I said you can go now. Liza will be coming upstairs soon - and I HIGHLY doubt, you want to be standing in front of me with no pants on, when she comes in."
    MC "Good point."

    scene LiR1_MAS4_p20

    MC "Are we square, then?"
    Yazmin "Eh... For now. I might need to borrow you again, in the future. But for the meantime, I have everything I need."
    MC "Okay. See you later, then... I guess."
    MC "(What does she mean, with that - waiting for tonight, though...?)"

    $ LiR1_NS1 = True
    $ LiR1_climbing = True
    $ LiR1_MAS4 = 3
    $ LiR1_MAS4can3 = False
    $ day_time += 1
    $ LiR1_MAS5_can2 = True

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump a_home_outside_M1
