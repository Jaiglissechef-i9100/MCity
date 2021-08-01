image CR2_AS4_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS4/1.jpg"
image CR2_AS4_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS4/2.jpg"
image CR2_AS4_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS4/3.jpg"
image CR2_AS4_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS4/4.jpg"

label CR2_AS4_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_AS4_p1 with dissolve
    $ can_hide_windows = True

    MC "Huh?"
    MC "(What’s this thing? A bottle of perfume maybe?)"

    scene CR2_AS4_p2

    MC "(It’s made of glass, and there’s a thick black liquid inside.)"
    MC "(Could it be… nail polish?)"
    MC "(Caroline never wears black nail polish…)"

    scene CR2_AS4_p3 at pandown3

    MC "(Oh no…)"
    MC "(That girl that Caroline brought to our house… What was her name? Violet?)"

    scene CR2_AS4_p4

    MC "Shit! Violet must have been here!"
    MC "(Could she be involved in the robbery?)"
    $ CR2_AS4 = False
    $ CR2_ES2_qViolet = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump cloth_shop_label

