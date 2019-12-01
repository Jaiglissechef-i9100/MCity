image Zv2_ES3a_p6 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/6.jpg"
image Zv2_ES3a_p6anim = Movie(play="videos/02 Zuri-1.webm", loop = True )
image Zv2_ES3a_p7 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/7.jpg"
image Zv2_ES3a_p7anim = Movie(play="videos/02 Zuri-2.webm", loop = True )
image Zv2_ES3a_p8 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/8.jpg"
image Zv2_ES3a_p9 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/9.jpg"
image Zv2_ES3a_p9anim = Movie(play="videos/02 Zuri-3.webm", loop = True )
image Zv2_ES3a_p10 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/10.jpg"
image Zv2_ES3a_p11 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/11.jpg"
image Zv2_ES3a_p12 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/12.jpg"
image Zv2_ES3a_p13 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/13.jpg"
image Zv2_ES3a_p14 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/14.jpg"
image Zv2_ES3a_p15 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/15.jpg"

default Zv2_ES3a = False
default Zv2_ES4 = False
default Zv2_ES4_counter = 0

label Zv2_ES3a_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Zv2_ES3_p1 with dissolve
    $ can_hide_windows = True
    Zuri "Welcome back, [player_name]."
    Zuri "Thanks again for your help! Let’s go to our, room of pleasure."
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene Zv2_ES3_p2

    Zuri "You’ve done another excellent job for us."
    Suri "Yeah, you really came through, kid. You’re gonna make us super rich!"
    MC "I get another reward now, right?"
    Suri "Hehe... You do. I believe we promised you a blowjob."

    scene Zv2_ES3lick_p1
    Suri "Mmm, I can’t wait to suck on his cock. It looked sooo delicious, last time we did it!"
    Zuri "Well? What are we waiting for? Let’s get these pants off him."
    MC "(This is gonna be great!)"

    scene Zv2_ES3lick_p2

    Suri "So, which of us gets to suck it first?"
    MC "I’m not fussy!"
    Zuri "Be my guest, Suri!"

    scene Zv2_ES3lick_p3

    Zuri "If you enjoy us doing this, then just wait till you see what we have in store for you, for the grand finale!"
    Suri "Yeah, we’ll blow your cock today, but next time - we’ll blow your mind!"

    scene Zv2_ES3lick_p4

    Suri "Are you always this hard, kid?"
    Suri "I don’t think I’ve ever seen you, without a massive erection."
    MC "It’s hard not to have one, when I’m near someone as beautiful as you."

    scene Zv2_ES3lick_p5

    Suri "Lick Lick"
    Zuri "Lick Lick"
    MC "Mmm… That’s good. RIght there…"

    scene Zv2_ES3a_p6

    Suri "Suuuuck"
    MC "Oooh…"
    MC "(I can feel Suri’s mouth, wrapped around the tip of my cock. It’s so hot and wet!)"

    scene Zv2_ES3a_p7

    MC "God… Mmmm…"
    scene Zv2_ES3a_p6anim
    Zuri "Lick Lick"
    scene Zv2_ES3a_p7anim
    Suri "Shluuurrrp"

    scene Zv2_ES3a_p8

    MC "(This is too much! Their tongues are so good!)"
    MC "(Who knew, corporate espionage could feel so right?)"
    Zuri "Mmmm…"
    Suri "Lick Lick"

    scene Zv2_ES3a_p9

    Zuri "Suck Suck"
    scene Zv2_ES3a_p9anim
    if persistent.incest_patch == True:
        MC "(Damn, Zuri is just as good at sucking cock, as her twin sister is!)"
    else:
        MC "(Damn, Zuri is just as good at sucking cock as Suri is!)"
    MC "(The two of them together, are fucking incredible!)"

    scene Zv2_ES3a_p10

    Zuri "GULP"
    MC "Fuck! Mmm!"
    MC "(I can feel Zuri’s tight throat around my glans!)"

    scene Zv2_ES3a_p11

    MC "(If she keeps this up, I’m gonna cum! It’s too intense!)"
    MC "Hnnng! Ahh!"
    Zuri "Shluuuuuurrrrp"

    scene Zv2_ES3a_p12

    Suri "MMPPFFF!!!"
    Zuri "Oops! Sorry, Suri!"
    MC "Ahhh! Huh?"

    scene Zv2_ES3a_p13
    if persistent.incest_patch == True:
        Zuri "Sorry, it looks like my sister’s head has... accidentally fallen on your cock."
    else:
        Zuri "Sorry, it looks like Suri's head has... accidentally fallen on your cock."
    Suri "Mmmpfff! SHLURRRRP"
    MC "Oh! Ahhhh!"

    scene Zv2_ES3a_p14

    MC "I’m cumming!"
    Zuri "Drink it ALL up, Suri!"
    Suri "SHLURRRP! COUGH!"
    MC "HNNNNNGGG!!! UGH! YES!"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene Zv2_ES3a_p14 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene Zv2_ES3a_p14 with dissolve
    MC "(I can feel my cock twitching in her mouth! She’s drinking me dry!)"

    scene Zv2_ES3a_p15

    MC "Wow… That was amazing..."
    Suri "Zuri! You naughty bitch!"
    Zuri "Hehe! I couldn’t resist!"
    Suri "I’m gonna have to spank you later on tonight, for that!"
    Zuri "Feel free to go now, [player_name]."
    $ Zv2_ES3a = False
    $ zuri_inhome = False
    $ day_time = 4
    $ Zv2_ES4 = 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
