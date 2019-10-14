


label Ne_outside_M1:
    $ in_map = False
    $ can_map = True
    if Ne_ES1 == True:
        $ can_map = False

    if day_time == 3:
        jump Ne_outside_E1

    if day_time == 4:
        jump Ne_outside_N1