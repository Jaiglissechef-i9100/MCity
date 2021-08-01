image caroline_cloth_shop_afternoon_scene3_p1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/1.jpg"
image caroline_cloth_shop_afternoon_scene3_p2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/2.jpg"
image caroline_cloth_shop_afternoon_scene3_p3 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/3.jpg"
image caroline_cloth_shop_afternoon_scene3_p4 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/4.jpg"
image caroline_cloth_shop_afternoon_scene3_p5 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/5.jpg"
image caroline_cloth_shop_afternoon_scene3_p6 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/6.jpg"
image caroline_cloth_shop_afternoon_scene3_p7 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/7.jpg"
image caroline_cloth_shop_afternoon_scene3_p8 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/8.jpg"
image caroline_cloth_shop_afternoon_scene3_p9 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/9.jpg"
image caroline_cloth_shop_afternoon_scene3_p10 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/10.jpg"
image caroline_cloth_shop_afternoon_scene3_p11 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/11.jpg"
image caroline_cloth_shop_afternoon_scene3_p12 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/12.jpg"
image caroline_cloth_shop_afternoon_scene3_p13 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/13.jpg"
image caroline_cloth_shop_afternoon_scene3_p14 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/14.jpg"
image caroline_cloth_shop_afternoon_scene3_p15 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/15.jpg"
image caroline_cloth_shop_afternoon_scene3_p16 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/16.jpg"
image caroline_cloth_shop_afternoon_scene3_p17 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/17.jpg"
image caroline_cloth_shop_afternoon_scene3_p18 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/18.jpg"
image caroline_cloth_shop_afternoon_scene3_p19 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/19.jpg"
image caroline_cloth_shop_afternoon_scene3_p20 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/20.jpg"
image caroline_cloth_shop_afternoon_scene3_p21 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/21.jpg"
image caroline_cloth_shop_afternoon_scene3_p22 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene3/22.jpg"
image caroline_cloth_shop_afternoon_scene3_p12anim = Movie(play="/videos/Caroline-AfternoonS3-Ass1.webm", loop = True,)
image caroline_cloth_shop_afternoon_scene3_p12anim_faster = Movie(play="/videos/Caroline-AfternoonS3-Ass1a.webm", loop = True,)
image caroline_cloth_shop_afternoon_scene3_p14anim = Movie(play="/videos/Caroline-AfternoonS3-Ass2.webm", loop = True,)
image caroline_cloth_shop_afternoon_scene3_p18anim = Movie(play="/videos/Caroline-AfternoonS3-Ass3.webm", loop = True,)

