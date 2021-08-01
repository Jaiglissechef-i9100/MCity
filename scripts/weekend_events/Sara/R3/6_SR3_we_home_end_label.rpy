image SR3_we_home_end_p1 = "images/v71/2_WE/6_Home_End/1.jpg"
image SR3_we_home_end_p2 = "images/v71/2_WE/6_Home_End/2.jpg"
image SR3_we_home_end_p3 = "images/v71/2_WE/6_Home_End/3.jpg"
image SR3_we_home_end_p4 = "images/v71/2_WE/6_Home_End/4.jpg"
image SR3_we_home_end_p5 = "images/v71/2_WE/6_Home_End/5.jpg"
image SR3_we_home_end_p6 = "images/v71/2_WE/6_Home_End/6.jpg"
image SR3_we_home_end_p7 = "images/v71/2_WE/6_Home_End/7.jpg"
image SR3_we_home_end_p8 = "images/v71/2_WE/6_Home_End/8.jpg"
image SR3_we_home_end_p9 = "images/v71/2_WE/6_Home_End/9.jpg"
image SR3_we_home_end_p10 = "images/v71/2_WE/6_Home_End/10.jpg"
image SR3_we_home_end_p11 = "images/v71/2_WE/6_Home_End/11.jpg"
image SR3_we_home_end_p12 = "images/v71/2_WE/6_Home_End/12.jpg"
image SR3_we_home_end_p13 = "images/v71/2_WE/6_Home_End/13.jpg"
image SR3_we_home_end_p14 = "images/v71/2_WE/6_Home_End/14.jpg"
image SR3_we_home_end_p15 = "images/v71/2_WE/6_Home_End/15.jpg"
image SR3_we_home_end_p16 = "images/v71/2_WE/6_Home_End/16.jpg"
image SR3_we_home_end_p17 = "images/v71/2_WE/6_Home_End/17.jpg"

