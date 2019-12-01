image headmaster_S1_p1 = "images/school/headmaster_room/morning/headmaster_S1/1.jpg"
image headmaster_S1_p2 = "images/school/headmaster_room/morning/headmaster_S1/2.jpg"
image headmaster_S1_p3 = "images/school/headmaster_room/morning/headmaster_S1/3.jpg"
image headmaster_S1_p4 = "images/school/headmaster_room/morning/headmaster_S1/4.jpg"
image headmaster_S1_p5 = "images/school/headmaster_room/morning/headmaster_S1/5.jpg"
image headmaster_S1_p6 = "images/school/headmaster_room/morning/headmaster_S1/6.jpg"
image headmaster_S1_p7 = "images/school/headmaster_room/morning/headmaster_S1/7.jpg"

label headmaster_S1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    if persistent.incest_patch == True:
        $ Headmaster_name = __("Headmaster")
    else:
        $ Headmaster_name = __("Headmaster")

    $ clickable = False
    if day_time == 1:
        show screen school_corridor3_morning
    if day_time == 2:
        show screen school_corridor3_day

    MC "(Well, this is the headmaster’s office. I suppose I should knock before going in. I’ve only seen this guy a couple of times before. He’s a bit of a recluse - students hardly ever see him walking the corridors.)"
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*KNOCK KNOCK*"
    $ renpy.music.stop(channel="sound")

    Headmaster "Yo yo! The door’s open!"
    hide screen school_corridor3_morning
    hide screen school_corridor3_day
    $ clickable = True

    scene headmaster_S1_p1 with dissolve
    $ can_hide_windows = True
    Headmaster "Wassup, my man? I recognise your face, but I can’t put a name to it."
    MC "It’s [player_name], sir."
    Headmaster "Ahh, [player_name]. Now WHY does that ring a bell when I hear it. Hmm..."

    scene headmaster_S1_p2

    Headmaster "You didn’t win the school any awards, did ya?"
    MC "No, sir."
    Headmaster "No debating competitions, no sports trophies?"
    MC "Umm, no. I’m honestly not that into either of those."

    scene headmaster_S1_p3

    Headmaster "[player_name]. [player_name], [player_name]..."
    Headmaster "AHA! Back up a second - you’re that kid who asked Celia out, ain’tcha?"
    MC "(Oh God, is THAT the only reason people know my name in this school?!)"
    MC "Yeah… that was… me, sir."

    scene headmaster_S1_p4

    Headmaster "Ouch! I feel for you, boy. I really do."
    Headmaster "Geez, that’s a real doozy. You know what - props to you, son. Forget what everyone else says about you being a weirdo."
    MC "What?! Everyone’s saying I’m a weirdo?!"
    Headmaster "I said forget about it! In my eyes, you’ve got cojones of pure iron!"

    scene headmaster_S1_p5

    Headmaster "Seriously, you just marched right up to her and declared your love. I mean, what chance did you have? One in a million?"
    MC "I guess, in hindsight I-"
    Headmaster "You were like Han fuckin’ Solo doing that asteroid belt shit."
    MC "(I’ve never seen any of the other teachers wearing as much jewelry as the headmaster does. He must earn a LOT more than them!)"

    scene headmaster_S1_p6

    Headmaster "So yeah - Major respect for you."
    MC "Umm, thank you, sir?"
    Headmaster "*Ahem* I guess I do have to warn you, not to make any… uh… sexual advances on any other teachers."
    MC "I’ll try not to, sir."
    Headmaster "Oh, and one more thing: The school counsellor, Judy, is keeping me up to date on your progress with her."

    scene headmaster_S1_p7

    Headmaster "I know taking these therapy sessions with Judy can be embarrassing, especially with all your gossiping peers."
    Headmaster "I just wanted to urge you to continue seeing Judy. Don’t slack off on your mental health. Taking care of your mind is just as important as exercising."
    Headmaster "Now, I’ve taken up enough of your time, and you should probably be in class. See ya around, Iron Cojones."

    $ headmaster_S1 = False

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump school_corridor3_morning1
