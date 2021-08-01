image SR2_weekend_swimming_pool_p1 = "images/Weekend_Events/Sara/R2/1.jpg"
image SR2_weekend_swimming_pool_p2 = "images/Weekend_Events/Sara/R2/2.jpg"
image SR2_weekend_swimming_pool_p3 = "images/Weekend_Events/Sara/R2/3.jpg"
image SR2_weekend_swimming_pool_p4 = "images/Weekend_Events/Sara/R2/4.jpg"

image SR2_weekend_swimming_pool_background = "images/Weekend_Events/Sara/R2/Map/1.jpg"

default SR2_after_swimming = False
default SR2_after_lemonade = False
default SR2_after_sunbed = False
default SR2_after_waterslide = False
default music_continue = True

label SR2_weekend_swimming_pool_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ week_day = 6
    $ day_time = 2
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3,hard = True)
    $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_weekend_swimming_pool_p1 with dissolve
    $ can_hide_windows = True
    MC "(Alright, that’s me changed and ready to swim.)"
    MC "(Now… where the heck is Sara?)"
    MC "(It’s not even that busy today.)"

    scene SR2_weekend_swimming_pool_p2

    Sara "Hi, [player_name]!"
    MC "Ah!"
    Sara "Sorry! Did I scare you, there?"
    MC "Just a bit!"
    Sara "Hehe!"

    scene SR2_weekend_swimming_pool_p3

    Sara "MWAH!"
    MC "(Wow! I’ve never seen Sara this giddy before. She must be really happy to go on this date with me.)"
    Sara "I’m so happy you’re here!"
    MC "Me too, Sara. Were you waiting long?"

    scene SR2_weekend_swimming_pool_p4

    Sara "Just a few minutes."
    Sara "What do you want to do together?"
    MC "Want to dip in the pool?"
    Sara "Umm… I can’t swim."
    MC "Oh yeah, I totally forgot. Sorry."
    $ can_hide_windows = False
    jump swimming_poll_label

label swimming_poll_label:
    hide screen displayTextScreen
    scene SR2_weekend_swimming_pool_background
    if music_continue == True:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
        $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    $ music_continue = True
    call screen swimming_poll_scr

screen swimming_poll_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1097
        ypos 478
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b1.png"
        hover "images/Weekend_Events/Sara/R2/Map/b1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Swim with Sara In The Pool"))
            action [Hide("displayTextScreen"),Jump("SR2_swimming_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 725
        ypos 278
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b2.png"
        hover "images/Weekend_Events/Sara/R2/Map/b2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Drink Lemonade"))
            action [Hide("displayTextScreen"),Jump("SR2_Lemonade_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1511
        ypos 463
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b3.png"
        hover "images/Weekend_Events/Sara/R2/Map/b3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Lounge Chairs"))
            action [Hide("displayTextScreen"),Jump("SR2_SunBed_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 15
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b4.png"
        hover "images/Weekend_Events/Sara/R2/Map/b4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = __("Water Slide"))
            action [Hide("displayTextScreen"),Jump("SR2_waterslide_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1352
        ypos 297
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b5.png"
        hover "images/Weekend_Events/Sara/R2/Map/b5_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Jacuzzi")
            action [Hide("displayTextScreen"),Jump("SR2_jacuzzi_label")]
            unhovered Hide("displayTextScreen")

