image ml_morning_salon_scene2_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/2.jpg"
image ml_morning_salon_scene2_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/3.jpg"
image ml_morning_salon_scene2_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/4.jpg"
image ml_morning_salon_scene2_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/5.jpg"
image ml_morning_salon_scene2_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/6.jpg"
image ml_morning_salon_scene2_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/7.jpg"

label ml_salon_morning_scene_dish_wash_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_morning_salon_scene2_v1_p2 with dissolve
    $ can_hide_windows = True
    MC "(There we go… That’s most of them.)"
    MC "(They must have been left-over from last night’s dinner.)"

    scene ml_morning_salon_scene2_v1_p3
    if persistent.incest_patch == True:
        MC "(I wonder why Mom didn’t just stick them in the dishwasher.)"
    else:
        MC "(I wonder why Linda didn’t just stick them in the dishwasher.)"
    MC "(Anyway, this is the last one.)"
    MC "(It’s a good thing too - any more and I would have been late for school!)"

    scene ml_morning_salon_scene2_v1_p4
    Mom "Thank you so much for doing those for me!"
    Mom "You have no idea how much, you helping around the house, means to me."
    if persistent.incest_patch == True:
        MC "Yeah, it’s no problem. Happy to help, Mom."
    else:
        MC "Yeah, it’s no problem. Happy to help, Linda."

    scene ml_morning_salon_scene2_v1_p5
    if persistent.incest_patch == True:
        Mom "Your father is terrible when it comes to chores."
    else:
        Mom "Bob is terrible when it comes to chores."
    Mom "Never puts his clothes in the wash. Never scrapes his plate clean after meals."
    Mom "You’re a real man."

    scene ml_morning_salon_scene2_v1_p6
    MC "(A real man?!)"
    if persistent.incest_patch == True:
        MC "(Mom’s acting very… intimate again.)"
    else:
        MC "(Linda’s acting very… intimate again.)"
    MC "(Maybe it’s got something to do with her hormones or something?)"
    MC "(Girls are weird…)"

    scene ml_morning_salon_scene2_v1_p7
    Mom "(Sniff…)"
    Mom "(Mmm… God… he smells so good.)"
    Mom "(I’d love to just, lie naked beside him and cuddle him all night-)"
    Mom "(Shit! I’m getting far too involved in these fantasies again.)"

    scene black
    Mom "You better go to school! Hurry up! Get a move on!"
    MC "Yeah, I’ll just dry the plates-"
    Mom "No time! Chop chop!"
    MC "Okay, I’m going! (Geez, what got into her?)"
    $ ml_can_salon_morning_scene_dish_wash = 3
    $ ml_salon_morning_visit = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump kitchen_morning1
