image LiR1_MAS6_p1 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/1.jpg"
image LiR1_MAS6_p2 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/2.jpg"
image LiR1_MAS6_p3 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/3.jpg"
image LiR1_MAS6_p4 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/4.jpg"
image LiR1_MAS6_p5 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/5.jpg"
image LiR1_MAS6_p6 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/6.jpg"
image LiR1_MAS6_p7 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/7.jpg"
image LiR1_MAS6_p8 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/8.jpg"
image LiR1_MAS6_p9 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/9.jpg"
image LiR1_MAS6_p10 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/10.jpg"
image LiR1_MAS6_p11 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/11.jpg"
image LiR1_MAS6_p12 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/12.jpg"
image LiR1_MAS6_p13 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/13.jpg"
image LiR1_MAS6_p14 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/14.jpg"
image LiR1_MAS6_p15 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/15.jpg"
image LiR1_MAS6_p16 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/16.jpg"
image LiR1_MAS6_p17 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/17.jpg"
image LiR1_MAS6_p18 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/18.jpg"
image LiR1_MAS6_p19 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/19.jpg"
image LiR1_MAS6_p20 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/20.jpg"
image LiR1_MAS6_p21 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/21.jpg"
image LiR1_MAS6_p22 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/22.jpg"
image LiR1_MAS6_p23 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/23.jpg"
image LiR1_MAS6_p24 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/24.jpg"
image LiR1_MAS6_p25 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/25.jpg"
image LiR1_MAS6_p26 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/26.jpg"
image LiR1_MAS6_p27 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/27.jpg"
image LiR1_MAS6_p28 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/28.jpg"
image LiR1_MAS6_p29 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/29.jpg"
image LiR1_MAS6_p30 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/30.jpg"
image LiR1_MAS6_p31 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/31.jpg"
image LiR1_MAS6_p32 = "/images/a_home/Outside/Pool/M/scenes/LiR1_MAS6/32.jpg"

