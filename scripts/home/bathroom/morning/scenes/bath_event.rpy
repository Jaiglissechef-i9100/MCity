image bath_event_p1 = "images/home/bathroom/morning/scenes/bath_event/1.jpg"
image bath_event_p2 = "images/home/bathroom/morning/scenes/bath_event/2.jpg"
image bath_event_p3 = "images/home/bathroom/morning/scenes/bath_event/3.jpg"
image bath_event_pAu = "images/home/bathroom/morning/scenes/bath_event/Au.jpg"
image bath_event_pCaroline = "images/home/bathroom/morning/scenes/bath_event/Caroline.jpg"
image bath_event_pCelia = "images/home/bathroom/morning/scenes/bath_event/Celia.jpg"
image bath_event_pJudy = "images/home/bathroom/morning/scenes/bath_event/Judy.jpg"
image bath_event_pLily = "images/home/bathroom/morning/scenes/bath_event/Lily.jpg"
image bath_event_pLinda = "images/home/bathroom/morning/scenes/bath_event/Linda.jpg"
image bath_event_pSara = "images/home/bathroom/morning/scenes/bath_event/Sara.jpg"
image bath_event_pViolet = "images/home/bathroom/morning/scenes/bath_event/Violet.jpg"
image bath_event_pZuri = "images/home/bathroom/morning/scenes/bath_event/Zuri.jpg"
image white = "#FFFFFF"

default zuri_bath_event_unlock = False

transform pandown2:
    crop (0, 0, 1920, 2160)
    linear 4 crop (0, 1080, 1920, 1080)
transform pandown3:
    crop (0, 1080, 1920, 2160)
    linear 4 crop (0, 0, 1920, 2160)

transform pandown8:
    crop (0, 1080, 1920, 2160)
    linear 4 crop (0, 0, 1920, 2160)

transform pandown5:
    crop (0, 0, 1920, 1592)
    linear 4 crop (0, 512, 1920, 1080)
transform pandown6:
    crop (0, 512, 1920, 1592)
    linear 4 crop (0, 0, 1920, 1592)

label bath_event_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if day_time == 1:
        show screen bathroom_morning_notclickable
    if day_time == 2:
        show screen bathroom_day_notclickable
    if day_time == 3:
        show screen bathroom_evening_notclickable
    if day_time == 4:
        show screen bathroom_night_notclickable

    menu:
        "Take a bath.":

            if day_time == 1:
                show screen bathroom_morning_notclickable
                jump bath_event_menu2
            if day_time == 2:
                show screen bathroom_day_notclickable
                jump bath_event_menu2
            if day_time == 3:
                show screen bathroom_evening_notclickable
                jump bath_event_menu2
            if day_time == 4:
                show screen bathroom_night_notclickable
                MC "It’s too late to take a bath."
                jump bathroom_morning1
        "Cancel.":
            jump bathroom_morning1

label bath_event_menu2:
    hide screen bathroom_morning_notclickable
    hide screen bathroom_day_notclickable
    hide screen bathroom_evening_notclickable
    hide screen bathroom_night_notclickable
    scene bath_event_p1 with dissolve
    $ can_hide_windows = True
    menu:
        "Finish the bath.":
            $ renpy.block_rollback()
            $ day_time +=1
            scene black with dissolve
            $ renpy.sound.play("sfx/bath_sound.mp3")
            $ renpy.pause(5, hard = True)
            $ renpy.music.stop(channel="sound", fadeout=1)
            jump bathroom_morning1
        "Masturbate and think about someone.":
            jump bath_event_menu3

label bath_event_menu3:
    scene bath_event_p2 with dissolve
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music1", loop=True, fadein = 2)
    $ renpy.block_rollback()
    menu:
        "Mom" if renpy.loadable("patch.rpy"):
            scene bath_event_pLinda at pandown3
            $ renpy.pause(5)
            scene bath_event_pLinda at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pLinda with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Linda" if not renpy.loadable("patch.rpy"):
            scene bath_event_pLinda at pandown3
            $ renpy.pause(5)
            scene bath_event_pLinda at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pLinda with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Sara":
            scene bath_event_pSara at pandown3
            $ renpy.pause(5)
            scene bath_event_pSara at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pSara with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Caroline":
            scene bath_event_pCaroline at pandown3
            $ renpy.pause(5)
            scene bath_event_pCaroline at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pCaroline with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Judy":
            scene bath_event_pJudy at pandown3
            $ renpy.pause(5)
            scene bath_event_pJudy at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pJudy with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Celia":
            scene bath_event_pCelia at pandown3
            $ renpy.pause(5)
            scene bath_event_pCelia at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pCelia with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Aunt" if au_bath_event_unlock == True and renpy.loadable("patch.rpy"):
            scene bath_event_pAu at pandown3
            $ renpy.pause(5)
            scene bath_event_pAu at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pAu with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Linda's friend" if au_bath_event_unlock == True and not renpy.loadable("patch.rpy"):
            scene bath_event_pAu at pandown3
            $ renpy.pause(5)
            scene bath_event_pAu at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pAu with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Violet" if violet_bath_event_unlock == True:
            scene bath_event_pViolet at pandown3
            $ renpy.pause(5)
            scene bath_event_pViolet at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pViolet with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
        "Lily" if lily_bath_event_unlock == True:
            scene bath_event_pLily at pandown3
            $ renpy.pause(5)
            scene bath_event_pLily at pandown2
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pLily with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1

        "Zuri and Suri " if zuri_bath_event_unlock == True:
            scene bath_event_pZuri at pandown6
            $ renpy.pause(5)
            scene bath_event_pZuri at pandown5
            $ renpy.pause(5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_pZuri with dissolve
            $ renpy.pause(0.5)
            scene white with dissolve
            $ renpy.pause(0.5)
            scene bath_event_p3 with dissolve
            $ renpy.pause(2)
            $ day_time +=1
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bathroom_morning1
