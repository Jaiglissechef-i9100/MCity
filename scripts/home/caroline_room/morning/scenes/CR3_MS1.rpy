image CR3_MS1_p1 = "/images/home/caroline_room/morning/scenes/CR3_MS1/1.jpg"
image CR3_MS1_p2 = "/images/home/caroline_room/morning/scenes/CR3_MS1/2.jpg"
image CR3_MS1_p3 = "/images/home/caroline_room/morning/scenes/CR3_MS1/3.jpg"
image CR3_MS1_p4 = "/images/home/caroline_room/morning/scenes/CR3_MS1/4.jpg"
image CR3_MS1_p5 = "/images/home/caroline_room/morning/scenes/CR3_MS1/5.jpg"
image CR3_MS1_p6 = "/images/home/caroline_room/morning/scenes/CR3_MS1/6.jpg"
image CR3_MS1_p7 = "/images/home/caroline_room/morning/scenes/CR3_MS1/7.jpg"
image CR3_MS1_p8 = "/images/home/caroline_room/morning/scenes/CR3_MS1/8.jpg"
image CR3_MS1_p9 = "/images/home/caroline_room/morning/scenes/CR3_MS1/9.jpg"
image CR3_MS1_p10 = "/images/home/caroline_room/morning/scenes/CR3_MS1/10.jpg"
image CR3_MS1_p11 = "/images/home/caroline_room/morning/scenes/CR3_MS1/11.jpg"
image CR3_MS1_p12 = "/images/home/caroline_room/morning/scenes/CR3_MS1/12.jpg"
image CR3_MS1_p13 = "/images/home/caroline_room/morning/scenes/CR3_MS1/13.jpg"
image CR3_MS1_p14 = "/images/home/caroline_room/morning/scenes/CR3_MS1/14.jpg"

image CR3_MS1_Deal_p1 = "/images/home/caroline_room/morning/scenes/CR3_MS1/Deal/1.jpg"
image CR3_MS1_Deal_p2 = "/images/home/caroline_room/morning/scenes/CR3_MS1/Deal/2.jpg"
image CR3_MS1_Deal_p3 = "/images/home/caroline_room/morning/scenes/CR3_MS1/Deal/3.jpg"
image CR3_MS1_Deal_p4 = "/images/home/caroline_room/morning/scenes/CR3_MS1/Deal/4.jpg"

label CR3_MS1_label:
    if CR3_MS1_talked == True:
        hide screen map_button
        show screen caroline_room_morning
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen caroline_room_morning
        jump caroline_room_morning1
    if CR3_MS1_q1 == False and CR3_MS1_q2 == False and  CR3_MS1_q3 == False and  CR3_MS1_q4 == False and CR3_MS1_q5 == False and  CR3_MS1_q6 == False:
        hide screen map_button
        show screen caroline_room_morning
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen caroline_room_morning
        jump caroline_room_morning1

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR3_MS1_p1 with dissolve

    MC "(There’s Caroline, working away again. She never seems to stop or rest!)"
    MC "(Well, here we go. Let’s see if, I can break the ice and get our deal, back up and running.)"
    MC "Morning, Caroline!"

    scene CR3_MS1_p2

    Caroline "Morning, [player_name]! Did you sleep well?"

    MC "Yeah - like a log!"
    Caroline "Good to hear! What can I do for you?"
    MC "Nothing much - I just came to chat."

    jump CR3_MS1_menu

