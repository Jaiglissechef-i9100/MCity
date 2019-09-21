label ml_bedroom_morning_money_label:
    if day_time == 1:
        show screen parents_bedroom_morning_notclickable
    if day_time == 2:
        show screen parents_bedroom_day_notclickable
    if day_time == 3:
        show screen parents_bedroom_evening_notclickable
    $ money = renpy.random.choice( [10, 11, 12, 13, 14, 15,16,17,19,18,20])
    $ inventory.earn(money)
    MC "Nice! +[money]$"
    $ moeny_parents_room  = False
    hide screen parents_bedroom_morning_notclickable
    jump parents_bedroom_morning1
