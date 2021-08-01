image sara_room_evening_scene1_v1_p1 = "images/home/sara_room/evening/scene1_v1/1.jpg"
image sara_room_evening_scene1_v1_after = "images/home/sara_room/evening/scene1_v1/after_sara_scene1.png"

image sara_room_evening_scene2_v1_p1 = "images/home/sara_room/evening/scene2_v1/1.jpg"
image sara_room_evening_scene2_v1_p2 = "images/home/sara_room/evening/scene2_v1/2.jpg"
image sara_room_evening_scene2_v1_p3 = "images/home/sara_room/evening/scene2_v1/3.jpg"
image sara_room_evening_scene2_v1_p4 = "images/home/sara_room/evening/scene2_v1/4.jpg"
image sara_room_evening_scene2_v1_p5 = "images/home/sara_room/evening/scene2_v1/5.jpg"
image sara_room_evening_scene2_v1_p6 = "images/home/sara_room/evening/scene2_v1/6.jpg"
image sara_room_evening_scene2_v1_p7 = "images/home/sara_room/evening/scene2_v1/7.jpg"
image sara_room_evening_scene2_v1_p8 = "images/home/sara_room/evening/scene2_v1/8.jpg"
image sara_room_evening_scene2_v1_p9 = "images/home/sara_room/evening/scene2_v1/9.jpg"
image sara_room_evening_scene2_v1_p10 = "images/home/sara_room/evening/scene2_v1/10.jpg"
image sara_room_evening_scene2_v1_p11 = "images/home/sara_room/evening/scene2_v1/11.jpg"
image sara_room_evening_scene2_v1_p12 = "images/home/sara_room/evening/scene2_v1/12.jpg"
image sara_room_evening_scene2_v1_p13 = "images/home/sara_room/evening/scene2_v1/13.jpg"
image sara_room_evening_scene2_v1_p14 = "images/home/sara_room/evening/scene2_v1/14.jpg"
image sara_room_evening_scene2_v1_p15 = "images/home/sara_room/evening/scene2_v1/15.jpg"
image sara_room_evening_scene2_v1_p16 = "images/home/sara_room/evening/scene2_v1/16.jpg"
image sara_room_evening_scene2_v1_p17 = "images/home/sara_room/evening/scene2_v1/17.jpg"
image sara_room_evening_scene2_v1_p18 = "images/home/sara_room/evening/scene2_v1/18.jpg"
image sara_room_evening_scene2_v1_p19 = "images/home/sara_room/evening/scene2_v1/19.jpg"
image sara_room_evening_scene2_v1_p20 = "images/home/sara_room/evening/scene2_v1/20.jpg"

define Console = Character("Console")

