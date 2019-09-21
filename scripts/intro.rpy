image intro1 = "/images/intro/1.jpg"
image intro2 = "/images/intro/2.jpg"
image intro3 = "/images/intro/3.jpg"
image intro4 = "/images/intro/4.jpg"
image intro5 = "/images/intro/5.jpg"
image intro6 = "/images/intro/6.jpg"
image intro7 = "/images/intro/7.jpg"
image intro8 = "/images/intro/8.jpg"
image intro9 = "/images/intro/9.jpg"
image intro10 = "/images/intro/10.jpg"
image intro11 = "/images/intro/11.jpg"
image intro12 = "/images/intro/12.jpg"
image intro13 = "/images/intro/13.jpg"
image intro14 = "/images/intro/14.jpg"
image intro15 = "/images/intro/15.jpg"
image intro16 = "/images/intro/16.jpg"
image intro17 = "/images/intro/17.jpg"
image intro18 = "/images/intro/18.jpg"
image intro19 = "/images/intro/19.jpg"
image intro20 = "/images/intro/20.jpg"
image intro21 = "/images/intro/21.jpg"
image intro22 = "/images/intro/22.jpg"
image intro23 = "/images/intro/23.jpg"
image intro24 = "/images/intro/24.jpg"
image intro25 = "/images/intro/25.jpg"
image intro26a = "/images/intro/26a.jpg"
image intro26b = "/images/intro/26b.jpg"
image intro27 = "/images/intro/27.jpg"
image intro28 = "/images/intro/28.jpg"
image intro29 = "/images/intro/29.jpg"
image intro30 = "/images/intro/30.jpg"
image intro31 = "/images/intro/31.jpg"
image intro32 = "/images/intro/32.jpg"
image intro33 = "/images/intro/33.jpg"
image intro34 = "/images/intro/34.jpg"
image intro35 = "/images/intro/35.jpg"
image intro36 = "/images/intro/36.jpg"
image intro37 = "/images/intro/37.jpg"
image intro38 = "/images/intro/38.jpg"
image intro39 = "/images/intro/39.jpg"
image intro40 = "/images/intro/40.jpg"
image intro41 = "/images/intro/41.jpg"
image intro42 = "/images/intro/42.jpg"
image intro43 = "/images/intro/43.jpg"
image intro44 = "/images/intro/44.jpg"
image intro45 = "/images/intro/45.jpg"
image intro46 = "/images/intro/46.jpg"
image intro47 = "/images/intro/47.jpg"
image intro48 = "/images/intro/48.jpg"
image intro49 = "/images/intro/49.jpg"
image intro50 = "/images/intro/50.jpg"
image intro51 = "/images/intro/51.jpg"
image intro52 = "/images/intro/52.jpg"
image intro53 = "/images/intro/53.jpg"
image intro54 = "/images/intro/54.jpg"
image before_intro1 = "/images/intro/before/1.jpg"
image before_intro2 = "/images/intro/before/2.jpg"
image before_intro3a = "/images/intro/before/3a.jpg"
image before_intro3b = "/images/intro/before/3b.jpg"
image before_intro4 = "/images/intro/before/4.jpg"
define flash = Fade(.25, 0.0, .75, color="#fff")

default Students_name = "Students"
default Mom_name = "Mom"

define Judy = Character("[Judy_name]", color="#993333")
define MC = Character("[player_name]", color="#3366FF")
define Sara = Character("[Sara_name]", color="#00FFCC")
define Mom = Character("[Mom_name]", color="#CC00CC")
define Linda = Character("[Mom_name]", color="#CC00CC")
define Celia = Character("[Celia_name]", color="#FF6EC7")
define Students = Character("[Students_name]")
define Caroline = Character("[Caroline_name]", color="#66CC33")

image intro_movie = Movie(play="/images/intro/before/intro_movie.webm", loop = True,)
transform slightleft:
    xalign 0.96
    yalign 0.4

