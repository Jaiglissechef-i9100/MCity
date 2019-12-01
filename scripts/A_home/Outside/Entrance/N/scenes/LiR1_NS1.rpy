image LiR1_NS1_p1 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/1.jpg"
image LiR1_NS1_p2 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/2.jpg"
image LiR1_NS1_p3 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/3.jpg"
image LiR1_NS1_p4 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/4.jpg"
image LiR1_NS1_p5 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/5.jpg"
image LiR1_NS1_p6 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/6.jpg"
image LiR1_NS1_p7 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/7.jpg"
image LiR1_NS1_p8 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/8.jpg"
image LiR1_NS1_p9 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/9.jpg"
image LiR1_NS1_p10 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/10.jpg"
image LiR1_NS1_p11 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/11.jpg"
image LiR1_NS1_p12 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/12.jpg"
image LiR1_NS1_p13 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/13.jpg"
image LiR1_NS1_p14 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/14.jpg"
image LiR1_NS1_p15 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/15.jpg"
image LiR1_NS1_p16 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/16.jpg"
image LiR1_NS1_p17 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/17.jpg"
image LiR1_NS1_p18 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/18.jpg"
image LiR1_NS1_p19 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/19.jpg"
image LiR1_NS1_p20 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/20.jpg"
image LiR1_NS1_p21 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/21.jpg"
image LiR1_NS1_p21anim = Movie(play="videos/04 Liza-NS1-1.webm", loop = True )
image LiR1_NS1_p22 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/22.jpg"
image LiR1_NS1_p22anim = Movie(play="videos/04 Liza-NS1-2.webm", loop = True )
image LiR1_NS1_p23 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/23.jpg"
image LiR1_NS1_p24 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/24.jpg"
image LiR1_NS1_p25 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/25.jpg"
image LiR1_NS1_p26 = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/26.jpg"

