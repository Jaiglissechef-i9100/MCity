image SR3_ES1_p1 = "images/v71/1_ES1/1.jpg"
image SR3_ES1_p2 = "images/v71/1_ES1/2.jpg"
image SR3_ES1_p3 = "images/v71/1_ES1/3.jpg"
image SR3_ES1_p4 = "images/v71/1_ES1/4.jpg"
image SR3_ES1_p5 = "images/v71/1_ES1/5.jpg"
image SR3_ES1_p6 = "images/v71/1_ES1/6.jpg"
image SR3_ES1_p7 = "images/v71/1_ES1/7.jpg"
image SR3_ES1_p8 = "images/v71/1_ES1/8.jpg"
image SR3_ES1_p9 = "images/v71/1_ES1/9.jpg"
image SR3_ES1_p10 = "images/v71/1_ES1/10.jpg"
image SR3_ES1_p11 = "images/v71/1_ES1/11.jpg"
image SR3_ES1_p12 = "images/v71/1_ES1/12.jpg"
image SR3_ES1_p13 = "images/v71/1_ES1/13.jpg"
image SR3_ES1_p14 = "images/v71/1_ES1/14.jpg"
image SR3_ES1_p15 = "images/v71/1_ES1/15.jpg"
image SR3_ES1_p16 = "images/v71/1_ES1/16.jpg"
image SR3_ES1_p17 = "images/v71/1_ES1/17.jpg"
image SR3_ES1_p18 = "images/v71/1_ES1/18.jpg"
image SR3_ES1_p19 = "images/v71/1_ES1/19.jpg"
image SR3_ES1_p20 = "images/v71/1_ES1/20.jpg"
image SR3_ES1_p21 = "images/v71/1_ES1/21.jpg"
image SR3_ES1_p22 = "images/v71/1_ES1/22.jpg"
image SR3_ES1_p23 = "images/v71/1_ES1/23.jpg"
image SR3_ES1_p24 = "images/v71/1_ES1/24.jpg"
image SR3_ES1_p25a = "images/v71/1_ES1/25a.jpg"
image SR3_ES1_p25aa = "images/v71/1_ES1/25aa.jpg"
image SR3_ES1_p25b = "images/v71/1_ES1/25b.jpg"
image SR3_ES1_p25bb = "images/v71/1_ES1/25bb.jpg"

