image SR2_NS1_p1 = "images/home/mc_room/night/scenes/SR2_NS1/1.jpg"
image SR2_NS1_p2 = "images/home/mc_room/night/scenes/SR2_NS1/2.jpg"
image SR2_NS1_p3 = "images/home/mc_room/night/scenes/SR2_NS1/3.jpg"
image SR2_NS1_p4 = "images/home/mc_room/night/scenes/SR2_NS1/4.jpg"
image SR2_NS1_p5 = "images/home/mc_room/night/scenes/SR2_NS1/5.jpg"
image SR2_NS1_p6 = "images/home/mc_room/night/scenes/SR2_NS1/6.jpg"
image SR2_NS1_p7a = "images/home/mc_room/night/scenes/SR2_NS1/7a.jpg"
image SR2_NS1_p7b = "images/home/mc_room/night/scenes/SR2_NS1/7b.jpg"
image SR2_NS1_p8 = "images/home/mc_room/night/scenes/SR2_NS1/8.jpg"
image SR2_NS1_p9a = "images/home/mc_room/night/scenes/SR2_NS1/9a.jpg"
image SR2_NS1_p9b = "images/home/mc_room/night/scenes/SR2_NS1/9b.jpg"
image SR2_NS1_p10 = "images/home/mc_room/night/scenes/SR2_NS1/10.jpg"

label SR2_NS1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True

    scene SR2_NS1_p1 with dissolve

    Sara "I hope you didn’t forget that I was coming to visit you tonight."
    MC "Of course not, Sara!"
    Sara "Hehe... I’m just teasing you."
    MC "What’s up?"

    scene SR2_NS1_p2

    Sara "Actually… it’s a little… difficult to talk about."
    MC "Is something wrong?"
    Sara "No! At least… I don’t think so. I hope not."
    if renpy.loadable("patch.rpy"):
        Sara "Can you climb under the sheets with me? I REALLY don’t want Mom or Dad to overhear us."
    else:
        Sara "Can you climb under the sheets with me? I REALLY don’t want Linda or Bob to overhear us."
    MC "Sure, no problem."

    scene SR2_NS1_p3

    MC "What did you want to say?"
    Sara "It’s… I don’t know why it’s so difficult. I KNOW what I want to say, but I can’t make myself say the words."
    Sara "Do you understand what I mean?"

    scene SR2_NS1_p4

    MC "I… I think so?"
    Sara "[player_name], we’ve done… stuff together. Like that time I gave you a blowjob."
    MC "Or that time we played strip videogaming?"
    Sara "That too..."

    scene SR2_NS1_p5

    Sara "And then you told me that you loved me…"
    Sara "I need to know… Am I your girlfriend now?"
    MC "(It sounds like she wants me to commit myself to her. If I’m fooling around with any other women - this could POTENTIALLY make things awkward…)"

    menu:
        "You’ll become my girlfriend after we have sex.":
            scene SR2_NS1_p6

            MC "I’ll tell you what, Sara. How about we commemorate the day you become my girlfriend with something special?"
            Sara "Wh-What do you mean?"
            MC "I was thinking that you become my girlfriend the first time we have sex."

            scene SR2_NS1_p9a

            Sara "S-Sex?!"
            MC "(She looks pretty shocked by my suggestion.)"
            MC "Are you alright, Sara?"

            scene SR2_NS1_p9b

            Sara "Y-Yeah, I’m fine. You just took me by surprise."
            MC "Sorry, my bad."
            Sara "No, it’s not your fault. I just… I don’t think I’m ready to actually have sex yet."
            MC "Honestly, don’t worry about it, Sara. We can take our time."

            scene SR2_NS1_p10

            Sara "Really?! Thank you so much, [player_name]."
            Sara "I DO want to do it with you… someday. I just need a little more time right now."
            Sara "Maybe we could do some other stuff together, in the meantime?"
            MC "Sure. Whatever you’re comfortable with, Sara."
            Sara "Thanks, [player_name]. You’re the best."
            jump SR2_NS1_continue
        "Can I answer later? Everything is happening very fast right now.":

            scene SR2_NS1_p6

            MC "Can I give you an answer later? It feels like everything is happening really fast right now."
            Sara "Oh…"
            MC "I’m not saying 'no'. I just need some time to think about everything."

            scene SR2_NS1_p8

            Sara "I was kinda hoping you’d say ‘yes’."
            MC "Someday, Sara. Just… not right now. I need more time."
            Sara "Hmmph…."

            scene SR2_NS1_p7a

            MC "Aww, c’mon Sara. Don’t be like that!"
            MC "How would you feel, if I started pressuring you to have sex before you were ready? You’d feel stressed, right?"

            scene SR2_NS1_p9b

            Sara "Huh… I guess so."
            MC "Well, calling you my girlfriend before I’m ready, is kinda the same thing. I’d love to call you my other half, but I’m only gonna do it when I’m feeling truly ready."
            MC "Do you understand?"
            Sara "Yeah, I guess so. I’m sorry, [player_name]."

            scene SR2_NS1_p6

            MC "You don’t need to apologise, Sara. I really DO love you."
            Sara "Hehe... I know."

            scene SR2_NS1_p7b

            MC "*Mwah*"
            Sara "(Oh, my God! I just melt, every time he kisses me.)"
            jump SR2_NS1_continue
        "Yes, but… we’re still not doing what couples do.":

            scene SR2_NS1_p10

            MC "Of course, Sara. I’d love to call you my girlfriend."
            Sara "Really?!"
            MC "There’s just one little issue… We’re not actually doing what couples do."

            scene SR2_NS1_p9a

            Sara "Wh-What’s wrong? I don’t understand."
            MC "Sara, we still haven’t had sex together. Sure, we’ve done some little things here and there, but we haven’t even come close to actually fucking each other."

            scene SR2_NS1_p9b

            Sara "Oh..."
            Sara "I don’t… I don’t think I’m ready to do… that kinda stuff yet."

            scene SR2_NS1_p7a

            MC "Don’t worry, Sara. Take your time."
            MC "We can discuss this again, whenever some more time has past. I don’t want you being pressured into something you’re not entirely comfortable with."
            MC "Don’t forget, that I really DO love you."

            scene SR2_NS1_p7b

            MC "*Mwah*"
            jump SR2_NS1_continue

label SR2_NS1_continue:
    scene SR2_NS1_p4

    Sara "Well… maybe we could try some other things, to help us build up towards sex?"
    MC "Sounds good to me. What are you thinking?"
    Sara "I honestly don’t know. Sorry, I’m not experienced at this kind of thing, at all. Do you think you could give me some ideas?"

    scene SR2_NS1_p6

    MC "That’s okay. Let me think… Hmm…"
    MC "How about I get you a vibrator? You can use it to practice masturbating and gain some confidence with your own body."
    Sara "Umm… Sorry, I’m a little nervous."
    MC "That’s okay. I’ll tell you what - I’ll go and buy you one. You can keep it in your room and try it out, yourself. I won’t pressure you to use it - you’ll only try it out if you want to."

    scene SR2_NS1_p10

    Sara "Yeah… That doesn’t sound too bad!"
    Sara "After you buy it, come and let me know, in school. Let me know and I’ll sneak into your bedroom again to collect it."
    MC "No problem, Sara. I’ll let you know."
    Sara "Okay, I better get back to bed now. I’ll see you later, [player_name]. Goodnight!"
    MC "Sweet dreams, Sara."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_AS2 = False
    $ SR2_NS1 = False
    $ SR2_AS3 = True
    $ S_N_inbed = True
    jump sleeping_after_scene
