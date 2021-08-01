image CR4_sceurity2_p1 = "images/Nightclub/Corridor/N/Scenes/Security2/1.jpg"
image CR4_sceurity2_p2 = "images/Nightclub/Corridor/N/Scenes/Security2/2.jpg"
image CR4_sceurity2_p3 = "images/Nightclub/Corridor/N/Scenes/Security2/3.jpg"
image CR4_sceurity2_p4 = "images/Nightclub/Corridor/N/Scenes/Security2/4.jpg"
image CR4_sceurity2_p5 = "images/Nightclub/Corridor/N/Scenes/Security2/5.jpg"
image CR4_sceurity2_p6 = "images/Nightclub/Corridor/N/Scenes/Security2/6.jpg"
image CR4_sceurity2_p7 = "images/Nightclub/Corridor/N/Scenes/Security2/7.jpg"
image CR4_sceurity2_p8 = "images/Nightclub/Corridor/N/Scenes/Security2/8.jpg"
image CR4_sceurity2_p9 = "images/Nightclub/Corridor/N/Scenes/Security2/9.jpg"
image CR4_sceurity2_p10 = "images/Nightclub/Corridor/N/Scenes/Security2/10.jpg"
image CR4_sceurity2_p11 = "images/Nightclub/Corridor/N/Scenes/Security2/11.jpg"
image CR4_sceurity2_p12 = "images/Nightclub/Corridor/N/Scenes/Security2/12.jpg"
image CR4_sceurity2_p13 = "images/Nightclub/Corridor/N/Scenes/Security2/13.jpg"
image CR4_sceurity2_p14 = "images/Nightclub/Corridor/N/Scenes/Security2/14.jpg"
image CR4_sceurity2_p15 = "images/Nightclub/Corridor/N/Scenes/Security2/15.jpg"
image CR4_sceurity2_p16 = "images/Nightclub/Corridor/N/Scenes/Security2/16.jpg"
image CR4_sceurity2_p17 = "images/Nightclub/Corridor/N/Scenes/Security2/17.jpg"
image CR4_sceurity2_p18 = "images/Nightclub/Corridor/N/Scenes/Security2/18.jpg"
image CR4_sceurity2_p19 = "images/Nightclub/Corridor/N/Scenes/Security2/19.jpg"
image CR4_sceurity2_p20 = "images/Nightclub/Corridor/N/Scenes/Security2/20.jpg"
image CR4_sceurity2_p21 = "images/Nightclub/Corridor/N/Scenes/Security2/21.jpg"
image CR4_sceurity2_p22 = "images/Nightclub/Corridor/N/Scenes/Security2/22.jpg"
image CR4_sceurity2_p23 = "images/Nightclub/Corridor/N/Scenes/Security2/23.jpg"
image CR4_sceurity2_p24 = "images/Nightclub/Corridor/N/Scenes/Security2/24.jpg"
image CR4_sceurity2_p25 = "images/Nightclub/Corridor/N/Scenes/Security2/25.jpg"
image CR4_sceurity2_p26 = "images/Nightclub/Corridor/N/Scenes/Security2/26.jpg"
image CR4_sceurity2_p27 = "images/Nightclub/Corridor/N/Scenes/Security2/27.jpg"
image CR4_sceurity2_p28 = "images/Nightclub/Corridor/N/Scenes/Security2/28.jpg"
image CR4_sceurity2_p29 = "images/Nightclub/Corridor/N/Scenes/Security2/29.jpg"
image CR4_sceurity2_p30 = "images/Nightclub/Corridor/N/Scenes/Security2/30.jpg"
image CR4_sceurity2_p32 = "images/Nightclub/Corridor/N/Scenes/Security2/32.jpg"
image CR4_sceurity2_p33 = "images/Nightclub/Corridor/N/Scenes/Security2/33.jpg"
image CR4_sceurity2_p34 = "images/Nightclub/Corridor/N/Scenes/Security2/34.jpg"
image CR4_sceurity2_p35 = "images/Nightclub/Corridor/N/Scenes/Security2/35.jpg"
image CR4_sceurity2_p36 = "images/Nightclub/Corridor/N/Scenes/Security2/36.jpg"
image CR4_sceurity2_p37 = "images/Nightclub/Corridor/N/Scenes/Security2/37.jpg"
image CR4_sceurity2_p38 = "images/Nightclub/Corridor/N/Scenes/Security2/38.jpg"
image CR4_sceurity2_p39 = "images/Nightclub/Corridor/N/Scenes/Security2/39.jpg"
image CR4_sceurity2_p40 = "images/Nightclub/Corridor/N/Scenes/Security2/40.jpg"
image CR4_sceurity2_p41 = "images/Nightclub/Corridor/N/Scenes/Security2/41.jpg"
image CR4_sceurity2_p42 = "images/Nightclub/Corridor/N/Scenes/Security2/42.jpg"
image CR4_sceurity2_p43 = "images/Nightclub/Corridor/N/Scenes/Security2/43.jpg"

