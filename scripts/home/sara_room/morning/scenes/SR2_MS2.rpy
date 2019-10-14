image SR2_MS2_p1 = "images/home/sara_room/morning/SR2_MS2/1.jpg"
image SR2_MS2_p2 = "images/home/sara_room/morning/SR2_MS2/2.jpg"
image SR2_MS2_p3 = "images/home/sara_room/morning/SR2_MS2/3.jpg"
image SR2_MS2_p4 = "images/home/sara_room/morning/SR2_MS2/4.jpg"
image SR2_MS2_p5 = "images/home/sara_room/morning/SR2_MS2/5.jpg"
image SR2_MS2_p6 = "images/home/sara_room/morning/SR2_MS2/6.jpg"
image SR2_MS2_p7 = "images/home/sara_room/morning/SR2_MS2/7.jpg"
image SR2_MS2_p8 = "images/home/sara_room/morning/SR2_MS2/8.jpg"

label SR2_MS2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen sister_nerdy_morning_notclickable
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

    Mom "It’s no use lying to me, Sara. Your report came through the post today."
    Sara "Wh-What?!"
    if renpy.loadable("patch.rpy"):
        MC "(Huh? It sounds like Mom and Sara are having an argument. I should check it out and see what’s going on.)"
    else:
        MC "(Huh? It sounds like Linda and Sara are having an argument. I should check it out and see what’s going on.)"

    hide screen sister_nerdy_morning_notclickable
    $ can_hide_windows = True
    scene SR2_MS2_p1 with dissolve
    Mom "You’ve always been a straight A student. So, imagine my surprise when I open up your report card, to reveal a plethora of D’s, E’s and EVEN an F!"
    Mom "I mean, seriously - how on Earth did you get an F in History?!"
    if renpy.loadable("patch.rpy"):
        Sara "Mom, I-"
    else:
        Sara "Linda, I-"

    scene SR2_MS2_p2

    Mom "This is completely unacceptable. Do you know what happens to students who fail in school? They don’t get to go to good colleges."
    Mom "You want to go to a good college, don’t you?"
    if renpy.loadable("patch.rpy"):
        Sara "Y-Yes, Mom."
    else:
        Sara "Y-Yes, Linda."

    scene SR2_MS2_p3

    Mom "Perhaps you can offer me some kind of explanation then, for these utterly atrocious results."
    Sara "I… don’t know…"
    Mom "How often have you been studying, for the past few months?"
    Sara "Same as alway-"
    Mom "Don’t lie to me, Sara!"

    scene SR2_MS2_p4

    Mom "I know what this is - you’ve been spending all your time playing that STUPID online game."
    Mom "Well, no more! As of moment, you this are GROUNDED."
    Sara "Wh-What?!"
    if renpy.loadable("patch.rpy"):
        Mom "No computer games, no going out with friends, and no hanging out with your brother."
    else:
        Mom "No computer games, no going out with friends, and no hanging out with [player_name]."

    scene SR2_MS2_p5

    Sara "(Sniff!)"
    Mom "It’s no use crying, young lady. If you can’t be trusted to take care of your own education, then I’ll have to revoke your privileges."
    Mom "You are to remain in your bedroom and study. I’ll call you when it’s time for dinner. But after that, you will return to your room and study some more."
    Sara "This isn’t fair! (Sob!)"

    scene SR2_MS2_p6

    Mom "I don’t care if it takes you a week or ten weeks. You will be revising and resitting every single exam until you get, AT LEAST a B, in every single one."
    Mom "Is that clear?"
    Sara "…"
    Mom "I said, is that clear?!"
    if renpy.loadable("patch.rpy"):
        Sara "(Sniff) Y-Yes, Mom."
    else:
        Sara "(Sniff) Y-Yes, Linda."

    scene SR2_MS2_p7

    Mom "Oh, [player_name]! I didn’t see you standing there."
    MC "Is everything okay with Sara?"
    Mom "She’ll be fine. She just chose to play video games, rather than study. She’s going to learn, a very valuable lesson, over the coming days."
    MC "Maybe I could help her study?"

    scene SR2_MS2_p8

    Mom "Sorry, Sweetie. I know she really likes hanging out with you, but I can’t have her being distracted."
    Mom "Until she gets, every subject back with at LEAST a B, then she will be grounded to her room."
    MC "Can I go and talk with her, at least?"
    Mom "No, give her some space. You two can always chat at school."
    if renpy.loadable("patch.rpy"):
        MC "(Gee… Mom’s being REALLY harsh on Sara, right now.)"
    else:
        MC "(Gee… Linda’s being REALLY harsh on Sara, right now.)"
    MC "(Then again, Sara probably should have actually studied for her tests. She did bring most of this on, herself.)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_MS2 = False
    $ SR2_grounded = True
    $ SR2_AS1 = False
    $ SR2_AS2 = True
    $ day_time = 1
    jump corridor_morning1



label SR2_grounded_label:
    $ clickable = False

    if day_time == 1:
        show screen corridor_morning

    if day_time == 2:
        show screen corridor_day
    if day_time == 3:
        show screen corridor_evening

    if renpy.loadable("patch.rpy"):
        MC "I can't go in. Mom asked me to not do it."
    else:
        MC "I can't go in. Linda asked me to not do it."
    $ clickable = True
    jump corridor_morning1