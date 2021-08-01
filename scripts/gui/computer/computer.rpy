image main_deskop = "images/game_gui/pc/deskop.jpg"

image mc_playing_morning = "images/home/mc_room/morning/playing_computer/PlayingMorning.png"
image mc_playing_day = "images/home/mc_room/morning/playing_computer/PlayingMorning.png"
image mc_playing_evening = "images/home/mc_room/morning/playing_computer/PlayingEvening.png"
image mc_playing_night = "images/home/mc_room/morning/playing_computer/PlayingNight.png"

label computer_menu:
    hide screen map_button
    hide screen displayTextScreen
    if day_time == 1:
        show screen mc_room_morning_notclickable
    if day_time == 2:
        show screen mc_room_day_notclickable
    if day_time == 3:
        show screen mc_room_evening_notclickable
    if day_time == 4:
        show screen mc_room_night_notclickable

    menu:
        "Use Computer.":
            hide screen mc_room_night_notclickable
            hide screen mc_room_evening_notclickable
            hide screen mc_room_day_notclickable
            hide screen mc_room_morning_notclickable
            jump pc_icon_label
        "Play Computer Games.":
            $ in_bed_menu  = False
            $ renpy.hide("mc_sleep_morning", layer="screens")
            $ renpy.hide("mc_sleep_day", layer="screens")
            $ renpy.hide("mc_sleep_evening", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            hide screen new_message_incoming1
            if day_time == 1:
                show screen mc_room_morning_notclickable
                $ renpy.show("mc_playing_morning", layer="screens")
            if day_time == 2:
                show screen mc_room_day_notclickable
                $ renpy.show("mc_playing_day", layer="screens")

            if day_time == 3:
                show screen mc_room_evening_notclickable
                $ renpy.show("mc_playing_evening", layer="screens")
            if day_time == 4:
                show screen mc_room_night_notclickable
                MC "I'm too tired."
                jump mc_room_morning1
            $ renpy.sound.play("sfx/computer_playing.mp3")
            $ renpy.pause(2, hard = True)
            hide screen mc_room_night_notclickable
            hide screen mc_room_evening_notclickable
            hide screen mc_room_day_notclickable
            hide screen mc_room_morning_notclickable

            $ renpy.hide("mc_playing_morning", layer="screens")
            $ renpy.hide("mc_playing_day", layer="screens")
            $ renpy.hide("mc_playing_evening", layer="screens")
            $ renpy.hide("mc_playing_night", layer="screens")
            scene black
            $ day_time +=1
            $ renpy.pause(2, hard = True)
            $ renpy.music.stop(channel="sound", fadeout=1)
            if day_time == 1:
                scene mc_room_morning
                show screen mc_room_morning_notclickable
                $ renpy.show("mc_playing_morning", layer="screens")
            if day_time == 2:
                scene mc_room_day
                show screen mc_room_day_notclickable
                $ renpy.show("mc_playing_day", layer="screens")

            if day_time == 3:
                scene mc_room_evening
                show screen mc_room_evening_notclickable
                $ renpy.show("mc_playing_evening", layer="screens")
            if day_time == 4:
                scene mc_room_night
                show screen mc_room_night_notclickable
                $ renpy.show("mc_playing_night", layer="screens")
            MC "Okay. That’s enough."
            $ renpy.hide("mc_playing_morning", layer="screens")
            $ renpy.hide("mc_playing_day", layer="screens")
            $ renpy.hide("mc_playing_evening", layer="screens")
            $ renpy.hide("mc_playing_night", layer="screens")
            $ renpy.block_rollback()
            jump mc_room_morning1
        "Back.":
            jump mc_room_morning1




label pc_icon_label:
    $ can_hide_windows = False
    if music_continue == False:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ music_continue = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene main_deskop
    call screen main_deskop_pcv1

label name_change:
    show screen main_deskop_pcv1
    $ clickable = False
    $ player_name_old = player_name
    $ player_name = renpy.input("Enter your new name.")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = player_name_old
    $ clickable = True
    hide screen main_deskop_pcv1
    jump pc_icon_label
screen main_deskop_pcv1:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 20
        ypos 37
        focus_mask True
        idle "images/game_gui/pc/internet.png"
        hover "images/game_gui/pc/Internet_Hover.png"
        hovered Show("displayTextScreen", displayText = "Internet")
        if clickable == True:
            action [Play ("sound", "sfx/mouse_click.mp3"),Jump("internet_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 20
        ypos 185
        focus_mask True
        idle "images/game_gui/pc/CD.png"
        hover "images/game_gui/pc/CD_Hover.png"
        hovered Show("displayTextScreen", displayText = "CD")
        if clickable == True:
            action [Play ("sound", "sfx/mouse_click.mp3"),Jump("CD_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 20
        ypos 330
        focus_mask True
        idle "images/game_gui/pc/Gallery.png"
        hover "images/game_gui/pc/Gallery_Hover.png"
        hovered Show("displayTextScreen", displayText = "Gallery")
        if clickable == True:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/mouse_click.mp3"),Jump("gallery_label")]
            unhovered Hide("displayTextScreen")

    if live_camera_instaled == True:
        imagebutton:
            xpos 20
            ypos 472
            focus_mask True
            idle "images/game_gui/pc/LiveCamera.png"
            hover "images/game_gui/pc/LiveCamera_Hover.png"
            hovered Show("displayTextScreen", displayText = "Live Camera")
            if clickable == True:
                action [Play ("sound", "sfx/mouse_click.mp3"),Jump("live_camera_label")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1776
        ypos 883
        focus_mask True
        idle "images/game_gui/pc/TurnOFF.png"
        hover "images/game_gui/pc/TurnOFF_Hover.png"
        hovered Show("displayTextScreen", displayText = "Turn Off")
        if clickable == True:
            action [Play ("sound", "sfx/mouse_click.mp3"),Jump("turn_off_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1770
        ypos 37
        focus_mask True
        idle Transform("images/RPS_minigame/PCIcon Normal.png", zoom=.89)
        hover Transform("images/RPS_minigame/PCIcon Hover.png", zoom=.89)
        hovered Show("displayTextScreen", displayText = "Rock Paper Scissors")
        if clickable == True:
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("main_deskop_pcv1"),Hide("displayTextScreen"),Jump("rps_money_select_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1770
        ypos 165
        focus_mask True
        idle Transform("images/Memoriax/MemoriaxNormal.png", zoom=.89)
        hover Transform("images/Memoriax/MemoriaxHover.png", zoom=.89)
        hovered Show("displayTextScreen", displayText = "Memoriax")
        if clickable == True:
            action [Play ("sound", "sfx/mouse_click.mp3"),Hide("main_deskop_pcv1"),Hide("displayTextScreen"),SetVariable("music_continue", False),Jump("memoriax_label")]
            unhovered Hide("displayTextScreen")

    textbutton (player_name):
        if clickable == True:
            action Jump("name_change")
        xpos 90 ypos 1027

    imagebutton:
        xpos 20
        ypos 820
        focus_mask True
        idle "images/game_gui/pc/Stats.png"
        hover "images/game_gui/pc/Stats_hover.png"
        hovered Show("displayTextScreen", displayText = "Statistics")
        if clickable == True:
            action [Hide("displayTextScreen"),Play ("sound", "sfx/mouse_click.mp3"),Jump("G_Stats_label")]
            unhovered Hide("displayTextScreen")