label CR3_MS1_menu:

    scene CR3_MS1_p2
    menu:
        "When you were young, did you always want to run your own business?" if CR3_MS1_q1 == True:
            scene CR3_MS1_p3

            MC "When you were young, did you always want to run your own business?"

            scene CR3_MS1_p13

            Caroline "Heh… When - I was young - I wanted to be a princess."
            MC "Haha! Seriously?!"
            Caroline "Of course! Princesses are - insanely rich - and they’re powerful enough to - do whatever they want. They’re beholden to no one."

            scene CR3_MS1_p4

            MC "I see. So you grew out of your - princess fantasy - and matured, then started your own business."

            scene CR3_MS1_p5

            Caroline "Why do you think I grew out of it? As far as I’m concerned, I’m closer to being a princess than I’ve - ever been - in my life."
            MC "I’m not following you... What do you mean?"

            scene CR3_MS1_p8

            Caroline "Just think about it – I’m independent, to run my own business and - do as I please. There’s no boss above me, dictating what I can and cannot do."
            if persistent.incest_patch == True:
                Caroline "Now that I’ve got a steady stream of income. I’m not even worried about having to borrow money, from Mom and Dad."
            else:
                Caroline "Now that I’ve got a steady stream of income. I’m not even worried about having to borrow money, from Linda and Bob."
            MC "Huh... I guess you’re right."

            scene CR3_MS1_p10

            Caroline "Of course I am – I’m the mother-fucking princess! Hehe!"

            $ CR3_MS1_q1 = False

            jump CR3_MS1_menu

        "Are you planning to expand your business, any time soon?" if CR3_MS1_q2 == True:
            scene CR3_MS1_p5

            MC "Are you planning to expand your business, any time soon?"
            Caroline "Not in the near future. The first two years of a private company, are always the toughest. I mean, just look how bad things were - a couple of weeks back. I was in a really bad place."

            scene CR3_MS1_p6

            Caroline "The best thing for me to do right now, is play it safe and focus on my online sales. At the minute - the high streets are dying. If I open another store and the trend continues, I could - very quickly - find myself in the red."

            scene CR3_MS1_p7

            Caroline "Whereas, if I focus on online sales, I don’t need to concern myself with additional rent costs – I can operate entirely as a distributor."
            Caroline "I mean, in an age where people can simply log-on and order anything they want - with a few clicks, what could possibly entice people, to visit a brick and mortar store?"
            MC "Yeah, I see where you’re coming from. It sounds like you’re acting very sensibly."

            $ CR3_MS1_q2 = False
            jump CR3_MS1_menu

        "{color=#00ff00}Have you thought any more about our deal? Maybe we could make a new one?{/color}" if CR3_MS1_q3 == True:
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
            scene CR3_MS1_Deal_p1

            MC "Have you thought any more about our deal? I know the old one is gone - but perhaps we could... make a new one?"
            Caroline "…"
            MC "Caroline?"

            scene CR3_MS1_Deal_p2

            Caroline "*Sigh* I thought I was PRETTY clear, the last time we talked. The deal is over, [player_name]. You’re just gonna have to - try to accept it - and move on."
            MC "Wait, what if-"

            scene CR3_MS1_Deal_p3

            Caroline "No ‘ifs’ or ‘buts’, please, [player_name]. Don’t make this - any harder - than it needs to be."
            MC "Please, just hear me out. This doesn’t need to be over... If we just-"

            scene CR3_MS1_Deal_p4

            Caroline "If you keep pushing the topic, I’m going to have to put some distance between us."
            MC "Huh? What do you mean?!"
            Caroline "I’ll have to block your phone number and move out. I’m not sure where I’ll go, but I think I have a few friends I can - shack up with. This obsession you have, with our deal, is just... unhealthy. It’s over - and you NEED to move on."
            MC "(Shit... Something - really has gotten to her. Did I - come on too strong - when we were fooling around together?)"
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)
            if CR3_MS1_can == True:
                $ CR3_MS1_can = 3

            $ CR3_ES1 = True
            $ CR3_MS1_q3 = False
            $ CR3_AS1_can = True
            jump CR3_MS1_menu

        "Are you planning to expand your business anytime soon?" if CR3_MS1_q4 == True:

            scene CR3_MS1_p3

            MC "Have you thought any more about hiring a part time employee?"

            scene CR3_MS1_p8

            Caroline "Yeah, it’s happening, and sorry, but before you ask – I can’t hire you."
            MC "Yeah, I guessed that. Have you got someone in mind?"
            Caroline "I’ve got a couple of potential candidates. I need someone I can trust, though - so I’m being very cautious, before I commit myself to anyone, in particular."
            MC "Well, if you ever need a volunteer, you know I’m always happy to-"

            scene CR3_MS1_p11

            Caroline "Absolutely not... I don’t think it would be appropriate, in the slightest - after everything that happened between us."

            $ CR3_MS1_q4 = False
            jump CR3_MS1_menu

        "If you’re looking someone to help you out with your business, perhaps you could speak to Sara." if CR3_MS1_q5 == True:
            scene CR3_MS1_p3

            MC "If you’re looking for someone to help out with your business, perhaps you could speak to Sara."

            scene CR3_MS1_p7

            Caroline "Seriously? She’s FAR too young! Besides, she’s busy at school right now. I don’t want her, working a job AND trying to keep her grades good!"
            MC "Yeah, I guess you’re right."

            $ CR3_MS1_q5 = False
            jump CR3_MS1_menu

        "Would you like to hang out sometime? Maybe dinner or a movie?" if CR3_MS1_q6 == True:
            scene CR3_MS1_p9

            MC "Would you like to hang out sometime? Maybe dinner or a movie?"

            scene CR3_MS1_p6

            Caroline "*Sigh* I know what you’re trying to do. I already told you - the deal is off."
            MC "What makes you think I was trying to get our deal back on?!"

            scene CR3_MS1_p8
            Caroline "Oh please... You’re a guy! I see through you, like a glass window."

            MC "(Damn! Am I really that easy to read?)"

            $ CR3_MS1_q6 = False
            jump CR3_MS1_menu
        "Bye.":

            scene CR3_MS1_p9

            MC "Okay, I better head on, here. Lots of things to do."
            Caroline "No problem, [player_name]. I’ll see you around."
            MC "Are you gonna be working on - this crap - all morning?"

            scene CR3_MS1_p4

            Caroline "Yeah - unfortunately. Tax returns are a fucking nightmare! I swear to God, I’ve been at this since six AM!"
            MC "Ugh! Best of luck with that!"

            scene CR3_MS1_p14

            Caroline "See ya later, [player_name]."
            MC "Bye, Caroline!"
            $ CR3_MS1_talked = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump caroline_room_morning1

