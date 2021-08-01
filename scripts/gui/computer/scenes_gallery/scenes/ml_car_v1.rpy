label mom_car_v1:
    hide screen scenes_gallery
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    scene black
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(I think Mom’s changing now. If I’m quick I might be able to sneak a peek!)"
    if not renpy.loadable("patch.rpy"):
        MC "(I think Linda’s changing now. If I’m quick I might be able to sneak a peek!)"
    scene ml_bedroom_morning_scene5_v1_p1 with dissolve
    MC "(Perfect timing!)"
    MC "(Damn! She’s got an incredible ass. And she looks so sexy in those black high heels.)"

    scene ml_bedroom_morning_scene5_v1_p2
    MC "(No! She’s walking out of sight!)"
    MC "(I’m gonna have to creep in further, or I’ll miss it!)"

    scene ml_bedroom_morning_scene5_v1_p3
    MC "(Aww - looks like she’s putting her panties back on.)"
    MC "(I was hoping I’d catch a glimpse of her pussy.)"

    scene ml_bedroom_morning_scene5_v1_p4
    MC "(This isn’t bad though! I could fap to the mental image of her ass for a week!)"
    MC "(I probably shouldn’t hang around much longer. She’s almost finished dressing.)"

    scene ml_bedroom_morning_scene5_v1_p5
    MC "(She’s so stunningly beautiful though.)"
    MC "(Looks like she’s grabbing a dress from her closet.)"

    scene ml_bedroom_morning_scene5_v1_p6
    MC "(Okay, that’s her almost finished getting dressed - I better bolt before she notices I’ve been peeping at her.)"
    scene ml_bedroom_morning_scene5_v1_p6
    if renpy.loadable("patch.rpy"):
        MC "(Actually - instead of leaving, I could take this chance to talk with Mom about getting a job.)"
        MC "Hey, Mom!"
    if not renpy.loadable("patch.rpy"):
        MC "(Actually - instead of leaving, I could take this chance to talk with Linda about getting a job.)"
        MC "Hey, Linda!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p7
    Mom "Hi, Sweetie. I didn’t I didn’t see you there. What’s up?"
    if renpy.loadable("patch.rpy"):
        MC "I had been talking with Dad, and he thought it would be a good idea for me to start earning money now."
    if not renpy.loadable("patch.rpy"):
        MC "I had been talking with Landlord and he thought it would be a good idea for me to start earning money now."
    MC "He said you might have some work for me?"

    scene ml_bedroom_morning_scene5_v1_p8
    Mom "Hmm… I’m not sure. I can’t think of any work I need done right now."
    MC "How about in your office building?"
    Mom "I’m not sure."
    if renpy.loadable("patch.rpy"):
        MC "Please, Mom! I really need the money. I can’t just keep begging Dad for spare change!"
    if not renpy.loadable("patch.rpy"):
        MC "Please, Linda! I really need the money. I can’t just keep begging Landlord for spare change!"

    scene ml_bedroom_morning_scene5_v1_p9
    Mom "Well… Maybe."
    Mom "There’s a small possibility that I could give you a job."
    Mom "It comes with a condition though."

    scene ml_bedroom_morning_scene5_v1_p10
    MC "Awesome! What’s the condition?"
    Mom "I’ll tell you later. In the meantime, just follow me."
    MC "Great!"
    scene black
    $ renpy.sound.play('/sfx/car_start.mp3')
    $ renpy.pause(2, hard = True)

    scene ml_bedroom_morning_scene5_v1_p11
    if renpy.loadable("patch.rpy"):
        MC "Where are we going, Mom?"
    if not renpy.loadable("patch.rpy"):
        MC "Where are we going, Linda?"
    Mom "Just one more turn and then we’ll be there. "
    Mom "This is one of the car parks, near where I work."
    MC "Oh, right."

    scene ml_bedroom_morning_scene5_v1_p12
    MC "It looks pretty desolate."
    Mom "Yeah - nobody ever comes into here apart from me."
    Mom "(And having no people around, is essential for what I’m about to try next.)"

    scene ml_bedroom_morning_scene5_v1_p13
    MC "So? What’s this condition?"
    Mom "Just wait a minute. I need to plan it first."
    Mom "(Okay, you can do this. You’ve rehearsed it in your mind a hundred times!)"

    scene ml_bedroom_morning_scene5_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Is everything okay, Mom? You’re looking a little nervous."
    if not renpy.loadable("patch.rpy"):
        MC "Is everything okay, Linda? You’re looking a little nervous."
    Mom "I’m fine. Okay, here’s what’s going to happen."

    scene ml_bedroom_morning_scene5_v1_p15
    Mom "The condition is, that you sit completely still for one full minute. Close your eyes and act like a doll."
    MC "Huh?"
    Mom "You aren’t allowed to react. And you aren’t allowed to talk about it later on."
    $ ml_bedroom_morning_scene5_v1_label2_menu_q1 = True
    $ ml_bedroom_morning_scene5_v1_label2_menu_q2 = True
    $ ml_bedroom_morning_scene5_v1_label2_menu_q3 = True
    jump ml_bedroom_morning_scene5_v1_label2_menu1r
