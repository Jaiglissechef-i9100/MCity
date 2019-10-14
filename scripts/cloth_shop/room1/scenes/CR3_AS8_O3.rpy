image CR3_AS8_O3_p1 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/1.jpg"
image CR3_AS8_O3_p2 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/2.jpg"
image CR3_AS8_O3_p3 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/3.jpg"
image CR3_AS8_O3_p5 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/5.jpg"
image CR3_AS8_O3_p6 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/6.jpg"
image CR3_AS8_O3_p7 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/7.jpg"
image CR3_AS8_O3_p7a = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/7a.jpg"
image CR3_AS8_O3_p8 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/8.jpg"
image CR3_AS8_O3_p9 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/9.jpg"
image CR3_AS8_O3_p10 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/10.jpg"
image CR3_AS8_O3_p11 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/11.jpg"
image CR3_AS8_O3_p12 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/12.jpg"
image CR3_AS8_O3_p13 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/13.jpg"
image CR3_AS8_O3_p14 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/14.jpg"
image CR3_AS8_O3_p15 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/15.jpg"
image CR3_AS8_O3_p16 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/16.jpg"
image CR3_AS8_O3_p17 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/17.jpg"
image CR3_AS8_O3_p18 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/18.jpg"
image CR3_AS8_O3_p19 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/19.jpg"
image CR3_AS8_O3_p20anim = Movie(play="videos/04 Caroline-AS8-1.webm", loop = True )
image CR3_AS8_O3_p21 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/21.jpg"
image CR3_AS8_O3_p22 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/22.jpg"
image CR3_AS8_O3_p23 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/23.jpg"
image CR3_AS8_O3_p24 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/24.jpg"
image CR3_AS8_O3_p25 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/25.jpg"
image CR3_AS8_O3_p26 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/26.jpg"
image CR3_AS8_O3_p27 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/27.jpg"
image CR3_AS8_O3_p28anim = Movie(play="videos/04 Caroline-AS8-2.webm", loop = True )
image CR3_AS8_O3_p29 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/29.jpg"
image CR3_AS8_O3_p30anim = Movie(play="videos/04 Caroline-AS8-3.webm", loop = True )
image CR3_AS8_O3_p31 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/31.jpg"
image CR3_AS8_O3_p31anim = Movie(play="videos/04 Caroline-AS8-4.webm", loop = True )
image CR3_AS8_O3_p32 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/32.jpg"
image CR3_AS8_O3_p33 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/33.jpg"
image CR3_AS8_O3_p34 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/34.jpg"
image CR3_AS8_O3_p35anim = Movie(play="videos/04 Caroline-AS8-5.webm", loop = True )
image CR3_AS8_O3_p36 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/36.jpg"
image CR3_AS8_O3_p37 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/37.jpg"
image CR3_AS8_O3_p38 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/38.jpg"
image CR3_AS8_O3_p39anim = Movie(play="videos/04 Caroline-AS8-7.webm", loop = True )
image CR3_AS8_O3_p40 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/40.jpg"
image CR3_AS8_O3_p41 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/41.jpg"
image CR3_AS8_O3_p42 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/42.jpg"
image CR3_AS8_O3_p42anim = Movie(play="videos/04 Caroline-AS8-6.webm", loop = True )
image CR3_AS8_O3_p42a = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/42a.jpg"
image CR3_AS8_O3_p43 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/43.jpg"
image CR3_AS8_O3_p44 = "images/cloth_shop/room1/day/scenes/CR3_AS8_O3/44.jpg"

