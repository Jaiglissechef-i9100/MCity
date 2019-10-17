default C_end_content = False
default S_end_content = False
default ML_end_content = False
default Li_end_content = False
default Ce_end_content = False
screen C_end_content_scr:
    key "game_menu" action NullAction()
    modal True
    zorder 110
    add "images/game_gui//End_content.png"
    add "images/game_gui/Phone/Relations/Caroline.png" xpos 530 ypos 200

    imagebutton:
        xpos 1340
        ypos 239
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        if Caroline_points == 3:
            action [SetVariable("C_SMS5",False), SetVariable("C_end_content",False), Hide ("C_end_content_scr")]
        else:
            action [SetVariable("C_end_content",False), Hide ("C_end_content_scr")]
    timer 2.26 action [Hide ("new_message_incoming1_NC"),Hide("new_message_incoming1")]

screen Ce_end_content_scr:
    key "game_menu" action NullAction()
    modal True
    zorder 110
    add "images/game_gui//End_content.png"
    add "images/game_gui/Phone/Relations/Celia.png" xpos 530 ypos 200

    imagebutton:
        xpos 1340
        ypos 239
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [SetVariable("Ce_sms3",False), SetVariable("Ce_end_content",False), Hide ("Ce_end_content_scr")]
    timer 2.26 action [Hide ("new_message_incoming1_NC"),Hide("new_message_incoming1")]

screen S_end_content_scr:
    key "game_menu" action NullAction()
    modal True
    zorder 110
    add "images/game_gui//End_content.png"
    add "images/game_gui/Phone/Relations/Sara.png" xpos 530 ypos 200

    imagebutton:
        xpos 1340
        ypos 239
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [SetVariable("sms7_sara",False), SetVariable("S_end_content",False), Hide ("S_end_content_scr")]
    timer 2.26 action [Hide ("new_message_incoming1_NC"),Hide("new_message_incoming1")]

screen ML_end_content_scr:
    key "game_menu" action NullAction()
    modal True
    zorder 110
    add "images/game_gui//End_content.png"
    add "images/game_gui/Phone/Relations/ML.png" xpos 530 ypos 200

    imagebutton:
        xpos 1340
        ypos 239
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [SetVariable("ML_end_content",False), Hide ("ML_end_content_scr")]


screen Li_end_content_scr:
    key "game_menu" action NullAction()
    modal True
    zorder 110
    add "images/game_gui//End_content.png"
    add "images/game_gui/Phone/Relations/Liza.png" xpos 530 ypos 200

    imagebutton:
        xpos 1340
        ypos 239
        idle "images/cosplay_minigame/R3/Outfit_Close.png"
        hover "images/cosplay_minigame/R3/Outfit_Close_hover.png"
        action [SetVariable("Li_end_content",False), Hide ("Li_end_content_scr")]