image Z_ES1_p1 = "images/Zuri_home/outside/E/scenes/Z_ES1/1.jpg"
image Z_ES1_p2 = "images/Zuri_home/outside/E/scenes/Z_ES1/2.jpg"
image Z_ES1_p3 = "images/Zuri_home/outside/E/scenes/Z_ES1/3.jpg"
image Z_ES1_p4 = "images/Zuri_home/outside/E/scenes/Z_ES1/4.jpg"
image Z_ES1_p5 = "images/Zuri_home/outside/E/scenes/Z_ES1/5.jpg"
image Z_ES1_p6 = "images/Zuri_home/outside/E/scenes/Z_ES1/6.jpg"
image Z_ES1_p7 = "images/Zuri_home/outside/E/scenes/Z_ES1/7.jpg"
image Z_ES1_p8 = "images/Zuri_home/outside/E/scenes/Z_ES1/8.jpg"
image Z_ES1_p9 = "images/Zuri_home/outside/E/scenes/Z_ES1/9.jpg"
image Z_ES1_p10 = "images/Zuri_home/outside/E/scenes/Z_ES1/10.jpg"
image Z_ES1_p11 = "images/Zuri_home/outside/E/scenes/Z_ES1/11.jpg"
image Z_ES1_p12 = "images/Zuri_home/outside/E/scenes/Z_ES1/12.jpg"
image Z_ES1_p13 = "images/Zuri_home/outside/E/scenes/Z_ES1/13.jpg"
image Z_ES1_p14 = "images/Zuri_home/outside/E/scenes/Z_ES1/14.jpg"
image Z_ES1_p15 = "images/Zuri_home/outside/E/scenes/Z_ES1/15.jpg"
image Z_ES1_p16 = "images/Zuri_home/outside/E/scenes/Z_ES1/16.jpg"
image Z_ES1_p17 = "images/Zuri_home/outside/E/scenes/Z_ES1/17.jpg"
image Z_ES1_p18 = "images/Zuri_home/outside/E/scenes/Z_ES1/18.jpg"
image Z_ES1_p19 = "images/Zuri_home/outside/E/scenes/Z_ES1/19.jpg"
image Z_ES1_p20 = "images/Zuri_home/outside/E/scenes/Z_ES1/20.jpg"

default Suri_name = "Suri"
default can_Zv2_ES1 = True

label Z_ES1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene Z_ES1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Well, this looks like the place. It’s a REALLY nice house!)"
    if renpy.loadable("patch.rpy"):
        MC "(I wonder if this was a date. Zuri does seem kinda flirty with me every time I visit Dad.)"
    else:
        MC "(I wonder if this was a date. Zuri does seem kinda flirty with me every time I visit Bob.)"
    MC "(Maybe I’m just overthinking things right now.)"

    $ renpy.sound.play("sfx/knock_knock.wav")
    "*KNOCK KNOCK KNOCK*"
    $ renpy.music.stop(channel="sound", fadeout=1)
    $ Zuri_name = "???"
    Zuri "COOOOOMMMIINNGGGGGGGG!"
    $ Zuri_name = "Zuri"

    scene Z_ES1_p2

    Zuri "Oh! Hey! Is that you!?"
    MC "(Holy shit! She’s almost naked!)"
    MC "I- Uh- Hi-"
    Zuri "Well, what are you waiting for? Come on in? Just don’t stand out there like a big dumbo!"

    scene Z_ES1_p3

    Zuri "What’s wrong? You look shell-shocked, kid."
    MC "Y-You’re… bottoms… You’re.."
    Zuri "What’s wrong, kid? You’re stammering on me."
    MC "You’ve got… bottom…"

    scene Z_ES1_p4

    Zuri "Is there something on me?"
    MC "You’re only wearing panties!"
    Zuri "What do you mean?"

    scene Z_ES1_p5

    MC "I… uh (Jesus! Why am I so nervous right now!)"
    MC "(Why is Zuri acting so weird! She’s NEVER like this in the office!)"
    Zuri "I don’t see anything down me."

    scene Z_ES1_p6

    Zuri "Oooh! Are you just shocked that I’m only wearing panties?"
    MC "Y-Yes!"
    Zuri "Haha! How cute! Are you a virgin, or something?"
    MC "Wh-What?"
    Zuri "Go ahead and take a seat on the couch."

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_Zv2_ES1 = False
    $ can_hide_windows = False
    jump zuri_home_E_label2

