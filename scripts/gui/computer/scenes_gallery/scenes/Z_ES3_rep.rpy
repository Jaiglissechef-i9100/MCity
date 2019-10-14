


label Z_ES3_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene Zv2_ES3_p2
    $ can_hide_windows = True
    window hide
    menu:
        "{color=#ff8000}Lick and Footjob.{/color}":
            scene Zv2_ES3_p1 with dissolve

            Zuri "Welcome back, [player_name]."
            Suri "It’s good to see you again, kid."
            MC "I’m glad to see you too."
            Zuri "Thanks again for your help with the company name. We’ll both make sure you are adequately rewarded."
            Suri "How about we head into the back room and get this party started?"
            $ renpy.music.stop(channel="music1", fadeout=1)
            scene black
            $ renpy.pause(3, hard= True)
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            scene Zv2_ES3_p2

            Suri "So, what were you thinking?"
            Zuri "We could give you a footjob."
            Suri "Or we could lick your cock until you cum."
            window hide
            menu:
                "Can you lick my cock?":
                    scene Zv2_ES3_p2

                    MC "I’d love to see the two of you lick my cock."

                    scene Zv2_ES3lick_p1

                    Suri "Is that so, kid?"
                    Zuri "I imagine you must enjoy the sight of two pretty girls, on their knees before you."
                    Zuri "Let’s get these jeans undone."

                    scene Zv2_ES3lick_p2

                    MC "(This is gonna be awesome! I’ve never had a double blowjob before!)"
                    Zuri "Now, we’re only going to lick you today. But if you get us more names, we can certainly think about giving you a proper sucking. Deal?"
                    MC "Yeah, deal."

                    scene Zv2_ES3lick_p3

                    Zuri "It’s pretty big, Suri, isn’t it!"
                    Suri "The kid surprised me!"
                    if renpy.loadable("patch.rpy"):
                        MC "(God, why am I just letting them do this? They’re seducing me into ruining Dad’s company!)"
                    else:
                        MC "(God, why am I just letting them do this? They’re seducing me into ruining Bob’s company!)"
                    scene Zv2_ES3lick_p4

                    MC "(I have to make a stand and say “No more”.)"
                    Zuri "It’s sooo thick too!"
                    Suri "That would feel REALLY good inside me!"

                    scene Zv2_ES3lick_p5

                    MC "Oooh…."
                    Suri "(Lick Lick)"
                    Zuri "(Lick Lick)"

                    scene Zv2_ES3lick_p6
                    if renpy.loadable("patch.rpy"):
                        MC "(On the other hand, maybe Dad’s company isn’t worth a blowjob THIS good!)"
                    else:
                        MC "(On the other hand, maybe Bob’s company isn’t worth a blowjob THIS good!)"
                    Suri "(Lick Lick)"
                    MC "(They’re teasing every inch of my dick! I’ll be cumming in no time!)"

                    scene Zv2_ES3lick_p7

                    Zuri "(Lick! Slurp!)"
                    MC "Ahh… Ohh…"
                    Suri "(Lick! Lick!)"

                    scene Zv2_ES3lick_p8

                    MC "(God, her eyes are stunning!)"
                    scene Zv2_ES3lick_p8anim
                    MC "(The way she looks at me while she licks my cock, is heart-melting!)"

                    scene Zv2_ES3lick_p9

                    Suri "Suck Suck!"
                    Zuri "Suck Suck!"
                    MC "Ooohhh God! Mmmmm!"

                    scene Zv2_ES3lick_p10

                    MC "Ahhh!"
                    scene Zv2_ES3lick_p10anim
                    Zuri "Shluuuurrrrp!"
                    Suri "SUCK SUCK!"

                    scene Zv2_ES3lick_p11

                    MC "Hnnnng!"
                    MC "I’m gonna cum! It’s too intense! AHHHH!"
                    $ Suri_name = "Both"
                    Suri "SHLURP! SUCK SUCK!"
                    $ Suri_name = "Suri"

                    scene Zv2_ES3lick_p12

                    MC "I’m cumming! Hnnnnggg!"
                    Suri "Lick Lick"
                    Zuri "Lick Lick"
                    scene white with dissolve
                    $ renpy.pause(0.7, hard = True)
                    scene Zv2_ES3lick_p12 with dissolve
                    $ renpy.pause(0.7, hard = True)
                    scene white with dissolve
                    $ renpy.pause(0.7, hard = True)
                    scene Zv2_ES3lick_p12a with dissolve

                    MC "AYAAAAAHHHHH!!!"
                    MC "Oh God…"
                    Suri "Mmm… Salty!"

                    scene Zv2_ES3lick_p13

                    Zuri "You’ve seen what we can do now. How about you get us that third name?"
                    Suri "Yeah. If you do that we’ll take your WHOLE cock in our mouths. Sound good?"
                    MC "Absolutely! You girls are incredible!"
                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False
                    jump pc_icon_label
                "Could you give me a footjob?":


                    MC "I’ll go for the footjob."
                    Zuri "Mmm... Good choice. Go ahead and take your trousers off, then lie back on the bed."

                    scene Zv2_ES3foot_p1

                    Suri "His cock is so big, Zuri! Hehe!"
                    Zuri "It REALLY is! I hope he’s going to enjoy us rubbing our feet ALL over it."
                    MC "(Twins rubbing their feet over my cock? It’s my lucky day!)"


                    scene Zv2_ES3foot_p2

                    Suri "And here we go. Hehe! I can feel it twitching beneath my toes!"
                    scene Zv2_ES3foot_p2anim
                    Suri "I think he’s enjoying this!"
                    MC "Mmm! Oh yeah..."


                    scene Zv2_ES3foot_p3

                    Zuri "There’s going to be MANY more things we can do for you. "
                    Suri "We can give you sooo much pleasure."
                    Zuri "And the only thing you have to do, is lie back and enjoy it."

                    scene Zv2_ES3foot_p4

                    MC "Mmm! Ah…"
                    scene Zv2_ES3foot_p4anim
                    MC "(This feels so fucking good…)"
                    Suri "Maybe we’ll even let you fuck our pussies someday."

                    scene Zv2_ES3foot_p5

                    Zuri "And the only thing you need to do - to keep earning these rewards - is get us those names."
                    Zuri "Simple, right?"
                    MC "Ah… uh huh…"

                    scene Zv2_ES3foot_p6

                    Suri "What’s wrong, kid? Would you like us to go faster?"
                    scene Zv2_ES3foot_p6anim
                    MC "God yes!"
                    Zuri "Let’s speed things up, Suri."

                    scene Zv2_ES3foot_p7

                    MC "Ooh! God… That’s amazing…"
                    if renpy.loadable("patch.rpy"):
                        MC "(I shouldn’t be doing this to Dad’s company… but they’re so fucking sexy…)"
                    else:
                        MC "(I shouldn’t be doing this to Bob’s company… but they’re so fucking sexy…)"
                    MC "(My cock is so hard right now!)"

                    scene Zv2_ES3foot_p8

                    MC "AH! Ahhh!"
                    Suri "Sounds like this kid isn’t gonna last much longer!"
                    Zuri "Aww, what a shame."

                    scene Zv2_ES3foot_p9

                    Suri "Are you gonna cum, kid?"
                    Zuri "Yeah, are you gonna cum all over our feet?"
                    MC "Mmmm! Ahhh…"

                    scene Zv2_ES3foot_p10

                    MC "Fuck! I’m cumming!"
                    MC "Hnnnnnngggg!"
                    Suri "That’s it, cum for me! Cum for me now!"
                    scene white with dissolve
                    $ renpy.pause(0.7, hard = True)
                    scene Zv2_ES3foot_p10
                    $ renpy.pause(0.7, hard = True)
                    scene white with dissolve
                    $ renpy.pause(0.7, hard = True)
                    scene Zv2_ES3foot_p11

                    Suri "Squirt your cum all over my toes!"
                    MC "AHH! AHHHHHH!"

                    scene Zv2_ES3foot_p11a

                    MC "Oooh….. (Pant Pant)"
                    Zuri "Wow! That’s a LOT of cum, Suri."
                    Suri "We can do this again, kid. All you have to do is get us more names. Okay?"
                    MC "(Pant) Y-Yeah, okay..."
                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False
                    jump pc_icon_label
        "{color=#ff8000}Blowjob.{/color}":

            scene Zv2_ES3_p1 with dissolve

            Zuri "Welcome back, [player_name]."
            Zuri "Thanks again for your help! Let’s go to our, room of pleasure."
            $ renpy.music.stop(channel="music1", fadeout=1)
            scene black
            $ renpy.pause(3, hard= True)
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            scene Zv2_ES3_p2

            Zuri "You’ve done another excellent job for us."
            Suri "Yeah, you really came through, kid. You’re gonna make us super rich!"
            MC "I get another reward now, right?"
            Suri "Hehe... You do. I believe we promised you a blowjob."



            scene Zv2_ES3lick_p1
            Suri "Mmm, I can’t wait to suck on his cock. It looked sooo delicious, last time we did it!"
            Zuri "Well? What are we waiting for? Let’s get these pants off him."
            MC "(This is gonna be great!)"

            scene Zv2_ES3lick_p2

            Suri "So, which of us gets to suck it first?"
            MC "I’m not fussy!"
            Zuri "Be my guest, Suri!"

            scene Zv2_ES3lick_p3

            Zuri "If you enjoy us doing this, then just wait til you see what we have in store for you, for the grand finale!"
            Suri "Yeah, we’ll blow your cock today, but next time - we’ll blow your mind!"

            scene Zv2_ES3lick_p4

            Suri "Are you always this hard, kid?"
            Suri "I don’t think I’ve ever seen you, without a massive erection."
            MC "It’s hard not to have one, when I’m near someone as beautiful as you."

            scene Zv2_ES3lick_p5

            Suri "Lick Lick"
            Zuri "Lick Lick"
            MC "Mmm… That’s good. RIght there…"

            scene Zv2_ES3a_p6

            Suri "Suuuuck"
            MC "Oooh…"
            MC "(I can feel Suri’s mouth, wrapped around the tip of my cock. It’s so hot and wet!)"

            scene Zv2_ES3a_p7

            MC "God… Mmmm…"
            scene Zv2_ES3a_p6anim
            Zuri "Lick Lick"
            scene Zv2_ES3a_p7anim
            Suri "Shluuurrrp"

            scene Zv2_ES3a_p8

            MC "(This is too much! Their tongues are so good!)"
            MC "(Who knew, corporate espionage could feel so right?)"
            Zuri "Mmmm…"
            Suri "Lick Lick"

            scene Zv2_ES3a_p9

            Zuri "Suck Suck"
            scene Zv2_ES3a_p9anim
            if renpy.loadable("patch.rpy"):
                MC "(Damn, Zuri is just as good at sucking cock, as her twin sister is!)"
            else:
                MC "(Damn, Zuri is just as good at sucking cock as Suri is!)"
            MC "(The two of them together, are fucking incredible!)"

            scene Zv2_ES3a_p10

            Zuri "GULP"
            MC "Fuck! Mmm!"
            MC "(I can feel Zuri’s tight throat around my glans!)"

            scene Zv2_ES3a_p11

            MC "(If she keeps this up, I’m gonna cum! It’s too intense!)"
            MC "Hnnng! Ahh!"
            Zuri "Shluuuuuurrrrp"

            scene Zv2_ES3a_p12

            Suri "MMPPFFF!!!"
            Zuri "Oops! Sorry, Suri!"
            MC "Ahhh! Huh?"

            scene Zv2_ES3a_p13
            if renpy.loadable("patch.rpy"):
                Zuri "Sorry, it looks like my sister’s head has... accidentally fallen on your cock."
            else:
                Zuri "Sorry, it looks like Suri's head has... accidentally fallen on your cock."
            Suri "Mmmpfff! SHLURRRRP"
            MC "Oh! Ahhhh!"

            scene Zv2_ES3a_p14

            MC "I’m cumming!"
            Zuri "Drink it ALL up, Suri!"
            Suri "SHLURRRP! COUGH!"
            MC "HNNNNNGGG!!! UGH! YES!"
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3a_p14 with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3a_p14 with dissolve
            MC "(I can feel my cock twitching in her mouth! She’s drinking me dry!)"

            scene Zv2_ES3a_p15

            MC "Wow… That was amazing..."
            Suri "Zuri! You naughty bitch!"
            Zuri "Hehe! I couldn’t resist!"
            Suri "I’m gonna have to spank you later on tonight, for that!"
            Zuri "Feel free to go now, [player_name]."
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump pc_icon_label