

label CR2_minigame_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene caroline_cloth_shop_afternoon_scene1_p1
    $ can_hide_windows = True
    Caroline "Hi again, [player_name]. Back to help me with some more cosplay photoshoots?"
    if CR2_CSfirstvisit == True:
        MC "Sure, Caroline! What have you got in stock this time?"

        scene caroline_cloth_shop_afternoon_scene1_p3

        Caroline "I’ve got for a real mixture of things again. Give me a shout whenever you’re ready."
        Caroline "I’ve got a strong feeling you’ll really like them."
        $ CR2_CSfirstvisit = False
    menu:
        "Sure! We can start.":
            $ can_hide_windows = False
            jump cosplay_menu_label
        "Not now.":
            $ can_hide_windows = False
            jump cloth_shop_open_label