label Z_ES1_q2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES1_p7
    $ can_hide_windows = True
    MC "So, uh… You wanted me to come over tonight?"
    MC "What did you, um… plan to do? Dinner? Or a movie?"
    Zuri "You talk a lot, kid."

    scene Z_ES1_p8

    Zuri "Just breathe and try to relax. You’re making ME feel nervous now."
    Zuri "Have you never seen a girl dressed like a slut before?"
    MC "Y-Yes. I mean…"

    scene Z_ES1_p9

    Zuri "Then you shouldn’t be this nervous around me."
    Zuri "Now go and sit on the couch."

    jump Z_ES1_q1_label

label Z_ES1_q1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES1_p10
    $ can_hide_windows = True
    MC "(What the hell is going on?)"
    MC "(Zuri isn’t acting like herself, at all. And I have NO idea what she even invited me over here for.)"
    MC "(She’s dressed really scantily, so perhaps she wants to have sex?)"

    scene Z_ES1_p11

    Zuri "Ahh, there you are."
    MC "Wow! You got dressed quickly!"
    Zuri "Hmm?"

    scene Z_ES1_p12

    MC "You really scared me when you opened the front door, almost naked!"
    Zuri "Uh huh…"
    MC "Seriously, what if it wasn’t me? What if it was, like the postman or someone?"

    scene Z_ES1_p13

    Zuri "I didn’t open the door for you."
    MC "Huh?"
    Zuri "And I’ve been wearing these clothes all night."
    MC "Then who-"

    scene Z_ES1_p14
    $ Suri_name = "???"
    Suri "Boo!"
    MC "Ahh!"
    if renpy.loadable("patch.rpy"):
        Zuri "[player_name], meet my twin sister, Suri."
    else:
        Zuri "[player_name], meet, Suri."
    $ Suri_name = "Suri"
    Suri "Sorry I didn’t tell you earlier. I just couldn’t resist, winding you up a bit."

    scene Z_ES1_p15

    MC "There’s two of you?!"
    if renpy.loadable("patch.rpy"):
        Zuri "Oh yes. Suri doesn’t work at your dad’s company though."
    else:
        Zuri "Oh yes. Suri doesn’t work at Bob’s company though."
    MC "Why did you want me to come over tonight then?"

    scene Z_ES1_p16

    Zuri "This isn’t a date. I’m sure you know that much by now."
    if renpy.loadable("patch.rpy"):
        Zuri "It’s a business proposition. Your father is currently building an investment portfolio of very wealthy companies. If he acquires a majority of their shares, his company could be set to earn millions."
    else:
        Zuri "It’s a business proposition. Bob is currently building an investment portfolio of very wealthy companies. If he acquires a majority of their shares, his company could be set to earn millions."
    Zuri "This is where you come in."

    scene Z_ES1_p17

    Suri "We want you to get us the company names."
    if renpy.loadable("patch.rpy"):
        MC "Wh-Why would I do that? Wouldn’t that hurt my dad’s company?"
    else:
        MC "Wh-Why would I do that? Wouldn’t that hurt Bob’s company?"
    Suri "Of course! Big time!"
    Suri "But we’re offering you something REALLY fun."

    scene Z_ES1_p18
    if renpy.loadable("patch.rpy"):
        Zuri "This may be the ONLY time in your life you will ever be with twins."
    else:
        Zuri "This may be the ONLY time in your life you will ever be with us."
    Zuri "That’s right. For every company name you give us, we’ll give you some sexual rewards."
    Zuri "How does that sound?"
    MC "(Holy shit… I’m so conflicted right now.)"

    scene Z_ES1_p19

    Zuri "I’ll leave you alone now to make up your mind."
    Zuri "In the meantime, I’m sure that Suri can… help convince you of the right decision."
    if renpy.loadable("patch.rpy"):
        Suri "I certainly can, Sis."
    else:
        Suri "I certainly can, Zuri."

    scene Z_ES1_p20

    Suri "This is just a taste of what will come if you help us."
    Suri "What do you say?"
    MC "(Wow! Those tits are amazing!)"
    MC "I… uh…"
    Suri "Take some time to think about it. Then speak with Zuri when you’re ready to make a decision."
    $ zuri_bath_event_unlock = True
    $ day_time = 4
    $ Zv2_ES1 = False
    $ Zv2_MS2_q9 = True
    $ zuri_inhome = False
    $ Bobv2_MS1_q4 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
