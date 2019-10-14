



label MLR2_ES3_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene garage_evening with dissolve
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen garage_evening
    $ can_hide_windows = False
    $ clickable = False
    MC "..."
    MC "Now, as I think about it.. I should wear something better.."
    MC "Yeah. I should quickly go change!"
    hide screen garage_evening
    $ clickable = True
    scene black
    $ can_hide_windows = True
    $ renpy.pause(3,hard = True)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR2_ES3_p0a with dissolve
    if renpy.loadable("patch.rpy"):
        MC "(Okay? Date night with Mom. What should I wear?)"
    else:
        MC "(Okay? Date night with Linda. What should I wear?)"
    MC "(I don’t want to look TOO formal.)"
    MC "(But I have to dress up, smarter than usual.)"
    scene black
    $ renpy.pause(2,hard = True)
    scene MLR2_ES3_p0b

    MC "(Yeah, this is looking good.)"
    MC "(It’s only dinner anyway.)"
    if renpy.loadable("patch.rpy"):
        MC "(Okay - time to meet Mom in the garage.)"
    else:
        MC "(Okay - time to meet Linda in the garage.)"


    scene black
    $ renpy.sound.play('sfx/door_open.mp3', loop=False)
    $ renpy.pause(3,hard = True)

    scene MLR2_ES3_p1 with dissolve
    if renpy.loadable("patch.rpy"):
        MC "(I’ve been waiting in the garage for ten minutes now. I wonder if Mom has forgotten about our meeting.)"
    else:
        MC "(I’ve been waiting in the garage for ten minutes now. I wonder if Linda has forgotten about our meeting.)"
    MC "(Then again, she’s a woman - and they can take FOREVER, getting ready to go out.)"
    MC "(I’ll give her another five minutes before I search for her.)"

    scene MLR2_ES3_p2 at pandown3

    Mom "Hi, Sweetie. Sorry to keep you waiting!"
    MC "Wow!"
    Mom "What do you think? Like my dress?"
    MC "Hell yeah! It’s amazing!"


    scene MLR2_ES3_p3
    if renpy.loadable("patch.rpy"):
        Mom "I haven’t worn this little number, in almost ten years. I just never felt sexy enough to wear it while I was with your father."
    else:
        Mom "I haven’t worn this little number, in almost ten years. I just never felt sexy enough to wear it while I was with Bob."
    Mom "What do you think? Is it too short to go out in?"
    MC "Maybe a little bit."
    Mom "Good. That’s what I was aiming for."

    scene MLR2_ES3_p4
    if renpy.loadable("patch.rpy"):
        MC "You ARE looking great tonight, Mom."
    else:
        MC "You ARE looking great tonight, Linda."
    Mom "Thanks! I actually had to climb into the attic to find this dress. It was packed away."

    scene MLR2_ES3_p5

    Mom "Now, hop in the car. I’ll drive us to the restaurant."
    Mom "We’re already a little bit late!"
    MC "Okay, let’s go!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3,hard = True)


    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    scene MLR2_ES3_p6
    if renpy.loadable("patch.rpy"):
        MC "(I wonder if I’ll get to fuck Mom tonight?)"
    else:
        MC "(I wonder if I’ll get to fuck Linda tonight?)"
    MC "(That’s what happens after a guy and girl come back from a date, right?)"
    MC "(I should probably try and bring her back to my bedroom, after we get home.)"
    MC "(God, I’m getting so nervous. Is this even a date? Should I have brought her some flowers?)"

    scene MLR2_ES3_p7

    Mom "You okay there, Sweetie? You’ve been awfully quiet."
    MC "Y-Yeah, I’m fine."
    Mom "Are you sure? You can tell me anything at all."

    scene MLR2_ES3_p8

    MC "Well… I was kind of nervous about tonight."
    MC "I didn’t bring you any flowers or chocolates - and to be honest, I’m not even sure if this is a date or not. Or maybe just-"
    Mom "[player_name], just relax and don’t think too much about it, okay?"
    MC "But...-"
    scene MLR2_ES3_p9

    Mom "-Haha! You’re adorable. Just focus on enjoying yourself tonight, okay?"
    if renpy.loadable("patch.rpy"):
        MC "Alright. Thanks, Mom. Sorry I was so nervous."
    else:
        MC "Alright. Thanks, Linda. Sorry I was so nervous."
    Mom "It’s alright, Sweetie. Just let me lead the way."


    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3,hard=True)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene MLR2_ES3_p10

    Mom "Here we go - you’ll absolutely LOVE the food."
    MC "Uhh… Where are we sitting? It looks like they’re really busy tonight."
    Mom "How about you go and find us an empty table?"

    scene MLR2_ES3_p11

    Mom "I’ll pop off to the ladies’ room, and join you in a couple of minutes."
    if renpy.loadable("patch.rpy"):
        MC "No problem, Mom."
    else:
        MC "No problem, Linda."
    jump resteurant_label_rep

