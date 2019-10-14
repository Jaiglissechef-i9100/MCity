image MLR3_beach_drink_p1 = "images/Beach/MLR3_beach_event/drinks/1.jpg"
image MLR3_beach_drink_p1a = "images/Beach/MLR3_beach_event/drinks/1a.jpg"
image MLR3_beach_drink_p2 = "images/Beach/MLR3_beach_event/drinks/2.jpg"
image MLR3_beach_drink_p3 = "images/Beach/MLR3_beach_event/drinks/3.jpg"
image MLR3_beach_drink_p4 = "images/Beach/MLR3_beach_event/drinks/4.jpg"
image MLR3_beach_drink_p5 = "images/Beach/MLR3_beach_event/drinks/5.jpg"
image MLR3_beach_drink_p6 = "images/Beach/MLR3_beach_event/drinks/6.jpg"
image MLR3_beach_drink_p7 = "images/Beach/MLR3_beach_event/drinks/7.jpg"
image MLR3_beach_drink_p8 = "images/Beach/MLR3_beach_event/drinks/8.jpg"
image MLR3_beach_drink_p9 = "images/Beach/MLR3_beach_event/drinks/9.jpg"
image MLR3_beach_drink_p10 = "images/Beach/MLR3_beach_event/drinks/10.jpg"
image MLR3_beach_drink_p11 = "images/Beach/MLR3_beach_event/drinks/11.jpg"

default beach_buy_B2_talk = False

label MLR3_beach_drink:
    hide screen map_button
    scene shop_M_map
    if not drink in inventory.items and beach_buy_B2_talk == False:

        show screen beach_shop_M_scr
        $ clickable = False
        MC "Do you fancy grabbing something to drink, [Mom_name]?"
        Mom "Yeah, I’m parched. There’s a little shop just at the end of the beach. We could go there together."
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen beach_shop_M_scr
        scene black
        $ renpy.pause(2, hard = True)
        scene MLR3_beach_drink_p1 with dissolve
        $ can_hide_windows = True
        MC "Take a seat, I’ll grab us drinks."
        Mom "No, don’t you worry, I’ll get them."
        MC "[Mom_name] - you paid for this whole holiday! Let me get us drinks at the very least! Now, what do you want?"

        scene MLR3_beach_drink_p1a

        Mom "Well… if you insist. Hmm… I think I’ll just take a Cocka Cola."
        MC "That’s two Cocka Colas then. I’ll be back in a minute, [Mom_name]."
        Mom "Sure thing!"
        $ can_hide_windows = False
        $ clickable = True
        $ beach_buy_B2_talk = True

        jump beach_shop_M1
    if not drink in inventory.items and beach_buy_B2_talk == True:
        show screen beach_shop_M_scr
        $ clickable = False
        MC "I have to buy drinks from the beach shop."
        hide screen beach_shop_M_scr
        $ clickable = True
        jump beach_shop_M1
    if drink in inventory.items:
        jump MLR3_beach_drink2

label MLR3_beach_drink2:
    scene shop_M_map
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer

    scene MLR3_beach_drink_p2 with dissolve
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    MC "There you go! One ice cold, Cocka Cola."
    Mom "Thanks! God, I didn’t realise how hot it actually was out here until you handed me this."
    MC "I know! I must be at least eighty degrees today."

    scene MLR3_beach_drink_p3

    Mom "What’s that in celsius? Twenty eight?"
    MC "Around that maybe. I use Fahrenheit more often."
    MC "You look fantastic in that bikini by the way. You should wear it more often."
    Mom "Haha! Like around the house or in my office?! That’s the only two places I ever seem to be! At least, it feels that way sometimes with how damn busy I am."

    scene MLR3_beach_drink_p4

    Mom "*Glug Glug*"
    MC "You could always go sunbathing in the garden, or we could hit the local pool together."
    MC "It gives you an excuse to wear it."

    scene MLR3_beach_drink_p5

    Mom "But MORE importantly, it gives YOU a chance to see me wear it. Am I right?"
    MC "Haha! You got me there!"
    Mom "Of course I did. Although… if it was in our back garden, I guess I could sunbathe topless."
    if renpy.loadable("patch.rpy"):
        Mom "How could I possibly know that you’d be peeping down at me from your bedroom window? There’s no way your sisters or Bob would suspect anything."
    else:
        Mom "How could I possibly know that you’d be peeping down at me from your bedroom window? There’s no way your roommates or Bob would suspect anything."
    scene MLR3_beach_drink_p6

    Mom "I could casually just roll over and flash my sunscreen soaked tits up at you."
    Mom "If there was no one else around I’m might even take a selfie or two for you."

    scene MLR3_beach_drink_p7

    MC "Mmm, that does sound good!"
    Mom "The only downside about staying back home is that there’s no water to go swimming in to cool down. "
    Mom "Ah well, I guess that’s the price I have to pay for topless sunbathing."

    scene MLR3_beach_drink_p8

    MC "You could lose your bikini bottoms too. That would REALLY give me something to enjoy!"
    Mom "[player_name]!"
    MC "Aww, c’mon! I know you love being watched. It’s hardly a surprise! Remember how hot and bothered you got during our restaurant date?"

    scene MLR3_beach_drink_p9

    Mom "Haha! True…"
    MC "I’m sure you would be soaking wet within seconds if you took your bottoms off. Just knowing that I’m watching you from my window would really turn you on-"
    Mom "Okay! Enough! Haha, you’re gonna turn me on right NOW if you don’t cut it out."

    scene MLR3_beach_drink_p10

    MC "Haha, sorry [Mom_name], I couldn’t resist."
    Mom "*Glug Glug*"

    scene MLR3_beach_drink_p11

    Mom "Ahh, thanks for the Cocka Cola. That was really refreshing."
    MC "Glad you enjoyed it!"
    Mom "Shall we head back to the beach now?"
    MC "Yeah, let’s go."
    $ inventory.drop(drink)
    $ can_hide_windows = False
    $ MLR3_beach_drink = False
    $ MLR3_beach_done += 1
    $ beach_buy_B2_talk = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump beach_shop_M1
