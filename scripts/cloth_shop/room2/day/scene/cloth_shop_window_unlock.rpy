label cloth_shop_window_unlock_label:
    hide screen map_button
    $ clickable = False
    if CR2_before_robber == False:
        show screen cloth_shop_room2_robbery_screen
    else:
        show screen cloth_shop_room2_screen_notclickable
    "Do you want to unlock the window?"
    window hide
    menu:
        "Yes.":

            $ renpy.sound.play("sfx/window_unlock.mp3")
            $ cloth_shop_window_unlock = True
            $ clickable = True
            jump cloth_shop_room2_label
        "No.":

            $ clickable = True
            jump cloth_shop_room2_label