image CR4_sceurity_p1 = "images/Nightclub/Corridor/N/Scenes/Security/1.jpg"
image CR4_sceurity_p2 = "images/Nightclub/Corridor/N/Scenes/Security/2.jpg"
image CR4_sceurity_p3 = "images/Nightclub/Corridor/N/Scenes/Security/3.jpg"

default CR4_Cindy_S1 = False
default NC_Boss = False

label CR4_sceurity_lab:
    if CR4_guard == 2:
        hide screen map_button
        show screen nightclub_corridor_scr
        $ clickable = False
        MC "I need a password."
        $ clickable = True
        hide screen nightclub_corridor_scr
        jump nc_corridor_N

    if CR4_guard == 1:

        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_sceurity_p1 with dissolve
        MC "(This looks like where the manager’s office is.)"
        MC "Hey, I’d like to speak with the manager."

        scene CR4_sceurity_p2
        $ Bodyguard1_name = __("Bodyguard1")
        $ Bodyguard2_name = __("Bodyguard2")
        Bodyguard1 "Password?"
        MC "Excuse me?"
        Bodyguard1 "Password."
        MC "Umm… I just want to speak with the-"

        scene CR4_sceurity_p3
        Bodyguard1 "No password. No entry."
        MC "How do I get a password?"
        Bodyguard1 "Sir, you clearly don’t know what you’re getting involved in. Please stay away."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)

        $ CR4_Cindy_S1 = 1
        $ can_hide_windows = False
        $ CR4_guard = 2
        jump nc_corridor_N

    if CR4_guard == 3:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_sceurity2_p1 with dissolve
        Bodyguard1 "*Groan* Look who it is again - I already told you, kid: No password; no entry."
        Bodyguard1 "Stop wasting my time and go back onto the dancefloor."
        Bodyguard1 "If you got a complaint about the estabilshment then raise it with the bartender, okay?"

        scene CR4_sceurity2_p2
        MC "Truth."
        Bodyguard1 "E-Excuse me?"
        MC "Truth."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

        scene CR4_sceurity2_p3

        Bodyguard1 "I… uh... "
        MC "That IS the password, isn’t it?"

        scene CR4_sceurity2_p4
        Bodyguard1 "Just give me a minute, kid. I need to figure out what’s going on here."
        MC "Well? Are you going to let me in now?"
        Bodyguard1 "Hold your horses, kiddo. "

        scene CR4_sceurity2_p5
        MC "Are you texting security to kick me out now?"
        Bodyguard1 "…"
        MC "(Dammit, I’m NEVER getting past these guys.)"

        scene CR4_sceurity2_p6
        Bodyguard1 "Well… hot damn."
        MC "Huh?"
        Bodyguard1 "That’s a yes from the Boss. He’s content to meet you."

        scene CR4_sceurity2_p7
        Bodyguard1 "Usual rules apply: no touching him, no sudden moves, and we’ll be right here at the door just in case you try anything funny."
        MC "Seriously? You’re letting me in now? This isn’t you pulling my leg?"

        scene CR4_sceurity2_p8
        Bodyguard2 "He’s not winding you up. My gaffer never jokes around. Head on in, fella."
        Bodyguard1 "The door’s unlocked."

        scene CR4_sceurity2_p9
        MC "Um… Hey there, my name is [player_name]."
        "…"
        MC "I’m here to speak with you about a… about a necklace?"

        scene CR4_sceurity2_p10
        MC "*Ahem* Did a guy named Charles give you a necklace a few days ago?"
        MC "It’s a very precious piece of family memorabilia. It was stolen from someone."

        scene CR4_sceurity2_p11
        Cindy "Hush, baby. You’re yabbering WAY too much."
        Cindy "The Boss will get to you when he gets to you, mmmkay?"

        scene CR4_sceurity2_p12
        MC "(Cindy is here too. I didn’t realise she was this close to whoever is running this show.)"
        MC "Umm… sir? Hello?"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Danger Storm.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_sceurity2_p13
        Headmaster "Why, hello - if it isn’t Iron Cajones himself."
        Headmaster "I see you’re still making your mark in the world after trying to ask out Ms. Celia."

        scene CR4_sceurity2_p14
        MC "Wh-What are you doing here?!"
        MC "Are you not supposed to be, like, running a school right now?!"

        scene CR4_sceurity2_p15
        Headmaster "I prefer to keep my professional life and my… other professional life separate."
        Headmaster "I can see… one connection, and ONLY one connection that links you and me here today."
        Headmaster "Cindy."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)

        scene CR4_sceurity2_p16
        Cindy "Uh oh."
        Headmaster "How does one of my students know about my job here?"
        Cindy "I uh…"
        Headmaster "And, please tell me, how did they know the password?"

        scene CR4_sceurity2_p17
        Headmaster "Don’t think that I don’t know you sent him to steal those joints for you. Those were a special present from my favourite rapper - Soup Dog."
        Headmaster "Do you know how much they were worth? Easily over a grand!"
        Headmaster "So, you’ve threatened my security, risked leaking my private life into my school, and had one of my favourite possessions stolen."

        scene CR4_sceurity2_p18
        Cindy "Aww, c’mon! They’re just stupid joints!"
        Headmaster "And yet, you wanted them more than any of the other joints you could have had."
        Cindy "Because you forbid me from taking them! That only made me want to smoke them more! Duh!"

        scene CR4_sceurity2_p19
        Headmaster "That’s it! You’re going to repay me for what you stole!"
        Cindy "Oh please, whatcha going to do? Cry about it?"
        Headmaster "Much worse than that."

        scene CR4_sceurity2_p20
        Cindy "H-Hey! No need to stand up or anything, b-baby!"
        Cindy "We’re cool! We cool, right?"
        Headmaster "We. Are. Not. Cool."

        scene CR4_sceurity2_p21
        "*SLAP*"
        Cindy "OW!"

        scene CR4_sceurity2_p22
        Cindy "I’m sorry, okay? I shouldn’t have nicked your joints!"
        Headmaster "You shouldn’t have given out MY password to MY office either!"

        scene CR4_sceurity2_p23
        MC "(Fuck me… This is so awkward... )"
        MC "(I’m watching my Principal slap around one of his students for stealing his drugs… This must be what it feels like to go to school in Detroit.)"

        scene CR4_sceurity2_p24
        Headmaster "Take her away!"
        Headmaster "Throw her in the back room until she repays her debt!"

        scene CR4_sceurity2_p25
        Bodyguard1 "Sure thing, boss!"
        Bodyguard1 "Can I just add, that you look fantastic in that suit, sir!"
        Headmaster "Stop trying to get into my pants, and just take her away."
        Bodyguard1 "Sorry, sir. Yes, sir."

        scene CR4_sceurity2_p26
        Cindy "HEEEYYY! Put me down, you big meanie!"
        Headmaster "Apologies for this, [player_name]. This must seem very unprofessional of me."
        MC "It’s… alright."

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_sceurity2_p27
        Headmaster "That silly girl… If she'd only waited she would have gotten those joints anyway. I was going to give them to her, for her birthday."
        Cindy "What?! Are you SERIOUS?! I went through all that effort for nothing!?"
        MC "Err…"

        scene CR4_sceurity2_p28
        Cindy "I wasn’t even the one who snuck into the warehouse! It was HIM!"
        Cindy "He was the one who-"
        Headmaster "Quiet, girl. I KNOW you put him up to it."

        scene CR4_sceurity2_p29
        Headmaster "Now, hurry up and get her out of my sight."
        Bodyguard1 "Right away, sir."

        scene CR4_sceurity2_p30
        Headmaster "Did you watch how I handled that, [player_name]?"
        Headmaster "That is how you command respect. That bitch will serve her time and repay her debt."
        Headmaster "When she gets out, she’ll understand the value of loyalty. She’ll respect me."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Danger Storm.mp3', channel="music1", loop=True, fadein = 2)

        scene CR4_sceurity2_p32
        MC "Sir, I-"
        Headmaster "I don’t blame you for breaking into my warehouse. There was clearly something very important about this necklace."
        Headmaster "It takes some massive fucking balls to risk your life over some metal."

        scene CR4_sceurity2_p33
        Headmaster "Tell me your story, [player_name]. Entertain me."
        MC "Right… A while ago, Charles busted up your club. He owed you money."
        Headmaster "Yes. Go on?"

        scene CR4_sceurity2_p34
        MC "Charles couldn’t afford to pay it. He attacked someone very close to me and stole a necklace that's a family heirloom."
        MC "I have heard rumours, he gave it to you to repay his debt."

        scene CR4_sceurity2_p35
        MC "She’s devastated over the loss of it. I just… want it back for her."
        MC "Do you have it?"

        scene CR4_sceurity2_p36
        Headmaster "I do."
        MC "You have it?! Are you sure it’s the right necklace?"
        Headmaster "It’s not often, people bring me beautiful antique necklaces."

        scene CR4_sceurity2_p37
        Headmaster "It did cost me a lot of money though. I accepted this as payment in lieu of the damage."
        Headmaster "I hope you understand that it wouldn’t make business sense to just… give it away again."
        MC "Y-Yeah… I know…"

        scene CR4_sceurity2_p38
        Headmaster "You told me that the one who stole the necklace was the same person who damaged my nightclub. Is that true?"
        MC "Yes. It is. Charles: he’s about a foot taller than me, brown hair, looks like every frat boy ever."
        Headmaster "Do me a favour - check the monitors for me. Find this Charles chap. If the security cameras corroborate this young man’s story, then we will return the necklace."
        Bodyguard1 "Yes, sir!"

        scene CR4_sceurity2_p39
        Headmaster "And as for Charles… I will be dealing with him myself."
        Headmaster "I might be the head honcho of a rather clandestine network of individuals - but I abhor those who prey on the weak. There’s something grossly unfair about that."

        scene CR4_sceurity2_p40
        MC "Thank you, sir."
        Headmaster "I have a lot to consider right now. Would you kindly return tomorrow?"
        MC "Yes, not a problem."

        scene CR4_sceurity2_p41
        MC "Sir?"
        Headmaster "Hmm?"
        MC "Thank you for listening. And sorry again for breaking into your warehouse."

        scene CR4_sceurity2_p42
        Headmaster "Water off a duck’s back, kid. Now, I’ll start working with my men to substantiate your claims about Charles."
        MC "Thank you, sir."

        scene CR4_sceurity2_p43
        MC "(In the grand scheme of things, this probably went better than expected!)"
        MC "(I know where Caroline’s necklace is now, and I know that once they see Charles trashing the place they might be able to return it to me! Things are finally starting to look up again!)"

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ CR4_guard = 4
        $ NC_Boss = 1
        jump nc_corridor_N

