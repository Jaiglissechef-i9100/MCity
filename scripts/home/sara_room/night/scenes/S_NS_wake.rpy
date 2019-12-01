label SR2_NSwake_label:
    MC "(I don’t know what I’m so worried about! I’ve already caught Sara, trying to take pictures of my cock while I’m asleep.)"
    MC "(What’s the worst that could happen?)"
    MC "(Alright, here goes nothing…)"
    MC "Psst… Sara…"
    Sara "Zzz..."
    MC "Sara?"
    Sara "Hmm?"

    scene sara_room_night_sleeping2_WakeUp1

    Sara "(Yawwwnn!)"
    Sara "Huh? [player_name]?"
    Sara "Ugh… What time is it?"
    MC "It’s the middle of the night."

    scene sara_room_night_sleeping2_WakeUp2

    Sara "Why’d you wake me up? What’s wrong?"
    MC "Nothing’s wrong."
    Sara "And why is my duvet all crumpled up at the bottom of my bed?"
    MC "Err… You must have wriggled out of it while you were sleeping."
    Sara "Huh…"
    MC "Anyway, I just had to see you again. I couldn’t get what we did, off my mind. I was wondering if we could do it again."

    scene sara_room_night_sleeping2_WakeUp3

    Sara "(He wants another blowjob?)"
    Sara "(I guess it WAS pretty fun.)"
    $ renpy.block_rollback()
    call screen S_NS_wake_scr

label SNS_wake_5:
    scene sara_room_night_sleeping2_WakeUp2

    Sara "Sure, why not."
    MC "Awesome! Could you bend over?"
    if persistent.incest_patch == True:
        MC "Make sure to keep your voice down, by the way. I don’t want to wake up Mom and Dad."
    else:
        MC "Make sure to keep your voice down, by the way. I don’t want to wake up Linda and Bob."

    scene sara_room_night_sleeping2_WakeUp3

    Sara "Suur- Wait? Bend over? Like… sex? I- I’m not ready for that, [player_name]!"
    MC "Relax. I promise I won’t do anything that you’re not ready for."
    Sara "D-Do you still need me to bend over?"
    MC "Yeah - just get on all fours."
    Sara "Promise you won’t fuck me yet? It’s just a bit… fast for me."
    MC "I promise. I just want to use your thighs."
    Sara "O-Okay..."

    scene sara_room_night_sleeping2_WakeUp4

    Sara "J-Just like this?"
    Sara "(My heart is pounding so fast right now! I know this isn’t sex, but it feels like it’s getting really close to it.)"
    MC "That’s perfect, Sara."

    scene sara_room_night_sleeping2_WakeUp5

    MC "Just hold still, and let ME do all the work."
    Sara "O-Okay, [player_name]…"
    MC "(She looks so cute in her little pink underwear.)"

    scene sara_room_night_sleeping2_WakeUp6

    MC "I’m going to push my cock forward now, Sara."
    Sara "Mmm hmm…"
    Sara "(Why am I so nervous? I wasn’t this scared when I was giving him a blowjob!)"
    Sara "(Perhaps it’s just how close his cock is, to my pussy.)"

    scene sara_room_night_sleeping2_WakeUp7

    Sara "Ooh…."
    MC "Are you okay?"
    scene sara_room_night_sleeping2_WakeUp7anim
    Sara "Y-Yeah… It just rubbed against my clitoris through my panties…"
    MC "Sorry."
    Sara "Don’t apologise… It was nice."

    scene sara_room_night_sleeping2_WakeUp8

    MC "Ahh…"
    MC "(Her warm thighs are wrapped, either side of my cock. This feels incredible!)"
    MC "(I can’t wait to fuck her pussy, some day.)"
    Sara "Ohh… Ah…. Mmm…"
    Sara "(I never imagined, dry humping could be this good!)"

    scene sara_room_night_sleeping2_WakeUp9

    MC "Ugh! Are you enjoying this, Sara?"
    Sara "Ah! Ahh! It’s sooo good…"
    Sara "F-Faster!"

    scene sara_room_night_sleeping2_WakeUp10

    Sara "Oh… yes! Yes! Oooohhhhh!"
    MC "(Wow, she’s really getting into this!)"
    MC "Ahh... "
    MC "I’m not gonna last much longer, Sara."

    scene sara_room_night_sleeping2_WakeUp11

    Sara "Ahh! It’s okay! Ugh! Ohhh! C-Cum wherever you want!"
    scene sara_room_night_sleeping2_WakeUp11anim
    if persistent.incest_patch == True:
        MC "(She’s getting pretty loud. I hope Mom and Dad don’t hear this!)"
    else:
        MC "(She’s getting pretty loud. I hope Linda and Bob don’t hear this!)"
    window hide
    menu:
        "Cum on her back.":
            scene sara_room_night_sleeping2_WakeUp12a

            MC "Oh God… yes… Ugh!"
            MC "Ahhhh…."
            Sara "(Damn… I wish he’d finished in my mouth again…)"
            Sara "(I loved the hot salty taste of it.)"

            scene sara_room_night_sleeping2_WakeUp12aa

            MC "Hnnnnnggg! Gaaaahhh!"
            MC "Ugh! Yes!"
            MC "Phew… That was amazing, Sara. Thank you, so much."
            Sara "No problem, [player_name]."
            Sara "Umm… could you get me some tissues before you go back to bed? I have some cleaning to do."
            MC "Err… sure. Sorry about that. Haha!"
            $ renpy.music.stop(channel="music1", fadeout=1)
            scene black
            $ renpy.sound.play("sfx/door_open.mp3")
            $ renpy.pause(1, hard = True)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_sis_nerdy_night_sleeping1_v1 = False
            jump corridor_morning1
        "Finish in her mouth.":
            scene black

            MC "Open wide, Sara. I’ll finish in your mouth."
            Sara "(YAY!)"
            Sara "Ahhh…."

            scene sara_room_night_sleeping2_WakeUp12bb

            MC "Hnnng! Oh God! Yes!"
            MC "(Her mouth is so warm and wet, around the tip of my cock!)"
            Sara "(Gulp Gulp!)"
            MC "Ahhhh…. Fuck…."

            scene black

            MC "Phew… That was amazing. Thank you, so much."
            Sara "You’re welcome [player_name]. Goodnight."
            MC "Sleep tight, Sara."
            Sara "You too, [player_name]."
            $ renpy.music.stop(channel="music1", fadeout=1)
            scene black
            $ renpy.sound.play("sfx/door_open.mp3")
            $ renpy.pause(1, hard = True)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_sis_nerdy_night_sleeping1_v1 = False
            jump corridor_morning1
