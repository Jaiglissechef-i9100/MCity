label sara_botlle_game_v1:
    hide screen scenes_gallery
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene sis_nerdy_school_scene3_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "I honestly don’t know what to do."
    Lily "Well… do you like him?"
    Sara "Of course I like him."
    Lily "C’mon, Sara. You know what I mean - do you ‘like’ like him?"
    Sara "Y...Yeah… I think I do."

    scene sis_nerdy_school_scene3_v1_p2
    Lily "Speak of the Devil!"
    Sara "Huh?!"
    Lily "Hey, [player_name]. We were just talking about you."

    scene sis_nerdy_school_scene3_v1_p3
    MC "Only good things, I hope."
    Lily "Hehe! Of course!"
    MC "What’s wrong, Sara? You’re looking a bit nervous."
    Lily "She’s fine! She just needs to lighten up. How about we all get together and play a fun game? Chill out for a bit!"

    scene sis_nerdy_school_scene3_v1_p4
    MC "Sure - sounds good to me."
    Sara "Uh… I guess so…"
    Sara "(God… I hope he didn’t hear me saying those things to Lily…)"
    Lily "Are your parents home right now, Sara?"
    Sara "I don’t think so."
    Lily "Great! We can use your bedroom then!"
    Sara "My bedroom? What kind of game IS this?"

    menu:
        "Let’s go! This sounds fun!":

            MC "This sounds interesting. Let’s!"
            Lily "That’s the spirit!"
            jump after_sis_nerdy_school_scene3_v1_choice1r
        "It’s your bedroom, Sara. Do you want to do this?":


            MC "It’s your bedroom, Sara. Do you want to do this?"
            Sara "Umm… Maybe? I think so…"
            Lily "Yeah, she does. Let’s go!"
            jump after_sis_nerdy_school_scene3_v1_choice1r

