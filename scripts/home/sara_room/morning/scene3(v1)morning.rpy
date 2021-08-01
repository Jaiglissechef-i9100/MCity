image scene3_v1p1 = "images/home/sara_room/morning/Scene3_v1/1.jpg"
image scene3_v1p2 = "images/home/sara_room/morning/Scene3_v1/2.jpg"
image scene3_v1p3 = "images/home/sara_room/morning/Scene3_v1/3.jpg"
image scene3_v1p4 = "images/home/sara_room/morning/Scene3_v1/4.jpg"
image scene3_v1p5 = "images/home/sara_room/morning/Scene3_v1/5.jpg"
image scene3_v1p6 = "images/home/sara_room/morning/Scene3_v1/6.jpg"
image scene3_v1p7 = "images/home/sara_room/morning/Scene3_v1/7.jpg"
image scene3_v1pdrawer = "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"

label sis_nerdy_scene3_v1:
    hide screen displayTextScreen
    hide screen corridor_morning
    scene SisterNerdy_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    call screen sister_nerdy_morning

label scene3_v1drawer:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    MC "(Huh, no sign of Sara. I wonder where she is.)"
    MC "(Come to think of it… if she’s not around, I could take a nosy in her cupboards. Maybe she has something interesting hidden away?)"
    $ drawer_sis_nerdy = 2
    jump sister_nerdy_morning1

label sis_nerdy_scene3_1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene3_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Let’s see what could be hidden in here.)"
    MC "(Most of the girls her age have started drinking alcohol now. She might have some stashed away in here.)"
    scene black
    $ renpy.sound.play('/sfx/Drawer open.mp3', loop=False)
    $ renpy.pause(2)
    $ renpy.sound.stop(channel="sound")
    MC "(Boring… Junk… Garbage…)"
    MC "(How much makeup does one girl need?!)"
    MC "(Whoa! Hold up!)"

    scene scene3_v1p2
    MC "(A pair of Sara’s panties?)"
    MC "(I could sneak these back to my room before she returns.)"
    MC "(Wait - why am I even thinking of doing something like that?! That stupid therapist is putting perverted ideas into my head!)"
    MC "(I should probably just put them back and-)"

    scene scene3_v1p3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)
    Sara "AHEM!"
    Sara "[player_name]? What are you doing in my underwear drawer?"
    MC "(FUCK!)"
    MC "(I’m gonna need to come up with a plan to get out of this one…)"
    window hide
    menu:
        "Drop the panties in the drawer and walk away without saying a word.":

            scene scene3_v1p4
            MC "(The less that I say the better. Maybe if I act like nothing weird is going on, then Sara will think I was just cleaning or putting away laundry?)"
            MC "(Yeah, that’s the best way to handle this.)"
            Sara "[player_name]! What are you doing with my-"

            scene scene3_v1p6
            Sara "Huh?!"
            Sara "(Wh-What?! He just dropped my panties and left?)"
            MC "(Haha! Nailed it! Now she thinks I was just putting away the laundry!)"
            Sara "(Was that supposed to be a bluff that he was doing the laundry?)"
            MC "(There’s no way she’ll ever think that I was about to steal her panties and jerk off into them!)"
            Sara "(Damn… the thought of him stealing my panties and jerking off into them is pretty fucking hot.)"

            scene scene3_v1p7
            Sara "Really… really… hot..."
            Sara "(He must have really liked those panties if he took them out of the drawer first.)"
            Sara "(I wonder if I could surprise him with them.)"
            jump after_scene3_v1_ch1
        "Lie and state that you found them lying on the floor.":

            scene scene3_v1p4
            MC "(I just have to tell her that I came into her room and found her panties lying on the floor.)"
            MC "(You can do this, [player_name]. Practice in your head, then turn around, and confidently explain what happened.)"
            MC "(Sara, I came into your room, saw your panties laying on the floor, and picked them up.)"
            Sara "[player_name]?"
            MC "(Sara, I came into your room, saw your panties laying on the floor.)"
            Sara "[player_name]! What the heck are you doing?!"
            MC "(Sara, I came into your room, saw your panties laying on the-)"
            Sara "[player_name]! Answer me!"

            scene scene3_v1p5
            MC "S-Sara, I lay in your room and came in your panties!"
            Sara "WHAT?!"
            MC "N-No! I came in your panties - I mean, I came on your floor!"
            Sara "Wh-What?! Eww!"
            MC "(Oh fuck! I’m screwing this up! I need to take a deep breath and start again.)"
            MC "I came into your… room. I saw your panties lying on the floor. Then I picked them up to put back in the drawer."
            MC "Here, take them back!"

            scene scene3_v1p6
            MC "(Jesus Christ! That was almost as bad as my experience with Mrs. Celia!)"
            MC "(Why can’t I just socialise with people properly!)"

            scene scene3_v1p7
            Sara "(Hehe! It was REALLY funny seeing [player_name] get flustered like that.)"
            Sara "(I gotta admit though - the thought of him using my panties and cumming in them is really hot.)"
            Sara "(Just the thought alone is getting me all wet.)"
            jump after_scene3_v1_ch1

label after_scene3_v1_ch1:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
    $ drawer_sis_nerdy = 3
    $ sis_nerdy_evening_scene2_v1 = 1
    $ day_time += 1
    $ sis_nerdy_scene4_v1 = 1
    $ first_sis_nerdy_scene4_v1 = 1
    $ can_sms1_from_sara = 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    $ can_hide_windows = False
    jump sister_nerdy_morning1

