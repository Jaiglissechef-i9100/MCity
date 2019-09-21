image ml_kitchen_morning_scene4_v1_p1 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/1.jpg"
image ml_kitchen_morning_scene4_v1_p2 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/2.jpg"
image ml_kitchen_morning_scene4_v1_p3 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/3.jpg"
image ml_kitchen_morning_scene4_v1_p4 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/4.jpg"
image ml_kitchen_morning_scene4_v1_p5 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/5.jpg"
image ml_kitchen_morning_scene4_v1_p6 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/6.jpg"

screen ml_kitchen_morning_scene4_V1__screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_kitchen_morning_scene4_V1__screen"),Jump("kitchen_morning1")]


label ml_kitchen_morning_scene4_V1_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_bedroom_morning_scene5 == False:
        show screen kitchen_morning
        show screen ml_kitchen_morning_scene4_V1__screen
        show screen kitchen_morning_notclickable
        MC "I've already talked with them."
        jump kitchen_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_kitchen_morning_scene4_v1_p1 at pandown1
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        $ Linda_name = __("Mom")
        $ Liza2_name = __("Auntie")
    else:
        $ Mom_name = "Linda"
        $ Liza2_name = "Liza"
    $ renpy.pause(2)
    if renpy.loadable("patch.rpy"):
        MC "(Huh, looks like Auntie is visiting today!)"
        MC "(She’s a fairly close, member of the family. We see her probably every other week, at the very least.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Huh, looks like Linda's friend is visiting today!)"
        MC "(She’s a fairly close, member of this house. We see her probably every other week, at the very least.)"

    scene ml_kitchen_morning_scene4_v1_p2
    if renpy.loadable("patch.rpy"):
        MC "(Which is strange, because Mom and Auntie have such different personalities!)"
        MC "(While Mom is a hard worker and career-driven woman, Auntie is a walking, talking, Barbie doll.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Which is strange, because she and Linda have such different personalities!)"
        MC "(While Linda is a hard worker and career-driven woman, she is a walking, talking, Barbie doll.)"
    MC "(She spends most of her free time at day spas, shopping, and hanging out with her similarly air-headed friends.)"

    scene ml_kitchen_morning_scene4_v1_p3
    Mom "Ah! There you are!"
    Mom "I thought I was going to have to come to your bedroom and get you up."

    if renpy.loadable("patch.rpy"):
        MC "Hi, Mom! Hi, Auntie!"
        $ Liza2_name = __("Auntie")
    if not renpy.loadable("patch.rpy"):
        MC "Hi."
        $ Auntie_name = __("Linda's Friend")
    Auntie "Hi, [player_name]."
    Mom "C’mere and let me kiss you."

    scene ml_kitchen_morning_scene4_v1_p4
    Mom "Mwah!"
    Auntie "Anyway, I was saying to Margaret - if you want to go out in THAT dress, then we’re NOT sitting at the same table during lunch."
    Auntie "I mean, SERIOUSLY - who wears a beige dress?!"

    scene ml_kitchen_morning_scene4_v1_p2
    Mom "Oh yeah… That’s… really something else…"
    if renpy.loadable("patch.rpy"):
        Mom "(God, does [Auntie_name] not have ANY other interests than clothes and fashion?!)"
    if not renpy.loadable("patch.rpy"):
        Mom "(God, does she not have ANY other interests than clothes and fashion?!)"
    Mom "(I have to change the topic before she drives me crazy.)"
    Mom "So, [player_name] is looking for a part-time job. Did you know that?"
    Auntie "Really?"

    scene ml_kitchen_morning_scene4_v1_p5
    Auntie "I have a swimming pool that needs cleaning out regularly."
    Auntie "If you’re interested, I’m happy to pay you for it."
    Auntie "What do you say?"
    if renpy.loadable("patch.rpy"):
        MC "Sure! Thanks, Auntie!"
    if not renpy.loadable("patch.rpy"):
        MC "Sure! Thanks."

    scene ml_kitchen_morning_scene4_v1_p6
    Auntie "Great! We’ll organise a date for you to come around soon."
    if renpy.loadable("patch.rpy"):
        Mom "Thanks, Sis. I really appreciate that."
    if not renpy.loadable("patch.rpy"):
        Mom "Thanks. I really appreciate that."
    if renpy.loadable("patch.rpy"):
        Auntie "Aww, come on! It’s nothing. I’ve got money to burn - and I may as well spend it on my favourite nephew!"
    if not renpy.loadable("patch.rpy"):
        Auntie "Aww, come on! It’s nothing. I’ve got money to burn - and I may as well spend it on you!"
    if renpy.loadable("patch.rpy"):
        MC "Thanks, Auntie!"
    if not renpy.loadable("patch.rpy"):
        MC "Thanks!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_aunt_house_unlocked = True
    $ ml_kitchen_morning_scene = False
    $ ml_bedroom_morning_scene5 = True
    $ ml_can_bedroom_morning_scene5 = False
    $ ml_salon_morning_visit = 5
    $ au_bath_event_unlock = True
    $ can_hide_windows = False
    jump kitchen_morning1
