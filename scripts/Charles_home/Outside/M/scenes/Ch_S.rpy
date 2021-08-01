image Ch_doors_p1 = "/images/Charles_home/outside/M/scenes/Ch_NS1/1.jpg"
image Ch_doors_p1b = "/images/charles_home/outside/M/scenes/Ch_NS1/1b.jpg"
image Ch_doors_p2 = "/images/charles_home/outside/M/scenes/Ch_NS1/2.jpg"
image Ch_doors_p2a = "/images/charles_home/outside/M/scenes/Ch_NS1/2a.jpg"
image Ch_doors_p3 = "/images/charles_home/outside/M/scenes/Ch_NS1/3.jpg"
image Ch_doors_p3a = "/images/charles_home/outside/M/scenes/Ch_NS1/3a.jpg"
image Ch_doors_p3b = "/images/charles_home/outside/M/scenes/Ch_NS1/3b.jpg"

image Ch_inside_p0 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/0.jpg"
image Ch_inside_p1 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/1.jpg"
image Ch_inside_p2 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/2.jpg"
image Ch_inside_p3 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/3.jpg"
image Ch_inside_p4 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/4.jpg"
image Ch_inside_p5 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/5.jpg"
image Ch_inside_p6 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/6.jpg"
image Ch_inside_p7 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/7.jpg"
image Ch_inside_p8 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/8.jpg"
image Ch_inside_p9 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/9.jpg"
image Ch_inside_p10 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/10.jpg"
image Ch_inside_p11 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/11.jpg"
image Ch_inside_p12 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/12.jpg"
image Ch_inside_p13a = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/13a.jpg"
image Ch_inside_p13b = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/13b.jpg"
image Ch_inside_p14a = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/14a.jpg"
image Ch_inside_p14b = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/14b.jpg"
image Ch_inside_p14c = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/14c.jpg"
image Ch_inside_p15 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/15.jpg"
image Ch_inside_p16 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/16.jpg"
image Ch_inside_p17 = "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/17.jpg"

default CR4_guard = False
default Ch_S_door = True

