image CeR2_moni_p1 = "images/CeR2/Monitoring/Talking/1.jpg"
image CeR2_moni_p2 = "images/CeR2/Monitoring/Talking/2.jpg"
image CeR2_moni_p3 = "images/CeR2/Monitoring/Talking/3.jpg"
image CeR2_moni_p4 = "images/CeR2/Monitoring/Talking/4.jpg"
image CeR2_moni_p5 = "images/CeR2/Monitoring/Talking/5.jpg"
image CeR2_moni_p6 = "images/CeR2/Monitoring/Talking/6.jpg"
image CeR2_moni_p7 = "images/CeR2/Monitoring/Talking/7.jpg"
image CeR2_moni_p8 = "images/CeR2/Monitoring/Talking/8.jpg"
image CeR2_moni_p8a = "images/CeR2/Monitoring/Talking/8a.jpg"

default CeR2_moni = 1
default B_J_name = __("Big Jake")
define B_J = Character("[B_J_name]", color="#6600FF")

label CeR2_moni_lab:
    hide screen map_button
    if CeR2_moni == 2:
        if day_time == 2:
            show screen moni_D_scr
        if day_time == 1:
            show screen moni_M_scr
        $ clickable = False
        MC "I've already talked to him."
        $ clickable = True
        hide screen moni_D_scr
        hide screen moni_M_scr
        jump moni_M1

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer


    if CeR2_moni == 1:

        $ B_J_name = "???"

        scene CeR2_moni_p1 with dissolve
        MC "(Oh wow… this place is awesome!)"
        MC "(It looks like something straight out of a James Bond film!)"

        scene CeR2_moni_p2
        MC "(This must be the guy who handles the security. He’s way too overweight to be a conventional security guard. This must be why they have him holed up in this backroom.)"
        MC "Hey there, I love your setup. You can see the entire college from here!"

        scene CeR2_moni_p3
        B_J "*Wheeze*"
        MC "…"
        MC "Umm… There’s a lot of buttons and stuff. Do you use them all?"

        scene CeR2_moni_p4
        B_J "*SHLUUURRRRP*"
        MC "Not a very talkative guy, are you?"
        B_J "*Shlurp*"

        scene CeR2_moni_p5
        B_J "Whatcha want, kid?"
        MC "I was just looking around. The name’s [player_name]."
        B_J "Uh huh… I’m Big Jake."
        $ B_J_name = __("Big Jake")

        scene CeR2_moni_p6
        MC "Nice to meet-"
        B_J "Ya shouldn’t be here. *Wheeze* No students."
        MC "Yeah, I was just-"
        B_J "Scram, lad."

        scene CeR2_moni_p7
        MC "Umm… Okay, no problem."
        MC "Just before I go, how long have you worked here? I don’t remember seeing you around before."
        B_J "I’ve been here ever since they hired me."
        MC "And that was…"
        B_J "The same day I started *Wheeze* working here."
        MC "(Fuck me… It’s like talking with a Furby.)"

        scene CeR2_moni_p8
        B_J "I’m serious, lad. No students in the security suite. Scam."
        MC "Are there rules about having food in the security suite?"
        B_J "*Wheeze* That’s it, I’m calling the *Wheeze* headmaster."
        MC "Ugh, don’t bother. I’m leaving."
        B_J "Don’t let the *Wheeze* door hit you ass on the way out."

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
        $ can_hide_windows = False
        $ CeR2_moni = 2
        jump school_corridor2_morning1

    if CeR2_moni == 3:

        scene CeR2_moni_p1 with dissolve
        MC "Hey there, Big Jake. Me again!"
        MC "How are you keeping?"

        scene CeR2_moni_p4
        B_J "*Slurp*"
        MC "I… uh… I see you got yourself another burger…"
        B_J "*Shlurrrp*"
        MC "...and a pizza too."

        scene CeR2_moni_p5
        MC "(None of the fast food packaging matches. The only explanation I can come up with is that this guy has literally gone to at least three different fast food joints on his lunch.)"
        MC "(He must have picked up the burger from one place, the pizza from another, and God-knows-what was in that red box.)"
        MC "(It’s actually rather impressive, the dedication that he is putting into his lunch hour.)"
        B_J "Didn’t I see you before? No students in here. Vamanos!"

        scene CeR2_moni_p7
        MC "Aww, c’mon man. I just wanted to see how it all worked in here."
        B_J "*Wheeze* You’re interrupting my lunch hour. This is my happy time - and you’re ruining it."
        MC "Just-"
        B_J "Do I have to *Wheeze* get off my seat and call the headmaster?"

        scene CeR2_moni_p8a
        MC "*Sigh* No. I’ll go now."
        MC "(There has to be a way to distract this guy so I can actually get access to the monitoring system.)"
        MC "(It’s the only way I’ll ever be able to delete those security tapes.)"


        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
        $ can_hide_windows = False
        $ CeR2_moni = 4

        jump school_corridor2_morning1