image LiR1_NS1_sleeping = "images/a_home/Outside/Entrance/N/Scenes/LiR1_NS1/27.jpg"
label LiR1_NS1_label:
    if persistent.incest_patch == True:
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"

    if LiR1_NS4 == True:
        jump LiR1_NS4_label
    if LiR1_NS2 == True:
        jump LiR1_NS2_label
    if LiR1_NS1 == True:
        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene ClimbingSuccess_p4
        MC "(Alright, I should have a good view, from up here...)"

        scene LiR1_NS1_p1 with dissolve

        MC "*Whistle*"
        MC "(Looks like it’s my lucky day! I’ve caught the two of them, just before they were about to start!)"
        MC "(Yazmin is certainly - dressed for the occasion. She might have smaller breasts than [Liza2_name], but she’s certainly making up for it - downstairs - tonight!)"

        scene LiR1_NS1_p2

        MC "(I wonder what they’re talking about... if I lean in closer, I might be able to hear some of their conversation.)"
        Liza2 "...it’s not the first time you’ve wanted to use that strap-on."
        Liza2 "I’m not saying I want you to take it off... I just... don’t swing that way. Phallic shapes, really don't do anything for me."

        scene LiR1_NS1_p3

        Yazmin "Oh c’mon! You must enjoy it - even just a little bit!"
        Yazmin "I’ve heard - how loudly - you moan, when I fuck you with - this bad boy."
        Liza2 "Yeah, well... it’s not as enjoyable as the times, when you use your fingers... or even your tongue."

        scene LiR1_NS1_p4

        Yazmin "That’s alright. I understand. Can we try using it tonight, though? It took me nearly - five full minutes - to get all these buckles on."
        Liza2 "(Sigh) Okay, we can use it tonight. You owe me another romantic dinner, though? Okay?"
        Yazmin "We’ll go wherever you want, Liza."

        scene LiR1_NS1_p5

        Liza2 "I assume you want me to do the ‘blowjob fantasy’ for you again."
        Yazmin "You know me too well, Honey."
        Liza2 "(Sigh) I don’t understand what YOU get out of this. You can’t feel ANYTHING, when I’m sucking on that pink plastic."

        scene LiR1_NS1_p6

        Yazmin "There’s more to sex, than the physical pleasure. Simply watching you, suck on this strap-on, is intensely erotic."
        Liza2 "Alright - let’s get this over with."
        Yazmin "Can you - at least - pretend to enjoy it?"

        scene LiR1_NS1_p7

        MC "(Huh, it looks like [Liza2_name] is a complete lesbian. Yazmin, on the other hand, seems to be much more open to both men AND women.)"
        Liza2 "*Suck Suck*"
        Yazmin "Mmm... that’s more like it."

        scene LiR1_NS1_p8

        Yazmin "I’ve seen you suck it before - I know you can take it deeper than that."
        Liza2 "*Shluuurrrp*"
        MC "(Wow! This is so fucking hot!)"

        scene LiR1_NS1_p9

        Yazmin "Make sure you take it - nice and deep. Get it all - soaking wet - with your saliva."
        Liza2 "*Shlllurrrrrp*"
        Yazmin "Do you know what I’m gonna do next? I’m gonna lie you back on the bed and - screw you silly."

        scene LiR1_NS1_p10

        Liza2 "I don’t know if I’m wet enough yet... It’s just - I don’t get as horny, around cocks."
        Yazmin "Yeah, I know. That’s what the saliva is for! Now c’mere, and let me kiss you."

        scene LiR1_NS1_p11

        Yazmin "I love you, Honey. You know that?"
        Liza2 "Yeah, I know."
        Yazmin "Thanks for putting up with my - silly little fantasies. It’s the perfect ending to a day, for me."

        scene LiR1_NS1_p12

        Liza2 "I’m glad I can make you - happy like that."
        Liza2 "Sorry I’m not - super excited - about this kinda stuff..."
        Yazmin "Shush... It’s okay. You don’t need to apologise. Everyone has their own kinks. I know you like your lace tights."

        scene LiR1_NS1_p13

        Liza2 "*Mwah*"
        Yazmin "Mmm..."
        MC "(Damn, I wish I was in Yazmin’s position right now. I would love to explore [Liza2_name]’s mouth with my tongue.)"

        scene LiR1_NS1_p14

        Liza2 "Mmm!"
        Liza2 "(I’m beginning to get wet, now that she’s actually started making out with me!)"
        Yazmin "(Okay, this has gone on long enough... Let’s get the show started!)"

        scene LiR1_NS1_p15

        Liza2 "Whoa!"
        MC "(Haha! Yazmin just pushed her - back onto the bed!)"
        Yazmin "Sorry. Was I too rough?"

        scene LiR1_NS1_p16

        Liza2 "I- I’m fine."
        Yazmin "You’re still nervous about being fucked by this strap-on, aren’t you?"
        Liza2 "Yeah, a bit."

        scene LiR1_NS1_p17

        Yazmin "You use dildos and vibrators all the time, by yourself. How is this any different?"
        Liza2 "It’s... how it looks, I guess. The fact that it’s on you, and kinda looks like a cock..."
        Yazmin "Well, just lie back and try to think of it - as me fucking you with a dildo. Okay?"

        scene LiR1_NS1_p18

        Liza2 "O-Okay... It’s just a dildo..."
        Yazmin "(I’d love to be able to introduce a guy into our house, for a threesome, but Liza is one of the most frigid lesbians I’ve ever met! She freezes up, when she has to eat a banana!)"
        Yazmin "I’m gonna put it in now. Are you ready?"

        scene LiR1_NS1_p19

        Liza2 "Oooh..."
        Yazmin "How does that feel?"
        Liza2 "Mmm... That’s good... You’re brushing against my clitoris there. That feels amazing..."

        scene LiR1_NS1_p20

        Yazmin "Okay, I’m going to start pushing it in now."
        Liza2 "Ahh... Ah...."
        MC "(It sounds like [Liza2_name] is finally beginning to relax - and enjoy the sex!)"

        scene LiR1_NS1_p21

        Yazmin "Fuck... That’s it... "
        scene LiR1_NS1_p21anim with dissolve
        Yazmin "(I love seeing it, bury, deep into my wife’s pussy. The sight of her squirming and creaming herself, over my fake cock, is just so hot.)"
        Liza2 "Mmmmm! Uhhh! Ahhh!"

        scene LiR1_NS1_p22

        Liza2 "Ah! Ah! Ahhh!"
        scene LiR1_NS1_p22anim with dissolve
        MC "(She’s getting louder. It sounds like she might be about to cum soon!)"
        Yazmin "That’s it... Take my cock... Take it all, in your slutty pussy..."

        scene LiR1_NS1_p23

        Yazmin "You like it when I fuck you like this, don’t you?"
        Liza2 "Ah! Ohhh!"
        Yazmin "You love being pounded hard - over and over!"
        Liza2 "Ohhh! AHHHH! I’m gonna cuuummm!"

        scene LiR1_NS1_p24

        Yazmin "Cum for me! Cum on my fat cock!"
        Liza2 "AHHHHHH!!! YEEEEEESSSSSS!!!"

        MC "(Oh my God! [Liza2_name]’s whole body is shaking uncontrollably! I don’t think I’ve ever seen a woman cum - so hard - in my life!)"

        scene LiR1_NS1_p25

        Liza2 "AHH! AHHH!!!! HNNNNGGGGG!!!!"
        Liza2 "Ughhh! Ahhh! Ohhh...."
        Yazmin "Wow! That was a BIG one! Good girl!"
        Liza2 "*Pant Pant*"

        scene LiR1_NS1_p26

        Yazmin "Mmm..."
        Yazmin "(She says she hates cocks, but she always - cums the hardest - when she gets fucked by a strap-on. There’s no way I could ever make her do that, with my fingers.)"
        Liza2 "Mmm!"
        MC "(Okay, it looks like they’re finishing, for the night. I should probably slip away now, in case [Liza2_name] opens her eyes and spots me leering at them!"

        $ LiR1_NS1 = False
        $ can_LiR1_NS = False
        $ LiR1_NS2_can1 = True
        $ LiR1_MAS5_can1 = True

        $ LiR1_climbing = False

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump map_label
    else:

        scene LiR1_NS1_sleeping with dissolve
        $ can_LiR1_NS = False
        MC "Hmm... They're sleeping."
        jump a_home_outside_M1