label LiR1_MAS6_label:
    if persistent.incest_patch == True:
        $ Liza2_name = __("Auntie")
    else:
        $ Liza2_name = "Liza"

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene LiR1_MAS6_p1 with dissolve

    MC "(Cool! Looks like [Liza2_name] is - finally - getting some use out of the swimming pool, now that I’ve finished cleaning it up for her.)"
    MC "(She looks - incredible - in that bikini. I should go over and say hello.)"

    scene LiR1_MAS6_p2
    if persistent.incest_patch == True:
        MC "Hey, Aunt Liza! How are you?"
    else:
        MC "Hey, Liza! How are you?"
    Liza2 "Oh! Hi, [player_name]. I decided to take - a quick dip - in the pool, today. It’s so nice, just being able to use it any time you want, without having to worry about - if it needs cleaned."
    Liza2 "Thanks so much, for your hard work!"
    MC "It was nothing! I’m just glad that you’re enjoying it!"

    scene LiR1_MAS6_p3

    Liza2 "What brings you over today, then?"
    MC "I was just passing through the neighbourhood, and thought I’d drop by to say hello."
    Liza2 "Aww, that’s nice. I’m afraid that Yazmin isn’t around at the minute. Can I get you something to drink? A cola perhaps?"

    scene LiR1_MAS6_p4

    MC "I’m good, [Liza2_name]. Thanks for offering, though. Is that you done, in the pool, for today?"
    Liza2 "No, I’m just going to take a short break, then I’ll be back in."
    MC "I have to say - you’re looking very well toned there!"

    scene LiR1_MAS6_p5

    Liza2 "Yeah - I’ve been practicing diving, and doing laps. I used to be a competitive swimmer, in college."
    MC "Really?!"
    Liza2 "Oh yeah! Almost qualified for the national championships!"
    MC "Wow! What happened? Why didn’t you qualify?"
    Liza2 "(I can’t tell him the real reason...)"
    Liza2 "(I missed the tryouts, because Yazmin had me tied up in the gym showers - eating my pussy out - for several hours straight.)"
    Liza2 "(The only reason I forgave her was because, she’s so damn good with that tongue!)"
    Liza2 "I... uh... came fourth in the qualifiers. Only the top three got through."
    MC "Aww... Sorry to hear that."

    scene LiR1_MAS6_p6

    Liza2 " Say - why don’t you join me for a few laps?"
    MC "Sure! Why not? Umm... I don’t have any swimming trunks though."
    Liza2 "Don’t worry about it - just take your pants off. It’ll be fine."
    MC "Okay, [Liza2_name]!"

    scene LiR1_MAS6_p7

    MC "(Wow! She’s good!)"
    MC "(It’s a shame that she didn’t qualify. She’s clearly a natural at this kinda thing!)"

    scene LiR1_MAS6_p8

    MC "(And just look at how - perfect - her ass is! It’s the epitome of a bubble butt!)"
    MC "(I could squeeze that thing - for hours - and never get bored! Yazmin really is a lucky woman, to get to sleep with her, every single night.)"

    scene LiR1_MAS6_p9

    Liza2 "Well? Are you coming in or not?"
    MC "Hang on! I’m coming now!"

    scene LiR1_MAS6_p10

    MC "(Hopefully, I won’t get a boner, when I’m in the water with her...)"
    MC "(I’ll be swimming and moving around a lot. The chances of me getting hard, are VERY slim! It’ll be fine!)"
    MC "(I just need to calm down and relax. That’s all!)"

    scene LiR1_MAS6_p11

    MC "Geronimo!"
    Liza2 "Haha!"
    "*SPLASH*"

    scene LiR1_MAS6_p12

    MC "(Oh cool! I’ve got a great view of - her bikini bottoms - down here!)"
    MC "(I don’t think she’ll be suspicious, if I spend another few seconds - lingering down here - after my dive.)"

    scene LiR1_MAS6_p13

    MC "(That bra is so tight, that I can almost see the outline of [Liza2_name]’s nipples!)"
    MC "(God, her tits are just incredible! I could stare at them for hours!)"
    MC "(I better get back up, before she starts wondering what’s taking me so long!)"

    scene LiR1_MAS6_p14

    Liza2 "It’s a scorcher of a day - you must be enjoying the cool water."
    MC "Yeah, it’s great! Thanks for letting me use your pool, [Liza2_name]."
    Liza2 "Don’t think anything of it! You’re the one who helps keep it clean, after all! You might as well enjoy - the fruits of your labour."
    Liza2 "C’mon! Let’s go for a swim! I’m aiming to burn another two hundred calories today!"
    MC "You don’t need to be burning calories - you’re looking great as you are."

    scene LiR1_MAS6_p15

    Liza2 "You’re very kind, but I’ve got to keep in shape. Let’s get started!"
    MC "Sure! I’m right behind you."

    scene LiR1_MAS6_p16

    MC "(I was hoping to catch up to her, and get a better view of that ass.)"
    MC "(She’s WAY too fast though - I never imagined she’d be THIS quick in the water.)"
    MC "(Then again, she DID use to be a near-professional swimmer - so I guess it makes sense.)"

    scene LiR1_MAS6_p17

    MC "(Dammit - I’m gonna have to swim EXTREMELY hard if I’m gonna catch her.)"
    MC "(Alright, let’s take a deep breath - and push myself to my limit.)"
    MC "(I’m a man - and I’m much younger than she is - I might be able to gain on her!)"

    scene LiR1_MAS6_p18

    MC "(Yes! Almost made it!)"
    MC "(Damn, just look at how that - tight thong - rides up between her thighs. I’d love to pull those panties aside, and bury my cock, deep in her lesbian pussy.)"

    scene LiR1_MAS6_p19

    MC "(I can almost see the outline of her - tight little asshole - too.)"
    MC "(It would feel amazing - wrapped all snugly - around my cock. I’d give anything to fuck her, doggystyle.)"
    MC "(Uh oh! I think I’ve gotten a bit too close.)"

    scene LiR1_MAS6_p20

    "*Bump*"
    Liza2 "Huh?!"
    MC "Oof!"

    scene LiR1_MAS6_p21

    MC "(Dammit! She slowed down, and I face planted myself, right between her buttcheeks!)"
    MC "(Fuck! She’s gonna think I did this on purpose!)"
    Liza2 "Whoops!"

    scene LiR1_MAS6_p22

    Liza2 "Sorry about that! I slowed down too fast, there. Did you hurt yourself?"
    MC "(Huh? She thinks it was her fault, that I bumped into her.)"
    MC "Uh... Y-Yeah, I’m fine. I didn’t hit anywhere, hard."
    Liza2 "It isn’t sore, is it?"
    MC "N-No - just a little bit. I’m good - really."

    scene LiR1_MAS6_p23
    if persistent.incest_patch == True:
        Liza2 "Oh! Good to hear - My sister would kill me, if I hurt her son!"
    else:
        Liza2 "Oh! Good to hear - Linda would kill me, if I hurt her [player_name]!"
    Liza2 "C’mere! Let me give you a hug and make it all better."
    MC "(Uh oh... There’s no way I’m gonna be able to hug her, without getting a huge boner!)"

    scene LiR1_MAS6_p24

    MC "It’s- ah- I’m okay! Really! Don’t worry about me!"
    if persistent.incest_patch == True:
        Liza2 "Aww c’mon... you’re never too old to get a cuddle from your auntie. Don’t be embarrassed - it’s not like any of your friends are around to see you."
    else:
        Liza2 "Aww c’mon... you’re never too old to get a cuddle from me. Don’t be embarrassed - it’s not like any of your friends are around to see you."

    MC "I... uh..."
    MC "(Oh shit... I can feel it getting hard!)"

    scene LiR1_MAS6_p25

    Liza2 "See? There we go. It’s not so bad, after all, is it?"
    MC "*Gulp*"
    MC "Y-Yeah, all... g-good."
    Liza2 "You seem a little anxious. Is everything okay?"

    scene LiR1_MAS6_p26

    MC "(Dammit! I’m completely hard, right now! Hopefully she’s won’t feel it...)"
    MC "Y-Yeah... I’m just... maybe a little warm... It’s a really hot day."
    MC "In fact - I’m gonna leave now and get myself a drink..."

    scene LiR1_MAS6_p27

    Liza2 "Hey! Don’t you go yet - something’s up!"
    MC "*Gulp*"
    MC "(She’s right, there! Something is - definitely - up...)"

    scene LiR1_MAS6_p28

    Liza2 "Are you hiding something from me?"
    MC "Ye-No! No, I’m not!"
    Liza2 "What have you got there?"

    scene LiR1_MAS6_p29

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music2", loop=True, fadein = 2)
    MC "No! Wait!"
    Liza2 "Oh, my God!"
    MC "(Fuck...)"

    scene LiR1_MAS6_p30

    Liza2 "(He’s... erect! Oh, my God...)"
    MC "(I should have worn proper swimming trunks into the pool. My boxer shorts are too loose! They’ve just slipped down!)"
    MC "(Now she’s seen that I’ve got a boner, from her hugging me. Fucking fantastic..!)"

    scene LiR1_MAS6_p31

    MC "[Liza2_name]! I’m so, so sorry!"
    MC "When you hugged me, and your... chest was pressed up against me, I just..."
    MC "I’m sorry, it’s just a reaction I have to every woman."
    Liza2 "..."

    scene LiR1_MAS6_p32

    Liza2 "I guess - you are - a young man..."
    Liza2 "Sorry for prying - I shouldn’t have pushed it, once you tried to hide it. That was my fault."
    Liza2 "Can we just agree to NEVER talk about this again?"
    MC "Y-Yeah, I think that’s a good idea."

    $ LiR1_MAS6_can1 = False
    $ LiR1_MAS4can3 = True
    $ LiR1_MAS6= False
    $ LiR1_MAS2= True
    $ LiR1_MAS3= True

    $ LiR1_MAS7_can1 = True
    $ day_time += 1

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump a_pool_M1
