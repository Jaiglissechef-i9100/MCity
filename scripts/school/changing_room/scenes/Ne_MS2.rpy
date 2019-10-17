image Ne_MS2_p1 = "images/Ne_1/MS2/1.jpg"
image Ne_MS2_p2 = "images/Ne_1/MS2/2.jpg"
image Ne_MS2_p3 = "images/Ne_1/MS2/3.jpg"
image Ne_MS2_p4 = "images/Ne_1/MS2/4.jpg"
image Ne_MS2_p5 = "images/Ne_1/MS2/5.jpg"
image Ne_MS2_p6 = "images/Ne_1/MS2/6.jpg"
image Ne_MS2_p7 = "images/Ne_1/MS2/7.jpg"
image Ne_MS2_p8 = "images/Ne_1/MS2/8.jpg"
image Ne_MS2_p9 = "images/Ne_1/MS2/9.jpg"

image Ne_MS2a_p1 = "images/Ne_1/MS2/2/1.jpg"
image Ne_MS2a_p2 = "images/Ne_1/MS2/2/2.jpg"
image Ne_MS2a_p3 = "images/Ne_1/MS2/2/3.jpg"
image Ne_MS2a_p4 = "images/Ne_1/MS2/2/4.jpg"
image Ne_MS2a_p5 = "images/Ne_1/MS2/2/5.jpg"
image Ne_MS2a_p6 = "images/Ne_1/MS2/2/6.jpg"
image Ne_MS2a_p7 = "images/Ne_1/MS2/2/7.jpg"
image Ne_MS2a_p8 = "images/Ne_1/MS2/2/8.jpg"
image Ne_MS2a_p9 = "images/Ne_1/MS2/2/9.jpg"
image Ne_MS2a_p10 = "images/Ne_1/MS2/2/10.jpg"
image Ne_MS2a_p11 = "images/Ne_1/MS2/2/11.jpg"
image Ne_MS2a_p12 = "images/Ne_1/MS2/2/12.jpg"
image Ne_MS2a_p13 = "images/Ne_1/MS2/2/13.jpg"
image Ne_MS2a_p14 = "images/Ne_1/MS2/2/14.jpg"

image Ne_MS2aa_p1 = "images/Ne_1/MS2/Truth/1.jpg"
image Ne_MS2aa_p2 = "images/Ne_1/MS2/Truth/2.jpg"
image Ne_MS2aa_p3 = "images/Ne_1/MS2/Truth/3.jpg"
image Ne_MS2aa_p4 = "images/Ne_1/MS2/Truth/4.jpg"
image Ne_MS2aa_p5 = "images/Ne_1/MS2/Truth/5.jpg"
image Ne_MS2aa_p6 = "images/Ne_1/MS2/Truth/6.jpg"
image Ne_MS2aa_p7 = "images/Ne_1/MS2/Truth/7.jpg"
image Ne_MS2aa_p8 = "images/Ne_1/MS2/Truth/8.jpg"
image Ne_MS2aa_p9 = "images/Ne_1/MS2/Truth/9.jpg"
image Ne_MS2aa_p10 = "images/Ne_1/MS2/Truth/10.jpg"

