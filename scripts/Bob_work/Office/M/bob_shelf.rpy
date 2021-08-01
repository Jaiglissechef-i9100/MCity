image bob_shelf_p1 = "/images/Bob_work/office/M/shelf/Shelf1.jpg"
image bob_shelf_p2 = "/images/Bob_work/office/M/shelf/Shelf2.jpg"
image bob_shelf_p3 = "/images/Bob_work/office/M/shelf/Shelf3.jpg"

image bob_sec_p1 = "/images/Bob_work/office/M/scenes/sec/1.jpg"
image bob_sec_p2 = "/images/Bob_work/office/M/scenes/sec/2.jpg"
image bob_sec_p3 = "/images/Bob_work/office/M/scenes/sec/3.jpg"
image bob_sec_p4 = "/images/Bob_work/office/M/scenes/sec/4.jpg"
image bob_sec_p5 = "/images/Bob_work/office/M/scenes/sec/5.jpg"

default bob_secretroom_after_first_visit = False
default shelf_putbook = False
label bob_shelf_label:
    scene bob_shelf_p1
    call screen bob_shelf_scr

screen bob_shelf_scr:
    key "hide_windows" action NullAction()
    if bob_carbook.selected:
        imagebutton:
            xpos 948
            ypos 807
            focus_mask True
            idle "images/Bob_work/office/M/shelf/B1.png"
            hover "images/Bob_work/office/M/shelf/B1_hover.png"
            if clickable == True and day_time ==2:
                action [Play ("sound", "sfx/door_squeak.mp3"),Hide("displayTextScreen"),Jump("bob_shelfopen_label")]
            if clickable == True and day_time ==1:
                action [Hide("displayTextScreen"),Jump("bob_shelfopen_label")]
                unhovered Hide("displayTextScreen")

    if shelf_putbook == True:
        imagebutton:
            xpos 948
            ypos 807
            focus_mask True
            idle "images/Bob_work/office/M/shelf/B1_hover.png"
            hover "images/Bob_work/office/M/shelf/B1_hover.png"

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]

label bob_shelfopen_label:
    if day_time==1:
        $ clickable = False
        show screen bob_shelf_scr
        MC "I can't do it when someone is in the room."
        $ clickable = True
        jump bob_shelf_label

    if day_time==2:
        scene bob_shelf_p1
        $ shelf_putbook = True
        $ inventory.drop(bob_carbook)
        $ bob_carbook.selected = False
        show screen bob_shelf_scr
        $ renpy.pause(0.2,hard= True)
        hide screen bob_shelf_scr
        scene bob_shelf_p2
        $ renpy.pause()
        if bob_secretroom_after_first_visit == False:
            jump bob_secret_room_scene
        else:
            jump bob_secret_room_label

label bob_secret_room_label:
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    scene bob_shelf_p3
    call screen bob_secret_room_scr

label bob_secret_room_leave_label:
    $ inventory.add(bob_carbook)
    $ shelf_putbook = False
    jump bob_office_M1

screen bob_secret_room_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_secret_room_leave_label")]

label bob_secret_room_scene:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    MC "Huh?!"
    MC "(Is this a secret passageway?)"
    if persistent.incest_patch == True:
        MC "(Why the hell would Dad need a hidden room?)"
    else:
        MC "(Why the hell would Bob need a hidden room?)"
    MC "(Maybe he keeps some of his money in here.)"

    scene bob_sec_p1 with dissolve

    MC "Ahhhh!"
    MC "Jesus Christ! No!"

    scene bob_sec_p2

    MC "Its… It’s… He’s naked!"
    MC "Eww! That’s revolting!"

    scene bob_sec_p3

    MC "(He’s getting whipped and treated like shit…)"
    MC "(Is someone blackmailing him?)"
    MC "(No… that doesn’t make sense. He wouldn’t keep blackmail evidence in his own office.)"

    scene bob_sec_p4

    MC "(He must be into this sorta thing.)"
    if persistent.incest_patch == True:
        MC "(It all makes sense now! The way Mom treats him so badly…)"
    else:
        MC "(It all makes sense now! The way Linda treats him so badly…)"
    MC "(That explains why he hasn’t left her yet! He’s getting off on being treated like crap.)"

    scene bob_sec_p5

    MC "(Some things should remain private. I’m just going to forget about what I saw in here today.)"
    if persistent.incest_patch == True:
        MC "(This isn’t any of my business. I wouldn’t want Dad snooping into MY sex life.)"
    else:
        MC "(This isn’t any of my business. I wouldn’t want Bob snooping into my sex life.)"
    MC "(So I shouldn’t be snooping into his either.)"
    $ can_hide_windows = False
    $ bob_secretroom_after_first_visit = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump bob_secret_room_label

