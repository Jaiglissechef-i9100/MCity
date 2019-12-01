label MLR3_AS3_rep:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    scene black
    $ renpy.pause(2,hard= True)

    scene MLR3_AS3_p1 with dissolve

    MC "(Huh? What’s [Mom_name] doing in my room? She almost never comes in here when I’m not around.)"
    MC "(She must have something really important bothering her. Come to think of it, she’s looking a little anxious there.)"
    MC "(Shit! I wonder if I’ve done something wrong in the past few days, to upset her?)"

    scene MLR3_AS3_p2

    Mom "Hi, [player_name]. We need to talk."
    MC "(Fuck… This could be worse than I expected. I wonder what the hell is going on?)"
    MC "Y-Yeah, no problem, [Mom_name]."

    scene MLR3_AS3_p3

    Mom "Sit down beside me."
    MC "Are you alright, [Mom_name]?"
    Mom "I think so… maybe. Sorry, that’s why I had to do this in your room. I needed to guarantee that we had some privacy."

    scene MLR3_AS3_p4

    Mom "Listen, [player_name]… You know that I really care about you. Don’t you?"
    MC "Yeah, of course I know that, [Mom_name]."
    if persistent.incest_patch == True:
        Mom "I know we’ve done a lot of stuff together. Especially late at night, when your father is asleep."
    else:
        Mom "I know we’ve done a lot of stuff together. Especially late at night, when Bob is asleep."

    scene MLR3_AS3_p5

    Mom "I just wanted to say… sorry."
    MC "Sorry? What for, [Mom_name]? You’ve done nothing wrong."
    Mom "You probably feel like I’m just using you for sex."
    if persistent.incest_patch == True:
        Mom "We don’t get to go on dates that often, and the only time we get to spend together is wasted on quickies, with the threat of your father walking in on us."
    else:
        Mom "We don’t get to go on dates that often, and the only time we get to spend together is wasted on quickies, with the threat of Bob walking in on us."

    scene MLR3_AS3_p6

    Mom "I get so turned on when I’m around you. I just want to screw you silly, each time I get close to you…"
    Mom "...but we never get to go on romantic dates or anything, because of the nature of our relationship."
    MC "[Mom_name]! We went to that restaurant together, remember?"

    scene MLR3_AS3_p7

    Mom "Yeah, and where else?"
    MC "Umm… The beach house?"
    Mom "Two dates, [player_name]. I’ve made you cum, more times than we’ve gone out somewhere together - romantically."
    Mom "I’ve come to the realisation, that I’m using you like a sex toy."

    scene MLR3_AS3_p8

    MC "What?! No, you’re not, [Mom_name]!"
    Mom "I am. I need to start treating you like an actual other half in a relationship. That means giving you time, that isn’t just about us having sex."
    Mom "I don’t want to leave you feeling like I’m using you… because, if you feel that way, I know you’ll end up leaving me."

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    scene MLR3_AS3_p9

    MC "[Mom_name]! I don’t feel that way and I’d NEVER do that! I love you more than you know."
    Mom "Really?"
    MC "I swear on Sara’s life! I don’t feel like you’re using me. Sure, I’d love to spend more quality time together, but I know that’s difficult right now, with [Dad_name] in the background."

    scene MLR3_AS3_p10

    Mom "Thank you, Sweetie. I appreciate you understanding."
    Mom "I promise you, someday I’m gonna make this right. I’m gonna find a way to spend more time together."
    MC "Don’t put pressure on yourself, [Mom_name]. We’ll work through this. All you need to know, right now, is that I don’t feel used."

    scene MLR3_AS3_p11

    Mom "You’re so understanding and mature. I’m lucky that I snapped you up before you started dating someone."
    Mom "You’re a real catch, you know that?"
    MC "Aww, thanks, [Mom_name]."

    scene MLR3_AS3_p12

    Mom "Anyway, now that I’m no longer worried about you leaving me, let’s move on to something else."
    Mom "How’s school going? I don’t feel like I’ve asked you that in quite a while."
    MC "Eh, not too bad. You can take a look at my current projects, over on my desk."

    scene MLR3_AS3_p13

    Mom "Over here?"
    MC "Yeah, you see those two red folders to the right? That’s what I’m working on right now."

    scene MLR3_AS3_p14
    Mom "Yuck… this takes me back to my days in school."
    Mom "I used to hate revising. During the exam period my mom would ALWAYS yap at me: “Why aren’t you studying?! Why can’t you be more like Liza?!”"
    Mom "Liza worked her ass off, locked herself away in her bedroom, and did nothing but work."
    Mom "Meanwhile, I procrastinated and delayed…"

    scene MLR3_AS3_p15

    Mom "At the end of the day, Liza got the better grades - but I got the better job. Grades aren’t everything, [player_name]."
    MC "Really?"
    Mom "Sure, they’re important, but there are lots of other things that can affect your chances of success in life."

    scene MLR3_AS3_p16

    Mom "Confidence, maturity, emotional intelligence, and empathy - to name a few."
    Mom "And you’ve got an abundance of all of those. You’ll do just fine."
    Mom "How are your grades, by the way?"

    scene MLR3_AS3_p17

    MC "Not too bad. I’m slightly above average."
    Mom "That’s fine by me."
    MC "(Hmm… Let’s see if I can spice things up here. Should I grab her ass or her breasts?)"

    menu:
        "Grab [Mom_name]’s ass.":
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
            scene MLR3_AS3_p18a

            MC "(Hehe, I bet she never saw this one coming!)"
            Mom "Oh my!"
            MC "Sorry, [Mom_name], I couldn’t resist!"

            scene MLR3_AS3_p18b

            Mom "You couldn’t resist grabbing my ass? Well, at least you understand how I feel about you, now. I can’t resist toying with you, every time we meet."
            Mom "You’ve got a good firm grip there… Now you’ve gone and turned me on again!"
            jump MLR3_AS3_con2_rep
        "Grab [Mom_name]’s breasts.":
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
            scene MLR3_AS3_p19a

            MC "([Mom_name]’s breasts are amazing! There’s nothing better than groping a huge pair of tits like this!)"
            Mom "Ohh!"

            scene MLR3_AS3_p19b

            Mom "My my… someone is horny!"
            MC "Sorry, [Mom_name]. I couldn’t hold myself back. Your tits are awesome!"
            jump MLR3_AS3_con2_rep