label resteurant_label_rep:
    scene resteurant_background
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    $ can_hide_windows = False
    call screen resteurant_scr_rep


screen resteurant_scr_rep:

    imagebutton:
        xpos 416
        ypos 254
        focus_mask True
        idle "images/home/garage/evening/scenes/MLR2_ES3/b2.png"
        hover "images/home/garage/evening/scenes/MLR2_ES3/b2_hover.png"
        hovered Show("displayTextScreen", displayText = "Free Table")
        action [Hide("displayTextScreen"),Jump("resteurant_table_label_rep")]
        unhovered Hide("displayTextScreen")


label resteurant_table_label_rep:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene MLR2_ES3_p12
    $ can_hide_windows = True
    Mom "Good find! This is a nice little booth."
    MC "(That dress is so short; I can see her panties!)"
    if renpy.loadable("patch.rpy"):
        MC "Thanks, Mom."
    else:
        MC "Thanks, Linda."

    scene MLR2_ES3_p13

    Mom "How about you choose the dish tonight?"
    MC "Are you sure?"
    Mom "Everything is really great here. You can’t go wrong, I promise."
    MC "Are there any foods you don’t like?"
    Mom "Red onion and anchovies. I’ll eat anything else."
    jump dish_menu_label_rep

label dish_menu_label_rep:
    scene dish_menu_bg
    $ can_hide_windows = False
    call screen dish_menu_scr_rep


