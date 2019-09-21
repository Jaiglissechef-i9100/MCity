image MLR3_beach_house_wait_p1 = "images/Beach/MLR3_beach_event/House/Waiting/1.jpg"
image MLR3_beach_house_wait_p2 = "images/Beach/MLR3_beach_event/House/Waiting/2.jpg"
image MLR3_beach_house_wait_p3 = "images/Beach/MLR3_beach_event/House/Waiting/3.jpg"
image MLR3_beach_house_wait_p4 = "images/Beach/MLR3_beach_event/House/Waiting/4.jpg"
image MLR3_beach_house_wait_p5 = "images/Beach/MLR3_beach_event/House/Waiting/5.jpg"
image MLR3_beach_house_wait_p6 = "images/Beach/MLR3_beach_event/House/Waiting/6.jpg"
image MLR3_beach_house_wait_p7 = "images/Beach/MLR3_beach_event/House/Waiting/7.jpg"
image MLR3_beach_house_wait_p8 = "images/Beach/MLR3_beach_event/House/Waiting/8.jpg"
image MLR3_beach_house_wait_p9 = "images/Beach/MLR3_beach_event/House/Waiting/9.jpg"
image MLR3_beach_house_wait_p10 = "images/Beach/MLR3_beach_event/House/Waiting/10.jpg"
image MLR3_beach_house_wait_p11 = "images/Beach/MLR3_beach_event/House/Waiting/11.jpg"

label MLR3_b_house_wait:

    scene b_house_bedroom_N_map
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if MLR3_b_house_wait == 1:

        scene MLR3_beach_house_wait_p1 with dissolve

        MC "(Damn, that looks like a REALLY comfy bed.)"
        MC "(This is where I’ll be sleeping with [Mom_name] tonight, then.)"

        scene MLR3_beach_house_wait_p2

        MC "(After all these weeks, it’s FINALLY going to happen. And there is no one around to interrupt us.)"
        MC "(We’ll make the most of tonight.)"

        scene MLR3_beach_house_wait_p3

        MC "(Hmm, very soft! This will be perfect for fucking on, together!)"
        MC "(I wonder what she needs ten minutes to do, before we meet?)"

        scene MLR3_beach_house_wait_p4

        MC "Pfft... "
        MC "(Ugh… It’s been like two minutes and I’m already bored!)"

        scene MLR3_beach_house_wait_p5

        MC "([Mom_name] was talking, earlier on… about time going faster, the older you got.)"
        MC "(I sure wish it would speed up right now, so we could both get started!)"

        scene MLR3_beach_house_wait_p6

        MC "(I wonder if this will be the night that I finally fuck her?)"
        MC "(What position will we do it in the first time?"
        MC "(I still have that condom with me, that [Dad_name] gave me too. So I’ve got protection. There’s nothing that should come in the way of us getting together.)"
        MC "(I guess I’ll check out the bathroom while I’m waiting.)"

        $ MLR3_b_house_wait = 2
        $ can_hide_windows = False
        jump b_house_bedroom_M1

    if MLR3_b_house_wait == 2:

        scene MLR3_beach_house_wait_p7 with dissolve

        MC "Wow! This place is huge!"
        MC "Holy shit… It looks like it belongs in a mansion!"

        scene MLR3_beach_house_wait_p8

        MC "(This is like the most modern bathroom I’ve ever seen!)"
        MC "(No wonder [Mom_name] loves renting this place)"

        scene MLR3_beach_house_wait_p9

        MC "(A walk-in shower? It would be so fun to fuck [Mom_name], in that!)"
        MC "I’m getting all excited at the thought of fucking her, up against the wall of the shower.)"

        scene MLR3_beach_house_wait_p11

        MC "(Alright, it’s been WAY over ten minutes. Let’s go and see what [Mom_name]’s up to.)"
        MC "(I have to admit, I’m starting to feel a little bit nervous!)"

        $ MLR3_b_house_wait = 3
        $ can_hide_windows = False
        $ can_b_living_room = True
        jump b_house_bath_M1
