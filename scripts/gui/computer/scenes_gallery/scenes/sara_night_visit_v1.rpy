label sara_night_visit_v1:
    hide screen scenes_gallery
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "…"
    Sara "(I wonder if he’s definitely asleep.)"
    Sara "[player_name]? Are you up?"
    MC "…"

    scene mc_sara_night_scene1_v1_p2
    Sara "(Okay, you can do this, Sara. Be brave!)"
    Sara "(You have to get this picture of his cock, for Lily.)"
    Sara "(Then you can prove that you’re one of the cool kids, and not just a nerdy virgin!)"

    scene mc_sara_night_scene1_v1_p3
    Sara "(Hey, this is easier than I thought it would be! He’s only in his boxer shorts!)"
    Sara "(I just need to strip these off him, then start moving his cock until it gets, all stiff and hard…)"
    Sara "(...like that time in my bedroom, when he pressed it up against my belly.)"

    scene mc_sara_night_scene1_v1_p4
    Sara "(Wow… It always takes my breath away, each time I see it!)"
    Sara "(It feels like there’s a hundred tiny butterflies in my belly right now!)"
    Sara "(I don’t think I even need to move his cock at all… it’s already quite stiff!)"

    scene mc_sara_night_scene1_v1_p5
    Sara "(I’ll just take a quick picture of it, then sneak out of his bedroom.)"
    Sara "([player_name] won’t even know I was in here! Haha! Prefect!)"
    Sara "(On the other hand… maybe I could touch his cock, just a little bit…)"

    scene mc_sara_night_scene1_v1_p6
    Sara "(Yeah, I should rub it a bit - just to get a better picture, of course.)"
    Sara "(Wow… it’s getting so much bigger and harder!)"
    Sara "(I wonder how long I should do this for?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p7
    MC "Boo!"
    Sara "EEEKKK!"
    Sara "(AHHH! He woke up!)"

    scene mc_sara_night_scene1_v1_p8
    Sara "I- I- *Sniff* I’m s-so sorry!"
    MC "What are you doing?"
    Sara "I was… I was… *sob* t-trying to take a… picture…"
    MC "Don’t you already have one on your phone?"

    scene mc_sara_night_scene1_v1_p9
    Sara "I… wanted another…"
    Sara "Please forgive me. I’m sooo sorry! *Sob*"
    if persistent.incest_patch == True:
        Sara "I’ll- I’ll do anything! Just don’t tell Dad!"

        scene mc_sara_night_scene1_v1_p10
        MC "Hey - relax. I won’t tell Dad."
    else:
        Sara "I’ll- I’ll do anything! Just don’t tell Landlord!"

        scene mc_sara_night_scene1_v1_p10
        MC "Hey - relax. I won’t tell Landlord."
    Sara "Th-Thank you. *Sniff* I’ll do anything for you."
    Sara "O-Or to you!"

    scene mc_sara_night_scene1_v1_p11
    MC "Come on into bed and sleep beside me tonight."
    Sara "Th...that’s all?"
    MC "Yeah, come on in beside me. It’s warm under the covers."

    scene mc_sara_night_scene1_v1_p12
    Sara "Th...thank you… I’m so sorry. *Sniff*"
    MC "Hey - it’s alright. Dry your eyes. Try to breathe."
    MC "If you were THAT desperate for a picture of my junk, you could have just asked."

    scene mc_sara_night_scene1_v1_p13
    Sara "Hehe… You always make me laugh so easily…"
    MC "That’s better. Let’s get rid of those tears."
    MC "I’ll shuffle over here, so there’s room for you."

    scene mc_sara_night_scene1_v1_p14
    Sara "Thanks, [player_name]..."
    MC "You still look a little stressed. Is everything alright?"
    Sara "Actually… I wanted to ask you something..."

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)
    scene mc_sara_night_scene1_v1_p15
    Sara "D...Do you… like me?"
    Sara "B-Because after everything that happened - with the videogames, Lily, you.. and me..."
    Sara "Y-you said.. I’m nice.. s-sexy..."
    Sara "I… I just need to know…"

    menu:
        "Yes, Sara. I really like you.":

            Sara "(Please say yes…)"
            MC "Yes, Sara. I really like you."
            scene mc_sara_night_scene1_v1_p16a
            MC "Honestly, I thought it would have been pretty obvious."
            Sara "(Oh, my God!)"

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "I- I- I can’t believe I just asked you that. G-Go back to sleep."
            Sara "Forget what I just said!"
            if persistent.incest_patch == True:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your brother!)"
            else:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! )"
            MC "(Huh?! Women are strange…)"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice1r
        "Stay silent.":


            scene mc_sara_night_scene1_v1_p17
            if persistent.incest_patch == True:
                Sara "Because I think I like you… more than a brother..."
            else:
                Sara "Because I think I like you… more than a friend..."
            MC "…"
            Sara "(Please say yes…)"
            MC "…"
            Sara "(Please, [player_name]… say anything...)"
            MC "…"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "N-Nevermind! I- Forget I asked you about it!"
            if persistent.incest_patch == True:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your brother!)"
            else:
                Sara "(Stupid, Sara! How could he ever love a nerdy virgin like you?! And he’s your friend!)"
            Sara "(You shouldn’t have put him in that position! You could ruin your relationship with him!)"
            MC "Are you okay, Sara?"
            Sara "J-Just go to sleep, you b-big dumbo!"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice1r

label after_mc_sara_night_scene1_v1_choice1r:

    scene mc_sara_night_scene1_v1_p19
    MC "(YAWN!)"
    MC "(Looks like Sara left during the night. I wonder when she snuck out. I’ll probably see her around school today anyway.)"
    MC "(I’ve never seen her that emotional before.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label