label CR3_AS8_O3:

    $ outfit_start = 3
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2,hard=True)
    $ can_hide_windows = True
    if C_R3_outfit3.t_played == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)

        scene CR3_AS8_O3_p1 with dissolve

        MC "(What the fuck is this outfit, even supposed to be?)"
        MC "(I mean, the gloves are the only part of the costume, that’s ALMOST normal.)"
        MC "(I swear to God, these cosplay fanatics get weirder every year!)"

        scene CR3_AS8_O3_p2

        MC "Caroline!"
        Caroline "Yes?"
        MC "What did you say this outfit was supposed to be again?"
        Caroline "It’s a superhero costume!"

        scene CR3_AS8_O3_p3

        Violet "What kind of superhero has horns, and - absolutely no chest armour?"
        Caroline "It’s Dragon Man! Do neither of you watch anime?"
        MC "Nope."
        Violet "Not really."

        scene CR3_AS8_O3_p5

        Caroline "Fine. I guess it’s up to me, to explain the scenario for this one, then."
        Caroline "Dragon Man got bitten by a radioactive dragon, so he’s now half dragon."
        MC "I guess that’s... kinda cool?"
        Caroline "I’ll be playing, his long-term love interest, Princess White Lady."

        scene CR3_AS8_O3_p6

        Violet "Princess... White Lady?"
        Caroline "The translations to English suck. Don’t blame me!"
        Caroline "Anyway, Princess White Lady and Dragon Man were on a quest - Princess White Lady got captured, and Dragon Man heroically rescued her."

        scene CR3_AS8_O3_p7

        Caroline "Is that enough background, for you two to work on?"
        Violet "Sort of... I guess?"
        MC "Yeah, I think so..."

        scene CR3_AS8_O3_p7a

        Caroline "Good. I could explain more, but it would take me HOURS! The lore for Dragon Man, is surprisingly deep."
        Violet "...…no kidding. This wikipedia article scrolls forever!"
        MC "Alright - let’s get started. What are we gonna do?"
        Caroline "You’ve just rescued me - so I’m still on my knees, looking up to you, as my hero. I want you to reach out, as if you’re going to put your thumb in my mouth - but just hold before it goes in."

        scene CR3_AS8_O3_p8

        MC "It’s a rather... unusual pose."
        Caroline "We’re re-enacting the art of the second season’s promo trailer."

        scene CR3_AS8_O3_p9

        MC "That explains a lot."
        MC "(Damn, I just noticed the pink high heel shoes, she’s wearing. They look so sexy on her!)"
        Caroline "This isn’t the most comfortable position to be sitting in. Can we get things rolling?"

        scene CR3_AS8_O3_p10

        Violet "Okay, are you two finally ready?"
        MC "Yup! Let’s get this show on the road!"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump outfit_R3_start
    else:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/MenuMusic.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump outfit_R3_start

