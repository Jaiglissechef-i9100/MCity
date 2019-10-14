label celia_morning_laptopv1_label:
    scene celia_laptopv1_p1
    $ celia_laptopv1_password = renpy.input ("Enter Password", "" )
    $ renpy.sound.play('/sfx/mouse_click.mp3', loop=False)
    if celia_laptopv1_password == "Ossa36":
        MC "(Yes! The password was accepted!)"
        MC "(Let’s see if I can embarrass her in any way!)"
        jump celia_morning_password_correct_v1
    else:
        MC "(Fuck! The password is wrong.)"
        jump teacher_room1_morning1

label celia_morning_password_correct_v1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    MC "(Let’s see… grades? Emails? Course content guides?)"
    MC "(Maybe the emails have something interesting in them…)"
    MC "(Course planning… Parent-Teacher meetings… Ugh… it’s all boring rubbish.)"
    MC "(I guess I could just boost my grades, while I’m here.)"

    scene celia_laptopv1_p2 with dissolve
    MC "(Wait… Hold up! This isn’t a grades recording folder!)"
    MC "(Maddox $2000? England $4400?)"
    MC "(No way! Is Mrs. Celia SELLING grades?!)"

    scene celia_laptopv1_p3
    MC "(YES! This is top quality blackmail material!)"
    MC "(She won’t be picking on me anymore, now that I have this!)"
    MC "(I better take a photo quickly.)"

    scene celia_laptopv1_p4
    $ renpy.sound.play("sfx/photo_take.wav")
    MC "(And… there we go. I’ll need to come up with a solid plan, but at least I have all the evidence I’ll ever need.)"

    scene celia_laptopv1_p5
    MC "(Watch out, Mrs. Celia, because I’m coming for you!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_celia_laptopv1 = False
    $ Judy_scene1_v1 = 1
    $ can_hide_windows = False
    jump teacher_room1_morning1
