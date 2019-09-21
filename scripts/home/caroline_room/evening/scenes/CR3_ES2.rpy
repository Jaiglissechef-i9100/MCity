image CR3_ES2_p1 = "/images/home/caroline_room/evening/scenes/CR3_ES2/1.jpg"
image CR3_ES2_p2 = "/images/home/caroline_room/evening/scenes/CR3_ES2/2.jpg"
image CR3_ES2_p3 = "/images/home/caroline_room/evening/scenes/CR3_ES2/3.jpg"
image CR3_ES2_p4 = "/images/home/caroline_room/evening/scenes/CR3_ES2/4.jpg"
image CR3_ES2_p5 = "/images/home/caroline_room/evening/scenes/CR3_ES2/5.jpg"
image CR3_ES2_p6 = "/images/home/caroline_room/evening/scenes/CR3_ES2/6.jpg"
image CR3_ES2_p7 = "/images/home/caroline_room/evening/scenes/CR3_ES2/7.jpg"
image CR3_ES2_p8 = "/images/home/caroline_room/evening/scenes/CR3_ES2/8.jpg"
image CR3_ES2_p9 = "/images/home/caroline_room/evening/scenes/CR3_ES2/9.jpg"
image CR3_ES2_p10 = "/images/home/caroline_room/evening/scenes/CR3_ES2/10.jpg"
image CR3_ES2_p11 = "/images/home/caroline_room/evening/scenes/CR3_ES2/11.jpg"
image CR3_ES2_p12 = "/images/home/caroline_room/evening/scenes/CR3_ES2/12.jpg"
image CR3_ES2_p13 = "/images/home/caroline_room/evening/scenes/CR3_ES2/13.jpg"
image CR3_ES2_p14 = "/images/home/caroline_room/evening/scenes/CR3_ES2/14.jpg"
image CR3_ES2_p15 = "/images/home/caroline_room/evening/scenes/CR3_ES2/15.jpg"
image CR3_ES2_p16 = "/images/home/caroline_room/evening/scenes/CR3_ES2/16.jpg"
image CR3_ES2_p17 = "/images/home/caroline_room/evening/scenes/CR3_ES2/17.jpg"

label CR3_ES2_label:

    if CR3_ES2_can == False:
        hide screen map_button
        show screen caroline_room_evening
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen caroline_room_evening
        jump caroline_room_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR3_ES2_p1 with dissolve
        $ can_hide_windows = True

        MC "(Heh... I always walk in at the best moments. Just look at that view!)"
        MC "(I can see all the way up to her panties. God, I’d love to just - tear them off her - right now!)"

        scene CR3_ES2_p2

        MC "Hey Caroline, what’s up?"
        Caroline "…"
        MC "Hello? Caroline?"

        scene CR3_ES2_p3

        Caroline "Hmm? Oh! Sorry, I’m just in the middle of something, here. Give me two seconds, and I’ll be with you."
        MC "No problem, Caroline. Take your time."
        MC "(It must be something really engrossing! I was standing right beside her, and it was like, she didn't even see me!)"

        scene CR3_ES2_p4

        Caroline "Sorry about that. What’s up?"
        MC "Well, I just wanted to try out our - new and improved - deal."
        Caroline "Oh yeah? What were you thinking of doing?"

        scene CR3_ES2_p5

        MC "I was hoping to kiss you on the lips - for a change. They’re included in the package now, right?"
        Caroline "Hehe - that’s such an ugly way to put it. Yes, my lips are included in our new deal."
        MC "Great!"

        scene CR3_ES2_p6

        Caroline "So, what do you want to do to me? Lie down beside me, on the bed and make out?"
        Caroline "Or would you prefer to - pin me - against my bedroom wall and ravage my neck?"
        Caroline "Or perhaps..."

        scene CR3_ES2_p7

        Caroline "...you’d like me to seize the initiative - and go on top."
        MC "Mmm... I’d like that very much."
        Caroline "I hope you enjoy this new deal, as much as I do."

        scene CR3_ES2_p8

        Caroline "(Whispered) You really have no idea, how lucky a guy you are."
        Caroline "(Whispered) My ex would LITERALLY kill to have what you have with me."
        MC "(That probably says a lot more about Caroline’s taste in men, than it does about her!)"

        scene CR3_ES2_p9

        Caroline "Mmm!"
        MC "(Oh wow! She’s an amazing kisser!)"
        MC "(Why couldn’t THIS have been included in the original deal? I missed out on weeks of - great making out!)"

        scene CR3_ES2_p10

        MC "Mmm..."
        Caroline "(Hehe. I love hearing a guy moan, when I kiss him. It’s just-)"
        "*Bzzt Bzzt*"

        scene CR3_ES2_p11

        MC "Huh? What’s that noise?"
        Caroline "Gah! Ignore it. It’s my stupid phone."
        "*Bzzt Bzzt Bzzt*"
        MC "Geez! Aren’t you going to answer it?"
        Caroline "No - wait!"
        MC "Huh? They hung up anyway."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music2", loop=True, fadein = 2)
        scene CR3_ES2_p12

        MC "Wait..."
        MC "Huh?"
        if renpy.loadable("patch.rpy"):
            MC "Jesus Christ! Who the hell is that, Sis?"
        else:
            MC "Jesus Christ! Who the hell is that, Caroline?"

        scene CR3_ES2_p13

        Caroline "I- Uh- It’s nothing!"
        MC "What kind of dickhead is calling you - and sending creepy messages?"
        Caroline "It’s no one - seriously!"

        scene CR3_ES2_p14

        MC "You clearly know them. Who is it? Are they bullying you?"
        Caroline "*Sigh* It’s my most recent ex. He’s a dickhead. He’s been spamming me with calls and texts, since that night out."
        MC "Jesus! You should really block his number."

        scene CR3_ES2_p15

        Caroline "I thought about doing that - but then, if he ever does something to hurt me, I won’t have the evidence."
        Caroline "At least this way, I’ll have a string of text messages I can always take to the police, if required."
        MC "That makes sense. Good call, Caroline. Do you need me to help, in any way?"

        scene CR3_ES2_p16

        Caroline "Haha! You? Help me? Hahaha!"
        MC "Oof!"
        Caroline "You couldn’t even beat ME in a fight, let alone my ex."

        scene CR3_ES2_p17

        Caroline "Thanks for the offer, though. Don’t worry about me - I’ll handle this one."
        MC "Okay. As long as you’re absolutely sure."
        Caroline "I’ll be fine. Catch you later on, [player_name]."
        MC "See ya, Caroline."

        $ CR3_ES2_can = False

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump caroline_room_morning1
