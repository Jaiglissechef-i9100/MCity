image CR3_AS7a_p1 = "/images/home/caroline_room/day/scenes/CR3_AS7a/1.jpg"
image CR3_AS7a_p2 = "/images/home/caroline_room/day/scenes/CR3_AS7a/2.jpg"
image CR3_AS7a_p3 = "/images/home/caroline_room/day/scenes/CR3_AS7a/3.jpg"


label CR3_AS7a_label:

    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR3_AS7a_p1 with dissolve


    MC "(Caroline seems to rely VERY heavily on that dildo, to keep her lust in check.)"
    MC "(If I can find and steal it, I’ll hopefully leave her feeling extra horny, when she can’t - get herself off.)"
    MC "(If my plan works properly, she’ll come running to me, to try and relieve herself.)"

    scene CR3_AS7a_p2

    MC "Hmm... lets see... I could have sworn, she hid it under her bed."
    MC "Ugh... I should have brought a torch."
    MC "Aha! (I think I’ve got it.)"

    scene CR3_AS7a_p3

    MC "Bingo!"
    MC "(Let’s see what Caroline does, now that she can’t use her fancy vibrator, to cum!)"
    MC "(I’ll hide this in my room, so she doesn’t find it.)"
    scene black
    $ renpy.pause(2,hard=True)
    $ CR3_AS7a_can1 = False
    $ CR3_AS7a_can2 = False
    $ CR3_AS5 = False
    $ CR3_AS7 = False

    $ outfit_box.drop_outfit(C_R3_outfit3_loc)
    $ outfit_box.add_outfit(C_R3_outfit3)

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1