image CeR2_MS2_p1 = "images/CeR2/MS2/1.jpg"
image CeR2_MS2_p2 = "images/CeR2/MS2/2.jpg"
image CeR2_MS2_p3 = "images/CeR2/MS2/3.jpg"
image CeR2_MS2_p4 = "images/CeR2/MS2/4.jpg"
image CeR2_MS2_p5 = "images/CeR2/MS2/5.jpg"
image CeR2_MS2_p6 = "images/CeR2/MS2/6.jpg"
image CeR2_MS2_p7 = "images/CeR2/MS2/7.jpg"
image CeR2_MS2_p8 = "images/CeR2/MS2/8.jpg"
image CeR2_MS2_p9 = "images/CeR2/MS2/9.jpg"
image CeR2_MS2_p10 = "images/CeR2/MS2/10.jpg"
image CeR2_MS2_p11 = "images/CeR2/MS2/11.jpg"
image CeR2_MS2_p12 = "images/CeR2/MS2/12.jpg"
image CeR2_MS2_p13 = "images/CeR2/MS2/13.jpg"
image CeR2_MS2_p14 = "images/CeR2/MS2/14.jpg"
image CeR2_MS2_p15 = "images/CeR2/MS2/15.jpg"
image CeR2_MS2_p16 = "images/CeR2/MS2/16.jpg"
image CeR2_MS2_p17 = "images/CeR2/MS2/17.jpg"
image CeR2_MS2_p18 = "images/CeR2/MS2/18.jpg"
image CeR2_MS2_p19 = "images/CeR2/MS2/19.jpg"
image CeR2_MS2_p20 = "images/CeR2/MS2/20.jpg"
image CeR2_MS2_p21 = "images/CeR2/MS2/21.jpg"
image CeR2_MS2_p22 = "images/CeR2/MS2/22.jpg"
image CeR2_MS2_p23 = "images/CeR2/MS2/23.jpg"
image CeR2_MS2_p24 = "images/CeR2/MS2/24.jpg"
image CeR2_MS2_p25 = "images/CeR2/MS2/25.jpg"
image CeR2_MS2_p26 = "images/CeR2/MS2/26.jpg"
image CeR2_MS2_p27 = "images/CeR2/MS2/27.jpg"

