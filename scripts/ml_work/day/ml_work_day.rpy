label ml_work_day1:
    $ can_hide_windows = False
    if day_time == 2:
        hide screen displayTextScreen
        scene ml_work_day
        $ can_map = True
        hide screen map
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        call screen ml_work_day
    else:

        show screen map
        show screen shop_closed_screen
        MC "It’s only open in the afternoon."
        jump map_label

screen shop_closed_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("shop_closed_screen"),Jump("map_label")]