label ml_bedroom_morning_scene5_v1_label2_menu1r:
    scene ml_bedroom_morning_scene5_v1_p14
    menu:
        "Why? I don’t understand." if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True:

            MC "Why? I don’t understand why I’d have to do this to get a job."
            Mom "I’m not asking you to understand - it’s simply the condition I’ve laid out."

            $ ml_bedroom_morning_scene5_v1_label2_menu_q1 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q2 == True and ml_bedroom_morning_scene5_v1_label2_menu_q3 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
        "What if I open my eyes or move? " if ml_bedroom_morning_scene5_v1_label2_menu_q2 == True:

            MC "What happens if I open my eyes or move?"
            scene ml_bedroom_morning_scene5_v1_p15
            Mom "Then the condition is forfeit, and you won’t get the job."
            MC "Alright…"

            $ ml_bedroom_morning_scene5_v1_label2_menu_q2 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True and ml_bedroom_morning_scene5_v1_label2_menu_q3 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
        "What if I have questions after the minute is up?" if ml_bedroom_morning_scene5_v1_label2_menu_q3 == True:

            MC "What if I have questions after the minute is up?"
            scene ml_bedroom_morning_scene5_v1_p15
            Mom "You’ll just have to contain your curiosity - because if you ask me ANY questions about what happens, you won’t be getting that job."
            if renpy.loadable("patch.rpy"):
                MC "(Gee… Mom’s pretty serious about this.)"
            if not renpy.loadable("patch.rpy"):
                MC "(Gee… Linda’s pretty serious about this.)"

            $ ml_bedroom_morning_scene5_v1_label2_menu_q3 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True and ml_bedroom_morning_scene5_v1_label2_menu_q2 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
label ml_bedroom_morning_scene5_v1_label2_menu_after1r:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p16
    MC "Okay - that’s me ready."
    Mom "The minute starts now. Remember, no talking, moving, or asking questions after."

    scene ml_bedroom_morning_scene5_v1_p17
    MC "(One… Two… Three…)"
    MC "(She’s just put her hand on my shoulder. Nothing too strange yet…)"
    MC "(Seven… Eight… Nine…)"

    scene ml_bedroom_morning_scene5_v1_p18
    Mom "(God… He’s so handsome.)"
    Mom "(I have to kiss him. This could be my only chance.)"
    if renpy.loadable("patch.rpy"):
        Mom "(I hope he doesn’t say anything to his father about this.)"
    if not renpy.loadable("patch.rpy"):
        Mom "(I hope he doesn’t say anything to Landlord about this.)"

    scene ml_bedroom_morning_scene5_v1_p19
    Mom "(Here we go… Now or never!)"
    MC "(Thirteen… Fourteen… Fifteen…)"
    MC "(What’s she doing?)"

    scene ml_bedroom_morning_scene5_v1_p20
    MC "(OH MY GOD!)"
    scene ml_bedroom_morning_scene5_v1_p20anim with dissolve
    if renpy.loadable("patch.rpy"):
        MC "(Mom’s full-on making out with me!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Linda’s full-on making out with me!)"
    MC "(I can feel her tongue in my mouth, and everything!)"

    scene ml_bedroom_morning_scene5_v1_p21
    MC "(I… I’ve lost count. Was I on twenty or thirty?)"
    scene ml_bedroom_morning_scene5_v1_p21anim with dissolve
    Mom "(Why did I only say a minute? I could have said two or three…)"
    Mom "(I wish this moment would last forever. It’s like a dream come true, right now.)"

    scene ml_bedroom_morning_scene5_v1_p22
    if renpy.loadable("patch.rpy"):
        Mom "(If I think about this when his father fucks tonight, I might even climax, for a change.)"
    if not renpy.loadable("patch.rpy"):
        Mom "(If I think about this when Bob fucks tonight, I might even climax, for a change.)"
    Mom "(I have to contain myself… but right now, I could just rip [player_name]’s clothes off and ride him in the car seat.)"

    scene ml_bedroom_morning_scene5_v1_p23
    Mom "(I have to know if he’s hard. I have to know if he’s enjoying this as much as I am…)"
    Mom "(I’ll just move my hand down quickly, then take it away.)"

    scene ml_bedroom_morning_scene5_v1_p24
    Mom "(He’s hard! There’s no question about it.)"
    Mom "(It also feels like he’s got a pretty sizeable member.)"
    Mom "(If only I could feel it, hard and throbbing, deep inside my pussy!)"
    MC "(Holy shit! Did she just grope my crotch?! She HAS to have done that on purpose, right?) "
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p25
    Mom "O-Okay, that’s a minute up now."
    Mom "(Wow… That was… something else.)"
    MC "C-Can I talk now?"
    Mom "Yes, but you can’t speak about what happened."

    scene ml_bedroom_morning_scene5_v1_p26
    MC "Oh… O-Okay…"
    if renpy.loadable("patch.rpy"):
        MC "(Why would she do that? I don’t understand it… She’s my mother.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Why would she do that? I don’t understand it… She’s my friend.)"
    MC "(I mean, unless she has a crush on me, or something? But that doesn't make sense.)"
    if renpy.loadable("patch.rpy"):
        MC "(If Mrs. Celia didn’t want to date me, how could my own mom be interested?)"
    if not renpy.loadable("patch.rpy"):
        MC "(If Mrs. Celia didn’t want to date me, how could my own friend be interested?)"

    scene ml_bedroom_morning_scene5_v1_p27
    Mom "Ahem... I work in the building, just round the front of this carpark."
    Mom "If you drop by tomorrow afternoon, I’ll set you up with a job."
    if renpy.loadable("patch.rpy"):
        MC "Th-Thanks, Mom."
    if not renpy.loadable("patch.rpy"):
        MC "Th-Thanks, Linda."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label