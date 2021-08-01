image CR3_MS2_p1 = "images/home/entrace1/morning/scenes/CR3_MS2/1.jpg"
image CR3_MS2_p2 = "images/home/entrace1/morning/scenes/CR3_MS2/2.jpg"
image CR3_MS2_p3 = "images/home/entrace1/morning/scenes/CR3_MS2/3.jpg"
image CR3_MS2_p4 = "images/home/entrace1/morning/scenes/CR3_MS2/4.jpg"
image CR3_MS2_p5 = "images/home/entrace1/morning/scenes/CR3_MS2/5.jpg"
image CR3_MS2_p6 = "images/home/entrace1/morning/scenes/CR3_MS2/6.jpg"
image CR3_MS2_p7 = "images/home/entrace1/morning/scenes/CR3_MS2/7.jpg"
image CR3_MS2_p8 = "images/home/entrace1/morning/scenes/CR3_MS2/8.jpg"
image CR3_MS2_p9 = "images/home/entrace1/morning/scenes/CR3_MS2/9.jpg"
image CR3_MS2_p10 = "images/home/entrace1/morning/scenes/CR3_MS2/10.jpg"

label CR3_MS2_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_MS2_p1 with dissolve

    Caroline "One... Two... Three..."
    MC "(It looks like Caroline is stretching. She must be going out for some exercise!)"
    MC "Hey Caroline, what’s up?"

    scene CR3_MS2_p2

    Caroline "Hi, [player_name]! Two seconds!"
    Caroline "Four... Five... Six!"
    Caroline "Sorry about that. I just wanted to finish, stretching out my calves."
    scene CR3_MS2_p3

    MC "Are you heading off to the gym?"
    Caroline "Not today! The weather is great, so I’m going to jog in - the great outdoors. A couple of laps around the block ought to do me."
    MC "Any particular reason?"

    scene CR3_MS2_p4

    Caroline "Yeah, I mostly run to clear my head. My brain’s fried, after that damn tax return I had to submit. Plus, I’m trying to get myself in shape."
    MC "Are you serious? You’re in great shape already!"
    Caroline "I thought I was too - but this new batch of clothes I ordered are a size too small for me. I’m gonna have to tone myself up, here."

    scene CR3_MS2_p5

    MC "Cool! If you wait five minutes, I could grab my tracksuit and join you!"
    Caroline "Sorry, [player_name]. This is something I prefer to do on my own. It’s - me time."
    MC "Oh, okay..."

    scene CR3_MS2_p6

    Caroline "What’s wrong? You’re looking downhearted, all of a sudden."
    MC "It’s just... It’s nothing."
    Caroline "Aww c’mon - you can tell ME."

    scene CR3_MS2_p7

    MC "It just, kinda feels that you’re avoiding me - ever since this deal ended. I mean, we used to hang out more than this, right?"
    Caroline "*Sigh*"
    Caroline "How often did we hang out before the deal?"
    MC "I uh... I don’t remember."
    Caroline "Let me remind you, We - almost NEVER - hung out. Then, once this deal came into place, we were seeing each other all the time."

    scene CR3_MS2_p8
    if persistent.incest_patch == True:
        Caroline "We can work out a healthy balance, but as of now, I’m your sister, NOT your girlfriend."
    else:
        Caroline "We can work out a healthy balance, but as of now, I’m your close friend, NOT your girlfriend."
    MC "...You were never my girlfriend. It was just a-"
    Caroline "-I know exactly what it was. There’s no need to rehash it. Can’t we just bury this, and move on?"

    scene CR3_MS2_p9

    MC "How can you expect me to just, bury and forget, after everything that we did together?"
    Caroline "One... Two... Three..."
    MC "(Dammit...! She’s stretching again.)"

    scene CR3_MS2_p10

    Caroline "Okay, [player_name] - Gotta go! There ain’t no way I’m getting into those outfits, if I don’t get started today!"
    MC "*Sigh* See you later, Caroline."
    MC "(What has gotten into her? Why has she had, such a sudden change of heart, about our deal.)"

    $ CR3_MS2 = False
    $ CR3_MS2_can = False
    $ CR3_MS1_can = True

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump entrace1_morning1