label SR3_we_home_end_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if SR3_romantic_route == True:
        scene SR3_we_home_end_p1
        Sara "She ruined everything…"
        MC "Sara, c’mon, we had a lovely day up until she arrived. Just try and put Lily out of your mind."
        Sara "I can’t! She’s just so… so… so brazen!"
        scene SR3_we_home_end_p3
        MC "Everything is going to be fine, I promise. Look on the bright side. You got your mint ice cream, and we got to see the grand opening of the mall!"
        MC "That was a pretty damn-good date, even if Lily made the end a bit awkward."

        scene SR3_we_home_end_p4
        MC "Plus, I got to enjoy seeing you in your brand new dress. You really were a sight to behold."

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

        MC "Like, seriously, you were the hottest girl in the whole mall."
        scene SR3_we_home_end_p5
        Sara "Hotter than Lily?"
        MC "Haha, much hotter."
        Sara "You’re just saying that to make me feel better. Lily has bigger breasts, she dresses sexier, and knows how to wear makeup better."
        scene SR3_we_home_end_p6
        MC "I’m serious, Sara. You’re so much cuter than she is. I love your breasts the way they are, I love your freckles, I loved your dress today."
        MC "If I didn’t like you I wouldn’t have said yes to making today a formal date, would I?"
        Sara "I… guess not."
        scene SR3_we_home_end_p7
        MC "See? This never had anything to do with Lily. All she did was show up and make a fool of herself."
        Sara "Yeah… I guess you’re right."
        scene SR3_we_home_end_p8
        Sara "You don’t like her though, do you?"
        MC "No, I don’t have any feelings for Lily. I promise you that."
        Sara "Okay… I feel better hearing you say that."
        scene SR3_we_home_end_p9
        MC "I promise you, Sara, it’s only you and me. Okay? Just you and me until the end."
        Sara "I’m sorry, [player_name], I keep overreacting when she’s around…"
        scene SR3_we_home_end_p10
        MC "It’s alright, Sara."
        MC "The day isn’t over yet, by the way. We can still give our first date a happy ending."
        scene SR3_we_home_end_p11
        Sara "What do you mean?"
        MC "How about we do it for the first time, together?"
        scene SR3_we_home_end_p12
        Sara "Y-You mean have sex?"
        MC "Yeah, not anal this time. I’m talking real sex. We went out in public as a couple. Everyone who saw us should know you’re mine by now."
        scene SR3_we_home_end_p13
        Sara "*Gulp* I’m a little nervous."
        Sara "Is it going to hurt as much as anal did?"
        MC "Absolutely not. Your pussy is going to produce a natural lube, like what we used the second time we tried anal."
        scene SR3_we_home_end_p14
        MC "You might feel a slight pang of pain for a second or two when my cock first goes in. That’s just what happens when your hymen tears."
        MC "There also might be a little bit of blood, but don’t worry about that. It’s perfectly normal."
        Sara "And then it will feel good?"
        MC "It will feel good after that."
        scene SR3_we_home_end_p15
        MC "What do you say, Sara?"
        Sara "I… I… yeah… Let’s do it."
        MC "Are you absolutely sure you want to? I’m happy to wait a bit longer if you need some time."
        scene SR3_we_home_end_p17
        Sara "N-No… I’m ready, [player_name]. I’m ready to have my first time with my boyfriend."
        MC "I’m happy to hear that. Let’s make this a perfect end to our first date together."
        Sara "Thank you, [player_name]. I love you."
        MC "I love you too, Sara. You’re amazing."
    else:
        scene SR3_we_home_end_p1
        Sara "She ruined everything…"
        MC "Sara, c’mon, we had a lovely day up until she arrived. Just try and put Lily out of your mind."
        Sara "I can’t! She’s just so… so… so brazen!"
        scene SR3_we_home_end_p3
        MC "Everything is going to be fine, I promise. Look on the bright side. You got your mint ice cream, and we got to see the grand opening of the mall!"
        MC "We had a really fun time going out together, even if Lily made the end a bit awkward."
        scene SR3_we_home_end_p4
        MC "Plus, I got to enjoy seeing you in your brand new dress. You really were a sight to behold."

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

        MC "Like, seriously, you were the hottest girl in the whole mall."
        scene SR3_we_home_end_p5
        Sara "Hotter than Lily?"
        MC "Haha, much hotter."
        Sara "You’re just saying that to make me feel better. You didn’t even want us to be a public couple though."
        Sara "There’s other girls out there that you have your eyes on. Lily has bigger breasts, she dresses sexier, and knows how to wear makeup better."
        scene SR3_we_home_end_p6
        MC "I’m serious, Sara. You’re so much cuter than she is. I love your breasts the way they are, I love your freckles, I loved your dress today."
        Sara "Then why do we have to pretend we aren’t a couple? I hate that..."
        if persistent.incest_patch == True:
            MC "Sara… It’s complicated. A lot of people wouldn’t approve of a brother and sister dating. For your safety and mine, it’s best to keep ourselves out of the spotlight."
        else:
            MC "Sara… It’s complicated. A lot of people wouldn’t approve of our dating. For your safety and mine, it’s best to keep ourselves out of the spotlight."
        scene SR3_we_home_end_p7
        Sara "(I need to make myself MORE appealing to [player_name] than Lily is. That slut would do anything to get her claws into him.)"
        MC "All Lily did was show up and make a fool of herself."
        Sara "Uh huh..."
        scene SR3_we_home_end_p8
        Sara "Do you find Lily attractive?"
        MC "Of course, I mean, she’s an attractive girl. I like you more though."
        Sara "(It hurts to hear him say that… but at least I know where I stand. I’m in competition with that bitch.)"
        scene SR3_we_home_end_p9
        Sara "What if… What if I could do… more for you?"
        MC "What do you mean, Sara?"
        scene SR3_we_home_end_p10
        Sara "I’ve already let you take my anal virginity. I know you really want to fuck my other place too."
        MC "Are you suggesting what I think you are suggesting?"
        Sara "(I’ve got no choice. If I want to keep [player_name] in my life I’m going to have to up my game. Blowjobs and anal aren’t enough. I need to give him my virginity.)"
        scene SR3_we_home_end_p11
        Sara "Y-Yeah, let’s do it. Tonight. Actual sex - not anal, not a blowjob. Full… sex. I want to go all the way with you."
        MC "Are you sure?"
        Sara "Absolutely. We’ll do it now. It’ll mark the end of our first date."
        scene SR3_we_home_end_p12
        MC "Mmm, that sounds like a wonderful end to the day."
        Sara "If we do this, do you think you’d want to make me your girlfriend in public?"
        MC "Sara… I’ll think about it. Like I said, it’s complicated and very risky."
        scene SR3_we_home_end_p13
        Sara "*Sigh* Okay… Can I be honest with you, [player_name]? I’m a little nervous."
        Sara "Is it going to hurt as much as anal did?"
        MC "Absolutely not. Your pussy is going to produce a natural lube, like what we used the second time we tried anal."
        scene SR3_we_home_end_p14
        MC "You might feel a slight pang of pain for a second or two when my cock first goes in. That’s just what happens when your hymen tears."
        MC "There also might be a little bit of blood, but don’t worry about that. It’s perfectly normal."
        Sara "And then it will feel good?"
        MC "It will feel good after that."
        scene SR3_we_home_end_p15
        MC "What do you say, Sara?"
        Sara "I… I… yeah… Let’s do it."
        MC "Are you absolutely sure you want to? I’m happy to wait a bit longer if you need some time."
        scene SR3_we_home_end_p17
        Sara "N-No… I’m ready, [player_name]. I’m ready to have my first time with my boyfriend."
        Sara "(This is how I’m going to keep you away from that harpy, Lily.)"
        MC "I’m happy to hear that. Let’s make this a perfect end to our first date together."
        Sara "I love you, [player_name]. You know that? I love you more than any other girl ever will."
    Sara "Well, how should we warm up?"
    MC "I could play with your tits to get you nice and wet."
    Sara "Or I could go down and suck your cock to get you hard. You pick."
    $ SR3_home_end_both = True
    $ SR3_home_end_bed = True
    $ SR3_home_end_couch = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump sister_nerdy_evening1