default Ne_MS3 = False
label Ne_MS2_lab:
    hide screen map_button
    if Ne_MS2 == 3:
        $ clickable = False
        show screen changing_room_morning
        MC "I've already talked to her."
        hide screen changing_room_morning
        $ clickable = True
        jump changing_room_morning1

    if Ne_MS2 == 2:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        scene Ne_MS2_p1 with dissolve

        MC "(Isn’t that the girl who I saw across the street with my binoculars?)"
        MC "(It is! She’s the girl with that older woman! They’re my new neighbours!)"
        scene Ne_MS2_p2
        MC "Hey there, my name’s [player_name]."
        MC "I think I might actually live next door to you. How cool is that?"
        scene Ne_MS2_p3
        MC "(Huh, she looks rather deep in thought.)"
        MC "Hello?"
        Isla "Hmm?"
        scene Ne_MS2_p4
        Isla "Oh! Sorry! Where you talking to me?"
        MC "Yeah, I was just saying that I think we’re neighbours. I’m [player_name]."
        Isla "Ahh, I’m Isla. Nice to meet you!"
        $ Isla_name = "Isla"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene Ne_MS2_p5
        MC "Say, do you fancy hanging out at my place some time?"
        Isla "Umm… Not really, sorry."
        MC "No sweat. Sure, if you even just want to grab a coffee or-"
        scene Ne_MS2_p6
        Isla "I said no!"
        MC "Okay, okay! I get it, that’s a no."
        Isla "*Sigh*"
        MC "I was just trying to be friendly, it’s not like I’m trying to date you or anyth-"
        scene Ne_MS2_p7
        Isla "Will you just go away please? Like right now?"
        MC "Geez, I’m sorry!"
        scene Ne_MS2_p8
        MC "I didn’t mean to offend you."
        Isla "Just… leave me alone. Okay?"
        scene Ne_MS2_p9
        MC "Sheesh…"
        MC "(I wonder what bee got into her bonnet! Maybe she’s not attracted to guys?)"


        $ Ne_MS1 = 5
        $ Ne_MS2 = 3
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump changing_room_morning1
    if Ne_MS2 == 4:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer

        scene Ne_MS2a_p1 with dissolve
        MC "Hey again."
        Isla "Oh, hi. Do you need something?"
        scene Ne_MS2a_p2
        MC "I just wanted to share a really funny story."
        Isla "Sorry, not interested."
        MC "Oh, trust me. You will be! "
        scene Ne_MS2a_p3
        MC "The strangest thing happened to me the other day. I was out for a walk when I heard this moaning sound. So I decided to investigate."
        MC "And then I saw the most unusual thing."
        MC "There were two women in your house eating each others pussies! "
        scene Ne_MS2a_p4
        Isla "W-Wait-"
        MC "And do you want to know the craziest part of all this?"
        MC "They looked EXACTLY like you and that woman you live with!"
        Isla "*Gulp*"
        scene Ne_MS2a_p5
        MC "Y’know, when I asked you out the other day you could have just told me you were a lesbian or that you had a girlfriend."
        Isla "I… I’m not a lesbian."
        MC "Wait, what?"

        scene Ne_MS2a_p6
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music2", loop=True, fadein = 2)
        if renpy.loadable("patch.rpy"):
            Isla "You caught my mum punishing me. She… God, I wish you’d never seen that… She makes me cum for each bad mark I get in mathematics."
        else:
            Isla "You caught Sindra punishing me. She… God, I wish you’d never seen that… She makes me cum for each bad mark I get in mathematics."
        MC "Wait, what?!"
        MC "(I CAN’T have heard that correctly!)"
        scene Ne_MS2a_p7
        if renpy.loadable("patch.rpy"):
            MC "Your mum goes down on your pussy each time you get a bad mark in maths?!"
        else:
            MC "Sidra goes down on your pussy each time you get a bad mark in maths?!"
        MC "Is that not an incentive to do badly?!"
        scene Ne_MS2a_p8
        Isla "It’s not just her going down on me… There’s spanking too."
        Isla "Besides, while one orgasm might be fun - imagine only getting eighty percent in a maths test. That’s twenty orgasms she forces me to have!"
        scene Ne_MS2a_p9
        Isla "Please, please don’t tell anyone!"
        MC "Hey, relax! I’m not gonna say a word to anyone. Promise."
        scene Ne_MS2a_p10
        Isla "Oh, thank you!"
        Isla "God, she should have closed the curtains before she started doing that! I knew we’d get caught again!"
        MC "(They got caught before? I wonder if that’s why they moved house and are living beside us.)"
        scene Ne_MS2a_p11
        MC "Hey, I’ve got an idea!"
        Isla "Huh?"
        MC "How about I tutor you in maths?"
        scene Ne_MS2a_p12
        Isla "Really? You would do that for me?!"
        MC "Of course! I mean, I’m not perfect. You’ll still probably get a couple of questions wrong."
        Isla "I can handle getting a question or two wrong! I can cum seven or eight times before it gets too much to handle!"
        scene Ne_MS2a_p13
        Isla "This is perfect! When can we start?"
        MC "When suits you?"
        if renpy.loadable("patch.rpy"):
            Isla "Come over in the evening. My mum will be out!"
        else:
            Isla "Come over in the evening. Sidra will be out!"
        scene Ne_MS2a_p14
        MC "Great, I’ll see you then, Isla."
        Isla "Thank you so much, [player_name]!"

        $ Ne_ES2 = True
        $ Ne_MS2 = 3

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump changing_room_morning1

    if Ne_MS2 == 5:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer

        scene Ne_MS2aa_p1 with dissolve

        MC "Hey there, Isla. Are you alright?"
        Isla "…"
        MC "Isla?"
        scene Ne_MS2aa_p2
        Isla "…you heard everything, didn’t you?"
        MC "Yeah, I did. I saw it all as well."
        Isla "Ah... "
        scene Ne_MS2aa_p3
        MC "Hey, don’t look so down! It’s fine."
        MC "What happened doesn’t bother me at all, okay?"
        Isla "Okay… Sorry I’m so bad at maths. It’s all my fault..."
        scene Ne_MS2aa_p4
        MC "Whoa, hold on. This isn’t your fault!"
        Isla "Wh-What do you mean?!"
        if renpy.loadable("patch.rpy"):
            MC "I heard your mom on the phone with Celia after you left."
        else:
            MC "I heard Sidra on the phone with Celia after you left."
        Isla "My teacher, Celia?"
        MC "Yeah! She teaches Literature and Mathematics, doesn’t she?"
        Isla "I’m in her maths class…"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music2", loop=True, fadein = 2)

        scene Ne_MS2aa_p5
        if renpy.loadable("patch.rpy"):
            MC "Your mom has been bribing Celia to deliberately lose you marks."
            Isla "WHAT?!"
            MC "Your maths skills probably aren’t that bad at all. Your mom is just using it as an excuse to dish out one of those weird punishments!"
        else:
            MC "Sidra has been bribing Celia to deliberately lose you marks."
            Isla "WHAT?!"
            MC "Your maths skills probably aren’t that bad at all. Sidra is just using it as an excuse to dish out one of those weird punishments!"
        scene Ne_MS2aa_p6
        Isla "Gahhhh!!"
        MC "H-Hey, it’s okay. At least we know now-"
        Isla "*Sob*"
        scene Ne_MS2aa_p7
        MC "Isla?"
        MC "Isla, everything’s going to be alright. I promise."
        Isla "*Sob*"
        scene Ne_MS2aa_p8
        Isla "I don’t even want *sob* to be a lesbian…"
        MC "Huh?"
        Isla "I just want a nice boyfriend who’ll treat me well…"
        scene Ne_MS2aa_p9
        MC "It’s okay, Isla. We’ll work together on this."
        MC "Everything is going to be fine. Now that we know what is going on, we have the advantage."
        scene Ne_MS2aa_p10
        Isla "Ugh! I fucking hate her!"
        MC "I know."
        MC "How about you go to the bathroom and get yourself cleaned up? I’ll meet you later on."
        Isla "….Fine! "
        Isla "Just promise me one thing! You’ll go with me to talk to her soon! "
        MC "Okay, okay. I promise."
        show workinprogress2
        "This is the end of current content in this version for this character."
        hide workinprogress2
        $ Ne_MS2 = False
        $ Ne_MS3 = True

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump changing_room_morning1