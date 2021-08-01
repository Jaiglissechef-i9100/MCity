image caroline_room_morning_scene1_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/1.jpg"
image caroline_room_morning_scene1_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/2.jpg"
image caroline_room_morning_scene1_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/3.jpg"
image caroline_room_morning_scene1_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/4.jpg"
image caroline_room_morning_scene1_p5 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/5.jpg"
image caroline_room_morning_scene1_p6 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/6.jpg"

label caroline_room_morning_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_can_room_morning_scenes == False:
        show screen caroline_room_morning_not_clickable
        MC "I've already talked to her."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_room_morning_scene1_p1 with dissolve
    $ can_hide_windows = True
    if persistent.incest_patch == True:
        MC "(Caroline’s always been a caring sister.)"
    else:
        MC "(Caroline’s always been a caring friend.)"
    MC "(In fact, one of my earliest memories was when I was getting bullied in school. I must have been six or seven years old.)"
    MC "(A duo of pricks named Tom and Samson had decided to steal my lunch money - just a couple of dollars; but I refused to give it up.)"
    MC "(I remember the agony of getting punched in the stomach, and the cruel sound of their laughter.)"
    MC "(Caroline was four years older than me, but that didn’t stop her from beating the bullies down with her bare fists.)"
    MC "(For her trouble, she got two sets of bruised knuckles and a three week suspension.)"
    MC "(Tom and Samson got three weeks off school too. However, their “break” was spent in the hospital.)"

    scene caroline_room_morning_scene1_p2 at pandown2
    $ renpy.pause(4)
    MC "Caroline, I-"
    MC "(Holy shit! Look at that ass! Talk about a bubble butt!)"
    MC "S-Sorry! I didn’t know you were changing! I should have knocked!"

    scene caroline_room_morning_scene1_p3
    Caroline "Hiiiii, [player_name]!"
    Caroline "Don’t sweat it - you’re my [player_name]. It’s not like you’re one of those, creepy guys from college, who’s just trying to get in my pants."
    MC "Uhh, yeah…"
    MC "(I thought her ass was good, but her breasts might even be better!)"
    Caroline "So, what’s up?"
    MC "Nothing much - just came by to say hello."

    scene caroline_room_morning_scene1_p4
    Caroline "Oh! Before I forget - what happened in school the other day?"
    if persistent.incest_patch == True:
        Caroline "I’ve only picked up fragments of the story from Sara and Mom?"
    else:
        Caroline "I’ve only picked up fragments of the story from Sara and Linda?"
    menu:
        "Tell her the full truth.":
            MC "Eh… It wasn’t good. I asked out Mrs. Celia, and got rejected."
            Caroline "Ouch, that sounds rough. I know how tough a broken heart can feel."
            MC "Oh! It’s not the broken heart that’s the bad part - she humiliated me in the middle of a busy corridor."
            Caroline "Oh God… [player_name]... I’m so sorry."
            jump caroline_room_morning_scene1_after_menu
        "Play it cool.":
            MC "Relax - it was nothing."
            Caroline "Are you sure? I heard something about you getting humiliated in public?"
            MC "Really! It wasn’t a big deal. I asked Mrs. Celia out, but nothing came of it."
            Caroline "Hmm… A lot of men tend to withold their feelings, rather than talking about their problems."
            Caroline "Make sure you take care of yourself - and if you do ever want to talk, you know my door is always open."
            jump caroline_room_morning_scene1_after_menu
        "I’d rather not talk about it.":
            MC "Yeah… I’d rather not talk about this."
            Caroline "Oh! I’m sorry!"
            MC "No, it’s not your fault. You don’t need to apologise."
            Caroline "Okay, just promise to take care of yourself? I heard something about Mrs. Celia and you in a corridor, but I didn’t get the full details."
            MC "I… Sorry, I’d rather not think about it."
            Caroline "That’s okay. If you ever change your mind, you know I’m always here to chat."
            MC "Thanks, Caroline."
            jump caroline_room_morning_scene1_after_menu

label caroline_room_morning_scene1_after_menu:
    scene caroline_room_morning_scene1_p5
    Caroline "Before you go, I want you to promise me something?"
    MC "Yes?"
    Caroline "Promise you’ll come to me if you’re ever feeling stressed or down about this, won’t you?"
    MC "I’m gonna be fine."

    scene caroline_room_morning_scene1_p6
    Caroline "I didn’t ask if you were going to be fine."
    Caroline "I asked you to promise me that you’ll come to me if you are feeling down."
    MC "Fine… I promise."
    Caroline "Thank you."

    scene caroline_room_morning_scene1_p3
    Caroline "Catch you later, [player_name]. I need to finish getting my makeup on."
    MC "See ya, Caroline."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 2
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump caroline_room_morning1