screen dish_menu_scr_rep:
    imagebutton:
        xpos 185
        ypos 223
        focus_mask True
        idle "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b1.png"
        hover "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b1_hover.png"
        action [Hide("displayTextScreen"),Jump("dish1_label_rep")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 185
        ypos 628
        focus_mask True
        idle "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b2.png"
        hover "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b2_hover.png"

        action [Hide("displayTextScreen"),Jump("dish2_label_rep")]
        unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 1144
        ypos 223
        focus_mask True
        idle "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b3.png"
        hover "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b3_hover.png"

        action [Hide("displayTextScreen"),Jump("dish3_label_rep")]
        unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 1144
        ypos 628
        focus_mask True
        idle "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b4.png"
        hover "images/home/garage/evening/scenes/MLR2_ES3/Dish Select/b4_hover.png"

        action [Hide("displayTextScreen"),Jump("dish4_label_rep")]
        unhovered Hide("displayTextScreen")


label dish1_label_rep:
    $ dish_select = 1
    jump MLR2_ES3_continue_label_rep
label dish2_label_rep:
    $ dish_select = 2
    jump MLR2_ES3_continue_label_rep
label dish3_label_rep:
    $ dish_select = 3
    jump MLR2_ES3_continue_label_rep
label dish4_label_rep:
    $ dish_select = 4
    jump MLR2_ES3_continue_label_rep


label MLR2_ES3_continue_label_rep:
    scene MLR2_ES3_p14
    $ can_hide_windows = True

    Mom "So, while we’re waiting for our meal to come, I’ve got a question I really wanted to know."
    MC "Uh huh?"
    Mom "I was wondering. Are you still looking for a girlfriend?"

    scene MLR2_ES3_p15
    window hide

    menu:
        "No, I’m still trying to get over that embarrassment with Celia.":
            scene MLR2_ES3_p15

            MC "Not right now. I’m still the laughing stock of the school, because of that Celia incident."
            Mom "Ahh, of course. Well, that’s perfectly understandable."

            scene MLR2_ES3_p16

            Mom "Just return to dating in your own time, whenever you feel comfortable."
            Mom "And, as always, I’m always here if you need me."
            if renpy.loadable("patch.rpy"):
                MC "Thanks, Mom. You’re the best."
            else:
                MC "Thanks, Linda. You’re the best."
            jump after_menu_MLR2_ES3_continue_label_rep
        "Yeah, I’m still searching.":

            scene MLR2_ES3_p14
            if renpy.loadable("patch.rpy"):
                MC "Yeah, Mom. I’m still searching."
            else:
                MC "Yeah, Linda. I’m still searching."
            Mom "Oh."

            scene MLR2_ES3_p15

            Mom "Is there… anyone in particular?"
            MC "A few hot girls, here and there."
            Mom "Hmm..."
            Mom "I don’t think it’s a good idea for you to rush into a relationship again, so soon after what happened last time with your teacher."
            MC "Umm… I’ll keep that in mind."
            jump after_menu_MLR2_ES3_continue_label_rep
        "I’m not sure.":

            scene MLR2_ES3_p15

            MC "I’m not sure, right now."
            if renpy.loadable("patch.rpy"):
                Mom "That’s okay. You know - both your sisters are single. Maybe you could pick up one of them!"
                MC "MOM!"
            else:
                Mom "That’s okay. You know - both your friends are single. Maybe you could pick up one of them!"
                MC "LINDA!"


            scene MLR2_ES3_p16

            Mom "Hahaha! I’m just teasing! After all we’ve done together, that joke was HARDLY taboo, right?"
            MC "Heh... I guess so."
            scene black
            $ renpy.pause(2,hard=True)
            jump after_menu_MLR2_ES3_continue_label_rep



label after_menu_MLR2_ES3_continue_label_rep:
    if dish_select == 1:
        scene MLR2_ES3_p17a
        $ can_hide_windows = True
        Mom "Mmm... Roasted salmon with sweet potato. Good choice."
        Mom "I always loved how they both melt in your mouth, when slow-cooked."

        scene MLR2_ES3_p18a

        Mom "Well, let’s dig in, shall we?"
        MC "Sounds good to me! Want any salt or pepper?"
        Mom "Just a little pepper, please. Too much salt, and you’ll ruin the salmon."

    if dish_select == 2:
        scene MLR2_ES3_p17b

        Mom "Tomato and pesto linguine. Very nice."
        Mom "I can’t remember the last time I had a proper pasta dish - it must have been three years ago, when I last visited Italy."
        MC "Was the food good, over there?"
        Mom "It was incredible! Completely out of this world!"

        scene MLR2_ES3_p18b
        if renpy.loadable("patch.rpy"):
            MC "What about Dad? Did he enjoy the food in Italy?"
        else:
            MC "What about Bob, did he enjoy the food in Italy?"
        Mom "Mmm... Absolutely not. He didn’t even come with me. I went by myself - ended up having dinner with a lovely young Italian lady named Viviana."
        Mom "Last time I heard from her, I think she was looking to immigrate here for work."

    if dish_select == 3:
        scene MLR2_ES3_p17c

        Mom "Hmm… Sausages and potatoes…"
        Mom "You sure know how to treat a girl!"
        MC "(Uh oh… Maybe I should have picked something more… upmarket.)"

        scene MLR2_ES3_p18c

        Mom "At least it tastes pretty good."
        MC "(Phew!)"
        if renpy.loadable("patch.rpy"):
            MC "(I think I’m off the hook, at least. I should definitely consider a fancier dish, if I ever take Mom out for dinner again!)"
        else:
            MC "(I think I’m off the hook, at least. I should definitely consider a fancier dish, if I ever take Linda out for dinner again!)"

    if dish_select == 4:
        scene MLR2_ES3_p17d

        Mom "I must admit. I’ve never actually tried seafood salad before."
        Mom "My loathing of anchovies has made me somewhat anxious when it comes to trying new seafoods."
        MC "Give it a go - you’ll probably like it!"
        MC "If it turns out you don’t we can just order another dish - I’ll pay."

        scene MLR2_ES3_p18d

        Mom "Hmm…"
        MC "Not a fan?"
        Mom "It’s… just alright. A nice pasta would have probably gone down better."
        MC "Ahh, I’ll remember that for future."
        Mom "Don’t worry - it’s nice to be pushed out of my comfort zone every now and then."


    scene MLR2_ES3_p19

    Mom "Thank you for joining me tonight, [player_name]."
    if renpy.loadable("patch.rpy"):
        MC "You don't’ need to thank me, Mom. I’m having a great time!"
    else:
        MC "You don't need to thank me, Linda. I’m having a great time!"
    Mom "How about a wine, then? Red or white?"
    MC "Uhh…"
    Mom "You’re clearly not a wine connoisseur. We’ll go for a red."
    scene black
    $ renpy.pause(2,hard = True)
    scene MLR2_ES3_p20

    Mom "Well? What do you think?"
    MC "It’s… uh… fruity?"
    Mom "Someone more experienced would probably describe this as: floral, with strong undertones of red grape, garnished with a crisp afterbite."
    Mom "But, yes, I suppose “fruity” works too."

    scene MLR2_ES3_p21

    MC "Sorry, it’s my first time ever drinking such an expensive wine, so I’m not very experienced with the terminologies."
    Mom "Relax - it’s cute."
    if renpy.loadable("patch.rpy"):
        MC "Uh… Mom? Is that you?"
    else:
        MC "Uh… Linda? Is that you?"
    Mom "What do you mean?"

    scene MLR2_ES3_p22

    MC "(I KNEW it was her!)"
    MC "Your foot… it’s on my…"
    Mom "On your what, Dear?"

    scene MLR2_ES3_p23
    if renpy.loadable("patch.rpy"):
        MC "We’re in public, Mom…"
    else:
        MC "We’re in public, Linda…"
    MC "There’s shit-loads of people! This place is packed out tonight!"
    Mom "Hmm... We better not get caught then. That would be rather embarrassing for you."

    scene MLR2_ES3_p24

    MC "Oh, my God - you’re not seriously going to go through with this, right?"
    Mom "Mmm... I most certainly am, Dear."
    MC "(Fuck! Should I try to stop her?)"

    window hide

    menu:
        "{color=#ff8000}Try to stop Mom from rubbing her feet on your cock.{/color} {color=#00ff00}(Different event.){/color} " if renpy.loadable("patch.rpy"):
            jump MLR2_ES3_blowjob_label_rep

        "{color=#ff8000}Try to stop Linda from rubbing her feet on your cock.{/color} {color=#00ff00}(Different event.){/color} " if not renpy.loadable("patch.rpy"):
            jump MLR2_ES3_blowjob_label_rep




        "{color=#ff8000}Let Mom give you a footjob under the table.{/color} {color=#00ff00}(Different event.){/color}" if renpy.loadable("patch.rpy"):
            jump MLR2_ES3_footjob_label_rep

        "{color=#ff8000}Let Linda give you a footjob under the table.{/color} {color=#00ff00}(Different event.){/color}" if not renpy.loadable("patch.rpy"):
            jump MLR2_ES3_footjob_label_rep

label MLR2_ES3_footjob_label_rep:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)
    scene MLR2_ES3_p24
    MC "(I guess it wouldn’t hurt to let her continue. We just have to be very careful.)"
    $ can_hide_windows = True
    scene black

    $ renpy.sound.play('sfx/slow_zipper.wav', loop=False)
    "*Zzzzzziiiiiipppp*"
    $ renpy.pause(2.15, hard = True)

    scene MLR2_ES3__footjobp1

    MC "(She just undid my zipper with her toes and pulled my boxer shorts down!)"
    if renpy.loadable("patch.rpy"):
        MC "Mom-"
    else:
        MC "Linda-"
    Mom "Shush. The trick is, to avoid reacting. You don’t want to alert any other diners, as to what is going on."

    scene MLR2_ES3__footjobp2

    Mom "Besides - Don’t tell me that you’re not enjoying this?"
    MC "…"
    Mom "I thought so."
    Mom "Now, let me slip my other shoe off, so I can get both feet working on your cock."

    scene MLR2_ES3__footjobp3

    MC "Oooh…"
    scene MLR2_ES3__footjobp3anim
    if renpy.loadable("patch.rpy"):
        Mom "Sounds like my big boy’s enjoying having Mommy’s feet, rubbing over his thick hard cock."
    else:
        Mom "Sounds like my big boy’s enjoying having Linda’s feet, rubbing over his thick hard cock."
    MC "(Fuck, this feels so good…)"

    scene MLR2_ES3__footjobp4

    Mom "What’s wrong? You’re looking a little flustered, Sweetie."
    Mom "Did you drink too much wine?"
    MC "S-Stop teasing me! Someone could- ahh- see us!"

    scene MLR2_ES3__footjobp5

    Mom "You worry too much. You need to learn to relax and enjoy the simple things in life…"
    Mom "...like your mother massaging your cock with her feet, in the middle of a public restaurant."
    MC "Ah… Oohh…"
    MC "(She’s got a twisted definition of “simple things in life.)"

    scene MLR2_ES3__footjobp6

    MC "Mmm!"
    MC "(She’s getting faster!)"
    Mom "You’re acting rather strange - is everything okay, Sweetie?"

    scene MLR2_ES3__footjobp7

    MC "Shit! Someone LITERALLY just walked right by us!"
    MC "If they see us, they could call the police!"
    Mom "Well, you better hurry up and cum, then. Because this isn’t ending until you do."

    scene MLR2_ES3__footjobp8

    MC "Ahhh… Fuck…"
    Mom "Oh, is my big boy close?"
    if renpy.loadable("patch.rpy"):
        Mom "Cum for me. Cum all over your mommy’s feet. "
    else:
        Mom "Cum for me. Cum all over your Linda’s feet. "
    MC "(Dammit, I have to try and suppress my moaning, in public.)"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene MLR2_ES3__footjobp8 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene MLR2_ES3__footjobp8a with dissolve

    MC "Hnnnggg…. Ah….. Ugh…."
    Mom "That’s it! Good boy!"
    MC "Fuck… Ah…. Ohhh…"

    scene MLR2_ES3__footjobp9

    Mom "Wow - so muchh cum! You must have been REALLY horny!"
    MC "Q-Quiet. Here, take my napkin. Clean your feet quickly, before someone sees!"
    MC "(I think that has to be the most dangerous sex I’ve EVER had.)"
    Mom "Finish off your wine, if you want. Then we can head home."
    MC "You’ve barely touched YOUR wine."
    Mom "That’s because I’m driving - Safety first, Dear."
    jump MLR2_ES3_end_label_rep


