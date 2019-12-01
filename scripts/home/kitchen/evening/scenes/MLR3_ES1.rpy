image MLR3_ES1_p1 = "images/home/kitchen/evening/scenes/MLR3_ES1/1.jpg"
image MLR3_ES1_p2 = "images/home/kitchen/evening/scenes/MLR3_ES1/2.jpg"
image MLR3_ES1_p3 = "images/home/kitchen/evening/scenes/MLR3_ES1/3.jpg"
image MLR3_ES1_p4 = "images/home/kitchen/evening/scenes/MLR3_ES1/4.jpg"
image MLR3_ES1_p5 = "images/home/kitchen/evening/scenes/MLR3_ES1/5.jpg"
image MLR3_ES1_p6 = "images/home/kitchen/evening/scenes/MLR3_ES1/6.jpg"
image MLR3_ES1_p7 = "images/home/kitchen/evening/scenes/MLR3_ES1/7.jpg"
image MLR3_ES1_p8 = "images/home/kitchen/evening/scenes/MLR3_ES1/8.jpg"
image MLR3_ES1_p9 = "images/home/kitchen/evening/scenes/MLR3_ES1/9.jpg"
image MLR3_ES1_p10 = "images/home/kitchen/evening/scenes/MLR3_ES1/10.jpg"
image MLR3_ES1_p11 = "images/home/kitchen/evening/scenes/MLR3_ES1/11.jpg"
image MLR3_ES1_p12 = "images/home/kitchen/evening/scenes/MLR3_ES1/12.jpg"
image MLR3_ES1_p13 = "images/home/kitchen/evening/scenes/MLR3_ES1/13.jpg"
image MLR3_ES1_p14 = "images/home/kitchen/evening/scenes/MLR3_ES1/14.jpg"
image MLR3_ES1_p15 = "images/home/kitchen/evening/scenes/MLR3_ES1/15.jpg"
image MLR3_ES1_p16 = "images/home/kitchen/evening/scenes/MLR3_ES1/16.jpg"
image MLR3_ES1_p17 = "images/home/kitchen/evening/scenes/MLR3_ES1/17.jpg"

