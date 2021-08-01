image CR4_Cindy_S1_p1 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/1.jpg"
image CR4_Cindy_S1_p2 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/2.jpg"
image CR4_Cindy_S1_p3 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/3.jpg"
image CR4_Cindy_S1_p4 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/4.jpg"
image CR4_Cindy_S1_p5 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/5.jpg"
image CR4_Cindy_S1_p6 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/6.jpg"
image CR4_Cindy_S1_p7 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/7.jpg"
image CR4_Cindy_S1_p8 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/8.jpg"
image CR4_Cindy_S1_p9 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/9.jpg"
image CR4_Cindy_S1_p10 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/10.jpg"
image CR4_Cindy_S1_p11 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/11.jpg"
image CR4_Cindy_S1_p12 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/12.jpg"

image CR4_Cindy_S2_p1 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/1.jpg"
image CR4_Cindy_S2_p2 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/2.jpg"
image CR4_Cindy_S2_p3 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/3.jpg"
image CR4_Cindy_S2_p4 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/4.jpg"
image CR4_Cindy_S2_p5 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/5.jpg"
image CR4_Cindy_S2_p6 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/6.jpg"
image CR4_Cindy_S2_p7 = "images/Nightclub/Corridor/N/Scenes/CR4_Cindy/S2/7.jpg"

default warehouse_unlocked = False
label CR4_Cindy_S1_lab:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene CR4_Cindy_S1_p1 with dissolve
    MC "(God dammit… I can’t believe this. I was SO fucking close!)"
    MC "(Caroline’s necklace could be right behind that door!)"

    scene CR4_Cindy_S1_p2
    MC "(Why the hell does a nightclub require a password to speak with the manager? None of this makes any fucking sense!)"
    MC "(And why was Charles so scared to repay this nightclub for the damages he caused?)"

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/realizer.mp3', channel="music1", loop=True, fadein = 2)

    scene CR4_Cindy_S1_p3

    $ Cindy_name = "???"

    Cindy "Why, hi there, baby!"
    MC "Huh?"

    scene CR4_Cindy_S1_p4
    MC "I… uh… don’t I know you from somewhere? You seem familiar."
    Cindy "The name’s Cindy! We go to the same school!"
    $ Cindy_name = "Cindy"
    MC "Oh shit, yes! I remember you now! I knew I recognised you from somewhere."

    scene CR4_Cindy_S1_p5
    Cindy "Are you with anyone tonight?"
    MC "Nah, just by myself."
    Cindy "Oh, you must be seeing the Ghos- *Ahem* I mean, the boss too!"

    scene CR4_Cindy_S1_p5
    MC "You know the boss of this place!?"
    Cindy "Uh, yeah. Do you not, baby?"
    MC "Not yet… But I want to."

    scene CR4_Cindy_S1_p7
    MC "Can you help me arrange a meeting? All I need is the password to the-"
    Cindy "Hehehe! You think I’m just gonna give you the password like that, baby?"

    scene CR4_Cindy_S1_p8
    Cindy "I’ll cut you a deal - scratching two heads is better than one."
    MC "I’m not sure that’s the correct expression… Do you mean you’ll scratch my back if I scratch yours?"
    Cindy "No?"
    MC "*Sigh* Fine, why not. What do you need?"

    scene CR4_Cindy_S1_p9
    Cindy "Great! There’s a warehouse nearby. Inside that you’ll find a bright pink box."
    Cindy "Take these keys. You’ll need them to get in. Bring me back that pink box."
    Cindy "Easy, right?"

    scene CR4_Cindy_S1_p10
    MC "This isn’t legal, is it?"
    Cindy "Of course not, baby. But if you’re not willing to get two birds dirty with one hand, then you-"
    MC "I don’t think that’s a real expression either…"

    scene CR4_Cindy_S1_p11
    Cindy "Are you sure?"
    MC "I’m… more certain of this than anything else in my life."
    Cindy "Hmm… I’d ask my English teacher on Monday, but I always skip his classes."
    MC "(That explains a lot!)"

    scene CR4_Cindy_S1_p12
    Cindy "Hit me up when you got that pink box, baby!"
    MC "Stay right here. I’ll be back soon."

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)

    $ inventory.add(warehouse_key)
    $ CR4_Cindy_S1 = 2
    $ can_hide_windows = False
    $ warehouse_unlocked = True

    jump nightclub_N1

label CR4_Cindy_S2_lab:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/realizer.mp3', channel="music2", loop=True, fadein = 2)

    scene CR4_Cindy_S2_p1 with dissolve
    MC "You almost got me killed! That was soooo fucking dangerous!"
    Cindy "Kinda hot, baby, ain’t it?"
    MC "What?! NO! They had GUNS! What kinda place is that?"
    Cindy "Aww, stop being a pussy! C’mon and pass the box over."
    MC "*Sigh* There you go."

    scene CR4_Cindy_S2_p2
    Cindy "Fine - I’m not gonna beat around the drawing board."
    MC "(Christ almighty… Stay in school, kids.)"
    Cindy "This place is a front, baby. It ain’t just a nightclub."

    scene CR4_Cindy_S2_p3
    MC "Are you saying this is for money laundering?"
    Cindy "Uh huh! And so so much more, baby!"
    MC "(Shit, this could make getting Caroline’s necklace back, very difficult.)"

    scene CR4_Cindy_S2_p4
    MC "I upheld my end of the bargain. I need the password."
    Cindy "The password is… the name of this Nightclub!"
    MC "This club is called ‘Truth’."

    scene CR4_Cindy_S2_p5
    Cindy "SHUSH! You can’t just go around blurting out the password!"
    MC "But… that’s literally the name of the club. People are probably saying that all night long…"

    scene CR4_Cindy_S2_p6
    Cindy "Huh… I guess you’re right! You’re like super smart, ain’tcha, baby?"
    MC "*Sigh* If I say “Truth” to those bouncers, will they let me past?"
    Cindy "Uh huh!"

    scene CR4_Cindy_S2_p7
    Cindy "Catch ya later, baby! Good luck meeting the Boss!"
    MC "Thanks. It sounds like I’ll need it. See you later."

    $ inventory.drop(cindy_box)
    $ CR4_Cindy_S1 = 4
    $ can_hide_windows = False

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)

    $ CR4_guard = 3
    jump nightclub_N1

