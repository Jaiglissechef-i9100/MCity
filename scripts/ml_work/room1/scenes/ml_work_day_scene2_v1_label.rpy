image ml_work_day_scene2_v1_p1 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/1.jpg"
image ml_work_day_scene2_v1_p2 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/2.jpg"
image ml_work_day_scene2_v1_p3 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/3.jpg"
image ml_work_day_scene2_v1_p4 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/4.jpg"
image ml_work_day_scene2_v1_p5 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/5.jpg"
image ml_work_day_scene2_v1_p6 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/6.jpg"
image ml_work_day_scene2_v1_p7 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/7.jpg"
image ml_work_day_scene2_v1_p8 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/8.jpg"
image ml_work_day_scene2_v1_p9 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/9.jpg"
image ml_work_day_scene2_v1_p10 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/10.jpg"
image ml_work_day_scene2_v1_p11 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/11.jpg"
image ml_work_day_scene2_v1_p12 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/12.jpg"
image ml_work_day_scene2_v1_p13 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/13.jpg"
image ml_work_day_scene2_v1_p14 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/14.jpg"
image ml_work_day_scene2_v1_p15 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/15.jpg"
image ml_work_day_scene2_v1_p16 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/16.jpg"
image ml_work_day_scene2_v1_p17 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/17.jpg"
image ml_work_day_scene2_v1_p18 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/18.jpg"
image ml_work_day_scene2_v1_p19 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/19.jpg"
image ml_work_day_scene2_v1_p19a = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/19a.jpg"
image ml_work_day_scene2_v1_p20 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/20.jpg"
image ml_work_day_scene2_v1_p21 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/21.jpg"

image ml_work_day_scene2_v1_p6anim = Movie(play="videos/Linda-AfternoonS2-1.webm", loop = True )
image ml_work_day_scene2_v1_p6anim2 = Movie(play="videos/Linda-AfternoonS2-2.webm", loop = True )
image ml_work_day_scene2_v1_p15anim = Movie(play="videos/Linda-AfternoonS2-4.webm", loop = True )
image ml_work_day_scene2_v1_p17anim = Movie(play="videos/Linda-AfternoonS2-3.webm", loop = True )
image ml_work_day_scene2_v1_p18anim = Movie(play="videos/Linda-AfternoonS2-5.webm", loop = True )

label ml_work_day_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Hi, Mom! That’s me back again."
    if not renpy.loadable("patch.rpy"):
        MC "Hi, Linda! That’s me back again."
    Mom "Great! If you just do the same as last time."
    Mom "Is $25 okay for you again?"
    MC "Sure. No problem."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_room2_label

