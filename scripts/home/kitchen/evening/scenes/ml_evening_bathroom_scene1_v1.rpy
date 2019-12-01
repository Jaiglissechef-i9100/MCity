image ml_evening_bathroom_scene_v1_p1 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene_v1/1.jpg"
image ml_evening_bathroom_scene_v1_p2 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene_v1/2.jpg"

image ml_evening_bathroom_scene2_v1_p1 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene2_v1/1.jpg"
image ml_evening_bathroom_scene2_v1_p2 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene2_v1/2.jpg"

screen ml_evening_bathroom_scene_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_evening_bathroom_scene_v1_screen"),Jump("kitchen_evening1")]

label ml_evening_bathroom_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_evening_bathroom_scene_v1 == False:
        show screen kitchen_evening
        show screen ml_evening_bathroom_scene_v1_screen
        MC "I already know who's there."
        $ can_hide_windows = False
        jump kitchen_evening1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    if ml_evening_bathroom_vist_scene_v1 == 1 and ml_can_evening_bathroom_scene_v1 == True:
        scene ml_evening_bathroom_scene_v1_p1 with dissolve
        $ can_hide_windows = True
        if persistent.incest_patch == True:
            MC "(Just in time! It looks like Mom’s about to take a bath!)"
        else:
            MC "(Just in time! It looks like Linda’s about to take a bath!)"
        MC "(Damn… She’s got the best pair of thighs I’ve ever seen on a woman.)"
        MC "(No girl in my school even comes close to that!)"

        scene ml_evening_bathroom_scene_v1_p2
        if persistent.incest_patch == True:
            MC "(I can’t help but feel this is wrong… She’s my mother and I shouldn’t be thinking these things about her.)"
        else:
            MC "(I can’t help but feel this is wrong… She’s my friend and I shouldn’t be thinking these things about her.)"
        MC "(On the other hand, just look at that ass. It’s fucking perfect!)"
        MC "(I can almost see her vulva, with that tight g-string she’s wearing!)"
        $ ml_can_evening_bathroom_scene_v1 = False
        $ ml_evening_bathroom_vist_scene_v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_evening1
    if ml_evening_bathroom_vist_scene_v1 == 2 and ml_can_evening_bathroom_scene_v1 == True:
        scene black
        $ can_hide_windows = True
        if persistent.incest_patch == True:
            MC "(I’m a little late tonight - I hope I haven’t missed Mom getting washed!)"
        else:
            MC "(I’m a little late tonight - I hope I haven’t missed Linda getting washed!)"

        scene ml_evening_bathroom_scene2_v1_p1 with dissolve
        MC "(Phew! Just in time!)"
        MC "(And she’s naked too! Awesome!)"
        MC "(I wonder how often she works out, to get a body THAT fit.)"

        scene ml_evening_bathroom_scene2_v1_p2
        if persistent.incest_patch == True:
            MC "(I’d give my right arm, for the girls at my school to have tits like Mom does! Those puppies are amazing!)"
        else:
            MC "(I’d give my right arm, for the girls at my school to have tits like Linda does! Those puppies are amazing!)"
        MC "(I’d be so distracted in class that I’d never learn anything though. Haha!)"
        MC "(Right, I better head on out of here before I get caught…)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_evening_bathroom_scene_v1 = False
        $ ml_evening_bathroom_scene_v1 = False
        $ can_hide_windows = False
        jump kitchen_evening1

label ml_evening_bathroom_locked_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if ml_can_evening_bathroom_scene_v1 == False:
        show screen kitchen_evening
        show screen ml_evening_bathroom_scene_v1_screen
        MC "I already know who's there."
        $ can_hide_windows = False
        jump kitchen_evening1
    else:
        $ renpy.sound.play("sfx/door_locked.mp3")
        show screen kitchen_evening_notclickable
        MC "It’s locked! I wonder who is there…?"
        MC "If I only had some spy camera I could use it to see through the door!"
        hide screen kitchen_evening_notclickable
        $ can_hide_windows = False
        jump kitchen_evening1
