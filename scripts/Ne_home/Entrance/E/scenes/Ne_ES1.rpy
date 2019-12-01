image Ne_ES1_p1 = "images/Ne_1/ES1/1.jpg"
image Ne_ES1_p1a = "images/Ne_1/ES1/1a.jpg"
image Ne_ES1_p2 = "images/Ne_1/ES1/2.jpg"
image Ne_ES1_p2a = "images/Ne_1/ES1/2a.jpg"
image Ne_ES1_p3 = "images/Ne_1/ES1/3.jpg"
image Ne_ES1_p3a = "images/Ne_1/ES1/3a.jpg"
image Ne_ES1_p4 = "images/Ne_1/ES1/4.jpg"
image Ne_ES1_p5 = "images/Ne_1/ES1/5.jpg"
image Ne_ES1_p5a = "images/Ne_1/ES1/5a.jpg"
image Ne_ES1_p6 = "images/Ne_1/ES1/6.jpg"
image Ne_ES1_p7 = "images/Ne_1/ES1/7.jpg"
image Ne_ES1_p7a = "images/Ne_1/ES1/7a.jpg"
image Ne_ES1_p8 = "images/Ne_1/ES1/8.jpg"
image Ne_ES1_p9 = "images/Ne_1/ES1/9.jpg"
image Ne_ES1_p10 = "images/Ne_1/ES1/10.jpg"
image Ne_ES1_p11 = "images/Ne_1/ES1/11.jpg"
image Ne_ES1_p12 = "images/Ne_1/ES1/12.jpg"
image Ne_ES1_p13 = "images/Ne_1/ES1/13.jpg"
image Ne_ES1_p13anim = Movie(play="videos/06 Neighboors ES1-2.webm", loop = True )
image Ne_ES1_p14 = "images/Ne_1/ES1/14.jpg"
image Ne_ES1_p15 = "images/Ne_1/ES1/15.jpg"
image Ne_ES1_p15anim = Movie(play="videos/06 Neighboors ES1-1.webm", loop = True )
image Ne_ES1_p16 = "images/Ne_1/ES1/16.jpg"
image Ne_ES1_p16anim = Movie(play="videos/06 Neighboors ES1-3.webm", loop = True )
image Ne_ES1_p17 = "images/Ne_1/ES1/17.jpg"
image Ne_ES1_p18 = "images/Ne_1/ES1/18.jpg"
image Ne_ES1_p19 = "images/Ne_1/ES1/19.jpg"
image Ne_ES1_p20 = "images/Ne_1/ES1/20.jpg"
image Ne_ES1_p21 = "images/Ne_1/ES1/21.jpg"
image Ne_ES1_p21anim = Movie(play="videos/06 Neighboors ES1-5.webm", loop = True )
image Ne_ES1_p22 = "images/Ne_1/ES1/22.jpg"
image Ne_ES1_p23 = "images/Ne_1/ES1/23.jpg"
image Ne_ES1_p24 = "images/Ne_1/ES1/24.jpg"
image Ne_ES1_p24anim = Movie(play="videos/06 Neighboors ES1-4.webm", loop = True )
image Ne_ES1_p25 = "images/Ne_1/ES1/25.jpg"
image Ne_ES1_p25anim = Movie(play="videos/06 Neighboors ES1-4a.webm", loop = True )
image Ne_ES1_p26 = "images/Ne_1/ES1/26.jpg"
image Ne_ES1_p27 = "images/Ne_1/ES1/27.jpg"
image Ne_ES1_p28 = "images/Ne_1/ES1/28.jpg"
image Ne_ES1_p29 = "images/Ne_1/ES1/29.jpg"
image Ne_ES1_p30 = "images/Ne_1/ES1/30.jpg"
image Ne_ES1_p31 = "images/Ne_1/ES1/31.jpg"
image Ne_ES1_p32 = "images/Ne_1/ES1/32.jpg"
image Ne_ES1_p33 = "images/Ne_1/ES1/33.jpg"
image Ne_ES1_p34 = "images/Ne_1/ES1/34.jpg"
image Ne_ES1_p35 = "images/Ne_1/ES1/35.jpg"
image Ne_ES1_p36 = "images/Ne_1/ES1/36.jpg"
image Ne_ES1_p36anim = Movie(play="videos/06 Neighboors ES1-6.webm", loop = True )
image Ne_ES1_p37 = "images/Ne_1/ES1/37.jpg"
image Ne_ES1_p38 = "images/Ne_1/ES1/38.jpg"
image Ne_ES1_p39 = "images/Ne_1/ES1/39.jpg"
image Ne_ES1_p40 = "images/Ne_1/ES1/40.jpg"

