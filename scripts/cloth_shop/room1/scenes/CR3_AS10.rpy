label CR3_AS10_label:
    if CR3_AS10_can == False:
        hide screen map_button
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "I've already talked with her."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    hide screen map_button
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer

    scene CR3_AS7_p1 with dissolve

    MC "Hey Caroline? Where’s Violet?"
    Caroline "Hi, [player_name]. She’s off today. I don’t need her in."
    MC "Why?"

    scene CR3_AS7_p2

    Caroline "Sales are through the roof right now! I don’t actually need to do any additional advertising. "
    Caroline "In fact, if I kept advertising it would be stupid - because I can’t even keep up with the level of current orders I’m getting through."
    MC "(Damn, that’s a shame. I was hoping to do some more photography sessions with her.)"

    scene CR3_AS7_p3

    MC "Do you think you’ll be doing any more cosplay sessions in the future?"
    Caroline "I honestly don’t know what the future will bring. Right now though, my business is stable and growing faster than I can control it."

    scene CR3_AS7_p4

    MC "I guess congratulations are in order, then!"
    Caroline "Hehe, thanks. I’m really proud of how things are turning out!"
    Caroline "Anyway, I’ve got two dozen more orders to pack and process before tonight’s post leaves. I’ll talk to you later."
    MC "No problem. Catch you later, Caroline!"

    $ CR3_AS10_can = False
    $ CR3_NS5 = True
    $ C_NS_locked = True
    $ CR3_AS5 = False
    $ can_violet_CR3 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump cloth_shop_open_label
