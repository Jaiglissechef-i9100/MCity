image SR2_weekend_sunbed_p1 = "images/Weekend_Events/Sara/R2/SunBed/1.jpg"
image SR2_weekend_sunbed_p2 = "images/Weekend_Events/Sara/R2/SunBed/2.jpg"
image SR2_weekend_sunbed_p3 = "images/Weekend_Events/Sara/R2/SunBed/3.jpg"
image SR2_weekend_sunbed_p4 = "images/Weekend_Events/Sara/R2/SunBed/4.jpg"
image SR2_weekend_sunbed_p5 = "images/Weekend_Events/Sara/R2/SunBed/5.jpg"
image SR2_weekend_sunbed_p6 = "images/Weekend_Events/Sara/R2/SunBed/6.jpg"

label SR2_SunBed_label:
    if SR2_after_sunbed == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "We've already been there."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "How about we chill out on the lounge chairs for a while?"
        Sara "Cool. Works for me."
        Sara "Ahh! There’s a couple of free ones over there! Hurry! Follow me!"

        scene SR2_weekend_sunbed_p1

        MC "Ahh… These are perfect. You got a great spot."
        MC "Most of the other chairs were stuck in the shade."
        Sara "Yeah, when you come here as often as I do, you learn where the best spots are!"
        Sara "We’ll get - at least - two good hours of sunlight here."

        scene SR2_weekend_sunbed_p2

        MC "Awesome."
        Sara "Mmm… Do you mind if I doze off for a few minutes?"
        MC "Do whatever you want, Sara. Just chill out and relax."
        Sara "Thanks, [player_name]."

        scene SR2_weekend_sunbed_p3

        MC "(Damn, I never realised how thin her swimsuit was, until now.)"
        MC "(Just look at how little it leaves to the imagination, between her thighs.)"
        MC "(Another half inch, and I’d be able to see her pussy!)"

        scene SR2_weekend_sunbed_p4

        Sara "Are you not going to sleep too?"
        MC "I was just admiring how beautiful you are."
        Sara "[player_name]…"
        Sara "You’re gonna make me blush in public."
        Sara "Can… Can I hold your hand while I sleep?"
        MC "Of course, Sara."

        scene SR2_weekend_sunbed_p5

        MC "(She’s so adorable. I love how she thought she needed to ask my permission.)"
        MC "(Her hands are so soft against mine. I could very easily fall asleep right now too.)"
        MC "Sara, I love you."
        Sara "..."

        scene SR2_weekend_sunbed_p6

        MC "Sara?"
        Sara "Zzz…."
        MC "(Aww… it looks like she’s so content, that she has gone straight to sleep.)"
        MC "Sweet dreams, Sara."
        $ SR2_after_sunbed = True
        $ can_hide_windows = False
        jump swimming_poll_label