label MLR3_AS3_con2_rep:
    scene MLR3_AS3_p20
    if persistent.incest_patch == True:
        Mom "Well, if you’re horny, that’s a problem - and Mommy is going to have to do something about that!"
    else:
        Mom "Well, if you’re horny, that’s a problem - I have to do something about that!"
    MC "Mmm… what are you suggesting?"
    Mom "I’m thinking that you deserve a good sloppy blowjob."

    scene MLR3_AS3_p21

    MC "Mmm, I like the sound of that!"
    if persistent.incest_patch == True:
        Mom "I think your father is out right now, so we have a little bit of privacy."
    else:
        Mom "I think Bob is out right now, so we have a little bit of privacy."
    MC "That’s a relief."
    if persistent.incest_patch == True:
        Mom "Go ahead and pull your pants down. Just lie back and relax. Let Mommy take care of all the work."
    else:
        Mom "Go ahead and pull your pants down. Just lie back and relax. Let me take care of all the work."

    scene MLR3_AS3_p22

    MC "Mmm…"
    Mom "I shouldn’t be surprised that you’re already hard. You’ve got such a nice cock, you know that?"
    Mom "It’s so long and thick."

    scene MLR3_AS3_p22

    Mom "*Suck Suck*"
    Mom "(God, I miss the feeling of this, plunging into my pussy.)"
    MC "Ohh… Fuck…"

    scene MLR3_AS3_p24

    Mom "*Shlurp*"
    scene MLR3_AS3_p24anim
    MC "Ugh… fuck, this is good."
    Mom "*SUCK SUCK*"

    scene MLR3_AS3_p27 with dissolve

    MC "(I love it when she uses her hand and mouth at the same time.)"
    MC "Ah… Yes, just like that, [Mom_name]. Don’t stop!"
    MC "Ugh! Ohh…"

    scene MLR3_AS3_p28

    Mom "*Shluuuurrrrrp*"
    scene MLR3_AS3_p28anim with dissolve
    MC " Mmm!"
    MC "(She’s rolling her tongue around the tip. Fuck… this is indescribable.)"

    scene MLR3_AS3_p29

    Mom "Do you want me to try deepthroating you?"
    MC "Oh yeah, that sounds great!"
    Mom "Okay, here we go. I might gag a bit, but don’t worry about that - just relax and enjoy this."

    scene MLR3_AS3_p30

    MC "Okay, [Mom_name]."
    MC "(Damn, I wish she would just pull her pants off right now and ride me.)"

    scene MLR3_AS3_p31

    Mom "*Suck Suck*"
    MC "Ah… Oh…"
    MC "(Fuck me, this is heavenly.)"

    scene MLR3_AS3_p32

    Mom "*SHLURRRP*"
    Mom "*GAG* *COUGH*"
    MC "Hnnng! Ugh! Oh yes! Ahh…"

    scene MLR3_AS3_p33

    Mom "*Suck Suck*"
    MC "Ah… Yes, [Mom_name]! Just like that!"
    MC "I want you to go deeper! Mmm!"

    scene MLR3_AS3_p34

    MC "Ah… Yes… just like that."
    scene MLR3_AS3_p34anim with dissolve
    Mom "*SUCK SUCK*"
    MC "Mmm! Yes! Yes, [Mom_name]!"

    scene MLR3_AS3_p35

    Mom "*GAG!* *SPLUTTER*"
    scene MLR3_AS3_p35anim with dissolve
    MC "Hnnng! Ohhh!"
    MC "(I can feel my dick, slipping down her tight throat! This is fucking incredible!)"

    scene MLR3_AS3_p36

    MC "Fuck… Mmm…"
    MC "(This is so hot - I just wish [Mom_name] wasn’t wearing so many clothes.)"
    MC "(I wonder if she’d mind me stripping some off her? Probably not!)"

    scene MLR3_AS3_p37

    MC "(Let’s go for her trousers - it’ll be easier to take those off without interrupting her blowjob.)"
    MC "(If I go for her shirt, then she’s gonna have stop while I pull it over her head.)"
    Mom "*Suck Suck*"

    scene MLR3_AS3_p38

    MC "(Goddamn, she’s good with her lips.)"
    Mom "*Shluuurrrp*"
    MC "Ohh… fuck…"

    scene MLR3_AS3_p39

    Mom "*Suck Suck* Hmm?"
    Mom "(Looks like he wants to play with my ass, while I suck him off! Nothing wrong with that!)"
    MC "Mmm, you’re not wearing any panites, [Mom_name]!"

    scene MLR3_AS3_p40

    MC "Fuck, your ass is great."
    Mom "*SUCK SUCK*"
    MC "Ahh… Ugh…"

    scene MLR3_AS3_p41

    MC "I’d love to plunge my cock deep into you right now. Just throw you down on the bed, or up against the wall, and take you from behind."
    MC "Ah… Fuck…"
    Mom "(You have NO IDEA how much I want that too!)"

    scene MLR3_AS3_p42

    Mom "*Gasp*"
    Mom "Are you close to cumming?"
    MC "Yeah, not far off it."
    Mom "Okay, I want you to cum in my mouth. I want to taste your, hot virile cum, on my tongue."

    scene MLR3_AS3_p43

    Mom "*Suck Suck Suck*"
    MC "Mmm! Ahh…"
    MC "(She’s sped up now! I’m not gonna last long, if she keeps up this pace!)"

    scene MLR3_AS3_p44

    Mom "*GAG* *SHLUUURRRRP*"
    MC "OHHH! FUCK! Yessss!"
    MC "I’m cumming, [Mom_name]! I’m cumming!"

    scene MLR3_AS3_p45

    MC "Hnnnnggg! Ugh! Ahh…"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene MLR3_AS3_p45 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene MLR3_AS3_p45 with dissolve
    MC "(Fuck, it feels so good, blowing my load in her mouth. It reminds me of how amazing it felt, to cum in her tight pussy!)"
    Mom "Mmm! (It tastes so good…)"
    Mom "*Gulp*"

    scene MLR3_AS3_p46

    Mom "Ahh…"
    MC "Fuck...That was amazing. Thanks, [Mom_name]."
    Mom "*Gulp*"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Scheming Weasel faster.mp3', channel="music1", loop=True, fadein = 2)

    scene MLR3_AS3_p47

    "*Creeeaak*"
    MC "Footsteps?!"
    if persistent.incest_patch == True:
        Mom "Shit! Your dad isn’t supposed to be home yet - pull your pants up!"
    else:
        Mom "Shit! Bob isn’t supposed to be home yet - pull your pants up!"
    scene MLR3_AS3_p48

    MC "(Fuck fuck fuck!)"
    Mom "(Shit! Fucking shit!)"
    "*Creak*"

    scene MLR3_AS3_p49

    Caroline "Hey, [player_name]! I’ve run out of white paper. Can I steal some of yours?"
    MC "Y-Yeah, s-sure!"
    Caroline "Is everything okay? You seem nervous."

    scene MLR3_AS3_p50

    MC "Uh… Y-Yeah, the paper is over there, on my desk."
    Caroline "No problem. Hi, [Mom_name]!"
    Mom "Mmm hmm!"

    scene MLR3_AS3_p51

    Mom "(Shit, I’ve still got some of [player_name]’s cum in my mouth!)"
    Mom "(Please, please, please, don’t notice…)"
    Caroline "Anyway, sorry for interrupting you two. I won’t be a minute!"

    scene MLR3_AS3_p52

    Caroline "Do you mind if I steal a pen as well? I think mine’s about to run dry on me."
    MC "Yeah, go ahead."
    MC "(Thank God we both got our pants back on in time. We came THIS CLOSE, to blowing the gig!)"

    scene MLR3_AS3_p53

    Mom "I’m gonna go and prepare dinner. I’ll see you both later on."
    Caroline "Bye, [Mom_name]!"
    MC "S-See ya, later!"
    MC "(Phew… That was FAR too close!)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
