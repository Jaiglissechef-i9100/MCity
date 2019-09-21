image a_bathroom_bg_M = "/images/a_home/Inside/Bathroom/M/1.jpg"

label a_bathroom_M1:

    if LiR1_MAS8 == True and LiR1_MAS8_talked == False and day_time <=2:
        scene LiR1_MAS9_p1
        hide screen map_button
        MC "Eh!? Fuck! She's in there! I think it's not the best idea to talk to her, after what happened... Especially while she's nude..."

        jump a_living_M1

    if LiR1_MAS9 == True:
        jump LiR1_MAS9_label

    if day_time == 1:
        jump a_bathroom_M2

    if day_time == 2:
        jump a_bathroom_D1

    if day_time == 3:
        jump a_bathroom_E1

    if day_time == 4:
        jump a_bathroom_N1

label a_bathroom_M2:
    hide screen displayTextScreen
    scene a_bathroom_bg_M
    $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen a_bathroom_M_scr
