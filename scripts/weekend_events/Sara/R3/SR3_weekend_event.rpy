image SR3_WE_p1 = "images/v71/2_WE/1.jpg"
image SR3_WE_p2 = "images/v71/2_WE/2.jpg"
image SR3_WE_p3 = "images/v71/2_WE/3.jpg"
image SR3_WE_p4 = "images/v71/2_WE/4.jpg"
image SR3_WE_p5 = "images/v71/2_WE/5.jpg"
image SR3_WE_p6 = "images/v71/2_WE/6.jpg"
image SR3_WE_p7 = "images/v71/2_WE/7.jpg"
image SR3_WE_p8 = "images/v71/2_WE/8.jpg"
image SR3_WE_p9 = "images/v71/2_WE/9.jpg"
image SR3_WE_p10 = "images/v71/2_WE/10.jpg"
image SR3_WE_p11 = "images/v71/2_WE/11.jpg"
image SR3_WE_p12 = "images/v71/2_WE/12.jpg"
image SR3_WE_p13 = "images/v71/2_WE/13.jpg"
image SR3_WE_p14 = "images/v71/2_WE/14.jpg"
image SR3_WE_p15 = "images/v71/2_WE/15.jpg"
image SR3_WE_p16 = "images/v71/2_WE/16.jpg"
image SR3_WE_p17 = "images/v71/2_WE/17.jpg"
image SR3_WE_p18 = "images/v71/2_WE/18.jpg"
image SR3_WE_p19 = "images/v71/2_WE/19.jpg"
image SR3_WE_p20 = "images/v71/2_WE/20.jpg"
image SR3_WE_p21 = "images/v71/2_WE/21.jpg"
image SR3_WE_p22 = "images/v71/2_WE/22.jpg"
image SR3_WE_p23 = "images/v71/2_WE/23.jpg"
image SR3_WE_p24 = "images/v71/2_WE/24.jpg"
image SR3_WE_p25 = "images/v71/2_WE/25.jpg"
image SR3_WE_p25anim1 = Movie(play="/videos/v71/1.webm", loop = True )
image SR3_WE_p25anim2 = Movie(play="/videos/v71/1a.webm", loop = True )
image SR3_WE_p25anim3 = Movie(play="/videos/v71/2.webm", loop = True )
image SR3_WE_p26 = "images/v71/2_WE/26.jpg"
image SR3_WE_p27 = "images/v71/2_WE/27.jpg"
image SR3_WE_p28 = "images/v71/2_WE/28.jpg"
image SR3_WE_p29 = "images/v71/2_WE/29.jpg"
image SR3_WE_p30 = "images/v71/2_WE/30.jpg"
image SR3_WE_p31 = "images/v71/2_WE/31.jpg"
image SR3_WE_p32 = "images/v71/2_WE/32.jpg"
image SR3_WE_p32anim1 = Movie(play="/videos/v71/3.webm", loop = True )
image SR3_WE_p33 = "images/v71/2_WE/33.jpg"
image SR3_WE_p33anim1 = Movie(play="/videos/v71/4.webm", loop = True )
image SR3_WE_p34 = "images/v71/2_WE/34.jpg"
image SR3_WE_p35 = "images/v71/2_WE/35.jpg"
image SR3_WE_p35anim1 = Movie(play="/videos/v71/9.webm", loop = True )
image SR3_WE_p36 = "images/v71/2_WE/36.jpg"
image SR3_WE_p37 = "images/v71/2_WE/37.jpg"
image SR3_WE_p38 = "images/v71/2_WE/38.jpg"
image SR3_WE_p39 = "images/v71/2_WE/39.jpg"
image SR3_WE_p39anim1 = Movie(play="/videos/v71/5.webm", loop = True )
image SR3_WE_p39anim2 = Movie(play="/videos/v71/5a.webm", loop = True )
image SR3_WE_p40 = "images/v71/2_WE/40.jpg"
image SR3_WE_p41 = "images/v71/2_WE/41.jpg"
image SR3_WE_p41anim1 = Movie(play="/videos/v71/8.webm", loop = True )
image SR3_WE_p42 = "images/v71/2_WE/42.jpg"
image SR3_WE_p42anim1 = Movie(play="/videos/v71/6.webm", loop = True )
image SR3_WE_p43 = "images/v71/2_WE/43.jpg"
image SR3_WE_p44 = "images/v71/2_WE/44.jpg"
image SR3_WE_p45 = "images/v71/2_WE/45.jpg"
image SR3_WE_p46 = "images/v71/2_WE/46.jpg"
image SR3_WE_p46anim1 = Movie(play="/videos/v71/7.webm", loop = True )
image SR3_WE_p46anim2 = Movie(play="/videos/v71/7a.webm", loop = True )
image SR3_WE_p47 = "images/v71/2_WE/47.jpg"
image SR3_WE_p48 = "images/v71/2_WE/48.jpg"
image SR3_WE_p49 = "images/v71/2_WE/49.jpg"
image SR3_WE_p50 = "images/v71/2_WE/50.jpg"
image SR3_WE_p51 = "images/v71/2_WE/51.jpg"
image SR3_WE_p52 = "images/v71/2_WE/52.jpg"


