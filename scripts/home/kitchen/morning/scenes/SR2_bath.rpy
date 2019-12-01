image SR2_bath_p1 = "images/home/kitchen/morning/scenes/SR2_bath/1.jpg"
image SR2_bath_p2 = "images/home/kitchen/morning/scenes/SR2_bath/2.jpg"
image SR2_bath_p3 = "images/home/kitchen/morning/scenes/SR2_bath/3.jpg"

label SR2_bath_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if can_SR2_bath == False:
        show screen kitchen_morning_notclickable
        MC "I already know who's there."
        jump kitchen_morning1

    if camera in inventory.items:

        if camera.selected == True:
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
            $ can_hide_windows = True
            scene SR2_bath_p1 with dissolve
            MC "Huh? What is she doing?"
            MC "She was supposed to take a shower."
            scene SR2_bath_p2
            MC "Is she sleepy again? Those games are gonna kill her one day."
            scene SR2_bath_p3
            MC "Seriously!? Is she planning on taking a nap in the bathroom?"
            MC "..."
            if persistent.incest_patch == True:
                MC "I hope Mom doesn't notice her."
            else:
                MC "I hope Linda doesn't notice her."
            $ can_SR2_bath = False
            jump kitchen_morning1

        if not camera.selected:
            show screen kitchen_morning_notclickable
            MC "It’s locked! I wonder who is there…?"
            MC "If I only had some spy camera I could use it to see through the door!"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump kitchen_morning1

    if not camera.selected:
        show screen kitchen_morning_notclickable
        MC "It’s locked! I wonder who is there…?"
        MC "If I only had some spy camera I could use it to see through the door!"
        jump kitchen_morning1
