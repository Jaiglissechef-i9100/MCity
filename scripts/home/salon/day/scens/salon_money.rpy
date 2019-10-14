


label salon_money_label:
    if day_time == 1:
        show screen salon_morning_notclickable
    if day_time == 2:
        show screen salon_day_notclickable
    if day_time == 3:
        show screen salon_evening_notclickable
    if day_time == 4:
        show screen salon_night_notclickable
    $ money = renpy.random.choice( [10, 11, 12, 13, 14, 15,16,17,19,18,20])
    $ inventory.earn(money)
    MC "Nice! +[money]$"
    $ slon_money = False
    jump salon_morning1