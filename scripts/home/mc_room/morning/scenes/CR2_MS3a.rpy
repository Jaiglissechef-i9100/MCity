label CR2_MS3a_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_MS3_p1 with dissolve
    $ can_hide_windows = True
    MC "What’s up? You’re looking glum again."
    Caroline "Things aren’t… I’m sorry, I should go."
    MC "Wait- what’s wrong?"

    scene CR2_MS3_p2

    Caroline "Things aren’t picking up at the shop as quickly as I originally thought they would."
    MC "Oh no... Is everything okay?"
    Caroline "N-Not really… I owe a hundred and fifty in rent, for the shop this time."
    Caroline "I was wondering if…"

    scene CR2_MS3_p1

    MC "You were wondering if you could borrow it from me?"
    Caroline "I’m so sorry, [player_name]. I don’t want to be a burden."
    window hide
    menu:
        "Yeah, I have $150 here. There you go. (disabled)" if inventory.money < 150:
            $ can_hide_windows = False
            jump mc_room_morning1

        "{color=#00ff00}Yeah, I have $150 here. There you go.{/color}" if inventory.money >= 150:
            scene CR2_MS3_p3

            MC "It was a hundred and fifty dollars, right?"
            Caroline "Yeah."
            MC "Luckily for you, I have that right here."
            Caroline "R-Really?"

            scene CR2_MS3_p4

            Caroline "Are you sure I can just have this?"
            if persistent.incest_patch == True:
                MC "Absolutely! I said it last time, and I’ll say it again - you’re my sister. We have to take care of each other."
            else:
                MC "Absolutely! I said it last time, and I’ll say it again - you’re my friend. We need to look out for each other."
            Caroline "Thank you so much!"

            scene CR2_MS3_p5

            Caroline "I never knew you cared about me this much. It’s really sweet of you to do this."
            MC "Please, don’t think anything of it."

            scene CR2_MS3_p6

            Caroline "I’m a really lucky girl. You know that?"
            Caroline "*Mwah!*"
            MC "(She actually kissed me! Caroline hasn’t done that in… never!)"

            scene CR2_MS3_p7

            Caroline "Actually, before I go… just one quick question."
            MC "Yes, Caroline?"
            Caroline "Are you giving me this money because…"
            Caroline "..."

            scene CR2_MS3_p8

            MC "Because what, Caroline?"
            Caroline "Nevermind. Meet me outside the front of our house tonight, and we can talk about it."
            MC "Okay, I’ll see you there."
            Caroline "Thanks again, [player_name]."
            $ CR2_MS3a = False
            $ CR2_NS2 = True
            $ inventory.drop_money(150)
            $ sms3_fromC = True
            $ CR2_ES2 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
        "Sorry, I don’t have $150 on me right now.":

            scene CR2_MS3_p2

            MC "I’m so sorry, Caroline. I don’t have that kinda money right now."
            Caroline "I-It’s okay, I can push things back for a few days."
            MC "I’m really sorry."
            Caroline "Don’t apologise. This isn’t your fault."
            $ can_CR2_MS3a = True
            $ CR2_MS3a = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1