label intro:
    $ can_hide_windows = True
    scene before_intro1 with dissolve
    "Hey there! W-wait! Don’t skip ME!"
    "Before we get to the prologue, give me a chance to quickly tell you a few things!"
    scene before_intro4
    "Firstly, and most importantly… this game is still in progress!"
    scene before_intro2
    "Damn... Like almost every other game, right?"
    "Fuck… That was a bad start."

    scene before_intro4
    "But - don’t worry! There should be MORE than enough content already, to make you *ahem* have some fun!"
    scene before_intro3a
    "The second important piece of information is that this game is fully interactive! Maps, Inventory, Items, Minigames, loads of characters!"
    "YOU decide what story you want to push forward! If you don’t like someone, you can even completely ignore her!"

    scene before_intro4
    "The third and final piece of information is that the game has animated sex scenes!!"
    "Yep! That’s it! A-N-I-M-A-T-E-D!! You heard me well!"


    scene before_intro3b
    "Just check out THIS shit!"
    show intro_movie at slightleft
    window hide
    $ renpy.pause()
    scene before_intro1
    "Okay, I think that’s enough! Have FUN!"
    $ renpy.music.stop(channel="music", fadeout=2)
    scene black
    show intro21 with flash
    hide intro21
    show intro28 with flash
    hide intro28
    show intro46 with flash
    scene black
    $ Judy_name="???"
    $ player_name="???"
    Judy "Are you alright?"
    Judy "Hey, you need to wake up."
    $ renpy.music.play('/sfx/RetroFuture_Clean.mp3',channel="music1", loop=True, fadein=2)
    scene intro1 with dissolve
    MC "Huh?! Where am I?!"
    Judy "It’s me, Judy - the school therapist."
    $ Judy_name="Judy"
    Judy "I asked you to close your eyes and try to recall the events of yesterday, but you fell asleep."
    MC "Oh, oh yeah. Sorry, I haven’t been sleeping well lately."
    Judy "Hmm... try sitting back in your chair and relaxing. Make yourself comfortable."

    scene intro2
    MC "Okay, no problem."
    Judy "Actually, before we begin, I need to check if I have your details correct."
    Judy "You’re in class 7C, is that right?"
    MC "Yeah, 7C."
    Judy "Good, and is your name spelt correctly here?"
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="MC"
    if not renpy.loadable("patch.rpy"):
        Judy "And the person living with, is… Linda?"
    if renpy.loadable("patch.rpy"):
        Judy "And your mother is… Linda?"
    MC "Yes, that’s her."

    scene intro7
    Judy "Okay, everything seems to be in order."
    Judy "I’m gonna take a couple of minutes to go over everything again."
    Judy "My name’s Judy Hannigan. I’m the school’s therapist."
    Judy "What happened yesterday was-"

    scene intro3
    MC "Relax! Everything is fine! Really - I promise."
    Judy "[player_name], what happened was very serious. You can’t just-"
    MC "Everything’s cool - I can handle myself."
    Judy "I’m not satisfied that everything is “fine”. This counselling service is for your own well-being."
    MC "I- I don’t want to think about yesterday ever again. I’m going to leave now and pretend like it never happened."
    MC "Haha! Honestly, it’s a joke that I’m even here at all. This has been blown WAY out of proportion."

    scene intro4
    Judy "But it DID happen, [player_name]. The fact that you simply choose not to address it, isn’t healthy."
    Judy "Avoidant behaviours are common in people recovering from trauma."
    Judy "Besides - if you leave this room right now, I will have no choice but to sign this letter of expulsion."

    scene intro5
    Judy "I see you’ve stopped walking towards the door. Were you unaware that I report directly to the headmaster?"
    Judy "He asked me to monitor your progress and behaviour, [player_name]."
    Judy "I know you don’t feel like it right now - but I promise, this is for your own good."
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene intro6
    Judy "What happened to you was embarrassing. Tremendously so. I can’t even begin to imagine how you must feel right now."
    Judy "But running away from this won’t fix anything. Please, help me to help you. Take a seat. Let’s talk things through."
    Judy "You can trust me."
    MC "(Sigh)"
    if renpy.loadable("patch.rpy"):
        MC "Fine... Don’t send that letter to the headmaster though - my mom will kill me."
    if not renpy.loadable("patch.rpy"):
        MC "Fine... Don’t send that letter to the headmaster though - Linda will kill me."
    Judy "(I know she would. Linda would be raging if you will be kicked out of school.)"
    Judy "I’m glad you changed your mind. Take a seat. Let’s start at the beginning."
    scene intro7
    $ a1 = True
    $ a2 = True
