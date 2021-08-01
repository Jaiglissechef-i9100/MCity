image Vv2_AS1_p1 = "/images/dark_alley/D/scenes/Vv2_AS1/1.jpg"
image Vv2_AS1_p2 = "/images/dark_alley/D/scenes/Vv2_AS1/2.jpg"
image Vv2_AS1_p3 = "/images/dark_alley/D/scenes/Vv2_AS1/3.jpg"
image Vv2_AS1_p4 = "/images/dark_alley/D/scenes/Vv2_AS1/4.jpg"
image Vv2_AS1_p5 = "/images/dark_alley/D/scenes/Vv2_AS1/5.jpg"
image Vv2_AS1_p6 = "/images/dark_alley/D/scenes/Vv2_AS1/6.jpg"
image Vv2_AS1_p7a = "/images/dark_alley/D/scenes/Vv2_AS1/7a.jpg"
image Vv2_AS1_p7b = "/images/dark_alley/D/scenes/Vv2_AS1/7b.jpg"
image Vv2_AS1_p8 = "/images/dark_alley/D/scenes/Vv2_AS1/8.jpg"
image Vv2_AS1_p8a = "/images/dark_alley/D/scenes/Vv2_AS1/8a.jpg"
image Vv2_AS1_p8b = "/images/dark_alley/D/scenes/Vv2_AS1/8b.jpg"
image Vv2_AS1_p8c = "/images/dark_alley/D/scenes/Vv2_AS1/8c.jpg"
image Vv2_AS1_p8d = "/images/dark_alley/D/scenes/Vv2_AS1/8d.jpg"
image Vv2_AS1_p8e = "/images/dark_alley/D/scenes/Vv2_AS1/8e.jpg"
image Vv2_AS1_p8f = "/images/dark_alley/D/scenes/Vv2_AS1/8f.jpg"
image Vv2_AS1_p8g = "/images/dark_alley/D/scenes/Vv2_AS1/8g.jpg"
image Vv2_AS1_p8h = "/images/dark_alley/D/scenes/Vv2_AS1/8h.jpg"
image Vv2_AS1_p8i = "/images/dark_alley/D/scenes/Vv2_AS1/8i.jpg"
image Vv2_AS1_p8j = "/images/dark_alley/D/scenes/Vv2_AS1/8j.jpg"
image Vv2_AS1_p9 = "/images/dark_alley/D/scenes/Vv2_AS1/9.jpg"
image Vv2_AS1_p10 = "/images/dark_alley/D/scenes/Vv2_AS1/10.jpg"
image Vv2_AS1_p11 = "/images/dark_alley/D/scenes/Vv2_AS1/11.jpg"
image Vv2_AS1_p12 = "/images/dark_alley/D/scenes/Vv2_AS1/12.jpg"
image Vv2_AS1_p13 = "/images/dark_alley/D/scenes/Vv2_AS1/13.jpg"
image Vv2_AS1_p14 = "/images/dark_alley/D/scenes/Vv2_AS1/14.jpg"
image Vv2_AS1_p15 = "/images/dark_alley/D/scenes/Vv2_AS1/15.jpg"

default V_points = 1
default Dwayne_name = "Dwayne"
default player_name1 = "{color=#3366FF}[player_name]{/color}"

label Vv2_AS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Vv2_AS1_p1 with dissolve
    $ can_hide_windows = True
    MC "(This looks like the area Caroline told me to check...)"
    MC "(And THAT looks like Violet over there! I wonder who she’s with.)"
    MC "(I can’t confront her in front of him - he’d beat the shit out of me in a fight!)"
    MC "(I’ll hang back and watch what’s going on first…)"

    scene Vv2_AS1_p2

    Violet "I-I’m sorry, Dwayne."
    Dwayne "Sorry’s not gunna cut it, is it?"
    Violet "N-No… *Sniff*"

    scene Vv2_AS1_p3

    Dwayne "You OWE me. Never forget that."
    Violet "I won’t, Dwayne."
    Dwayne "I mean, shit, I asked you to do ONE simple thing for me."
    Dwayne "One simple thing!"

    scene Vv2_AS1_p4

    Dwayne "And my stupid fucking sister can’t even get that right!"
    Dwayne "I oughta just turn you into the cops right now! How would you like to serve some time in jail, like I did? Huh?!"
    Violet "Noooo!"

    scene Vv2_AS1_p5

    Violet "Ooof!"
    Dwayne "Next time, you better rob a store that has some fucking money in it!"
    Dwayne "How am I supposed to pay the cartel back, with this shit?! Huh?!"

    scene Vv2_AS1_p6

    Violet "P-Please! No more!"
    Dwayne "Stupid..! Fucking..! Bitch..!"
    window hide
    menu:
        "Intervene to help Violet. You’ve got to save her!":
            scene Vv2_AS1_p8

            MC "(Fuck! He’s gonna murder her! I can’t just stand still and watch!)"
            MC "(Should I punch him? Or maybe kick him?)"
            window hide
            menu:
                "Punch him!":
                    scene Vv2_AS1_p8b

                    MC "Hyaaaahhh!"
                    Dwayne "UGH!"
                    MC "Leave her alone!"
                    MC "(Take that, you bastard!)"
                    jump Vv2_AS1_q1
                "Kick him!":
                    scene Vv2_AS1_p8a

                    MC "Hey! Leave her alone!"
                    "*WHACK*"
                    Dwayne "Ooof!"
                    jump Vv2_AS1_q1
        "Stay out of it! This guy would murder you!":


            scene Vv2_AS1_p7a

            "*THUD*"
            Violet "Eeeek!"
            Dwayne "Arrgh! You made me hurt my fucking fist."

            scene Vv2_AS1_p7b

            Dwayne "Get me actual money next time."
            Dwayne "If you screw up again, then YOU’LL be the one paying the cartel back."
            Dwayne "I’m sure they’ll knock a few grand off my decbt, for a month of letting them use your body."
            Violet "N-No! Please!"
            Dwayne "Then get me the rest of the money."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
            jump Vv2_AS1_continue