label SR3_we_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ renpy.pause(3, hard= True)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)
    $ week_day = 6
    $ day_time = 1
    if SR3_romantic_route == True:
        scene black
        Sara "Wakey wakey, [player_name]! Rise and shine!"
        MC "*Yawn*"
        scene SR3_WE_p1
        Sara "Boop! Hehe!"
        MC "Ugh… Stop poking my nose!"
        scene SR3_WE_p2
        Sara "Time to get up, sleepy head! It’s our big day."
        MC "Our big… day?"
        Sara "It’s the grand opening of the mall! It’s OUR date! C’mon! Hurry up and get ready, we’re gonna be late!"
        scene SR3_WE_p3
        MC "*Yawn*"
        MC "Yea, I’m coming… just give me a couple more minutes…"
        Sara "You’re just gonna go straight back to sleep, and then I’m gonna have to wake you up all over again! I know you too well, [player_name]."
        scene SR3_WE_p4
        MC "Yeah, you’re right. Fine, I’m getting up."
        Sara "C’mon, get your ass in the shower and let’s hit the road."
        scene SR3_WE_p5
        MC "Heh, what time have you been awake from?"
        Sara "I BARELY slept. I’m so EXCITED! It’s gonna be amazing!"
        MC "I can’t believe you’re this excited about the mall."
        scene SR3_WE_p2
        Sara "It’s not the mall I’m excited about, silly! "
        scene SR3_WE_p1
        Sara "It’s getting to spend the day with you!"
        MC "Aww, in that case I’ll get ready as quickly as I can."
        scene SR3_WE_p7
        Sara "That’s the spirit, [player_name]!"
        MC "Just give me five minutes to have a quick bath and I’ll be done."
        jump SR3_we_end1
    else:

        scene SR3_WE_p2
        Sara "Hey [player_name], are you awake?"
        MC "Zzz… Hmm?"
        Sara "Morning…"
        scene SR3_WE_p5
        MC "Oh, morning Sara, what’s up?"
        Sara "I… uh… It’s the grand opening of the mall today."
        scene SR3_WE_p6
        Sara "You know the way you sorta agreed to go on a date with me."
        MC "Yeah, a date, but we keep it on the down low. Don’t make it too obvious?"
        Sara "*Sigh* Yeah… "
        Sara "Well, the mall is opening today. Do you still want to go with me?"
        scene SR3_WE_p5
        MC "Yeah, of course, Sara. I’ll just hit the bathroom and we’ll be ready to go."
        scene SR3_WE_p7
        Sara "I’d been thinking… Do we really need to keep this date a secret?"
        MC "Sorry, Sara. It’s too risky otherwise. We talked about this - just imagine what would happen if someone from our school saw us."
        Sara "*Sigh*"
        scene SR3_WE_p8
        Sara "([player_name] didn’t worry about this kind of stuff when he asked our Ms. Celia in school.)"
        Sara "(I mean, sure, he embarrassed himself, but if he could pick up the courage to ask a teacher out in public, why can’t he do the same for me?)"
        Sara "(Do I honestly mean less to him than Ms. Celia?)"
        Sara "(Maybe I am just his sidepiece to be fucked and used until someone better comes along…)"
        scene SR3_WE_p9
        Sara "(I need to prove to [player_name] that I’m worthy of being his girlfriend. Then he’ll love me and actually want to be a proper couple in public!)"
        Sara "(I’ll begin right now by marching into the bathroom and showing him EXACTLY what he will get with me as his official girlfriend!)"
        jump SR3_we_end1

label SR3_we_end1:
    scene black
    $ can_hide_windows = True
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR3_we_bath = True
    jump mc_room_morning2


label SR3_bath_time:
    hide screen displayTextScreen
    hide screen map_button
    show screen mc_room_morning
    $ clickable = False
    MC "Not now, it's time for a bath."
    hide screen mc_room_morning
    $ clickable = True
    jump mc_room_morning2

