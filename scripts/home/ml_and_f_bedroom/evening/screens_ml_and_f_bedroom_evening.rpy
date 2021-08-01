screen parents_bedroom_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_evening1")]

    if ml_bedroom_book_scene == True and ml_points == 1:
        imagebutton:
            xpos 1576
            ypos 551
            focus_mask True
            idle "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1.png"
            hover "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_book_scene_v1_label")]
            hovered Show("displayTextScreen", displayText = __("Book"))
            unhovered Hide("displayTextScreen")

    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/evening/money_b1.png"
            hover "/images/home/ml_and_f_bedroom/evening/money_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_money_label")]
            hovered Show("displayTextScreen", displayText = __("Money"))
            unhovered Hide("displayTextScreen")

screen parents_bedroom_evening_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"

    if ml_bedroom_book_scene == True and ml_points == 1:
        imagebutton:
            xpos 1576
            ypos 551
            focus_mask True
            idle "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1.png"


    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/evening/money_b1.png"

