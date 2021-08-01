


label CR2_NS2_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR2_NS2_p1 with dissolve
    $ can_hide_windows = True
    MC "Hey, Caroline."
    if renpy.loadable("patch.rpy"):
        Caroline "Shush... Try to keep your voice down. We may be outside, but the rest of the family are sleeping."
    else:
        Caroline "Shush... Try to keep your voice down. We may be outside, but Linda and Bob and Sara are sleeping."
    MC "No problem. I’ll try to be quiet."

    scene black
    $ renpy.pause(3,hard = True)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    scene CR2_NS2_p2

    MC "What was it you wanted to talk about, Caroline?"
    Caroline "I wanted to have a serious conversation."
    Caroline "Come and sit with me on the bench."

    scene CR2_NS2_p3

    MC "(A serious conversation? I hope everything’s okay.)"
    MC "(I wonder if this has to do with her shop being robbed - She did seem very stressed after that whole event.)"
    MC "(Is there even anything else she would want to have a serious conversation about?)"

    scene CR2_NS2_p4

    Caroline "Don’t look so worried. Nothing seriously bad has happened."
    MC "Oh, thank God."
    MC "You had me scared there!"


    scene CR2_NS2_p5

    Caroline "Haha! I’m sorry, [player_name]. It’s a serious topic, but you don’t need to worry."
    Caroline "Grab a seat beside me here."

    scene CR2_NS2_p6

    Caroline "…"
    MC "(She’s being very quiet now. Perhaps, I should start the conversation?)"
    MC "So, what was it you wanted to talk about?"

    scene CR2_NS2_p7

    Caroline "…"
    MC "Caroline?"
    MC "(Shit, I’m feeling sick to my stomach. I think I know what it is now.)"
    MC "(She wants to end the deal we made!)"
    MC "Caroline? Is this about the deal we made?"
    Caroline "Yeah…"
    MC "(I knew it! It’s over…)"

    scene CR2_NS2_p8

    MC "(Gulp) Y-You want to end it, don’t you?"
    Caroline "What?! NO! No.. "

    scene CR2_NS2_p9

    Caroline "Of course, if you don’t want to.."
    MC "I don't want to!"
    MC "(Oh, thank God!)"
    MC "Phew... I was getting worried again, there."
    Caroline "Haha! Try to relax. I’m not here to end anything."

    scene CR2_NS2_p10

    Caroline "I actually wanted to talk to you about, everything you’ve done for me lately."
    MC "You don’t have to thank me for that."
    Caroline "No, I really do. I wouldn’t be where I am right now, if you hadn’t lent me that money."

    scene CR2_NS2_p11

    Caroline "Or helped me take those pictures."
    Caroline "Or supported me when my shop got robbed."
    MC "It’s nothing. Honestly."

    scene CR2_NS2_p12

    Caroline "Don’t keep saying it’s nothing, you idiot!"
    Caroline "You’re the only person in my life right now, who’s actually supported me!"
    if renpy.loadable("patch.rpy"):
        Caroline "Not Mom. Not Dad. Not even my friends. All the help I ever got, came from YOU, [player_name]. Do you understand that?"
    else:
        Caroline "Not Linda. Not Bob. Not even my friends. All the help I ever got, came from YOU, [player_name]. Do you understand that?"
    MC "I… I guess so."

    scene CR2_NS2_p13
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    Caroline "(Mwah!)"
    MC "Mmm!"
    MC "(Wow! That came out of nowhere!)"

    scene CR2_NS2_p14

    Caroline "(This is so wrong... It must be the romantic atmosphere of the night air and the full moon.)"
    if renpy.loadable("patch.rpy"):
        Caroline "(I can’t actually be feeling something for [player_name]. He’s my brother, for Christ’s sake!)"
    else:
        Caroline "(I can’t actually be feeling something for [player_name]. He’s my closest friend, for Christ’s sake!)"
    MC "Mmm..."

    scene CR2_NS2_p15

    Caroline "Don’t take me wrong, [player_name].. It’s only a reward for your help… Nothing more."
    MC "C-Caroline, I…"
    Caroline "Shush... Just… let me ask one thing."
    MC "A-Anything..."

    scene CR2_NS2_p16

    Caroline "This money you gave me, all the time you spend helping me out, the way you’re always there when I need you..."
    Caroline "Are you doing those things, for sexual favours as part of our deal?"
    Caroline "Or do you feel something more?"

    scene CR2_NS2_p17
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    window hide
    menu:
        "I… think I’m falling in love with you, Caroline.":
            scene CR2_NS2_p8

            MC "I… I think I’m falling in love with you, Caroline."
            Caroline "R-Really?"
            MC "Yeah, I think I am."

            scene CR2_NS2_p9

            Caroline "Thank you for telling me."
            Caroline "I... "
            if renpy.loadable("patch.rpy"):
                Caroline "I don’t feel the same way. I mean, I do love you - but just as a brother."
            else:
                Caroline "I don’t feel the same way. I mean, I do love you - but just as a friend."
            MC "Oh…"

            scene CR2_NS2_p8

            Caroline "Please don’t be sad!"
            MC "It’s okay. I still get to spend, almost every day with you. The deal we have is good enough for me right now."
            Caroline "Are you sure?"
            MC "If anything changes, we can talk about this again in the future, okay?"
            Caroline "Okay."
            jump CR2_NS2_continue1_rep

        "I’m doing them because your're my sister. Anything else is a bonus." if renpy.loadable("patch.rpy"):
            jump CR2_NS2_q1_rep

        "I’m doing them because your're my friend. Anything else is a bonus." if not renpy.loadable("patch.rpy"):
            jump CR2_NS2_q1_rep
        "I’m not gonna lie to you - I’ve been doing them as part of our deal.":
            scene CR2_NS2_p8

            MC "I’m not gonna lie to you - I’ve been doing them as part of our deal."
            MC "I help you out, and in exchange you help me get off."
            Caroline "Haha! WOW! I knew that guys were only interested in sex, but you’re the first one who’s actually been honest about it."

            scene CR2_NS2_p17

            MC "I’m sorry-"
            Caroline "No, don’t be sorry. I know exactly where I stand with you. That’s a good thing."
            MC "Are you sure?"
            Caroline "Absolutely, [player_name]."
            jump CR2_NS2_continue1_rep