label SR3_bath_time_corr:
    hide screen displayTextScreen
    hide screen map_button
    show screen corridor_morning
    $ clickable = False
    MC "Not now, it's time for a bath."
    hide screen corridor_morning
    $ clickable = True
    jump corridor_morning2

label SR3_bath_time_living:
    hide screen displayTextScreen
    hide screen map_button
    show screen salon_morning
    $ clickable = False
    MC "Not now, it's time for a bath."
    hide screen salon_morning
    $ clickable = True
    jump salon_morning2
label SR3_bath_time_kitchen:
    hide screen displayTextScreen
    hide screen map_button
    show screen kitchen_morning
    $ clickable = False
    MC "Not now, it's time for a bath."
    hide screen kitchen_morning
    $ clickable = True
    jump kitchen_morning2

label SR3_we_bath:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(3, hard= True)
    if SR3_romantic_route == True:
        scene SR3_WE_p10
        MC "(The mall’s grand opening is going to attract a big crowd. There’s definitely going to be a few people from our school there.)"
        MC "(I wonder how they’ll react to seeing Sara and me on a date?)"
        scene SR3_WE_p11
        MC "(At the end of the day, the thing that matters the most is that she is happy.)"
        MC "(God, she was so nervous when she was trying to ask me out. I’ll do my best to make today as special as I can for her.)"
        MC "(Okay, time to run myself a bath and get washed.)"
        scene SR3_WE_p12
        MC "Ahh…"
        MC "(There’s no better way to wake up on the weekend, than a relaxing hot bath.)"
        scene SR3_WE_p13
        Sara "(Oh wow! I’ve been grounded for so long, I forgot how hot [player_name] looks when he’s naked.)"
        Sara "(When was the last time I saw him like this? It must have been when we were both up on the roof trying anal.)"
        scene SR3_WE_p14
        Sara "(God… His cock is massive.)"
        Sara "(I still can’t believe he agreed to go on a date with me. I really want to do something for him, to show how grateful I am.)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)
        Sara "Hey [player_name], mind if I join you?"
        MC "Oh, hey Sara. Sure, c’mon in!"
        scene SR3_WE_p15
        MC "Just be careful. [Mom_name] or [Dad_name] didn’t see you come in here, did they?"
        Sara "Relax, [Mom_name] just went out to the shops, and [Dad_name] probably went to the office for overtime."
        MC "*Phew* That’s a relief. I’m a little too old now to plausibly be sharing a bath with you."
        scene SR3_WE_p16
        Sara "Hehe! Stop worrying, we’ll be fine. The only other person in the home is Caroline, and I think she’s just moping around in her room right now."
        MC "Okay, that’s good."
        MC "(Sara looks so fucking sexy, wearing nothing but those tight little denim shorts.)"
        scene SR3_WE_p17
        MC "Y’know, if you’re planning on joining me in here, you’re gonna have to lose those shorts."
        Sara "Oh, you mean these?"
        scene SR3_WE_p18
        Sara "Enjoying the view, [player_name]?"
        MC "*Whistle*"
        MC "(Damn, her teenage ass is stunning!)"
        scene SR3_WE_p19
        Sara "I’ll join you in a second, [player_name]. I just have to grab my shampoo and a spare towel."
        MC "Uh huh…"
        scene SR3_WE_p20
        MC "(I can’t just wait in the bath! That ass is just begging to be pounded right now!)"
        MC "(God, I’d love to just bend her over the sink, bury my shaft in her pussy and fuck her until her tight little hole cums around my cock.)"
        Sara "Did you see where I left my-"
        scene SR3_WE_p21
        Sara "Mmpff!"
        MC "Mmm…"
        scene SR3_WE_p22
        Sara "W-What happened to us bathing together? Hehe."
        MC "You were tempting me. I couldn’t resist."
        Sara "So you thought you’d just surprise me with a passionate kiss?"
        MC "Did it work?"
        scene SR3_WE_p23
        Sara "Yeah… I liked it."
        MC "I missed you when you were grounded, you know that, Sara?"
        Sara "I missed seeing you too, [player_name]."
        scene SR3_WE_p24
        Sara "Oh wow, I can feel your big guy between my thighs. You REALLY did miss me, huh?"
        MC "Hmm? Oh, he isn’t even that big yet. Give him a moment."
        scene SR3_WE_p25
        Sara "Oh!"
        MC "Haha! See what I mean?"
        Sara "Y-Yeah!"
        MC "Do you fancy doing something naughty together before our date?"
        scene SR3_WE_p25anim2
        MC "How does it feel when I slide my dick back and forth across your pussy like that?"
        Sara "Ah… It’s… It’s really nice…"
        MC "I could just slip it inside right now. How about even just the tip?"
        scene SR3_WE_p25anim1
        Sara "*Gulp*"
        MC "C’mon, you know you want it."
        Sara "I do… but..."
        Sara "(I can feel his cock brushing up against my vulva… If he really wanted to, he could plunge it into my pussy and pop my cherry right now.)"
        Sara "(I’m not ready for that yet. I don’t want my first time to be a quickie in a bathroom.)"
        scene SR3_WE_p25anim3
        Sara "W-Wait, I’m not ready for sex. I don’t want my first time to be in the bathroom."
        MC "Heh, I understand that."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)

        MC "How about you get down on your knees and suck my cock instead?"
        scene SR3_WE_p26
        Sara "Yeah! I can do that."
        Sara "(That’s a relief. I was worried he was going to want sex really badly right now.)"
        MC "You look so sexy, Sara. God, your freckles are just adorable."
        Sara "Hehe, thanks [player_name]."
        scene SR3_WE_p27
        Sara "*Gulp*"
        MC "You okay there, Sara?"
        Sara "I… uh… kinda forgot how big your guy was up close."
        MC "Haha, don’t worry. We can do this another time if you want."
        scene SR3_WE_p28
        Sara "No way! Do you not think I’m up to the challenge, [player_name]?"
        MC "Mmm... "
        MC "(Her palm feels so warm wrapped around my shaft.)"
        MC "Go ahead, but don’t push yourself if you don’t want to."
        scene SR3_WE_p29
        Sara "I’ve been practicing [player_name], you know?"
        MC "Practicing giving head?"
        Sara "I’d been asking [Mom_name] for cucumbers and bananas to eat while I studied. Remember when I first started giving you blowjobs I could barely fit an inch in my mouth?"
        scene SR3_WE_p30
        MC "Yeah, I remember. It was adorable though."
        Sara "Well, I can do SOOO much more now. At least, on a banana. Hehe! The best part was, [Mom_name] never suspected a thing."
        MC "Okay then, Sara. Let’s see what you’ve got."
        scene SR3_WE_p31
        Sara "(Okay Sara, deep breaths… You can do this. It’s just like a banana…)"
        Sara "(You’ve practiced for this. You’ve read the articles and watched the guide videos.)"
        MC "Mmm… God that’s good… Keep stroking my cock like that."
        scene SR3_WE_p32
        Sara "Are you enjoying this, [player_name]?"
        scene SR3_WE_p32anim1
        MC "Mmm… Oh yeah, it’s so good."
        Sara "Well, it’s about to get a whole lot better."
        scene SR3_WE_p33
        Sara "You’re so big and hard, [player_name]. I can feel it pulsing against my fingers."
        scene SR3_WE_p33anim1
        MC "That just means I’m super excited."
        scene SR3_WE_p34
        MC "Alright, let’s see what you’ve taught yourself."
        Sara "I’m about to blow your mind, [player_name]. Just close your eyes, relax, and enjoy the sensation of my mouth wrapped around your cock."
        scene SR3_WE_p35
        Sara "*Mwah*"
        scene SR3_WE_p35anim1
        MC "Ohhh… fuck…"
        Sara "(Just think back to how you used to practice, Sara. You can do this!)"
        scene SR3_WE_p36
        Sara "(Remember what you read on Judy’s Blog, the glans is the most sensitive part of the guy’s cock. If I focus my efforts on the tip of his dick, I’ll make him cum so much harder!)"
        Sara "*Suck*"
        MC "Ahh… just like that… Mmm…"
        scene SR3_WE_p37
        Sara "*Suck* *Suck*"
        MC "Mmm! Ugh… I missed your little mouth so fucking much, Sara."
        MC "(Her tongue is so wet and warm against my cock. Sara’s blowjobs are fuckin' incredible.)"
        scene SR3_WE_p38
        Sara "*Mwah* *Lick*"
        MC "Hnnng… Mmm…"
        MC "(She’s so cute, down there on her knees sucking my dick.)"
        scene SR3_WE_p39
        Sara "(What was the next piece of advice that blog gave… Oh yeah! Move your head back and forth, allowing your lips to glide over the head of the penis.)"
        scene SR3_WE_p39anim1
        Sara "*Shlurp* *Suck* *Shluuuurrrp*"
        scene SR3_WE_p39anim2
        MC "Ahhh… You definitely ARE getting better, Sara. Mmm!"
        scene SR3_WE_p40
        MC "(Sara’s breasts were never the biggest; but they look so perky and perfect. Her skin looks phenomenal when the sunlight caresses it like that.)"
        Sara "*Suck*"
        MC "God, you’re fucking amazing, Sara… Don’t stop!"
        scene SR3_WE_p41
        MC "Mmm, please don’t stop!"
        scene SR3_WE_p41anim1
        Sara "*Suck* *Suck*"
        Sara "(His dick is starting to throb in my mouth. He must be REALLY enjoying this!)"
        scene SR3_WE_p42
        MC "This is brilliant, Sara, but do you think you can try going a bit deeper?"
        scene SR3_WE_p42anim1
        Sara "Mmm hmm! *Shlurp*"
        scene SR3_WE_p43
        Sara "*Glompfff*"
        MC "Mmm… That’s right. Just like that, Sara. Ugh! Fuck…"
        Sara "(What did Judy write next? Create a vacuum by sucking your cheeks in? I think that was it.)"
        scene SR3_WE_p44
        Sara "*Suuuuuccck*"
        MC "Oooohhh fuuucck… Oh Sara, that’s so fucking good!"
        MC "(I’m lucky [Mom_name] and [Dad_name] aren’t home. There’s no way I’ll be able to keep my voice down for the whole blowjob!)"
        scene SR3_WE_p45
        Sara "*Suck* *Suck* *Suck*"
        MC "Oh! Oh fuck! Arrrghhh! Ugh! Yes! Yes Sara, don’t stop!"
        Sara "*Shlurp* *Slluurrrp* *SUCK*"
        scene SR3_WE_p46
        MC "I… *Hnnnhhh* I… I’m gonna…"
        scene SR3_WE_p46anim1
        Sara "(What was I supposed to do after sucking my cheeks in? I can’t remember now. I think I’m supposed to start ‘deepthroating’ now, aren’t I?)"
        scene SR3_WE_p46anim2
        Sara "*Suck Suck*"
        scene SR3_WE_p47
        Sara "(Yeah, I’ll try taking his dick deeper into my mouth. I mean, he seems to be enjoying whatever I’m doing right now!)"
        Sara "*Suck Suck*"
        MC "Fuuuck! Hnnnnggg!! Ugghhh! I’m cumming!"
        scene SR3_WE_p48
        Sara "Hmm?!"
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)
        scene SR3_WE_p48 with dissolve
        $ renpy.pause(0.7, hard = True)
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)
        scene SR3_WE_p48 with dissolve
        Sara "Mmpplllfff! *Gulp*"
        MC "Ughhhh! Ohhh God, that’s amazing..."
        Sara "(H-Holy shit! I was NOT expecting him to cum yet! I got WAY too distracted thinking about what to do next!)"
        scene SR3_WE_p49
        Sara "(I think I accidentally swallowed the first big of cum he shot in my mouth, but there’s more and more coming!)"
        Sara "(Oh shit, there’s waaaayyy too much!)"
        MC "Ohh… Fuck… That was amazing, Sara."
        scene SR3_WE_p50
        MC "Jesus, you look so fucking hot right now. Do you think you can do me a favour, Sara? Can you swallow it for me?"
        Sara "Mmm hmm."
        Sara "*Gulp* *Gulp*"
        MC "Open wide, let me see."
        scene SR3_WE_p51
        Sara "Ahh…"
        MC "Fuck, you’re amazing. Thanks for letting me cum inside. It was amazing."
        scene SR3_WE_p30
        Sara "*Cough* N-No problem. Sorry I never got the chance to go deeper. I was about to try taking you down my throat, and then you suddenly came."
        MC "Haha, don’t worry about it. Your mouth felt fucking amazing."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        Sara "Thanks, [player_name]. Now, I seriously need to have a bath too. I’m all sweaty after that!"
        scene SR3_WE_p52
        Sara "I’ll get washed and dressed here. Head on over to the new shopping mall. I’ll meet you there when I’m ready."
        MC "Sounds good to me! Where exactly do you want to meet?"
        Sara "Just in the main foyer will be fine."
        MC "Great. I’ll see you there, Sara. I’m really looking forward to our date."
        Sara "Me too, [player_name]. I’m so excited!!!"
        Sara "Apologies for not going deeper. We will try again in future."
        jump SR3_we_bath_end
    else:
        scene SR3_WE_p10
        MC "(The mall’s grand opening is going to attract a big crowd. There’s definitely going to be a few people from our school there.)"
        MC "(It’s a good thing I told her to keep the date on the down low. It’s not worth risking the attention we could generate as a couple.)"
        scene SR3_WE_p11
        MC "(At the end of the day, the thing that matters the most is that we’re both safe.)"
        MC "(God, she was so nervous when she was trying to ask me out. It might not be a formal date, but I’ll do my best to make today as special as I can for her.)"
        MC "(Okay, time to run myself a bath and get washed.)"
        scene SR3_WE_p12
        MC "Ahh…"
        MC "(There’s no better way to wake up on the weekend, than a relaxing hot bath.)"
        scene SR3_WE_p13
        Sara "(I still can’t believe he didn’t want to be seen dating me in public...)"
        Sara "(Is there someone else he has his eyes on? Or am I just being paranoid? Maybe I’m just not good enough for him?)"
        scene SR3_WE_p14
        Sara "(What do I have to do to make him proud enough for him to call me his girlfriend in front of other people?)"
        Sara "(Maybe I should be more sexual? I’ve given him a couple of blowjobs and some anal - but maybe it isn’t enough for a horny guy like him.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)

        Sara "Hey [player_name], mind if I join you?"
        MC "Oh, hey Sara. Sure, c’mon in!"
        scene SR3_WE_p15
        MC "Just be careful. [Mom_name] or [Dad_name] didn’t see you come in here, did they?"
        Sara "Relax, [Mom_name] just went out to the shops, and [Dad_name] probably went to the office for overtime."
        MC "*Phew* That’s a relief. I’m a little too old now to plausibly be sharing a bath with you."
        scene SR3_WE_p16
        Sara "Hehe! Stop worrying, we’ll be fine. The only other person in the home is Caroline; and I think she’s just moping around in her room right now."
        MC "Okay, that’s good."
        MC "(Sara looks so fucking sexy, wearing nothing but those tight little denim shorts.)"
        scene SR3_WE_p17
        MC "Y’know, if you’re planning on joining me in here, you’re gonna have to lose those shorts."
        Sara "Oh, you mean these?"
        scene SR3_WE_p18
        Sara "Enjoying the view, [player_name]?"
        MC "*Whistle*"
        MC "(Damn, her teenage ass is stunning!)"
        scene SR3_WE_p19
        Sara "I’ll join you in a second, [player_name]. I just have to grab my shampoo and a spare towel."
        MC "Uh huh…"
        scene SR3_WE_p20
        MC "(I can’t just wait in the bath! That ass is just begging to be pounded right now!)"
        MC "(God, I’d love to just bend her over the sink, bury my shaft in her pussy and fuck her until her tight little hole cums around my cock.)"
        Sara "Did you see where I left my-"
        scene SR3_WE_p21
        Sara "Mmpff!"
        MC "Mmm…"
        scene SR3_WE_p22
        Sara "W-What happened to us bathing together? Hehe."
        MC "You were tempting me. I couldn’t resist."
        Sara "So you thought you’d just surprise me with a passionate kiss?"
        MC "Did it work?"
        scene SR3_WE_p23
        Sara "Yeah… I liked it."
        MC "I missed you when you were grounded, you know that, Sara?"
        Sara "I missed seeing you too, [player_name]."
        scene SR3_WE_p24
        Sara "Oh wow, I can feel your big guy between my thighs. You REALLY did miss me, huh?"
        MC "Hmm? Oh, he isn’t even that big yet. Give him a moment."
        scene SR3_WE_p25
        Sara "Oh!"
        MC "Haha! See what I mean?"
        Sara "Y-Yeah!"
        MC "Do you fancy doing something naughty together before our date?"
        scene SR3_WE_p25anim2
        MC "How does it feel when I slide my dick back and forth across your pussy like that?"
        Sara "Ah… It’s… It’s really nice…"
        MC "I could just slip it inside right now. How about even just the tip?"
        scene SR3_WE_p25anim1
        Sara "*Gulp*"
        MC "C’mon, you know you want it."
        Sara "I do… but..."
        Sara "(I can feel his cock brushing up against my vulva… If he really wanted to, he could plunge it into my pussy and pop my cherry right now.)"
        Sara "(I’m not ready for that yet. I don’t want my first time to be a quickie in a bathroom.)"
        scene SR3_WE_p25anim3
        Sara "W-Wait, I’m not ready for sex. I don’t want my first time to be in the bathroom."
        MC "Heh, I understand that."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)

        MC "How about you get down on your knees and suck my cock instead?"
        scene SR3_WE_p26
        Sara "Yeah! I can do that."
        Sara "(I think it’s pretty clear he wants to fuck me. Maybe that’s why he’s holding off on making us official? Does he worry that I’m never going to let him do me?)"
        MC "You look so sexy, Sara. God, your freckles are just adorable."
        Sara "Hehe, thanks [player_name]."
        scene SR3_WE_p27
        Sara "*Gulp*"
        MC "You okay there, Sara?"
        Sara "I… uh… kinda forgot how big your guy was up close."
        MC "Haha, don’t worry. We can do this another time if you want."
        scene SR3_WE_p28
        Sara "No way! Do you not think I’m up to the challenge, [player_name]?"
        MC "Mmm... "
        MC "(Her palm feels so warm wrapped around my shaft.)"
        MC "Go ahead, but don’t push yourself if you don’t want to."
        scene SR3_WE_p29
        Sara "I’ve been practicing [player_name], you know?"
        MC "Practicing giving head?"
        Sara "I’d been asking [Mom_name] for cucumbers and bananas to eat while I studied. Remember when I first started giving you blowjobs I could barely fit an inch in my mouth?"
        scene SR3_WE_p30
        MC "Yeah, I remember. It was adorable though."
        Sara "Well, I can do SOOO much more now. At least, on a banana. Hehe! The best part was, [Mom_name] never suspected a thing."
        MC "Okay then, Sara. Let’s see what you’ve got."
        scene SR3_WE_p31
        Sara "(Okay Sara, deep breaths… You can do this. It’s just like a banana…)"
        Sara "(You’ve practiced for this. You’ve read the articles and watched the guide videos.)"
        MC "Mmm… God that’s good… Keep stroking my cock like that."
        scene SR3_WE_p32
        Sara "Are you enjoying this, [player_name]?"
        scene SR3_WE_p32anim1
        MC "Mmm… Oh yeah, it’s so good."
        Sara "Well, it’s about to get a whole lot better."
        scene SR3_WE_p33
        Sara "You’re so big and hard, [player_name]. I can feel it pulsing against my fingers."
        scene SR3_WE_p33anim1
        MC "That just means I’m super excited."
        scene SR3_WE_p34
        MC "Alright, let’s see what you’ve taught yourself."
        Sara "I’m about to blow your mind, [player_name]. Just close your eyes, relax, and enjoy the sensation of my mouth wrapped around your cock."
        scene SR3_WE_p35
        Sara "*Mwah*"
        scene SR3_WE_p35anim1
        MC "Ohhh… fuck…"
        Sara "(Just think back to how you used to practice, Sara. You can do this!)"
        scene SR3_WE_p36
        Sara "(Remember what you read on Judy’s Blog, the glans is the most sensitive part of the guy’s cock. If I focus my efforts on the tip of his dick, I’ll make him cum so much harder!)"
        Sara "*Suck*"
        MC "Ahh… just like that… Mmm…"
        scene SR3_WE_p37
        Sara "*Suck* *Suck*"
        MC "Mmm! Ugh… I missed your little mouth so fucking much, Sara."
        MC "(Her tongue is so wet and warm against my cock. Sara’s blowjobs are fuckin' incredible.)"
        scene SR3_WE_p38
        Sara "*Mwah* *Lick*"
        MC "Hnnng… Mmm…"
        MC "(She’s so cute, down there on her knees sucking my dick.)"
        scene SR3_WE_p39
        Sara "(What was the next piece of advice that blog gave… Oh yeah! Move your head back and forth, allowing your lips to glide over the head of the penis.)"
        scene SR3_WE_p39anim1
        Sara "*Shlurp* *Suck* *Shluuuurrrp*"
        scene SR3_WE_p39anim2
        MC "Ahhh… You definitely ARE getting better, Sara. Mmm!"
        scene SR3_WE_p40
        MC "(Sara’s breasts were never the biggest, but they look so perky and perfect. Her skin looks phenomenal when the sunlight caresses it like that.)"
        Sara "*Suck*"
        MC "God, you’re fucking amazing, Sara… Don’t stop!"
        scene SR3_WE_p41
        MC "Mmm, please don’t stop!"
        scene SR3_WE_p41anim1
        Sara "*Suck* *Suck*"
        Sara "(His dick is starting to throb in my mouth. He must be REALLY enjoying this!)"
        scene SR3_WE_p42
        MC "This is brilliant, Sara, but do you think you can try going a bit deeper?"
        scene SR3_WE_p42anim1
        Sara "Mmm hmm! *Shlurp*"
        scene SR3_WE_p43
        Sara "*Glompfff*"
        MC "Mmm… That’s right. Just like that, Sara. Ugh! Fuck…"
        Sara "(What did Judy write next? Create a vacuum by sucking your cheeks in? I think that was it.)"
        scene SR3_WE_p44
        Sara "*Suuuuuccck*"
        MC "Oooohhh fuuucck… Oh Sara, that’s so fucking good!"
        MC "(I’m lucky [Mom_name] and [Dad_name] aren’t home, there’s no way I’ll be able to keep my voice down for the whole blowjob!)"
        scene SR3_WE_p45
        Sara "*Suck* *Suck* *Suck*"
        MC "Oh! Oh fuck! Arrrghhh! Ugh! Yes! Yes Sara, don’t stop!"
        Sara "*Shlurp* *Slluurrrp* *SUCK*"
        scene SR3_WE_p46
        MC "I… *Hnnnhhh* I… I’m gonna…"
        scene SR3_WE_p46anim1
        Sara "(What was I supposed to do after sucking my cheeks in? I can’t remember now. I think I’m supposed to start ‘deepthroating’ now, aren’t I?)"
        scene SR3_WE_p46anim2
        Sara "*Suck Suck*"
        scene SR3_WE_p47
        Sara "(Yeah, I’ll try taking his dick deeper into my mouth. I mean, he seems to be enjoying whatever I’m doing right now! I’m gonna do it! I’m gonna prove to him I’m the best girl he could possibly have!)"
        Sara "*Suck Suck*"
        MC "Fuuuck! Hnnnnggg!! Ugghhh! I’m cumming!"
        scene SR3_WE_p48
        Sara "Hmm?!"
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)
        scene SR3_WE_p48 with dissolve
        $ renpy.pause(0.7, hard = True)
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)
        scene SR3_WE_p48 with dissolve
        Sara "Mmpplllfff! *Gulp*"
        MC "Ughhhh! Ohhh God, that’s amazing..."
        Sara "(H-Holy shit! I was NOT expecting him to cum yet! I got WAY too distracted thinking about what to do next!)"
        scene SR3_WE_p49
        Sara "(I think I accidentally swallowed the first big of cum he shot in my mouth, but there’s more and more coming!)"
        Sara "(Oh shit, there’s waaaayyy too much!)"
        MC "Ohh… Fuck… That was amazing, Sara."
        scene SR3_WE_p50
        MC "Jesus, you look so fucking hot right now. Do you think you can do me a favour, Sara? Can you swallow it for me?"
        Sara "Mmm hmm."
        Sara "*Gulp* *Gulp*"
        MC "Open wide, let me see."
        scene SR3_WE_p51
        Sara "Ahh…"
        MC "Fuck, you’re amazing. Thanks for letting me cum inside. It was amazing."
        scene SR3_WE_p30
        Sara "*Cough* N-No problem. Sorry I never got the chance to go deeper. I was about to try taking you down my throat, and then you suddenly came."
        MC "Haha, don’t worry about it. Your mouth felt fucking amazing."

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        Sara "Thanks, [player_name]. Now, I seriously need to have a bath too. I’m all sweaty after that!"
        scene SR3_WE_p52
        Sara "I’ll get washed and dressed here. Head on over to the new shopping mall. I’ll meet you there when I’m ready."
        MC "Sounds good to me! Where exactly do you want to meet?"
        Sara "Just in the main foyer will be fine."
        MC "Great. I’ll see you there, Sara. I’m really looking forward to our day out."
        Sara "Me too, [player_name]. I’m so excited!!!"
        if renpy.loadable("patch.rpy"):
            MC "Just remember, don’t run up and kiss me or anything. We don’t want to look too romantic when we go out, okay? We’re supposed to be keeping this on the down low. You don’t want your whole class bullying you for dating your brother, do you?"
        else:
            MC "Just remember, don’t run up and kiss me or anything. We don’t want to look too romantic when we go out, okay? We’re supposed to be keeping this on the down low. You don’t want your whole class bullying you for dating with me, do you?"
        Sara "*Sigh* Okay, [player_name]."
        scene black
        $ renpy.pause(3, hard= True)
        jump SR3_we_bath_end

label SR3_we_bath_end:
    $ day_time = 2
    $ SR3_we_bath = False
    $ SR3_we_SC_wait = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SC_closed = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    call screen SR3_we_map2


screen SR3_we_map2:
    add "images/game_gui/map/Map_Day.jpg"

    imagebutton:
        xpos 945
        ypos 256
        focus_mask True
        idle "images/v71/gui/SC_idle.png"
        hover "images/v71/gui/SC_hover.png"
        if clickable == True:
            action Jump("SC_label")