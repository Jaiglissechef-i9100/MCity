image CR4_AS2_p1 = "images/cloth_shop/room1/day/scenes/CR4_AS2/1.jpg"
image CR4_AS2_p2 = "images/cloth_shop/room1/day/scenes/CR4_AS2/2.jpg"
image CR4_AS2_p3 = "images/cloth_shop/room1/day/scenes/CR4_AS2/3.jpg"
image CR4_AS2_p4 = "images/cloth_shop/room1/day/scenes/CR4_AS2/4.jpg"
image CR4_AS2_p5 = "images/cloth_shop/room1/day/scenes/CR4_AS2/5.jpg"
image CR4_AS2_p6 = "images/cloth_shop/room1/day/scenes/CR4_AS2/6.jpg"
image CR4_AS2_p7 = "images/cloth_shop/room1/day/scenes/CR4_AS2/7.jpg"
image CR4_AS2_p8 = "images/cloth_shop/room1/day/scenes/CR4_AS2/8.jpg"
image CR4_AS2_p9 = "images/cloth_shop/room1/day/scenes/CR4_AS2/9.jpg"
image CR4_AS2_p10 = "images/cloth_shop/room1/day/scenes/CR4_AS2/10.jpg"
image CR4_AS2_p11 = "images/cloth_shop/room1/day/scenes/CR4_AS2/11.jpg"
image CR4_AS2_p12 = "images/cloth_shop/room1/day/scenes/CR4_AS2/12.jpg"
image CR4_AS2_p13 = "images/cloth_shop/room1/day/scenes/CR4_AS2/13.jpg"
image CR4_AS2_p14 = "images/cloth_shop/room1/day/scenes/CR4_AS2/14.jpg"
image CR4_AS2_p15 = "images/cloth_shop/room1/day/scenes/CR4_AS2/15.jpg"
image CR4_AS2_p16 = "images/cloth_shop/room1/day/scenes/CR4_AS2/16.jpg"
image CR4_AS2_p17 = "images/cloth_shop/room1/day/scenes/CR4_AS2/17.jpg"
image CR4_AS2_p18 = "images/cloth_shop/room1/day/scenes/CR4_AS2/18.jpg"


default CR4_AS2 = False

label CR4_AS2_label:
    if CR4_AS2 == 3:
        hide screen map_button
        show screen cloth_shop_robber_screen
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen cloth_shop_robber_screen
        jump cloth_shop_open_label
    else:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR4_AS2_p1 with dissolve

        Caroline "I said, get the hell out of here!"
        MC "(Huh? Who’s Caroline screaming at?)"
        MC "(Aww, nuts. I recognise this douchebag - it’s Caroline’s dickhead ex-boyfriend I met in the nightclub! What was his name? Charles or something like that?)"

        scene CR4_AS2_p2

        Charles "I ain’t leaving here without that money!"
        Caroline "Okay, two points, Charles: First of all, you’re not getting a single penny of my money; and secondly, if you refuse to leave I’m going to call the cops."
        MC "(What the hell have I walked in on?)"

        scene CR4_AS2_p3

        Charles "Listen here, you bitch. That nightclub owner is after me for causing damage to their bar."
        Charles "If I don’t come up with two grand by the end of the week, they’ve threatened to take me to court!"
        Caroline "Tough shit! Not my problem!"

        scene CR4_AS2_p4

        Charles "Oh yeah? I think it IS your problem. Because I wasn’t the one who smashed up that bar."
        Charles "It was that dorky little creep you were hanging out with. The one who ASSAULTED me!"
        Caroline "Fuck off, Charles. We both know that’s not true. At least a dozen people saw you behaving like a twat that night."
        Charles "I’m going to-"

        scene CR4_AS2_p5

        Caroline "Enough! You’re not taking any of MY money to fix your own fucked up life!"
        MC "(I was considering intervening… but it looks like Caroline is holding her own!)"
        Charles "But it-"

        scene CR4_AS2_p6

        Caroline "Now, get the fuck out of my shop, before I shove a wooden pole up your ass and use you as a mannequin to display my clothes!"
        Charles "Grr…"
        Charles "(I’ll get that money out of you yet, you ignorant bitch!)"

        scene CR4_AS2_p7

        Charles "I’m getting that money, Caroline. I’m not letting you and that fucking little twerp screw me over."
        Caroline "Out. Now."

        scene CR4_AS2_p8

        Charles "Oh, look who just showed up."
        MC "(Fuck - he noticed me.)"
        Caroline "Leave [player_name] out of this. This is between you and me, Charles."

        scene CR4_AS2_p9

        Charles "Pfft… Get outta my way, dick."
        MC "Ooof!"
        MC "(Asshole…)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_AS2_p10

        Caroline "Grrr… What a fucking…"
        MC "What the heck was that about? How did he get in here?"
        Caroline "The asshole just barged his way into the back of the shop. I couldn’t stop him."

        scene CR4_AS2_p11

        MC "Shit! He didn’t hurt you, did he?"
        Caroline "No; but he just stormed in here and started looking for money. Thankfully I had it locked away."
        MC "Have you called the police?"

        scene CR4_AS2_p12

        Caroline "And what good would that do?! They’d close my business down for a day or two, while they gather evidence!"
        Caroline "I’d probably end up LOSING more revenue than Charles wanted off me in the first place!"
        MC "O-Okay! How about we calm down and talk about this, to see what we can do?"
        Caroline "I am calm!"
        MC "Umm… Your fist?"

        scene CR4_AS2_p13

        Caroline "Shit… Sorry! I was still caught up in the moment, there. That asshole just set me on edge."
        MC "Relax, Caroline. I understand. It’s okay."
        MC "What can I do to help?"

        scene CR4_AS2_p14

        Caroline "Nothing, I’m fine. I said ‘no’ to the bastard. He’s not getting any money from me."
        Caroline "Thanks for being there though. If you weren’t around he might have been brave enough and give me a black eye. (Again…)"
        MC "Shit. Well, I’m just glad you’re safe."

        scene CR4_AS2_p15

        Caroline "Listen, I don’t want you getting involved in this, [player_name]. Can you promise me that?"
        MC "Why? I was there at the nightclub. I saw what happened!"
        Caroline "I can handle Charles. He left with his tail between his legs today. He won’t show his face around here again for a while."

        scene CR4_AS2_p16

        MC "Well… if you need anything can you AT LEAST promise to call me?"
        Caroline "I’ll be fine."
        MC "Please? I don’t want you dealing with this dickhead by yourself. I mean… what if he attacked you or tried to rape you in here?!"

        scene CR4_AS2_p17

        Caroline "*Sigh*"
        Caroline "Alright, I promise I’ll call you if things ever get out of hand."
        MC "Thanks, Caroline. I appreciate it."

        scene CR4_AS2_p18

        Caroline "Hey, [player_name]."
        MC "Yeah?"
        Caroline "Do you seriously think I couldn’t take that dick on in a fight?"
        MC "Haha! I’m sure you could kick his ass, Caroline."
        Caroline "I reckon I could as well. Catch you later, [player_name]."

        $ CR4_ES1_q8 = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ CR4_AS2 = 3
        jump map_label