label SR3_ES1_label:
    if SR3_ES1_talked == True:
        hide screen map_button
        show screen sister_nerdy_evening
        $ clickable = False
        Sara "Not now, [player_name]."
        $ clickable = True
        hide screen sister_nerdy_evening
        jump sister_nerdy_morning1
    else:

        $ can_hide_windows = True
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        scene SR3_ES1_p1
        MC "(Sara said she wasn’t grounded any longer. I’m lucky that she finally got her act together and improved her grades.)"
        MC "(I wonder how she’s been doing locked up in her room. [Mom_name] has been constantly checking to make sure she isn’t slacking off playing video games. I guess all she needed was some tough love.)"
        scene SR3_ES1_p2
        $ renpy.sound.play("sfx/knock_knock.wav")
        "*Knock Knock*"
        $ renpy.music.stop(channel="sound")
        Sara "Who is it?"
        MC "Just me, Sara."
        scene SR3_ES1_p3
        Sara "The door’s unlocked, [player_name]! C’mon in!"
        "*Click*"
        $ renpy.sound.play("sfx/door_open.mp3")
        scene SR3_ES1_p4
        if persistent.incest_patch == True:
            MC "Hey, little sis. How’ve you been?"
        else:
            MC "Hey, little Sara. How’ve you been?"
        Sara "I hope you aren’t referring to my tits."
        scene SR3_ES1_p5
        MC "Wh-What? I wasn’t- You’re my- and you’re younger th-"
        Sara "Hmmp! Calling me “little.” Not everyone can have a massive pair of boobs like Caroline or [Mom_name]!"
        MC "I- That isn’t what I meant by-"
        scene SR3_ES1_p6
        Sara "Hehe… Hahaha! YOUR FACE! Gotcha!"
        MC "*Sigh* I legitimately thought you were pissed off at me there."
        Sara "Ahahaha! Sorry, I couldn’t resist. I missed you, [player_name]."
        if persistent.incest_patch == True:
            MC "I missed you too, Sara. So, Mom says you’re not grounded anymore?"
        else:
            MC "I missed you too, Sara. So, Linda says you’re not grounded anymore?"
        scene SR3_ES1_p7
        Sara "Yup, I’m a free woman! Take a seat, [player_name]."
        MC "How did you get her to end it?"
        Sara "I came home one day with an A from my English Literature class. [Mom_name] was, like, super proud when she saw it."
        scene SR3_ES1_p8
        MC "Cool, what book were you studying?"
        Sara "No book, it was creative writing. Mr Stewart asked us to try our hand writing dystopian stories, so I spent ages thinking of the most dystopian things I could. In the end I decided to draw off my real life experience of being stuck in my room while grounded."
        MC "Huh, interesting. What was your story about, then?"
        Sara "So, hear me out… think of me being grounded and stuck inside all day, okay?"
        MC "Yeah?"
        scene SR3_ES1_p9
        Sara "Now, imagine the WHOLE WORLD was grounded!"
        MC "What?"
        Sara "There’s like this super deadly virus and everyone has to stay indoors to hide from it for a full year or it spreads and kills people!"
        MC "Geez, that sounds horrible."
        Sara "I know, right? Anyway, Mr Stewart said something like, “Prose and dramatic tension were akin to Sartre’s No Exit, even if the premise was a little unrealistic.” But hey - I got an A, and found a passion for writing."
        MC "I’m glad to hear that, Sara."
        scene SR3_ES1_p10
        Sara "Me too. You’ve got NO idea what it’s like! [Mom_name] ended up taking away the power cable for my computer. I couldn’t even do any gaming."
        MC "Well, it worked, didn’t it?"
        Sara "Yeah, I suppose."
        MC "Did [Dad_name] say anything?"
        scene SR3_ES1_p11
        Sara "When has [Dad_name] EVER tried to discipline us? He just rides along with whatever [Mom_name] decides. She’s the one who wears the pants in this house."
        if persistent.incest_patch == True:
            MC "You aren’t wrong there. I’ve always had a soft spot for Dad."
        else:
            MC "You aren’t wrong there. I’ve always had a soft spot for our old man."
        Sara "Me too."
        scene SR3_ES1_p12
        MC "(I don’t think Sara’s wearing a bra today! I can see the outline of her nipples through her tanktop!)"
        MC "(It’s been so long since I last saw her tits. Hopefully I’ll get another opportunity soon.)"
        MC "(Hmm, I wonder why she’s keeping her phone facing away from me.)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music2", loop=True, fadein = 2)

        scene SR3_ES1_p13
        MC "What are you reading on your phone, there?"
        Sara "N-Nothing!"
        if persistent.incest_patch == True:
            MC "Uh huh, I remember using that excuse when Mom almost caught me watching porn."
        else:
            MC "Uh huh, I remember using that excuse when Linda almost caught me watching porn."
        scene SR3_ES1_p14
        Sara "Eww! I’m not like you! I wasn’t watching porn!"
        MC "Well, if it’s not porn, what are you acting so cagey for?"
        Sara "I- It’s nothing. It’s private."
        scene SR3_ES1_p15
        MC "You've already texted me nudes! What could POSSIBLY be more private than that? Let me see!"
        Sara "I… I… Umm..."
        MC "C’mon Sara, it can’t be that bad?"
        scene SR3_ES1_p16
        Sara "W-Wait! Don’t!"
        Sara "D-Do you remember me… um… texting you earlier about the…"
        scene SR3_ES1_p17
        MC "When you said you wanted us to go to the mall together for ice cream?"
        Sara "Y-Yeah, but… I was thinking… Maybe we… I…"
        MC "(What on Earth has gotten into Sara? She’s acting so anxious right now.)"
        scene SR3_ES1_p18
        Sara "S-Sorry, don’t go anywhere, [player_name]. I just need a minute."
        MC "Uhh, okay. Take your time."
        Sara "I… wanted to go… to the mall with you, but…"
        scene SR3_ES1_p21
        Sara "(C’mon Sara! Be brave! You can do this!)"
        Sara "(Alright… I just have to tell [player_name] that this isn’t us going out for an ice cream and some shopping.)"
        Sara "(I have to explain that I want this to be an ACTUAL date like we’re boyfriend and girlfriend. I want people to KNOW that we’re a couple now.)"
        Sara "(Okay… Deep breaths, Sara. You can do this! Just ask him out. What’s the worst that could happen?)"
        scene SR3_ES1_p20
        MC "You okay there, Sara?"
        Sara "Y-Yeah, j-just a minute!"
        scene SR3_ES1_p19
        Sara "(If he says ‘no’ then it means he’s not actually interested in me romantically.. It would mean he was just using me for sex.)"
        Sara "(On the other hand, if he agrees to make it a date, then I’ll have my first ever boyfriend! Oh my God, I’m so nervous right now.)"
        MC "Your hands are shaking, Sara. Should I get [Mom_name]?"
        Sara "N-No!"
        scene SR3_ES1_p17
        Sara "I was w-wondering if y-you would… *gulp* ...want to… make our trip to the… mall… a… umm… date?"
        MC "A date, huh?"
        Sara "Y-Yeah, if that’s… cool… with you…"

        menu:
            "Of course, Sara! It’s a date.":
                scene SR3_ES1_p22
                MC "Of course, Sara! It’s a date."
                Sara "R-Really?!"
                MC "Yup! Just you and me!"
                scene SR3_ES1_p23
                MC "I’m going to head on and get ready for the mall."
                Sara "(That was a LOT less stressful than I imagined it would be. I don’t know what I was getting so worried for!)"
                scene SR3_ES1_p24
                Sara "Hold up, where should I meet you?"
                scene SR3_ES1_p25a
                MC "Tell you what, I’ll meet you at the mall on the weekend. How does that sound?"
                Sara "Great! I’ll catch you there."
                scene SR3_ES1_p25aa
                Sara "Oh, I should mention - I bought a special outfit, [player_name]. I think you’re reaaaaalllly gonna like it."
                MC "Mmm, I’m looking forward to seeing it. Catch you later, Sara."
                Sara "See you at the mall, [player_name]."
                $ SR3_romantic_route = True
                jump SR3_ES1_end
            "(I’m already in a relationship with someone else. I’m screwed if they catch me and Sara in public together! This date has to be kept on the down low for the meantime.)":

                scene SR3_ES1_p22
                MC "(Crap! I’ve already got other women in my life that I’m growing close too. If any of them catch Sara and me openly dating, things could get VERY awkward VERY quickly.)"
                MC "I… uh… Listen, Sara. Hmm… God… this is difficult."
                Sara "*Gulp*"
                MC "I’ll go out with you to the mall, but I don’t think we should publicly date each other. We can keep seeing each other as fuck buddies - we’ve got a great thing going on here."
                if persistent.incest_patch == True:
                    MC "Just… Just try to see this from an outsider’s perspective. Imagine someone from our school sees us kissing in public? What would they say, knowing that you’re my sister?"
                else:
                    MC "Just… Just try to see this from an outsider’s perspective. Imagine someone from our school sees us kissing in public? What would they say, knowing that you’re my girlfriend?"
                Sara "I… I understand…"
                scene SR3_ES1_p23
                MC "I’ll go and get myself ready. We’ll meet at the mall on the weekend."
                MC "Tell you what - ice cream is on me."
                Sara "*Sigh* Thanks…"
                scene SR3_ES1_p24
                MC "Don’t look so down, Sara. You can think of it as a date in your mind. It’s just not something we can make obvious in public. Okay?"
                scene SR3_ES1_p25b
                Sara "Yeah… I get it."
                MC "Cool. Catch you at the mall, Sara!"
                scene SR3_ES1_p25bb
                Sara "(I was excited for [player_name] to say yes, and prepared for him to tell me no. What I never expected was that he would leave me in some kind of romantic limbo.)"
                Sara "(What the heck am I supposed to do now? Does he even like me? Is there some other girl that he’s got his sights on?)"
                Sara "(Am I just some side chick to you, [player_name]? I gave you my anal virginity… was that not enough?)"
                $ SR3_romantic_route = False
                jump SR3_ES1_end

label SR3_ES1_end:
    $ SR3_ES1_talked = True
    $ SR3_weekend_event = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump sister_nerdy_morning1

