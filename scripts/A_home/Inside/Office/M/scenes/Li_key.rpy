image Li_key_p1 = "/images/a_home/Inside/Office/M/2.jpg"
default LiR1_key = False
default can_LiR1_key = False
label Li_key_label:
    if Li_points >1 and Y_points > 1:
        hide screen map_button
        scene Li_key_p1 with dissolve
        MC "Oh.. Nice! This should be the key to the front door. Let's try it at night."

        $ inventory.add(Li_key1)

        jump a_office_M1
    if LiR1_MAS3 == False:
        hide screen map_button
        scene Li_key_p1 with dissolve
        MC "Oh.. Nice! This should be the key to the front door. Let's try it at night."

        $ inventory.add(Li_key1)

        jump a_office_M1
    else:
        if day_time == 1:
            show screen a_office_M_scr
        if day_time == 2:
            show screen a_office_D_scr
        $ clickable = False
        MC "I can't take that key, when someone is here."
        $ clickable = True
        jump a_office_M1

