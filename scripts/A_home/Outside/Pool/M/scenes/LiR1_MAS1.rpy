image LiR1_MAS1_p1 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/1.jpg"
image LiR1_MAS1_p2 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/2.jpg"
image LiR1_MAS1_p3 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/3.jpg"
image LiR1_MAS1_p4 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/4.jpg"
image LiR1_MAS1_p5 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/5.jpg"
image LiR1_MAS1_p6 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/6.jpg"
image LiR1_MAS1_p7 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/7.jpg"
image LiR1_MAS1_p8 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/8.jpg"
image LiR1_MAS1_p9 = "images/a_home/Outside/Pool/M/Scenes/LiR1_MAS1/9.jpg"

label LiR1_MAS1_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene LiR1_MAS1_p1 with dissolve
    $ Yazmin_name = "???"

    Yazmin "Why, hello there. If it isn’t - [player_name]. It must have been three or four years, since I last saw you."
    if renpy.loadable("patch.rpy"):
        MC "Yeah, I think it was - the family barbeque on the beach."
    else:
        MC "Yeah, I think it was that barbeque on the beach."
    Yazmin "Oh, my God - yes! That was it. Geez, that was... four years ago? You don’t look - a day older - than when I last saw you."

    scene LiR1_MAS1_p2

    MC "Thanks, Yazmin. You’re looking great too."
    MC "(She was wearing a similar bikini - all those years ago - on the beach too. I remember staring at her from the dunes, while the sun set into the Pacific Ocean.)"
    if renpy.loadable("patch.rpy"):
        MC "(Mom had gone for a walk with Caroline, while Dad slept on the - warm golden sand. I think Auntie and Sara were beginning to pack away some beach towels.)"
    else:
        MC "(Linda had gone for a walk with Caroline, while Bob slept on the - warm golden sand. I think Liza and Sara were beginning to pack away some beach towels.)"
    MC "(Yazmin was lying at the water’s edge, so the waves would lap at her feet - every few seconds.)"
    scene LiR1_MAS1_p3
    $ Yazmin_name = "Yazmin"
    Yazmin "So, what brings you over today?"
    if renpy.loadable("patch.rpy"):
        MC "I’m actually here to help clean the pool. My aunt mentioned - it was in need of a thorough scrubbing."
    else:
        MC "I’m actually here to help clean the pool. Liza mentioned - it was in need of a thorough scrubbing."
    MC "(I love the way the sunlight falls on her hair. I hope she doesn’t notice my eyes - wandering - over her body.)"

    scene LiR1_MAS1_p4

    Yazmin "Ugh! Don’t get me started on that fucking pool. It’s a curse!"
    Yazmin "You spend two hours - raking the shit out - with a net, and the next day, it’s filled up with, drowned bugs, trash, and dead leaves."
    Yazmin "Well, that’s all your problem now. I swear, I think I’d go crazy if I had to clean that - God-awful thing - one more time! "

    scene LiR1_MAS1_p5

    MC "Well, put that out of your head. I’m gonna be cleaning it, from now on. I really need the money! Haha!"
    Yazmin "I know exactly how it is - trust me. The things I used to do for money, when I was your age..."
    MC "What did you work as?"
    Yazmin "Err... Forget I said that."

    scene LiR1_MAS1_p6

    if renpy.loadable("patch.rpy"):
        Yazmin "Your aunt is indoors - it was - too hot outside - for her, today."
    else:
        Yazmin "Liza is indoors... It was - too hot outside - for her, today."
    Yazmin "(Damn, this little guy would look so hot, cleaning our pool. No shirt, no pants - just a tight pair of y-fronts. God... Thinking about this, makes me so wet!)"
    MC "Yeah, she’s never been the sunbathing type. How do I get inside?"

    scene LiR1_MAS1_p7

    Yazmin "Oh! I forgot - you probably haven’t visited this place before."
    MC "Yeah, it’s my first time here."
    Yazmin "That’s okay - the back door is just over there, at the top of those steps."

    scene LiR1_MAS1_p8

    Yazmin "Are you okay, going around the front entrance? I’ll need some privacy to - get changed - out of my swimsuit."
    MC "Sure. No problem."
    Yazmin "(I wonder how large his package is - down there... Now that [player_name] will be cleaning our pool, we might have him over more regularly. Perhaps I’ll get a chance to see his cock?)"

    scene LiR1_MAS1_p9
    if renpy.loadable("patch.rpy"):
        Yazmin "Just pop around the front. I’ll grab your auntie and open the door, after putting something - more appropriate - on."
    else:
        Yazmin "Just pop around the front. I’ll grab Liza and open the door, after putting something - more appropriate - on."
    MC "Cool. I’ll see you in a few minutes!"

    $ LiR1_MAS1 = False
    $ LiR1_MAS1a = True
    $ Li_door_locked = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump a_pool_M1
