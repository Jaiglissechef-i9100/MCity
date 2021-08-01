image SR2_AS1_p1 = "images/school/school_entrance/day/scenes/SR2_AS1/1.jpg"
image SR2_AS1_p2 = "images/school/school_entrance/day/scenes/SR2_AS1/2.jpg"
image SR2_AS1_p3 = "images/school/school_entrance/day/scenes/SR2_AS1/3.jpg"
image SR2_AS1_p4 = "images/school/school_entrance/day/scenes/SR2_AS1/4.jpg"
image SR2_AS1_p5 = "images/school/school_entrance/day/scenes/SR2_AS1/5.jpg"

label SR2_AS1_label:
    if can_SR2_AS1 == False:
        $ clickable = False
        show screen school_entrance_day
        MC "I've already talked with her."
        $ clickable = True
        jump school_entrance_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS1_p1 with dissolve

        MC "(There’s Sara! It looks like she’s deep in concentration. I wonder what could be so important?)"
        MC "Hey, Sara! what are you reading?"
        Sara "…"
        MC "(She didn’t seem to notice me. I’ll try again.)"
        MC "Hello, Sara!"

        scene SR2_AS1_p2

        Sara "Huh? Oh! Hey, [player_name]. What’s up?"
        MC "What are you reading?"
        Sara "Oh, I’m just doing some last-minute cramming for my history test."
        MC "What period are you studying?"
        Sara "Syria during the Cold War."
        MC "Huh, I remember doing that module. Except, it was Syria and Egypt during the Cold War."

        scene SR2_AS1_p3

        Sara "Oh shit! You’re right! I forgot about Egypt!"
        MC "Well, at least you’ve studied Syria. Just focus on Egypt now, and you should be fine."
        Sara "I haven’t studied ANYTHING yet! I only opened my book this morning!"
        MC "What?!"

        scene SR2_AS1_p4

        Sara "I kinda stayed up late last night playing some games. Haha…"
        MC "But… What about the test?"
        Sara "I’ll be fine, right?"
        MC "What was the United Arab Republic?"

        scene SR2_AS1_p2

        Sara "Umm… Was it an ally of Syria and Egypt?"
        MC "It WAS Syria and Egypt. They joined together and formed a unified country for a few years."

        scene SR2_AS1_p5

        Sara "Aww nuts. I’m so screwed..."
        MC "(This isn’t like Sara, at all! She used to be, top of her class!)"
        MC "(I guess she’s just been distracted by video games. She really needs to get back on track and focus. Hopefully she’ll pass this test.)"
        MC "Good luck, I guess. Hope it goes well for you."
        Sara "(Gulp) Thanks, [player_name]."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ can_SR2_AS1 = False
        jump school_entrance_morning1