label CR2_NS2_q1_rep:
    scene CR2_NS2_p17

    if renpy.loadable("patch.rpy"):
        MC "I’m doing these things because you’re my sister. Anything else is a bonus."
    else:
        MC "I’m doing these things because you’re my closest friend. Anything else is a bonus."
    MC "And that includes the deal."
    Caroline "Really?"
    MC "Really."
    if renpy.loadable("patch.rpy"):
        Caroline "I’m kinda relieved to hear that. Honestly, I only love you as a brother, and if things started to get romantic I’d be feeling a little weird."
    else:
        Caroline "I’m kinda relieved to hear that. Honestly, I only love you as a friend, and if things started to get romantic I’d be feeling a little weird."
    MC "Well, you don’t need to worry about that."
    jump CR2_NS2_continue1_rep

label CR2_NS2_continue1_rep:
    scene CR2_NS2_p18

    Caroline "C’mon. Follow me."
    MC "Where are we going?"
    Caroline "Back to my bedroom for some fun."

    scene CR2_NS2_p19
    if renpy.loadable("patch.rpy"):
        MC "But you said Mom and Dad were asleep!"
    else:
        MC "But you said Linda and Bob were asleep!"
    Caroline "Aww... are you a chicken?"
    MC "Hey! I’m not a chicken!"
    Caroline "Then, c’mon with me to my room."

    scene black

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.pause(3,hard=True)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)
    scene CR2_NS2_p20
    $ renpy.sound.play("sfx/door_squeak.mp3")

    "*Crreeeeaaaak*"

    "*Thud*"

    MC "Fuck ME, Caroline? You REALLY need to oil those hinges!"

    scene CR2_NS2_p21

    Caroline "I’ve never needed to before, since I’ve not snuck any boys into my bedroom."
    MC "Really?"
    Caroline "Why do you look so surprised?"

    scene CR2_NS2_p22

    MC "I figured you would have brought boys over before."
    if renpy.loadable("patch.rpy"):
        Caroline "With a nosy brother like you, and an even nosier sister like Sara? It wasn’t worth the risk!"
    else:
        Caroline "With a nosy person like you, and an even nosier person like Sara? It wasn’t worth the risk!"
    MC "Haha! I guess you’re right."
    Caroline "I just went over to their places to fuck."

    scene CR2_NS2_p23

    MC "So, what exactly are we doing tonight?"
    Caroline "Don’t get your hopes up - we won’t be having sex."
    Caroline "I haven’t quite decided how far I’m willing to go - but we’ll both find out soon enough."

    scene CR2_NS2_p24

    MC "(Her body looks so sexy! I wonder what I’ll get to do with her tonight.)"
    Caroline "Y’know, it’s probably a good thing that I don’t have a boyfriend right now."
    Caroline "It would make our deal a WHOLE lot more awkward."

    scene CR2_NS2_p25

    Caroline "And I don’t think I’d find a boyfriend who would treat me as well as you’ve done."
    Caroline "You helped grow my business - and then, when I got robbed - you saved it."
    MC "Caroline, you don’t need to keep thanking me for that. There’s more to you than just your business."

    scene CR2_NS2_p26

    Caroline "I know. I know. It’s my first real stab at independence though. I want to make it work."
    MC "Yeah, I get that."
    Caroline "Okay, I think I’m ready."

    scene CR2_NS2_p27

    Caroline "How about your rub your cock between my thighs, up against my panties?"
    MC "Sounds good to me!"
    Caroline "Cool. So, do you want to do it, back or front?"

    window hide
    menu:
        "Let’s do it with you facing back.":
            scene CR2_NS2_p27

            MC "Let’s do it with you facing back."
            Caroline "Mmm... Sounds good to me. Strip off and lie on your back, on the bed."

            scene CR2_NS2_back_p1

            Caroline "Well? How’s this? Are you comfortable?"
            MC "Yeah, this is good."
            Caroline "Great! I’ll start moving my hips now."
            scene CR2_NS2_back_p8anim
            MC "Ah..."

            scene CR2_NS2_back_p2

            MC "Mmm... Your mound is so warm!"
            Caroline "It feels good for you?"
            MC "Ah… so good."

            scene CR2_NS2_back_p3

            MC "Oohh…"
            Caroline "(I can feel his hard cock, rubbing up and down against my pussy, through my panties!)"
            Caroline "(This is more pleasurable for me, than I expected it to be!)"

            scene CR2_NS2_back_p4

            MC "Ah! Yes! That’s amazing, Caroline!"
            scene CR2_NS2_back_p4anim
            Caroline "Oh… Mmm…"
            Caroline "(I should try and keep my voice down. I don’t want him to think, I’m enjoying this too much…)"

            scene CR2_NS2_back_p5

            MC "(I’ll try thrusting MY hips as well!)"
            Caroline "MMM! Oh…"
            Caroline "(His cock is brushing against my clitoris!)"

            scene CR2_NS2_back_p6

            Caroline "(And now his hands are groping my ass!)"
            Caroline "(If he keeps this up, I’m probably going to cum!)"
            MC "(Her ass is so soft! I could squeeze it all day!)"

            scene CR2_NS2_back_p7

            Caroline "How- ahh- are you holding out there, [player_name]?"
            scene CR2_NS2_back_p9anim
            MC "MMM! Oh…"


            scene CR2_NS2_back_p8

            MC "I’m good, Caroline. Your ass feels amazing!"
            scene CR2_NS2_back_p8aanim
            MC "I’d love to fuck it, for real, someday."
            Caroline "Oohh… M-Maybe you will."

            scene CR2_NS2_back_p9

            Caroline "(I can’t believe I just said that!)"
            Caroline "(I’ll just put it down to, how damned horny I am right now.)"

            Caroline "Mmm..."

            scene CR2_NS2_back_p10

            MC "Ahh…"
            MC "Oohh…"
            Caroline "Ahh…"

            scene CR2_NS2_back_p11

            Caroline "(I’ll have to be careful though - I can’t let myself get this horny, EVERY TIME that [player_name] and I do stuff.)"
            Caroline "(If he keeps this up, I might not be able to resist, and end up letting him fuck me someday!)"
            jump CR2_NS2_continue2_rep
        "Let’s do it with you facing front.":

            scene CR2_NS2_p27

            MC "Let’s do it when you’re facing front."
            Caroline "Okay, take off your clothes and lie back on the bed."
            scene CR2_NS2_front_p1
            Caroline "Mmm…"

            MC "Wow…"
            Caroline "Enjoying the view?"
            MC "It’s incredible..."

            scene CR2_NS2_front_p2

            Caroline "How about when I close my thighs?"
            MC "Mmm!"
            Caroline "Does that feel good?"

            scene CR2_NS2_front_p3

            MC "So good!"
            scene CR2_NS2_front_p3anim
            Caroline "(I love the sensation of his cock, grinding against my panties.)"
            Caroline "(It’s brushing, perfectly against my clitoris!)"


            scene CR2_NS2_front_p4

            MC "Oohh…"
            Caroline "Ahh… Ah…"
            MC "It sounds like you’re enjoying this too, Caroline?"

            scene CR2_NS2_front_p5

            Caroline "I’m… ah… just breathing…"
            MC "Sure - if that’s what you call it, Caroline."

            scene CR2_NS2_front_p6

            Caroline "(Oh God, his cock feels so good! It’s making me so horny right now!)"
            Caroline "(This is dangerous… If I got REALLY HORNY someday, I might let him inside me…)"
            Caroline "(Damn, that would be so wrong…)"

            scene CR2_NS2_front_p7

            Caroline "Oohhh…"
            Caroline "(This is so wrong, but it feels SOOO good!)"
            MC "(She’s getting faster with each passing minute!)"

            scene CR2_NS2_front_p8

            MC "Ugh! I’m gonna cum soon, Caroline!"
            MC "Your thighs are fucking incredible!"
            scene CR2_NS2_front_p7anim
            Caroline "Ah! Ah! Ahh..."

            scene CR2_NS2_front_p9

            Caroline "(He’s going to be cumming, soooo close to my pussy!)"
            Caroline "(Holy shit… my heart is racing right now!)"
            Caroline "Ahh… Ohhh…"

            scene CR2_NS2_front_p10

            MC "(I’ll get a much better orgasm if I take control of the situation.)"
            MC "(I hope Caroline doesn’t mind if I pull myself on top, to change things up!)"
            Caroline "Mmm! Ohh!"

            scene CR2_NS2_front_p11

            MC "Ahh…"
            MC "(Well, here goes nothing!)"
            jump CR2_NS2_continue2_rep