label Vv2_AS1_q1:
    scene Vv2_AS1_p8c

    Dwayne "Huh? Oh look, Violet. You’ve got your very own white knight."
    Dwayne "Looks like I’m gunna have to teach this punk a lesson too."
    MC "I said, leave her alon-"

    scene Vv2_AS1_p8d

    "*THWACK*"

    MC "OUCH!"
    MC "(Fuck!)"

    scene Vv2_AS1_p8e

    MC "Owww..."
    MC "(Jesus Christ… My head’s spinning…)"

    scene Vv2_AS1_p8f

    Dwayne "I don’t know what the hell you were thinking, trying to take me on, you little piece of shit."
    Dwayne "But it’s time to put you back where you belong."
    MC "Ahh…."

    scene Vv2_AS1_p8g

    Dwayne "In the fucking garbage."
    MC "H-Hey! Stop! Put me down!"
    MC "Ahhhh!"

    scene Vv2_AS1_p8h

    Dwayne "Fucking punk kid. They got no respect for anyone nowadays."
    MC "Owwww…."
    Dwayne "I’ll be back for the rest of that money later, Violet. Don’t forget it."

    scene Vv2_AS1_p8i

    MC "(Is… Is he gone yet?)"
    MC "(Almost…)"
    MC "(That bastard’s probably given me a damn black eye! He punches like a fucking truck!)"

    scene Vv2_AS1_p8j
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)

    MC "Oh God… Violet…"
    MC "(Is she alright?! I have to go and check…)"
    MC "(I hope that asshole hasn’t hurt her!)"
    jump Vv2_AS1_continue

label Vv2_AS1_continue:

    scene Vv2_AS1_p9
    MC "Hey Violet...?"
    Violet "…"
    MC "Violet? Can you hear me?"

    scene Vv2_AS1_p10

    Violet "Ahh!"
    MC "Hey! It’s just me! It’s just me!"
    MC "Dwayne’s gone."
    Violet "Oh fuck…"
    MC "Let me help you get back on your feet."

    scene Vv2_AS1_p10

    Violet "Thanks for helping me, back there."
    MC "It’s not a problem - I'd do the same for anyone."
    Violet "You’re a good person."

    scene Vv2_AS1_p11

    Violet "I uh… guess this means, you know that I stole from Caroline now."
    MC "Yeah, I do!"
    Violet "Please don’t tell her. She’s the only friend that I truly trust..."
    Violet "I’ll get her the money back - somehow. I promise."
    $ menu_q1 = True
    $ menu_q2 = True
    jump Vv2_AS1_menu

label Vv2_AS1_menu:
    window hide
    scene Vv2_AS1_p11
    menu:
        "Why was that asshole beating you up?" if menu_q1 == True:
            scene Vv2_AS1_p11

            MC "Why was that asshole beating you up?"

            scene Vv2_AS1_p13

            Violet "God… I was stupid a few years ago. I smuggled some drugs for an ex-boyfriend."
            Violet "That guy, Dwayne, has enough evidence to put me in prison. In exchange for not showing it to the police, he makes me do odd jobs for him - like robbing Caroline’s store."
            MC "Jesus…"
            $ menu_q1 = False
            if menu_q2 == True and menu_q1 == True:
                jump Vv2_AS1_continue2
            else:
                jump Vv2_AS1_menu

        "Who is that asshole?" if menu_q2 == True:
            scene Vv2_AS1_p11

            MC "Who was that asshole?"

            Violet "It’s my brother, Dwayne. He’d been in jail for four, maybe five years. "

            Violet "I hadn’t missed him at all. But now he’s back, he’s just as bad as ever."
            MC "Has he beaten you before?"
            Violet "The beatings used to be daily. I’m used to them, don’t worry."

            $ menu_q2 = False
            if menu_q2 == True and menu_q1 == True:
                jump Vv2_AS1_continue2
            else:
                jump Vv2_AS1_menu

label Vv2_AS1_continue2:
    scene Vv2_AS1_p14

    Violet "Owww…"
    MC "Are you okay?"
    Violet "Just a bit sore. I need to go home and lie down."
    MC "Can I help you?"

    scene Vv2_AS1_p15

    Violet "N-No, I don’t need your help. I can handle this by myself."
    MC "Are you sure?"
    Violet "Just… Just focus on taking care of Caroline, okay?"
    MC "(That girl really needs more help than she’s letting on. Something needs to be done about Dwayne...)"
    $ violetV2_scene = False
    $ violet_scene2 = True
    $ V_points = 2
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ day_time +=1
    jump dark_alley_label

