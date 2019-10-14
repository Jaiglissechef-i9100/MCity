image cloth_shop_stealing_key_p1 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/1.jpg"
image cloth_shop_stealing_key_p2 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/2.jpg"
image cloth_shop_stealing_key_p3 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/3.jpg"
image cloth_shop_stealing_key_p4 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/4.jpg"

label cloth_shop_stealing_key_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene cloth_shop_stealing_key_p1 with dissolve
    MC "Hmm.. Let’s check.."
    MC "Great! The window is still unlocked, but I should be quiet anyway."
    scene cloth_shop_stealing_key_p2
    MC "Okay... I'm in. Where could she hide her spare key..?"
    MC "I should probably check the drawers."
    scene cloth_shop_stealing_key_p3
    MC "Please.. Be here.."
    scene cloth_shop_stealing_key_p4
    MC "Bingo! Nice - with this I could get into her bedroom at night.."
    MC "Just in case, of course!"
    $ cloth_shop_window_unlock = 3
    $ inventory.add(caroline_spare_key)
    $ can_hide_windows = False
    jump map_label