label ml_work_day_scene2_v1_label_after_work:
    scene black
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    MC "(That’s me done for the day.)"
    if renpy.loadable("patch.rpy"):
        MC "(Time to go back to Mom and get my money.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Time to go back to Linda and get my money.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_work_day_scene1_v1_p3 with dissolve
    MC "That’s it all done."
    Mom "Great!"

    scene ml_work_day_scene1_v1_p4
    Mom "Say - would you fancy sitting on the couch with me for a while?"
    MC "Sure."

    scene ml_work_day_scene2_v1_p2
    MC "(She just sat down on my knee! I didn’t expect that!)"
    Mom "You’ve got beautiful eyes, [player_name]. You know that?"
    if renpy.loadable("patch.rpy"):
        MC "Gee… Thanks, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "Gee… Thanks, Linda."
    Mom "You really do. I could gaze into them for hours."

    scene ml_work_day_scene2_v1_p3
    MC "(Gulp!)"
    Mom "You look a little nervous."
    Mom "You shouldn’t be. I promise, you’re in very safe hands right now."
    Mom "Try relaxing. Put your hand on my thigh."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene ml_work_day_scene2_v1_p4
    Mom "That’s it. See?"
    Mom "I can hear your heart pounding from here."
    Mom "Just try to breathe, and close your eyes."
    Mom "I promise you’ll enjoy this."

    scene ml_work_day_scene2_v1_p5
    MC "(Oh, my God… It’s really happening. She’s not worried about scaring me off anymore!)"
    MC "(How far is she going to take this, today? Just a kiss?)"

    scene ml_work_day_scene2_v1_p6
    Mom "Mmm…"
    scene ml_work_day_scene2_v1_p6anim with dissolve
    MC "Mmm!"
    scene ml_work_day_scene2_v1_p6anim2
    MC "(Wow! She’s an amazing kisser!)"

    scene ml_work_day_scene2_v1_p7
    Mom "(God… This is even better than I dreamt it would be.)"
    Mom "(I wish I could just freeze this moment, and stay right here forever.)"
    if renpy.loadable("patch.rpy"):
        MC "(Mom must be getting nervous too - I can hear her heart beating, even louder than mine!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Linda must be getting nervous too - I can hear her heart beating, even louder than mine!)"

    scene ml_work_day_scene2_v1_p8
    Mom "Lie down on the couch beside me. I want to do something for you."
    MC "D-Do something? Like what?"
    if renpy.loadable("patch.rpy"):
        Mom "Hush… Just you lie back and relax. Mommy will take care of everything."
    if not renpy.loadable("patch.rpy"):
        Mom "Hush… Just you lie back and relax. I will take care of everything."

    scene ml_work_day_scene2_v1_p9
    MC "Ooohh…."
    MC "(Holy shit… I can feel her fingers, wrapping around my cock.)"
    MC "(She’s massaging it now.)"

    scene ml_work_day_scene2_v1_p10
    if renpy.loadable("patch.rpy"):
        MC "M-Mom! Y-You-"
    if not renpy.loadable("patch.rpy"):
        MC "L-Linda. Y-You-"
    Mom "Shush… I see you’ve got a hard problem, down here."
    if renpy.loadable("patch.rpy"):
        Mom "Let Mother help you sort it out."
    if not renpy.loadable("patch.rpy"):
        Mom "Let me help you sort it out."

    scene ml_work_day_scene2_v1_p11
    Mom "(Mmm… It’s so big!)"
    Mom "(I’d love to feel this monster inside me. Filling up my pussy!)"
    Mom "(God, I’m getting wet at the mere thought of it!)"

    scene ml_work_day_scene2_v1_p12
    Mom "Does it feel good when I circle my fingers around, this little bit at the top?"
    MC "Ah… yes..."
    Mom "I’ll tell you why it’s so sensitive."

    scene ml_work_day_scene2_v1_p13
    Mom "It’s called the frenulum - and it’s a sensitive little cluster of nerves."
    Mom "A secret trick of mine, back in school, was to rapidly flick my tongue back and forth across it."
    Mom "No guy could last thirty seconds, when getting one of MY blowjobs."

    scene ml_work_day_scene2_v1_p14
    Mom "But enough foreplay - let’s get down to business."
    MC "Ah! Ahh… Oohhh!"
    if renpy.loadable("patch.rpy"):
        Mom "Mmm... sounds like my boy’s enjoying this."
    else:
        Mom "Mmm... sounds like my toyboy is enjoying."

    scene ml_work_day_scene2_v1_p15
    MC "Oooh!"
    scene ml_work_day_scene2_v1_p15anim
    if renpy.loadable("patch.rpy"):
        MC "(Oh, my God! I never imagined, Mom would be this kinky!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Oh, my God! I never imagined, Linda would be this kinky!)"
    Mom "(Haha! I felt him shudder as I licked him. He’ll be cumming for me, in no time.)"

    scene ml_work_day_scene2_v1_p16
    Mom "Up and down…"
    Mom "Up… and down."
    Mom "I hope you’re enjoying this as much as I am."

    scene ml_work_day_scene2_v1_p17
    MC "Ahh…"
    scene ml_work_day_scene2_v1_p17anim
    Mom "Are you close?"
    Mom "I want you to cum for me."

    scene ml_work_day_scene2_v1_p18
    MC "Mmm! MMMMM!"
    MC "(Fuck! I’m gonna cum!)"
    scene ml_work_day_scene2_v1_p18anim
    Mom "Mmm…"
    Mom "(I can feel his cock, twitching and throbbing in my hand. My boy’s about to blow his load!)"

    scene ml_work_day_scene2_v1_p19
    if renpy.loadable("patch.rpy"):
        Mom "That’s it! Cum for Mommy! Good boy!"
    if not renpy.loadable("patch.rpy"):
        Mom "That’s it! Cum for Linda! Good boy!"
    MC "Ahh! Ooooh! Ahhhh!"
    scene white with dissolve
    $ renpy.pause(1,hard=True)
    scene ml_work_day_scene2_v1_p19
    $ renpy.pause(1,hard=True)
    scene white with dissolve
    $ renpy.pause(1,hard=True)
    scene ml_work_day_scene2_v1_p19a with dissolve
    Mom "Wow… That’s a lot of cum! You’re lucky you had me around, to relieve you."

    scene ml_work_day_scene2_v1_p20
    Mom "Is that you all finished? Or should I keep going?"
    MC "N-No, I’m… I’m done..."
    Mom "So, how was it? Did you enjoy it?"

    scene ml_work_day_scene2_v1_p21
    if renpy.loadable("patch.rpy"):
        MC "It was amazing, Mom! Thank you!"
    if not renpy.loadable("patch.rpy"):
        MC "It was amazing, Linda! Thank you!"
    Mom "I’m very happy to hear that."
    Mom "You make SUCH a cute face when you cum!"
    if renpy.loadable("patch.rpy"):
        MC "MOM!"
        Mom "Haha! I better get back to work. I’ll see you, later this evening."
        MC "See ya, Mom. Thanks again."
    if not renpy.loadable("patch.rpy"):
        MC "Linda!"
        Mom "Haha! I better get back to work. I’ll see you, later this evening."
        MC "See ya, Linda. Thanks again."
    $ inventory.earn(25)
    $ ml_work_day_scene2 = False
    $ ml_mc_room_night_scene3 = True
    $ SR2_ML = True
    $ day_time = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_sms1_from_ml = True
    $ can_hide_windows = False
    jump map_label