label after_sis_nerdy_school_scene3_v1_choice1r:

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music2", loop=True, fadein = 2)

    scene sis_nerdy_school_scene3_v1_p5 with fadehold
    MC "Well? What now?"
    Lily "Go and get a bottle."
    MC "A bottle?"
    Lily "Yeah - a glass one. They spin better."
    MC "Oh! We’re gonna play, spin the bottle."

    scene sis_nerdy_school_scene3_v1_p6
    MC "I’ll be back in a few minutes."
    Lily "Cool! See you soon!"
    Sara "(Whispered) You can’t be serious, Lily! He’s not gonna actually kiss me if it points to me, is he?!"
    Lily "Let’s wait and see…"

    scene sis_nerdy_school_scene3_v1_p7
    Lily "Aww... Don’t look soooo gloomy, Sara! What’s the matter?"
    Sara "Wh… What if he doesn’t want to kiss me?"
    Lily "Well, that doesn’t matter…"

    scene sis_nerdy_school_scene3_v1_p8
    Lily "...because he’s gonna be kissing these luscious lips first!"
    Lily "I think he’s really gonna enjoy making out with me. I’ll make sure to kiss him REAL good for you."

    scene sis_nerdy_school_scene3_v1_p9
    if renpy.loadable("patch.rpy"):
        Sara "Hey! That’s my brother you’re talking about!"
    if not renpy.loadable("patch.rpy"):
        Sara "Hey! That’s my friend you’re talking about!"
    Lily "Easy, Sara. Chill out!"
    Sara "Don’t tell me to chill out!"

    scene sis_nerdy_school_scene3_v1_p10
    Sara "Don’t you dare think you can just kis-"
    MC "Hey, I found a glass bot-"
    MC "*Ahem* Is everything alright? You two aren’t fighting, are you?"

    scene sis_nerdy_school_scene3_v1_p11
    Lily "Fighting? Haha! No, we’re just wrestling!"
    Sara "Y-Yeah…"
    MC "Great! Let’s get started then. How do you want to do this?"

    scene sis_nerdy_school_scene3_v1_p12
    Lily "Okay, you’re first, [player_name]. Whoever the bottle points at - you’ve got to kiss them."
    MC "Wait - even Sara?"
    Lily "Yup! Sara too!"
    MC "(Wow… Sara looks so nervous…)"

    scene sis_nerdy_school_scene3_v1_p13
    Lily "Let’s spin the bottle!"

    scene bottle_spin1
    $ renpy.pause (2.26, hard=True)

    Lily "Woo! That’s me!"

    scene sis_nerdy_school_scene3_v1_p14
    Lily "C’mere, big boy, and gimme a kiss!"
    MC "Uh… O-Okay…"
    MC "(She seems really into this! I never imagined that girls might actually like me this much!)"
    if renpy.loadable("patch.rpy"):
        Sara "(Nooo! God… the sight of her leaning into my bro, is making me feel sick.)"
    if not renpy.loadable("patch.rpy"):
        Sara "(Nooo! God… the sight of her leaning into my friend is making me feel sick.)"

    scene sis_nerdy_school_scene3_v1_p15
    Sara "(I know she’s meant to be my friend… but I feel so… sad and angry, that she flirts with him like this.)"
    if renpy.loadable("patch.rpy"):
        Sara "(And he’s my brother - I shouldn’t even have feelings about him!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(And he’s my friend - I shouldn’t even have feelings about him!)"

    scene sis_nerdy_school_scene3_v1_p16
    Lily "Mmm…"
    MC "(Wow! She’s a good kisser!)"
    Sara "(Calm down, Sara… it’s just ONE kiss. You’ll get your turn with him soon.)"

    scene sis_nerdy_school_scene3_v1_p17
    Lily "(Hehe… I can feel Sara’s eyes on me right now. Why are men always, so much more attractive when other women want them?)"
    MC "(Her lips are so soft! I could kiss her for hours!)"

    scene sis_nerdy_school_scene3_v1_p18

    Lily "Mmm, that was fun. Thanks, [player_name]."
    Lily "Hopefully that won’t be the last time our lips touch today."
    Sara "(That bitch…)"
    MC "Y-Yeah, I hope so too!"

    scene sis_nerdy_school_scene3_v1_p19
    Lily "Your turn, Sara! Who do you want to spin the bottle for?"
    Sara "…"
    Lily "C’mon! We’re burning daylight here!"
    Sara "I’ll… pass."
    Lily "Eh? Your loss!"

    scene sis_nerdy_school_scene3_v1_p20
    Lily "I guess it’s your turn again, [player_name]! Who do you want to spin the bottle for?"
    MC "Can I pick myself?"
    Lily "Hehe! Sure!"

    scene bottle_spin1
    $ renpy.pause (2.26, hard=True)

    scene sis_nerdy_school_scene3_v1_p21
    Lily "Yay! Me again!"
    Lily "Hope you’re ready for round two!"

    scene sis_nerdy_school_scene3_v1_p22
    MC "(Damn! I never imagined this would turn out to be such an awesome afternoon!)"
    MC "(I ought to hang out with Lily more often!)"

    scene sis_nerdy_school_scene3_v1_p23
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)
    if renpy.loadable("patch.rpy"):
        Sara "(That… fucking bitch! That’s my brother!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(That… fucking bitch! That’s my friend!)"
    Sara "(How DARE she think she can just come into my bedroom and make out with him like this?!)"

    scene sis_nerdy_school_scene3_v1_p24
    Sara "(I’ll show her. I’ll FUCKING show that slutty little tart!)"
    if renpy.loadable("patch.rpy"):
        Sara "Get off my brother!"
    if not renpy.loadable("patch.rpy"):
        Sara "Get off my friend!"

    scene sis_nerdy_school_scene3_v1_p25
    $ renpy.pause(0.7)

    scene sis_nerdy_school_scene3_v1_p26 with flash2

    $ renpy.sound.play('/sfx/glass-smash.mp3', loop=False)
    $ renpy.pause(1, hard = True)
    scene sis_nerdy_school_scene3_v1_p27
    MC "WHAT?!"
    Sara "EEK!"
    Sara "Lily! Get OUT of my house!"
    Lily "Geez! Okay, I’m going! Catch you later, [player_name]."

    scene sis_nerdy_school_scene3_v1_p28
    Sara "I don’t want to play this… stupid game anymore."
    MC "Sara, I-"
    Sara "Leave me alone!"
    MC "But-"
    Sara "I said I wanted to be alone!"

    scene sis_nerdy_school_scene3_v1_p29
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    MC "Hey, Sara... It’s alright. What’s wrong?"
    Sara "(Sniff)"
    MC "Are you crying?"

    scene sis_nerdy_school_scene3_v1_p30
    Sara "I (sniff) I-I’m s-sorry, [player_name]. When I saw you k-kissing her, I…"
    MC "Hey, it’s alright. Shush - it’s okay."

    menu:
        "Kiss her.":

            scene sis_nerdy_school_scene3_v1_p31b
            MC "Mwah."
            Sara "(Oh wow… He’s actually kissing me... )"
            Sara "(It’s like one of my dreams coming true…)"
            jump after_sis_nerdy_school_scene3_v1_choice21r
        "Hug her.":


            scene sis_nerdy_school_scene3_v1_p31a
            MC "It’s okay, Sara. I think I understand."
            Sara "(Sniff)"
            MC "There there - I’ve got you. We won’t play that game anymore."
            jump after_sis_nerdy_school_scene3_v1_choice21r

