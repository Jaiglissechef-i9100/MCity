

label Z_ES2_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Z_ES2_p1 with dissolve
    $ can_hide_windows = True
    MC "Well, I did exactly what you asked for. I got you the company name."
    Zuri "And you did excellently. We have already begun buying up shares, in order to assume a voting majority within the company."
    Suri "And we couldn’t have done it without your help."
    MC "Well… What’s the reward you have in mind?"
    Zuri "Follow me. "
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES2_p2

    Zuri "Suri is all yours tonight, [player_name]. Go ahead and play with her breasts."

    Suri "You can do whatever you want with my tits, [player_name]."
    MC "(This is gonna be awesome!)"


    scene Z_ES2_p3

    Suri "So, what do you think, kid?"
    MC "They’re amazing!"
    Suri "Hehe... I thought so."

    scene Z_ES2_p4

    Suri "You want to play with them, don’t you?"
    MC "Oh yeah!"
    Suri "They’re all yours. And there will be, much much more to come, if you give us more names."

    scene Z_ES2_p5

    Suri "Now, let’s get started with your reward."
    Suri "Try to relax - don’t be shy."
    MC "(God! I wish I could fuck both of them at the same time! That would be the hottest thing ever!)"

    scene Z_ES2_p6

    Suri "Ooh, I can feel your hard cock through your jeans. It seems like someone is getting excited by this!"
    MC "It’s hard not to get excited, when I’ve got a sexy girl like you on my lap."
    Suri "Hehe! Okay, so what do you want to do to my titties?"

    scene Z_ES2_p7

    MC "I can do anything?"
    Suri "Anything you want, kid."
    MC "Hmm…"
    $ menu_q1 = True
    $ menu_q2 = True
    $ menu_q3 = True
    jump Zv2_ES2_menu_rep

label Zv2_ES2_menu_rep:
    scene Z_ES2_p7
    window hide
    menu:
        "Pinch her nipples." if menu_q1 == True:
            scene Z_ES2_p8a

            MC "(I think I’ll start by pinching and squeezing her nipples a bit.)"
            Suri "Mmm, you naughty boy."
            Suri "Do you like teasing my nipples like that?"

            scene Z_ES2_p8aa

            Suri "Oooh! That’s good…."
            if renpy.loadable("patch.rpy"):
                Zuri "My sister LOVES having her nipples played with. She can turn into a real slut if a guy turns her on enough."
            else:
                Zuri "Suri LOVES having her nipples played with. She can turn into a real slut if a guy turns her on enough."
            Suri "Ignore her, kid. She’s just trying to embarass me."
            $ menu_q1 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue_rep
            else:
                jump Zv2_ES2_menu_rep

        "Grope her breasts." if menu_q2 == True:
            scene Z_ES2_p8b

            MC "(Let’s grope and squeeze Suri’s breasts!)"
            MC "These are really soft, Suri!"
            Suri "Hehe. I know. Zuri likes to use them as a pillow, some nights."
            MC "Really?"

            scene Z_ES2_p8bb

            Zuri "SURI! That’s supposed to be a secret!"
            Suri "Oh, come on. You’ve done MUCH more to me than simply using my breasts as a pillow."
            Zuri "(Sigh) That’s very true."
            MC "(These girls are total nymphos!)"
            $ menu_q2 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue_rep
            else:
                jump Zv2_ES2_menu_rep

        "Suck on her nipples." if menu_q3 == True:
            scene Z_ES2_p8c

            MC "(Okay, let’s see how she likes it when I suck on her nipples.)"
            Suri "Ooooh! Hehe! That really tickles!"
            Zuri "Don’t be afraid to bite a little with your teeth. She’s kinky like that!"
            Suri "Zuri! Stop it! Hehe!"

            scene Z_ES2_p8cc

            Suri "Oooh! Ahhh! Oh, my God! Mmm!"
            MC "(Suck suck!)"
            Suri "Ooohhh…."
            $ menu_q3 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue_rep
            else:
                jump Zv2_ES2_menu_rep

label Zv2_ES2_continue_rep:
    scene Z_ES2_p9

    Zuri "(The fuck is she doing…?)"
    Zuri "Oh, come on Suri. You’re not seducing him at all!"
    Suri "I’m trying, Zuri!"
    Zuri "Please, you’re acting like a mom with her child! Let me help."

    scene Z_ES2_p10

    Suri "Hey! I had this!"
    Zuri "Of course you did. I’m just here to give you a hand."
    Suri "Fine…"

    scene Z_ES2_p11

    Zuri "I was able to get us the first name. If we work together, I’m sure we can convince [player_name] to give us some more."
    Suri "Ahh… yes!"

    scene Z_ES2_p12

    Suri "So, what do you say, [player_name]?"
    Suri "Next time you get us a company name, you’ll get to enjoy both of us at the same time. How does that sound?"
    MC "Fucking amazing!"
    Zuri "I thought so too."

    scene Z_ES2_p13

    Zuri "I have to promise you - you are in for a night you will NEVER forget."
    Suri "All you have to do is get us that name."
    Suri "And then we’ll suck and fuck your brains out, kid."

    scene Z_ES2_p14

    Zuri "Do we have a deal?"
    MC "(God… They’re irresistible!)"
    MC "Hell yeah..."
    Zuri "That’s what we like to hear!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label