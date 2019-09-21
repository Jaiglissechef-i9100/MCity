image MLR2_NS2_p1 = "images/home/salon/night/scenes/MLR2_NS2/1.jpg"
image MLR2_NS2_p2 = "images/home/salon/night/scenes/MLR2_NS2/2.jpg"
image MLR2_NS2_p3 = "images/home/salon/night/scenes/MLR2_NS2/3.jpg"
image MLR2_NS2_p4 = "images/home/salon/night/scenes/MLR2_NS2/4.jpg"
image MLR2_NS2_p5 = "images/home/salon/night/scenes/MLR2_NS2/5.jpg"
image MLR2_NS2_p6 = "images/home/salon/night/scenes/MLR2_NS2/6.jpg"
image MLR2_NS2_p8 = "images/home/salon/night/scenes/MLR2_NS2/8.jpg"
image MLR2_NS2_p9 = "images/home/salon/night/scenes/MLR2_NS2/9.jpg"
image MLR2_NS2_p10 = "images/home/salon/night/scenes/MLR2_NS2/10.jpg"
image MLR2_NS2_p11 = "images/home/salon/night/scenes/MLR2_NS2/11.jpg"
image MLR2_NS2_p11anim = Movie(play="videos/02 Linda-NS2-2.webm", loop = True )
image MLR2_NS2_p12 = "images/home/salon/night/scenes/MLR2_NS2/12.jpg"
image MLR2_NS2_p12anim = Movie(play="videos/02 Linda-NS2-1.webm", loop = True )
image MLR2_NS2_p13 = "images/home/salon/night/scenes/MLR2_NS2/13.jpg"
image MLR2_NS2_p14 = "images/home/salon/night/scenes/MLR2_NS2/14.jpg"
image MLR2_NS2_p15 = "images/home/salon/night/scenes/MLR2_NS2/15.jpg"
image MLR2_NS2_p16 = "images/home/salon/night/scenes/MLR2_NS2/16.jpg"
image MLR2_NS2_p17 = "images/home/salon/night/scenes/MLR2_NS2/17.jpg"
image MLR2_NS2_p17anim = Movie(play="videos/02 Linda-NS2-3.webm", loop = True )
image MLR2_NS2_p18 = "images/home/salon/night/scenes/MLR2_NS2/18.jpg"
image MLR2_NS2_p18anim = Movie(play="videos/02 Linda-NS2-4.webm", loop = True )
image MLR2_NS2_p19 = "images/home/salon/night/scenes/MLR2_NS2/19.jpg"
image MLR2_NS2_p20 = "images/home/salon/night/scenes/MLR2_NS2/20.jpg"
image MLR2_NS2_p21 = "images/home/salon/night/scenes/MLR2_NS2/21.jpg"
image MLR2_NS2_p22 = "images/home/salon/night/scenes/MLR2_NS2/22.jpg"
image MLR2_NS2_p23 = "images/home/salon/night/scenes/MLR2_NS2/23.jpg"
image MLR2_NS2_p24 = "images/home/salon/night/scenes/MLR2_NS2/24.jpg"
image MLR2_NS2_p24anim = Movie(play="videos/02 Linda-NS2-5.webm", loop = True )
image MLR2_NS2_p25 = "images/home/salon/night/scenes/MLR2_NS2/25.jpg"
image MLR2_NS2_p26 = "images/home/salon/night/scenes/MLR2_NS2/26.jpg"
image MLR2_NS2_p26anim = Movie(play="videos/02 Linda-NS2-6.webm", loop = True )
image MLR2_NS2_p26a = "images/home/salon/night/scenes/MLR2_NS2/26a.jpg"
image MLR2_NS2_p27 = "images/home/salon/night/scenes/MLR2_NS2/27.jpg"
image MLR2_NS2_p28 = "images/home/salon/night/scenes/MLR2_NS2/28.jpg"
image MLR2_NS2_p29 = "images/home/salon/night/scenes/MLR2_NS2/29.jpg"
image MLR2_NS2_p29anim = Movie(play="videos/02 Linda-NS2-7.webm", loop = True )
image MLR2_NS2_p30 = "images/home/salon/night/scenes/MLR2_NS2/30.jpg"
image MLR2_NS2_p30anim = Movie(play="videos/02 Linda-NS2-8r.webm", loop = True )
image MLR2_NS2_p30a = "images/home/salon/night/scenes/MLR2_NS2/30a.jpg"
image MLR2_NS2_p31 = "images/home/salon/night/scenes/MLR2_NS2/31.jpg"
image MLR2_NS2_p32 = "images/home/salon/night/scenes/MLR2_NS2/32.jpg"
image MLR2_NS2_p33 = "images/home/salon/night/scenes/MLR2_NS2/33.jpg"
image MLR2_NS2_p34 = "images/home/salon/night/scenes/MLR2_NS2/34.jpg"

