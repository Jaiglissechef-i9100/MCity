image CR3_AS7_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS7/1.jpg"
image CR3_AS7_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS7/2.jpg"
image CR3_AS7_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS7/3.jpg"
image CR3_AS7_p4 = "images/cloth_shop/room1/day/scenes/CR3_AS7/4.jpg"

label CR3_AS7_label:
    if CR3_AS7a_can1 == True:
        hide screen map_button
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I should steal her vibrator. It's a good time for that while she's in the shop."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    if CR3_AS7_can == False:
        hide screen map_button
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I've already talked to her."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    hide screen map_button
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer

    scene CR3_AS7_p1 with dissolve

    MC "Afternoon, Caroline! How can I help today?"
    Caroline "Hey, [player_name]. There’s honestly, not much you can do right now."
    MC "Huh? Why? Is something wrong?"

    scene CR3_AS7_p2

    Caroline "God no! Nothing’s wrong. We just, sold out of our stock. I’m currently waiting for the next batch to be delivered."
    MC "Really?! That’s amazing, Caroline! Congratulations!"
    Caroline "Yeah, those pictures we took are spreading on the internet - like wildfire. The online store, even crashed from having too many visitors, last night!"

    scene CR3_AS7_p3

    Caroline "So yeah, I’m basically down to, whatever you see sitting around. There’s been a few customers today, but most people seem interested in waiting, until they see the new stuff."
    MC "Have you any idea when it will arrive?"
    Caroline "Hopefully in the next few days. Just keep checking back with me."

    scene CR3_AS7_p4

    MC "Okay, I guess I’ll enjoy my day off, then!"
    Caroline "No problem! Have fun, [player_name]!"
    MC "Catch you later, Caroline."
    $ CR3_AS7_can = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump cloth_shop_open_label

label CR3_AS7_outfit4_lock:
    hide screen map_button
    $ clickable = False
    show screen cloth_shop_robber_screen
    MC "I've already talked to her."
    $ clickable = True
    hide screen cloth_shop_robber_screen
    jump cloth_shop_open_label

