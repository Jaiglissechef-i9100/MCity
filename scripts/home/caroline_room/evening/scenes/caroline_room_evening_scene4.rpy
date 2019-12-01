image caroline_room_evening_scene4_p1 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/1.jpg"
image caroline_room_evening_scene4_p2 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/2.jpg"
image caroline_room_evening_scene4_p3 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/3.jpg"
image caroline_room_evening_scene4_p4 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/4.jpg"
image caroline_room_evening_scene4_p5 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/5.jpg"
image caroline_room_evening_scene4_p6 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/6.jpg"
image caroline_room_evening_scene4_p7 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/7.jpg"
image caroline_room_evening_scene4_p8 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/8.jpg"

label caroline_room_evening_scene4_label:

    hide screen map_button
    if caroline_room_evening_scene4 == 3:
        show screen caroline_room_evening_not_clickable
        MC "I've already talked to her."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    scene caroline_room_evening_scene4_p1 with dissolve

    $ can_hide_windows = True
    Caroline "Haha! I can’t believe it!"
    MC "(She sure seems, happy for a change!)"
    MC "Hey, Caroline! What’s so funny?"

    scene caroline_room_evening_scene4_p2
    Caroline "Oh! Hiii! I didn’t see you come in, there."
    Caroline "Nothing’s funny - I’m just… You need to see this."
    Caroline "Here - take a seat beside me! Quick! This is amazing!"

    scene caroline_room_evening_scene4_p3
    MC "Okay... what am I looking at?"
    Caroline "These are my profit/loss accounts for the past year!"
    MC "What are all those red numbers?"
    Caroline "Those are months where I lost money - but look at the last one!"
    MC "Huh? It’s black there."
    Caroline "That means I turned a profit! And look! It’s almost enough to pay off, the past four months debts!"
    Caroline "Most of it, ended up, coming from online sales."

    scene caroline_room_evening_scene4_p4
    MC "Ahh, so what you’re really saying, is that you couldn’t have done it without ME?"
    Caroline "I never said that."
    MC "Who took all those pictures, for your website and store?"

    scene caroline_room_evening_scene4_p5
    Caroline "Haha! I’m grateful you took the pictures - but remember, that I spent MONTHS; setting up business accounts, organising shipping, finding a location to rent."
    Caroline "You certainly helped - but I still did the LION’S share of the work."
    MC "Fine! Fine! I get it! Haha!"
    MC "Say - you remember that thing that happened, during the last cosplay?"

    scene caroline_room_evening_scene4_p6
    MC "I’d really like to do that again."
    Caroline "Wh-What?"
    MC "You know - when you rubbed yourself against my cock?"
    MC "Don’t you want to do it again too?"

    scene caroline_room_evening_scene4_p7
    Caroline "[player_name]... That was just us having a bit of fun."
    Caroline "Were were just blowing off some steam."
    MC "But, I’m really attracted to you."
    if persistent.incest_patch == True:
        Caroline "I’m sorry… I don’t feel that way. You’re my brother. We had fun together, and did something we shouldn’t have. Let’s not talk about this again. Please..."
    else:
        Caroline "I’m sorry… I don’t feel that way. You’re my friend. We had fun together, and did something we shouldn’t have. Let’s not talk about this again. Please..."
    MC "I’m sorry… I just thought… maybe you enjoyed it too."
    Caroline "(Sigh) Give me some time alone, to think."
    MC "Okay… I’ll see you later, Caroline."

    scene caroline_room_evening_scene4_p8
    Caroline "(What have I done? Was he already attracted to me? Or have I caused it, by posing in those sexy outfits?)"
    Caroline "(I can’t believe what I’ve gotten myself into…)"
    $ caroline_room_evening_scene4 = 3
    $ caroline_mc_room_moenig_scene5 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
