
default persistent.mod_skip_splashscreen = False
default mod_is_modal = True
default persistent.mod_winter_bgs = True
default persistent.mod_unlock_secret_gallery = False
default persistent.mod_unlock_scene_gallery = False
default persistent.mod_minigame_cheat = False

init 969:
    python:
        import datetime
        if (datetime.date.today().month == 11 and datetime.date.today().day >= 29) or datetime.date.today().month == 12:
            mod_is_winter = True
        else:
            mod_is_winter = False

    if persistent.mod_winter_bgs and mod_is_winter:
        image corridor_morning = "mod/images/winter_bgs/Coridor_Morning_Evening.jpg"
        image caroline_room_morning = "mod/images/winter_bgs/caroline_room_morning.jpg"
        image salon_morning = "mod/images/winter_bgs/Salon_morning_evening.jpg"
        image kitchen_morning = "mod/images/winter_bgs/kitchen_morning.jpg"
        image mc_room_morning = "mod/images/winter_bgs/mc_room_morning.jpg"

        image corridor_day = "mod/images/winter_bgs/Coridor_Morning_Evening.jpg"
        image caroline_room_day = "mod/images/winter_bgs/caroline_room_morning.jpg"
        image salon_day = "mod/images/winter_bgs/Salon_morning_evening.jpg"
        image kitchen_day = "mod/images/winter_bgs/kitchen_evening.jpg"
        image mc_room_day = "mod/images/winter_bgs/mc_room_morning.jpg"

        image corridor_evening = "mod/images/winter_bgs/Coridor_Morning_Evening.jpg"
        image caroline_room_evening = "mod/images/winter_bgs/caroline_room_evening.jpg"
        image salon_evening = "mod/images/winter_bgs/Salon_morning_evening.jpg"
        image kitchen_evening = "mod/images/winter_bgs/kitchen_evening.jpg"
        image mc_room_evening = "mod/images/winter_bgs/mc_room_evening.jpg"

        image entrace1_night = "mod/images/winter_bgs/Entrance_night.jpg"
        image entrance2_night = "mod/images/winter_bgs/Entrance2_night.jpg"
        image corridor_night = "mod/images/winter_bgs/Coridor_night.jpg"
        image caroline_room_night = "mod/images/winter_bgs/caroline_room_night.jpg"
        image salon_night = "mod/images/winter_bgs/Salon_night.jpg"
        image kitchen_might = "mod/images/winter_bgs/kitchen_night.jpg"
        image kitchen_night = "mod/images/winter_bgs/kitchen_night.jpg"
        image mc_room_night = "mod/images/winter_bgs/mc_room_night.jpg"

init 969 python:
    config.label_overrides["splashscreen"] = "splashscreen_m"

label splashscreen_m:
    if not persistent.mod_skip_splashscreen:
        scene black
        $ renpy.pause(1, hard = True)
        show splash1 with dissolve
        $ renpy.pause(2, hard = True)
        hide splash1 with dissolve
        show splash2 with dissolve
        $ renpy.pause(2, hard = True)
        hide splash2 with dissolve
        show splash3 with dissolve
        $ renpy.pause(2, hard = True)
        hide splash3 with dissolve
    $ persistent.isAndroid = False
    if not renpy.variant("pc"):
        $ persistent.isAndroid = True
    return

    screen scenes_gallery:
        key "hide_windows" action NullAction()
        modal True
        zorder 106
        add "images/secret_gallery/Bonus/Black.jpg"
        $ start2 = gallery_page2 * maxperpage2
        $ end2 = min(start2 + maxperpage2 - 1, len(scenes_gallery_items) - 1)
        grid maxnumx2 maxnumy2:
            xfill True
            yfill True
            for i in range(start2, end2 + 1):
                $ scenes_gallery_items[i].refresh_lock2()
                if scenes_gallery_items[i].is_locked2 and not persistent.mod_unlock_scene_gallery:
                    add scenes_gallery_items[i].locked2:
                        xalign 0.5
                        yalign 0.5
                else:
                    $ scenes_repeat = scenes_gallery_items[i].name
                    imagebutton idle scenes_gallery_items[i].thumb hover scenes_gallery_items[i].thumb_hover:
                        action [Jump(scenes_repeat)]
                        xalign 0.5
                        yalign 0.5
            for i in range(end2 - start2 + 1, maxperpage2):
                null
        grid maxnumx2 maxnumy2:
            xfill True
            yfill True
            for i in range(start2, end2 + 1):
                hbox:
                    spacing maxthumbx2 - 70
                    xalign 0.5
                    yalign 0.9
                    $ total2 = scenes_gallery_items[i].num_images2()
                    $ partial2 = scenes_gallery_items[i].num_unlocked2
            for i in range(end2 - start2 + 1, maxperpage2):
                null
        if gallery_page2 > 0:
            textbutton "Previous":
                action SetVariable("gallery_page2", gallery_page2 - 1)
                xalign 0.1
                yalign 0.99999
        if (gallery_page2 + 1) * maxperpage2 < len(scenes_gallery_items):
            textbutton "Next":
                action SetVariable("gallery_page2", gallery_page2 + 1)
                xalign 0.9
                yalign 0.99999
        textbutton "Return":
            action [Hide("scenes_gallery"), Jump("pc_icon_label")]
            xalign 0.5
            yalign 0.99999
        text "{size=+6}Scenes Gallery{/size}":
            xalign 0.5
            yalign 0.0

    screen secret_gallery:
        key "hide_windows" action NullAction()
        modal True
        zorder 106
        add "images/secret_gallery/Bonus/Black.jpg"
        $ start = gallery_page * maxperpage
        $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
        grid maxnumx maxnumy:
            xfill True
            yfill True

            for i in range(start, end + 1):
                $ gallery_items[i].refresh_lock()
                if gallery_items[i].is_locked and not persistent.mod_unlock_secret_gallery:
                    add gallery_items[i].locked:
                        xalign 0.5
                        yalign 0.5
                else:
                    imagebutton idle gallery_items[i].thumb hover gallery_items[i].thumb_hover:
                        action Show("gallery_closeup", dissolve, gallery_items[i].images)
                        xalign 0.5
                        yalign 0.5
            for i in range(end - start + 1, maxperpage):
                null
        grid maxnumx maxnumy:
            xfill True
            yfill True
            for i in range(start, end + 1):
                hbox:
                    spacing maxthumbx - 70
                    xalign 0.5
                    yalign 0.9
                    $ total = gallery_items[i].num_images()
                    $ partial = gallery_items[i].num_unlocked
            for i in range(end - start + 1, maxperpage):
                null
        if gallery_page > 0:
            textbutton "Previous":
                action SetVariable("gallery_page", gallery_page - 1)
                xalign 0.1
                yalign 0.99999
        if (gallery_page + 1) * maxperpage < len(gallery_items):
            textbutton "Next":
                action SetVariable("gallery_page", gallery_page + 1)
                xalign 0.9
                yalign 0.99999
        textbutton "Return":
            action [Hide("secret_gallery")]
            xalign 0.5
            yalign 0.99999
        text "{size=+6}Secret Gallery{/size}":
            xalign 0.5
            yalign 0.0
