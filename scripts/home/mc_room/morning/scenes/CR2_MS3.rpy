image CR2_MS3_p1 = "images/home/mc_room/morning/scenes/CR2_MS3/1.jpg"
image CR2_MS3_p2 = "images/home/mc_room/morning/scenes/CR2_MS3/2.jpg"
image CR2_MS3_p3 = "images/home/mc_room/morning/scenes/CR2_MS3/3.jpg"
image CR2_MS3_p4 = "images/home/mc_room/morning/scenes/CR2_MS3/4.jpg"
image CR2_MS3_p5 = "images/home/mc_room/morning/scenes/CR2_MS3/5.jpg"
image CR2_MS3_p6 = "images/home/mc_room/morning/scenes/CR2_MS3/6.jpg"
image CR2_MS3_p7 = "images/home/mc_room/morning/scenes/CR2_MS3/7.jpg"
image CR2_MS3_p8 = "images/home/mc_room/morning/scenes/CR2_MS3/8.jpg"

label CR2_MS3_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_MS3_p1 with dissolve

    $ can_hide_windows = True
    MC "What’s up, Caroline? You’re looking a little worried. Is there something stressing you out?"
    Caroline "No - I mean, yes. There is."
    MC "Do you want to take a seat and we’ll talk about it?"

    scene CR2_MS3_p2

    Caroline "No, I… Do you remember that offer you made me? To give me money for my business."
    MC "Yeah."
    if persistent.incest_patch == True:
        Caroline "Does that offer still… stand? I really need two hundred, to pay rent to Mom."
    else:
        Caroline "Does that offer still… stand? I really need two hundred, to pay rent to Linda."

    scene CR2_MS3_p1

    Caroline "I’m sure she wouldn’t mind me missing one month’s rent… but I don’t want her to know that I’m failing in business."
    window hide
    menu:
        "{color=#00ff00}Of course! I have two hundred here.{/color}" if inventory.money >= 200:
            scene CR2_MS3_p3

            if persistent.incest_patch == True:
                MC "Of course, Caroline! I have two hundred here. And don’t worry, I won’t say a word to Mom about this."
            else:
                MC "Of course, Caroline! I have two hundred here. And don’t worry, I won’t say a word to Linda about this."
            Caroline "Seriously? Y-You don’t have to do this, you know."

            MC "Relax. I’m happy to help."

            scene CR2_MS3_p4

            Caroline "Thank you so much. You have no idea, how much this means to me right now."
            Caroline "I’ll be back on my feet soon. I just need a little help, to get my finances back on track."
            Caroline "You’re a real life saver, [player_name]."

            scene CR2_MS3_p5

            MC "It’s nothing! You’d do the same for me."
            Caroline "Thanks again! I’ll pay you back someday. I promise."
            $ inventory.drop_money(200)
            $ CR2_MS3 = False
            $ can_CR2_MS3a = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1

        "Of course, I have two hundred here. (disabled)" if inventory.money < 200:
            $ can_hide_windows = False
            jump mc_room_morning1
        "Sorry, Caroline. I’m really short on money too right now.":

            scene CR2_MS3_p2

            MC "I’m so sorry, Caroline. I don’t have two hundred on me right now."
            Caroline "Oh! Right… I’m so so sorry that I brought it up."
            Caroline "I… I have to go now."
            $ CR2_MS3 = False
            $ can_CR2_MS2 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
