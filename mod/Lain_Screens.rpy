define modversion = "0.71b"

define m_main_girls = [("Linda", "linda_mod_list"), ("Caroline", "caroline_mod_list"), ("Sara", "sara_mod_list"), ("Celia", "celia_mod_list"), ("Liza & Yazmin", "lizaYazmin_mod_list"), ("Zuri & Suri", "zuriSuri_mod_list"), ("Sidra & Isla", "sidraIsla_mod_list")]
define m_side_girls = [("Cindy", "cindy_mod_list"), ("Delilah", "delilah_mod_list"), ("Judy", "judy_mod_list"), ("Lily", "lily_mod_list"), ("Macy", "macy_mod_list"), (" ", "fillerdivider_mod_list"), ("Bath dream scenes", "dreams_mod_list"), ("Night scenes", "night_mod_list"), ("Spy cam scenes", "spycam_mod_list")]

define m_other_scenes = [("Bath dream scenes", "dreams_mod_list"), ("Night scenes", "night_mod_list"), ("Spy cam scenes", "spycam_mod_list")]

define linda_mod_list = [("Main story", "mod_linda_story"), ("Night scenes", "mod_linda_nightscenes")]
define caroline_mod_list = [("Main story", "mod_caroline_story"), ("Night scenes", "mod_caroline_nightscenes")]
define sara_mod_list = [("Main story", "mod_sara_story"), ("Night scenes", "mod_sara_nightscenes")]
define celia_mod_list = [("Main story", "mod_celia_story"), ("Night scenes", "mod_celia_nightscenes")]
define lizaYazmin_mod_list = [("Main story", "mod_lizaYazmin_story"), ("Night scenes", "mod_lizaYazmin_nightscenes")]
define zuriSuri_mod_list = [("Main story", "mod_zuriSuri_story")]
define sidraIsla_mod_list = [("Main story", "mod_sidraIsla_story"), ("Night scenes", "mod_sidraIsla_nightscenes")]

define cindy_mod_list = [("Main story", "mod_cindy_story")]
define delilah_mod_list = [("Main story", "mod_delilah_story")]
define judy_mod_list = [("Main story", "mod_judy_story")]
define lily_mod_list = [("Main story", "mod_lily_story")]
define macy_mod_list = [("Main story", "mod_macy_story")]

define dreams_mod_list = [("Bath dream scenes", "mod_bathdreamscenes")]

define night_mod_list = [("Linda", "mod_linda_nightscenes"), ("Caroline", "mod_caroline_nightscenes"), ("Sara", "mod_sara_nightscenes"), ("Celia", "mod_celia_nightscenes"), ("Liza & Yazmin", "mod_lizaYazmin_nightscenes"), ("Sidra & Isla", "mod_sidraIsla_nightscenes")]
define spycam_mod_list = [("Replay spy cam scenes", "mod_replayspycamscenes")]
define fillerdivider_mod_list = [(" ", "mod_notimplemented")]

