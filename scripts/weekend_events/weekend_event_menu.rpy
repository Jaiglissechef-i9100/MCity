


label weekend_event_menu_label:
    $ can_hide_windows = False
    if renpy.loadable("patch.rpy"):
        $ Mom_name = "Mom"
    else:
        $ Mom_name = "Linda"
    menu:
        "{color=#00ff00}Go meet with Celia.{/color}" if CeR2_LS == 4:
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump CeR2_LS_lab
        "{color=#00ff00}Go with Sara to the swimming pool.{/color}" if SR2_weekend_swimming_pool == True and week_day == 5 and SR3_weekend_event == False and SR2_grounded == False and SR3_grounded == False:
            $ SR2_after_waterslide = False
            $ SR2_after_swimming = False
            $ SR2_after_sunbed = False
            $ SR2_after_lemonade = False
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump SR2_weekend_swimming_pool_label

        "Locked: (Sara weekend event.) (disabled)" if SR2_weekend_swimming_pool == False and week_day == 5:
            jump day_time_changer
        "{color=#00ff00}Start Sara's weekend event.{/color}" if SR3_weekend_event == True and week_day == 5:
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump SR3_we_label

        "Locked: ([Mom_name] weekend event.) (disabled)" if MLR2_weekend_event == False and week_day == 5 and ml_points < 3:
            jump day_time_changer
        "{color=#f00}{alpha=0.4} [Mom_name] weekend event.(Required: Red Wine){/alpha}{/color} (disabled)" if MLR2_weekend_event == True and not red_wine in inventory.items and week_day == 5 and ml_points < 3:
            jump day_time_changer

        "{color=#00ff00}[Mom_name] weekend event.{/color}" if MLR2_weekend_event == True and red_wine in inventory.items and week_day == 5 and ml_points < 3:
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump MLR2_weekend_label

        "Locked: (Caroline weekend event.) (disabled)" if CR3_weekend_event == False:
            jump day_time_changer
        "{color=#f00}{alpha=0.4} Meet up with Caroline. (Required: 200$){/alpha}{/color} (disabled)" if CR3_weekend_event == True and inventory.money < 200:
            jump day_time_changer

        "{color=#00ff00} Meet up with Caroline. {/color} " if CR3_weekend_event == True and inventory.money >= 200:
            $ inventory.money -= 200
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")

            jump CR3_WE_label

        "{color=#00ff00} (Caroline weekend event.) {/color} " if CR4_week_event == True:

            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")

            jump CR4_WE_label
        "Back.":
            jump day_time_changer