label Ne_ES1_lab:
    hide screen map_button
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    $ can_hide_windows = True
    scene Ne_ES1_p8 with dissolve
    MC "(Genius! It worked like a charm!)"
    MC "(Now let’s see what my neighbours are up to tonight…)"
    if Ne_ES1 == False:
        MC "There is nothing intresting now."
        $ can_hide_windows = False
        jump Ne_outside_M1

    scene Ne_ES1_p9
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

    MC "(Aww, yeah! Jackpot!)"
    Sidra "What is the matter, Isla? Are you unhappy with your new outfit?"
    Isla "N-No, it’s just…"
    scene Ne_ES1_p10
    Sidra "Just what, darling?"
    Isla "I could… maybe do with some panties? Or even a skirt?"
    Sidra "Haha, you know you aren’t allowed to wear any panties around me. Not after what you did."
    scene Ne_ES1_p11
    MC "(Ohh, some kinky roleplay!)"
    Isla "I’m sorry, I’ll try harder next time!"
    Sidra "Uh huh, that is what you tell me every time, darling. It grows tiresome hearing it."
    scene Ne_ES1_p12
    if persistent.incest_patch == True:
        Sidra "Now, get over here and give your mother a kiss."
    else:
        Sidra "Now, get over here and give me a kiss."
    Isla "Mmm!"
    scene Ne_ES1_p13
    Sidra "Mmm…"
    scene Ne_ES1_p13anim
    Isla "Mmm!"
    MC "(Damn! I wish I’d brought a camera to record this!)"
    scene Ne_ES1_p14
    MC "(They’re so fucking hot!)"
    MC "(I’d give ANYTHING to get a double blowjob from the two of them!)"
    scene Ne_ES1_p15
    Sidra "Mmm…"
    scene Ne_ES1_p15anim
    Isla "Mmm!"
    MC "(That’s it, keep making out for me!)"
    scene Ne_ES1_p16
    MC "(Her ass if fucking perfect. I’d ram my cock into it so hard if I ever got the chance!)"
    scene Ne_ES1_p16anim
    MC "(And she looks so slutty in those rainbow stockings.)"
    scene Ne_ES1_p17
    MC "(I’m having a hard time deciding which of the two I like better now…)"
    if persistent.incest_patch == True:
        MC "(The MILF’s ass is rounder, but the teen has a REALLY nice pussy on her)"
    else:
        MC "(Sindra’s ass is rounder, but Isla's has a REALLY nice pussy on her)"
    scene Ne_ES1_p18
    MC "(I wonder how long the two of them have been dating. There’s already quite an age difference!)"
    Sidra "Mmm!"
    scene Ne_ES1_p19
    Sidra "Only eighty four percent. Tut, tut."
    Isla "I’m sorry, I promise you I’ll do better next time!"
    Sidra "You know the punishment, sixteen orgasms."
    scene Ne_ES1_p20
    MC "(Awesome! They’re actually going all the way!)"
    Isla "I… I can’t do sixteen!"
    Sidra "Please, Isla. You’re being melodramatic. You’ve taken thirty five before!"
    Isla "I- I could barely walk the next day!"
    scene Ne_ES1_p21
    Sidra "Then it will be a lesson well learnt."
    Sidra "*Lick*"
    scene Ne_ES1_p21anim
    Isla "Ohhh!"
    scene Ne_ES1_p22
    Sidra "*Shlurp* *Lick*"
    Isla "Ahh! Ahhhh! AHHHH!!"
    if persistent.incest_patch == True:
        Isla "O-OH GOD!!! M-Mom! It’s too s-sensitive when you ah... use your tongue like that ohhhhhn my clitoris! *GASP*"
    else:
        Isla "O-OH GOD!!! S-Sindra! It’s too s-sensitive when you ahh... use your tongue like that ohhhhhn my clitoris! *GASP*"
    scene Ne_ES1_p23
    Sidra "*LICK LICK LICK*"
    Isla "AHHHHH!!! I’M CUMMINGGG!!"
    Sidra "*Shlurp*"
    Sidra "Fifteen to go."
    scene Ne_ES1_p24
    Isla "*Pant* *Gasp*"
    scene Ne_ES1_p24anim
    Sidra "*Lick* *Slurrrrp*"
    Isla "Ahhh! Ayaaaahhhh!"
    scene Ne_ES1_p25
    Sidra "*Lick Lick Lick Lick*"
    scene Ne_ES1_p25anim
    Isla "N-NOT AGAIN AAAAAHHhHHH!!!!!"
    Sidra "*SLURP*"
    Isla "*Pant Pant*"
    Sidra "Only fourteen to go. Shall we increase the intensity a bit?"
    scene Ne_ES1_p26
    Isla "N-No, p-please!"
    Sidra "I’m going to slip a couple of fingers in your ass now, darling."
    Isla "*GASP* Ohhh!!!"
    scene Ne_ES1_p27
    Isla "AAAYAAAAHHHHHHH!!!! OHHHH FUUUUCCCCK!"
    Sidra "Mmm! *Slurp*"
    Isla "Hnnnngggg!!! OOHHHH AAAAHHHH!!!"
    scene Ne_ES1_p28
    Sidra "That’s it, cum for me! Cum for me!"
    Sidra "*LICK* *SLURP*"
    Isla "AHAHHHHHHH!!!! HNNNGGGG!!! *GASP*"
    scene Ne_ES1_p29
    Sidra "Thirteen to go. Are you still conscious, darling? You know how annoyed I get when you pass out from pleasure on me."
    Isla "Y-Y-Yeah…"
    Sidra "*Lick Lick*"
    Isla "Ohhh…."
    scene Ne_ES1_p30
    MC "(Hehe, this is SO much better than online porn!)"
    MC "(Sidra is really going to town on Isla with her tongue! That teenager must have a really sensitive pussy!)"
    MC "(Hopefully I get to experience it too someday!)"
    Sidra "Let’s swap things up a bit."
    scene Ne_ES1_p31
    Isla "Ohhh!!"
    Sidra "*Lick*"
    Isla "Ahh! Ohh!"
    scene Ne_ES1_p32
    Sidra "Good girl, mmm! Don’t stop licking this time! Ahh!"
    Isla "*Lick*"
    Sidra "Mmm… Right there…"
    scene Ne_ES1_p33
    Sidra "*Lick* *Slurp*"
    Isla "Ahhh! Mmm!"
    Sidra "*Lick*"
    scene Ne_ES1_p34
    Isla "AHHHHHH!!!!!!"
    Sidra "(There she goes again; twelve to go.)"
    Isla "*GASP* *Pant*"
    scene Ne_ES1_p35
    Sidra "Cumming isn’t an excuse to stop licking, Isla."
    Isla "S-Sorry! Ahh! *Lick Lick*"
    Sidra "Ohh…"
    scene Ne_ES1_p36
    Sidra "*Slurp* *Suck*"
    Isla "MMMM!!!! *Lick*"
    scene Ne_ES1_p36anim
    MC "(Holy fuck this is incredible!)"
    scene Ne_ES1_p37
    MC "(She’s really digging her tongue deep into that girl’s pussy!)"
    MC "(Fuck, this is really hot!)"
    Isla "AAAHHHHH!!!!!"
    scene Ne_ES1_p38
    Isla "I’m cumming! *GASP* I’m cumming!"
    Sidra "You can say it twice, but it only counts as one, darling. Eleven to go!"
    Isla "*Pant* I-"
    Sidra "*Lick*"
    Isla "AYAAAHHHH!!!"
    scene Ne_ES1_p39
    MC "(This show is great, but I should probably bail before one of them glances up at the window and sees me.)"
    Isla "AHH! AHHH!!!"
    scene Ne_ES1_p40
    MC "(Thanks for the show, ladies!)"
    MC "(Maybe I should talk with Isla about this at school in the morning?)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ Ne_MS2 = 4
    $ Ne_ES1 = False
    $ day_time = 4
    jump map_label


label Ne_ES1_door:
    hide screen map_button
    if day_time ==3:
        show screen Ne_outside_E_scr
    else:

        show screen Ne_outside_N_scr

    $ clickable = False
    MC "(Okay, let’s give that door a try. Maybe they keep the back one unlocked?)"
    MC "(It’s all fenced off out back anyway, so there’s probably no real need to lock it.)"
    MC "Hmm…"
    MC "(There’s a second floor window - but if I want to get up to that I’d need to scale the wall.)"
    MC "(I could try using that ladder lying there!)"
    $ clickable = True
    hide screen Ne_outside_E_scr
    hide screen Ne_outside_N_scr
    jump Ne_outside_M1

label Ne_ES1_door2:
    hide screen map_button
    if day_time ==3:
        scene Ne_ES1_p7
    else:

        scene Ne_ES1_p7a

    MC "C’mon…"
    "*RATTLE RATTLE*"
    MC "Damn!"
    MC "(I’m going to need to find another entrance.)"
    jump Ne_outside_M1