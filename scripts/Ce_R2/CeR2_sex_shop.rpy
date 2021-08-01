image CeR2_sex_shop_p1 = "images/CeR2/Shop/1.jpg"
image CeR2_sex_shop_p2 = "images/CeR2/Shop/2.jpg"
image CeR2_sex_shop_p3 = "images/CeR2/Shop/3.jpg"
image CeR2_sex_shop_p4 = "images/CeR2/Shop/4.jpg"
image CeR2_sex_shop_p5 = "images/CeR2/Shop/5.jpg"
image CeR2_sex_shop_p6 = "images/CeR2/Shop/6.jpg"
image CeR2_sex_shop_p7 = "images/CeR2/Shop/7.jpg"
image CeR2_sex_shop_p8 = "images/CeR2/Shop/8.jpg"
image CeR2_sex_shop_p9 = "images/CeR2/Shop/9.jpg"
image CeR2_sex_shop_p10 = "images/CeR2/Shop/10.jpg"
default CeR2_LS = False
default Ce_sms4 = False

label CeR2_sex_shop:
    scene CeR2_sex_shop_p1
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    menu:
        "Look at the table.":
            jump sex_shop_table_label
        "{color=#00ff00}Ask for a electro-Stimulation dildo.{/color}" if CeR2_dildo_buy >= 1:
            jump CeR2_sex_shop_lab
        "Back":

            jump sex_shop_evening_label

label CeR2_sex_shop_lab:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if CeR2_dildo_buy == 1:
        scene CeR2_sex_shop_p1
        S "Hey there, need any help finding something?"
        MC "Hi. Yes actually. It’s a bit of a weird one though."
        S "Haha, don’t worry, honey. Three years working in this store, and I’ve heard them all."

        scene CeR2_sex_shop_p2
        MC "I’m looking for a dildo for-"
        S "A guy?"
        MC "No, a girl!"

        scene CeR2_sex_shop_p3
        S "Oh sorry, you looked like the type of guy who… Nevermind."
        MC "I’m looking for a dildo that has-"
        S "Different vibration modes?"
        MC "No, it-"

        scene CeR2_sex_shop_p2
        S "Squirting pump with a bottle of fake cum?"
        MC "No!"
        S "Pleasure bumps with a rotation mode?"
        MC "No! I just need a dildo with built-in electric stimulation."

        scene CeR2_sex_shop_p3
        S "Ahh… Why didn’t you just say?"

        scene CeR2_sex_shop_p4
        S "Give me a few minutes. I’ll check our stock for you and see what I can find."
        MC "Thank you."
        MC "(Christ, I thought she’d NEVER shut up!)"

        scene CeR2_sex_shop_p5
        S "I gotta admit, it’s not something I get asked about every day."
        S "If I don’t have it in stock, then I can certainly order it in for you."
        scene CeR2_sex_shop_p6
        MC "Thanks. Appreciate it!"
        S "I won’t be a moment!"

        scene CeR2_sex_shop_p7
        S "Ta-da! I present to you, the Zapper Maximus 9001."

        scene CeR2_sex_shop_p8
        MC "Is that… a military grade battery?"
        S "Absolutely! It’s a prototype. They tend to send out one to each shop to see how well they sell. If there’s demand, they’ll make more."

        scene CeR2_sex_shop_p9
        MC "What does it… do?"
        S "I’ve never tried it myself, but the advertising campaign made it sounds pretty impressive."
        S "Hang on, I might have the box with the description back here."

        scene CeR2_sex_shop_p8
        S "*Ahem* Here we go…"
        S "Where the fuck did you just fucking stick me, you little bitch? I’ll have you know I graduated top of my class in the sex toy tests, as well as being involved in numerous human rights violations, and I have over 300 confirmed orgasms."
        MC "Is this seriously how they are trying to advertise their product?"
        S "Shush, I’m not done yet."
        S "I am trained in anal warfare and I’m the top dildo in the entire US armed forces. You are nothing to me but just another hole. I will fuck you with force the likes of which has never been seen before on this Earth. Mark my fucking words."
        S "You think you can get away with only window shopping and not purchasing me? Think again, fucker. "
        S "As we speak I am being shipped across stores all over the USA, and your holes are being traced so you better prepare for the cumming storm, faggot. The storm that destroys that pretty little thing you call a pussy."
        MC "Are we almost there?"
        S "No."
        S "You’re gonna fucking cum, kiddo. I can fit anywhere, anytime, and I can make you cum in over seven hundred ways, and that’s without the power turned on. "
        S "Not only am I extensively trained in vaginal sex, but I also have access to the entire Karma Sutra and I will use it to its full extent to wipe your sexy ass off the bed, you dumb slut."
        MC "(How the fuck is this a sales pitch?!)"
        S "If only you could have known what unholy retribution your “clever” request to ask for an electrostimulation dildo was about to bring down upon your pussy, maybe you would have held your fucking tongue."
        S "But you couldn’t, you didn’t, and now you’re paying the price, you fucking whore. I will make you cum buckets, and you will drown in it. You’re gonna cum, kiddo."

        scene CeR2_sex_shop_p9
        S "So, what do you think?"
        MC "..."
        MC "It’s perfect for her. How much?"
        S "$600."
        if inventory.money >= 600:
            $ CeR2_LS = 1
            scene CeR2_sex_shop_p10
            MC "Deal."
            S "Just… don’t use full power. Okay? I’m not even sure this thing is safe for human use."
            $ inventory.buy(Ce_dildo)
            $ CeR2_dildo_buy = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:

            scene CeR2_sex_shop_p7
            MC "Actually… that’s a bit pricier than I anticipated."
            S "That’s okay. I can hold onto it for you. I highly doubt there’s many other customers interested in such an… exotic toy."
            MC "Thanks, I’ll be back when I’ve got the cash."
            $ CeR2_dildo_buy = 2
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

            $ can_hide_windows = False
            jump sex_shop_evening_label

    if CeR2_dildo_buy == 2:
        scene CeR2_sex_shop_p5
        MC "Could you remind me, how much for that electro-Stimulation dildo?"
        scene CeR2_sex_shop_p9
        S "The Zapper Maximus 9001?"
        MC "Yes."
        S "$600."
        if inventory.money >= 600:
            scene CeR2_sex_shop_p10
            MC "Deal."
            S "Just… don’t use full power. Okay? I’m not even sure this thing is safe for human use."
            $ inventory.buy(Ce_dildo)
            $ CeR2_dildo_buy = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ CeR2_LS = 1
            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:

            scene CeR2_sex_shop_p7
            MC "Actually… that’s a bit pricier than I anticipated."
            S "That’s okay. I can hold onto it for you. I highly doubt there’s many other customers interested in such an… exotic toy."
            MC "Thanks, I’ll be back when I’ve got the cash."
            $ CeR2_dildo_buy = 2
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

            $ can_hide_windows = False
            jump sex_shop_evening_label