label CR2_NS2_continue2_rep:
    scene black with dissolve
    $ renpy.pause(0.7,hard= True)
    scene CR2_NS2_p28 with dissolve

    Caroline "Whoa!"
    MC "You gotta stay quiet, Caroline. Remember?"
    if renpy.loadable("patch.rpy"):
        MC "Don’t want to wake Mom and Dad up!"
    else:
        MC "Don’t want to wake Linda and Bob up!"

    scene CR2_NS2_p29

    Caroline "Mmmm…. Ohh…"
    MC "(This is much better!)"
    MC "(And by the look on Caroline’s face, she’s LOVING the feeling of it too!)"

    scene CR2_NS2_p30

    Caroline "Ah! Ah! Ah!"
    scene CR2_NS2_p30anim
    Caroline "(God! He’s gonna make me cum!)"
    MC "Fuck, this is good!"

    scene CR2_NS2_p31
    Caroline "Ooohhh!"
    Caroline "(I can feel my pussy burning up! I’m gonna cum soon!)"
    MC "I’m not gonna last much longer! Ugh!"

    scene CR2_NS2_p32

    Caroline "Thrust faster! Ah! "
    MC "Are you - ugh - sure?"
    scene CR2_NS2_p32anim
    Caroline "Ah! Yes! Yes!"

    scene CR2_NS2_p33

    Caroline "Mmm! Fuck… It’s so good…"
    Caroline "Ahh!"
    MC "Hnnng! I’m gonna cum!"

    scene CR2_NS2_p34

    Caroline "W-Wait! Oh God!"
    Caroline "Careful! You’ll get it on my-"
    MC "HNNNG!!! AAHHH!"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR2_NS2_p34 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR2_NS2_p35 with dissolve

    Caroline "...face."
    MC "Oh shit! Sorry, Caroline."
    Caroline "Don’t worry about it..."

    scene CR2_NS2_p36

    Caroline "Go on back to your room. I need to clean up, here."
    MC "Are you sure?"
    Caroline "Yeah. I’ll see you tomorrow."

    scene CR2_NS2_p37

    Caroline "(Damn… the scent of his cum, there is making me VERY horny!)"
    Caroline "(It doesn't help that he came before I did, either.)"
    Caroline "(Time to get my special toy out…)"

    scene CR2_NS2_p38

    Caroline "Hmm… Where did I leave it, after last time?"
    Caroline "I could have sworn I had it under my pillow…"
    Caroline "Unless…"

    scene CR2_NS2_p39
    if renpy.loadable("patch.rpy"):
        Caroline "(I had to hide it under my bed, in case Mom decided to clean my room.)"
    else:
        Caroline "(I had to hide it under my bed, in case Linda decided to clean my room.)"
    Caroline "(It would have been embarrassing if she’d found it.)"
    Caroline "(Oh, come on… Where have you gone?)"

    scene CR2_NS2_p40


    Caroline "Aha! There you are!"
    Caroline "(How on Earth did you get THAT far under the bed?)"
    Caroline "(It must have rolled, after I threw it under, last time.)"
    Caroline "(I just need to wash it quickly, then it’ll be ready to use.)"

    scene CR2_NS2_p41

    Caroline "(Okay, that’s it washed… Now, time to have some fun.)"
    Caroline "(It’s been faaaar too long since I’ve had, a good long session with you.)"
    Caroline "(I think I’ll put you in my pussy tonight.)"

    scene CR2_NS2_p42

    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Oooh…"
    Caroline "Yes... Right there…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Mmm! That’s it…"

    scene CR2_NS2_p43

    Caroline "Yes… Take off your pants and thrust your cock inside me…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Mmm… That’s sooooo goood! Ahhh!"
    Caroline "OH! OHHH, [player_name]! Fuck me harder!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")

    scene CR2_NS2_p44

    Caroline "W-what!? Eh!? What did I JUST SAY!?"
    Caroline "(Am I seriously getting off, to the thought of [player_name] fucking me?)"
    Caroline "(That’s sick and wrong… isn’t it?)"
    Caroline "(What’s wrong with me!?)"


    scene CR2_NS2_p45

    Caroline "(Dammit! This stupid deal is affecting me!)"
    Caroline "(I CAN’T like [player_name] THAT way! This was only supposed to be fun!)"
    Caroline "(This is… weird… and wrong!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label