label MLR2_ES3_blowjob_label_rep:
    $ can_hide_windows = True
    scene MLR2_ES3__blowjobp0
    if renpy.loadable("patch.rpy"):
        MC "Mom, you’ve got to stop! We’re in public!"
    else:
        MC "Linda, you’ve got to stop! We’re in public!"
    Mom "Aww... Why?"
    MC "If a waiter catches us right now, we’ll both be screwed!"
    Mom "(Sigh) If you insist."
    MC "Thank you."
    Mom "At the very least, can I come over and give you a hug?"
    MC "Sure, that’s perfectly fine."

    scene MLR2_ES3__blowjobp1

    Mom "See? This is nice."
    MC "Yeah, it is."
    if renpy.loadable("patch.rpy"):
        MC "Thanks for bringing me out tonight, Mom."
    else:
        MC "Thanks for bringing me out tonight, Linda."

    scene MLR2_ES3__blowjobp2

    Mom "Well, I’d say the pleasure is all mine; but you seem to be enjoying yourself too."
    Mom "Do you like looking at my breasts?"
    MC "What- I wasn’t-"
    Mom "Of course you are!"

    scene MLR2_ES3__blowjobp3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

    Mom "I mean, what other reason could you POSSIBLY have, for being THIS hard?"
    if renpy.loadable("patch.rpy"):
        MC "Mom! Public!"
    else:
        MC "Linda! Public!"
    MC "You can’t just start giving me a handjob in a place like this!"
    Mom "Haha! Who said anything about a handjob?"

    scene MLR2_ES3__blowjobp4

    Mom "(Shlurrrrp!)"
    MC "Ahh!"
    Waiter "Is everything alright, Sir?"
    MC "Y-Yeah, she just -ah- dropped her contact lens!"

    scene MLR2_ES3__blowjobp5

    Waiter "No problem. If you need anything else, give me a shout."
    Mom "(SUCK! SUCK!)"
    scene MLR2_ES3__blowjobp5anim
    MC "Ohh... fuck…"

    scene MLR2_ES3__blowjobp6

    MC "(I can’t believe she’s doing this right now! What the hell has gotten into her?!)"
    Mom "(Shlurrrp)"
    scene MLR2_ES3__blowjobp6anim
    MC "Ohh... fuck! She's speeded up!"
    Mom "(I just can’t hold myself back, around him! I need him to cum in my mouth!)"

    scene MLR2_ES3__blowjobp7

    MC "Mmm…."
    if renpy.loadable("patch.rpy"):
        MC "(Damn! This feels so good! Mom gives phenomenal blowjobs!)"
    else:
        MC "(Damn! This feels so good! Linda gives phenomenal blowjobs!)"
    MC "(There’s so many people around though - I’m lucky we haven’t been spotted yet!)"

    scene MLR2_ES3__blowjobp8

    Mom "(SUCK SUCK SUCK!)"
    scene MLR2_ES3__blowjobp12anim
    MC "Ohhh… Ohhh…"
    Mom "(I can’t wait for [player_name] to spew his hot cum in my wet mouth!)"

    scene MLR2_ES3__blowjobp9
    if renpy.loadable("patch.rpy"):
        MC "Ahh… I’m gonna cum soon, Mom."
    else:
        MC "Ahh… I’m gonna cum soon, Linda."
    Mom "(Lick! Shlurp!)"
    scene MLR2_ES3__blowjobp9anim
    MC "God…"

    scene MLR2_ES3__blowjobp10

    MC "(Pant! Pant!)"
    Mom "(His cock’s beginning to throb between my lips! Time for the grand finale!)"
    MC "(Any seconds now! Yes!)"

    scene MLR2_ES3__blowjobp11

    MC "Huh? (Why did she take it out of her mouth?)"
    Mom "Aaah…"
    if renpy.loadable("patch.rpy"):
        MC "M-Mom? Why did you stop? Is everything-"
    else:
        MC "L-Linda? Why did you stop? Is everything-"

    scene MLR2_ES3__blowjobp12

    Mom "(SHLLURRRRRRRRRPPP!!!)"
    MC "OH God! Ahhh! Ahhhh!"
    MC "Fuck! I’m cumming… Shit! Hnnnng!"
    scene white with dissolve
    $ renpy.pause(0.5, hard = True)
    scene MLR2_ES3__blowjobp12 with dissolve
    $ renpy.pause(0.5, hard = True)
    scene white with dissolve
    $ renpy.pause(0.5, hard = True)
    scene MLR2_ES3__blowjobp12 with dissolve
    Mom "(Gulp! Gulp!)"
    MC "(Holy fuck! She’s swallowing it all as I spray it into her mouth!)"

    scene MLR2_ES3__blowjobp13

    MC "Holy shit… Phew…"
    MC "That was fucking incredible!"
    Mom "I’m glad you enjoyed it, Sweetie."
    MC "Were you not afraid of getting caught?"
    Mom "Honestly - that just makes it even hotter for me."
    jump MLR2_ES3_end_label_rep


