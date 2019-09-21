image lily_school_day_scene2_v1_p1 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/1.jpg"
image lily_school_day_scene2_v1_p2 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/2.jpg"
image lily_school_day_scene2_v1_p3 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/3.jpg"
image lily_school_day_scene2_v1_p3a = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/3a.jpg"
image lily_school_day_scene2_v1_p4 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/4.jpg"
image lily_school_day_scene2_v1_p5 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/5.jpg"
image lily_school_day_scene2_v1_p6 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/6.jpg"

label lily_school_day_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)

    scene lily_school_day_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    Lily "Ooh! Hi there, [player_name]. Did you come all the way over here, just to visit me?"
    MC "Hey, Lily. I was passing by, so I thought I’d drop in to say hi."
    Lily "I’m very glad that you came by. Things were getting a little boring - and things are always so much more fun when you’re about."

    scene lily_school_day_scene2_v1_p2
    MC "Haha! I guess I’ll take that as a compliment."
    if renpy.loadable("patch.rpy"):
        Lily "How’s your sister? Has she recovered from her freakout, the other day?"
    if not renpy.loadable("patch.rpy"):
        Lily "How’s Sara? Has she recovered from her freakout, the other day?"
    MC "Freakout?"
    Lily "Yeah - when she threw the bottle across the room."
    MC "Oh! Right! Yeah, she’s calmed down now."
    Lily "Good to hear."

    scene lily_school_day_scene2_v1_p3
    Lily "Whoops! Silly me - I’ve gone and dropped my pen."
    Lily "You couldn’t bend down and pick it up for me, could you?"

    menu:
        "Bend down and pick up the pen.":
            scene lily_school_day_scene2_v1_p4
            MC "Yeah, no problem, Lily."
            MC "(There it is there. I wonder why she didn’t just bend down to pick it up herself though!)"

            scene lily_school_day_scene2_v1_p5
            MC "(Holy shit!)"
            MC "(Lily’s spreading her legs on purpose! I can see right up to her panties.)"
            Lily "Ahem!"
            MC "(Uh oh…)"

            scene lily_school_day_scene2_v1_p6
            Lily "Did you find my pen down there? Or did something else… distract you?"
            MC "N-No! I got it here."
            Lily "Cool… So, are you coming back up, then?"
            MC "Uh, yeah!"

            scene lily_school_day_scene2_v1_p2
            MC "I better head on out of here. But I’ll see you around, Lily."
            Lily "See ya later, [player_name]."
            jump after_lily_school_day_scene2_v1_choice
        "Refuse to pick up the pen.":

            scene lily_school_day_scene2_v1_p3a
            MC "Oh look! It rolled under your side of the table. I think it’ll be easier for you to pick it up."
            Lily "Huh?"
            MC "Look - it’s just down on your side of the desk."
            Lily "(Does he not understand? I’m TRYING to show him my panties!)"

            Lily "(Is he seriously this dense?! I’m giving him the PERFECT opportunity! Dozens of guys in this school would KILL to be able to see up my skirt!)"
            MC "Anyway, I better head on out of here. Things to do! I’ll catch you later, Lily."
            Lily "Grr… See you later."
            jump after_lily_school_day_scene2_v1_choice

label after_lily_school_day_scene2_v1_choice:
    $ lily_work_in_progress_v1 = 1
    $ can_lily_work_in_progress = False
    $ lily_school_day_scene1_v1 = 3
    $ lily_school_day_scene2_v1 = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom2_day1