label Ch_doors_lab:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if day_time == 1:
        scene Ch_doors_p1 with dissolve
        MC "(Okay, here goes nothing…)"
        $ renpy.sound.play('/sfx/knock_knock.wav', channel="sound")
        MC "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        "...."
        MC "(Hmm, nobody seems to be answering.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump charles_outside_M1

    if day_time == 2:
        scene Ch_doors_p1 with dissolve
        MC "(Okay, here goes nothing…)"
        $ renpy.sound.play('/sfx/knock_knock.wav', channel="sound")
        MC "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        "...."
        MC "(Hmm, nobody seems to be answering.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump charles_outside_M1

    if day_time == 3:
        scene Ch_doors_p2 with dissolve
        MC "(I wonder if Charles will be around in the evening.)"
        $ renpy.sound.play('/sfx/knock_knock.wav', channel="sound")
        MC "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        MC "(Still no answer. Bugger.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump charles_outside_M1

    if day_time == 4:
        scene Ch_doors_p3 with dissolve
        MC "(I can understand Charles not being here during the day. Perhaps he’s at work. But if he isn’t answering now, I have no idea what is going on!)"
        $ renpy.sound.play('/sfx/knock_knock.wav', channel="sound")
        MC "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        "…"
        MC "Goddammit!"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump charles_outside_M1

label Ch_window_lab:
    menu:
        "Play":
            $ can_hide_windows = True
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button

            if day_time == 1:
                scene Ch_doors_p1b with dissolve
                MC "(Let’s give this window a go. Maybe I can jimmy it open?)"
                MC "Ugh… Gah!"
                MC "(Nope, this thing isn’t budging a single inch! Perhaps I should come back later on in the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 2:
                scene Ch_doors_p1b with dissolve
                MC "(Let’s give this window a go. Maybe I can jimmy it open?)"
                MC "Ugh… Gah!"
                MC "(Nope, this thing isn’t budging a single inch! Perhaps I should come back later on in the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 3:
                scene Ch_doors_p2a with dissolve
                MC "Ugh!"
                MC "(Dammit, the window isn’t shifting. Maybe I should try another time of the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 4:
                if crowbar.selected == True:
                    $ clean_bar_value = 0
                    scene Ch_doors_p3b with dissolve
                    MC "(If you’re not going to let me in, then I’ll just have to make an entrance myself!)"
                    MC "Hnnnng… Come on!"
                    MC "Ugh! (Just a few more inches!)"
                    $ can_hide_windows = False
                    show screen week_day_viewer
                    show screen time_skip_button
                    show screen day_time_viewer
                    call screen Ch_window_scr
                else:
                    scene Ch_doors_p3a with dissolve
                    MC "(Please be open!)"
                    MC "Gah! Come on!"
                    MC "Let me in Charles! Open up the door, you bastard!"

                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False

                    jump charles_outside_M1
        "{image=cheat_code}":
            $ can_hide_windows = True
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button

            if day_time == 1:
                scene Ch_doors_p1b with dissolve
                MC "(Let’s give this window a go. Maybe I can jimmy it open?)"
                MC "Ugh… Gah!"
                MC "(Nope, this thing isn’t budging a single inch! Perhaps I should come back later on in the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 2:
                scene Ch_doors_p1b with dissolve
                MC "(Let’s give this window a go. Maybe I can jimmy it open?)"
                MC "Ugh… Gah!"
                MC "(Nope, this thing isn’t budging a single inch! Perhaps I should come back later on in the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 3:
                scene Ch_doors_p2a with dissolve
                MC "Ugh!"
                MC "(Dammit, the window isn’t shifting. Maybe I should try another time of the day?)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False

                jump charles_outside_M1

            if day_time == 4:
                if crowbar.selected == True:
                    $ clean_bar_value = 0
                    scene Ch_doors_p3b with dissolve
                    MC "(If you’re not going to let me in, then I’ll just have to make an entrance myself!)"
                    MC "Hnnnng… Come on!"
                    MC "Ugh! (Just a few more inches!)"
                    $ can_hide_windows = False
                    show screen week_day_viewer
                    show screen time_skip_button
                    show screen day_time_viewer
                    jump Ch_inside_lab
                else:
                    scene Ch_doors_p3a with dissolve
                    MC "(Please be open!)"
                    MC "Gah! Come on!"
                    MC "Let me in Charles! Open up the door you bastard!"

                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False

                    jump charles_outside_M1

screen Ch_window_scr:
    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1120 ypos 180
    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True
    imagebutton:

        xpos 944
        ypos 71
        focus_mask True
        idle "/images/charles_home/outside/M/scenes/Ch_NS1/B1.png"
        hover "/images/charles_home/outside/M/scenes/Ch_NS1/B1_hover.png"

        action [SetVariable("clean_bar_value", clean_bar_value + 0.30)]
        unhovered Hide("displayTextScreen")

    if clean_bar_value >= 1.5:
        timer 1.3 action [Hide("Ch_window_scr"),SetVariable("clean_bar_value", 0),Jump("Ch_inside_lab")]

label Ch_inside_lab:
    scene black
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.pause(2,hard = True)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    scene Ch_inside_p0 with dissolve
    "*CRACK*"
    MC "Yes!"
    MC "(I’m gonna get you now, you bastard!)"

    scene Ch_inside_p1
    Television "Suck my fucking cock, you whore!"
    Charles "Ugh… Yeah… Mmm…"
    MC "(Huh… It looks like he didn’t hear me break into his place. The TV must be too loud for him to hear.)"

    scene Ch_inside_p2
    MC "*Sniff*"
    MC "(Ugh, this place stinks of stale beer. He must be drunk.)"
    MC "(This could be my chance to take this bastard down. I probably wouldn’t win a one on one fight, but him being drunk might be the advantage I need!)"

    scene Ch_inside_p3
    Charles "Oh yeah, deepthroat that big dick! Woo!"
    Charles "Mmm!"

    scene Ch_inside_p4
    Television "*SHLURP* *GAG* *SPLUTTER*"
    Television "Hnnng! Swallow it all! Don’t you dare spill a drop!"
    Charles "Ah… Shit! Ugh!"

    scene Ch_inside_p5
    Television "Turn around, bitch! I’m gonna plough your tight asshole now!"
    Charles "*Glug Glug*"
    MC "(He’s distracted. Now’s my chance!)"

    scene Ch_inside_p6
    MC "(I’m gonna bring you down, you piece of shit.)"
    MC "(I’m gonna get Caroline her necklace back; and I’m gonna make you pay for treating her like shit for all those years.)"

    $ can_hide_windows = False

    menu:
        "Play":
            jump start_ch_mg
        "{image=cheat_code}":
            jump Ch_inside_lab2

label Ch_inside_lab2:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ can_hide_windows = True
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
    scene black
    $ renpy.pause(2, hard = True)
    scene Ch_inside_p7
    MC "Hyah!"
    Charles "AAARGGHHH!!"
    Charles "*Hack* *Cough*"
    Charles "Th-There’s no *Hack* m-money here... "

    scene Ch_inside_p8
    MC "I’m not after money, you pathetic excuse for a human being."
    Charles "Wait- I recognise that voice. Y-You?!"

    scene Ch_inside_p9
    Charles "What the… *Hack* fuck do you want?!"
    MC "I want that necklace you stole from Caroline. I’m not leaving here empty-handed."
    MC "I don’t care if I have to choke you out - I WILL get it back!"

    scene Ch_inside_p10
    Charles "Caroline’s necklace?"
    Charles "I already fucking *cough* sold it."
    MC "Wh-What?!"

    scene Ch_inside_p11
    Charles "Haha *cough* haha… It’s gone."
    MC "WHERE?! Who did you sell it to?!"
    Charles "The… *cough* nightclub owner. *Hack* Paid of my whole debt…"

    scene Ch_inside_p12
    MC "You’re lying…"
    Charles "Do you think I’d be relaxing here right now if I was still in debt to that sociopath?! I’m a free man, baby!"

    scene Ch_inside_p13a
    Charles "Haha! I really should kick your ass for trying that shit on me."
    Charles "But I gave that arrogant bitch Caroline, enough beatings for the two of you."
    Charles "She must be saving a fortune on concealer now - a wimp like you couldn’t give her a proper shiner if he tried! AHAHAHA!"
    $ night_club_unlocked = True
    $ Ch_S_door = False
    $ CR4_guard = 1
    menu:
        "Caroline was worried about you. Leave safely while you still have the chance. It isn’t work putting your future with her at risk over a pointless fight.":
            scene Ch_inside_p13b

            MC "(I want to kill this fucker right now…)"
            MC "(...but if I don’t win I might not ever see Caroline again. I should just focus on finding her necklace.)"
            MC "(Maybe I can find this nightclub owner and take things from there.)"
            Charles "Yeah! Just walk away, you fucking chicken! Get the fuck outta my place and let me finish my porn in peace."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False

            jump charles_outside_M1
        "Charles can NOT go unpunished for what he did to Caroline. It’s time to take the fight back to him.":

            scene Ch_inside_p13a
            MC "…"

            scene Ch_inside_p14a
            "*CRACK*"
            Charles "AHHHHHH!!!!"

            scene Ch_inside_p14b
            "*CRASH*"
            Charles "Ow… M-My neck… Aaaarrghhh… C-Call an ambulance!"
            MC "I’m going to leave you now, Charles."
            Charles "P-Please! Ahh..."
            MC "I don’t think I broke your neck; but even if I did, it wouldn’t be a fraction of the punishment you actually deserved."

            scene Ch_inside_p14c
            MC "Goodbye, Charles. I don’t expect to ever see you again."
            Charles "Ahhhhh!!!!"

            scene Ch_inside_p15
            MC "(That’s Charles dealt with, for good. I don’t think he has any reason to bother me or Caroline ever again.)"
            MC "(I didn’t get what I came for though. He still sold the necklace before I could get it.)"

            scene Ch_inside_p16
            MC "(I can’t go back to Caroline empty handed. She’ll just think I put my life at risk for no reason at all!)"
            MC "(Dammit… I should have come over here quicker. Maybe I could have caught him before he sold it?)"

            scene Ch_inside_p17
            MC "(He said he gave it to the owner of the nightclub. I should probably drop by there and see if I can arrange a meeting with the club owner.)"

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False

            jump charles_outside_M1



init:
    transform shake_ch_mg:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat

default ch_mg_r = 1

label start_ch_mg:
    if ch_mg_r == 4:
        $ ch_mg_r = 1
        jump Ch_inside_lab2

    call screen ch_mg_scr
screen ch_mg_scr:
    if clean_bar_value >0:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.10) repeat True
        if ch_mg_r == 1:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/4.jpg" at shake_ch_mg
        if ch_mg_r == 2:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/5.jpg" at shake_ch_mg
        if ch_mg_r == 3:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/9.jpg" at shake_ch_mg

    if clean_bar_value <= 0:
        if ch_mg_r == 1:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/4.jpg"
        if ch_mg_r == 2:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/5.jpg"
        if ch_mg_r == 3:
            add "/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/9.jpg"


    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1400 ypos 200

    imagebutton:

        xpos 1300
        ypos 71
        focus_mask True
        idle Transform("/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/B1.png", zoom=  0.8)
        hover Transform("/images/charles_home/outside/M/scenes/Ch_NS1/Inside/Minigame/B1_hover.png", zoom=  0.8)

        action [SetVariable("clean_bar_value", clean_bar_value + 0.30)]
        unhovered Hide("displayTextScreen")

    if clean_bar_value >= 1.5:
        timer 1.3 action [SetVariable("clean_bar_value", 0), SetVariable("ch_mg_r", ch_mg_r +1), Jump("start_ch_mg"),]

