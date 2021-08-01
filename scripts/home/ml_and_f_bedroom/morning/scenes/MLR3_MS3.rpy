image MLR3_MS3_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/1.jpg"
image MLR3_MS3_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/2.jpg"
image MLR3_MS3_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/3.jpg"
image MLR3_MS3_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/4.jpg"
image MLR3_MS3_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/5.jpg"
image MLR3_MS3_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/6.jpg"
image MLR3_MS3_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR3_MS3/7.jpg"


label MLR3_MS3:
    hide screen displayTextScreen
    hide screen map_button
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR3_MS3_p1 with dissolve

    MC "(That’s [Mom_name]’s suitcase. The last time I saw that bag was when she went to a conference in Toronto.)"
    MC "(I wonder if she’s going on another business trip.)"
    MC "Hey, [Mom_name] - are you going somewhere with work?"

    scene MLR3_MS3_p2

    Mom "Heh, thankfully not! I’ve had enough of that damned place for a while. Besides, those conferences are basically excuses to have an expenses-paid holiday."
    MC "What’s in the bag, then?"
    Mom "Clothes, shower gel, towels. Just the essentials."

    scene MLR3_MS3_p3

    MC "Are you going on holiday?"
    Mom "… Yeah, I guess you could say that."
    MC "(Wait a minute… [Mom_name] and [Dad_name] have been arguing a lot, lately. Could it be that [Mom_name] is moving out?!)"
    MC "Where are you headed?"

    scene MLR3_MS3_p4

    Mom "That’s a secret right now - but don’t you worry: when the time comes you’ll know what’s happening."
    MC "(Fuck… I think she’s leaving. This is gonna destroy [Dad_name] when he finds out. He’s still madly in love with her.)"
    Mom "Aww, don’t look so worried. This will be a good surprise, I promise!"

    scene MLR3_MS3_p5

    MC "How much stuff have you got in there?"
    Mom "Mostly just the essentials for a couple of days."
    MC "When are you leaving?"

    scene MLR3_MS3_p6

    Mom "You ask A LOT of questions, don’t you?"
    Mom "You’ll find out when the time comes. Right now, all you need to know is that I’m packing a bag for myself."
    MC "(Should I tell [Dad_name] about this? Is she going to talk to him before she goes? Or will she just disappear one day?)"

    scene MLR3_MS3_p7
    if renpy.loadable("patch.rpy"):
        Mom "Oh, and before you think of asking your sisters or father about this… don’t."
    else:
        Mom "Oh, and before you think of asking your roommates or Bob about this… don’t."

    Mom "This is a secret between you and me. Got it? You weren’t even supposed to see me packing."
    MC "But I-"
    Mom "I’m serious, [player_name]: not a word to Sara or Caroline. Nobody, okay? Promise me."
    MC "Fine, I promise. I won’t tell anyone."
    Mom "Good… You won’t have to keep this secret for long, I promise."
    MC "(She clearly doesn't want to talk about it at home. Maybe tomorrow I should visit her at her workplace?)"


    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ MLR3_MS3 = False
    $ MLR3_AS2_event_can = True
    jump parents_bedroom_morning1