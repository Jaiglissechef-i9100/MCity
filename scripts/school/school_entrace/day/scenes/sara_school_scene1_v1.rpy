image sis_nerdy_school_scene1_v1_p1 = "images/school/school_entrance/day/scenes/sara_scene1_v1/1.jpg"
image sis_nerdy_school_scene1_v1_p2 = "images/school/school_entrance/day/scenes/sara_scene1_v1/2.jpg"
image sis_nerdy_school_scene1_v1_sara = ("images/school/school_entrance/day/scenes/sara_scene1_v1/sara1.png")


label sis_nerdy_school_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 1 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "(There she is! I wonder what she’s doing out here, by herself.)"
        MC "Hi, Sara. Are you busy right now?"

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Oh! Hey, [player_name]!"
        Sara "I’m ALMOST finished this chapter - then I can drop my notes in to Dr. Roberts and head home."
        MC "Great! See you soon."
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        $ can_hide_windows = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 2 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Heya, Sara. Ready to go?"
        Sara "Not yet, [player_name]. I’ll let you know when I’m free."

        scene sis_nerdy_school_scene1_v1_p2
        Sara "I might be a while, so go and find something to do."
        MC "Fine, catch you later."
        Sara "See ya!"
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        $ can_hide_windows = False
        jump school_entrance_day1


    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 3 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Hi Sara, what’s up? Ready to go?"

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Not quite yet. I’ve still got Chemistry class. I’ll be free after that though."
        MC "Okay, I’ll see you back home."
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 4 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        Sara "(Mumbling) ...and then take the square root… gets us… 12.806…"
        MC "Maths today?"
        Sara "Ugh, yeah. This is melting my brain!"

        scene sis_nerdy_school_scene1_v1_p2
        MC "I take it you’re not ready to come home yet?"
        Sara "Give me another hour or so to crank out this maths homework."
        MC "Why do you keep using the corridor instead of the library?"
        Sara "The library’s too quiet - I need background noise to concentrate."
        MC "Do you at least want a chair?"
        Sara "Nah, I’m comfy like this. Catch you later, [player_name]."
        MC "See ya, Sara."
        $ can_sis_nerdy_school_scene1_v1 = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 5 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Hey there, sexy."

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Shush! Y-You can’t say stuff like that in public!"

        menu:
            "Flatter her.":

                MC "Can’t say stuff like what? Like how absolutely gorgeous you are?"
                Sara "(Oooh… I get so wet when he compliments me like that…)"
                Sara "J-Just save it for when we get home… I don’t want anyone else to see…"
                MC "I’ll see you later on then… beautiful."
                Sara "[player_name]! Haha!"
                $ can_sis_nerdy_school_scene1_v1 = False
                $ can_hide_windows = False
                jump school_entrance_day1
            "Don’t embarrass her in school.":


                MC "Yeah, you’re probably right. I won’t say it anymore."
                Sara "I… I didn’t tell you… to not say it anymore… Just not in public."
                MC "Oh, so you want me to keep telling you that you’re stunningly beautiful?"
                Sara "(Hehe!) N-No… I didn’t say that either…"
                MC "I’ll see you when you get home."
                Sara "See ya [player_name]!"
                $ can_sis_nerdy_school_scene1_v1 = False
                $ can_hide_windows = False
                jump school_entrance_day1

    if can_sis_nerdy_school_scene1_v1 == False:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        show screen school_entrance_day_notclickable
        $ can_hide_windows = False
        MC "I've already talked to her."
        jump school_entrance_day1