label caroline_cloth_shop_afternoon_scene3_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if unlock_caroline_closth_shop_afternoon_scene3 == False:
        scene caroline_cloth_shop_afternoon_scene3_p1 with dissolve
        Caroline "Okay - that’s me ready to go."
        Caroline "Let’s just get this photo session over, as soon as possible."
        MC "No problem. Do you want to strike a pose and I’ll get the camera ready."

        scene caroline_cloth_shop_afternoon_scene3_p2
        Caroline "(Oh, my God… he’s got a boner again!)"
        Caroline "(Again?! I guess it must be his age.)"
        Caroline "(That’s.. That’s not my problem anyway…)"
        Caroline "Okay, let’s start."
        jump cosplay_outfit6_label

    if unlock_caroline_closth_shop_afternoon_scene3 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene3_p1 with dissolve
        Caroline "Okay - that’s me ready to go."
        Caroline "Let’s just get this photo session over, as soon as possible."
        MC "No problem. Do you want to strike a pose and I’ll get the camera ready."

        scene caroline_cloth_shop_afternoon_scene3_p2
        Caroline "(Oh, my God… he’s got a boner again!)"
        Caroline "(Again?! I guess it must be his age.)"
        Caroline "..."

        scene caroline_cloth_shop_afternoon_scene3_p3
        Caroline "(And he REALLY needs to buy himself a proper belt.)"
        Caroline "(He can’t just have his dick pop out, every time he gets turned on!)"
        MC "Is everything alright, Caroline? Did you hear what I said?"

        scene caroline_cloth_shop_afternoon_scene3_p4
        Caroline "You’ve… umm… got a problem."
        MC "Huh?"
        Caroline "It’s happening again, [player_name]."
        MC "Wh-What?!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music2", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene3_p5
        MC "Oh shit! I’m so sorry!"
        MC "I didn’t even notice. It was the costume!"
        Caroline "You are a sick little pervert."

        scene caroline_cloth_shop_afternoon_scene3_p4
        Caroline "I swear to God… after I caught you peeping last time, I thought we had this sorted."
        MC "I’m sorry, Caroline! I didn’t mean to-"
        Caroline "Ugh! You disgust me."
        MC "I- I didn’t mean to!"

        scene caroline_cloth_shop_afternoon_scene3_p6
        Caroline "Jesus Christ… You are SO hard right now!"
        if persistent.incest_patch == True:
            Caroline "I can’t believe you get turned on, by your own sister like this!"
        else:
            Caroline "I can’t believe you get turned on, by your own friend like this!"
        if persistent.incest_patch == True:
            Caroline "We share the same parents, you fucking sicko!"
        else:
            Caroline "We’re supposed to be friends, you fucking sicko."
        MC "(I’m so fucked… She’s actually gonna kill me!)"

        scene caroline_cloth_shop_afternoon_scene3_p7
        Caroline "Sit down and stay the Hell away from me, you pervert!"
        MC "Caroline, I SWEAR - I didn’t mean to get an erection!"
        MC "I can’t control them!"

        scene caroline_cloth_shop_afternoon_scene3_p8
        Caroline "Bullshit! You’re just a horny little creep."

        if persistent.incest_patch == True:
            Caroline "God… what am I going to tell Dad?"
            MC "NO! Don’t say anything to Dad! PLEASE!"
            Caroline "I’m gonna have to advertise for a new photographer too."
            MC "PLEASE DON’T TELL DAD!"

        else:
            Caroline "God… what am I going to tell Bob?"
            MC "NO! Don’t say anything to Bob! PLEASE!"
            Caroline "I’m gonna have to advertise for a new photographer too."
            MC "PLEASE DON’T TELL Bob!"

        Caroline "..."
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene3_p9
        Caroline "Haha…"
        Caroline "AHAHAHAAHAHAHA!"
        MC "Huh?"
        Caroline "Your face! HAHA! You were terrified!"
        MC "Is… Is this a joke?"
        Caroline "Hahaha! I couldn’t resist!"

        scene caroline_cloth_shop_afternoon_scene3_p10 at pandown3
        Caroline "My anger may have been fake - but this boner is very much real."
        Caroline "I’m not gonna fuck you, but let’s see what I can do to help you out."
        MC "Caroline, you don’t have t-"

        scene caroline_cloth_shop_afternoon_scene3_p11 at pandown3
        Caroline "Shush. Don’t try to talk me out of it."
        Caroline "Do you seriously want me to change my mind?"
        MC "Haha! I guess not!"
        Caroline "Good."

        scene caroline_cloth_shop_afternoon_scene3_p12
        Caroline "Now, sit back, shut up, and enjoy this."
        scene caroline_cloth_shop_afternoon_scene3_p12anim
        MC "..."
        MC "Mmm…"
        MC "(My cock is sliding between her asscheeks!)"
        scene caroline_cloth_shop_afternoon_scene3_p12anim_faster
        MC "Ah... She sped up..."
        MC "It feels amazing..."

        scene caroline_cloth_shop_afternoon_scene3_p13
        Caroline "(Shit… maybe this was a bad idea…)"
        Caroline "(His shaft keeps brushing against my pussy.)"
        Caroline "(If I keep letting him do this I’ll get far too turned on… It would be more awkward if I just stopped now, though.)"

        scene caroline_cloth_shop_afternoon_scene3_p14
        MC "Ah…"
        scene caroline_cloth_shop_afternoon_scene3_p14anim
        MC "This is sooo good, Caroline…"
        Caroline "(And I’ve started making him happy… I’d only blueball him if I stopped now.)"

        scene caroline_cloth_shop_afternoon_scene3_p15
        MC "Mmm! Yes…"
        Caroline "Ah…"
        Caroline "(Shit! I can’t let myself moan. He can’t think I’m enjoying this!)"

        scene caroline_cloth_shop_afternoon_scene3_p16
        MC "(Well, this was certainly an unexpected surprise!)"
        MC "(I didn’t think Caroline would even be, slightly open to doing something like this.)"
        MC "(Especially after how angry she got, when she caught me peeping on her!)"

        scene caroline_cloth_shop_afternoon_scene3_p17
        MC "(Women are strange creatures - I don’t think I’ll ever fully understand them!)"
        Caroline "Are you enjoying this?"
        MC "Yeah, Caroline. It’s great! Can you go a bit faster?"

        scene caroline_cloth_shop_afternoon_scene3_p18
        Caroline "Like this?"
        scene caroline_cloth_shop_afternoon_scene3_p18anim
        MC "Ahh… That’s perfect!"
        MC "Yeee.. ahh..."
        MC "Ahh! Mmmm!"

        scene caroline_cloth_shop_afternoon_scene3_p19
        MC "Fuck! I’m getting close!"
        Caroline "You’re gonna cum?"
        Caroline "Just be careful that you don’t get any over the costume! I still have to sell this!"

        scene caroline_cloth_shop_afternoon_scene3_p20
        MC "Ahhhh! I’m cumming!"
        MC "Ugh! Fuck!"
        Caroline "(Wow! He came REALLY hard there! I think he enjoyed that!)"

        scene caroline_cloth_shop_afternoon_scene3_p21
        MC "Phew… That was amazing."
        MC "Thanks for that, Caroline. You were incredible!"
        Caroline "I don’t know what you’re talking about?"

        scene caroline_cloth_shop_afternoon_scene3_p22
        MC "What you just did there now-"
        Caroline "We were about to take some photos. Hurry up and get the camera ready!"
        MC "Uh, okay! Sure. But seriously, you were amazing with your ass, back there."
        Caroline "I think your imagination has run a little wild, [player_name]. Nothing happened."
        MC "(Huh?! Why is she acting like she didn’t just, grind against my cock?)"
        Caroline "Come on! We have photos to take! Chop chop!"
        $ caroline_closth_shop_afternoon_scene3 = False
        $ caroline_room_evening_scene4 = True
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump cosplay_outfit6_label