label CR3_AS8_O3_con2:
    scene black
    $ renpy.pause(2,hard=True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

    scene CR3_AS8_O3_p11

    MC "Well? Are you happy with the pictures?"
    Caroline "I think I will be! I’m hoping to break into the Japanese market, overseas. It won’t be an easy ride - but if we keep up this targeted advertising, then I stand a solid chance."
    MC "Good to hear!"

    scene CR3_AS8_O3_p12

    Violet "Hey guys, I gotta head on, here. My mom needs me to pick up some groceries, on the way home."
    MC "No problem. Catch you later, Violet."
    Caroline "Thanks for your help today! See you later!"

    scene CR3_AS8_O3_p13

    MC "Well, it’s just you and me now."
    Caroline "Do you have any plans for the evening?"
    MC "No, I’m free to spend some time here, if you want to relax together."

    scene CR3_AS8_O3_p14

    Caroline "Yeah, I’d like that. Now that we’ve got some privacy - perhaps we could fool around?"
    MC "Mmm... that sounds good!"
    Caroline "Go ahead. You can do whatever you want."

    scene CR3_AS8_O3_p15

    MC "Is this okay?"
    Caroline "You don’t need to worry about seeking my permission, for every action. The deal’s back on - and I know I’m safe with you."
    MC "(God, her tits are fucking amazing!)"

    scene CR3_AS8_O3_p16

    Caroline "You really like my breasts, don’t you?"
    MC "They stand out, so well in this outfit!"
    Caroline "How about you strip out of that silly costume, and I’ll show you a good time."
    MC "Great - could I request that you keep YOUR outfit on, though? It’s kinda sexy."

    scene CR3_AS8_O3_p17

    Caroline "Hehe. Of course I’ll keep mine on for you."
    Caroline "(Fuck, his cock looks so hot. I can’t wait to play with it!)"
    Caroline "Remember - no putting your dick in any of my holes. Aside from that, I’m open to almost anything."

    scene CR3_AS8_O3_p18

    MC "No problem, Caroline. That sounds fair enough."
    Caroline "Close your eyes, for me. I want to show you something."
    MC "Okay, what-"

    scene CR3_AS8_O3_p19

    MC "Mmm!"
    Caroline "Mmm..."
    MC "(Oh wow! She’s an incredible kisser!)"

    scene CR3_AS8_O3_p20anim

    Caroline "Mmm... "
    Caroline "(He tastes so good... I could make out with him forever.)"

    scene CR3_AS8_O3_p21

    Caroline "Well? Enjoy that?"
    MC "Oh yeah... That was something else!"
    Caroline "I think you’re going to enjoy - what comes next - even more."

    scene CR3_AS8_O3_p22

    MC "(Is she going to take her panties off?! I wonder if she’ll let me fuck her today!)"
    Caroline "I hope you’re enjoying the view there. I want you - extra hard - by the time I turn around."
    MC "I’ve been rock-hard, since I saw you in that white costume!"

    scene CR3_AS8_O3_p23

    Caroline "What do you think?"
    MC "Wow... "
    Caroline "There’s not a lot of guys, get to see those parts. You better - damn well - appreciate the view!"

    scene CR3_AS8_O3_p24

    Caroline "Now, onto the main show..."
    MC "Careful - are you not worried about it slipping inside you?"
    Caroline "Relax, I’ve got your little guy - gripped firmly - between my thighs. He’s not going anywhere."

    scene CR3_AS8_O3_p25

    Caroline "Well... maybe ‘little’ wasn’t the right adjective to use."
    MC "Mmm... That feels good."

    scene CR3_AS8_O3_p26

    Caroline "I’m gonna start grinding my hips, up and down. Will you let me know if it feels good?"
    MC "Yeah, I will. What about you though? You deserve to get some pleasure too."
    Caroline "Don’t you worry - I can feel your shaft, against my pussy. I’ll be enjoying this, as much as you."

    scene CR3_AS8_O3_p27

    MC "Ah..."
    Caroline "My thighs aren’t too tight around your cock, are they?"
    MC "Ah... n-no... that’s perfect."
    Caroline "Good! I want you to enjoy this."

    scene CR3_AS8_O3_p28anim

    MC "Mmm... That’s so fucking good, Caroline."
    MC "Where did you learn to use your thighs like that?"
    Caroline "There were more than a few nights when my ex claimed he forgot his condom - or outright refused to wear it.."

    scene CR3_AS8_O3_p29

    Caroline "I had to improvise ways to get him off without letting him into my pussy."
    MC "Huh? That’s pretty clever. Ah..."
    Caroline "Yeah, it worked, most of the time."
    MC "Why only most of the time?"

    scene CR3_AS8_O3_p30anim

    Caroline "This position has your cock, rub up against my clitoris. There were a few times when it REALLY turned me on, and I just couldn’t hold myself back any longer."
    Caroline "Ah... Oh..."
    Caroline "I ended up screwing him bareback a couple of times. We just had to be super careful that he pulled out in time."
    Caroline "But, let's not talk about him anymore. I want to forget about that time."

    scene CR3_AS8_O3_p31

    Caroline "Violet takes birth control, for the exact same reason. Once a guy turns her on, she just needs to fuck him. She’s insatiable like that."
    MC "Ah... Mmm!"
    scene CR3_AS8_O3_p31anim
    MC "(I wonder if I could turn on Caroline, that way.)"

    scene CR3_AS8_O3_p32

    Caroline "H-Hey! Wh-What are you doing?!"
    MC "It’s not fair that you’re doing all the work! Let me help, by moving my hips a bit!"
    Caroline "W-Wait!"

    scene CR3_AS8_O3_p33

    Caroline "Ah! Ah!"
    MC "(I can feel my shaft digging into her pussy now. I can definitely stimulate her better, from this angle!)"
    MC "(Plus, I can go much faster than she could, when she was on top of me!)"

    scene CR3_AS8_O3_p34

    Caroline "Ah! Oh, my God! Mmm! Oh!"
    Caroline "[player_name]! Y-You have to - ahhh - s-slow down!"
    MC "Mmm! Ah! Ugh!"

    scene CR3_AS8_O3_p35anim

    Caroline "OOOHHHHHHH!!!"
    Caroline "(He’s got the perfect angle on my pussy! It feels so fucking good!)"
    Caroline "(I can’t let him get the better of me like this!)"

    scene CR3_AS8_O3_p36

    Caroline "Ah! AHHH! AHHH!"
    MC "Hnnnng..."
    MC "(Damn, she is REALLY wet right now!)"

    scene CR3_AS8_O3_p37

    MC "(Let’s change the angle a bit, so my cock is ALMOST poking at her pussy.)"
    Caroline "Oh... Oh... Ohh... Wow..."
    Caroline "(The feeling of his cock, against my pussy, is making me melt. This is FAR too risky! Why did I ever think, doing this without panties, would be a good idea?!)"

    scene CR3_AS8_O3_p38

    MC "(Okay, I’ve got the angle! Now I can press against her pussy, as if I’m about to go inside.)"
    MC "(I’ll slip past, at the very last second - and tease her. Haha!)"
    Caroline "Ah! Ah! W-Wait! Don’t go inside!"

    scene CR3_AS8_O3_p39anim

    Caroline "Ohhhhhh!!!"
    Caroline "(He is sliding the whole length of his cock against my clitoris! It feels soooo good!)"
    MC "(Heh, I’m REALLY making her moan here!)"

    scene CR3_AS8_O3_p40

    Caroline "Ohhh... Mmm... God..."
    MC "(She’s absolutely loving this! My cock is completely SOAKED with her juices now.)"
    Caroline "Yeeessss..! Mmmm!"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    scene CR3_AS8_O3_p41

    MC "(Fuck! I’m about to cum!)"
    MC "AH! Ahhh! Ugh!"
    Caroline "Oh! Oh! AHH!"

    scene CR3_AS8_O3_p42

    MC "Yes! HNNNGGGG! Arrghhhh!"
    scene CR3_AS8_O3_p42anim
    Caroline "AHHHHH!!!!!!"

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR3_AS8_O3_p42 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR3_AS8_O3_p42a with dissolve

    MC "*Pant Pant* Wow..."
    MC "Fuck... That was amazing, Caroline..."
    Caroline "(Huh?! He stopped?! I was SOOO close to cumming! Dammit! I want him inside me...)"

    scene CR3_AS8_O3_p43

    Caroline "(Fuck - this has gone too far again. I need to get home and relieve myself, before I find myself doing something I’ll regret.)"
    Caroline "(This ALWAYS happens when I get too horny.)"
    MC "Caroline? Where are you going?"

    scene CR3_AS8_O3_p44

    Caroline "I... er... I have to go and do... something urgent. I completely forgot about it!"
    Caroline "Feel free to clean yourself up and head back home!"
    MC "Um, okay? I’ll see you later."
    Caroline "BYE! (Fuck! I was SOOO close to letting him pound my pussy there. I need to get a grip of myself!)"

    $ day_time = 3

    $ CR3_NS3 = True
    $ C_NS_locked = True
    $ CR3_MS3 = True
    $ CR3_outfit4_can = False

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump map_label