label MLR2_ES3_end_label_rep:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene black
    $ renpy.pause(3,hard = True)
    scene MLR2_ES3_p25
    if renpy.loadable("patch.rpy"):
        MC "Thanks again for taking me out for dinner. I had a really good time, Mom."
    else:
        MC "Thanks again for taking me out for dinner. I had a really good time, Linda."
    Mom "Me too, Sweetie. I can’t wait to do it again."
    MC "So, are we going home now or-"

    scene MLR2_ES3_p26

    MC "Mom, what’s wrong? Are you alright?"
    Mom "I- I’m fine…"
    MC "You suddenly looked sad there."

    scene MLR2_ES3_p27

    MC "W-Was it something I said?"
    Mom "No."
    MC "Did- Is this about me not bringing flowers or chocolates? I swear to God, I didn't know if this was supposed to be a date or not."


    scene MLR2_ES3_p28

    Mom "It’s not that."
    if renpy.loadable("patch.rpy"):
        Mom "Your father is at home right now. The date ends as soon as we get home."
    else:
        Mom "Bob is at home right now. The date ends as soon as we get home."
    MC "(So it WAS a date!)"
    MC "Hey, that’s okay."



    MC "We’ll have loads more dates together, in the future."
    MC "And we can hang out together when Dad goes on his business trips. Okay?"
    scene MLR2_ES3_p29
    Mom "Promise?"
    if renpy.loadable("patch.rpy"):
        MC "I promise, Mom."
    else:
        MC "I promise, Linda."

    scene MLR2_ES3_p30

    Mom "Thank you so much, [player_name]. I couldn’t have asked for a kinder boy."
    if renpy.loadable("patch.rpy"):
        Mom "Let’s get home before your father starts to wonder where we both are."
        MC "Okay, Mom. Love you!"
    else:
        Mom "Let’s get home before Bob starts to wonder where we both are."
        MC "Okay, Linda. Love you!"
    Mom "Love you too, Sweetie."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label