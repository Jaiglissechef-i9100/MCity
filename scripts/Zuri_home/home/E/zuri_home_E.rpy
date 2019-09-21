image Z_ES1_bg = "images/Zuri_home/outside/E/scenes/Z_ES1/bg.jpg"

default zuri_inhome = True

label zuri_home_E_label:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene Z_ES1_bg
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen zuri_home_E_scr

label zuri_inhome_E_label:
    $ can_hide_windows = False
    $ clickable = False
    show screen zuri_home_E_scr
    Zuri "I'm busy now, [player_name]"
    $ clickable = True
    jump zuri_home_E_label

label zuri_home_E_label2:
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen displayTextScreen
    scene Z_ES1_bg
    show screen zuri_home_E_scr
    $ can_hide_windows = False
    $ clickable = False
    MC "Should I sit on the couch as Zuri wants or should I try speak to her?"
    $ clickable = True
    jump zuri_home_E_label
