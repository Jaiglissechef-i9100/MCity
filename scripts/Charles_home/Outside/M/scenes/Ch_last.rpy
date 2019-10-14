image Ch_last_p1 = "/images/charles_home/outside/M/scenes/Ch_last/1.jpg"
image Ch_last_p2 = "/images/charles_home/outside/M/scenes/Ch_last/2.jpg"
image Ch_last_p3 = "/images/charles_home/outside/M/scenes/Ch_last/3.jpg"
image Ch_last_p4 = "/images/charles_home/outside/M/scenes/Ch_last/4.jpg"
image Ch_last_p5 = "/images/charles_home/outside/M/scenes/Ch_last/5.jpg"
image Ch_last_p6 = "/images/charles_home/outside/M/scenes/Ch_last/6.jpg"
image Ch_last_p7 = "/images/charles_home/outside/M/scenes/Ch_last/7.jpg"
image Ch_last_p8 = "/images/charles_home/outside/M/scenes/Ch_last/8.jpg"
image Ch_last_p9 = "/images/charles_home/outside/M/scenes/Ch_last/9.jpg"
image Ch_last_p10 = "/images/charles_home/outside/M/scenes/Ch_last/10.jpg"
image Ch_last_p11 = "/images/charles_home/outside/M/scenes/Ch_last/11.jpg"

label Ch_last_scene:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

    scene Ch_last_p1 with dissolve
    MC "Huh?"
    MC "(There’s a black van outside Charles’s place. Who the hell are those guys?)"

    scene Ch_last_p2
    Charles "Mppf! NMMPFFF!"
    Bodyguard1 "Stop struggling, sir. Get in the van."
    Charles "AHHHMMMMMMM!! HMMMM!!!"

    scene Ch_last_p3
    Bodyguard2 "Shut up and get your arse in the fecking car, fella! Yer making this far more difficult that it has to be!"
    MC "(Holy shit, is Charles getting kidnapped?!)"
    MC "(Shit, I better hide.)"

    scene Ch_last_p4
    MC "(Fuck me… they must be from the nightclub’s organised crime gang!)"
    MC "(I wonder what’s going to happen!)"

    scene Ch_last_p5
    Bodyguard1 "Get that trunk open."
    Bodyguard2 "Aye, gaffer. Will do."
    MC "(That bald one has a strange accent…)"
    Charles "MMM!! NMMFFPFF!!"

    scene Ch_last_p6
    Charles "HNMMMPFFF!!"
    Bodyguard2 "That’s him in, gaffer. Do it."
    Bodyguard1 "Stand back."

    scene Ch_last_p7
    Charles "Nmpfff!"
    Bodyguard2 "I can’t see any people about, gaffer. Yeh can do him now."

    scene Ch_last_p8
    MC "*Gulp* No way…"
    MC "(They’re not going to shoot him, are they?!)"


    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music2", loop=True, fadein = 2)

    scene Ch_last_p9
    "*BLAM*"
    MC "(HOLY FUCK!)"

    scene Ch_last_p10
    MC "(I have to get out of here!)"
    MC "*Pant Pant*"

    scene Ch_last_p11
    "*Clunk*"
    Bodyguard2 "Yeh never feel any guilt doing that, gaffer?"
    Bodyguard1 "Sometimes. This one was an especially… nasty subject though. He had a long history of domestic violence according to the boss."
    Bodyguard2 "Ugh, fuckin’ nonce. Y’know, if this was back in Belfast we’d ‘ave taken the wee shite out into an alley and just done his kneecaps in."
    Bodyguard1 "True. The boss wants this one dead though. Now, let’s take this to the usual burial spot."
    Bodyguard2 "Aye, gaffer."

    $ Ch_last_scene = False
    $ Charles_end = True

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    jump charles_outside_M1