label q1_intro:
    Judy "Before we begin, is there anything you’d like to ask me?"
    menu:
        "Could you tell me a little more about yourself?" if a1 == True:
            $ a1 = False
            jump q1_a1_intro

        "How long will this therapy take?" if a2 == True:
            $ a2 = False
            jump q1_a2_intro
        "No further questions.":
            jump after_q1_intro

label q1_a1_intro:
    Judy "Of course, [player_name]. It’s best when patients feel comfortable with their therapist."
    Judy "My full name is Judy Hannigan. I’m a qualified therapist. I graduated from the University of Wisconsin four years ago. I’ve been working in this school ever since."
    jump q1_intro
label q1_a2_intro:
    Judy "As long as is required. You can’t rush these things, [player_name]."
    Judy "Some people can be out of therapy in three or four sessions. Other people take… much longer. What matters is that you are making progress. Don’t view your treatment as a race - think of it as a journey."
    MC "Huh… I guess so. I don’t like the idea of it going on for a long time though."
    Judy "We’ll cross that bridge when we come to it."
    jump q1_intro
label after_q1_intro:
    Judy "Now tell me, [player_name], what happened yesterday?"
    $ renpy.music.stop(channel="music2", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro8 with dissolve
    $ renpy.music.play('/sfx/Vivacity.mp3', channel="music1", loop=True, fadein = 2)
    $ Sara_name="???"
    Sara "Hey, [player_name]! Wake up! You’re gonna be late for school!"
    MC "(Yawn) Five more minutes, Sara…"
    $ Sara_name="Sara"
    Sara "You’re gonna be laaaate!"

    scene intro9
    MC "(Sigh) Fine! I’m awake…"
    Sara "So, are you actually gonna do it?"
    MC "Hmm?"
    Sara "Are you really gonna ask Mrs. Celia out today?"
    MC "Yeah, of course I am."

    scene intro10
    Sara "I don’t think it’s such a good idea, [player_name]. She’s gonna reject you, for sure."
    MC "Just relax - everything will be fine, and I’ll finally get laid!"
    Sara "Is getting laid the only thing you ever think about?!"
    Sara "Besides, what makes you think she’s even interested in you!"

    scene intro11
    MC "We’re on a first name basis. She let’s me call her Celia."
    Sara "So? I call some of my teachers by their first names."
    MC "It’s not just that! She’s ALWAYS looking at me and smiling."
    Sara "Maybe she’s just a happy person?"
    MC "Plus, she touched my ass when I was walking in the corridor!"

    scene intro12
    Sara "Are you sure her hand didn’t just slip?"
    MC "What?! No, she definitely touched me, on purpose!"
    MC "(At least… I think so…)"
    Sara "Hey! What are you doing?! I’m still here!"

    scene intro13
    MC "Huh?"
    Sara "You’re getting changed! At least give me a warning, so I don’t have to see your icky ass!"
    MC "Oh please - you’ve got one too. If it really bothers you then get out of my room!"
    Sara "It’s just not-"

    scene intro14
    Sara "Eeek! [player_name]! Put some clothes on!"
    MC "I DID tell you to get out of my room!"
    Sara "Eww! Fine! But please listen to my advice - DON’T ask out Mrs. Celia! This will end badly."
    MC "Relax, Sara. What’s the worst that could happen?"
    $ renpy.music.stop(channel="music1", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro15 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Judy "Hmm… Interesting… Do you mind if I ask you a few questions about Sara?"
    MC "I guess so."
    $ a1 = True
    $ a2 = True
    $ a3 = True
label q2_intro:
    Judy "What’s Sara like?"
    menu:
        "Tell her about Sara’s hobbies." if a1 == True:
            MC "Sara’s a huge nerd. She spends her free time playing videogames, going to comic-cons, and watching geeky British TV shows."
            Judy "Do you enjoy these things yourself?"
            MC "I mean, videogames are fun - but I don’t really get the appeal of comic-cons or the shows she watches."
            $ a1 = False
            if a2 == False and a3 == False:
                jump after_q2_intro
            else:
                jump q2_intro
        "Tell her about Sara’s school life." if a2 ==True:
            MC "She’s top of her class in Maths, Biology and Chemistry. I think she actually wants to become a Computer Scientist someday."
            if renpy.loadable("patch.rpy"):
                Judy "She sounds very intelligent. You must be very proud to have her as a sister."
            if not renpy.loadable("patch.rpy"):
                Judy "She sounds very intelligent. You must be very proud to have her."
            MC "I guess so. I’ve never really thought about it. "
            $ a2 = False
            if a1 == False and a3 == False:
                jump after_q2_intro
            else:
                jump q2_intro
        "Tell her about Sara’s social life." if a3 == True:
            MC "Sara keeps to herself, mostly. She’s got a couple of close friends, but I think she enjoys, hanging out with small groups of people, to large crowds."
            Judy "Hmm... In my profession, we would call that ‘introverted’. Basically, she finds time in smaller groups more rewarding."
            Judy "Consequently, large social situations can be particularly tiresome for introverts."
            $ a3 = False
            if a1 == False and a2 == False:
                jump after_q2_intro
            else:
                jump q2_intro
label after_q2_intro:

    scene intro17
    Judy "Thank you for answering my question. My next one might… be a little awkward, but we are going to have to delve into some Freudian psychoanalysis techniques."
    MC "Psycho-what?"
    if renpy.loadable("patch.rpy"):
        Judy "Freudian Psychoanalysis. Tell me, [player_name], do you find your sister, Sara, sexually attractive?"
    if not renpy.loadable("patch.rpy"):
        Judy "Freudian Psychoanalysis. Tell me, [player_name], do you find Sara, sexually attractive?"
    scene intro16
    MC "Wh-What?!"
    if renpy.loadable("patch.rpy"):
        Judy "Do you think your sister is sexy?"
    if not renpy.loadable("patch.rpy"):
        Judy "Do you think Sara is sexy?"
    MC "I- How- This isn’t an appropriate question!"

    scene intro17
    Judy "I assure you, it absolutely is. Freudian Psychology delves into the nature of human sexuality. "
    Judy "Given the nature of this incident, which brought you to me, a sexualisised element of psychology is most definitely relevant."
    if renpy.loadable("patch.rpy"):
        MC "But… She’s my sister…"
    if not renpy.loadable("patch.rpy"):
        MC "But… She’s my very close friend…"
    Judy "How often do you fantasise about having sex with Sara?"

    scene intro16
    MC "(Honestly? I’ve thought about fucking her, more than once. I remember bumping into her as she got out of the shower, last year. Her towel fell off, and I saw her cute tits.)"
    MC "(I must have wanked to that mental image for a solid week!)"
    MC "These questions are really weird. I’m not… I’m not comfortable talking about these."

    scene intro18
    Judy "Understandable. You are still in the early stages of your treatment. It may take you some time to fully open up. "
    Judy "It is essential that you are honest with me, if you want to completely heal."
    if renpy.loadable("patch.rpy"):
        MC "(Sigh) Fine. I guess I’ve… maybe… fantasised about my sisters, a couple of times."
    if not renpy.loadable("patch.rpy"):
        MC "(Sigh) Fine. I guess I’ve… maybe… fantasised about Sara, a couple of times."
    Judy "Interesting..."
    Judy "We can return to this subject-matter another time. For now, please tell me what happened next, on the day of the incident."
    MC "Let me think… I was just about to leave for school."

    $ renpy.music.stop(channel="music2", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro19 with dissolve
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    MC "(Crap! Sara was right! I’m gonna be late if I don’t hurry!)"
    MC "(I think she’s already started walking, ten minutes ago. I shouldn’t have spent so long in the shower!)"

    scene intro20
    if renpy.loadable("patch.rpy"):
        $ Mom_name = __("Mom")
    if not renpy.loadable("patch.rpy"):
        $ Mom_name = "Linda"
    Mom "Where are you rushing off to?"
    MC "I’m gonna be late for school!"
    Mom "Have you not forgotten to say good morning to someone?"
    if renpy.loadable("patch.rpy"):
        MC "Morning, Mom! I’ll see you late-"
    if not renpy.loadable("patch.rpy"):
        MC "Morning, Linda! I’ll see you late-"
    scene intro21
    Mom "Oh, come on. You’ve got time to greet me properly."
    Mom "You’ll stress yourself out if you keep rushing around."
    MC "I really AM in a hurry."
    Mom "Why? Something special happening today?"
    MC "Uhh… N-No!"

    scene intro22
    Mom "Then come over and give me a kiss, at the very least."
    MC "Fine, no problem."
    Mom "On the lips."
    if renpy.loadable("patch.rpy"):
        MC "Seriously, Mom? NOBODY my age kisses their mom on the lips anymore! If anyone found out, they would laugh me out of the school!"
    else:
        MC "Seriously, Linda NOBODY my age kisses a lot older woman on the lips! If anyone found out, they would laugh me out of the school!?"
    Mom "You’d better make sure nobody finds out, then."

label choice1_intro:
    $ kiss_mom_cheek=False
    $ kiss_mom_lips=False
    menu:
        "Kiss Mom on the cheek." if renpy.loadable("patch.rpy"):

            $ kiss_mom_cheek=True
            scene intro23
            MC "*Mwah*"
            MC "Sorry, Mom - I’m too old for that now. I’ll see you later, when I get home from school."

            scene intro26b
            Mom "Hmmpf!"
            Mom "(Why won’t he kiss me?! It’s not like any of his classmates are around to see him do it…)"
            jump after_choice1_intro
        "Kiss Mom on the lips." if renpy.loadable("patch.rpy"):

            $ kiss_mom_lips=True
            scene intro24
            MC "Haha! Okay, Mom. If it’ll make you happy."
            Mom "It will...."

            scene intro25
            Mom "(Whispered) It really will..."
            MC "(Huh? Mom’s acting a little strange today. I wonder if she’s feeling alright.)"

            scene intro26a
            MC "(Mwah)"
            Mom "Mmm…"
            Mom "(God… I wish I could just pin him down to the bed and make out with him.)"
            jump after_choice1_intro
        "Kiss Linda on the cheek." if not renpy.loadable("patch.rpy"):

            $ kiss_mom_cheek=True
            scene intro23
            MC "*Mwah*"
            MC "Sorry, Linda - I’m too old for that now. I’ll see you later, when I get home from school."

            scene intro26b
            Mom "Hmmpf!"
            Mom "(Why won’t he kiss me?! It’s not like any of his classmates are around to see him do it…)"
            jump after_choice1_intro
        "Kiss Linda on the lips." if not renpy.loadable("patch.rpy"):

            $ kiss_mom_lips=True
            scene intro24
            MC "Haha! Okay, Linda. If it’ll make you happy."
            Mom "It will...."

            scene intro25
            Mom "(Whispered) It really will..."
            MC "(Huh? Linda’s acting a little strange today. I wonder if she’s feeling alright.)"

            scene intro26a
            MC "(Mwah)"
            Mom "Mmm…"
            Mom "(God… I wish I could just pin him down to the bed and make out with him.)"
            jump after_choice1_intro

label after_choice1_intro:

    scene intro22
    if renpy.loadable("patch.rpy"):
        MC "I’ll see you later, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "I’ll see you later, Linda."
    Mom "See you tonight, Sweetpea!"
    Mom "(Ooh… I’m starting to get wet, just thinking about making out with him.)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro27 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    if renpy.loadable("patch.rpy"):
        Judy "Your mother sounds like a very interesting person. She clearly cares about you, an awful lot."
    if not renpy.loadable("patch.rpy"):
        Judy "Linda sounds like a very interesting person. She clearly cares about you, an awful lot."
    MC "Yeah, I guess she does."
    Judy "We’ll come back to talk about HER later. For now though, please tell me about the incident."
    MC "(Gulp)"
    Judy "I know this is difficult. Please take your time. If you need to take a break, just let me know."

    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro28 with dissolve
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)
    MC "Mrs. Celia?"
    Celia "Please - I told you to call me Celia. How can I help you, [player_name]?"
    MC "Mrs. Celi- Celia, I was wondering if you would like to go… to Beniza’s Pizza with me, and… (gulp) c-catch a movie afterwards?"
    Celia "Are you asking me out on a date, [player_name]?"

    scene intro29
    MC "Y-Yes."
    Celia "…"
    MC "Well?"
    Celia "…"
    Celia "Hahahahaha! You are seriously asking out a teacher, on a date?!"
    MC "I- Um- Ah…"

    scene intro30
    Celia "Oh, my God! This is too funny!"
    MC "I thought… Oh...."
    Celia "Hehehehe!"

    show intro31 with hpunch
    if renpy.loadable("patch.rpy"):
        $ Students_name = __("Students")
    if not renpy.loadable("patch.rpy"):
        $ Students_name = __("Students")
    Students "Did he just ask her out?!"
    Students "Oh, my God! He did!"
    Students "I’d be mortified if that happened to me!"
    Students "Ahahaha!"
    Students "What a LOSER! HAHAHA!"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro32 with dissolve
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)
    MC "I was SO... fucking angry."
    Judy "I can see that. You’re displaying extremely aggressive body language - Your clenched fists, your hunched posture."
    Judy "You still are angry, aren’t you?"
    MC "Of course I fucking am! She embarrassed me, in-front of the whole school!"

    scene intro33
    Judy "I think it’s a good thing that you came to therapy, as soon as you did. It means that you can really focus on healing."
    Judy "Tell me, [player_name], do you have strong feelings, to exact revenge upon Mrs. Celia?"

    scene intro32
    MC "…"
    Judy "You can tell me the truth. Please be honest."
    MC "Yeah… I hate her right now."

    scene intro33
    Judy "Thank you for being honest. Let’s talk more about Mrs. Celia later. For now, could you tell me what happened after?"
    if renpy.loadable("patch.rpy"):
        MC "Let me think… I… I went and stole my sister’s whiskey from her room."
    if not renpy.loadable("patch.rpy"):
        MC "Let me think… I… I went and stole my friend’s whiskey from her room."
    Judy "Sara has whiskey in her bedroom? (This sounds like something I should report to the headmaster.)"
    if renpy.loadable("patch.rpy"):
        MC "No, this was my older sister, Caroline."
    if not renpy.loadable("patch.rpy"):
        MC "No, this was my older friend, Caroline."
    Judy "(Oh, thank God)"
    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro34 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    Caroline "Hmm? Oh hey, [player_name]! Don’t you know it’s polite to knock first?"
    MC "…"

    scene intro35
    Caroline "Uh… is something wrong, [player_name]?"
    MC "..."
    Caroline "(What’s up with him? He’s not usually the quiet type.)"

    scene intro36
    Caroline "If you’re looking for your phone charger, I already returned it. It’s beside your bed."
    MC "I… I need your whiskey."
    Caroline "Huh? Why?"
    MC "I… I need a drink."
    Caroline "Is everything alright? Do you need some cash to buy your own?"
    MC "I can’t be bothered leaving the house…"

    scene intro37
    Caroline "I’m getting a little worried about you..."
    MC "Yeah, whatever…"
    Caroline "(What’s up with him? I’ve never seen him acting this weird before.)"
    Caroline "(Could he be suffering from depression, or something?)"

    scene intro38
    Caroline "Anyway, I’ve got to finish three more chapters of this book by tomorrow morning."
    Caroline "Go ahead and take the bottle - you owe me a favour for that though."
    MC "Sure…"
    Caroline "(I wonder if something happened in school today. I should talk to Sara, when I get a chance.)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro7 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Judy "What happened after you took the whiskey, [player_name]?"

    scene intro27
    MC "I drank a lot of it… The next couple of hours were a bit of a blur. I remember lying on my bed, just wishing that… that…"
    Judy "That the world would swallow you whole?"
    MC "Yeah…"
    Judy "A lot of patients have said similar things."
    Judy "Tell me - what happened to bring you out of this slump?"
    if renpy.loadable("patch.rpy"):
        MC "My mom. She came into my room, that evening - I hadn’t shown up for family dinner."
    if not renpy.loadable("patch.rpy"):
        MC "Linda. She came into my room, that evening - I hadn’t shown up for dinner."

    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro39 with dissolve
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    MC "(Oh God… what have I done? I can’t ever show my face in school again.)"
    MC "(Mrs. Celia thinks I’m a joke. My classmates think I’m a loser.)"
    MC "(My life is ruined…)"

    scene intro40
    "(Knock Knock)"
    Mom "Hey there, Sweetpea. What’s wrong? You’re looking glum."
    if renpy.loadable("patch.rpy"):
        MC "It’s nothing, Mom. I’m fine."
    if not renpy.loadable("patch.rpy"):
        MC "It’s nothing, Linda. I’m fine."
    Mom "You don’t look fine. And it stinks of alcohol in here. Have you been drinking?"
    MC "Just a bit…"
    Mom "(Sigh)"

    scene intro41
    Mom "Caroline told me, everything that happened in school today. She was worried about you and went to speak to Sara. "
    if renpy.loadable("patch.rpy"):
        Mom "It seems, everybody in this family knows what happened, before me. I was hoping you’d open-up to me."
    if not renpy.loadable("patch.rpy"):
        Mom "It seems, everybody here knows what happened, before me. I was hoping you’d open-up to me."
    if renpy.loadable("patch.rpy"):
        MC "Mom?"
    if not renpy.loadable("patch.rpy"):
        MC "Linda?"
    Mom "Yes, Sweetpea?"
    MC "Am… Am I ugly?"

    scene intro42
    Mom "What?! Who told you that?"
    MC "Nobody... But I feel like I am."
    Mom "You’re a very handsome young man."
    if renpy.loadable("patch.rpy"):
        MC "(Sigh) You have to say that - You’re my mom."
    if not renpy.loadable("patch.rpy"):
        MC "(Sigh) You have to say that."
    Mom "Look at me, [player_name]."

    scene intro43
    if renpy.loadable("patch.rpy"):
        Mom "You’re not ugly. And I’m not saying that, just because I’m your mom. If anything, it means - even more - when it comes from me. I think you are incredibly handsome."
        MC "...thanks, Mom. I still don’t believe it’s true though."
    if not renpy.loadable("patch.rpy"):
        Mom "You’re not ugly. I think you are incredibly handsome."
        MC "...thanks, Linda. I still don’t believe it’s true though."
    scene intro44
    MC "Mmpff!"
    if renpy.loadable("patch.rpy"):
        MC "(What the heck, Mom?!)"
    if not renpy.loadable("patch.rpy"):
        MC "(What the heck, Linda?!)"
    Mom "Mmm!"

    scene intro45
    Mom "(Holy shit! I can’t believe I just did that!)"
    Mom "(I completely lost control, and let my lust take over!)"
    if renpy.loadable("patch.rpy"):
        MC "(What’s Mom doing?!)"
    if not renpy.loadable("patch.rpy"):
        MC "(What’s Linda doing?!)"
    scene intro46
    MC "Wh-What was THAT for?!"
    if renpy.loadable("patch.rpy"):
        MC "M-Mom! You just kissed me!?"
    if not renpy.loadable("patch.rpy"):
        MC "L-Linda! You just kissed me!?"
    if kiss_mom_cheek == True:
        Mom "Well, you owed me a proper kiss, since you only pecked me on the cheek this morning."
        MC "..."
        Mom "…"

        jump after_conditional_mom_kiss_cheek_lips_intro
    if kiss_mom_lips == True:
        Mom "What? How’s it any different to, you kissing me, like you did this morning?"
        MC "..."
        Mom "…"

        jump after_conditional_mom_kiss_cheek_lips_intro

label after_conditional_mom_kiss_cheek_lips_intro:

    scene intro47
    Mom "I’m sorry. I got a little carried away, and couldn’t hold myself back this time."
    MC "Wh-"
    Mom "I should go. Your dinner will be in the oven, to keep it warm."

    scene intro48
    MC "(What the heck did she mean by “hold myself back this time”?)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro49 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    MC "So yeah, that was pretty much what happened."
    Judy "Hmm... When did the headmaster find out about the incident with Mrs. Celia?"
    MC "About four hours ago - early this morning."

    scene intro50
    Judy "I really AM sorry to hear about what happened to you. It sounds terribly embarrassing. I can’t even begin to imagine, how it must feel to be in your position right now."
    Judy "Trust me though - with regular therapy sessions, we will get you through this."
    Judy "You are clearly - (ahem) - WERE clearly attracted to Mrs. Celia. I was wondering - does this attraction apply to other women, of a similar age?"
    MC "Uhh… like who?"
    if renpy.loadable("patch.rpy"):
        Judy "Oh, I don’t know... How about… your mother?"
    if not renpy.loadable("patch.rpy"):
        Judy "Oh, I don’t know... How about… Linda?"
    scene intro51
    if renpy.loadable("patch.rpy"):
        MC "What?! Are you asking me if I’m attracted to my mother?"
    if not renpy.loadable("patch.rpy"):
        MC "What?! Are you asking me if I’m attracted to Linda?"
    Judy "You did just tell me you were, kissing her while lying down on your bed."
    MC "She was the one who kissed me!"
    if renpy.loadable("patch.rpy"):
        Judy "Ahh, so you pushed your mom away when she tried to kiss you?"
    if not renpy.loadable("patch.rpy"):
        Judy "Ahh, so you pushed her away when she tried to kiss you?"
    MC "N-Not exactly- but-"

    scene intro1
    if renpy.loadable("patch.rpy"):
        Judy "So, let me ask you the question again. Do you have sexual fantasies about your mother?"
    if not renpy.loadable("patch.rpy"):
        Judy "So, let me ask you the question again. Do you have sexual fantasies about Linda?"
    MC "No!"
    if renpy.loadable("patch.rpy"):
        Judy "Why not? You stated you were attracted to your sister, Sara."
    if not renpy.loadable("patch.rpy"):
        Judy "Why not? You stated you were attracted to Sara."
    if renpy.loadable("patch.rpy"):
        MC "It doesn’t matter - even if I did like her, I wouldn’t do anything! She’s my mother! It’s just… weird. Y’know?"
    if not renpy.loadable("patch.rpy"):
        MC "It doesn’t matter - even if I did like her, I wouldn’t do anything! She’s my friend! It’s just… weird. Y’know?"
    scene intro15
    if renpy.loadable("patch.rpy"):
        Judy "You seem like a good-natured boy. Obviously, you want what’s best for your family, right? You want them to be happy?"
    if not renpy.loadable("patch.rpy"):
        Judy "You seem like a good-natured boy. Obviously, you want what’s best for your friends, right? You want them to be happy?"
    MC "Of course?"
    if renpy.loadable("patch.rpy"):
        Judy "What if that meant, accepting your mother as a romantic partner? What if that is, what was required, to really make your mother happy?"
    if not renpy.loadable("patch.rpy"):
        Judy "What if that meant, accepting Linda as a romantic partner? What if that is, what was required, to really make her happy?"
    MC "What kind of questions are these?!"
    Judy "I already told you, it’s Freudian Psychology. Feel free to read about it in the school library, if you don’t believe me."
    if renpy.loadable("patch.rpy"):
        Judy "So, let me rephrase. If you had the opportunity to fuck your mother, would you take it? "
    if not renpy.loadable("patch.rpy"):
        Judy "So, let me rephrase. If you had the opportunity to fuck Linda, would you take it? "
    if renpy.loadable("patch.rpy"):
        Judy "We’ve already established that you want to make your mom happy. And it’s pretty obvious, you want to get laid. Is this not a win-win situation?"
    if not renpy.loadable("patch.rpy"):
        Judy "We’ve already established that you want to make Linda happy. And it’s pretty obvious, you want to get laid. Is this not a win-win situation?"
    scene intro16
    MC "I… No! I’ve never thought about her like that!"
    if renpy.loadable("patch.rpy"):
        MC "She’s my mother! I’ve already said that I wouldn’t do anything with her!"
    if not renpy.loadable("patch.rpy"):
        MC "She’s my friend! I’ve already said that I wouldn’t do anything with her!"

    scene intro52
    if renpy.loadable("patch.rpy"):
        Judy "Interesting... I think that will do for today’s session. I’m going to ask you to visit me again, if anything noteworthy happens between you and your mother. Or even, perhaps, your sisters."
    if not renpy.loadable("patch.rpy"):
        Judy "Interesting... I think that will do for today’s session. I’m going to ask you to visit me again, if anything noteworthy happens between you and Linda. Or even, perhaps, your friends."
    MC "Noteworthy? Like what?"
    Judy "I’m sure you’ll recognise, something noteworthy, when it happens."
    Judy "Now, make sure you get some rest, [player_name]. Relaxation is very important, in recovering from trauma."
    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(5.0)

    scene intro53 with dissolve
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    MC "(Yawn!)"
    MC "(It’s the start of a brand new day. Let’s make the most of it!)"
    MC "(I need to focus on getting my life back on track after that… mishap yesterday.)"

    scene intro54

    MC "(Let’s get my confidence back, get a hot girl, and get laid!)"
    MC "(Picking up chicks would be so much easier if I was in one of those sex games from Patreon.)"
    MC "(I can’t give up though!)"
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    jump mc_room_morning1