label MLR3_ES1:
    hide screen map_button
    if MLR3_ES1_end == True:
        show screen kitchen_evening_notclickable
        MC "I've already talked with them."
        hide screen kitchen_evening_notclickable
        jump kitchen_morning1
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer

    scene MLR3_ES1_p1 with dissolve
    if persistent.incest_patch == True:
        MC "(Huh, looks like [Mom_name] and Sara are hanging out. I’ve never seen them do much mother-daughter stuff together.)"
    else:
        MC "(Huh, looks like [Mom_name] and Sara are hanging out. I’ve never seen them do much stuff together.)"
    MC "(I wonder what they’re up to.)"
    Mom "Now, you have to turn on the gas first. Do you see the little knobs?"

    scene MLR3_ES1_p2

    Sara "These ones in a row?"
    Mom "Yeah, just twist them up until you hear the hiss. That’s the gas coming out. Now, press the button over here to spark it off."
    "*CLICK*"

    scene MLR3_ES1_p3

    Mom "There you go! That’s how to turn the hob on. Now that we’ve got that going, we can start preparing our vegetables."
    if persistent.incest_patch == True:
        MC "(I wonder why Mom is teaching Sis how to cook. Maybe this has something to do with what Dad said about Sara being devastated if he leaves?)"
    else:
        MC "(I wonder why Linda is teaching Sara how to cook. Maybe this has something to do with what Bob said about Sara being devastated if he leaves?)"

    MC "(Perhaps [Mom_name] is trying to get closer to Sara to try and soften the blow, if it ever happens.)"

    scene MLR3_ES1_p4

    Mom "Oh! Hey, [player_name]. I’m just teaching Sara how to cook here. Do you want to learn too?"
    MC "I’m okay, I was just passing by."
    MC "How’s it going, Sara? You haven’t burnt anything yet, have you?"

    scene MLR3_ES1_p5

    Sara "Oh, HA HA! Very funny."
    if persistent.incest_patch == True:
        Mom "[player_name] - stop teasing your sister! Apologise to her now."
    else:
        Mom "[player_name] - stop teasing Sara! Apologise to her now."

    MC "Sorry, Sara."
    Mom "Although, to be fair…"

    scene MLR3_ES1_p6

    Mom "...she DID burn the bacon. "
    MC "Ahaha! Really?"
    Sara "It wasn’t my fault… the oven was too hot!"

    scene MLR3_ES1_p7

    Mom "Someone got centigrade and fahrenheit mixed up when they were reading the cookbook. I had to chuck the bacon in the bin. It was blacker than tar and tougher than a hockey puck."
    MC "Ahh, so THAT’S what the awful smell is in here!"
    Sara "Hmmph… Why do we need centigrade AND fahrenheit? If there was only one, I wouldn't get all confused…"
    Mom "Haha, don’t worry, Dear. It’s better that this happens, when I’m around to help you fix things. Now, let’s get back on track."

    scene MLR3_ES1_p8

    MC "(I suppose it’s good to see [Mom_name] and Sara spending some quality time together.)"
    Sara "Anyway, I better get back to this before I destroy a second dinner!"
    Mom "Haha, at least you’re keeping positive about it. Check if the water is boiling in the pot yet."

    scene MLR3_ES1_p9

    Sara "Sure, [Mom_name]!"
    Mom "So, what are you up to now? Big plans for this evening?"
    MC "Nothing much, I was just going to-"
    "*THUNK*"

    scene MLR3_ES1_p10

    Sara "Eek!"
    Mom "Are you alright, Sara?"
    Sara "Oops! Sorry, I knocked over a can with my elbow."

    scene MLR3_ES1_p11

    MC "Don’t worry about it. I’ll grab that for you."
    Sara "Thanks, [player_name]!"

    scene MLR3_ES1_p12

    MC "(Hmm, Sara is wearing a REALLY short skirt today. I could try and peek up it while I’m down here.)"
    MC "(It’s not like either of them would notice - they’re both FAR too focused on their cooking!)"

    scene MLR3_ES1_p13

    MC "(Oh yeah! Her panties are so slim, I can almost see her vulva either side of them.)"
    MC "(It’s a shame Sara never goes commando, or I would have hit the jackpot right now.)"

    scene MLR3_ES1_p14
    if persistent.incest_patch == True:
        MC "(Oh fuck! There’s no way she saw me peeking up my sister’s skirt? Right?!)"
    else:
        MC "(Oh fuck! There’s no way she saw me peeking up my Sara’s skirt? Right?!)"

    MC "(Fuck… she looks shocked! There’s no doubt about it - she’s caught me. I am SO screwed...)"
    Mom "(Huh… I’m almost certain I caught [player_name] looking up Sara’s skirt. It was a little difficult to tell though.)"

    scene MLR3_ES1_p15

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)
    Mom "(Let’s put this to the test, and see if he’s interested in her.)"
    MC "(Holy shit! [Mom_name]’s holding Sara’s skirt up! No way!)"
    Sara "Ahh! It’s all bubbling out of the pot!"
    Mom "Easy, Dear. You just need to turn the heat down, a little."

    scene MLR3_ES1_p16

    MC "Where do you want this can put, Sara?"
    Sara "Oh! I forgot about that! Umm… just pass it to me. I’ll be using it now, anyway."
    MC "Sure thing."

    scene MLR3_ES1_p17
    if persistent.incest_patch == True:
        Mom "(My, my, my… I knew my boy was a horny guy, but I never imagined he’d be so bold, as to lust after his own sister.)"
    else:
        Mom "(My, my, my… I knew [player_name] was a horny guy, but I never imagined he’d be so bold as to lust after Sara.)"
    Mom "(Then again, I’d be a hypocrite to say anything on the subject.)"
    if persistent.incest_patch == True:
        Mom "See you later, [player_name]. I hope you enjoyed watching your sister… cook."
    else:
        Mom "See you later, [player_name]. I hope you enjoyed watching Sara… cook."
    MC "(She paused in that sentence on purpose! She definitely knows I was looking - but I don’t think she’s actually angry about it.)"
    MC "Y-Yeah, see you later, [Mom_name]."
    $ MLR2_R3_MS1_q9 = True
    $ MLR3_ES1_end = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump kitchen_morning1