screen modmenu():

    default m_current_tab = None
    default m_column2 = None
    default m_column2_name = ""

    zorder 111

    drag:
        drag_name "modmenu"
        align (0.5, 0.5)
        drag_handle (0, 0, 1.0, 53)

        has fixed:
            xysize (1102, 756)
            align (0.5, 0.5)

        if mod_is_modal:
            button xysize (1102, 703) yalign 1.0 action NullAction()

        if m_current_tab == "home":
            add "mod/images/modmenu_home.png"
        elif m_current_tab == "settings" or m_current_tab == "cheats":
            add "mod/images/modmenu_empty.png"
        else:
            add "mod/images/modmenu.png"
        textbutton "X" action Hide("modmenu") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6
        text "Game: [config.version]   Mod: [modversion]" size 18 align (0.99, 0.99)

        hbox:
            align (0.015, 0.007)
            anchor (0.0, 0.0)
            spacing 70
            textbutton "Home" selected m_current_tab == None text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", None), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            textbutton "Main Girls" selected m_current_tab == m_main_girls text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", m_main_girls), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            textbutton "Side Girls" selected m_current_tab == m_side_girls text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", m_side_girls), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]

            textbutton "Settings" selected m_current_tab == "settings" text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", "settings"), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            textbutton "Cheats" selected m_current_tab == "cheats" text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", "cheats"), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]


        if m_current_tab is None:
            text "Character Walkthroughs" style "mod_home_title"
            vbox pos (90, 265):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_linda_story")
                    if ml_points >= 4:
                        idle Fixed(Transform("home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/15.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/15.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/15.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Linda"
            vbox pos (335, 265):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_caroline_story")
                    if Caroline_points >= 5:
                        idle Fixed(Transform("home/caroline_room/morning/scenes/CR4_MS1/9.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("home/caroline_room/morning/scenes/CR4_MS1/9.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("home/caroline_room/morning/scenes/CR4_MS1/9.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Caroline"
            vbox pos (580, 265):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_sara_story")
                    if SR3_v71_end:
                        idle Fixed(Transform("intro/10.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("intro/10.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("intro/10.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Sara"
            vbox pos (825, 265):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_celia_story")
                    if Celia_points >= 3:
                        idle Fixed(Transform("CeR2/NS2/Talking/46.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("CeR2/NS2/Talking/46.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("CeR2/NS2/Talking/46.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Celia"

            vbox pos (90, 495):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_lizaYazmin_story")
                    if Li_points >= 2:
                        idle Fixed(Transform("a_home/Inside/Living/M/Scenes/LiR1_MAS1a/1.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("a_home/Inside/Living/M/Scenes/LiR1_MAS1a/1.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("a_home/Inside/Living/M/Scenes/LiR1_MAS1a/1.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Liza & Yazmin"
            vbox pos (335, 495):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_zuriSuri_story")
                    if Z_points >= 2:
                        idle Fixed(Transform("Zuri_home/home/E/scenes/Zv2_ES2/1.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("Zuri_home/home/E/scenes/Zv2_ES2/1.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("Zuri_home/home/E/scenes/Zv2_ES2/1.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                text "Zuri & Suri"
            vbox pos (580, 495):
                style_prefix "walk_menu"
                imagebutton:
                    action Show("mod_sidraIsla_story")
                    if Ne_MS3:
                        idle Fixed(Transform("Ne_1/ES2/26.jpg", zoom=0.1), Transform("mod/images/black.png", zoom=0.1), mod_completed_text, maximum=(192, 108))
                    else:
                        idle Transform("Ne_1/ES2/26.jpg", zoom=0.1)
                        hover Transform(im.MatrixColor("Ne_1/ES2/26.jpg", im.matrix.brightness(0.175)), zoom=0.1)
                if Ne_fence:
                    text "Sidra & Isla"
                else:
                    text "Neighbors"



        elif m_current_tab == "settings":
            text "Settings" style "mod_home_title"

            hbox:
                style_prefix "mod_settingsCheats"
                align (0.5, 0.55)
                spacing 80
                vbox:
                    spacing 24
                    text "Skip game startup splash screens:"
                    text "Increase game fps (enable if good PC):"
                    text "Allow clicks behind main mod screen:"

                    if mod_is_winter:
                        text "Use winter backgrounds (requires restart):"

                vbox:
                    spacing 9
                    if persistent.mod_skip_splashscreen:
                        textbutton "Enabled" action SetVariable("persistent.mod_skip_splashscreen", False) selected persistent.mod_skip_splashscreen
                    else:
                        textbutton "Disabled" action SetVariable("persistent.mod_skip_splashscreen", True) selected persistent.mod_skip_splashscreen

                    if not _preferences.gl_powersave:
                        textbutton "Enabled" action Preference("gl powersave", True) selected not _preferences.gl_powersave
                    else:
                        textbutton "Disabled" action Preference("gl powersave", False) selected not _preferences.gl_powersave

                    if not mod_is_modal:
                        textbutton "Enabled" action SetVariable("mod_is_modal", True) selected not mod_is_modal
                    else:
                        textbutton "Disabled" action SetVariable("mod_is_modal", False) selected not mod_is_modal

                    if mod_is_winter:
                        if persistent.mod_winter_bgs:
                            textbutton "Enabled" action SetVariable("persistent.mod_winter_bgs", False) selected persistent.mod_winter_bgs
                        else:
                            textbutton "Disabled" action SetVariable("persistent.mod_winter_bgs", True) selected persistent.mod_winter_bgs


        elif m_current_tab == "cheats":
            text "Cheats" style "mod_home_title"


            vbox:
                style_prefix "mod_settingsCheats"
                align (0.52, 0.5)
                spacing 24
                textbutton "- Set money to $9,999" action ui.callsinnewcontext("lain_cheat_money") text_idle_color "#fff" text_size 30
                textbutton "- Unlock all secret cards" action ui.callsinnewcontext("lain_cheat_secretcards") text_idle_color "#fff" text_size 30
                textbutton "- Unlock all gallery scenes" action ui.callsinnewcontext("lain_cheat_scenegallery") text_idle_color "#fff" text_size 30

        elif m_current_tab is not None:
            vbox:
                align (0.03, 0.08)
                anchor (0.0, 0.0)
                for i in m_current_tab:
                    textbutton i[0] selected m_column2_name == i[0] text_style "mod_column1_textbutton" action [SetScreenVariable("m_column2", getattr(store, i[1])), SetScreenVariable("m_column2_name", i[0])]

            if m_column2 is not None:
                text m_column2_name align (0.0, 0.078) style "mod_column2_header" xoffset 318
                vbox:
                    pos (305, 99)
                    anchor (0.0, 0.0)
                    spacing 0
                    for i in m_column2:
                        button:
                            xysize (495, 48)
                            idle_background "mod/images/column2_idle.png"
                            hover_background "mod/images/column2_hover.png"
                            text i[0] align (0.0, 0.5) style "mod_column2_textbutton"
                            action Show(i[1])

screen mod_notimplemented():

    tag notimplemented

    zorder 998

    style_prefix "modguide"
    drag:
        drag_name "mod_notimplemented"
        align (1.0, 0.5)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_notimplemented") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Not yet implemented" pos (27, 70) font "mod/OSB.ttf"