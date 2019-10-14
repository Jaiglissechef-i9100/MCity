













define config.name = _("Milfy City")





define gui.show_name = True




define config.version = "0.6b"





define gui.about = _("")






define build.name = "Milfy_City"
define config.console = False






define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "Milfy City"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)








    config.main_menu_music = "sfx/MenuMusic.mp3"
    build.documentation('*.html')
    build.documentation('*.txt')
    build.classify("game/**.rpyc", "scripts")
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("sfx", "all")
    build.archive("movies", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webm", "movies")
    build.classify("game/**.mp3", "sfx")
    build.classify("game/**.wav", "sfx")