label sis_nerdy_evening_scene1_v1_l:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ can_hide_windows = True
    if can_sis_nerdy_evening_scene1_v1 == True and sis_nerdy_evening_scene2_v1 == 0:
        scene sara_room_evening_scene1_v1_p1 with dissolve
        MC "Hey Sara, are you free to-"
        Sara "Sorry, [player_name]. I’m in the middle of a league final right now! If I win this match I’m through to next season!"
        Sara "I’ll catch you later!"
        MC "(Sara takes her gaming waaaay too seriously.)"
        MC "Alright, see you later, Sara."
        $ can_sis_nerdy_evening_scene1_v1 = False
        $ can_hide_windows = False
        jump sister_nerdy_evening1

    if can_sis_nerdy_evening_scene1_v1 == False:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "I've already talked to her."
        jump sister_nerdy_evening1

    if sis_nerdy_evening_scene2_v1 == 1:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p1 with dissolve
        MC "Hey Sara, you still busy with your league game?"
        Sara "Give me two seconds… this match is almost over."
        Sara "Aaaaand I’m done!"

        scene sara_room_evening_scene2_v1_p2
        Sara "Say, do you fancy gaming together? I can boot up the XSwitch4!"
        MC "Great! What game do you want to play?"
        Sara "Let me have a look and see what multiplayer games I have."

        scene sara_room_evening_scene2_v1_p3
        Sara "Hmm… Medal of Duty? Call of Honour?"
        Sara "Oh! I have Street Brawler VII!"
        MC "Anything works for me."
        Sara "Let’s do Street Brawler VII then. One vs one deathmatch!"
        MC "Sounds fun!"

        scene sara_room_evening_scene2_v1_p4
        Sara "Okay, there’s your controller. You’ve played before, right?"
        MC "Thanks. Yeah, and I’m pretty damn good at it - so you better watch your back!"
        Sara "Well, since you’re that confident, how about we change up the rules a bit?"
        MC "What are you thinking? Betting some money?"

        scene sara_room_evening_scene2_v1_p5
        Sara "The loser has to.... take off… a piece of clothing, each time they die."
        Sara "(This is my revenge for trying to steal my panties!)"
        MC "(Wait? WHAT?!)"
        MC "S-Sorry, I didn’t hear you right, there. What did you say?"
        Sara "Each time your character dies in-game, you have to lose a piece of clothing. Deal?"

        scene sara_room_evening_scene2_v1_p6
        MC "(Holy shit! I must be dreaming! This can’t actually be happening!)"
        MC "Hell yeah, that’s a deal."
        MC "You do realise that this means you’re about to be stripped naked? When it comes to the Street Brawler series - I’m a freakin’ pro."

        scene sara_room_evening_scene2_v1_p7
        Sara "Uh huh, I’m sure you are."
        Sara "Take a good look right now - because this is the closest you’re gonna get to seeing my tits today."
        MC "(Damn, I can’t wait to see her boobs today. There’s no way I’m losing to a girl! I’ve been playing the Street Brawler series since I was in kindergarden!)"

        scene sara_room_evening_scene2_v1_p8
        Console "READY! SET! FIGHT!"
        MC "(Damn! She’s quick!)"
        Sara "What’s the matter, [player_name]? You’re looking a bit stressed!"
        Sara "Hehe... Why haven’t you hit me yet?"
        MC "Because you aren’t giving me a chance to-"
        Console "Player 2 has been defeated!"
        MC "Dammit!"
        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Fifteen Minutes Later…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p9
        Sara "Hehe! Are you sure you want to go for one more round? You’ve only got your boxers left!"
        if persistent.incest_patch == True:
            MC "It isn’t over yet! I was just going easy on you because you’re my sister."
        else:
            MC "It isn’t over yet! I was just going easy on you because you’re my friend."
        Sara "Suuuuure!"
        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Five Minutes Later…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        Console "Player 2 has been defeated!"
        Console "Player 1 has broken a new killstreak record!"
        Sara "Woohoo!"

        scene sara_room_evening_scene2_v1_p10
        Sara "Don’t worry, [player_name]. You don’t have to take your underwear off too."
        Sara "I think you’ve already been humiliated enough! Hehe!"
        MC "Fair is fair - we agreed to the rules before we started."
        Sara "Wait - you're not seriously going to-"

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p11
        Sara "Oh, my God! You’re hard!"
        Sara "Wh-Why is it so hard?!"
        MC "(Maybe because I want to, fuck you silly?)"
        MC "It’s because you’re looking at it right now. Cocks tend to get hard when they’re given attention."

        scene sara_room_evening_scene2_v1_p12
        MC "Right - what happens now then?"
        Sara "…"
        MC "Is it one more round to decide the winner? Or have you won, since I’m naked?"

        scene sara_room_evening_scene2_v1_p13
        MC "(She’s not listening to me anymore… She’s just staring at my cock.)"
        MC "(I wonder if it is the first time she’s ever seen one. She seems to be extremely interested in it!)"
        Sara "(Wow… It’s so big and hard… I don’t know why, but I really want to touch it.)"

        scene sara_room_evening_scene2_v1_p14
        MC "So… uhh… I’m gonna go and get dressed now."
        if persistent.incest_patch == True:
            MC "last thing we want is, Mom or Dad, walking in on us right now!"
        else:
            MC "Last thing we want is, Linda or Bob, walking in on us right now!"
        $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
        "(Click)(A flash of light fills the room)"
        $ renpy.sound.stop(channel="sound")
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p15
        Sara "(Got it! I couldn’t let this just be a memory!)"
        MC "What the hell, Sara! Did you just take a picture of my dick?"
        Sara "N-No?"
        MC "Yes you did! I can see you taking a photo right now! Delete it!"

        scene sara_room_evening_scene2_v1_p16
        Sara "You’re gonna have to catch me first! Hehe!"
        MC "Come back here!"
        MC "Seriously, Sara! Give me your phone!"
        if persistent.incest_patch == True:
            Sara "I-If you don’t stop chasing me, I’ll call Mom!"
        else:
            Sara "I-If you don’t stop chasing me, I’ll call Linda!"
        scene sara_room_evening_scene2_v1_p17
        MC "Gotcha!"
        Sara "[player_name], stop! Seriously!"
        MC "Delete that picture from your phone!"
        Sara "I’m not talking about this with you!"
        MC "Well, maybe I’ll just have to-"
        Sara "Umm… [player_name]?"

        scene sara_room_evening_scene2_v1_p18
        MC "(Oh shit! My cock pressed right up against her bare belly. It feels so warm against the tip of my cock.)"
        Sara "(Oh, my God! [player_name]’s cock is touching me!)"
        MC "I- I- I’m sorry... I’ll go now!"

        scene sara_room_evening_scene2_v1_p19
        MC "(Crap, that got weird, REALLY fast.)"
        MC "(I hope she’s not too angry at me for pushing my cock against her. I didn’t mean to!)"
        Sara "(That was intense… I have to check this picture out again when he leaves!)"

        scene sara_room_evening_scene2_v1_p20
        Sara "(Wow… It’s sooo big!)"
        Sara "(I have to show Lily! She won’t believe this!)"
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ day_time +=1
        $ sis_nerdy_evening_scene1_v1 = 0
        $ first_sis_nerdy_scene4_v1 = 3
        $ sara_door_open = False
        $ sis_nerdy_school_scene2_v1 = 1
        $ sis_nerdy_evening_scene2a_v1 = 1
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ can_sms2_from_sara = 1
        $ can_lily_scene = False
        $ can_gamepad_sara = True
        $ can_hide_windows = False
        jump corridor_night1

