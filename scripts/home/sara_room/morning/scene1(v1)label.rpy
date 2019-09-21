image scene1_v1p1 = "images/home/sara_room/morning/Scene1_v1/1.jpg"
image scene1_v1p2 = "images/home/sara_room/morning/Scene1_v1/2.jpg"
image scene1_v1p3 = "images/home/sara_room/morning/Scene1_v1/3.jpg"
image scene1_v1p4 = "images/home/sara_room/morning/Scene1_v1/4.jpg"
image after_sis_nerdy_scene1_v1p1 = "images/home/sara_room/morning/Scene1_v1/after_sara_scene1.png"

label scene1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene1_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Sara’s engrossed in one of her video games again!)"
    MC "(If she doesn’t hurry up and get ready, she’s gonna be late for her first class.)"
    MC "Hey, you almost ready to go?"

    scene scene1_v1p2

    MC "(Huh, I don’t think she heard me, with the headphones on.)"
    MC "Hey! Sara!"
    Sara "Huh?! Oh! Hey, [player_name]!"
    MC "You’re shouting!"
    Sara "What’s up?"
    MC "We need to leave for school in five minutes!"

    scene scene1_v1p3
    Sara "It’s okay, I’ll be done in like… a couple of minutes."
    MC "We both know that’s not true."
    MC "I can CLEARLY see, you’ve only just started the round!"

    scene scene1_v1p4
    if renpy.loadable("patch.rpy"):
        Sara "Aww, c’mon [player_name]! You’re not my dad! Hehe!"
    if not renpy.loadable("patch.rpy"):
        Sara "Aww, c’mon [player_name]! You’re not Bob! Hehe!"
    Sara "Why do you care if I’m a little bit late to school? I’m almost top of the class, anyway."
    MC "Almost top? Weren’t you THE top, two years ago? You’re slipping, Sara."

    scene scene1_v1p2
    Sara "Grr… Fine! I’ll log off."
    Sara "Say... About Mrs. Celia, the other day..."

    scene scene1_v1p3
    MC "I’d rather not talk about it."
    Sara "Oh… sorry. I understand."
    MC "Nah, you don’t need to apologise. You were right - I should have listened to your advice."
    MC "I’ll try to do that more in future, I promise."

    scene scene1_v1p4
    Sara "Want to walk to school together?"
    MC "You’ll need to hurry your ass up! I’ve been ready to leave for the past ten minutes!"
    $ sis_nerdy_scene1_v1= 2
    $ after_sis_nerdy_scene1_v1 = 2
    $ next_day = False
    $ can_morning_sara_scenes = False
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump sister_nerdy_morning1

label after_sis_nerdy_scene1_v1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show after_sis_nerdy_scene1_v1p1
    $ can_hide_windows = False
    MC "I've already talked to her."
    jump sister_nerdy_morning1

label next_day_after_sis_nerdy_scene1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene1_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Sigh… Computer games again?!)"
    MC "(Her grades are going to keep dipping if she doesn’t apply herself.)"
    MC "(And even if she does get good grades; what kind of employer is going to want a lazy worker who’s always late?)"

    scene scene1_v1p2
    MC "Sara! You’re going to be late AGAIN!"
    Sara "Just… five more minutes. I’ve almost earned my daily loot crate!"
    MC "Can you not do this when you get home, after school?"
    Sara "Umm…"

    scene scene1_v1p3
    Sara "But if I don’t open the loot crate now, I’ll be wondering what’s in it ALL DAY!"
    Sara "I’ll just be distracted at school, and not learn anything. So I REALLY need to get it out of the way now."
    MC "That’s… a terrible excuse. You know that?"
    Sara "Hehe, yeah…"
    $ scene1_v1q1a1 = True
    $ scene1_v1q1a2 = True
    $ scene1_v1q1a3 = True
    jump scene1_v1q1

label scene1_v1q1:
    scene scene1_v1p4
    menu:
        "Have you done your homework?" if scene1_v1q1a1 == True:

            MC "Have you at least done your homework?"
            Sara "Yeah! Most of it…"
            MC "What do you mean, most of it?!"
            Sara "Relax! I can finish it off in the school library, over lunch."
            $ scene1_v1q1a1 = False
            jump scene1_v1q1

        "What time did you go to bed at last night?" if scene1_v1q1a2 == True:

            MC "What time did you go to bed at last night?"
            Sara "Umm… Let’s see… I did three matches… then two more capture the flag games…"
            Sara "2AM?"
            MC "2AM?! On a school night?!"
            Sara "Hehe, yeah. I’m a little tired…"
            MC "(She really needs to go to bed earlier.)"
            $ scene1_v1q1a2 = False
            jump scene1_v1q1

        "{color=#00ff00}Up to anything exciting today?{/color}" if scene1_v1q1a3 == True:

            MC "Are you up to anything exciting today?"
            Sara "No, nothing interesting planned. I’ll probably just be hanging out with Lily."
            Sara "How about you?"
            MC "Aside from slowly trying to regain some self-esteem and get my life back on track?"
            Sara "You’re overdramatic."
            MC "It’s melodramatic actually."
            Sara "Really? Geez… maybe I shouldn’t be skipping English Literature."
            MC "You’re skipping literature?!"
            $ scene1_v1q1a3 = False
            jump after_scene1_v1q1

label after_scene1_v1q1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene scene1_v1p4
    Sara " Oops! Look at the time - I better get dressed quickly! I’m gonna be late!"
    $ sis_nerdy_scene1_v1 = 3
    $ after_sis_nerdy_scene1_v1 = 3
    $ drawer_sis_nerdy = 1
    $ can_morning_sara_scenes == False
    $ can_sara_scene3_v1 = False
    $ next_day = False
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2, fadeout=2)
    $ can_hide_windows = False
    jump corridor_morning1