default can_MLR2_MS1_ES3 = False

label MLR2_NS2_label:
    $ can_hide_windows = True
    scene MLR2_NS2_p1

    MC "(Gulp…)"
    if renpy.loadable("patch.rpy"):
        MC "(Well, there’s Dad. I wonder where Mom is, though.)"
    else:
        MC "(Well, there’s Bob. I wonder where Linda is, though.)"
    MC "(Jesus, my heart’s racing right now. If he wakes up and catches me - I’m sooo dead.)"

    scene MLR2_NS2_p2

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

    Mom "Hello, Sweetie!"
    MC "Ah-"
    Mom "Shush! Quiet! "

    scene MLR2_NS2_p3

    Mom "You have to be quiet, or we’ll wake up my husband."
    MC "O-Okay. You scared the shit out of me there, though!"
    MC "Could you not have just lied on the bed, waiting for me? "

    scene MLR2_NS2_p4

    Mom "I didn’t want to risk, falling asleep and missing your visit."
    if renpy.loadable("patch.rpy"):
        Mom "Besides - If I got into bed, your father would have wanted to have sex with me again."
    else:
        Mom "Besides - If I got into bed, Bob would have wanted to have sex with me again."
    Mom "I just wasted time, sorting out my clothes, until he drifted off to sleep."

    scene MLR2_NS2_p5

    MC "Ahh, I see. Just one thing - Maybe next time you could tap on my shoulder or whisper my name?"
    Mom "Aww, where’s the fun in that?"
    MC "(Sigh)"
    Mom "Now… about that promise I made…"

    scene MLR2_NS2_p6
    if renpy.loadable("patch.rpy"):
        Mom "I DID tell you that I would keep my boring husband off your back and make sure no harm ever came to you."
    else:
        Mom "I DID tell you that I would keep Bob off your back and make sure no harm ever came to you."
    Mom "HOWEVER - I want something in return."
    if renpy.loadable("patch.rpy"):
        MC "S-Sure, Mom. What are you thinking of?"
    else:

        MC "S-Sure, Linda. What are you thinking of?"

    scene MLR2_NS2_p8

    Mom "I want you to pleasure me, like the old man never could."
    Mom "You can do whatever you want - but focus on MY pleasure, not yours."
    Mom "Do you understand?"
    if renpy.loadable("patch.rpy"):
        MC "Yeah, no problem, Mom."
    else:
        MC "Yeah, no problem, Linda."
    Mom "Great! Let me just get undressed here."
    scene black
    $ renpy.pause(2, hard = True)
    scene MLR2_NS2_p9

    MC "(Wow! She’s so fucking hot!)"
    Mom "There we go."
    MC "Umm… are we sneaking into MY room now?"
    Mom "Why would we do that?"
    if renpy.loadable("patch.rpy"):
        MC "Because Dad is LITERALLY sleeping, right beside you."
    else:
        MC "Beceause Bob is LITERALLY sleeping, right beside you."
    Dad "(Snooooreeee)"
    Mom "But that’s HALF the fun, Sweetie!"

    scene MLR2_NS2_p10

    Mom "Now, how about you get over here and start playing with my tits, before I end up falling asleep too."
    if renpy.loadable("patch.rpy"):
        MC "(I guess Mom had a little bit of an exhibitionist streak in her!)"
        MC "Sure, Mom!"
    else:
        MC "(I guess Linda had a little bit of an exhibitionist streak in her!)"
        MC "Sure, Linda!"

    scene MLR2_NS2_p11

    MC "(Mwah!)"
    Mom "Oooohhh…."
    scene MLR2_NS2_p11anim
    MC "(Suck Suck)"
    Mom "Ahh…"

    scene MLR2_NS2_p12

    Mom "Mmm… harder… yes!"
    MC "(SUCK SUCK!)"
    scene MLR2_NS2_p12anim
    Mom "MMMM!!!"
    Dad "(Snooorrreeee)"

    scene MLR2_NS2_p13

    Mom "Eeek…."
    Mom "Ah… Ah… AH..."
    Mom "Don’t stop. Don’t stop..."
    Mom "Fuck, that’s good."

    scene MLR2_NS2_p11

    Mom "Phew... Okay… That’s enough."

    scene MLR2_NS2_p14

    Mom "Change of plans..."
    Mom "I need you down at my pussy, RIGHT NOW."

    scene MLR2_NS2_p15

    Mom "Mmm… here we go. Hurry up!"
    Mom "I’m so wet right now; I need to feel your tongue inside me!"
    if renpy.loadable("patch.rpy"):
        MC "Shush - careful you don’t wake Dad!"
    else:
        MC "Shush - careful you don’t wake Bob!"
    Mom "Mmm... Fuck him!"

    scene MLR2_NS2_p16

    Mom "God, I’m so hot right now. Please, start sucking on my clit. I need to feel, your hot wet mouth, clamped over it NOW!"
    MC "(Wow, she really can’t hold herself back!)"
    MC "Okay, hold still! Just try to keep your voice down."

    scene MLR2_NS2_p17

    MC "(Let’s begin by spreading her vulva.)"
    scene MLR2_NS2_p17anim
    MC "(There’s her clitoris at the top there. I can either focus on that, or plunge a finger inside and go for her g-spot.)"
    MC "(Let’s start with the g-spot.)"

    scene MLR2_NS2_p18

    Mom "Oooh….. Mmm!"
    scene MLR2_NS2_p18anim
    Mom "Yes… Yes, [player_name]. I love you!"
    MC "(Sounds like I made a good choice - She’s really enjoying this!)"
    Mom "Deeper!"

    scene MLR2_NS2_p19

    Mom "OOOHHHH!"
    MC "Shush! You’re gonna wake-"
    Mom "Stir up my slutty little pussy! Ahhh! AHHHH!"
    MC "(Damn, she’s so loud right now!)"

    scene MLR2_NS2_p20

    Mom "Oh yeah! Make me cum!"
    Dad "(Snore…)"
    if renpy.loadable("patch.rpy"):
        MC "(Thank God, Dad’s a deep sleeper!)"
    else:
        MC "(Thank God, Bob’s a deep sleeper!)"
    Dad "YAWN!"

    scene MLR2_NS2_p21

    MC "Oh shit..."
    Mom "(Fuck…)"
    Dad "(Snoooree…)"
    MC "Phew…"
    Mom "(I thought he was gonna wake up, there!)"

    scene MLR2_NS2_p22

    Mom "Did I not tell you to use your tongue?"
    MC "Yeah, but-"
    Mom "Get your face, pressed between my thighs, RIGHT NOW!"

    scene MLR2_NS2_p23

    Mom "Hurry! I’m so close to cumming!"
    if renpy.loadable("patch.rpy"):
        Mom "I need to feel my son’s tongue - writhing and flicking - deep inside my pussy!"
        MC "(Here we go… Let’s give Mom the best cunnilingus she’s ever had!)"
    else:
        Mom "I need to feel [player_name]'s tongue - writhing and flicking - deep inside my pussy!"
        MC "(Here we go… Let’s give Linda the best cunnilingus she’s ever had!)"

    scene MLR2_NS2_p24

    Mom "Ahh! Yes!"
    scene MLR2_NS2_p24anim
    MC "(Lick! Slurp!)"
    scene MLR2_NS2_p26anim
    Mom "Right there! Don’t stop! Ah!"

    scene MLR2_NS2_p25

    MC "(Suck! Lick! Shlurp!)"
    Mom "AHHH! Holy fuck! Ahhh! Mmmm!"
    Mom "Oh God! Oh God! Yes! Don’t stop!"

    scene MLR2_NS2_p26

    Mom "Deeper! Harder!"
    Dad "(Snoooore…)"
    MC "(She’s pulling my head in, right now!)"

    scene MLR2_NS2_p26a

    Mom "Oh! Oh! Oh!"
    MC "(Her breathing has become REALLY quick and rapid! It sounds like she’s on the verge of a climax!)"
    MC "(Lick! Lick! Lick!)"

    scene MLR2_NS2_p27

    Mom "Ohhhhh yeeeeessssss! C-Cuummmmmiiiinnng! Eeeeeekkk!"
    Mom "Ahhhhhhh! Oooohhhhh!"
    if renpy.loadable("patch.rpy"):
        Mom "(My son’s hot wet tongue is making me cum!)"
    else:
        Mom "([player_name]’s hot wet tongue is making me cum!)"
    Mom "Hnnnnnngggggg!!! Aaaahhhh!"

    scene MLR2_NS2_p28

    Mom "(Pant…)"
    Mom "(Gasp…)"
    Dad "(Snooorreeee…)"
    MC "(Lick!)"
    Mom "W-Wait… I’ve already- ahhh- cum!"
    MC "(Lick Lick Lick!)"

    scene MLR2_NS2_p29

    Mom "(Oh God! It’s soooo sensitive! Why isn’t he stopping?!)"
    scene MLR2_NS2_p29anim
    Mom "MMMMMM!!!!!"
    Mom "(It feels sooooo fucking good!)"

    scene MLR2_NS2_p30

    Mom "MMMM! MMMMMPPFFFFFF!!!"
    MC "(LICK LICK LICK!)"
    window hide
    scene MLR2_NS2_p30anim
    $ renpy.pause(7,hard = True)
    scene MLR2_NS2_p30a
    MC "(I think I made her cum, a second time!)"
    if renpy.loadable("patch.rpy"):
        MC "(Damn, she’s writhing and thrashing all over the bed! I’m surprised Dad hasn’t woken up!)"
    else:
        MC "(Damn, she’s writhing and thrashing all over the bed! I’m surprised Bob hasn’t woken up!)"

    scene MLR2_NS2_p31

    Mom "Holy shit… that was amazing."
    Mom "Where did you learn to do that?"
    MC "Honestly? This is the first time I’ve ever given cunnilingus to a girl."

    scene MLR2_NS2_p32

    Mom "Mmm... You’re a natural, then."
    MC "Heh! I guess so."
    Mom "That second one was the best orgasm I have ever had in my life."
    Mom "I love you."

    scene MLR2_NS2_p33

    Mom "Mmm…"
    MC "Mmm!"

    scene MLR2_NS2_p34

    MC "(Was I really THAT good at giving oral sex? I never realised!)"
    MC "(I’ll have to remember that, in future, for other girls.)"
    Mom "Mmm…"
    if renpy.loadable("patch.rpy"):
        MC "(I hope I get to fuck Mom, someday soon. I can’t wait for that.)"
    else:
        MC "(I hope I get to fuck Linda, someday soon. I can’t wait for that.)"
    $ can_MLR2_MS1_ES3 = True
    $ MLR2_NS2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump salon_morning1
