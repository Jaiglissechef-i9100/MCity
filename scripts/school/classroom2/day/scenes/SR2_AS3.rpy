image SR2_AS3_p1 = "images/school/classroom2/day/scenes/SR2_AS3/1.jpg"
image SR2_AS3_p2 = "images/school/classroom2/day/scenes/SR2_AS3/2.jpg"
image SR2_AS3_p3 = "images/school/classroom2/day/scenes/SR2_AS3/3.jpg"
image SR2_AS3_p4 = "images/school/classroom2/day/scenes/SR2_AS3/4.jpg"
image SR2_AS3_p5 = "images/school/classroom2/day/scenes/SR2_AS3/5.jpg"

label SR2_AS3_label:
    if can_SR2_AS3 == False:
        show screen classroom2_day
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        jump classroom2_morning1
    if not SR2_vibrator in inventory.items:
        show screen classroom2_day
        $ clickable = False
        MC "I still did not buy that vibrator."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS3_p1 with dissolve

        MC "*Psst! Sara… I got it."
        Sara "Huh?"
        MC "I went to the sex shop in the evening and got you the vibrator. It’s in my roo-"

        scene SR2_AS3_p2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music2", loop=True, fadein = 2)

        Sara "VIBRATOR!?"
        Sara "You actually got me a vibrator?!"
        MC "(Shit! She’s too loud! If she isn’t careful; someone will hear her!)"
        MC "(I don’t know why she sounds so surprised! We TALKED about this!)"

        scene SR2_AS3_p3

        MC "Shush! If you’re not careful, then half your classmates will hear you!"
        Sara "(Oops! I didn’t think of that… I was just so shocked, that it never occured to me.)"
        MC "Can I take my hand off now? Or are you going to announce to everyone that you gave me a blowjob too?"
        Sara "Mmm hmm..."

        scene SR2_AS3_p4

        Sara "S-Sorry, I was just… a little taken aback."
        MC "That's okay. I'll see you later on. Are you still good to meet in my room tonight?"
        MC "I’ll be able to give you it when we meet then."

        scene SR2_AS3_p5

        Sara "(Gulp) O-Okay, I’ll be in your bedroom."
        if renpy.loadable("patch.rpy"):
            MC "It’s probably best if you wait until Mom goes to sleep."
        else:
            MC "It’s probably best if you wait until Linda goes to sleep."
        Sara "Yeah, I’ll see you then."
        if renpy.loadable("patch.rpy"):
            MC "You should probably look for a good place to hide it too. I don’t want Mom finding it when she cleans your room."
        else:
            MC "You should probably look for a good place to hide it too. I don’t want Linda finding it when she cleans your room."
        Sara "Don’t worry, I know a few places she won’t look."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ can_SR2_AS3 = False
        $ SR2_NS2 = True
        $ S_N_inbed = False
        jump classroom2_morning1