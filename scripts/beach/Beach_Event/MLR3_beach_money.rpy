image MLR3_beach_money_p1 = "images/Beach/MLR3_beach_event/Bag1.jpg"
image MLR3_beach_money_p2 = "images/Beach/MLR3_beach_event/Bag2.jpg"

label MLR3_beach_money:
    $ clickable = False
    hide screen map_button
    scene beach1_map
    scene MLR3_beach_money_p1
    MC "Hmm... Let's see if there's something interesting in the bag."
    scene MLR3_beach_money_p2
    MC "Ah! Nice. There's some cash. {color=#00ff00}(+38$){/color}"
    $ inventory.earn(38)
    $ clickable = True
    hide screen beach_M_scr
    $ can_hide_windows = False
    $ beach_money = False
    jump beach_M1