image caroline_cloth_shop_afternoon_scene2_p1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/1.jpg"
image caroline_cloth_shop_afternoon_scene2_p2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/2.jpg"
image caroline_cloth_shop_afternoon_scene2_p3 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/3.jpg"
image caroline_cloth_shop_afternoon_scene2_p4 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/4.jpg"
image caroline_cloth_shop_afternoon_scene2_p5 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/5.jpg"
image caroline_cloth_shop_afternoon_scene2_p6 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/6.jpg"
image caroline_cloth_shop_afternoon_scene2_p7 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/7.jpg"
image caroline_cloth_shop_afternoon_scene2_p8 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/8.jpg"
image caroline_cloth_shop_afternoon_scene2_p9 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/9.jpg"
image caroline_cloth_shop_afternoon_scene2_p10 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/10.jpg"
image caroline_cloth_shop_afternoon_scene2_p11 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/11.jpg"
image caroline_cloth_shop_afternoon_scene2_p12 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/12.jpg"
image caroline_cloth_shop_afternoon_scene2_p13 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/13.jpg"
image caroline_cloth_shop_afternoon_scene2_p14 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/14.jpg"

label caroline_cloth_shop_afternoon_scene2_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_cloth_shop_afternoon_scene2_p1 with dissolve
    Caroline "This one’s a little bit embarrassing."
    MC "Relax! It’s just for your business, remember? Think of the sales you’ll make!"
    Caroline "Yeah, I suppose so."

    scene caroline_cloth_shop_afternoon_scene2_p2
    MC "You do look great in it, by the way."
    Caroline "Aww - you don’t have to say that. It’s AT LEAST one size too small, on me, anyway!"
    Caroline "Just look at how tight it is!"
    MC "(It sure is!)"

    scene caroline_cloth_shop_afternoon_scene2_p3
    Caroline "I’m off to get changed over here."
    MC "No problem, Caroline."
    MC "(Damn, that’s a REALLY skinny thong on that costume!)"

    scene caroline_cloth_shop_afternoon_scene2_p4
    MC "(Hmm... she normally takes a while to change out of her cosplay outfits.)"
    MC "(Maybe I’ll have enough time to peek at her while she’s undressing!)"
    MC "(Just a little bit closer…)"

    scene caroline_cloth_shop_afternoon_scene2_p5
    MC "(Here we go - perfect view.)"
    MC "(I’m well hidden, so she won’t be able to see me - and I can duck around the corner if she turns quickly.)"
    MC "(Time to sit back and enjoy the show!)"

    scene caroline_cloth_shop_afternoon_scene2_p6
    MC "(C’mon, Caroline. Time to undress…)"
    MC "(Let’s see those big titties of yours!)"

    scene caroline_cloth_shop_afternoon_scene2_p7
    MC "(Okay. She’s searching the drawer for her clothes.)"
    MC "(God, my heart’s racing right now! Just a few more seconds, and she’ll be-)"

    scene black
    $ renpy.sound.play("sfx/shelf_fall.mp3")
    MC "WHOOAAAAA!"

    scene caroline_cloth_shop_afternoon_scene2_p8 with dissolve
    Caroline "Eeek!"
    Caroline "Wh-What the hell?!"
    MC "Ouch…"
    MC "(Fuck! The shelf broke, as I was leaning on it!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music2", loop=True, fadein = 2)
    scene caroline_cloth_shop_afternoon_scene2_p9

    Caroline "[player_name]! What the FUCK were you doing?!"
    MC "I… um…"
    window hide
    menu:
        "Err… I was… dusting the shelf!":

            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "I was… err… dusting the shelf!"
            Caroline "Oh really?"
            MC "Y-Yeah?"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "With what?! You CLEARLY don’t have a cloth or any polish!"
            Caroline "PLUS, I dusted this whole place, like two hours ago!"
            MC "OW! OW!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu
        "I… um… was checking if you needed any help!":


            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "I was… um… checking if you needed any help!"
            Caroline "You were checking if I needed any help changing?"
            MC "Yeah- I mean, NO! Err…"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "You disgusting little pervert!"
            if renpy.loadable("patch.rpy"):
                Caroline "I’m your sister!"
            if not renpy.loadable("patch.rpy"):
                Caroline "I’m your friend!"
            MC "Ouch! Ahh! I’m sorry!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu
        "I saw a… big… um… spider! And I had to try and catch it!":


            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "I saw a… big… spider… over on the uhh… shelf!"

            scene caroline_cloth_shop_afternoon_scene2_p11
            Caroline "A big spider, Huh?"
            MC "Y-Yeah! A tarantula or something…"
            Caroline "You’re an awful liar."
            MC "N-No! Really! It was… uh…"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "It’s bad enough that you were spying on me while I changed…"
            MC "OW! I’M SORRY!"
            Caroline "But then you had to go and make things WORSE by lying to me!"
            Caroline "Do you think I’m stupid?!"
            MC "I’m sorry!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu

label caroline_cloth_shop_afternoon_scene2_after_menu:
    scene caroline_cloth_shop_afternoon_scene2_p12
    Caroline "WHAT THE FUCK?!"
    MC "Huh?"
    Caroline "You’ve got a boner!"
    MC "(Jesus Christ! Not now!)"

    scene caroline_cloth_shop_afternoon_scene2_p13
    MC "I-I’m sorry! I have no control over it!"
    Caroline "Yes you do! You were the one SPYING on me!"
    MC "(Damn, she actually has a point there…)"

    scene caroline_cloth_shop_afternoon_scene2_p14
    Caroline "Get out of my store, this instant."
    Caroline "Tonight, when I get home, we’re going to have a VERY serious discussion about boundaries."
    MC "I’m sorry, Caroline."
    Caroline "Just leave."
    $ caroline_after_cosplay_outfit5 = False
    $ day_time = 3
    $ caroline_salon_evening_scene1 = False
    $ caroline_mc_room_evening_scene2 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
