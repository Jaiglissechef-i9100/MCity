image caroline_cloth_shop_afternoon_scene1_p1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/1.jpg"
image caroline_cloth_shop_afternoon_scene1_p2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/2.jpg"
image caroline_cloth_shop_afternoon_scene1_p3 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/3.jpg"
image caroline_cloth_shop_afternoon_scene1_p4a = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/4a.jpg"

image caroline_cloth_shop_afternoon_scene1_gotcamerap1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/Got_camera/1.jpg"
image caroline_cloth_shop_afternoon_scene1_gotcamerap2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/Got_camera/2.jpg"

label caroline_cloth_shop_afternoon_scene1_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_cloth_shop_afternoon_scene1 == True and caroline_cloth_shop_have_camera == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene1_p1 with dissolve
        MC "Afternoon, Caroline!"
        Caroline "Hiiii, [player_name]!"
        Caroline "Perfect timing - I’ve just finished planning my idea to save the shop!"
        MC "Great! How can I help?"

        scene caroline_cloth_shop_afternoon_scene1_p2
        Caroline "Okay, listen to this. I’ve got a three point plan."
        Caroline "One - I’m going to order in a new range of cosplay outfits."
        Caroline "Two - I’m going to market these by modelling them and putting the pictures online."

        scene caroline_cloth_shop_afternoon_scene1_p3

        Caroline "Which leads me into point three - I’m starting an online store too!"
        Caroline "This will hopefully increase my annual turnover enough, to make a profit."
        MC "Sounds like a great idea! What do you need me to do?"
        Caroline "Can you take some pictures of me in the outfits?"
        MC "Of course!"

        scene caroline_cloth_shop_afternoon_scene1_p4a
        Caroline "Umm… there’s just one tiny problem."
        Caroline "I don’t have a camera."
        MC "Ah… Right."
        Caroline "If you can get one, come on back and we’ll begin."
        Caroline "I need to continue building my online catalogue."
        MC "Okay, Caroline. I’ll go and find a camera."
        $ caroline_cloth_shop_afternoon_scene1 = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ caroline_cloth_shop_have_camera = 2
        $ can_hide_windows = False
        jump cloth_shop_open_label

    if caroline_cloth_shop_afternoon_scene1 == False and not camera1 in inventory.items:
        scene caroline_cloth_shop_afternoon_scene1_p1 with dissolve
        Caroline "Hey, [player_name]. Did you manage to get any camera?"
        MC "Not yet."
        $ can_hide_windows = False
        jump cloth_shop_open_label

    if camera1 in inventory.items and caroline_cloth_shop_have_camera == 2:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene1_gotcamerap1 with dissolve
        MC "Hey, Caroline! I found a camera!"
        Caroline "Amazing, [player_name]! It looks like a really good one too."
        Caroline "I’m ready to begin doing some modelling sessions, with the clothes, whenever you’re ready."

        scene caroline_cloth_shop_afternoon_scene1_gotcamerap2
        Caroline "You’re doing the hard work - so how about you pick an outfit?"
        Caroline "Try and focus on getting good camera angles."
        Caroline "Better pictures means more sales, which means more money!"
        $ caroline_cloth_shop_have_camera = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ caroline_morning_scenes_visit = 5
        jump cosplay_menu_label

    if camera1 in inventory.items and caroline_cloth_shop_have_camera == 3:
        if caroline_mc_room_evening_scene2 == True:
            scene caroline_cloth_shop_afternoon_scene1_p4a
            Caroline "[player_name]... We should talk privately in the evening, now is not a good moment for this."
            $ can_hide_windows = False
            jump cloth_shop_open_label
        scene caroline_cloth_shop_afternoon_scene1_p1
        Caroline "Oh! Hey, [player_name]! Ready for another photo session?"

        menu:
            "Sure!":

                jump cosplay_menu_label
            "Not now.":
                $ can_hide_windows = False
                jump cloth_shop_open_label
