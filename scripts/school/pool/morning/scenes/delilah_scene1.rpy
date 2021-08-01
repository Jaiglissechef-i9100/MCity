image delilah_scene1_p1 = "images/school/pool/morning/scenes/delilah_scene1/1.jpg"
image delilah_scene1_p2 = "images/school/pool/morning/scenes/delilah_scene1/2.jpg"
image delilah_scene1_p3 = "images/school/pool/morning/scenes/delilah_scene1/3.jpg"
image delilah_scene1_p4 = "images/school/pool/morning/scenes/delilah_scene1/4.jpg"
image delilah_scene1_p5 = "images/school/pool/morning/scenes/delilah_scene1/5.jpg"

label delilah_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if delilah_work_inprogress == True:
        $ can_hide_windows = False
        show screen pool_morning_notclickable
        $ renpy.show("workinprogress2", layer="screens",)
        " Available soon."
        $ renpy.hide("workinprogress2", layer="screens",)
        jump pool_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene delilah_scene1_p1 with dissolve
    $ can_hide_windows = True
    MC "…."
    MC "(Damn.. She’s hot..)"
    MC "(I didn't see her here before... Is she a new student?)"
    $ Delilah_name = "???"
    Delilah "How long are you gonna stare at me like that?"
    Delilah "You know that I can see your reflection in the water, right?"
    scene delilah_scene1_p2
    MC "Ah!? Haha.. Sorry.."
    Delilah "By the way, my name is Delilah."
    $ Delilah_name = "Delilah"
    Delilah "Are you interested in joining the swimming pool club?"
    Delilah "We certainly need someone to do the dirty work."
    MC "Dirty work?"
    Delilah "You know.. Keep this place VERY shiny."
    MC "Not really.. (I don’t want to be a cleaner!)"
    scene delilah_scene1_p3
    Delilah "Huh? No? After the incident with Celia?"
    Delilah "Work HERE could be very beneficial for you."
    scene delilah_scene1_p4
    Delilah "Just think about it... I'm a girl… I can, for sure, find someone perfect for you."
    MC "Perfect for me? (Does she have someone in mind?)"
    Delilah "Yes, perfect for you! Let me think… Hmm.. "
    Delilah "Probably some fatty and stupid girl will, for sure be desperate enough, to be interested in you. "
    Delilah "No offense - Of course! I’m only telling the truth."
    MC "(That bitch! She’s making fun of me!)"
    MC "…"
    scene delilah_scene1_p5
    Delilah "Well, if you change your mind, you know where to find me."
    $ delilah_work_inprogress = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pool_morning1