default CeR2_AS2 = False
label CeR2_MS2_lab:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CeR2_MS2_p1 with dissolve
    MC "Hi Celia."
    Celia "Hi, [player_name]. It’s good you’re here. I wanted to talk with you about something."
    MC "Oh?"
    Celia "Is there anything you would like to confess before we begin?"

    scene CeR2_MS2_p2
    MC "Begin what? What do you mean?"
    MC "(She can’t have worked out it’s me. Can she?)"

    scene CeR2_MS2_p3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)

    Celia "Look, let’s cut this bullshit. We both know it was you."
    MC "We know what was me? "
    Celia "Fair enough. If you’re not going to admit to it, then I guess we’ll just have to go for some more drastic measures."

    scene CeR2_MS2_p2
    MC "What the hell are you talking about? Are you accusing me of something?"
    MC "All I’ve done is try and help you; and what do I get in return is what? Spurious accusations that I might be the one blackmailing you?!"
    MC "You’re messed up!"

    scene CeR2_MS2_p4
    Celia "Alright, let’s cut the crap. I am not the kind of woman you want to mess with!"
    Celia "I can easily break you down and make your sorry little ass beg for mercy!"

    scene CeR2_MS2_p5
    Celia "So, let’s sit down and talk about this. Shall we?"
    MC "(It’ll look suspicious if I run away now. I better sit down.)"
    MC "Alright."

    scene CeR2_MS2_p6
    Celia "So, [player_name], the funniest thing happened the other day. My blackmailer brought me to the toilet and made me suck their cock, or possibly one of their friends."
    MC "Okay…"

    scene CeR2_MS2_p7
    Celia "(Time for a little bit of bluffing. Let’s see if he was in the toilets at the time I was there. I can’t be certain, but I might be able to trick him into talking.)"
    Celia "So, I waited outside the men’s toilets and the darndest thing happened…"
    MC "(Oh fuck… She couldn’t have seen me, right?!)"

    scene CeR2_MS2_p8
    Celia "You walked out of them."
    MC "Wait - a LOT of guys in school use those toilets."
    Celia "I never saw you go into them, which leads me to believe you were already in them."

    scene CeR2_MS2_p9
    MC "I- I don’t know what you’re talking about."
    Celia "How did you end up in those toilets, [player_name]?"
    MC "I… I must have already been in them before you went in. The blackmailer must have left after I did."
    Celia "Oh yeah? And why did it take you so long before you came out of the toilet?"
    MC "I was constipated!"

    scene CeR2_MS2_p10
    Celia "That’s a load of shit!"

    scene CeR2_MS2_p6
    MC "Quite the opposite, actually…"

    scene CeR2_MS2_p11
    Celia "Let’s assume you were constipated. Why didn’t you hear me sucking off my assailant?"
    MC "I was… uhh…"
    Celia "You must have heard some noises? Why didn’t you think to check what was going on in the stall beside you?"

    scene CeR2_MS2_p12
    MC "(Shit… Think, [player_name]! You can lie your way out of this one.)"
    MC "I was… listening to music with my earphones in! That must be why I never heard you."

    scene CeR2_MS2_p13
    Celia "BULL! FUCKING! SHIT!"
    Celia "You’re a liar, [player_name], and I’ve caught you red handed!"

    scene CeR2_MS2_p14
    MC "Fuck you! I’m leaving! You’re on your own!"
    MC "I tried to help you out, but you’re fucking psychotic! You know that?!"

    scene CeR2_MS2_p15
    Celia "Ugh!"
    Celia "You know what? I gave you a chance to come clean about everything."

    scene CeR2_MS2_p16
    Celia "Where are you going?"
    MC "I’m leaving. I have classes to attend."

    scene CeR2_MS2_p17
    MC "Whoa! Hey! What the hell are you doing?"
    Celia "Teaching you not to mess with the wrong woman!"

    scene CeR2_MS2_p18
    Celia "I know it is you."
    MC "You’re insane! I’m the one who has been trying to HELP you!"

    scene CeR2_MS2_p19
    Celia "I don’t buy it. Not for a single second."
    MC "How am I supposed to prove I’m innocent? If I were the blackmailer why on earth would I be trying to help you catch me?! It doesn’t make ANY sense!"

    scene CeR2_MS2_p20
    MC "(Heh, I’ve got a really nice view of her panties down here!)"
    MC "(It’s a shame I’m not looking at them under more relaxed circumstances.)"

    scene CeR2_MS2_p21
    Celia "…"
    MC "See? I was actually the ONLY person in this place trying to help you."

    scene CeR2_MS2_p22
    MC "We could have teamed up together to solve this!"
    MC "But now you’ve gone and pushed me away. You’re alone again."

    scene CeR2_MS2_p23
    MC "I know you’re angry and frustrated. Guess what - so am I! "
    MC "We should have been handling this together. We were so close to catching the bastard who was behind this."

    scene CeR2_MS2_p24
    MC "I want nothing to do with you anymore."
    MC "Good luck with the blackmailer."

    scene CeR2_MS2_p25
    MC "Goodbye, Celia."
    Celia "(I’m still pretty sure he is the one behind all of this. I just need to get some more evidence to catch him.)"

    scene CeR2_MS2_p26
    MC "(I hope that I was convincing enough there!)"
    MC "(I’ll have to arrange to fuck her in the cubicle. This bitch needs to be brought down a peg or two!)"

    scene CeR2_MS2_p27
    Celia "(You can say all you want, I’m gonna catch you, you piece of shit.)"
    Celia "(Next time I’m told to give a blowjob in the toilet I’m gonna wait outside for as long as it takes. When I see you coming out of it, and I’m certain I will, I’ll catch you red-handed.)"

    $ CeR2_MS2 = False
    $ CeR2_AS2 = 1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ renpy.sound.play('/sfx/door_open.mp3', channel="sound")
    $ can_hide_windows = False
    jump school_corridor2_morning1

