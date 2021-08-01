image SR3_we_SC_wait_p1 = "images/v71/2_WE/3_Shopping Centre/1.jpg"
image SR3_we_SC_wait_p2 = "images/v71/2_WE/3_Shopping Centre/2.jpg"
image SR3_we_SC_wait_p3 = "images/v71/2_WE/3_Shopping Centre/3.jpg"
image SR3_we_SC_wait_p4 = "images/v71/2_WE/3_Shopping Centre/4.jpg"
image SR3_we_SC_wait_p5 = "images/v71/2_WE/3_Shopping Centre/5.jpg"
image SR3_we_SC_wait_p6 = "images/v71/2_WE/3_Shopping Centre/6.jpg"
image SR3_we_SC_wait_p7 = "images/v71/2_WE/3_Shopping Centre/7.jpg"
image SR3_we_SC_wait_p8 = "images/v71/2_WE/3_Shopping Centre/8.jpg"
image SR3_we_SC_wait_p9 = "images/v71/2_WE/3_Shopping Centre/9.jpg"


label SR3_SC_floor2_wait_locked:
    hide screen displayTextScreen
    hide screen map_button
    show screen SC_scr
    $ clickable = False
    MC "Sara is waiting for me."
    hide screen SC_scr
    $ clickable = True
    jump SC_label


label SR3_we_SC_wait_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if SR3_romantic_route == True:
        scene SR3_we_SC_wait_p1
        MC "(Oh wow! That dress is so skimpy! Sara looks really hot in it!)"
        MC "Sara! You look incredible!"
        scene SR3_we_SC_wait_p2
        Sara "[player_name]! I’m glad you like it! I chose it especially for you. It isn’t too revealing, is it?"
        MC "That’s the best part about it, Sara!"
        Sara "Haha, you perv!"
        scene SR3_we_SC_wait_p3
        MC "Seriously though, Sara. You look absolutely amazing right now. You’re the cutest person in the whole mall."
        Sara "Aww, stooop… You’re gonna make me blush."
        scene SR3_we_SC_wait_p4
        MC "Haha, it’s true though. You look good."
        Sara "Thanks for coming today, [player_name]. This date really means a lot to me."
        MC "I know. I means a lot to me too, Sara."
        Sara "I’m glad to hear you say that."
        scene SR3_we_SC_wait_p5
        MC "So, where do you want to head first? I remember you mentioned something about an ice cream parlour opening up here."
        Sara "Yeah! It’s the same chain Caroline used to take me to when I was just a kid, Thick n’ Creamy!"
        MC "They actually named their brand ‘Thick n’ Creamy’?"
        Sara "I mean, why not? It describes it perfectly!"
        scene SR3_we_SC_wait_p6
        MC "(Sara’s outfit is super cute, but it’s also a wardrobe malfunction waiting to happen.)"
        MC "(I mean, her skirt is so short that I can practically see her panties. And if that dress slips even a little bit she’ll be exposing her boobs to the whole mall!)"
        MC "How long has it been since you last went to Thick n’ Creamy?"
        scene SR3_we_SC_wait_p7
        Sara "Oh geez… It must be… five or six years since Caroline and I last went out together."
        MC "Come to think of it, I hardly ever see you two hanging out. What happened?"
        Sara "We just grew apart, y’know? She’s older than I am, so she matured quicker and found her own hobbies and interests."
        scene SR3_we_SC_wait_p8
        Sara "She’s been focused on her relationships, education, and starting a business, these past few years. I think I just sorta fell off her radar."
        MC "I’m sorry, Sara. Y’know, [Dad_name] gave me some advice once. It’s never too late to try and reconnect with family if you ever lose touch."
        MC "I mean, the fact that this mall has opened so close to our home, gives you the perfect opportunity to ask Caroline out for the day. Go and spend some time together with her. Do some shopping, grab an ice cream together for old time’s sake."
        scene SR3_we_SC_wait_p4
        Sara "Thanks, [player_name]. I think you’re right. I’ll speak with her later on this week."
        MC "Good to hear."
        scene SR3_we_SC_wait_p9
        Sara "Anyway! Thick n’ Creamy have their parlour and an ice cream van today! How about we get it from the van and walk around the mall?"
        MC "Sounds good to me!"
        Sara "C’mon! This way!"
        jump SR3_we_SC_wait_end
    else:
        scene SR3_we_SC_wait_p1
        Sara "(I hope [player_name] shows up…)"
        Sara "(He said he wanted our date to be kept on the down low so people wouldn’t notice us together. Maybe he was just saying that because I put too much pressure on him in my room?)"
        Sara "(Maybe he just won’t come at all…)"
        MC "Hey, Sara."
        scene SR3_we_SC_wait_p2
        Sara "[player_name]! You came!"
        MC "Haha, of course I did. I wasn’t gonna miss the opening of the new mall after all!"
        scene SR3_we_SC_wait_p8
        Sara "Oh, right… Yeah…"
        Sara "Umm, are we still doing the ‘secret date’? Do you think we could maybe make it official and just let everyone know we’re together?"
        MC "Sorry Sara, half our school looks like they’re here today."
        MC "(Plus, it would be super awkward if someone else I’m romantically interested in saw me dating Sara.)"
        scene SR3_we_SC_wait_p7
        Sara "*Sigh* That’s okay…"
        Sara "(I was really hoping he’d change his mind about this. I guess I just haven’t proven myself worthy to be his girlfriend in public yet…)"
        Sara "(Maybe I need to do more, or treat him better? I guess the blowjob I gave him in the bathroom wasn’t good enough.)"
        scene SR3_we_SC_wait_p4
        MC "So, where’s this great ice cream parlour you were talking about? The one you and Caroline used to go to?"
        Sara "The one we used to go to was in a different city. She used to drive us over there after school. This is just another franchise opening."
        MC "Ahh, fair enough."
        scene SR3_we_SC_wait_p6
        Sara "They’ve actually got the ice cream parlour set up as well as a van. Do you want to sit in and grab an ice cream, or get one to take away and we’ll walk around the mall?"
        MC "(It’s gonna look less like a date if we’re just walking together.)"
        MC "How about we just grab a couple of cones from the van and walk around?"
        scene SR3_we_SC_wait_p9
        Sara "Sure, no problem. It’s over this way!"
        Sara "(I shouldn’t beat myself up too much. [player_name] still showed up today! That means he’s still interested in me. If he didn’t want to date me, he never would have come at all! I think he just needs some time before making this public.)"
        Sara "(I just have to focus on being the most awesome girlfriend I can be, then he’ll want EVERYONE to know we’re together!)"
        Sara "Hurry up, [player_name]! Let’s go! You’re buying! Hehe!"
        jump SR3_we_SC_wait_end

label SR3_we_SC_wait_end:
    $ SR3_we_SC_wait = False
    $ SR3_we_SC_bus = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump SC_label

