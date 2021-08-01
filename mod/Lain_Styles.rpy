style mod_home_title is text:
    size 56
    font "mod/Proxima Nova Semibold.otf"
    align (0.5, 0.18)


style modguide_text is text:
    font "mod/OS.ttf"
    size 22
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style mod_toolbar_textbutton is text:
    font "mod/OS.ttf"
    color "#999999"
    selected_color "#fff"
    hover_color "#66c1e0"
    size 26

style mod_column1_textbutton is text:
    font "mod/OS.ttf"
    color "#a4a4a4"
    selected_color "#fff"
    hover_color "#66c1e0"
    size 26
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style mod_column2_header is text:
    font "mod/OS.ttf"
    color "#fff"
    size 26
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style mod_column2_textbutton is text:
    xoffset 15
    font "mod/OS.ttf"
    color "#a4a4a4"
    selected_color "#fff"
    hover_color "#66c1e0"
    size 24
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style mod_settingsCheats_text is text:
    font "mod/OS.ttf"
    color "#fff"
    size 28
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style mod_settingsCheats_button_text is button_text:
    font "mod/OS.ttf"
    color "#a4a4a4"
    selected_idle_color "#fff"
    hover_color "#66c1e0"
    size 28
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style walk_menu_text is text:
    size 26
    font "mod/Roboto-Thin.ttf"
    xalign 0.5

style walk_menu_vbox is vbox:
    spacing 18


init python:
    if preferences.language == "french":
        mod_completed_text = Text(__("Complété !"), align=(0.5, 0.5), size=30, font="mod/AktivGrotesk-Light.otf", color="#fff")
    else:
        mod_completed_text = Text(__("Completed!"), align=(0.5, 0.5), size=30, font="mod/AktivGrotesk-Light.otf", color="#fff")