label after_sis_nerdy_school_scene3_v1_choice21r:

    scene sis_nerdy_school_scene3_v1_p32
    Sara "(Sniff) Th-Thank you, [player_name]. D-Do you think you could give me a… real kiss?"
    MC "A real kiss?"
    if renpy.loadable("patch.rpy"):
        Sara "Like Mom and Dad do, when they watch a romantic movie."
    if not renpy.loadable("patch.rpy"):
        Sara "Like Linda and Landlord do when they watch a romantic movie."
    MC "Of course, Sara. Come closer."

    scene sis_nerdy_school_scene3_v1_p33r
    Sara "(Oh my God! He did it! …This is Heaven!)"
    if renpy.loadable("patch.rpy"):
        MC "(She’s a much better kisser than Lily! It feels like there’s more… passion behind Sara’s kiss.)"
        MC "(Why am I going along with this, so freely? She’s my sister! I shouldn’t be kissing her like this. Right?)"
    if not renpy.loadable("patch.rpy"):
        MC "(She’s a much better kisser than Lily! It feels like there’s more… passion behind my Sara’s kiss.)"
        MC "(Why am I going along with this, so freely? She’s my friend! I shouldn’t be kissing her like this. Right?)"
    scene sis_nerdy_school_scene3_v1_p34
    Sara "Thank you so much, [player_name]."
    MC "What was wrong? You kinda freaked out back there."
    Sara "I… I don’t know… When I saw Lily kissing you, I just got so… irrationally angry."
    MC "It’s okay. I think I understand."

    scene sis_nerdy_school_scene3_v1_p35
    Sara "I… I want to do… something for YOU."
    MC "What do you mean?"
    Sara "I saw a video once… of a woman using her mouth, to suck a guy’s… thing."
    MC "What?! Are you talking about giving me a blowjob?"

    scene sis_nerdy_school_scene3_v1_p36
    Sara "Please, [player_name] - just stay still and let me do this. I really want to make you feel good."
    if renpy.loadable("patch.rpy"):
        MC "Sara, I- You’re my little sister."
    if not renpy.loadable("patch.rpy"):
        MC "Sara, I- You’re my little friend."
    Sara "Shush! Just let me pull your trousers down."

    scene sis_nerdy_school_scene3_v1_p37
    MC "Sara, wait. Are you sure about this?"
    Sara "I- Um… yeah, I am."
    MC "I don’t want you doing something that you’ll regret later on."

    scene sis_nerdy_school_scene3_v1_p37a
    Sara "If I’m going to do it for you, there’s no way I could ever regret it."
    MC "Are you sure? Have you done anything like this before?"
    Sara "No… this is my first time."
    MC "Let me sit down on the bed, to make it easier for you then."
    Sara "Is there anything else I should do?"
    MC "Could you take your top off before you start?"
    Sara "(Ahh… That’s so embarrassing… I feel like I should do it for him though…)"
    Sara "O-Okay…"

    scene sis_nerdy_school_scene3_v1_p38
    MC "Wow… You look so hot, Sara."
    Sara "Th-Thank you…"
    Sara "What should I do now?"
    MC "Go ahead and pull down my underwear."

    scene sis_nerdy_school_scene3_v1_p39
    $ renpy.pause(1.2)
    scene sis_nerdy_school_scene3_v1_p39anim
    $ renpy.pause(3)
    scene sis_nerdy_school_scene3_v1_p40r
    Sara "Wow!"
    Sara "(It’s bigger than I remember! How can I possibly get it all in my mouth?)"
    Sara "Hehe! It’s all bouncy…"
    MC "(She definitely hasn’t played with a cock before. I guess I’ll just let her have some fun for a bit, while she experiments.)"
    Sara "Can you feel it when I do this?"
    MC "Yeah, but it feels better if you wrap your hands around it and move them up and down."

    scene sis_nerdy_school_scene3_v1_p41r
    Sara "Like this, [player_name]?"
    MC "Ahh… That’s good, Sara."
    Sara "Hehe... You’re smiling!"
    MC "That’s because it feels really good."

    scene sis_nerdy_school_scene3_v1_p41rr
    MC "Mmm!"
    Sara "(It keeps getting harder, the more I move!)"
    if renpy.loadable("patch.rpy"):
        Sara "(I’d only ever dreamed about touching [player_name]'s cock before! It’s actually happening now!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(I’d only ever dreamed about touching [player_name]’s cock before! It’s actually happening now!)"
    MC "Okay - you can start licking next. Just use your tongue to swirl around the tip of my cock."

    scene sis_nerdy_school_scene3_v1_p42r
    Sara "(It tastes a little salty! That’s not what I expected at all!)"
    MC "Ohh… That’s good. Keep going, Sara."

    scene sis_nerdy_school_scene3_v1_p43
    Sara "Am I doing it right, [player_name]?"
    MC "Y-Yeah, it’s so good."
    Sara "What should I do next?"

    scene sis_nerdy_school_scene3_v1_p44
    MC "Try and take my cock in your mouth."
    Sara "A-All of it?"
    Sara "(It’s so big… I don’t think I’ll be able to get, even HALF of it in my mouth!)"

    scene sis_nerdy_school_scene3_v1_p45
    MC "Just relax - you don’t have to do the whole thing. Just go as far as you can, without making yourself uncomfortable."
    Sara "But I want to make you feel good too…"
    MC "It’ll feel good - you don’t need to hurt yourself."
    Sara "O-Okay!"

    scene sis_nerdy_school_scene3_v1_p46r
    "(Shlurrrp)"
    "(Suck Suck)"
    MC "(Mmm… This feels good. She’s being so gentle with her lips!)"

    scene sis_nerdy_school_scene3_v1_p47
    "(Shllurrrrrrrpp)"
    Sara "(I don’t think I can go much deeper than this!)"
    MC "Easy, Sara. You don’t need to push yourself - it’s your first time."
    MC "This feels amazing, I promise."

    scene sis_nerdy_school_scene3_v1_p48
    MC "(I can’t believe that Sara was sexually attracted to me. How long has she felt this way?)"
    if renpy.loadable("patch.rpy"):
        MC "(Was I really, so obsessed with my teacher that I never even noticed my own sister’s affections for me?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Was I really, so obsessed with my teacher that I never even noticed my own friend’s affections for me?)"
    "(Suck Suck)"

    scene sis_nerdy_school_scene3_v1_p49r
    "(Shlurp Suck)"
    MC "Ohh! Ahh!"
    MC "(I’m gonna cum soon, if she keeps this up! It might be her first time giving a blowjob, but she’s pretty damn good at it!)"

    scene sis_nerdy_school_scene3_v1_p50
    MC "(I’m gonna cum soon. I should let her know!)"
    MC "Sara, I’m about to cum - that means semen is going to come out of my cock."
    Sara "Mmm hmm!"

    scene sis_nerdy_school_scene3_v1_p51
    MC "Ahhh! Fuck! I’m cumming!"
    Sara "(Wow! I can feel him shaking and trembling! He must really, love me doing this!)"
    MC "Hnnng!"
    Sara "(I should take the whole head of his cock, in my mouth, while he cums!)"

    scene sis_nerdy_school_scene3_v1_p52
    MC "Ahhhh! Yes! Ugh!"
    Sara "(I can feel it filling my mouth! It’s really warm and salty!)"
    MC "Fuck! Ah! You’re so good, Sara!"
    scene sis_nerdy_school_scene3_v1_p52 with fadehold
    $ renpy.pause(0.1)
    scene sis_nerdy_school_scene3_v1_p52 with fadehold
    $ renpy.pause(0.1)
    scene sis_nerdy_school_scene3_v1_p52
    MC "Ah! You can stop now - I’m done!"

    scene sis_nerdy_school_scene3_v1_p53
    Sara "Wha duh I duh wuh thus?"
    MC "(I think she’s asking what she does with my cum now.)"

    menu:
        "I want you to swallow it.":

            MC "I want to see you swallow my cum."

            scene sis_nerdy_school_scene3_v1_p54
            Sara "(GULP)"
            Sara "(Huh? It’s not too bad. Lily was telling me that she hated the taste of cum when she gave blowjobs!)"
            scene sis_nerdy_school_scene3_v1_p55
            Sara "Ahh! All gone!"
            MC "Thank you, Sara. You’re adorable."
            Sara "Hehe... I know!"
            jump after_sis_nerdy_school_scene3_v1_choice31r
        "You don’t have to swallow it if you don’t want to.":

            scene sis_nerdy_school_scene3_v1_p53
            MC "Some girls swallow cum, but you don’t have to if you don’t want-"
            scene sis_nerdy_school_scene3_v1_p54
            Sara "(Gulp!) Ahh!"
            Sara "(I hope he’ll like me more if I swallow all his cum!)"
            scene sis_nerdy_school_scene3_v1_p55
            Sara "All gone!"
            MC "You didn’t have to do that on your first time!"
            Sara "I wanted to. I wanted to make it the best for you!"
            jump after_sis_nerdy_school_scene3_v1_choice31r

label after_sis_nerdy_school_scene3_v1_choice31r:
    scene sis_nerdy_school_scene3_v1_p56
    Sara "I really love you, [player_name]."
    Sara "(It feels so good lying against him - feeling his clothes against my skin.)"
    MC "(Wow… She really likes me a whole lot!)"
    scene sis_nerdy_school_scene3_v1_p57
    Sara "I want to lie here with you for a while…"
    MC "Are you comfy?"
    Sara "Yeah."
    MC "Just relax then. Thank you so much for everything, Sara."
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
